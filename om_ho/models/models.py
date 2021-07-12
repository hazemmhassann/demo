# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class InheritPatient(models.Model):
    _inherit = 'sale.order'

    patient_name = fields.Char(string="Name")


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread.cc',
                'mail.activity.mixin']
    _description = 'Patients Records'
    _rec_name = "patient_name"

    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, '%s - %s' % (rec.name_seq, rec.patient_name)))
        return res

    patient_name = fields.Char(string="Name", required=True)
    active = fields.Boolean("Active", default=True)
    age_group = fields.Selection([('major', 'Major'), ('minor', 'Minor'), ], string="Age Group",
                                 compute='set_age_group')
    patient_age = fields.Integer(string="Age")
    patient_weight = fields.Integer(string="Weight")
    appointment_count = fields.Integer(string='Appointments', compute='get_appointment_count')
    # age_group = fields.Selection([('major', 'Major'), ('minor', 'Minor'), ], string="Age Group",
    #                              compute='set_age_group')

    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'other')], required=True,
                              default='male')
    notes = fields.Text(string="Notes")
    image = fields.Binary(string="Image")
    name_seq = fields.Char(string='Sequence', required=True, copy=False,
                           readonly=True, index=True, default='New')

    @api.constrains('patient_age')
    def check_age(self):
        for rec in self:
            if rec.patient_age <= 5:
                raise ValidationError("age is too small")

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or 'New'
        result = super(HospitalPatient, self).create(vals)
        return result

    @api.depends('patient_age')
    def set_age_group(self):
        for rec in self:
            if rec.patient_age < 18:
                rec.age_group = 'minor'
            else:
                rec.age_group = 'major'

    def open_patient_appointments(self):
        return {
            'name': 'Appointments',
            'domain': [('patient_id', '=', self.id)],
            'type': 'ir.actions.act_window',
            'res_model': 'hospital.appointment',
            'view_type': 'form',
            'view_id': False,
            'view_mode': 'tree,form',
        }

    def get_appointment_count(self):
        count = self.env['hospital.appointment'].search_count([('patient_id', '=', self.id)])
        self.appointment_count = count


# class om_ho(models.Model):
#     _name = 'om_ho.om_ho'
#     _description = 'om_ho.om_ho'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

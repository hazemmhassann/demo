from odoo import models, fields, api


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    @api.onchange('patient_id')
    def set_patient_gender(self):
        for rec in self:
            if rec.patient_id:
                rec.gender = rec.patient_id.gender

    name_seq = fields.Char(string='Sequence', required=True, copy=False,
                           readonly=True, index=True, default='New')
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    patient_age = fields.Integer(string='Age', required=True, related="patient_id.patient_age")
    appointment_lines = fields.One2many('hospital.appointment.lines', 'appointment_id', string='Appointment Lines')

    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'other')], required=True,
                              default='male')

    appointment_date = fields.Date(string='Date', required=True)
    notes = fields.Text(string="Registration Notes")
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Status', required=True, readonly=True, copy=False, tracking=True,
        default='draft')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or 'New'
        result = super(HospitalAppointment, self).create(vals)
        return result

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_done(self):
        for rec in self:
            rec.state = 'done'



    def delete_lines(self):
        for rec in self:
            rec.appointment_lines = [(5, 0, 0)]

class HospitalAppointmentlines(models.Model):
    _name = 'hospital.appointment.lines'
    _description = 'Appointment.lines'

    product_id = fields.Many2one('product.product', string='Medicine')
    product_qty = fields.Integer(string='Quantity')
    appointment_id = fields.Many2one('hospital.appointment', string='Sequence')

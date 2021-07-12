# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CreateAppointment(models.TransientModel):
    _name = 'create.appointment'

    patient_idd = fields.Many2one('hospital.patient', string="Patient")
    appointment_date = fields.Date(string="Appointment Date")

    def create_appointment(self):
        vals = {
            'patient_id': self.patient_idd.id,
            'appointment_date': self.appointment_date
        }
        self.patient_idd.message_post(body="Appointment Created", subject="Appointment Creation")
        self.env['hospital.appointment'].create(vals)

    def get_data(self):
        print("Get Data Function")
        appointments = self.env['hospital.appointment'].search([])
        print("appointments", appointments)
        for rec in appointments:
            print("App Name:", rec.gender)

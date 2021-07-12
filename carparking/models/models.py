# -*- coding: utf-8 -*-

from odoo import models, fields , api


class Car(models.Model):
    _name = "car.car"

    name = fields.Char(string='Name')
    horse_power = fields.Integer(string="Horse Power")
    door_number = fields.Integer(string="Door Number")
    driver_id = fields.Many2one('res.partner', string='Driver')
    parking_id = fields.Many2one('parking.parking', string='Parking')
    features_ids = fields.Many2many("car.features", string="Features")
    total_speed = fields.Integer(string="Total Speed", compute="get_total_speed")
   # random_message = fields.Char(string="RandomMessage", compute="say_hello")
    status = fields.Selection([('new', 'New'), ('used', 'Used'), ('sold', 'Sold')], string='Status', default='new')
    car_sequence=fields.Char(string='Sequence')

    #def say_hello(self):
      #  self.random_message = 'hello' + self.driver_id.name

    def get_total_speed(self):
        self.total_speed = self.horse_power * 50

    def set_car_to_used(self):
        self.status = "used"

    def set_car_to_sold(self):
        self.status = "sold"

    @api.model
    def create(self, vals):
        vals['car_sequence']=self.env['ir.sequence'].next_by_code('car.sequence')
        result = super(Car, self).create(vals)
        return result


class Parking(models.Model):
    _name = "parking.parking"

    name = fields.Char(string='Name')
    car_ids = fields.One2many('car.car', 'parking_id', string='Cars')


class CarFeatures(models.Model):
    _name = "car.features"

    name = fields.Char(string='Name')

# class carparking(models.Model):
#     _name = 'carparking.carparking'
#     _description = 'carparking.carparking'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

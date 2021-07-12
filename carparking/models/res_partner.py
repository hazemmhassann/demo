from odoo import models, fields, api


class Respart(models.Model):
    _inherit = "res.partner"

    message=fields.Char(string='Custom Message')
    other_information=fields.Char(string='Other information')

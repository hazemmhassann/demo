# -*- coding: utf-8 -*-
# from odoo import http


# class OmHo(http.Controller):
#     @http.route('/om_ho/om_ho/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/om_ho/om_ho/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('om_ho.listing', {
#             'root': '/om_ho/om_ho',
#             'objects': http.request.env['om_ho.om_ho'].search([]),
#         })

#     @http.route('/om_ho/om_ho/objects/<model("om_ho.om_ho"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('om_ho.object', {
#             'object': obj
#         })

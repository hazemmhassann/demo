# -*- coding: utf-8 -*-
# from odoo import http


# class Carparking(http.Controller):
#     @http.route('/carparking/carparking/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/carparking/carparking/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('carparking.listing', {
#             'root': '/carparking/carparking',
#             'objects': http.request.env['carparking.carparking'].search([]),
#         })

#     @http.route('/carparking/carparking/objects/<model("carparking.carparking"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('carparking.object', {
#             'object': obj
#         })

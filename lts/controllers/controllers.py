# -*- coding: utf-8 -*-
# from odoo import http


# class Lts(http.Controller):
#     @http.route('/lts/lts/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lts/lts/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lts.listing', {
#             'root': '/lts/lts',
#             'objects': http.request.env['lts.lts'].search([]),
#         })

#     @http.route('/lts/lts/objects/<model("lts.lts"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lts.object', {
#             'object': obj
#         })

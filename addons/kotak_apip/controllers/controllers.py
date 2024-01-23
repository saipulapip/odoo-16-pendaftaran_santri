# -*- coding: utf-8 -*-
# from odoo import http


# class KotakApip(http.Controller):
#     @http.route('/kotak_apip/kotak_apip', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kotak_apip/kotak_apip/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('kotak_apip.listing', {
#             'root': '/kotak_apip/kotak_apip',
#             'objects': http.request.env['kotak_apip.kotak_apip'].search([]),
#         })

#     @http.route('/kotak_apip/kotak_apip/objects/<model("kotak_apip.kotak_apip"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kotak_apip.object', {
#             'object': obj
#         })

# -*- coding: utf-8 -*-
# from odoo import http


# class PendaftaranSantri(http.Controller):
#     @http.route('/pendaftaran_santri/pendaftaran_santri', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pendaftaran_santri/pendaftaran_santri/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pendaftaran_santri.listing', {
#             'root': '/pendaftaran_santri/pendaftaran_santri',
#             'objects': http.request.env['pendaftaran_santri.pendaftaran_santri'].search([]),
#         })

#     @http.route('/pendaftaran_santri/pendaftaran_santri/objects/<model("pendaftaran_santri.pendaftaran_santri"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pendaftaran_santri.object', {
#             'object': obj
#         })

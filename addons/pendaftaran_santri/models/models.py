# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class pendaftaran_santri(models.Model):
#     _name = 'pendaftaran_santri.pendaftaran_santri'
#     _description = 'pendaftaran_santri.pendaftaran_santri'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields, api

class KotakApip(models.Model):
	_name    ='cep.kotak.apip'
	_description  ='cep.kotak.apip'

	name        = fields.Char(string='Nama', required=True)
	description = fields.Text(string='Masukan Kritik/Saran')
	user_id = fields.Many2one(comodel_name='res.users',string='Penanggung Jawab')
	
	   
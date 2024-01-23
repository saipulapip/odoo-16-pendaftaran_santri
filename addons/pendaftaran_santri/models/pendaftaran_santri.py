from odoo import models, fields, api

class PendaftaranSantri(models.Model):
	_name           = 'pendaftaran.santri'
	_description    = 'pendaftaran.santri'

	name        = fields.Char(string='Nama Santri', required=True)
	tempat_tgl_lahir = fields.Char(string='Tempat Tgl Lahir', required=True)
	tempat_tgl_lahir2 = fields.Char(string='Tempat Tgl Lahir', required=True)
	description = fields.Text(string='Orang Tua')
	user_id = fields.Many2one(comodel_name='res.users',string='Nama Orang Tua')
	jenis_kel = fields.Char(string='Jenis Kel', required=True)
	alamat = fields.Char(string='Alamat Tinggal', required=True)
	nama_ortu = fields.Char(string='Nama Orang Tua', required=True)
	pekerjaan = fields.Char(string='Pekerjaan', required=True)
	mobile = fields.Char(string='No Hp', required=True)
	infaq = fields.Char(string='Infaq Bulanan', required=True)
	state = fields.Selection(string='Status', selection=[('draft', 'Draft'), ('confirm', 'Sedang Berlangsung'),('done', 'Selesai'),],default='draft', tracking=True)

	def action_confirm(self):
				self.state='confirm'
				
	def action_done(self):
				self.state='done'

	def action_draft(self):
				self.state='draft'	
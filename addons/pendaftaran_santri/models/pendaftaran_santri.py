from odoo import models, fields, api

class PendaftaranSantri(models.Model):
	_name           = 'pendaftaran.santri'
	_description    = 'pendaftaran.santri'

	name        = fields.Char(string='Nama Santri',  compute='_compute_name',)
	jenis_kel = fields.Selection(string='Jenis Kelamin', selection=[('L', 'Laki-Laki'), ('P', 'Perempuan'),])
	tempat_lahir = fields.Char(string='Tempat Lahir',)
	tgl_lahir = fields.Date(string='Tanggal Lahir')
	nik = fields.Char(string='No NIK')
	nik_kk = fields.Char(string='No KK (Kartu Keluarga)')
	Saudara = fields.Char(string='Anak Ke')
	dari = fields.Char(string='Dari berapa saudara')
	Alamat = fields.Char(string='Alamat Tinggal')
	ibu = fields.Char(string='Nama Ibu Kandung')
	pekerjan1 = fields.Char(string='Pekerjaan')
	tlpn_ibu = fields.Char(string='No Telpon Ibu')
	ayah = fields.Char(string='Nama Ayah Kandung')
	pekerjan2 = fields.Char(string='Pekerjaan')
	tlpn_ayah = fields.Char(string='No Telpon Ayah')
	sekolah = fields.Char(string='Sekolah Asal')
	dituju = fields.Char(string='Pendidikan Dituju')
	image_1920 = fields.Binary(string='Foto Santri')
	state = fields.Selection(string='Status', selection=[('draft', 'Draft'), ('confirm', 'Sedang Berlangsung'),('done', 'Selesai'),],default='draft', tracking=True)

	@api.depends('create_uid')
	def _compute_name(self):
			for record in self:
				record.name = record.create_uid.name

			
	def action_confirm(self):
				self.state='confirm'
				
	def action_done(self):
				self.state='done'

	def action_draft(self):
				self.state='draft'	

	@api.constrains('nik')
	def _check_nik(self):
		for record in self:
			if record.nik and not record.nik.isdigit():
				raise models.ValidationError(' "NIK"nya gak boleh pakai angka tauu!!!')
			
	@api.constrains('nik_kk')
	def _check_nik_kk(self):
		for record in self:
			if record.nik_kk and not record.nik_kk.isdigit():
				raise models.ValidationError(' "NIK KK"nya gak boleh pakai angka tauu!!!')		
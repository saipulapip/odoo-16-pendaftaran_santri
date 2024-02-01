# -*- coding: utf-8 -*-
{
	'name': "pendaftaran_santri",

	'summary': """
	   Pendaftaran Santri Baru""",

	'description': """
		Menerima Pendaftaran Santri Baru yaitu: Aplikasi Pendaftaran Santri Baru
	""",

	'author': "PP Darussa'adah",
	'website': "https://www.Darsah.com",

	# Categories can be used to filter modules in modules listing
	# Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
	# for the full list
	'category': 'Uncategorized',
	'version': '16.0.1',

	# any module necessary for this one to work correctly
	'depends': ['base'],

	# always loaded
	'data': [
        'security/groups.xml',
		'security/ir.model.access.csv',
		'views/menu_pendaftaran.xml',
		'views/pendaftaran_santri.xml',
		'views/pengajar.xml',
	],
	# only loaded in demonstration mode
	'demo': [
		# 'demo/demo.xml',
	],
}

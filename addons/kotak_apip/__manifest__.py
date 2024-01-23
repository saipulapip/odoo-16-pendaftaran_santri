# -*- coding: utf-8 -*-
{
	'name': "Kotak_apip",

	'summary': """
		Kotak Apip""",
		

	'description': """
		Membuat Aplikasi Kotak Saran untuk menerima saran yaitu: Aplikasi Kotak Apip
	""",

	'author': "PT catur Elang Perkasa",
	'website': "https://www.caturelang.com",

	# Categories can be used to filter modules in modules listing
	# Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
	# for the full list
	'category': 'Uncategorized',
	'version': '16.0.1',

	# any module necessary for this one to work correctly
	'depends': ['base'],

	# always loaded
	'data': [
        'security/kotak_security.xml',
		'security/ir.model.access.csv',
		# 'views/views.es.xml',
		'views/menu_kotak_apip.xml',
		'views/kotak_apip.xml',
		# 'views/templatip.xml',
	],
	# only loaded in demonstration mode
	'demo': [
		 'demo/demo.xml',
	],
}

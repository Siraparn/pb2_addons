# -*- coding: utf-8 -*-
{
    'name': 'NSTDA :: Accounting Reports',
    'version': '8.0.1.0.0',
    'category': 'Accounting & Finance',
    'description': """
""",
    'author': 'Kitti U.',
    'website': 'http://ecosoft.co.th',
    'depends': [
        'payment_export',
        'pabi_utils',
    ],
    'data': [
        'data/menu.xml',
        'xlsx_template/templates.xml',
        'xlsx_template/load_template.xml',
        'reports/xlsx_report_cheque_register.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}

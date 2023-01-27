# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """
        Course Management system""",

    'description': """
        This an odoo app, going through the odoo building module tutorial.
The app is ment to be a tool to practice odoo concepts.

The app is totaly hypothetical and only useful for learning
    """,

    'author': "Humphrey Mugambi",
    'website': "https://synt.ax/",
    'maintainer': "Syntax LTD",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/partner.xml',
        'views/reports.xml',
        'views/session_board.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

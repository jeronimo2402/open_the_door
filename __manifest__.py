# -*- coding: utf-8 -*-
{
    'name': "open_the_door",

    'summary': """
        Modulo para administración de entrada de usuarios
    """,

    'description': """
        Modulo que permite ingresar y administrar los usuarios que van a ingresar con reconocimiento facial
        o tarjetas RFID a Pragmatic
    """,

    'author': "Open The Door",
    'website': "https://www.open_the_door.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/visit.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

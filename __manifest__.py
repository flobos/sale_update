# -*- coding: utf-8 -*-
{
    'name': "sale_update",

    'summary': """
        Modifica el formulario de venta , agrega % de margen""",

    'description': """
        Modifica el formulario de venta , agrega % de margen
    """,

    'author': "Fimar",
    'website': "http://www.fimarcorp.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
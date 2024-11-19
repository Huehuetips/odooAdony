# -*- coding: utf-8 -*-
{
    'name': "tracking_guides",

    'summary': "Aplicación para las guías de transporte",

    'description': """
Módulo para la gestión de guías de transporte de Guatex, forza y cropa.
Generación de guías, seguimiento y consulta de guías.
    """,

    'author': "DISSA - AD",
    'website': "https://emontejodev.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}


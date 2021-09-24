# -*- coding: utf-8 -*-
{
    'name': "Registro/Control de Correspondencias",

    'summary': """
        Registro y control de correspondencias de la CMAP
    """,
    'description': """
        Desarrollado con la finalidad de poder llevar el registro y control
        de todas las correspondencias fisicas que se manejan en la Contraloria
        del Municipio "Ambrosio Plaza"
    """,

    'author': "[CMAP], Josue Alfaro(josuealfarocmap@gmail.com)",
    'website': "https://www.contraloriaplaza.org.ve/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/oficio_enviado_views.xml',
        'views/oficio_recibido_views.xml',
        'views/partner_views.xml',
        'views/department_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

# -*- coding: utf-8 -*-
{
    'name': "custom_module",

    'summary': "Inject a custom statusbar button into Sale Orders",

    'description': """
Customized Sale module.
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales/Sales',
    'version': '1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        'views/sale_order_form.xml',
        'security/ir.model.access.csv',
        './views/sale_order_inherit.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    "installable": True,
    "application": False,
    "auto_install": False,
}


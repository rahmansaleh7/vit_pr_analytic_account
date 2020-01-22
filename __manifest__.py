# -*- coding: utf-8 -*-
{
    'name': "vit_pr_analytic_account",

    'summary': """
        Menambahkan Analytic Account di Product Request""",

    'description': """
        Analytic Account
    """,

    'author': "Iqbal Abdurrahman",
    'website': "http://www.vitraining.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
                'base',
                'vit_product_request',
                'hr',
                'purchase',
                'analytic',
                'vit_budget',
                'stock',
                ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
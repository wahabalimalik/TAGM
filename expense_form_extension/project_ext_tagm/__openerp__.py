# -*- coding: utf-8 -*-
{
    'name': "project_ext_tagm",

    'summary': """
        Project Extension Module in Project Managment.""",

    'description': """
        Project Extension Module in Project Managment.
    """,

    'author': "business cube",
    'website': "http://www.bcube.pk",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','project','hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
}
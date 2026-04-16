{
    'name': 'Odoo 19 Test Module',
    'version': '1.0',
    'category': 'Uncategorized',
    'summary': 'Module for testing purposes in Odoo 19',
    'description': """
        This is a boilerplate module for doing tests in Odoo 19.
    """,
    'author': 'Deisy',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/test_view.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}

# __manifest__.py

{
    'name': 'Blank Template Module',
    'version': '1.0.0',
    'category': 'Tools',
    'author': 'Your Name',
    'website': 'http://yourwebsite.com',
    'license': 'LGPL-3',
    'summary': 'A template module to quickly create Odoo modules, models, and views.',
    'depends': ['base'],  # Base dependency, add more as needed
    "data": [
        "views/blank_template_model_views.xml",
        "views/menu.xml",
        "security/ir.model.access.csv",
    ],
    'installable': True,
    'application': False,  # Set to True if this is an application module
    'auto_install': False,  # Automatically install dependent modules if set to True
    'sequence': 10,  # Define module installation sequence
    'description': """
        A blank template module to help developers quickly generate new Odoo modules.
        Includes a basic model and a view.
    """,
    'external_dependencies': {
        'python': [],
        'bin': [],
    },
}
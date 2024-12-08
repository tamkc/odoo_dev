# __manifest__.py

{
    'name': 'Document Gen Module',
    'version': '1.0.0',
    'category': 'Tools',
    'author': 'Your Name',
    'website': 'http://yourwebsite.com',
    'license': 'LGPL-3',
    'summary': 'A module to generate documents in various formats.',
    'depends': ['base'],  # Base dependency, add more as needed
    "data": [
        "security/ir.model.access.csv",
        "views/docgen_generator_views.xml",
        "views/menu.xml",
    ],
    'installable': True,
    'application': True,  # Set to True if this is an application module
    'auto_install': False,  # Automatically install dependent modules if set to True
    'sequence': 10,  # Define module installation sequence
    'description': """
        Document Generator Module
        =========================
        This module allows users to generate documents such as invoices,
        in different formats like PDF and Excel.
    """,
    'external_dependencies': {
        'python': [],
        'bin': [],
    },
}

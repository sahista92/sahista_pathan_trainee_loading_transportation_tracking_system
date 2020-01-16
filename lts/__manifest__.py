{
    'name': "LTS",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",


    'category': 'Uncategorized',
    'version': '0.1',


    'depends': ['website'],


    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/order.xml',
        'views/inquirey.xml',
        'views/transporter.xml',
        'views/wizard.xml',
        'views/report.xml', 
        'views/templates.xml'
    ],
    'demo': [

    ],
}

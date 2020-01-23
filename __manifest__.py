{
    'name': "LTS",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'version': '0.1',


    'depends': ['web_dashboard'],


    'data': [
        'security/ir.model.access.csv',
        'views/transporter.xml',
        'views/reports.xml'
    ],
    'demo': [
            'demo/demo.xml'
    ],
}

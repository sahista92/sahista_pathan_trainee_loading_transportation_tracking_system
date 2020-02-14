{
    'name': "LTS",

    'summary': """
        Loading Transportation System """,

    'version': '1.0',


    'depends': ['base', 'web_dashboard', 'portal'],


    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/LTS.xml',
        'views/reports.xml',
        'views/template.xml'

    ],
    'demo': [
         'demo/demo.xml',
    ],
}

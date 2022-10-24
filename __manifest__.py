{
    'name': 'Laboratorio',
    "description": "Laboratorios1",

    'depends': [
        'base',
        'hr',
        'hr_employee_relative',
        'hr_public_security',
        'oh_employee_documents_expiry',
        'history_employee_moves',
        'feature_location',

    ],


    "data": [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/view.xml',
        'report/empleas_report.xml',
        'report/custodia_report.xml',
        'report/etiqueta_report.xml',
        'report/final_report.xml',
        #'report/antido_report1.xml',
        #'report/antido_report2.xml',
        #'report/report.xml'
        ]

}

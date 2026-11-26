{
    'name': 'Biblioteca',
    'version': '19.0.1.0.0',
    'summary': 'Catálogo de libros',
    'author': 'Mario Payuela',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/tema_data.xml',
        'views/libro_views.xml',
        'views/tema_views.xml',
    ],

    'application': True,
}
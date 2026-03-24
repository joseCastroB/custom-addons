{
    'name': 'Opermaq Ventas',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Personalizaciones de Opermaq para el módulo de Ventas y Facturación',
    'description': """
        Este módulo agrega campos personalizados en las cotizaciones y pedidos de venta:
        - Enlace manual a la Factura (account.move)
        - Espejo del estado de la factura nativo
    """,
    'author': 'Jose Castro',
    'depends': [
        'base', 
        'sale_management', 
        'account'
    ],
    'data': [
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
{
    'name': 'Textile B2B Custom Addon',
    'version': '1.0',
    'summary': 'Custom functionalities for Textile B2B E-Commerce',
    'description': """
        Custom addon to handle multi-currency based on user location,
        enhanced product import with image handling, and product recommendations.
    """,
    'author': 'Your Name',
    'depends': ['base', 'website', 'sale', 'product', 'stock', 'website_sale', 'delivery'],
    'data': [
        'views/templates.xml',
        'views/product_import_view.xml',
        'security/ir.model.access.csv',
        'data/recommendation_cron.xml',
    ],
    'installable': True,
    'application': True,
}

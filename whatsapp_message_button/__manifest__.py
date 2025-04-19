{
    'name': 'WhatsApp Message Button',
    'version': '1.0',
    'summary': 'Send WhatsApp messages from Sale Order, Invoice, and Customers',
    'description': 'Open WhatsApp Web with pre-filled message for the contact number.',
    'category': 'Tools',
    'author': 'Murali',
    'price': 29,
    'depends': ['sale', 'account'],
    'data': [
        'views/sale_order_view.xml',
        'views/account_move_view.xml',
        'views/res_partner_view.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'OPL-1',
}

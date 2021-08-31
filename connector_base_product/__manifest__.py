# © 2014 David BEAL Akretion, Sodexis
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html)

{'name': 'Connector Base Product',
 'version': '11.0.1.0.0',
 'author': "Openerp Connector Core Editors, Odoo Community Association (OCA)",
 'website': 'http://odoo-connector.com',
 'license': 'LGPL-3',
 'category': 'Connector',
 'description': """
Connector Base Product
======================

Add 'Connector' tab to product view
""",
 'depends': [
     'connector',
     'product',
 ],
 'data': [
     'views/product_view.xml'
 ],
 'installable': True,
 }

from odoo import models, fields

class Product(models.Model):
    _inherit = 'product.product'
    apartment=fields.One2many('realtor.apartment', 'product_id',
    string="appartr")
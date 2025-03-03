from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    is_a_buyer=fields.Boolean('is a buyer', default=False)

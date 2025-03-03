from odoo import models, fields, api
from odoo.exceptions import ValidationError

# pour que les acheteur puissent proposer une offre 
class Offer(models.Model): 
    _name = 'realtor.offer'
    _description = 'Offer for Apartment'

    apartment_id = fields.Many2one('realtor.apartment', string="Apartment", required=True)
    buyer_id = fields.Many2one('res.partner', string="Buyer")
    offer_price = fields.Float(string="Offer Price", required=True)

    @api.constrains('offer_price')
    def _check_offer_price(self):
            for record in self:
                if record.offer_price <= 0: 
                    raise ValidationError("The offer price must be greater than zero.")
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta

class Apartment(models.Model): #models.MOdel sert a lier le model a la base de donner d'odoo
    _name = 'realtor.apartment'
    _description = 'Apartment'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    photo = fields.Binary(string='Photo')

    creation_date = fields.Datetime(string='Creation Date', default=fields.Datetime.now)
    availability_date = fields.Datetime(
        string='Availability Date',
        required=True,
        default=lambda self: datetime.now() + timedelta(days=90)
    )
    product_id = fields.Many2one('product.product', string="Product", required=True)

    expected_price = fields.Float(string='Expected Price', required=True)
    surface = fields.Float(string='Surface (m²)', required=True)
    terrace_surface = fields.Float(string='Terrace Surface (m²)', default=0.0)
    total_surface = fields.Float(string='Total Surface (m²)', compute='_compute_total_surface', store=True)

    # Meilleure offre 
    best_offer = fields.Float(string='Best Offer', compute='_compute_best_offer', store=True)
    # il idéntifie l'achteur ayant la meilleure offre 
    # Many2one prcque plusieurs appartement peuvent être liés à un seul acheteur 
    # si j'avais One2one alors un acheteur ne pouvait pas avoir la meilleure offre pour pls appartments 
    
    buyer_id = fields.Many2one('res.partner',
     string="Buyer with Best Offer",
     compute='_compute_best_offer',
     store=True,
     domain=[('is_a_buyer', '=', True)])#le filtre est pour reconnaitre si cest un vendeur ou un acheteur 

    offer_ids = fields.One2many('realtor.offer', 'apartment_id', string="Offers")
    # Stock fields
    
    # stock_quantity = fields.Float(string="Stock Quantity", default=0.0)
    stock_quantity = fields.Float(string="Stock Quantity", compute="_compute_stock_quantity", store=True)
    location_id = fields.Many2one('stock.location', string="Stock Location")
    
    _sql_constraints = [#definie dans la base de donnee
        ('unique_name', 'unique(name)', "The name must be unique. Another apartment already has this name."),
    ]
    
    
    @api.constrains('availability_date')#au niveau du code 
    def _check_availability_date(self):
        for record in self:
            if record.availability_date < (record.creation_date + timedelta(days=90)):
                raise ValidationError("The dat must be in 90 days")

    @api.constrains('expected_price', 'surface', 'terrace_surface', 'best_offer')
    def _check_values(self):
        for record in self:
            if record.expected_price <= 0:
                raise ValidationError("The expected price must be greater than zero.")
            if record.surface <= 0:
                raise ValidationError("The surface must be greater than zero.")
            if record.terrace_surface < 0:
                raise ValidationError("The terrace surface must be positive.")
            if record.best_offer and record.best_offer < record.expected_price * 0.9:
                raise ValidationError("The best offer must be at least 90% of the expected price.")

    @api.depends('surface', 'terrace_surface')
    def _compute_total_surface(self):
        for record in self:
            record.total_surface = record.surface + record.terrace_surface

    @api.depends('offer_ids')
    def _compute_best_offer(self):
        for record in self:
            if record.offer_ids:
                best_offer = max(record.offer_ids, key=lambda offer: offer.offer_price)
                record.best_offer = best_offer.offer_price
                record.buyer_id = best_offer.buyer_id.id
            else:
                record.best_offer = 0.0
                record.buyer_id = False
                
    @api.depends('product_id')
    def _compute_stock_quantity(self):
        for record in self:
            if record.product_id:
                record.stock_quantity = record.product_id.qty_available
            else:
                record.stock_quantity = 0.0


# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    partner_id = fields.Many2one(
        'res.partner', string='Vendor', required=True, 
        change_default=True, 
        tracking=True, domain="['|',('supplier_rank','>', 0),('is_supplier','=',True)]", help="You can find a vendor by its Name, TIN, Email or Internal Reference.")
    
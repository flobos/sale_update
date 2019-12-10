from odoo import models, fields, api

class sale_update_sale_order_line(models.Model):

    _inherit = 'sale.order'
    margen_porcentaje_venta = fields.Float(string="Margen venta(%)", readonly=True, store=True,
                                           compute='_calcular_margen_venta')

    @api.multi
    @api.depends('amount_untaxed')
    def _calcular_margen_venta(self):
        for rec in self:
            magen = 0
            if rec.amount_untaxed != 0:
                margen = (rec.margin / rec.amount_untaxed) * 100
                rec.margen_porcentaje_venta = margen

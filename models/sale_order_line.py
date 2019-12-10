from odoo import models, fields, api

class sale_update_sale_order_line(models.Model):

    _inherit = 'sale.order.line'
    marge_porcentaje = fields.Float(string="Margen (%)", readonly=True, store=True, compute='_calcular_margen')

    @api.multi
    @api.depends('product_id','price_unit')
    def _calcular_margen(self):
        for rec in self:
            magen = 0
            if rec.price_unit != 0:
                margen = ((rec.price_unit - rec.purchase_price) / rec.price_unit) * 100
                rec.marge_porcentaje = margen




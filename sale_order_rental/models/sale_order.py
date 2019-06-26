# Copyright 2019 Oihana Larrañaga - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    start_date = fields.Date(
        string='Start date')
    end_date = fields.Date(
        string='End date')
    rental_days = fields.Integer(
        string='Rental days')

    @api.onchange('start_date', 'end_date')
    def onchange_dates(self):
        if self.start_date and self.end_date:
            self.rental_days = abs(self.end_date - self.start_date).days + 1

    @api.multi
    def _action_confirm(self):
        res = super(SaleOrder, self)._action_confirm()
        for sale in self:
            for picking in sale.picking_ids:
                scheduled = "{} 08:00:00".format(sale.start_date)
                for picking_move in picking.move_ids_without_package:
                    picking_move.write(
                        {'start_date': picking_move.sale_line_id.start_date,
                        'end_date': picking_move.sale_line_id.end_date,
                        'date_expected': picking_move.sale_line_id.start_date,
                        })
                picking.write({'start_date': return min(move_ids_without_package
                                            , key=lambda x: x.start_date),
                               'end_date': sale.end_date,
                               
                               })
        return res


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    start_date = fields.Date(
        string='Start date')
    end_date = fields.Date(
        string='End date')
    rental_days = fields.Integer(
        string='Rental days')

    @api.onchange('start_date', 'end_date')
    def onchange_dates(self):
        if self.start_date and self.end_date:
            self.rental_days = abs(self.end_date - self.start_date).days + 1

    @api.multi
    @api.onchange('product_id')
    def product_id_change(self):
        result = super(SaleOrderLine, self).product_id_change()
        if self.order_id.start_date:
            self.start_date = self.order_id.start_date
        if self.order_id.end_date:
            self.end_date = self.order_id.end_date
        return result

    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id',
                 'rental_days')
    def _compute_amount(self):
        result = super(SaleOrderLine, self)._compute_amount()
        for line in self:
            line.price_subtotal = line.price_subtotal * line.rental_days
        return result

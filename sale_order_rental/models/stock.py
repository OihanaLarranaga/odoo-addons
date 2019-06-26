# Copyright 2019 Oihana Larrañaga - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    start_date = fields.Date(
        string='Start date')
    end_date = fields.Date(
        string='End date')

    @api.one
    @api.depends('start_date')
    def _compute_scheduled_date(self):
        result = super(StockPicking, self)._compute_scheduled_date()
        if self.start_date:
            scheduled = "{} 08:00:00".format(self.start_date)
            self.scheduled_date = scheduled
        return result


class StockMove(models.Model):
    _inherit = 'stock.move'

    start_date = fields.Date(
        string='Start date')
    end_date = fields.Date(
        string='End date')

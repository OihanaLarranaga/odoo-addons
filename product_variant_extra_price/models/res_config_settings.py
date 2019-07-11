# -*- coding: utf-8 -*-
# Copyright 2017 Alfredo de la Fuente - AvanzOSC
# Copyright 2019 Alejandro Nieto - Okatent
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    number_price_field = fields.Selection(
        selection=[('2', '2'), ('3', '3'), ('4', '4')],
        config_parameter='product_variant_extra_price.number_price_field',
        string='Prices in products')

# -*- coding: utf-8 -*-
# Copyright 2017 Alfredo de la Fuente - AvanzOSC
# Copyright 2019 Alejandro Nieto - Okatent
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Product Variant Extra Prices",
    "version": "12.0.1.0.0",
    "license": "AGPL-3",
    "author": "AvanzOSC, "
              "Okatent",
    "website": "http://www.avanzosc.es, "
               "https://www.okatent.com",
    "contributors": [
        "Ana Juaristi <anajuaristi@avanzosc.es>",
        "Alfredo de la Fuente <alfredodelafuente@avanzosc.es>",
        "Gotzon Imaz <gotzonimaz@avanzosc.es>",
        "Alejandro Nieto <alex.nieto0027@gmail.com>",
    ],
    "category": "Product Management",
    "depends": [
        "product",
    ],
    "data": [
        # "data/product_variant_extra_prices_data.xml",      NO FUNCIONA ?¿ FALTA MIGRAR
        "views/product_product_view.xml",
        "views/res_config_setting_view.xml",
    ],
    "installable": True,
}

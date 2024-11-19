# -*- coding: utf-8 -*-

from odoo import models, fields


class history_guide(models.Model):
    _name = 'tracking_guides.history_guide'
    _description = 'tracking_guides.history_guide'

    name_recip = fields.Char(string="Destinatario")
    phone_number = fields.Char(string="Número de teléfono")
    address = fields.Text(string="Dirección de entrega")
    description = fields.Text("Descripción de entrega")
    shipping_details = fields.Text()


class shipping_details(models.Model):
    _name = 'tracking_guides.shipping_details'
    _description = 'tracking_guides.shipping_details'
    
    selection_shipping_type = [
        ('sobre', '1'),
        ('caja', '2'),
    ]
    pieces = fields.Integer(string="Cantidad de piezas")
    shipping_type = fields.Selection(selection_shipping_type, string="Tipo de envío")
    weight = fields.Float(string="Peso")
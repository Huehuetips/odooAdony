# -*- coding: utf-8 -*-

from odoo import models, fields


class history_guide(models.Model):
    _name = 'tracking_guides.history_guide'
    _description = 'tracking_guides.history_guide'

    name_recip = fields.Char(string="Destinatario")
    phone_number = fields.Char(string="Número de teléfono")
    address = fields.Text(string="Dirección de entrega")
    description = fields.Text("Descripción de entrega")
    shipping_details_ids = fields.One2many('tracking_guides.shipping_details', 'history_guide_id', string="Detalles de Envío")


class shipping_details(models.Model):
    _name = 'tracking_guides.shipping_details'
    _description = 'tracking_guides.shipping_details'
    
    history_guide_id = fields.Many2one('tracking_guides.history_guide', string="Guía de Historia")
    selection_shipping_type = [
        ('1', 'Sobre'),
        ('2', 'Caja'),
    ]
    pieces = fields.Integer(string="Cantidad de piezas")
    shipping_type = fields.Selection(selection_shipping_type, string="Tipo de envío")
    weight = fields.Float(string="Peso")
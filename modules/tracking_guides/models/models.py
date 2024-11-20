# -*- coding: utf-8 -*-

from odoo import models, fields, api


class history_guide(models.Model):
    _name = 'tracking_guides.history_guide'
    _description = 'tracking_guides.history_guide'

    name_recip = fields.Char(string="Destinatario")
    phone_number = fields.Char(string="Número de teléfono")
    address = fields.Text(string="Dirección de entrega")
    description = fields.Text("Descripción de entrega")
    shipping_details_ids = fields.One2many('tracking_guides.shipping_details', 'history_guide_id', string="Detalles de Envío")

    def call_api_and_save(self):
        # Realiza la llamada a la API
        api_response = self.call_api()  # Implementa tu lógica para la llamada a la API

        if api_response.get('success'):  # Verifica si la llamada fue exitosa
            self.create()  # Guarda el registro si la llamada fue exitosa
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'tracking_guides.history_guide',
                'view_mode': 'form',
                'res_id': self.id,
                'target': 'current',
            }
        else:
            # Manejo de errores, mostrar mensaje de error
            return {
                'warning': {
                    'title': ("Error"),
                    'message': ("La llamada a la API falló."),
                }
            }

    def call_api(self):
        # Implementa la lógica para llamar a la API
        # Retorna un diccionario con el resultado
        return {'success': True}  # Ejemplo de respuesta

class shipping_details(models.Model):
    _name = 'tracking_guides.shipping_details'
    _description = 'tracking_guides.shipping_details'
    
    history_guide_id = fields.Many2one('tracking_guides.history_guide', string="Guía de Historia")
    selection_shipping_type = [
        ('1', 'Sobre'),
        ('2', 'Caja'),
    ]
    pieces = fields.Integer(string="Cantidad de piezas")
    shipping_type = fields.Selection(selection_shipping_type, string="Tipo de envío", default='2')
    weight = fields.Float(string="Peso (Lb)")
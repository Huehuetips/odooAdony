# -*- coding: utf-8 -*-

from odoo import models, fields, api
class history_guide(models.Model):
    _name = 'tracking_guide.history_guide'
    _description = 'tracking_guide.history_guide'

    name_recip = fields.Char(string="Destinatario", required=True)
    phone_number = fields.Char(string="Número de teléfono", required=True)
    address = fields.Text(string="Dirección de entrega", required=True)
    description = fields.Text("Descripción de entrega", required=True)
    no_guide = fields.Char(string="Número de guía", default="NW94000001", required=True)
    shipping_details_ids = fields.One2many('tracking_guide.shipping_details', 'history_guide_id', string="Detalles de Envío", required=True)

    def call_api_and_save(self):
        # Realizar la llamada a la API
        print("Contenido de self:", self)
        print("Propiedades y métodos de self:", dir(self))
        for record in self:
            print("Contenido de record: ", record.name_recip)
            print("Contenido de record: ", record.phone_number)
        api_response = self.call_api()  # Implementa tu lógica para la llamada a la API

        if api_response.get('success'):  # Verifica si la llamada fue exitosa
            vals = {
                'name_recip': self.name_recip,
                'phone_number': self.phone_number,
                'address': self.address,
                'description': self.description,
                'no_guide' : self.no_guide,
                'shipping_details_ids': [(6, 0, [detail.id for detail in self.shipping_details_ids])],
            }
            print("Datos: ", vals)
            self.create(vals)  # Guarda el registro si la llamada fue exitosa
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'tracking_guide.history_guide',
                'view_mode': 'form',
                'res_id': self.id,
                'target': 'current',
            }
        else:
            # Manejo de errores, mostrar mensaje de error
            return {
                'warning': {
                    'title': "Error",
                    'message': "La llamada a la API falló.",
                }
            }

    def call_api(self):
        # Implementa la lógica para llamar a la API
        # Retorna un diccionario con el resultado
        return {'success': True}  # Ejemplo de respuesta

class shipping_details(models.Model):
    _name = 'tracking_guide.shipping_details'
    _description = 'tracking_guide.shipping_details'
    
    selection_shipping_type = [
        ('1', 'Sobre'),
        ('2', 'Caja'),
    ]
    
    history_guide_id = fields.Many2one('tracking_guide.history_guide', string="Guía de Historia", required=True)
    shipping_type = fields.Selection(selection_shipping_type, string="Tipo de envío", default='2', required=True)
    pieces = fields.Integer(string="Cantidad de piezas", default="1", required=True)
    weight = fields.Float(string="Peso (Lb)", required=True)

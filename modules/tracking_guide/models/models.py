# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from .api_handler import ApiHandler  # Importa la clase ApiHandler

class HistoryGuide(models.Model):
    _name = 'tracking_guide.history_guide'
    _description = 'tracking_guide.history_guide'

    name_recip = fields.Char(string="Destinatario", required=True)
    phone_number = fields.Char(string="Número de teléfono", required=True)
    address = fields.Text(string="Dirección de entrega", required=True)
    description = fields.Text("Descripción de entrega", required=True)
    no_guide = fields.Char(string="Número de guía", required=True)
    code_muni = fields.Selection(municipality_codes , string="Municipalidad", required=True)
    municipality = fields.Char(string="Municipio", required=True)
    shipping_details_ids = fields.One2many('tracking_guide.shipping_details', 'history_guide_id', string="Detalles de Envío", required=True)

    send_request = False

    def call_api_and_save(self):
        for record in self:
            if not record.shipping_details_ids:
                raise ValidationError("Debe haber al menos un detalle de envío.")
            

            # Realizar la llamada a la API para enviar los datos
            api_response = ApiHandler.call_api(record)

            if api_response.get('success'):  # Verifica si la llamada fue exitosa
                vals = {
                    'name_recip': record.name_recip,
                    'phone_number': record.phone_number,
                    'address': record.address,
                    'description': record.description,
                    'no_guide': record.no_guide,
                    'shipping_details_ids': [(6, 0, record.shipping_details_ids.ids)],
                }
                record.write(vals)
                return {
                    'type': 'ir.actions.act_window',
                    'res_model': self._name,
                    'view_mode': 'tree,form',
                    'target': 'current',
                }
            else:
                raise ValidationError("La llamada a la API falló. Por favor, inténtelo de nuevo.")

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


class ConfirmWizard(models.TransientModel):
    _name = 'confirm.wizard'
    _description = 'Confirm Wizard'

    def confirm_action(self):
        active_id = self.env.context.get('active_id')
        record = self.env['tracking_guide.history_guide'].browse(active_id)
        record.call_api_and_save()
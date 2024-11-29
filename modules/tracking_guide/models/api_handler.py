import requests
from odoo.exceptions import ValidationError

class ApiHandler:
    @staticmethod
    def fetch_data_from_api(record):
        # Implementa la lógica para llamar a la API y obtener los datos
        url = "https://api.example.com/data"  # Reemplaza con la URL de tu API
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer YOUR_API_KEY'  # Reemplaza con tu clave de API si es necesario
        }
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            api_response = response.json()
            # Actualiza los campos del modelo con los datos obtenidos de la API
            record.description = api_response.get('description', '')
            # Actualiza otros campos según sea necesario
        else:
            raise ValidationError("La llamada a la API para obtener datos falló. Por favor, inténtelo de nuevo.")

    @staticmethod
    def call_api(record):
        # Implementa la lógica para llamar a la API
        url = "https://api.example.com/send"  # Reemplaza con la URL de tu API
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer YOUR_API_KEY'  # Reemplaza con tu clave de API si es necesario
        }
        data = {
            'name_recip': record.name_recip,
            'phone_number': record.phone_number,
            'address': record.address,
            'description': record.description,
            'no_guide': record.no_guide,
            'shipping_details_ids': [detail.id for detail in record.shipping_details_ids],
        }
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            return response.json()
        else:
            return {'success': False}

    @staticmethod
    def get_municipality_codes():
        # Implementa la lógica para llamar a la API y obtener los códigos de municipio
        url = "https://api.example.com/municipalities"  # Reemplaza con la URL de tu API
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer YOUR_API_KEY'  # Reemplaza con tu clave de API si es necesario
        }
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            api_response = response.json()
            municipality_codes = [(item['code'], item['name']) for item in api_response]
            return municipality_codes
        else:
            raise ValidationError("La llamada a la API para obtener los códigos de municipio falló. Por favor, inténtelo de nuevo.")
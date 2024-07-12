from odoo import models, fields, api
import requests


class ResCurrency(models.Model):
    _inherit = 'res.currency'

    @api.model
    def get_user_currency(self):
        user_ip = requests.get('https://api.ipify.org').text
        geo_info = requests.get(f'https://ipapi.co/{user_ip}/json/').json()
        currency_code = geo_info.get('currency', 'USD')
        currency = self.search([('name', '=', currency_code)], limit=1)
        return currency

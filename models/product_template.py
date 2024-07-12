from odoo import models, fields, api
import requests
from PIL import Image
from io import BytesIO
import base64


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    image_url = fields.Char(string="Image URL")
    brand_id = fields.Char(string="Brand")
    logo = fields.Binary(string="Logo")

    @api.model
    def create_product_from_excel(self, values):
        product = self.create({
            'name': values['name'],
            'list_price': values['price'],
            'type': 'product',
        })
        image_url = values.get('image_url')
        if image_url:
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                image = Image.open(BytesIO(image_response.content))
                buffer = BytesIO()
                image.save(buffer, format="PNG")
                image_str = base64.b64encode(buffer.getvalue())
                product.write({'image_1920': image_str})
        return product

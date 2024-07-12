from odoo import models, fields, api


class ProductRecommendation(models.Model):
    _name = 'product.recommendation'
    _description = 'Product Recommendation'

    product_id = fields.Many2one('product.product', required=True)
    recommendation_score = fields.Float()

    @api.model
    def update_recommendations(self):
        products = self.env['product.product'].search([])
        for product in products:
            sales = self.env['sale.order.line'].search([('product_id', '=', product.id)])
            score = sum(sale.product_uom_qty for sale in sales)
            recommendation = self.search([('product_id', '=', product.id)], limit=1)
            if recommendation:
                recommendation.recommendation_score = score
            else:
                self.create({
                    'product_id': product.id,
                    'recommendation_score': score
                })

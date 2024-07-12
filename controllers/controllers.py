# -*- coding: utf-8 -*-
# from odoo import http


# class TextileB2bCustom(http.Controller):
#     @http.route('/textile_b2b_custom/textile_b2b_custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/textile_b2b_custom/textile_b2b_custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('textile_b2b_custom.listing', {
#             'root': '/textile_b2b_custom/textile_b2b_custom',
#             'objects': http.request.env['textile_b2b_custom.textile_b2b_custom'].search([]),
#         })

#     @http.route('/textile_b2b_custom/textile_b2b_custom/objects/<model("textile_b2b_custom.textile_b2b_custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('textile_b2b_custom.object', {
#             'object': obj
#         })


# -*- coding: utf-8 -*-
# from odoo import http


# class TrackingGuide(http.Controller):
#     @http.route('/tracking_guide/tracking_guide', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tracking_guide/tracking_guide/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tracking_guide.listing', {
#             'root': '/tracking_guide/tracking_guide',
#             'objects': http.request.env['tracking_guide.tracking_guide'].search([]),
#         })

#     @http.route('/tracking_guide/tracking_guide/objects/<model("tracking_guide.tracking_guide"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tracking_guide.object', {
#             'object': obj
#         })


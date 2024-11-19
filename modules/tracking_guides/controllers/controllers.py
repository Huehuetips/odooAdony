# -*- coding: utf-8 -*-
# from odoo import http


# class TrackingGuides(http.Controller):
#     @http.route('/tracking_guides/tracking_guides', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tracking_guides/tracking_guides/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tracking_guides.listing', {
#             'root': '/tracking_guides/tracking_guides',
#             'objects': http.request.env['tracking_guides.tracking_guides'].search([]),
#         })

#     @http.route('/tracking_guides/tracking_guides/objects/<model("tracking_guides.tracking_guides"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tracking_guides.object', {
#             'object': obj
#         })


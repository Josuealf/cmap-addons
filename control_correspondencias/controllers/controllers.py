# -*- coding: utf-8 -*-
# from odoo import http


# class ControlCorrespondencias(http.Controller):
#     @http.route('/control_correspondencias/control_correspondencias/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/control_correspondencias/control_correspondencias/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('control_correspondencias.listing', {
#             'root': '/control_correspondencias/control_correspondencias',
#             'objects': http.request.env['control_correspondencias.control_correspondencias'].search([]),
#         })

#     @http.route('/control_correspondencias/control_correspondencias/objects/<model("control_correspondencias.control_correspondencias"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('control_correspondencias.object', {
#             'object': obj
#         })

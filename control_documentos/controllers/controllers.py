# -*- coding: utf-8 -*-

from odoo import http


class ControlDocumentos(http.Controller):
    @http.route('/control_documentos/control_documentos/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/control_documentos/control_documentos/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('control_documentos.listing', {
            'root': '/control_documentos/control_documentos',
            'objects': http.request.env['control_documentos.control_documentos'].search([]),
        })

    @http.route('/control_documentos/control_documentos/objects/<model("control_documentos.control_documentos"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('control_documentos.object', {
            'object': obj
        })

# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OficiosEnviados(models.Model):
    _name = 'control_documentos.oficios_enviados'
    _description = 'Oficios Enviados'

    dependencia_id = fields.Many2one(
        'hr.department',
        string="Dependencia",
        help="Seleccione la dependencia que suscribe el oficio.",
        required=True
    )
    correlativo = fields.Char(
        string="N° de correlativo", 
        required=True, 
        index=True
    )
    destinatario_id = fields.Many2one('res.partner', string="Dirigido", required=True)
    asunto = fields.Text(string="Asunto", help="Colocar el motivo o descripcion resaltante del documento.")
    fecha = fields.Date(string="Fecha")
    status = fields.Selection(
    	[
    		('cancelado', 'Cancelado'),
     		('en_espera', 'En espera'),
     		('enviado', 'Enviado'),
     		('recibido', 'Recibido')
     	],
     	string="Estado",
     	default='en_espera'
    )
    archivo_img = fields.Binary(string="Anexar documento")

    def set_cancelado_progressbar(self):
        for self in self:
    	    self.status = 'cancelado'

    def set_enviado_progressbar(self):
        for self in self:
    	    self.status = 'enviado'

    def set_recibido_progressbar(self):
        for self in self:
    	    self.status = 'recibido'

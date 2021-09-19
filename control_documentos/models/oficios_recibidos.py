# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OficiosRecibidos(models.Model):
    _name = 'control_documentos.oficios_recibidos'
    _description = 'Oficios Recibidos'

    correlativo = fields.Char(string="N° de correlativo", required=True, index=True)
    remitente_id = fields.Many2one('res.partner', string="Remitente", required=True)
    asunto = fields.Text(string="Asunto", help="Colocar el motivo o descripcion resaltante del documento.")
    fecha = fields.Date(string="Fecha")
    fechahora_recibo = fields.Datetime(string="Fecha de recibido", default=fields.Datetime.now())
    archivo_img = fields.Binary(string="Anexar documento")

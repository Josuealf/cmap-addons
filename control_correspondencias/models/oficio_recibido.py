# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OficioRecibido(models.Model):
    _name = 'cmap.oficio_recibido'
    _description = 'Oficio Recibido'

    id_id = fields.Integer(
        string="ID", 
        index=True,
        required=True
    )
    correlativo = fields.Char(
    	string="N° de correlativo", 
    	required=True
    )
    remitente_id = fields.Many2one(
    	'res.partner',
    	string="Remitente", 
    	required=True
    )
    asunto = fields.Text(
    	string="Asunto", 
    	help="Colocar el motivo o descripcion resaltante del documento."
    )
    fecha = fields.Date(string="Fecha")
    fechahora_recibo = fields.Datetime(
    	string="Fecha de recibido", 
    	default=fields.Datetime.now()
    )
    archivo_img = fields.Binary(string="Anexar documento")

    _sql_constraints = [
        ('id_unique',
         'UNIQUE(id_id)',
         "The ID must be unique"),
    ]
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'
    _description = 'Partner'

    oficio_enviado_ids = fields.One2many(
    	'cmap.oficio_enviado',
    	'destinatario_id',
    	string="Oficios Recibidos", 
    	readonly=True,
    	domain=[('status', '=', 'recibido')]
    )
    oficio_recibido_ids = fields.One2many(
    	'cmap.oficio_recibido',
    	'remitente_id',
    	string="Oficios Enviados", 
    	readonly=True
    )

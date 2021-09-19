# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Department(models.Model):
    _inherit = 'hr.department'
    _description = 'HR Department'

    acronyms = fields.Char(string="Department Acronyms")
    total_oficios_enviados = fields.Integer(
    	string="Total de oficios enviados", 
    	readonly=True, 
    	compute="_get_total_oficios_enviados"
    )

    def _get_total_oficios_enviados(self):
    	for department in self:
    		department.total_oficios_enviados = self.env["control_documentos.oficios_enviados"].search_count(
    			[("dependencia_id", "=", department.id)])
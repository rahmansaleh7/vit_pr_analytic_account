# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Vitpranalyticaccount(models.Model):
    _name = "vit.product.request.line"
    _inherit = "vit.product.request.line"

    def action_create_pr(self):
    	# print(self.department_id.analytic_account_id.name)
    	# print("================================================================")

        res = super(Vitpranalyticaccount, self).action_create_pr()
        for x in self :
            pra = x.env['purchase.requisition.line'].search([('requisition_id.origin','=', x.product_request_id.name)])
            pra.account_analytic_id = x.department_id.analytic_account_id
        return res



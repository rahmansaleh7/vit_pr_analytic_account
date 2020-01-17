# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class vit_pr_analytic_account(models.Model):
#     _name = 'vit_pr_analytic_account.vit_pr_analytic_account'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
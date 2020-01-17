# -*- coding: utf-8 -*-
from odoo import http

# class VitPrAnalyticAccount(http.Controller):
#     @http.route('/vit_pr_analytic_account/vit_pr_analytic_account/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_pr_analytic_account/vit_pr_analytic_account/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_pr_analytic_account.listing', {
#             'root': '/vit_pr_analytic_account/vit_pr_analytic_account',
#             'objects': http.request.env['vit_pr_analytic_account.vit_pr_analytic_account'].search([]),
#         })

#     @http.route('/vit_pr_analytic_account/vit_pr_analytic_account/objects/<model("vit_pr_analytic_account.vit_pr_analytic_account"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_pr_analytic_account.object', {
#             'object': obj
#         })
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class Project(models.Model):
    _inherit = 'project.project'

    analytic_line_plan_sales_ids = fields.One2many(
        'account.analytic.line',
        'analytic_project_id',
        domain=[('category', '=', 'plan'),
                ('analytic_type', '=', 'sales')],
        string='Analytic Lines (Plan)',
    )
    analytic_line_actual_sales_ids = fields.One2many(
        'account.analytic.line',
        'analytic_project_id',
        domain=[('category', '=', 'actual'),
                ('analytic_type', '=', 'sales')],
        string='Analytic Lines (Actual)',
    )

# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class Project(models.Model):
    _inherit = 'project.project'

    analytic_line_plan_sales_ids = fields.One2many(
        'account.analytic.line',
        'analytic_project_id',
        domain=[('category', '=', 'plan'),
                ('analytic_type', '=', '10_sales')],
        string='Sales (Plan)',
    )
    analytic_line_actual_sales_ids = fields.One2many(
        'account.analytic.line',
        'analytic_project_id',
        domain=[('category', '=', 'actual'),
                ('analytic_type', '=', '10_sales')],
        string='Sales (Actual)',
    )
    analytic_line_plan_labour_ids = fields.One2many(
        'account.analytic.line',
        'analytic_project_id',
        domain=[('category', '=', 'plan'),
                ('analytic_type', '=', '20_labour')],
        string='Labour (Plan)',
    )
    analytic_line_actual_labour_ids = fields.One2many(
        'account.analytic.line',
        'analytic_project_id',
        domain=[('category', '=', 'actual'),
                ('analytic_type', '=', '20_labour')],
        string='Labour (Actual)',
    )
    analytic_line_plan_pack_mat_ids = fields.One2many(
        'account.analytic.line',
        'analytic_project_id',
        domain=[('category', '=', 'plan'),
                ('analytic_type', '=', '30_pack_mat')],
        string='Packaging Materials (Plan)',
    )
    analytic_line_actual_pack_mat_ids = fields.One2many(
        'account.analytic.line',
        'analytic_project_id',
        domain=[('category', '=', 'actual'),
                ('analytic_type', '=', '30_pack_mat')],
        string='Packaging Materials (Actual)',
    )
    analytic_line_plan_outsourcing_ids = fields.One2many(
        'account.analytic.line',
        'analytic_project_id',
        domain=[('category', '=', 'plan'),
                ('analytic_type', '=', '40_outsourcing')],
        string='Outsourcing (Plan)',
    )
    analytic_line_actual_outsourcing_ids = fields.One2many(
        'account.analytic.line',
        'analytic_project_id',
        domain=[('category', '=', 'actual'),
                ('analytic_type', '=', '40_outsourcing')],
        string='Outsourcing (Actual)',
    )
    analytic_line_plan_logistics_ids = fields.One2many(
        'account.analytic.line',
        'analytic_project_id',
        domain=[('category', '=', 'plan'),
                ('analytic_type', '=', '50_logistics')],
        string='Logistics (Plan)',
    )
    analytic_line_actual_logistics_ids = fields.One2many(
        'account.analytic.line',
        'analytic_project_id',
        domain=[('category', '=', 'actual'),
                ('analytic_type', '=', '50_logistics')],
        string='Logistics (Actual)',
    )
    analytic_line_plan_expenses_ids = fields.One2many(
        'account.analytic.line',
        'analytic_project_id',
        domain=[('category', '=', 'plan'),
                ('analytic_type', '=', '60_expenses')],
        string='Expenses (Plan)',
    )
    analytic_line_actual_expenses_ids = fields.One2many(
        'account.analytic.line',
        'analytic_project_id',
        domain=[('category', '=', 'actual'),
                ('analytic_type', '=', '60_expenses')],
        string='Expenses (Actual)',
    )

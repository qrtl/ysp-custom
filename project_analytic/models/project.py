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
        string='Sales (Plan)',
    )
    analytic_line_actual_sales_ids = fields.One2many(
        'account.analytic.line',
        'analytic_project_id',
        domain=[('category', '=', 'actual'),
                ('analytic_type', '=', 'sales')],
        string='Sales (Actual)',
    )
    analytic_line_plan_labour_ids = fields.One2many(
        'account.analytic.line',
        'analytic_project_id',
        domain=[('category', '=', 'plan'),
                ('analytic_type', '=', 'labour')],
        string='Labour (Plan)',
    )
    analytic_line_actual_labour_ids = fields.One2many(
        'account.analytic.line',
        'analytic_project_id',
        domain=[('category', '=', 'actual'),
                ('analytic_type', '=', 'labour')],
        string='Labour (Actual)',
    )
    analytic_line_plan_pack_mat_ids = fields.One2many(
        'account.analytic.line',
        'analytic_project_id',
        domain=[('category', '=', 'plan'),
                ('analytic_type', '=', 'pack_mat')],
        string='Packaging Materials (Plan)',
    )
    analytic_line_actual_pack_mat_ids = fields.One2many(
        'account.analytic.line',
        'analytic_project_id',
        domain=[('category', '=', 'actual'),
                ('analytic_type', '=', 'pack_mat')],
        string='Packaging Materials (Actual)',
    )
    analytic_line_plan_outsourcing_ids = fields.One2many(
        'account.analytic.line',
        'analytic_project_id',
        domain=[('category', '=', 'plan'),
                ('analytic_type', '=', 'outsourcing')],
        string='Outsourcing (Plan)',
    )
    analytic_line_actual_outsourcing_ids = fields.One2many(
        'account.analytic.line',
        'analytic_project_id',
        domain=[('category', '=', 'actual'),
                ('analytic_type', '=', 'outsourcing')],
        string='Outsourcing (Actual)',
    )
    analytic_line_plan_logistics_ids = fields.One2many(
        'account.analytic.line',
        'analytic_project_id',
        domain=[('category', '=', 'plan'),
                ('analytic_type', '=', 'logistics')],
        string='Logistics (Plan)',
    )
    analytic_line_actual_logistics_ids = fields.One2many(
        'account.analytic.line',
        'analytic_project_id',
        domain=[('category', '=', 'actual'),
                ('analytic_type', '=', 'logistics')],
        string='Logistics (Actual)',
    )
    analytic_line_plan_expenses_ids = fields.One2many(
        'account.analytic.line',
        'analytic_project_id',
        domain=[('category', '=', 'plan'),
                ('analytic_type', '=', 'expenses')],
        string='Expenses (Plan)',
    )
    analytic_line_actual_expenses_ids = fields.One2many(
        'account.analytic.line',
        'analytic_project_id',
        domain=[('category', '=', 'actual'),
                ('analytic_type', '=', 'expenses')],
        string='Expenses (Actual)',
    )

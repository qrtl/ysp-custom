# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    # this field is added to keep corresponding project to analytic account
    # since 'project_id' field is only populated for timesheet entries
    analytic_project_id = fields.Many2one(
        'project.project',
        string='Related Project',
        compute='_compute_analytic_project_id',
        inverse='_set_account_id',
        store=True,
    )
    sale_id = fields.Many2one(
        'sale.order',
        string='Sales Order',
        compute='_compute_analytic_project_id',
        store=True,
        readonly=True,
    )
    team_id = fields.Many2one(
        related='sale_id.team_id',
        store=True,
        readonly=True,
    )
    sale_user_id = fields.Many2one(
        related='sale_id.user_id',
        store=True,
        readonly=True,
    )
    # this overrides the standard employee_id field to add compute method
    employee_id = fields.Many2one(
        # 'hr.employee',
        # string='Employee',
        compute='_compute_employee_id',
        store=True,
        readonly=True,
    )
    department_id = fields.Many2one(
        'hr.department',
        string='Department',
        compute='_compute_employee_id',
        store=True,
        readonly=True,
    )
    product_categ_id = fields.Many2one(
        related='product_id.categ_id',
        store=True,
        readonly=True,
    )


    @api.multi
    @api.depends('account_id')
    def _compute_analytic_project_id(self):
        for ln in self:
            projects = ln.account_id and ln.account_id.project_ids
            ln.analytic_project_id = projects and projects[0].id or False
            # use sudo() for search here - not all users have access to all
            # the sales orders
            sale_orders = self.env['sale.order'].sudo().search(
                [('analytic_account_id', '=', ln.account_id.id),
                 ('state', '!=', 'cancel')])
            if len(sale_orders) == 1:
                ln.sale_id = sale_orders[0].id

    @api.multi
    @api.depends('user_id')
    def _compute_employee_id(self):
        for ln in self:
            emp_ids = self.env['hr.employee'].search(
                [('user_id', '=', ln.user_id.id)])
            if emp_ids:
                ln.employee_id = emp_ids[0]
                ln.department_id = emp_ids[0].department_id

    @api.multi
    def _set_account_id(self):
        for ln in self:
            ln.account_id = ln.analytic_project_id.analytic_account_id.id

    @api.model
    def create(self, vals):
        # assumption: 'plan' is set when plan records are created through
        # project form
        if not vals.get('category'):
            vals['category'] = 'actual'
            # assumption: project_id is included only for timesheet entries
            if vals.get('project_id'):
                vals['analytic_type'] = '20_labour'
        return super(AccountAnalyticLine, self).create(vals)

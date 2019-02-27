# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class Project(models.Model):
    _inherit = 'project.project'


    analytic_line_ids = fields.One2many(
        'account.analytic.line',
        'analytic_project_id',
        # domain="([('category', '=', 'plan')])",
        string='Analytic Lines',
    )

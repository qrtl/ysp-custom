# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    # we cannot make this field required at model level because that would
    # interfere the record creation from HrTimesheetSheet thru JS
    analytic_type_id = fields.Many2one(
        'analytic.type',
        string='Analytic Type',
        # required=True,
    )
    related_analytic_type = fields.Selection(
        related="analytic_type_id.type",
        readonly=True,
    )
    category = fields.Selection(
        [('plan', 'Plan'),
         ('actual', 'Actual')],
    )


    @api.onchange('general_account_id')
    def _onchange_analytic_type_id(self):
        self.analytic_type_id = self.general_account_id.analytic_type_id

    @api.model
    def create(self, vals):
        analytic_type = False
        if vals.get('general_account_id') and not vals.get('analytic_type_id'):
            account = self.env['account.account'].browse(
                vals['general_account_id'])
            analytic_type = account.analytic_type_id
        vals['analytic_type_id'] = analytic_type and analytic_type.id or False
        return super(AccountAnalyticLine, self).create(vals)

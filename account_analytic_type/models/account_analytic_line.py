# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api

ANALYTIC_TYPE_SELECTION = [
        ('10_sales', 'Sales'),
        ('20_labour', 'Labour'),
        ('30_pack_mat', 'Packaging Materials'),
        ('40_outsourcing', 'Outsourcing'),
        ('50_logistics', 'Logistics'),
        ('60_expenses', 'Expenses'),
        ('70_other', 'Other')]


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    # FIXME check if below statement is valid
    # we cannot make this field required at model level because that would
    # interfere the record creation from HrTimesheetSheet thru JS
    analytic_type = fields.Selection(
        ANALYTIC_TYPE_SELECTION,
        'Analytic Type',
    )
    category = fields.Selection(
        [('plan', 'Plan'),
         ('actual', 'Actual')],
    )


    @api.onchange('general_account_id')
    def _onchange_general_account_id(self):
        if self.general_account_id:
            self.analytic_type_id = self.general_account_id.analytic_type_id

    @api.model
    def create(self, vals):
        # assumption: 'plan' is set when plan records are manually created
        if not vals.get('category') == 'plan':
            vals['category'] = 'actual'
            if vals.get('general_account_id') and not vals.get(
                    'analytic_type'):
                account = self.env['account.account'].browse(
                    vals['general_account_id'])
                vals['analytic_type'] = account.analytic_type
        return super(AccountAnalyticLine, self).create(vals)

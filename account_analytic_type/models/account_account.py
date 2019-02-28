# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models
from . import account_analytic_line as al


class AccountAccount(models.Model):
    _inherit = "account.account"

    analytic_type = fields.Selection(
        al.ANALYTIC_TYPE_SELECTION,
        'Analytic Type',
    )

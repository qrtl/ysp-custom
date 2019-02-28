# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Analytic Type",
    "description": """
- Adds analytic type model for better analysis of analytic lines
    """,
    "version": "12.0.1.0.0",
    "category": "Accounting",
    "website": "https://www.quartile.co/",
    "author": "Quartile Limited",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        'account',
    ],
    "data": [
        'views/account_account_views.xml',
        'views/account_analytic_line_views.xml',
    ],
}

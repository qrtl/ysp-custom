# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Project Analytic",
    "description": """
- Facilicates analytic analysis by creating links to analytic lines from 
project
    """,
    "version": "12.0.1.0.0",
    "category": "Project",
    "website": "https://www.quartile.co/",
    "author": "Quartile Limited",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        'account_analytic_type',
        'sale_timesheet',
    ],
    "data": [
        'views/project_views.xml',
        'views/account_analytic_line_views.xml',
    ],
}

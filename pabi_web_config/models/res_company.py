# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Business Applications
#    Copyright (C) 2016 Savoir-faire Linux
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    pabiweb_active = fields.Boolean(
        string="Open Connection to PABI Web.",
    )
    pabiweb_hr_url = fields.Char(
        string='PABI Web URL for HR Salary',
    )
    pabiweb_exp_url = fields.Char(
        string='PABI Web URL for Expense',
    )
    pabiweb_pcm_url = fields.Char(
        string='PABI Web URL for Procurement',
    )
    pabiweb_file_prefix = fields.Char(
        string='PABI Web URL for attachment prefix',
    )

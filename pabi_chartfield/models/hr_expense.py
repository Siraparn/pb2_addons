# -*- coding: utf-8 -*-
from openerp import api, models, fields
from .chartfield import ChartField, HeaderTaxBranch


class HRExpenseExpense(HeaderTaxBranch, models.Model):
    _inherit = 'hr.expense.expense'

    taxbranch_id = fields.Many2one(
        compute='_compute_taxbranch_id',
        store=True,
    )

    @api.one
    @api.depends('line_ids')
    def _compute_taxbranch_id(self):
        lines = self.line_ids
        self.taxbranch_id = self._check_taxbranch_id(lines)


class HRExpenseLine(ChartField, models.Model):
    _inherit = 'hr.expense.line'

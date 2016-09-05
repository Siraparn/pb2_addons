# -*- coding: utf-8 -*-
from openerp import models, fields, api


class AccountBudget(models.Model):
    _inherit = "account.budget"

    @api.model
    def document_check_budget(self, doc_date, doc_lines, amount_field):
        res = super(AccountBudget, self).document_check_budget(doc_date,
                                                               doc_lines,
                                                               amount_field)
        if not res['budget_ok']:
            return res
        # Add check by fund rule
        FundRule = self.env['budget.fund.rule']
        res = FundRule.document_check_fund_spending(doc_date,
                                                    doc_lines,
                                                    amount_field)
        if not res['budget_ok']:
            return res
        return res

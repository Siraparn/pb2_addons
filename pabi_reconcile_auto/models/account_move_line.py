# -*- coding: utf-8 -*-
from openerp import models, api, fields


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    auto_reconcile_id = fields.Many2one(
        'account.auto.reconcile',
        string='Auto Reconcile ID',
        related='move_id.auto_reconcile_id',
        help="To group journal entry for auto reconcilation",
    )

    @api.multi
    def reconcile_special_account(self):
        """ This method will reconcile move_line with account.reconcile = True,
        in addition to receviable and payable account by standard of Odoo """
        excludes = ('receivable', 'payable')
        move_lines = self.filtered(lambda l: l.account_id.reconcile and
                                   l.state == 'valid' and
                                   not l.reconcile_id and
                                   l.account_id.type not in excludes)
        if not move_lines:
            return
        accounts = move_lines.mapped('account_id')
        for account in accounts:
            to_rec = move_lines.filtered(lambda l: l.account_id == account)
            if len(to_rec) >= 2:
                to_rec.reconcile_partial('auto')

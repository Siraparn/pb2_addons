# -*- coding: utf-8 -*-
from openerp import models, api


class StockMove(models.Model):
    _inherit = 'stock.move'

    @api.multi
    def action_done(self):
        res = super(StockMove, self).action_done()
        MoveLine = self.env['account.move.line']
        Auto = self.env['account.auto.reconcile']
        # Case GR/IR, use order_number as auto_reconcile_id
        for picking in self.mapped('picking_id'):
            pick_mlines = MoveLine.search([('ref', '=', picking.name)])
            if pick_mlines:
                account_moves = False
                order_number = False
                # Case picking from SO
                if picking.sale_id:
                    account_moves = pick_mlines.mapped('move_id')
                    order_number = picking.sale_id.name
                else:
                    purchase = picking.move_lines.\
                        mapped('purchase_line_id.order_id')
                    if purchase:
                        account_moves = pick_mlines.mapped('move_id')
                        order_number = purchase.name
                # Got something to reconcile
                if account_moves and order_number:
                    auto_id = Auto.get_auto_reconcile_id(order_number)
                    account_moves.write({'auto_reconcile_id': auto_id})
                    mlines = MoveLine.search([('auto_reconcile_id',
                                               '=', auto_id)])
                    mlines.reconcile_special_account()
        return res

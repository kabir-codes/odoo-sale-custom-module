from odoo import api, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_form_sale_order(self):
        return {
        'name': 'My Window',
        'type': 'ir.actions.act_window',
        'view_mode': 'form',
        'view_type': 'form',
        'context': {},
        'target': 'new',
        'res_model': 'sale.order.form',
    }
    def action_saved_form_order(self):
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': '#'
        }

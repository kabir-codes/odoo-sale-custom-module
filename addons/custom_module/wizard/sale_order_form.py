from odoo import Command, _, api, fields, models

class SaleOrderForm(models.Model):
    _name = 'sale.order.form'
    _description = 'Form Wizard'

    first_name = fields.Char(string="First Name")
    last_name  = fields.Char(string="Last Name")
    date_of_birth = fields.Date(string="Date of Birth")
    select_occupancy = fields.Selection([('normal', 'In Progress'), ('done', 'Ready for next stage'), 
                                         ('blocked', 'Blocked')], string='State')
    def save_draft(self):
        return {
            'type': 'ir.actions.act_window',
            'target': 'current',
            'res_model': 'sale.order.form',
            'view_mode': 'tree,form',
        }
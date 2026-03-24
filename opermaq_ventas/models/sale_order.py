from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # 1. Campo para enlazar manualmente la factura
    opermaq_factura_id = fields.Many2one(
        comodel_name='account.move',
        string='Factura',
        # Este dominio asegura que solo puedas elegir Facturas de Clientes (no de proveedores ni notas internas)
        domain="[('move_type', '=', 'out_invoice')]"
    )

    # 2. Campo espejo del estado de facturación nativo
    opermaq_estado_factura = fields.Selection(
        related='invoice_status', 
        string='Estado de la factura',
        readonly=True
    )
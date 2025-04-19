from odoo import models
from ..models.whatsapp_mixin import WhatsAppMixin

class SaleOrder(models.Model, WhatsAppMixin):
    _inherit = 'sale.order'
    # Inherit WhatsApp Mixin directly in the class

    def action_send_whatsapp(self):
        # Directly call the method from WhatsAppMixin
        return self._action_send_whatsapp()

class AccountMove(models.Model, WhatsAppMixin):
    _inherit = 'account.move'

    def action_send_whatsapp(self):
        # Directly call the method from WhatsAppMixin
        return self._action_send_whatsapp()

class ResPartner(models.Model, WhatsAppMixin):
    _inherit = 'res.partner'

    def action_send_whatsapp(self):
        # Directly call the method from WhatsAppMixin
        return self._action_send_whatsapp()

from odoo import models
from urllib.parse import quote

class WhatsAppMixin(models.AbstractModel):
    _name = 'whatsapp.mixin'
    _description = 'Mixin to add WhatsApp message button'

    def _action_send_whatsapp(self):
        for record in self:
            partner = record.partner_id if hasattr(record, 'partner_id') else record
            if not partner.mobile:
                continue
            number = partner.mobile.replace(" ", "").replace("+", "")
            message = f"Hello {partner.name},\n\nHere is your document: {record.name}"
            return {
                'type': 'ir.actions.act_url',
                'url': f"https://wa.me/{number}?text={quote(message)}",
                'target': 'new',
            }

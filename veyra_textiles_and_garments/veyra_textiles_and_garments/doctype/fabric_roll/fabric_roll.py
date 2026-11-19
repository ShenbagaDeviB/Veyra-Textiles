# Copyright (c) 2026, Shenbaga Devi B and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import qrcode
from io import BytesIO
from frappe.utils.file_manager import save_file

class FabricRoll(Document):
    def validate(self):
        if self.consumed_length > self.initial_length:
            frappe.throw("Consumed length cannot be greater than initial length")
        if self.consumed_weight > self.initial_weight:
            frappe.throw("Consumed weight cannot be greater than initial weight")
        if self.initial_length <= 0.0:
            frappe.throw("Initial length cannot be zero")
        if self.initial_weight <= 0.0:
            frappe.throw("Initial weight cannot be zero")
    def after_insert(self):
        generate_qr_code(self)

def generate_qr_code(doc, method=None):
    if doc.custom_qr_code:
        return
    qr = qrcode.make(doc.name)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    file_doc = save_file(
        fname=f"{doc.name}-QR.png",
        content=buffer.getvalue(),
        dt=doc.doctype,
        dn=doc.name,
        is_private=1
    )
    doc.db_set("custom_qr_code", file_doc.file_url, update_modified=False)
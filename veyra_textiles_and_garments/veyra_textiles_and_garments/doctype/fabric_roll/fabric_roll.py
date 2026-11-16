# Copyright (c) 2026, Shenbaga Devi B and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


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
import frappe

def cancellation_policy(self):
    if(self.status=="To Bill"):
        frappe.throw("To bill document cannot be cancelled")
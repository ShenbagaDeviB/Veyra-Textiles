import frappe
from frappe.query_builder import DocType

@frappe.whitelist()
def fabric_roll_stock():
    fr=DocType("Fabric Roll")
    query=(frappe.qb.from_(fr)
           .select(fr.name,fr.item,fr.batch,fr.initial_length,
                  fr.consumed_length,fr.remaining_length,
                  fr.warehouse,fr.status)).run(as_dict=True)
    return query
import frappe
from frappe.utils import flt

@frappe.whitelist()
def get_item_warehouse_stock(item_code):
    if not frappe.has_permission("Item", "read", doc=item_code):
        frappe.throw("You do not have permission to view this Item.")
    entries = frappe.get_list(
        "Stock Ledger Entry",
        filters={
            "item_code": item_code,
            "is_cancelled": 0
        },
        fields=["warehouse", "actual_qty"],
        limit_page_length=0
    )
    bins = frappe.get_list(
        "Bin",
        filters={"item_code": item_code},
        fields=["warehouse", "actual_qty"],
        limit_page_length=0
    )
    warehouse_data = {}
    for entry in entries:
        warehouse = entry.warehouse
        if warehouse not in warehouse_data:
            warehouse_data[warehouse] = {
                "in_qty": 0,
                "out_qty": 0,
                "balance_qty": 0
            }
        qty = flt(entry.actual_qty)
        if qty > 0:
            warehouse_data[warehouse]["in_qty"] += qty
        elif qty < 0:
            warehouse_data[warehouse]["out_qty"] += abs(qty)
    for bin_row in bins:
        warehouse = bin_row.warehouse
        if warehouse not in warehouse_data:
            warehouse_data[warehouse] = {
                "in_qty": 0,
                "out_qty": 0,
                "balance_qty": 0
            }

        warehouse_data[warehouse]["balance_qty"] = flt(
            bin_row.actual_qty
        )
    warehouses = []
    for warehouse, data in warehouse_data.items():
        warehouses.append({
            "warehouse": warehouse,
            "in_qty": data["in_qty"],
            "out_qty": data["out_qty"],
            "balance_qty": data["balance_qty"]
        })
    return {
        "warehouses": warehouses,
        "total_in": sum(row["in_qty"] for row in warehouses),
        "total_out": sum(row["out_qty"] for row in warehouses),
        "total_balance": sum(row["balance_qty"] for row in warehouses)
    }
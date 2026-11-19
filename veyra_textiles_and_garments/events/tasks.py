import frappe

@frappe.whitelist()
def check_low_fabric_rolls():
    """Check fabric rolls with less than 10 metres remaining."""

    low_rolls = frappe.get_all(
        "Fabric Roll",
        filters={
            "remaining_length": ["<", 10]
        },
        fields=["name", "remaining_length"]
    )

    if not low_rolls:
        return

    message = "The following fabric rolls have less than 10 metres remaining:\n\n"

    for roll in low_rolls:
        message += (
            f"Roll: {roll.name} | "
            f"Remaining Length: {roll.remaining_length} metres\n"
        )

    frappe.log_error(
        message=message,
        title="Veyra - Low Fabric Roll Alert"
    )
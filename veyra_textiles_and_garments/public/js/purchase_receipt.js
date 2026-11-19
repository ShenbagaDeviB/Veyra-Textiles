frappe.ui.form.on("Purchase Receipt", {
    refresh(frm) {
        if (frm.doc.docstatus !== 1) {
            return;
        }
        const item_codes = [
            ...new Set(
                (frm.doc.items || [])
                    .map(row => row.item_code)
                    .filter(Boolean)
            )
        ];
        if (!item_codes.length) return;
        Promise.all(
            item_codes.map(item_code =>
                frappe.db.get_value(
                    "Item",
                    item_code,
                    "item_group"
                )
            )
        ).then(results => {
            const has_fabrics = results.some(
                result =>
                    result.message?.item_group === "Fabrics"
            );
            if (has_fabrics) {
                frm.add_custom_button(
                    __("Create Fabric Roll"),
                    function () {

                        frappe.new_doc("Fabric Roll", {
                            purchase_receipt: frm.doc.name
                        });

                    },
                    __("Actions")
                );
            }
        });
    }
});
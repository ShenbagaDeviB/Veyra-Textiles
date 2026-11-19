frappe.ui.form.on("Item", {
    refresh(frm) {
        if (frm.is_new()) return;
        frm.add_custom_button("View Warehouse Stock", function () {
            frappe.call({
                method: "veyra_textiles_and_garments.events.api.get_item_warehouse_stock",
                args: {
                    item_code: frm.doc.item_code
                },
                callback: function (r) {
                    if (!r.message) return;
                    let rows = r.message.warehouses.map(row => `
                        <tr>
                            <td>${frappe.utils.escape_html(row.warehouse)}</td>
                            <td>${row.in_qty}</td>
                            <td>${row.out_qty}</td>
                            <td>${row.balance_qty}</td>
                        </tr>
                    `).join("");
                    let html = `
                        <table class="table table-bordered">
                            <tr>
                                <th>Warehouse</th>
                                <th>In</th>
                                <th>Out</th>
                                <th>Available</th>
                            </tr>
                            ${rows}
                        </table>
                        <b>Total In:</b> ${r.message.total_in}<br>
                        <b>Total Out:</b> ${r.message.total_out}<br>
                        <b>Available:</b> ${r.message.total_balance}
                    `;
                    frappe.msgprint({
                        title: "Warehouse Stock",
                        message: html,
                        wide: true
                    });
                }
            });
        }, "Stock");
    }
});
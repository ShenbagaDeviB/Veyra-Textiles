// Copyright (c) 2026, Shenbaga Devi B and contributors
// For license information, please see license.txt

frappe.ui.form.on("Job Application", {
    after_save(frm) {
        let dob = new Date(frm.doc.date_of_birth)
        let today = new Date()
        let age = today.getFullYear() - dob.getFullYear()
        let month = today.getMonth() - dob.getMonth()
        let date = today.getDate() - dob.getDate()
        if(month < 0 || (month == 0 && (date < 0))){
            age--
        }
        frm.set_value("age",age)
	},
    refresh(frm){
        frm.set_intro("Please fill the details for further process","blue")
    },
    onload(frm) {
        if (frm.is_new()) {
            frappe.msgprint("Welcome to Veyra Textiles Job Application Form")
        }
    }
 });
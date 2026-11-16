// Copyright (c) 2026, Shenbaga Devi B and contributors
// For license information, please see license.txt

frappe.ui.form.on("Fabric Roll", {
    before_save(frm) {
        frm.doc.remaining_length=frm.doc.initial_length-frm.doc.consumed_length
        frm.doc.remaining_weight=frm.doc.initial_weight-frm.doc.consumed_weight
 	},
    setup(frm){
        frm.set_query("item",function(){
            return{
                filters:{
                    custom_is_fabric_item:1
                }
            }
        })
    },
    refresh(frm){
        if(frm.doc.remaining_length!=0){
            frm.add_custom_button("Roll Available",()=>{
                frappe.msgprint("Roll is available for Production.")
            })
        }
        if(frm.doc.status=="Available")
            frm.dashboard.add_indicator("Available","green")
        else if(frm.doc.status=="Rejected")
            frm.dashboard.add_indicator("Rejected","red")
        else if(frm.doc.status=="Partially Consumed")
            frm.dashboard.add_indicator("Partially Consumed","orange")
        else
            frm.dashboard.add_indicator("Status will be said later","grey")
    },
 });
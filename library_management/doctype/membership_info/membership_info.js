// Copyright (c) 2024, Ganesh Nikam and contributors
// For license information, please see license.txt

frappe.ui.form.on("Membership Info", {
	refresh(frm) {

	},
    fetch_membership_data:function(frm) {
        frappe.call({
            method:"get_membership_data",
            doc:frm.doc,
              
            callback:function(r){
                if (r.message){
                    frm.refresh_field("membership_details")
                }
            }

        })

	},
});

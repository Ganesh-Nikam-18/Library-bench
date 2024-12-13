// Copyright (c) 2024, Ganesh Nikam and contributors
// For license information, please see license.txt

frappe.ui.form.on("Library Member", {
	refresh(frm) {
        frm.add_custom_button("Create Membership", function(){
            add_membership();

        })
        frm.add_custom_button("Re-new Membership",function(){
            add_membership();
        }) 
    
        function add_membership() {
                    frappe.new_doc('Library Membership')
        
        }
    }
});
 


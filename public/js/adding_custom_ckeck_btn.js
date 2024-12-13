frappe.listview_settings['Library Membership'] = {
    refresh: function (listview) {
        listview.page.add_action_item('Check Paid count', function () {
            frappe.call({
                
                method: 'library_management.library_management.doctype.library_membership.library_membership.get_paid_membership_count',

            });
        });
    }
};

# Copyright (c) 2024, Ganesh Nikam and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document,DocStatus

class LibraryMembership(Document):
    # check before submitting this document
    def before_submit(self):
        exists = frappe.db.exists(
            "Library Membership",
            {
                "library_member": self.library_member,
                "docstatus": DocStatus.submitted(),
                # check if the membership's end date is later than this membership's start date
                "to_date": (">", self.from_date),
            },
        )
        if exists:
            frappe.throw("There is an active membership for this member")

    def onload(self):
        self.get_values()
                
    def get_values(self):
            Membership_status=frappe.db.get_value("Library Membership",self.name,"status")
            if Membership_status:
                frappe.msgprint(f"Membership Status :- {Membership_status}")		
            else:
                 frappe.msgprint("Membership not found for this member")

# ------------------- Num of membership was not submited  in the Library ------------------------
@frappe.whitelist()
def get_paid_membership_count():
    data=frappe.db.sql(
                        """
                            select count(name) from `tabLibrary Membership` where paid=1;
        """
    )

    frappe.msgprint(f"The count of paid membership is {data}")

                        
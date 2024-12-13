# Copyright (c) 2024, Ganesh Nikam and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _

class LibraryMember(Document):
    def before_save(self):
        self.full_name = f'{self.first_name} {self.last_name or ""}'

    def validate(self):
        self.new_document()
        # self.get_list()
        # self.set_value()

# -------------------Creating New Doc ------------------------

    def new_document(self):
        if not frappe.db.exists("Library Membership", {'library_member':self.name}):
            doc=frappe.new_doc("Library Membership")
            doc.library_member=self.name
            doc.insert()

# ------------------- DB List -------------------------

    def get_list(self):
        doc=frappe.db.get_list("Library Member",
                                                fields=['first_name' , 'last_name']
                           )
        for d in doc:
            frappe.msgprint(_("The first name {0} The last name {1}").format(d.first_name,d.last_name))

    def re_new_membership(self):
        print("This is from re-new-membership btn ")
        doc = frappe.get_doc('Library Membership', 'title')
        doc.save()
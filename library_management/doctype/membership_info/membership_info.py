# Copyright (c) 2024, Ganesh Nikam and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class MembershipInfo(Document):

	@frappe.whitelist()
	def get_membership_data(self):
		existing_memberships = {row.library_membership for row in self.membership_details}

		data=frappe.get_all("Library Membership",fields=["name","full_name","to_date"])

		for details in data:
					if details.name not in existing_memberships:
						self.append('membership_details',{
						"library_membership":details.name,
						"full_name":details.full_name,
						"validate_date":details.to_date,
							
					})
					existing_memberships.add(details.name)


		frappe.msgprint("Membership details have been updated successfully.")
		return True

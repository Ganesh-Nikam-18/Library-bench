# Copyright (c) 2024, Ganesh Nikam and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
#>>>>>>>>>>>>>>>>>------- custom file method call by url --------<<<<<<<<<<<<<<<<<
from library_management.library_management.cusiom_doc_API import get_article
# ----------------------------------------------------------------
class Article(WebsiteGenerator):
    
    def get_record(self,method):
        doc=frappe.get_doc("Article")
        print("this is doc-----------------",doc)
	

                        
		
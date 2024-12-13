import frappe 
def get_article(self,method=None):
    doc=frappe.get_doc('STUDENT','STD0007')
    for details in doc.educations:
        print("---------->",details.degree,details.certification,details.achivements,"parent------",details.parent)
    


#  =----------------------  

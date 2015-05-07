__author__ = 'nata'
from model.contact import Contact


testdata = [
    Contact(first_name="First Name 1", middle_name="Middle Name 1", last_name="Last Name 1", nickname="Nickname 1",
            title="Title 1", company="Company 1", address="Address 1 1", home_phone="+9999999991",
            mobile_phone="+9999999991", work_phone="+9999999991", fax="+9999999991", email="email1@none1.net",
            email2="email2@none1.net", email3="email3@none1.net", homepage="http://www1.homepage.net",
            address2= "Address 1 2", secondary_phone="+9999999991", notes="Notes 1"),
    Contact(first_name="First Name 2", middle_name="Middle Name 2", last_name="Last Name 2", nickname="Nickname 2",
            title="Title 2", company="Company 2", address="Address 1 2", home_phone="+9999999992",
            mobile_phone="+9999999992", work_phone="+9999999992", fax="+9999999992", email="email1@none2.net",
            email2="email2@none2.net", email3="email3@none2.net", homepage="http://www2.homepage.net",
            address2= "Address 2 2", secondary_phone="+9999999992", notes="Notes 2")
]

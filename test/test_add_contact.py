# -*- coding: utf-8 -*-
from model.contact import Contact



def test_add_a_contact(app):
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="first name", middle_name="middle name", last_name="last name",
                               nickname="nickname", title="title", company="company", address="address",
                               home_phone="home", mobile_phone="mobile", work_phone="work", fax="fax", address2="address2",
                               secondary_phone="phone2", email="email", email2="email2", email3="email3",
                               homepage="homepage", notes="notes")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts,key=Contact.id_or_max)
    app.return_to_home_page()


def test_add_empty_contact(app):
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="", middle_name="", last_name="", nickname="", title="",
                               company="", address="", home_phone="", mobile_phone="", work_phone="", fax="", address2="",
                               secondary_phone="", email="", email2="", email3="", homepage="", notes="")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts,key=Contact.id_or_max)
    app.return_to_home_page()

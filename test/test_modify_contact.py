# -*- coding: utf-8 -*-
import random
from model.contact import Contact, model_to_view
from generator import random_string


def test_modify_some_contact(app, orm, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="first name"))
    old_contacts = orm.get_contact_list()
    contact = random.choice(old_contacts)
    contact.first_name = random_string("modified")
    contact.last_name = random_string("modified")
    contact.address = random_string("modified")
    new_contact = Contact(id=contact.id, first_name=contact.first_name, last_name=contact.last_name,
                          address=contact.address)
    app.contact.modify_contact_by_id(contact.id, new_contact)
    old_contacts_modified = [contact if c.id == contact.id else c for c in old_contacts]
    new_contacts = orm.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts_modified, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(map(model_to_view, new_contacts), key=Contact.id_or_max) \
            == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

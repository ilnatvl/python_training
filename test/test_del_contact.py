# -*- coding: utf-8 -*-
__author__ = 'nata'
import random
from model.contact import Contact, model_to_view


def test_delete_some_contact(app, orm, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="first name"))
    old_contacts = orm.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = orm.get_contact_list()
    old_contacts.remove(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) \
        == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(map(model_to_view, new_contacts), key=Contact.id_or_max) \
            == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)



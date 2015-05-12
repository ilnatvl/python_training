# -*- coding: utf-8 -*-
from model.contact import Contact, model_to_view


def test_add_a_contact(app, random_contacts, orm, check_ui):
    contact = random_contacts
    old_contacts = orm.get_contact_list()
    app.contact.create(contact)
    new_contacts = orm.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) \
        == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        ui_contact_list = app.contact.get_contact_list()
        assert sorted(map(model_to_view, new_contacts), key=Contact.id_or_max) \
            == sorted(ui_contact_list, key=Contact.id_or_max)

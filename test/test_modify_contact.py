# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_first_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="first name"))
    app.contact.modify_first_contact(Contact(first_name="New first name"))


def test_modify_contact_middle_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="first name"))
    app.contact.modify_first_contact(Contact(middle_name="dlfjoir"))

# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(first_name="first name", middle_name="middle name", last_name="last name",
                                           nickname="nickname", title="title", company="company", address="address",
                                           home="home", mobile="mobile", work="work", fax="fax", address2="address2",
                                           phone2="phone2", email="email", email2="email2", email3="email3",
                                           homepage="homepage", notes="notes"))
    app.session.logout()

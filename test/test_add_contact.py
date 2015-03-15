# -*- coding: utf-8 -*-
from fixture.application import Application
from model.contact import Contact
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_a_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(first_name="first name", middle_name="middle name", last_name="last name",
                               nickname="nickname", title="title", company="company", address="address",
                               home="home", mobile="mobile", work="work", fax="fax", address2="address2",
                               phone2="phone2", email="email", email2="email2", email3="email3",
                               homepage="homepage", notes="notes"))
    app.return_to_home_page()
    app.session.logout()


def test_add_empty_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(first_name="", middle_name="", last_name="", nickname="", title="",
                               company="", address="", home="", mobile="", work="", fax="", address2="",
                               phone2="", email="", email2="", email3="", homepage="", notes=""))
    app.return_to_home_page()
    app.session.logout()

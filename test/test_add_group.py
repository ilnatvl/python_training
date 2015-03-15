# -*- coding: utf-8 -*-
from fixture.application import Application
from model.group import Group
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_a_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="dsdsdsds", header="fsfsfsffsfs", footer="fsfsfsfsfsfs"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()


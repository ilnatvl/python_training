# -*- coding: utf-8 -*-
from model.group import Group


def test_add_a_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="dsdsdsds", header="fsfsfsffsfs", footer="fsfsfsfsfsfs"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
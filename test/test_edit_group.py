# -*- coding: utf-8 -*-
__author__ = 'nata'

from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="dsdsdsds", header="fsfsfsffsfs", footer="fsfsfsfsfsfs"))
    app.session.logout()

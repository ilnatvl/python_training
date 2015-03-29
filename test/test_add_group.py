# -*- coding: utf-8 -*-
from model.group import Group


def test_add_a_group(app):
    app.group.create(Group(name="dsdsdsds", header="fsfsfsffsfs", footer="fsfsfsfsfsfs"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

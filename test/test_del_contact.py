# -*- coding: utf-8 -*-
__author__ = 'nata'


def test_delete_first_contact(app):
    app.contact.delete_first_contact()

# -*- coding: utf-8 -*-

from sys import maxsize


class Contact:

    def __init__(self, first_name=None, middle_name=None, last_name=None, nickname=None, title=None, company=None,
                 address=None, home=None, mobile=None, work=None, fax=None, email=None, email2=None, email3=None,
                 homepage=None, address2=None, phone2=None, notes=None, id=None):
        self.notes = notes
        self.phone2 = phone2
        self.address2 = address2
        self.homepage = homepage
        self.email3 = email3
        self.email2 = email2
        self.email = email
        self.fax = fax
        self.work = work
        self.mobile = mobile
        self.home = home
        self.address = address
        self.company = company
        self.title = title
        self.nickname = nickname
        self.last_name = last_name
        self.middle_name = middle_name
        self.first_name = first_name
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.first_name, self.last_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name and self.last_name == self.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
# -*- coding: utf-8 -*-
class Contact:

    def __init__(self, first_name=None, middle_name=None, last_name=None, nickname=None, title=None, company=None, address=None, home=None, mobile=None, work=None, fax=None,
                email=None, email2=None, email3=None, homepage=None, address2=None, phone2=None, notes=None):
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
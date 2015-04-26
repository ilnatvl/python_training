# -*- coding: utf-8 -*-

from sys import maxsize


class Contact:

    def __init__(self, first_name=None, middle_name=None, last_name=None, nickname=None, title=None, company=None,
                 address=None, home_phone=None, mobile_phone=None, work_phone=None, fax=None, email=None, email2=None,
                 email3=None, homepage=None, address2=None, secondary_phone=None, notes=None, id=None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.first_name = first_name
        self.last_name = last_name
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.secondary_phone = secondary_phone
        self.notes = notes
        self.address = address
        self.address2 = address2
        self.homepage = homepage
        self.email3 = email3
        self.email2 = email2
        self.email = email
        self.fax = fax
        self.company = company
        self.title = title
        self.nickname = nickname
        self.middle_name = middle_name
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.first_name, self.last_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
            and self.first_name == other.first_name and self.last_name == self.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
# -*- coding: utf-8 -*-
from sys import maxsize
import re


def simplify_phone(s):
    return re.sub("\(*.0*.\)|[\- ()]", "", s).replace("+41", "0")


def merge_phones_like_on_home_page(contact):
    return "\n".join(
        filter(None, map(
            lambda x: simplify_phone(x), filter(
                None, [contact.home_phone, contact.mobile_phone,
                       contact.work_phone, contact.secondary_phone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(None, [contact.email, contact.email2, contact.email3]))


def model_to_view(c):
    return Contact(
        id=c.id,
        last_name=" ".join(c.last_name.split()),
        first_name=" ".join(c.first_name.split()),
        address='\n'.join([_.strip() for _ in re.sub(' +', ' ', c.address).split('\n')]),
        all_emails_from_home_page=merge_emails_like_on_home_page(c),
        all_phones_from_home_page=merge_phones_like_on_home_page(c)
    )


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
        return "%s:%s;%s;%s;%s;%s" % (self.id, self.first_name, self.last_name, self.address,
                                   self.all_emails_from_home_page, self.all_phones_from_home_page)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (
            self.first_name == other.first_name
            and self.last_name == other.last_name
            and self.address == other.address
            and self.all_emails_from_home_page == other.all_emails_from_home_page
            and self.all_phones_from_home_page == other.all_phones_from_home_page)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
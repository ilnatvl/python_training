__author__ = 'nata'

import re
from random import randrange


def test_contact_data(app):
    contact_list = app.contact.get_contact_list()
    index = randrange(len(contact_list))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def simplify_phone(s):
    return re.sub("\(*.0*.\)|[\- ()]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(
        filter(None, map(
            lambda x: simplify_phone(x), filter(
                None, [contact.home_phone, contact.mobile_phone,
                       contact.work_phone, contact.secondary_phone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(None, [contact.email, contact.email2, contact.email3]))
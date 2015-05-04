# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen=20):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + " " + "".join([random.choice(symbols) for i in range(random.randrange(1, maxlen))])


def random_multiline_text(prefix, maxrows=5):
    return prefix + random_string("") + "\n".join([random_string("") for i in range(random.randrange(maxrows))])


def random_phone():
    return "+" + "".join(["%s" % random.randint(0, 9) for i in range(0, 10)])


def random_email(prefix, maxlen=10):
    symbols = string.ascii_lowercase
    suffixes =["com", "org", "ru", "net"]
    mailbox = prefix + "_" + "".join([random.choice(symbols) for i in range(random.randrange(1, maxlen))])
    domain = "".join([random.choice(symbols) for i in range(random.randrange(1, maxlen))])
    return mailbox + "@" + domain + "." + random.choice(suffixes)


def random_homepage(prefix, maxlen=10):
    symbols = string.ascii_lowercase
    suffixes =["com", "org", "ru", "net"]
    page = prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen) + 1)])
    domain = "".join([random.choice(symbols) for i in range(random.randrange(maxlen) + 1)])
    return "http://" + page + "." + domain + "." + random.choice(suffixes)

testdata = [
    Contact(first_name="", middle_name="", last_name="", nickname="", title="", company="", address="", home_phone="",
            mobile_phone="", work_phone="", fax="", address2="", secondary_phone="", email="", email2="", email3="",
            homepage="", notes="")
    ] + [
    Contact(first_name=random_string("first name"), middle_name=random_string("middle name"),
            last_name=random_string("last name"),nickname=random_string("nickname"), title=random_string("title"),
            company=random_string("company"), address=random_multiline_text("address"), home_phone=random_phone(),
            mobile_phone=random_phone(), work_phone=random_phone(), fax=random_phone(),
            address2=random_multiline_text("address2"), secondary_phone=random_phone(), email=random_email("email"),
            email2=random_email("email2"), email3=random_email("email3"), homepage=random_homepage("homepage"),
            notes=random_multiline_text("notes"))
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[str(i) + ":" + repr(x) for i, x in enumerate(testdata)])
def test_add_a_contact(app, contact):
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts,key=Contact.id_or_max)
    app.return_to_home_page()


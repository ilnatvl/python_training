__author__ = 'nata'

from model.contact import Contact, model_to_view


def test_contact_data(app, orm):
    contacts_from_db = sorted(map(model_to_view, orm.get_contact_list()), key=Contact.id_or_max)
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    assert contacts_from_db == contacts_from_home_page



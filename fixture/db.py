__author__ = 'nata'
import mysql.connector
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        lst = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list")
            for row in cursor:
                (id, name, header, footer) = row
                lst.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return lst

    def get_contact_list(self):
        lst = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, firstname, middlename, lastname, nickname, company, title, address,"
                           "home, mobile, work, fax, email, email2, email3, homepage, address2, phone2, notes"
                           "FROM addressbook WHERE deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, work, fax,
                 email, email2, email3, homepage, address2, phone2, notes) = row
                lst.append(Contact(id=str(id), first_name=firstname, middle_name=middlename, last_name=lastname,
                                   nickname=nickname, company=company, title=title, address=address, home_phone=home,
                                   mobile_phone=mobile, work_phone=work, fax=fax, email=email, email2=email2,
                                   email3=email3, homepage=homepage, address2=address2, secondary_phone=phone2,
                                   notes=notes))
        finally:
            cursor.close()
        return lst

    def destroy(self):
        self.connection.close()
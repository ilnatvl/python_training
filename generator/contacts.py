__author__ = 'nata'

import jsonpickle
import random
import string
import os.path
import getopt
import sys
from model.contact import Contact
from generator import random_string

n = 3
f = "data/contacts.json"


def random_multiline_text(prefix, maxrows=5):
    return prefix + random_string("") + "\n".join([random_string("") for _ in range(random.randrange(maxrows))])


def random_phone():
    return "+" + "".join(["%s" % random.randint(1, 9) for _ in range(1, 10)])


def random_email(prefix, maxlen=10):
    symbols = string.ascii_lowercase
    suffixes = ["com", "org", "ru", "net"]
    mailbox = prefix + "_" + "".join([random.choice(symbols) for _ in range(random.randrange(1, maxlen))])
    domain = "".join([random.choice(symbols) for _ in range(random.randrange(1, maxlen))])
    return mailbox + "@" + domain + "." + random.choice(suffixes)


def random_homepage(prefix, maxlen=10):
    symbols = string.ascii_lowercase
    suffixes = ["com", "org", "ru", "net"]
    page = prefix + "".join([random.choice(symbols) for _ in range(random.randrange(maxlen) + 1)])
    domain = "".join([random.choice(symbols) for _ in range(random.randrange(maxlen) + 1)])
    return "http://" + page + "." + domain + "." + random.choice(suffixes)

testdata = [
        Contact(first_name="", middle_name="", last_name="", nickname="", title="", company="", address="", home_phone="",
                mobile_phone="", work_phone="", fax="", address2="", secondary_phone="", email="", email2="", email3="",
                homepage="", notes="")
        ] + [
        Contact(first_name=random_string("first name"), middle_name=random_string("middle name"),
                last_name=random_string("last name"), nickname=random_string("nickname"),
                title=random_string("title"),
                company=random_string("company"), address=random_string("address"),
                home_phone=random_phone(),
                mobile_phone=random_phone(), work_phone=random_phone(), fax=random_phone(),
                address2=random_string("address2"), secondary_phone=random_phone(),
                email=random_email("email"),
                email2=random_email("email2"), email3=random_email("email3"),
                homepage=random_homepage("homepage"),
                notes=random_string("notes"))
        for i in range(n)
    ]


def usage():
    usage_text = """
    Usage:

    -f  --outfile (file)    File to save generated test data
    -n  --number (num)      Numbers of rows to generate
    """
    print(usage_text)


if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts=", "outfile="])
    except getopt.GetoptError as err:
        usage()
        sys.exit(2)

    for o, a in opts:
        if o in ("-n", "--number"):
            n = int(a)
        elif o in ("-f", "--outfile"):
            f = a

    outfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

    with open(outfile, "w") as out:
        jsonpickle.set_encoder_options("json", indent=2)
        out.write(jsonpickle.encode(testdata))

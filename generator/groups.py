__author__ = 'nata'

import jsonpickle
import os.path
import getopt
import sys
from model.group import Group
from generator import random_string

n = 3
f = "data/groups.json"

testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header"), footer=random_string("footer"))
    for _ in range(n)]


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

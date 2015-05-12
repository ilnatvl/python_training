__author__ = 'nata'
import string
import random


def random_string(prefix="", maxlen=20, punctuation=False, spaces=False):
    symbols = string.ascii_letters + string.digits
    if punctuation:
        symbols += string.punctuation
    if spaces:
        symbols += " " * 10
    return prefix + " " + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
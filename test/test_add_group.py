# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen=20):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + " " + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header"), footer=random_string("footer"))
    for i in range(5)]

@pytest.mark.parametrize("group", testdata, ids=[str(i) + ":" + repr(x) for i, x in enumerate(testdata)])
def test_add_a_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


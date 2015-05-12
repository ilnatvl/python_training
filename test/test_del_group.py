# -*- coding: utf-8 -*-
__author__ = 'nata'
import random
from model.group import Group, model_to_view


def test_delete_some_group(app, orm, check_ui):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = orm.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = orm.get_group_list()
    old_groups.remove(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(map(model_to_view, new_groups), key=Group.id_or_max) \
            == sorted(app.group.get_group_list(), key=Group.id_or_max)
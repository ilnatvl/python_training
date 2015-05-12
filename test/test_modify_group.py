# -*- coding: utf-8 -*-
__author__ = 'nata'
import random
from model.group import Group, model_to_view
from generator import random_string


def test_modify_some_group(app, orm, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = orm.get_group_list()
    group = random.choice(old_groups)
    new_group = Group(id=group.id, name=random_string("modified"),
                      header=random_string("modified"), footer=random_string("modified"))
    app.group.modify_group_by_id(group.id, new_group)
    new_groups = orm.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups_modified = [new_group if g.id == group.id else g for g in old_groups]
    assert old_groups_modified == new_groups
    if check_ui:
        assert sorted(map(model_to_view, new_groups), key=Group.id_or_max) \
            == sorted(app.group.get_group_list(), key=Group.id_or_max)

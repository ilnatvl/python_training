# -*- coding: utf-8 -*-
from model.group import Group, model_to_view


def test_add_a_group(app, orm, random_groups, check_ui):
    group = random_groups
    old_groups = orm.get_group_list()
    app.group.create(group)
    new_groups = orm.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(map(model_to_view, new_groups), key=Group.id_or_max) \
            == sorted(app.group.get_group_list(), key=Group.id_or_max)


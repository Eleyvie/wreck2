#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""W.R.E.C.K. plugin_test.py

File created by lav on 23.11.15 at 11:25.
Email: alex@lomskih.net
"""

__version__ = "$Revision$"
# $Source$

# DONE #1: plugin should be able to register without importing compiler library
register_plugin()


def plugin_internal_function():
    pass


# DONE #2: plugin should be able to register it's globals, and they should be available in plugin namespace as well
export_plugin_globals(
    plugin_internal_function,
    test_value1 = 10,
    test_value2 = 20,
)

value_must_be_30 = test_value1 + test_value2

# TODO #3: plugin should be able to declare data extensions normally

meshes = [
    ("test_mesh", 0, "test_mesh", 0, 0, 0, 0, 0, 0, 1, 1, 1),
]

# TODO #4: plugin should be able to declare injections the old-fashined way

injections = {
    'dialogs_top': [
        [anyone, "start", [(eq, "$talk_context", test_value1)], "Here you are.", "lco_conversation_end", [(change_screen_view_character)]],
        [anyone, "lco_conversation_end", [], "Nice to know you are not forgetting me!", "close_window", [(assign, "$window_manager_action", value_must_be_30), (assign, "$window_manager_param1", "$window_manager_param2"), (jump_to_menu, "mnu_window_manager"), (change_screen_return)]],
        [anyone, "lco_conversation_end", [], "It's a honor to serve you, {sir/my lady}!", "close_window", [(assign, "$window_manager_action", value_must_be_30), (assign, "$window_manager_param1", "$window_manager_param2"), (jump_to_menu, "mnu_window_manager"), (change_screen_return)]],
    ]
}

# TODO #5: plugin should be able to declare injections in simplified way

with injections:

    dialogs_top = [
        [anyone, "start", [(eq, "$talk_context", test_value1)], "Here you are.", "lco_conversation_end", [(change_screen_view_character)]],
        [anyone, "lco_conversation_end", [], "Nice to know you are not forgetting me!", "close_window", [(assign, "$window_manager_action", value_must_be_30), (assign, "$window_manager_param1", "$window_manager_param2"), (jump_to_menu, "mnu_window_manager"), (change_screen_return)]],
        [anyone, "lco_conversation_end", [], "It's a honor to serve you, {sir/my lady}!", "close_window", [(assign, "$window_manager_action", value_must_be_30), (assign, "$window_manager_param1", "$window_manager_param2"), (jump_to_menu, "mnu_window_manager"), (change_screen_return)]],
    ]

# TODO #6: dynamic entity modification with (relatively) intuitive search qualifiers

dialogs = WRECK.find_first(dlg).insert_before
with WRECK.find_one(skl, [contains('surgery'), 0, eq(entry & sf_inactive, 0)]) as surgery:
    surgery *= [None, None, None, 0]  # First three values are ignored, 4th multiplied by 0, rest ignored
    surgery[3] += 15 # First three values are ignored, 4th increased by 15, rest ignored

"""
  ("player_arrived",
   [
      (assign, ":player_faction_culture", "fac_culture_1"),
      (faction_set_slot, "fac_player_supporters_faction",  slot_faction_culture, ":player_faction_culture"),
      (faction_set_slot, "fac_player_faction",  slot_faction_culture, ":player_faction_culture"),
	]),
"""

myscript = WRECK \
    .find_one(script, [eq('player_arrived')])[1] \
    .find_first([eq(assign), eq(l.player_faction_culture)]) \
    .insert_after([
        (assign, reg99, l.player_faction_culture),
        (display_message, "@DEBUG: plr fac culture = {reg99}")
    ])


# TODO #7: plugin should be able to extend scripting syntax

def new_operation(dest, param1, param2):
    return [
        (store_add, dest, param1, param2),
        (val_add, dest, param2),
    ]
extend_syntax(new_operation)

# TODO #8: plugin should be able to extend scripting syntax in codeless way

with syntax_extension:
    new_operation = [
        (store_add, param(1), param(2), param(3)),
        (val_add, param(1), param(3)),
    ]

# TODO #9: plugin must support preprocessor function

def preprocess_entities():
    pass

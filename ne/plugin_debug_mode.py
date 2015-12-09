from compiler import *
register_plugin()

DISABLED_mission_templates = [
	("camera_test", 0, -1, "Camera Test.", [], [
		(1, 0, 0, [
			(mission_cam_set_mode,1),
			(entry_point_get_position, pos3, 3),
			(mission_cam_set_position, pos3)
		], [
		]),
		(ti_tab_pressed, 0, 0, [
		], [
			(finish_mission,0)
		]),
	]),
]

injection = {
	'menu_start_game_options': [
        ("start_mod", [(key_is_down,key_right_shift),], "Quick Character (for mod testing)", [
            (troop_raise_attribute, "trp_player",ca_strength, 40),
            (troop_raise_skill, "trp_player","skl_power_draw", 10),
            (troop_raise_skill, "trp_player","skl_power_throw", 10),
            (troop_raise_skill, "trp_player","skl_shield", 10),
            (troop_raise_skill, "trp_player","skl_riding", 10),
            (troop_add_gold, "trp_player", 2000000),
            (change_screen_map),
        ])
	],
	'menu_start_game_final_options': [
      # LAV DEBUG HACK!
      (try_begin),
        (key_is_down, key_right_shift),
        (set_show_messages, 0),
        (troop_add_gold, "trp_player", 2000000),
        (troop_set_slot, "trp_player", slot_troop_renown, 5000),
        (call_script, "script_change_player_honor", 100),
        #(add_xp_to_troop, 30000, "trp_player"),
        (add_xp_to_troop, 30000, "trp_npc1"),
        (add_xp_to_troop, 30000, "trp_npc2"),
        (add_xp_to_troop, 30000, "trp_npc3"),
        (add_xp_to_troop, 30000, "trp_npc4"),
        (add_xp_to_troop, 30000, "trp_npc5"),
        (add_xp_to_troop, 30000, "trp_npc6"),
        (add_xp_to_troop, 30000, "trp_npc7"),
        (add_xp_to_troop, 30000, "trp_npc8"),
        (add_xp_to_troop, 30000, "trp_npc9"),
        (add_xp_to_troop, 30000, "trp_npc10"),
        (add_xp_to_troop, 30000, "trp_npc11"),
        (add_xp_to_troop, 30000, "trp_npc12"),
        (add_xp_to_troop, 30000, "trp_npc13"),
        (add_xp_to_troop, 30000, "trp_npc14"),
        (add_xp_to_troop, 30000, "trp_npc15"),
        (add_xp_to_troop, 30000, "trp_npc16"),
        (call_script, "script_recruit_troop_as_companion", "trp_npc1"),
        (call_script, "script_recruit_troop_as_companion", "trp_npc2"),
        (call_script, "script_recruit_troop_as_companion", "trp_npc3"),
        (call_script, "script_recruit_troop_as_companion", "trp_npc4"),
        (call_script, "script_recruit_troop_as_companion", "trp_npc5"),
        (call_script, "script_recruit_troop_as_companion", "trp_npc6"),
        (call_script, "script_recruit_troop_as_companion", "trp_npc7"),
        (call_script, "script_recruit_troop_as_companion", "trp_npc8"),
        (call_script, "script_recruit_troop_as_companion", "trp_npc9"),
        (call_script, "script_recruit_troop_as_companion", "trp_npc10"),
        (call_script, "script_recruit_troop_as_companion", "trp_npc11"),
        (call_script, "script_recruit_troop_as_companion", "trp_npc12"),
        (call_script, "script_recruit_troop_as_companion", "trp_npc13"),
        (call_script, "script_recruit_troop_as_companion", "trp_npc14"),
        (call_script, "script_recruit_troop_as_companion", "trp_npc15"),
        (call_script, "script_recruit_troop_as_companion", "trp_npc16"),
        (set_show_messages, 1),
        (display_message, "@You are a filthy cheater!", 0xFF0000),
      (try_end),
	]
}

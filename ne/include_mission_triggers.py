from compiler import *

# Contains various definitions for mission templates so they don't have to be redefined all over the place.
# This file is included from module_mission_templates and various plugins.

pilgrim_disguise = [itm.pilgrim_hood,itm.pilgrim_disguise,itm.practice_staff, itm.throwing_daggers]
af_castle_lord = af_override_horse | af_override_weapons| af_require_civilian



lav_situational_damage_modifiers = (ti_on_agent_hit, 0, 0, [], [
    (store_trigger_param_3, reg3), # Damage amount
    (try_begin),
        (gt, reg3, 0),
        (store_trigger_param_1, reg1), # Agent receiving damage
        (agent_is_human, reg1),
        (agent_get_troop_id, reg2, reg1),
        (store_skill_level, reg4, "skl_ironflesh", reg2),
        (gt, reg4, 0),
        (val_sub, reg3, reg4),
        (val_max, reg3, 0),
    (try_end),
    (set_trigger_result, reg3),
])

lav_replace_horse_props_with_spawn_markers = (ti_before_mission_start, 0, 0, [], [
    (try_for_range, l.horse_id, itm.arabian_horse_a, itm.warhorse + 1),
        (replace_scene_items_with_scene_props, l.horse_id, spr.spawn_marker),
        (try_for_prop_instances, l.instance_id, spr.spawn_marker),
            (scene_prop_slot_eq, l.instance_id, slot_spawn_object_type, 0),
            (scene_prop_set_slot, l.instance_id, slot_spawn_object_type, ldop_horse),
            (scene_prop_set_slot, l.instance_id, slot_spawn_object_id, l.horse_id),
        (try_end),
    (try_end),
])

lav_activate_spawn_markers = (ti_after_mission_start, 0, 0, [], [
    (try_for_prop_instances, l.instance_id, spr.spawn_marker),
        (scene_prop_slot_eq, l.instance_id, slot_spawn_object_type, ldop_agent),
        (scene_prop_get_slot, l.object_id, l.instance_id, slot_spawn_object_id),
        (prop_instance_get_position, pos127, l.instance_id),
        (set_spawn_position, pos127),
        (spawn_agent, l.object_id, imod_plain),
        # TODO: determine what to do with this agent (predefined animations etc). For now will just stand at starting position.
        (agent_set_scripted_destination, reg0, pos127, 1),
    (else_try),
        (scene_prop_slot_eq, l.instance_id, slot_spawn_object_type, ldop_horse),
        (scene_prop_get_slot, l.object_id, l.instance_id, slot_spawn_object_id),
        (prop_instance_get_position, pos127, l.instance_id),
        (set_spawn_position, pos127),
        (spawn_horse, l.object_id, imod_plain),
        (agent_set_scripted_destination, reg0, pos127, 1),
    (else_try),
        (scene_prop_slot_eq, l.instance_id, slot_spawn_object_type, ldop_item),
        (scene_prop_get_slot, l.object_id, l.instance_id, slot_spawn_object_id),
        (prop_instance_get_position, pos127, l.instance_id),
        (set_spawn_position, pos127),
        (spawn_item, l.object_id, imod_plain, 0), # Spawn plain item with pruning turned off
    (try_end),
])



common_battle_mission_start = (
  ti_before_mission_start, 0, 0, [],
  [
    (team_set_relation, 0, 2, 1),
    (team_set_relation, 1, 3, 1),
    (call_script, "script_change_banners_and_chest"),
    ])

common_battle_tab_press = (
  ti_tab_pressed, 0, 0, [],
  [
    (try_begin),
      (eq, "$g_battle_won", 1),
      (call_script, "script_count_mission_casualties_from_agents"),
      (finish_mission,0),
    (else_try),
	# NE cam
      # (call_script, "script_cf_check_enemies_nearby"),
      (question_box,"str_do_you_want_to_retreat"),
    # (else_try),
      # (display_message,"str_can_not_retreat"),
	 # NE End cam
    (try_end),
    ])
# OVERRIDE FOR NEW DEATHCAM:
common_battle_tab_press = (
    ti_tab_pressed, 0, 0, [],
    [
        (try_begin),
            (eq, "$g_battle_won", 1),
            (call_script, "script_count_mission_casualties_from_agents"),
            (finish_mission, 0),
        (else_try),
            (eq, "$pin_player_fallen", 1),
            (call_script, "script_simulate_retreat", 0, 0, 0),
            (assign, "$g_battle_result", -1),
            (set_mission_result, -1),
            (call_script, "script_count_mission_casualties_from_agents"),
            (finish_mission, 0),
        (else_try),
            (eq, "$deathcam_on", 1),
            (question_box,"str_do_you_want_to_retreat"),
        (else_try),
            (call_script, "script_cf_check_enemies_nearby"),
            (question_box,"str_do_you_want_to_retreat"),
        (else_try),
            (display_message,"str_can_not_retreat"),
        (try_end),
    ]
)

common_battle_init_banner = (
  ti_on_agent_spawn, 0, 0, [],
  [
    (store_trigger_param_1, ":agent_no"),
    (agent_get_troop_id, ":troop_no", ":agent_no"),
    (call_script, "script_troop_agent_set_banner", "tableau_game_troop_label_banner", ":agent_no", ":troop_no"),
  ])


common_arena_fight_tab_press = (
  ti_tab_pressed, 0, 0, [],
  [
    (question_box,"str_give_up_fight"),
    ])

# common_battle_victory_display = (
  # 10, 0, 0, [],
  # [
    # (eq,"$g_battle_won",1),
    # (display_message,"str_msg_battle_won"),
    # ])

# NE building
## Refill arrows - Jinnai
common_siege_refill_arrows = (
   60.0, 0, 0, [(party_slot_eq, "$g_encountered_party", slot_center_has_blacksmith, 1),], [
      (try_for_agents,":agent"),
         (agent_is_alive,":agent"),
         (agent_is_human,":agent"),
         (agent_get_team,":team",":agent"),
         (this_or_next|eq,":team","$defender_team"),
         (eq,":team","$defender_team_2"),
         (agent_refill_ammo,":agent"),
      (end_try),
   ])
# Ne end building	
	
	
common_siege_question_answered = (
  ti_question_answered, 0, 0, [],
   [
     (store_trigger_param_1,":answer"),
     (eq,":answer",0),
	 # NE camera
	      (try_begin),  ## Fixing it so the player is handled correctly if knocked out - Jinnai
       (main_hero_fallen),
       (assign, "$g_battle_result", -1),
       (set_mission_result,-1),
       (assign, "$pin_player_fallen", 1),
     (else_try),
     # ne end 
     (assign, "$pin_player_fallen", 0),
	 # NE camera
	 (try_end), 
     # ne end
     (get_player_agent_no, ":player_agent"),
     (agent_get_team, ":agent_team", ":player_agent"),
     (try_begin),
       (neq, "$attacker_team", ":agent_team"),
       (neq, "$attacker_team_2", ":agent_team"),
       (str_store_string, s5, "str_siege_continues"),
       (call_script, "script_simulate_retreat", 8, 15, 0),
     (else_try),
       (str_store_string, s5, "str_retreat"),
       (call_script, "script_simulate_retreat", 5, 20, 0),
     (try_end),
     (call_script, "script_count_mission_casualties_from_agents"),
     (finish_mission,0),
     ])

common_siege_init = (
  0, 0, ti_once, [],
  [
    (assign,"$g_battle_won",0),
    (assign,"$defender_reinforcement_stage",0),
    (assign,"$attacker_reinforcement_stage",0),
    (call_script, "script_music_set_situation_with_culture", mtf_sit_siege),
    ])

common_music_situation_update = (
  30, 0, 0, [],
  [
    (call_script, "script_combat_music_set_situation_with_culture"),
    ])

common_siege_ai_trigger_init = (
  0, 0, ti_once,
  [
    (assign, "$defender_team", 0),
    (assign, "$attacker_team", 1),
    (assign, "$defender_team_2", 2),
    (assign, "$attacker_team_2", 3),
    ], [])

common_siege_ai_trigger_init_2 = (
  0, 0, ti_once,
  [
    (set_show_messages, 0),
    (entry_point_get_position, pos10, 10),
    (try_for_range, ":cur_group", 0, grc_everyone),
      (neq, ":cur_group", grc_archers),
      (team_give_order, "$defender_team", ":cur_group", mordr_hold),
      (team_give_order, "$defender_team", ":cur_group", mordr_stand_closer),
      (team_give_order, "$defender_team", ":cur_group", mordr_stand_closer),
      (team_give_order, "$defender_team_2", ":cur_group", mordr_hold),
      (team_give_order, "$defender_team_2", ":cur_group", mordr_stand_closer),
      (team_give_order, "$defender_team_2", ":cur_group", mordr_stand_closer),
    (try_end),
    (team_give_order, "$defender_team", grc_archers, mordr_stand_ground),
    (team_set_order_position, "$defender_team", grc_everyone, pos10),
    (team_give_order, "$defender_team_2", grc_archers, mordr_stand_ground),
    (team_set_order_position, "$defender_team_2", grc_everyone, pos10),
    (set_show_messages, 1),
    ], [])

common_siege_ai_trigger_init_after_2_secs = (
  0, 2, ti_once, [],
  [
    (try_for_agents, ":agent_no"),
      (agent_set_slot, ":agent_no", slot_agent_is_not_reinforcement, 1),
    (try_end),
    ])

common_siege_defender_reinforcement_check = (
  3, 0, 5, [],
  [(lt, "$defender_reinforcement_stage", 7),
   (store_mission_timer_a,":mission_time"),
   (ge,":mission_time",10),
   (store_normalized_team_count,":num_defenders",0),
   (lt,":num_defenders",8),
   (add_reinforcements_to_entry,4, 7),
   (val_add,"$defender_reinforcement_stage",1),
   (try_begin),
     (gt, ":mission_time", 300), #5 minutes, don't let small armies charge
     (get_player_agent_no, ":player_agent"),
     (agent_get_team, ":player_team", ":player_agent"),
     (neq, ":player_team", "$defender_team"), #player should be the attacker
     (neq, ":player_team", "$defender_team_2"), #player should be the attacker
     (ge, "$defender_reinforcement_stage", 2),
     (set_show_messages, 0),
     (team_give_order, "$defender_team", grc_infantry, mordr_charge), #AI desperate charge:infantry!!!
     (team_give_order, "$defender_team_2", grc_infantry, mordr_charge), #AI desperate charge:infantry!!!
     (team_give_order, "$defender_team", grc_cavalry, mordr_charge), #AI desperate charge:cavalry!!!
     (team_give_order, "$defender_team_2", grc_cavalry, mordr_charge), #AI desperate charge:cavalry!!!
     (set_show_messages, 1),
     (ge, "$defender_reinforcement_stage", 4),
     (set_show_messages, 0),
     (team_give_order, "$defender_team", grc_everyone, mordr_charge), #AI desperate charge: everyone!!!
     (team_give_order, "$defender_team_2", grc_everyone, mordr_charge), #AI desperate charge: everyone!!!
     (set_show_messages, 1),
   (try_end),
   ])

common_siege_defender_reinforcement_archer_reposition = (
  2, 0, 0,
  [
    (gt, "$defender_reinforcement_stage", 0),
    ],
  [
    (call_script, "script_siege_move_archers_to_archer_positions"),
    ])

common_siege_attacker_reinforcement_check = (
  1, 0, 5,
  [
    (lt,"$attacker_reinforcement_stage",5),
    (store_mission_timer_a,":mission_time"),
    (ge,":mission_time",10),
    (store_normalized_team_count,":num_attackers",1),
    (lt,":num_attackers",6)
    ],
  [
    (add_reinforcements_to_entry, 1, 8),
    (val_add,"$attacker_reinforcement_stage", 1),
    ])

common_siege_attacker_do_not_stall = (
  5, 0, 0, [],
  [ #Make sure attackers do not stall on the ladders...
    (try_for_agents, ":agent_no"),
      (agent_is_human, ":agent_no"),
      (agent_is_alive, ":agent_no"),
      (agent_get_team, ":agent_team", ":agent_no"),
      (this_or_next|eq, ":agent_team", "$attacker_team"),
      (eq, ":agent_team", "$attacker_team_2"),
      (agent_ai_set_always_attack_in_melee, ":agent_no", 1),
    (try_end),
    ])

common_battle_check_friendly_kills = (
  2, 0, 0, [],
  [
    (call_script, "script_check_friendly_kills"),
    ])

common_battle_check_victory_condition = (
  1, 60, ti_once,
  [
    (store_mission_timer_a,reg(1)),
    (ge,reg(1),10),
    (all_enemies_defeated, 5),
	# ne cam
    # (neg|main_hero_fallen, 0),
	# end ne cam
    (set_mission_result,1),
    (display_message,"str_msg_battle_won"),
    (assign,"$g_battle_won",1),
    (assign, "$g_battle_result", 1),
    (call_script, "script_play_victorious_sound"),
    ],
  [
    (call_script, "script_count_mission_casualties_from_agents"),
    (finish_mission, 1),
    ])

common_battle_victory_display = (
  10, 0, 0, [],
  [
    (eq,"$g_battle_won",1),
    (display_message,"str_msg_battle_won"),
    ])

common_siege_refill_ammo = (
  120, 0, 0, [],
  [#refill ammo of defenders every two minutes.
    (get_player_agent_no, ":player_agent"),
    (try_for_agents,":cur_agent"),
      (neq, ":cur_agent", ":player_agent"),
      (agent_is_alive, ":cur_agent"),
      (agent_is_human, ":cur_agent"),
##      (agent_is_defender, ":cur_agent"),
      (agent_get_team, ":agent_team", ":cur_agent"),
      (this_or_next|eq, ":agent_team", "$defender_team"),
      (eq, ":agent_team", "$defender_team_2"),
      (agent_refill_ammo, ":cur_agent"),
    (try_end),
    ])

common_siege_check_defeat_condition = (
  1, 4, ti_once,
  [
    (main_hero_fallen)
    ],
  [
  # NE cam 
  # Commenting this out so the battle continues - Jinnai
    # (assign, "$pin_player_fallen", 1),
    # (get_player_agent_no, ":player_agent"),
    # (agent_get_team, ":agent_team", ":player_agent"),
    # (try_begin),
      # (neq, "$attacker_team", ":agent_team"),
      # (neq, "$attacker_team_2", ":agent_team"),
      # (str_store_string, s5, "str_siege_continues"),
      # (call_script, "script_simulate_retreat", 8, 15, 0),
    # (else_try),
      # (str_store_string, s5, "str_retreat"),
      # (call_script, "script_simulate_retreat", 5, 20, 0),
    # (try_end),
    # (assign, "$g_battle_result", -1),
    # (set_mission_result,-1),
    # (call_script, "script_count_mission_casualties_from_agents"),
    # (finish_mission,0),
    ])
# OVERRIDE FOR NEW DEATHCAM:
common_siege_check_defeat_condition = (
    1, 4, ti_once,
    [
        (main_hero_fallen),
        (assign, ":pteam_alive", 0), 
        (try_for_agents, ":agent"), #Check players team is dead
        (neq, ":pteam_alive", 1), #Break loop
        (agent_is_ally, ":agent"),
        (agent_is_alive, ":agent"),
            (assign, ":pteam_alive", 1),
        (try_end),
        (eq, ":pteam_alive", 0),
    ],
    [
        (assign, "$pin_player_fallen", 1),
        (display_message, "@Press TAB to end the battle."),
    ]
)

common_battle_order_panel = (
  0, 0, 0, [],
  [
    (game_key_clicked, gk_view_orders),
    (neg|is_presentation_active, "prsnt_battle"),
    (start_presentation, "prsnt_battle"),
    ])

common_battle_order_panel_tick = (
  0.1, 0, 0, [],
  [
    (is_presentation_active, "prsnt_battle"),
    (call_script, "script_update_order_panel_statistics_and_map"),
    ])

common_battle_inventory = (
  ti_inventory_key_pressed, 0, 0, [],
  [
    (display_message,"str_use_baggage_for_inventory"),
    ])

common_inventory_not_available = (
  ti_inventory_key_pressed, 0, 0,
  [
    (display_message, "str_cant_use_inventory_now"),
    ], [])

common_siege_init_ai_and_belfry = (
  0, 0, ti_once,
  [
    (call_script, "script_siege_init_ai_and_belfry"),
    ], [])

common_siege_move_belfry = (
  0, 0, ti_once,
  [
    (call_script, "script_cf_siege_move_belfry"),
    ], [])

common_siege_rotate_belfry = (
  0, 2, ti_once,
  [
    (call_script, "script_cf_siege_rotate_belfry_platform"),
    ],
  [
    (assign, "$belfry_positioned", 3),
    ])

common_siege_assign_men_to_belfry = (
  0, 0, ti_once,
  [
    (call_script, "script_cf_siege_assign_men_to_belfry"),
    ], [])


# NE cam
	
	
# Freestyle camera by Zephilinox/MadVader

common_init_deathcam = (
   0, 0, ti_once,
   [],
   [
        (assign, "$deathcam_on", 0),
        (assign, "$deathcam_death_pos_x", 0),
        (assign, "$deathcam_death_pos_y", 0),
        (assign, "$deathcam_death_pos_z", 0),
        
        (assign, "$deathcam_mouse_last_x", 5000), 
        (assign, "$deathcam_mouse_last_y", 3750),
        
        (assign, "$deathcam_mouse_last_notmoved_x", 5000),
        (assign, "$deathcam_mouse_last_notmoved_y", 3750),
        (assign, "$deathcam_mouse_notmoved_x", 5000), #Center screen (10k fixed pos)
        (assign, "$deathcam_mouse_notmoved_y", 3750),
        (assign, "$deathcam_mouse_notmoved_counter", 0),
        
        (assign, "$deathcam_total_rotx", 0),
        
        (assign, "$deathcam_sensitivity_x", 400), #4:3 ratio may be best
        (assign, "$deathcam_sensitivity_y", 300), #If modified, change values in common_move_deathcam
        
        (assign, "$deathcam_prsnt_was_active", 0),
   ]
)
common_start_deathcam = (
    0, 1, ti_once, #1 second delay before the camera activates
    [
        (main_hero_fallen),
        (eq, "$deathcam_on", 0),
    ],
    [
        (set_fixed_point_multiplier, 10000),
        (assign, "$deathcam_on", 1),
        
        (display_message, "@You were defeated.", 0xFF2222),
        (display_message, "@Rotate with the mouse, move with standard keys."),
        (display_message, "@Shift/Control for Up/Down, Space Bar to increase speed."),
        (display_message, "@Numpad Plus/Minus to change sensitivity, Home to reset position, End to switch Y-inversion mode."),

        (mission_cam_get_position, pos1), #Death pos
        (position_get_x, reg3, pos1),
        (position_get_y, reg4, pos1),
        (position_get_z, reg5, pos1),
        (assign, "$deathcam_death_pos_x", reg3),
        (assign, "$deathcam_death_pos_y", reg4),
        (assign, "$deathcam_death_pos_z", reg5),
        (position_get_rotation_around_z, ":rot_z", pos1),
        
        (init_position, pos47),
        (position_copy_origin, pos47, pos1), #Copy X,Y,Z pos
        (position_rotate_z, pos47, ":rot_z"), #Copying X-Rotation is likely possible, but I haven't figured it out yet
        
        (mission_cam_set_mode, 1, 0, 0), #Manual?

        (mission_cam_set_position, pos47),
        
        #(team_give_order, 0, grc_everyone, mordr_charge),
        #(team_give_order, 1, grc_everyone, mordr_charge),
        #(team_give_order, 2, grc_everyone, mordr_charge),
        #(team_give_order, 3, grc_everyone, mordr_charge),
   ]
)
manual_start_deathcam = (
    0, 0, 0,
    [
        (key_clicked, key_f12),
        (eq, "$deathcam_on", 0),
    ],
    [
        (set_fixed_point_multiplier, 10000),
        (assign, "$deathcam_on", 1),
        
        (display_message, "@You were defeated.", 0xFF2222),
        (display_message, "@Rotate with the mouse, move with standard keys."),
        (display_message, "@Shift/Control for Up/Down, Space Bar to increase speed."),
        (display_message, "@Numpad Plus/Minus to change sensitivity, Home to reset position, End to switch Y-inversion mode."),

        (mission_cam_get_position, pos1), #Death pos
        (position_get_x, reg3, pos1),
        (position_get_y, reg4, pos1),
        (position_get_z, reg5, pos1),
        (assign, "$deathcam_death_pos_x", reg3),
        (assign, "$deathcam_death_pos_y", reg4),
        (assign, "$deathcam_death_pos_z", reg5),
        (position_get_rotation_around_z, ":rot_z", pos1),
        
        (init_position, pos47),
        (position_copy_origin, pos47, pos1), #Copy X,Y,Z pos
        (position_rotate_z, pos47, ":rot_z"), #Copying X-Rotation is likely possible, but I haven't figured it out yet
        
        (mission_cam_set_mode, 1, 0, 0), #Manual?

        (mission_cam_set_position, pos47),
   ]
)
common_move_deathcam = (
    0, 0, 0,
    [
        (eq, "$deathcam_on", 1),
        (this_or_next|game_key_is_down, gk_move_forward),
        (this_or_next|game_key_is_down, gk_move_backward),
        (this_or_next|game_key_is_down, gk_move_left),
        (this_or_next|game_key_is_down, gk_move_right),
        (this_or_next|key_is_down, key_left_shift),
        (this_or_next|key_is_down, key_left_control),
        (this_or_next|key_is_down, key_numpad_minus),
        (this_or_next|key_is_down, key_numpad_plus),
        (this_or_next|key_clicked, key_home),
        (key_clicked, key_end),
    ],
    [   
        (set_fixed_point_multiplier, 10000),
        (mission_cam_get_position, pos47),
        
        (try_begin),
        (key_clicked, key_home),
            (position_set_x, pos47, "$deathcam_death_pos_x"),
            (position_set_y, pos47, "$deathcam_death_pos_y"),
            (position_set_z, pos47, "$deathcam_death_pos_z"),
        (try_end),
        (try_begin),
            (key_clicked, key_end),
            (try_begin),
                (eq, "$deathcam_invert_y", 1),
                (assign, "$deathcam_invert_y", 0),
                (display_message, "@Deathcam Y-inversion mode off."),
            (else_try),
                (assign, "$deathcam_invert_y", 1),
                (display_message, "@Deathcam Y-inversion mode on."),
            (try_end),
        (try_end),

        (assign, ":move_x", 0),
        (assign, ":move_y", 0),
        (assign, ":move_z", 0),
        
        (try_begin),
        (game_key_is_down, gk_move_forward),
            (val_add, ":move_y", 10),
        (try_end),
        (try_begin),
        (game_key_is_down, gk_move_backward),      
            (val_add, ":move_y", -10),
        (try_end),

        (try_begin),
        (game_key_is_down, gk_move_right),      
            (val_add, ":move_x", 10), 
        (try_end),
        (try_begin),
        (game_key_is_down, gk_move_left),      
            (val_add, ":move_x", -10),
        (try_end),

        (try_begin),
        (key_is_down, key_left_shift),
            (val_add, ":move_z", 10),
        (try_end),
        (try_begin),
        (key_is_down, key_left_control),
            (val_add, ":move_z", -10),
        (try_end),
        
        (try_begin),
        (key_is_down, key_space),
            (val_mul, ":move_x", 4),
            (val_mul, ":move_y", 4),
            (val_mul, ":move_z", 2),
        (try_end),
        
        (position_move_x, pos47, ":move_x"),
        (position_move_y, pos47, ":move_y"),
        (position_move_z, pos47, ":move_z"),
        
        (mission_cam_set_position, pos47),
        
        (try_begin),
        (key_is_down, key_numpad_minus),
        (ge, "$deathcam_sensitivity_x", 4), #Negative check.
        (ge, "$deathcam_sensitivity_y", 3),
            (val_sub, "$deathcam_sensitivity_x", 4),
            (val_sub, "$deathcam_sensitivity_y", 3),
            (store_mod, reg6, "$deathcam_sensitivity_x", 100), #25% increments
            (store_mod, reg7, "$deathcam_sensitivity_y", 75),
            (try_begin),
            (eq, reg6, 0),
            (eq, reg7, 0),
                (assign, reg8, "$deathcam_sensitivity_x"),
                (assign, reg9, "$deathcam_sensitivity_y"),
                (display_message, "@Sensitivity - 25% ({reg8}, {reg9})"),
            (try_end),
        (else_try),
        (key_is_down, key_numpad_plus),
            (val_add, "$deathcam_sensitivity_x", 4),
            (val_add, "$deathcam_sensitivity_y", 3),
            (store_mod, reg6, "$deathcam_sensitivity_x", 100), #25% increments
            (store_mod, reg7, "$deathcam_sensitivity_y", 75),
            (try_begin),
            (eq, reg6, 0),
            (eq, reg7, 0),
                (assign, reg8, "$deathcam_sensitivity_x"),
                (assign, reg9, "$deathcam_sensitivity_y"),
                (display_message, "@Sensitivity + 25% ({reg8}, {reg9})"),
            (try_end),
        (try_end),
   ]
)
common_rotate_deathcam = (
    0, 0, 0,
    [
        (eq, "$deathcam_on", 1),
    ],
    [
        (set_fixed_point_multiplier, 10000), #Extra Precision
        
        (try_begin),
        (this_or_next|is_presentation_active, "prsnt_battle"), #Opened (mouse must move)
        (this_or_next|key_clicked, key_escape), #Menu
        (this_or_next|key_clicked, key_q), #Notes, etc
        (key_clicked, key_tab), #Retreat
        (eq, "$deathcam_prsnt_was_active", 0),
            (assign, "$deathcam_prsnt_was_active", 1),
            (assign, "$deathcam_mouse_last_notmoved_x", "$deathcam_mouse_notmoved_x"),
            (assign, "$deathcam_mouse_last_notmoved_y", "$deathcam_mouse_notmoved_y"),
        (try_end),
        
        (neg|is_presentation_active, "prsnt_battle"),
        
        (mouse_get_position, pos1), #Get and set mouse position
        (position_get_x, reg1, pos1),
        (position_get_y, reg2, pos1),
        
        (mission_cam_get_position, pos47),
        
        (assign, ":continue", 0),
        
        (try_begin),
        (neq, "$deathcam_prsnt_was_active", 1),
            (try_begin), #Check not moved
            (eq, reg1, "$deathcam_mouse_last_x"),
            (eq, reg2, "$deathcam_mouse_last_y"),
            (this_or_next|neq, reg1, "$deathcam_mouse_notmoved_x"),
            (neq, reg2, "$deathcam_mouse_notmoved_y"),
                (val_add, "$deathcam_mouse_notmoved_counter", 1),
                (try_begin), #Notmoved for n cycles
                (ge, "$deathcam_mouse_notmoved_counter", 15),
                    (assign, "$deathcam_mouse_notmoved_counter", 0),
                    (assign, "$deathcam_mouse_notmoved_x", reg1),
                    (assign, "$deathcam_mouse_notmoved_y", reg2),
                (try_end),
            (else_try), #Has moved
                (assign, ":continue", 1),
                (assign, "$deathcam_mouse_notmoved_counter", 0),
            (try_end),
            (assign, "$deathcam_mouse_last_x", reg1), #Next cycle, this pos = last pos
            (assign, "$deathcam_mouse_last_y", reg2),
        (else_try), #prsnt was active
            (try_begin),
            (neq, reg1, "$deathcam_mouse_last_x"), #Is moving
            (neq, reg2, "$deathcam_mouse_last_y"),
                (store_sub, ":delta_x2", reg1, "$deathcam_mouse_last_notmoved_x"), #Store pos difference
                (store_sub, ":delta_y2", reg2, "$deathcam_mouse_last_notmoved_y"),
            (is_between, ":delta_x2", -10, 11), #when engine recenters mouse, there is a small gap
            (is_between, ":delta_y2", -10, 11), #usually 5 pixels, but did 10 to be safe.
                (assign, "$deathcam_prsnt_was_active", 0),
                (assign, "$deathcam_mouse_notmoved_x", "$deathcam_mouse_last_notmoved_x"),
                (assign, "$deathcam_mouse_notmoved_y", "$deathcam_mouse_last_notmoved_y"),
            (else_try),
                (assign, "$deathcam_mouse_notmoved_x", reg1),
                (assign, "$deathcam_mouse_notmoved_y", reg2),
            (try_end),
                (assign, "$deathcam_mouse_last_x", reg1), #Next cycle, this pos = last pos
                (assign, "$deathcam_mouse_last_y", reg2),
        (try_end),
        
        (eq, ":continue", 1), #Else exit
            
        (store_sub, ":delta_x", reg1, "$deathcam_mouse_notmoved_x"), #Store pos difference
        (store_sub, ":delta_y", reg2, "$deathcam_mouse_notmoved_y"),

        (val_mul, ":delta_x", "$deathcam_sensitivity_x"),
        (val_mul, ":delta_y", "$deathcam_sensitivity_y"),
        (try_begin),
            (eq, "$deathcam_invert_y", 1),
            (val_mul, ":delta_y", -1),
        (try_end),
        (val_clamp, ":delta_x", -80000, 80001), #8
        (val_clamp, ":delta_y", -60000, 60001), #6
            
        (store_mul, ":neg_rotx", "$deathcam_total_rotx", -1),
        (position_rotate_x_floating, pos47, ":neg_rotx"), #Reset x axis to initial state
        
        (position_rotate_y, pos47, 90), #Barrel roll by 90 degrees to inverse x/z axis
        (position_rotate_x_floating, pos47, ":delta_x"), #Rotate simulated z axis, Horizontal
        (position_rotate_y, pos47, -90), #Reverse
        
        (position_rotate_x_floating, pos47, "$deathcam_total_rotx"), #Reverse
        
        (position_rotate_x_floating, pos47, ":delta_y"), #Vertical
        (val_add, "$deathcam_total_rotx", ":delta_y"), #Fix yaw
        
        (mission_cam_set_position, pos47),
    ]
)


## Allow the camera view to move after player death - Jinnai
camera_trigger_1 = (ti_before_mission_start, 0, 0, [], [(assign,"$camera_mode",0)])

camera_trigger_2 = (0, 0, 1, [(main_hero_fallen),(game_key_clicked, gk_jump)],[
        (try_begin),
          (eq,"$camera_mode",0),
          (assign,"$camera_mode",1),
          (set_fixed_point_multiplier, 100),
          (assign,"$camera_height",250),
          (mission_cam_set_mode, 1),
          (mission_cam_get_position, pos1),
          (position_get_rotation_around_z,":rot",pos1),
          (init_position,pos2),
          (position_copy_origin,pos2,pos1),
          (position_rotate_z,pos2,":rot"),
          (position_rotate_x,pos2,-5),
          (position_set_z_to_ground_level, pos2),
          (position_move_z,pos2,"$camera_height"),
          (mission_cam_set_position, pos2),
          (mission_cam_set_aperture, 97),
        (else_try),
          (assign,"$camera_mode",0),
          (mission_cam_set_mode, 0, 1000, 0),
        (try_end),
        ])

camera_trigger_3 = (0, 0, 0, [(main_hero_fallen),(game_key_is_down, gk_move_forward),(eq,"$camera_mode",1)],[
        (set_fixed_point_multiplier, 100),
        (mission_cam_get_position, pos1),
        (position_rotate_x,pos1,5),
        (position_get_rotation_around_z,":rot",pos1),
        (store_sin,":move_x",":rot"),
        (store_cos,":move_y",":rot"),
        (try_begin),
          (game_key_is_down, gk_zoom),
          (val_mul,":move_x",1),
          (val_mul,":move_y",1),
        (else_try),
          (val_div,":move_x",10),
          (val_div,":move_y",10),
        (try_end),
        (position_move_x,pos1,":move_x"),
        (position_move_y,pos1,":move_y"),
        (position_set_z_to_ground_level, pos1),
        (position_move_z,pos1,"$camera_height"),
        (position_rotate_x,pos1,-5),
        (mission_cam_animate_to_position, pos1, 10, 0),
        ])

camera_trigger_4 = (0, 0, 0, [(main_hero_fallen),(game_key_is_down, gk_move_backward),(eq,"$camera_mode",1)],[
        (set_fixed_point_multiplier, 100),
        (mission_cam_get_position, pos1),
        (position_rotate_x,pos1,5),
        (position_get_rotation_around_z,":rot",pos1),
        (store_sin,":move_x",":rot"),
        (store_cos,":move_y",":rot"),
        (try_begin),
          (game_key_is_down, gk_zoom),
          (val_mul,":move_x",-1),
          (val_mul,":move_y",-1),
        (else_try),
          (val_div,":move_x",-10),
          (val_div,":move_y",-10),
        (try_end),
        (position_move_x,pos1,":move_x"),
        (position_move_y,pos1,":move_y"),
        (position_set_z_to_ground_level, pos1),
        (position_move_z,pos1,"$camera_height"),
        (position_rotate_x,pos1,-5),
        (mission_cam_animate_to_position, pos1, 10, 0),
        ])

camera_trigger_5 = (0, 0, 0, [(main_hero_fallen),(game_key_is_down, gk_move_right),(eq,"$camera_mode",1)],[
        (set_fixed_point_multiplier, 100),
        (mission_cam_get_position, pos1),
        (position_rotate_x,pos1,5),
        (try_begin),
          (game_key_is_down, gk_zoom),
          (position_rotate_z,pos1,-4),
        (else_try),
          (position_rotate_z,pos1,-2),
        (try_end),
        (position_rotate_x,pos1,-5),
        (mission_cam_animate_to_position, pos1, 10, 0),
        ])

camera_trigger_6 = (0, 0, 0, [(main_hero_fallen),(game_key_is_down, gk_move_left),(eq,"$camera_mode",1)],[
        (set_fixed_point_multiplier, 100),
        (mission_cam_get_position, pos1),
        (position_rotate_x,pos1,5),
        (try_begin),
          (game_key_is_down, gk_zoom),
          (position_rotate_z,pos1,4),
        (else_try),
          (position_rotate_z,pos1,2),
        (try_end),
        (position_rotate_x,pos1,-5),
        (mission_cam_animate_to_position, pos1, 10, 0),
        ])

camera_trigger_7 = (0, 0, 0, [(main_hero_fallen),(game_key_is_down, gk_attack),(eq,"$camera_mode",1)],[
        (set_fixed_point_multiplier, 100),
        (mission_cam_get_position, pos1),
        (position_rotate_x,pos1,5),
        (val_add,"$camera_height",10),
        (val_min,"$camera_height",800),
        (position_set_z_to_ground_level, pos1),
        (position_move_z,pos1,"$camera_height"),
        (position_rotate_x,pos1,-5),
        (mission_cam_animate_to_position, pos1, 10, 0),
        ])

camera_trigger_8 = (0, 0, 0, [(main_hero_fallen),(game_key_is_down, gk_defend),(eq,"$camera_mode",1)],[
        (set_fixed_point_multiplier, 100),
        (mission_cam_get_position, pos1),
        (position_rotate_x,pos1,5),
        (val_sub,"$camera_height",10),
        (val_max,"$camera_height",10),
        (position_set_z_to_ground_level, pos1),
        (position_move_z,pos1,"$camera_height"),
        (position_rotate_x,pos1,-5),
        (mission_cam_animate_to_position, pos1, 10, 0),
        ])

## Shield bash code start
shield_bash_trigger_1 = (ti_before_mission_start, 0, 0, [], [(assign,"$bash_readiness",0)])

shield_bash_trigger_2 = (0.1, 0, 0, [(eq,"$setting_use_shieldbash",1)], [(val_add,"$bash_readiness",1),])

shield_bash_trigger_3 = (0, 0, 0, [(game_key_is_down, gk_defend),(game_key_clicked, gk_attack),(eq,"$setting_use_shieldbash",1),(ge,"$bash_readiness",10),],
       [
        (get_player_agent_no,":player"),
        (agent_is_alive,":player"),
       	(agent_get_horse,":horse",":player"),
        (neg|gt,":horse",0),
        # Lav's fixed code
        (agent_get_wielded_item, ":item", ":player", 1),
        (ge, ":item", 0),
        (item_get_type, ":itemtype", ":item"),
        (eq, ":itemtype", itp_type_shield),
        #(assign,":continue",0),
        #(agent_get_wielded_item, ":handone", ":player", 0),
        #(agent_get_wielded_item, ":handtwo", ":player", 1),
        #(try_for_range,":shield","itm_wooden_shield","itm_darts"),
        #    (this_or_next|eq,":handone",":shield"),
        #    (eq,":handtwo",":shield"),
        #    (assign,":continue",1),
        #(end_try),
        #(eq,":continue",1),
        (assign,"$bash_readiness",0),
        (call_script,"script_cf_agent_shield_bash",":player"),
        ])

shield_bash_trigger_4 = (3.0, 0, 0, [(eq,"$setting_use_shieldbash",1)],
       [(get_player_agent_no,":player"),
        (try_for_agents,":agent"),
           (agent_is_alive,":agent"),
           (agent_is_human,":agent"),
           (neq,":agent",":player"),
           (agent_get_class ,":class", ":agent"),
           (neq,":class",grc_cavalry),
           # Lav's fixed code
           (agent_get_wielded_item, ":item", ":agent", 1),
           (ge, ":item", 0),
           (item_get_type, ":itemtype", ":item"),
           (eq, ":itemtype", itp_type_shield),
           #(assign,":continue",0),
           #(agent_get_wielded_item, ":handone", ":agent", 0),
           #(agent_get_wielded_item, ":handtwo", ":agent", 1),
           #(try_for_range,":shield","itm_wooden_shield","itm_darts"),
           #    (this_or_next|eq,":handone",":shield"),
           #    (eq,":handtwo",":shield"),
           #    (assign,":continue",1),
           #(end_try),
           #(eq,":continue",1),
           (assign,":chances",0),
           (agent_get_team,":team",":agent"),
           (agent_get_position,pos1,":agent"),
           (try_for_agents,":other"),
                (agent_is_alive,":other"),
                (agent_is_human,":other"),
                (agent_get_class ,":class", ":other"),
                (neq,":class",grc_cavalry),
                (agent_get_team,":otherteam",":other"),
                (neq,":team",":otherteam"),
                (agent_get_position,pos2,":other"),
                (get_distance_between_positions,":dist",pos1,pos2),
                (neg|position_is_behind_position,pos2,pos1),
                (lt,":dist",200),
                (val_add,":chances",1),
           (end_try),
           (store_agent_hit_points,":health",":agent",0),
           (val_mul,":health",-1),
           (val_add,":health",100),
           (val_div,":health",10),
           (val_mul,":chances",":health"),
           (store_random_in_range,":rand",1,75),
           (lt,":rand",":chances"),
           (call_script,"script_cf_agent_shield_bash",":agent"),
        (end_try),])
## Shield bash code end

## Call for your horse - Jinnai
call_horse_trigger_1 = (0, 0, 3, [(gt, "$ne_key_whistle", 0),(key_clicked, "$ne_key_whistle")], [
      (get_player_agent_no,":agent"),
      (agent_get_horse,":horse",":agent"),
      (lt,":horse",0),
      (troop_get_slot,":horse",":agent",slot_troop_horse),
      (gt,":horse",0),
      (agent_is_alive,":horse"),
      (agent_play_sound,":agent","snd_whistle"),
      (display_message,"@You whistle for your horse."),
      (agent_get_position, pos1, ":agent"),
      (agent_set_scripted_destination, ":horse", pos1, 0),
    ])

call_horse_trigger_2 = (0.2, 0, ti_once, [], [
      (get_player_agent_no,":agent"),
      (agent_get_horse,":horse",":agent"),
      (troop_set_slot,":agent",slot_troop_horse,":horse"),
    ])

## Spearwall code start - Jinnai
spearwall_trigger_1 = (0.2, 0, ti_once, [], [
        (assign,"$spear_in_position",0),
        (try_for_agents,":agent"),
          (agent_set_slot,":agent",slot_agent_spearwall,0),
          (agent_set_slot,":agent",slot_agent_x,0),
          (agent_set_slot,":agent",slot_agent_y,0),
          (agent_set_slot,":agent",slot_agent_z,0),
          (agent_set_slot,":agent",slot_agent_speed,0),
        (try_end),
        ])

spearwall_trigger_2 = (0.2, 0, 0, [(eq,"$setting_use_spearwall",1)], [
        (set_fixed_point_multiplier, 100),
        (try_for_agents,":agent"),
          (agent_is_alive,":agent"),
          (agent_get_slot,":oldagentx",":agent",slot_agent_x),
          (agent_get_slot,":oldagenty",":agent",slot_agent_y),
          (agent_get_slot,":oldagentz",":agent",slot_agent_z),
          (agent_get_position, pos1, ":agent"),
          (position_get_x,":agentx",pos1),
          (position_get_y,":agenty",pos1),
          (position_get_z,":agentz",pos1),
          (position_set_x,pos2,":oldagentx"),
          (position_set_y,pos2,":oldagenty"),
          (position_set_z,pos2,":oldagentz"),
          (position_set_x,pos1,":agentx"),
          (position_set_y,pos1,":agenty"),
          (position_set_z,pos1,":agentz"),
          (get_distance_between_positions,":speed",pos1,pos2),
          (agent_set_slot,":agent",slot_agent_x,":agentx"),
          (agent_set_slot,":agent",slot_agent_y,":agenty"),
          (agent_set_slot,":agent",slot_agent_z,":agentz"),
          (agent_set_slot,":agent",slot_agent_speed,":speed"),
        (try_end),
        ])

spearwall_trigger_3 = (0, 0, 0, [(eq,"$spear_in_position",1),(this_or_next|game_key_clicked, gk_attack),
        (this_or_next|game_key_clicked, gk_defend),(this_or_next|game_key_clicked, gk_defend),
        (this_or_next|game_key_clicked, gk_move_forward),(this_or_next|game_key_clicked, gk_move_backward),
        (this_or_next|game_key_clicked, gk_move_left),(this_or_next|game_key_clicked, gk_move_right),
        (this_or_next|game_key_clicked, gk_equip_primary_weapon),(this_or_next|game_key_clicked, gk_equip_secondary_weapon),
        (this_or_next|game_key_clicked, gk_action),(game_key_clicked, gk_sheath_weapon)
        ], 
       [(get_player_agent_no,":player"),
        (agent_is_alive,":player"),
        (display_message,"@Releasing spear.",0x6495ed),
        (agent_set_animation, ":player", "anim_release_thrust_staff"),
        (assign,"$spear_in_position",0),
        ])

spearwall_trigger_4 = (0.2, 0, 0, [(eq,"$setting_use_spearwall",1)], [
        (try_for_agents,":agent"),
          (agent_get_horse,":horse",":agent"),
          (neg|gt,":horse",0),
          (agent_get_slot,":speartimer",":agent",slot_agent_spearwall),
          (lt,":speartimer",10),
          (val_add,":speartimer",2),
          (agent_set_slot,":agent",slot_agent_spearwall,":speartimer"),
        (try_end),
        ])

spearwall_trigger_5 = (3, 0, 0, [(eq,"$spear_in_position",1)],[
        (get_player_agent_no,":player"),
        (agent_is_alive,":player"),
        (agent_set_animation, ":player", "anim_spearwall_hold"),
        ])

spearwall_trigger_6 = (0.1, 0, 0, [(eq,"$setting_use_spearwall",1)], [
        (get_player_agent_no,":player"),
        (agent_get_team,":playerteam",":player"),
        (try_for_agents,":agent"),
           (agent_is_alive,":agent"),
           (neq,":agent",":player"),
           (agent_is_human,":agent"),
           (agent_get_horse,":horse",":agent"),
           (neg|gt,":horse",0),
           (agent_get_slot,":speartimer",":agent",slot_agent_spearwall),
           (ge,":speartimer",10),
           (agent_get_simple_behavior,":state",":agent"),
           (agent_get_team,":team1",":agent"),
           (agent_get_class,":class",":agent"),
           (team_get_movement_order,":order",":team1",":class"),
           (assign,":continue",0),
           (try_begin),
              (neq,":team1",":playerteam"),
              (this_or_next|eq,":state",aisb_hold),
              (this_or_next|eq,":state",aisb_flock),
              (eq,":state",aisb_go_to_pos),
              (assign,":continue",1),
           (else_try),
              (this_or_next|eq,":order",mordr_hold),
              (eq,":order",mordr_stand_ground),
              (this_or_next|eq,":state",aisb_hold),
              (this_or_next|eq,":state",aisb_flock),
              (this_or_next|eq,":state",aisb_melee),
              (eq,":state",aisb_go_to_pos),
              (assign,":continue",1),
           (try_end),
           (eq,":continue",1),
           (assign,":continue",0),
           (try_begin),
              (eq,":team1",":playerteam"),
              (eq,"$rout",0),
              (assign,":continue",1),
           (else_try),
              (eq,"$airout",0),
              (assign,":continue",1),
           (try_end),
           (eq,":continue",1),

           (agent_get_wielded_item, ":handone", ":agent", 0),
           (gt, ":handone", 0),
           (item_get_type, ":check", ":handone"),
           (eq, ":check", itp_type_polearm),
           (item_get_thrust_damage, ":check", ":handone"),
           (gt, ":check", 0), # Has thrust damage
           (item_get_thrust_damage_type, ":check", ":handone"),
           (neq, ":check", blunt), # Piercing or cutting
           (neg|item_has_property, ":handone", itp_couchable), # Not a lance
           (item_get_weapon_length, ":speardist", ":handone"),
           
           #(assign,":continue",0),
           #(agent_get_wielded_item, ":handone", ":agent", 0),
           #(agent_get_wielded_item, ":handtwo", ":agent", 1),
           #(assign,":speardist",145),
           #(try_for_range,":spear",weapons_begin,weapons_end),
           #   (this_or_next|eq,":handone",":spear"),
           #   (eq,":handtwo",":spear"),
           #   (assign,":continue",1),
           #   (try_begin),
           #      (eq,":spear","itm_war_spear"),
           #      (assign,":speardist",160),
           #   (else_try),
           #      (eq,":spear","itm_spear_e_2-5m"),
           #      (assign,":continue",0),
           #   (else_try),
           #      (eq,":spear","itm_light_lance"),
           #      (assign,":continue",0),
           #   (else_try),
           #      (eq,":spear","itm_lance"),
           #      (assign,":continue",0),
           #   (else_try),
           #      (eq,":spear","itm_heavy_lance"),
           #      (assign,":continue",0),
           #   (else_try),
           #      (eq,":spear","itm_pike"),
           #      (assign,":speardist",255),
           #   (else_try),
           #      (eq,":spear","itm_ashwood_pike"),
           #      (assign,":speardist",255),
           #   (else_try),
           #      (eq,":spear","itm_awlpike"),
           #      (assign,":speardist",170),
           #   (else_try),
           #      (eq,":spear","itm_pitch_fork"),
           #      (assign,":speardist",164),
           #   (else_try),
           #      (eq,":spear","itm_military_fork"),
           #      (assign,":speardist",145),
           #   (else_try),
           #      (eq,":spear","itm_battle_fork"),
           #      (assign,":speardist",152),
           #   (else_try),
           #      (eq,":spear","itm_boar_spear"),
           #      (assign,":speardist",167),
           #   (else_try),
           #      (eq,":spear","itm_glaive"),
           #      (assign,":speardist",167),
           #   (else_try),
           #      (eq,":spear","itm_poleaxe"),
           #      (assign,":speardist",190),
           #   (else_try),
           #      (eq,":spear","itm_polehammer"),
           #      (assign,":speardist",140),
           #   (else_try),
           #      (eq,":spear","itm_shortened_spear"),
           #      (assign,":speardist",130),
           #   (else_try),
           #      (eq,":spear","itm_halberd"),
           #      (assign,":speardist",185),
           #   (else_try),
           #      (eq,":spear","itm_ancient_halbard"),
           #      (assign,":speardist",185),
           #   (else_try),
           #      (eq,":spear","itm_klance"),
           #      (assign,":continue",0),
           #   (else_try),
           #      (eq,":spear","itm_jousting_lance"),
           #      (assign,":continue",0),
           #   (else_try),
           #      (eq,":spear","itm_double_sided_lance"),
           #      (assign,":continue",0),
           #   (else_try),
           #      (eq,":spear","itm_staff"),
           #      (assign,":continue",0),
           #   (else_try),
           #      (eq,":spear","itm_quarter_staff"),
           #      (assign,":continue",0),
           #   (else_try),
           #      (eq,":spear","itm_iron_staff"),
           #      (assign,":continue",0),
           #   (try_end),
           #(try_end),
           #(eq,":continue",1),

           (assign,":victim",-1),
           (agent_get_position,pos1,":agent"),
           (try_for_agents,":possible_victim"),
              (agent_is_alive,":possible_victim"),
              (neg|agent_is_human,":possible_victim"),
              (agent_get_rider,":rider",":possible_victim"),
              (ge,":rider",0),
              (agent_get_team,":team2",":rider"),
              (teams_are_enemies,":team1",":team2"),
              (agent_get_position,pos2,":possible_victim"),
              (get_distance_between_positions,":dist",pos1,pos2),
              (lt,":dist",":speardist"),
              (neg|position_is_behind_position,pos2,pos1),
              (agent_get_slot,":speed",":possible_victim",slot_agent_speed),
              (ge,":speed",120), # Remember to change this if the timing on speed checks changes
              (assign,":victim",":possible_victim"),
           (try_end),
           (gt,":victim",-1),
           (agent_set_animation, ":agent", "anim_spearwall_hold"),
           (agent_play_sound,":victim","snd_metal_hit_high_armor_high_damage"),
           (store_agent_hit_points,":hp",":victim",0),
           (store_agent_hit_points,":oldhp",":victim",1),
           (val_div,":speed",2), # Remember to change this if the timing on speed checks changes
           (val_sub,":speed",15),
           (val_sub,":hp",":speed"),
           (val_max,":hp",0),
           (agent_set_slot,":agent",slot_agent_spearwall,0),
           (agent_get_horse,":playerhorse",":player"),           
           (agent_set_hit_points,":victim",":hp",0),
           (agent_deliver_damage_to_agent,":victim",":victim"),
           (try_begin),
              (eq,":victim",":playerhorse"),
              (store_agent_hit_points,":hp",":victim",1),
              (val_sub,":oldhp",":hp"),
              (assign,reg1,":oldhp"),
              (display_message,"@Your horse received {reg1} damage from a braced spear!",0xff4040),
           (try_end),
# Debug code to make sure it's being used properly
#           (try_begin),
#              (eq,":team2",":playerteam"),
#              (display_message,"@An enemy spear wall has killed an allied horse!",0xff4040),
#           (else_try),
#              (display_message,"@An allied spear wall has killed an enemy horse!"),
#           (try_end),
        (try_end),
        ])

spearwall_trigger_7 = (0.1, 0, 0, [(eq,"$spear_in_position",1)], [
        (get_player_agent_no,":player"),
        (agent_is_alive,":player"),
        (store_agent_hit_points,":hp",":player",1),
        (lt,":hp","$spear_hp"),
        (display_message,"@The injury causes your grip on the spear to slip!",0xff4040),
        (agent_set_animation, ":player", "anim_release_thrust_staff"),
        (assign,"$spear_in_position",0),
        ])

spearwall_trigger_8 = (0.1, 0, 0, [(eq,"$spear_in_position",1)], [
        (get_player_agent_no,":player"),
        (agent_is_alive,":player"),
        (agent_get_slot,":speartimer",":player",slot_agent_spearwall),
        (ge,":speartimer",10),
        (assign,":victim",-1),
        (agent_get_position,pos1,":player"),
        (try_for_agents,":possible_victim"),
           (agent_is_alive,":possible_victim"),
           (neg|agent_is_human,":possible_victim"),
           (agent_get_rider,":rider",":possible_victim"),
           (ge,":rider",0),
           (neg|agent_is_ally,":rider"),
           (agent_get_position,pos2,":possible_victim"),
           (get_distance_between_positions,":dist",pos1,pos2),
           (lt,":dist","$spear_dist"),
           (neg|position_is_behind_position,pos2,pos1),
           (agent_get_slot,":speed",":possible_victim",slot_agent_speed),
           (ge,":speed",120), # Remember to change this if the timing on speed checks changes
           (assign,":victim",":possible_victim"),
        (try_end),
        (gt,":victim",-1),
        (agent_play_sound,":victim","snd_metal_hit_high_armor_high_damage"),
        (store_agent_hit_points,":hp",":victim",0),
        (store_agent_hit_points,":oldhp",":victim",1),
        (val_div,":speed",2), # Remember to change this if the timing on speed checks changes
        (val_sub,":speed",15),
        (val_sub,":hp",":speed"),
        (val_max,":hp",0),
        (agent_set_hit_points,":victim",":hp",0),
        (agent_deliver_damage_to_agent,":victim",":victim"),
        (agent_set_slot,":player",slot_agent_spearwall,0),
        (store_agent_hit_points,":hp",":victim",1),
        (val_sub,":oldhp",":hp"),
        (assign,reg1,":oldhp"),
        (display_message,"@Spear-wall dealt {reg1} damage!"),
        ])

spearwall_trigger_9 = (0, 0, 2, [(gt, "$ne_key_brace", 0),(key_clicked, "$ne_key_brace"),(eq,"$setting_use_spearwall",1)],
       [
        (get_player_agent_no,":player"),
        (agent_is_alive,":player"),

        (agent_get_wielded_item, ":handone", ":player", 0),
        (gt, ":handone", 0),
        (item_get_type, ":check", ":handone"),
        (eq, ":check", itp_type_polearm),
        (item_get_thrust_damage, ":check", ":handone"),
        (gt, ":check", 0), # Has thrust damage
        (item_get_thrust_damage_type, ":check", ":handone"),
        (neq, ":check", blunt), # Piercing or cutting
        (neg|item_has_property, ":handone", itp_couchable), # Not a lance
        #(item_get_weapon_length, ":speardist", ":handone"),
        
        #(assign,":continue",0),
        #(agent_get_wielded_item, ":handone", ":player", 0),
        #(agent_get_wielded_item, ":handtwo", ":player", 1),
        #(assign,"$spear_dist",145),
        #(try_for_range,":spear",weapons_begin,weapons_end),
        #    (this_or_next|eq,":handone",":spear"),
        #    (eq,":handtwo",":spear"),
        #    (assign,":continue",1),
        #      (try_begin),
        #         (eq,":spear","itm_war_spear"),
        #         (assign,"$spear_dist",160),
        #      (else_try),
        #         (eq,":spear","itm_spear_e_2-5m"),
        #         (assign,":continue",0),
        #      (else_try),
        #         (eq,":spear","itm_light_lance"),
        #         (assign,":continue",0),
        #      (else_try),
        #         (eq,":spear","itm_lance"),
        #         (assign,":continue",0),
        #      (else_try),
        #         (eq,":spear","itm_heavy_lance"),
        #         (assign,":continue",0),
        #      (else_try),
        #         (eq,":spear","itm_pike"),
        #         (assign,"$spear_dist",255),
        #      (else_try),
        #         (eq,":spear","itm_ashwood_pike"),
        #         (assign,"$spear_dist",255),
        #      (else_try),
        #         (eq,":spear","itm_awlpike"),
        #         (assign,"$spear_dist",170),
        #      (else_try),
        #         (eq,":spear","itm_pitch_fork"),
        #         (assign,"$spear_dist",164),
        #      (else_try),
        #         (eq,":spear","itm_military_fork"),
        #         (assign,"$spear_dist",145),
        #      (else_try),
        #         (eq,":spear","itm_battle_fork"),
        #         (assign,"$spear_dist",152),
        #      (else_try),
        #         (eq,":spear","itm_boar_spear"),
        #         (assign,"$spear_dist",167),
        #      (else_try),
        #         (eq,":spear","itm_glaive"),
        #         (assign,"$spear_dist",167),
        #      (else_try),
        #         (eq,":spear","itm_poleaxe"),
        #         (assign,"$spear_dist",190),
        #      (else_try),
        #         (eq,":spear","itm_polehammer"),
        #         (assign,"$spear_dist",140),
        #      (else_try),
        #         (eq,":spear","itm_shortened_spear"),
        #         (assign,"$spear_dist",130),
        #      (else_try),
        #         (eq,":spear","itm_halberd"),
        #         (assign,"$spear_dist",185),
        #      (else_try),
        #         (eq,":spear","itm_ancient_halbard"),
        #         (assign,"$spear_dist",185),
        #      (else_try),
        #         (eq,":spear","itm_klance"),
        #         (assign,":continue",0),
        #      (else_try),
        #         (eq,":spear","itm_jousting_lance"),
        #         (assign,":continue",0),
        #      (else_try),
        #         (eq,":spear","itm_double_sided_lance"),
        #         (assign,":continue",0),
        #      (else_try),
        #         (eq,":spear","itm_staff"),
        #         (assign,":continue",0),
        #      (else_try),
        #         (eq,":spear","itm_quarter_staff"),
        #         (assign,":continue",0),
        #      (else_try),
        #         (eq,":spear","itm_iron_staff"),
        #         (assign,":continue",0),
        #      (try_end),
        #(try_end),
        #(eq,":continue",1),

       	(agent_get_horse,":horse",":player"),
        (neg|gt,":horse",0),
        (neq, "$spear_in_position", 1),
        (display_message,"@Bracing spear for charge.",0x6495ed),
        (agent_set_animation, ":player", "anim_spearwall_hold"),
        (assign, "$spear_in_position", 1),
        (store_agent_hit_points,"$spear_hp",":player",1),
        ])
## Spearwall code end


# NE end cam
		
tournament_triggers = [
  (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest"),
                                       (assign, "$g_arena_training_num_agents_spawned", 0)]),
  (ti_inventory_key_pressed, 0, 0, [(display_message,"str_cant_use_inventory_arena")], []),
  (ti_tab_pressed, 0, 0, [],
   [(try_begin),
      (eq, "$g_mt_mode", abm_visit),
      (set_trigger_result, 1),
    (else_try),
      (question_box,"str_give_up_fight"),
    (try_end),
    ]),
  (ti_question_answered, 0, 0, [],
   [(store_trigger_param_1,":answer"),
    (eq,":answer",0),
    (try_begin),
      (eq, "$g_mt_mode", abm_tournament),
      (call_script, "script_end_tournament_fight", 0),
    (else_try),
      (eq, "$g_mt_mode", abm_training),
      (get_player_agent_no, ":player_agent"),
      (agent_get_kill_count, "$g_arena_training_kills", ":player_agent", 1),#use this for conversation
    (try_end),
    (finish_mission,0),
    ]),

  (1, 0, ti_once, [], [
      (eq, "$g_mt_mode", abm_visit),
      (call_script, "script_music_set_situation_with_culture", mtf_sit_travel),
      (store_current_scene, reg(1)),
      (scene_set_slot, reg(1), slot_scene_visited, 1),
      (mission_enable_talk),
      (get_player_agent_no, ":player_agent"),
      (assign, ":team_set", 0),
      (try_for_agents, ":agent_no"),
        (neq, ":agent_no", ":player_agent"),
        (agent_get_troop_id, ":troop_id", ":agent_no"),
        (is_between, ":troop_id", regular_troops_begin, regular_troops_end),
        (eq, ":team_set", 0),
        (agent_set_team, ":agent_no", 1),
        (assign, ":team_set", 1),
      (try_end),
    ]),
##
##  (0, 0, 0, [],
##   [
##      #refresh hit points for arena visit trainers
##      (eq, "$g_mt_mode", abm_visit),
##      (get_player_agent_no, ":player_agent"),
##      (try_for_agents, ":agent_no"),
##        (neq, ":agent_no", ":player_agent"),
##        (agent_get_troop_id, ":troop_id", ":agent_no"),
##        (is_between, ":troop_id", regular_troops_begin, regular_troops_end),
##        (agent_set_hit_points, ":agent_no", 100),
##      (try_end),
##    ]),
  
##      (1, 4, ti_once, [(eq, "$g_mt_mode", abm_fight),
##                       (this_or_next|main_hero_fallen),
##                       (num_active_teams_le,1)],
##       [
##           (try_begin),
##             (num_active_teams_le,1),
##             (neg|main_hero_fallen),
##             (assign,"$arena_fight_won",1),
##             #Fight won, decrease odds
##             (assign, ":player_odds_sub", 0),
##             (try_begin),
##               (ge,"$arena_bet_amount",1),
##               (store_div, ":player_odds_sub", "$arena_win_amount", 2),
##             (try_end),
##             (party_get_slot, ":player_odds", "$g_encountered_party", slot_town_player_odds),
##             (val_add, ":player_odds_sub", 5),
##             (val_sub, ":player_odds", ":player_odds_sub"),
##             (val_max, ":player_odds", 250),
##             (party_set_slot, "$g_encountered_party", slot_town_player_odds, ":player_odds"),
##           (else_try),
##             #Fight lost, increase odds
##             (assign, ":player_odds_add", 0),
##             (try_begin),
##               (ge,"$arena_bet_amount",1),
##               (store_div, ":player_odds_add", "$arena_win_amount", 2),
##             (try_end),
##             (party_get_slot, ":player_odds", "$g_encountered_party", slot_town_player_odds),
##             (val_add, ":player_odds_add", 5),
##             (val_add, ":player_odds", ":player_odds_add"),
##             (val_min, ":player_odds", 4000),
##             (party_set_slot, "$g_encountered_party", slot_town_player_odds, ":player_odds"),
##           (try_end),
##           (store_remaining_team_no,"$arena_winner_team"),
##           (assign, "$g_mt_mode", abm_visit),
##           (party_get_slot, ":arena_mission_template", "$current_town", slot_town_arena_template),
##           (set_jump_mission, ":arena_mission_template"),
##           (party_get_slot, ":arena_scene", "$current_town", slot_town_arena),
##           (modify_visitors_at_site, ":arena_scene"),
##           (reset_visitors),
##           (set_visitor, 35, "trp_veteran_fighter"),
##           (set_visitor, 36, "trp_hired_blade"),
##           (set_jump_entry, 50),
##           (jump_to_scene, ":arena_scene"),
##           ]),
  
  (0, 0, ti_once, [],
   [
     (eq, "$g_mt_mode", abm_tournament),
     (play_sound, "snd_arena_ambiance", sf_looping),
     (call_script, "script_music_set_situation_with_culture", mtf_sit_arena),
     ]),

  (1, 4, ti_once, [(eq, "$g_mt_mode", abm_tournament),
                   (this_or_next|main_hero_fallen),
                   (num_active_teams_le, 1)],
   [
       (try_begin),
         (neg|main_hero_fallen),
         (call_script, "script_end_tournament_fight", 1),
         (call_script, "script_play_victorious_sound"),
         (finish_mission),
       (else_try),
         (call_script, "script_end_tournament_fight", 0),
         (finish_mission),
       (try_end),
       ]),

  (ti_battle_window_opened, 0, 0, [], [(eq, "$g_mt_mode", abm_training),(start_presentation, "prsnt_arena_training")]),
  
  (0, 0, ti_once, [], [(eq, "$g_mt_mode", abm_training),
                       (assign, "$g_arena_training_max_opponents", 40),
                       (assign, "$g_arena_training_num_agents_spawned", 0),
                       (assign, "$g_arena_training_kills", 0),
                       (assign, "$g_arena_training_won", 0),
                       (call_script, "script_music_set_situation_with_culture", mtf_sit_arena),
                       ]),

  (1, 4, ti_once, [(eq, "$g_mt_mode", abm_training),
                   (store_mission_timer_a, ":cur_time"),
                   (gt, ":cur_time", 3),
                   (assign, ":win_cond", 0),
                   (try_begin),
                     (ge, "$g_arena_training_num_agents_spawned", "$g_arena_training_max_opponents"),#spawn at most 40 agents
                     (num_active_teams_le, 1),
                     (assign, ":win_cond", 1),
                   (try_end),
                   (this_or_next|eq, ":win_cond", 1),
                   (main_hero_fallen)],
   [
       (get_player_agent_no, ":player_agent"),
       (agent_get_kill_count, "$g_arena_training_kills", ":player_agent", 1),#use this for conversation
       (assign, "$g_arena_training_won", 0),
       (try_begin),
         (neg|main_hero_fallen),
         (assign, "$g_arena_training_won", 1),#use this for conversation
       (try_end),
       (assign, "$g_mt_mode", abm_visit),
       (set_jump_mission, "mt_arena_melee_fight"),
       (party_get_slot, ":arena_scene", "$current_town", slot_town_arena),
       (modify_visitors_at_site, ":arena_scene"),
       (reset_visitors),
       (set_visitor, 35, "trp_veteran_fighter"),
       (set_visitor, 36, "trp_hired_blade"),
       (set_jump_entry, 50),
       (jump_to_scene, ":arena_scene"),
       ]),


  (0.2, 0, 0,
   [
       (eq, "$g_mt_mode", abm_training),
       (assign, ":num_active_fighters", 0),
       (try_for_agents, ":agent_no"),
         (agent_is_human, ":agent_no"),
         (agent_is_alive, ":agent_no"),
         (agent_get_team, ":team_no", ":agent_no"),
         (is_between, ":team_no", 0 ,7),
         (val_add, ":num_active_fighters", 1),
       (try_end),
       (lt, ":num_active_fighters", 7),
       (neg|main_hero_fallen),
       (store_mission_timer_a, ":cur_time"),
       (this_or_next|ge, ":cur_time", "$g_arena_training_next_spawn_time"),
       (this_or_next|lt, "$g_arena_training_num_agents_spawned", 6),
       (num_active_teams_le, 1),
       (lt, "$g_arena_training_num_agents_spawned", "$g_arena_training_max_opponents"),
      ],
    [
       (assign, ":added_troop", "$g_arena_training_num_agents_spawned"),
       (store_div,  ":added_troop", "$g_arena_training_num_agents_spawned", 6),
       (assign, ":added_troop_sequence", "$g_arena_training_num_agents_spawned"),
       (val_mod, ":added_troop_sequence", 6),
       (val_add, ":added_troop", ":added_troop_sequence"),
       (val_min, ":added_troop", 9),
       (val_add, ":added_troop", "trp_arena_training_fighter_1"),
       (assign, ":end_cond", 10000),
       (get_player_agent_no, ":player_agent"),
       (agent_get_position, pos5, ":player_agent"),
       (try_for_range, ":unused", 0, ":end_cond"),
         (store_random_in_range, ":random_entry_point", 32, 40),
         (neq, ":random_entry_point", "$g_player_entry_point"), # make sure we don't overwrite player
         (entry_point_get_position, pos1, ":random_entry_point"),
         (get_distance_between_positions, ":dist", pos5, pos1),
         (gt, ":dist", 1200), #must be at least 12 meters away from the player
         (assign, ":end_cond", 0),
       (try_end),
       (add_visitors_to_current_scene, ":random_entry_point", ":added_troop", 1),
       (store_add, ":new_spawned_count", "$g_arena_training_num_agents_spawned", 1),
       (store_mission_timer_a, ":cur_time"),
       (store_add, "$g_arena_training_next_spawn_time", ":cur_time", 14),
       (store_div, ":time_reduction", ":new_spawned_count", 3),
       (val_sub, "$g_arena_training_next_spawn_time", ":time_reduction"),
       ]),

  (0, 0, 0,
   [
       (eq, "$g_mt_mode", abm_training)
       ],
    [
       (assign, ":max_teams", 6),
       (val_max, ":max_teams", 1),
       (get_player_agent_no, ":player_agent"),
       (try_for_agents, ":agent_no"),
         (agent_is_human, ":agent_no"),
         (agent_is_alive, ":agent_no"),
         (agent_slot_eq, ":agent_no", slot_agent_arena_team_set, 0),
         (agent_get_team, ":team_no", ":agent_no"),
         (is_between, ":team_no", 0 ,7),
         (try_begin),
           (eq, ":agent_no", ":player_agent"),
           (agent_set_team, ":agent_no", 6), #player is always team 6.
         (else_try),
           (store_random_in_range, ":selected_team", 0, ":max_teams"),
          # find strongest team
           (try_for_range, ":t", 0, 6),
             (troop_set_slot, "trp_temp_array_a", ":t", 0),
           (try_end),
           (try_for_agents, ":other_agent_no"),
             (agent_is_human, ":other_agent_no"),
             (agent_is_alive, ":other_agent_no"),
             (neq, ":agent_no", ":player_agent"),
             (agent_slot_eq, ":other_agent_no", slot_agent_arena_team_set, 1),
             (agent_get_team, ":other_agent_team", ":other_agent_no"),
             (troop_get_slot, ":count", "trp_temp_array_a", ":other_agent_team"),
             (val_add, ":count", 1),
             (troop_set_slot, "trp_temp_array_a", ":other_agent_team", ":count"),
           (try_end),
           (assign, ":strongest_team", 0),
           (troop_get_slot, ":strongest_team_count", "trp_temp_array_a", 0),
           (try_for_range, ":t", 1, 6),
             (troop_slot_ge, "trp_temp_array_a", ":t", ":strongest_team_count"),
             (troop_get_slot, ":strongest_team_count", "trp_temp_array_a", ":t"),
             (assign, ":strongest_team", ":t"),
           (try_end),
           (store_random_in_range, ":rand", 5, 100),
           (try_begin),
             (lt, ":rand", "$g_arena_training_num_agents_spawned"),
             (assign, ":selected_team", ":strongest_team"),
           (try_end),
           (agent_set_team, ":agent_no", ":selected_team"),
         (try_end),
         (agent_set_slot, ":agent_no", slot_agent_arena_team_set, 1),
         (try_begin),
           (neq, ":agent_no", ":player_agent"),
           (val_add, "$g_arena_training_num_agents_spawned", 1),
         (try_end),
       (try_end),
       ]),
  ]

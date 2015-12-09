from compiler import *
register_plugin()


common_siege_init_ai_and_belfry   = (0, 0, ti_once, [ (call_script, "script_siege_init_ai_and_belfry")        ], [])
common_siege_move_belfry          = (0, 0, ti_once, [ (call_script, "script_cf_siege_move_belfry")            ], [])
common_siege_rotate_belfry        = (0, 2, ti_once, [ (call_script, "script_cf_siege_rotate_belfry_platform") ], [ (assign, "$belfry_positioned", 3) ])
common_siege_assign_men_to_belfry = (0, 0, ti_once, [ (call_script, "script_cf_siege_assign_men_to_belfry")   ], [])


scripts = [

  # script_siege_init_ai_and_belfry
  # Input: none
  # Output: none (required for siege mission templates)
  ("siege_init_ai_and_belfry",
   [(assign, "$cur_belfry_pos", 50),
    (assign, ":cur_belfry_object_pos", slot_scene_belfry_props_begin),
    (store_current_scene, ":cur_scene"),
    #Collecting belfry objects
    (try_for_range, ":i_belfry_instance", 0, 3),
      (scene_prop_get_instance, ":belfry_object", "spr_belfry_a", ":i_belfry_instance"),
      (ge, ":belfry_object", 0),
      (scene_set_slot, ":cur_scene", ":cur_belfry_object_pos", ":belfry_object"),
      (val_add, ":cur_belfry_object_pos", 1),
    (try_end),
    (try_for_range, ":i_belfry_instance", 0, 3),
      (scene_prop_get_instance, ":belfry_object", "spr_belfry_platform_a", ":i_belfry_instance"),
      (ge, ":belfry_object", 0),
      (scene_set_slot, ":cur_scene", ":cur_belfry_object_pos", ":belfry_object"),
      (val_add, ":cur_belfry_object_pos", 1),
    (try_end),
    (try_for_range, ":i_belfry_instance", 0, 3),
      (scene_prop_get_instance, ":belfry_object", "spr_belfry_platform_b", ":i_belfry_instance"),
      (ge, ":belfry_object", 0),
      (scene_set_slot, ":cur_scene", ":cur_belfry_object_pos", ":belfry_object"),
      (val_add, ":cur_belfry_object_pos", 1),
    (try_end),
    (assign, "$belfry_rotating_objects_begin", ":cur_belfry_object_pos"),
    (try_for_range, ":i_belfry_instance", 0, 5),
      (scene_prop_get_instance, ":belfry_object", "spr_belfry_wheel", ":i_belfry_instance"),
      (ge, ":belfry_object", 0),
      (scene_set_slot, ":cur_scene", ":cur_belfry_object_pos", ":belfry_object"),
      (val_add, ":cur_belfry_object_pos", 1),
    (try_end),
    (assign, "$last_belfry_object_pos", ":cur_belfry_object_pos"),

    #Lifting up the platform  at the beginning
    (try_begin),
      (scene_prop_get_instance, ":belfry_object_to_rotate", "spr_belfry_platform_a", 0),
    (try_end),

    #Moving the belfry objects to their starting position
    (entry_point_get_position,pos1,55),
    (entry_point_get_position,pos3,50),
    (try_for_range, ":i_belfry_object_pos", slot_scene_belfry_props_begin, "$last_belfry_object_pos"),
      (assign, ":pos_no", pos_belfry_begin),
      (val_add, ":pos_no", ":i_belfry_object_pos"),
      (val_sub, ":pos_no", slot_scene_belfry_props_begin),
      (scene_get_slot, ":cur_belfry_object", ":cur_scene", ":i_belfry_object_pos"),
      (prop_instance_get_position, pos2, ":cur_belfry_object"),
      (try_begin),
        (eq, ":cur_belfry_object", ":belfry_object_to_rotate"),
        (position_rotate_x, pos2, 90),
      (try_end),
      (position_transform_position_to_local, ":pos_no", pos1, pos2),
      (position_transform_position_to_parent, pos4, pos3, ":pos_no"),
      (prop_instance_animate_to_position, ":cur_belfry_object", pos4, 1),
    (try_end),
    (assign, "$belfry_positioned", 0),
    (assign, "$belfry_num_slots_positioned", 0),
    (assign, "$belfry_num_men_pushing", 0),

    (set_show_messages, 0),
    (team_give_order, "$attacker_team", grc_everyone, mordr_stand_ground),
    (team_give_order, "$attacker_team_2", grc_everyone, mordr_stand_ground),
    (set_show_messages, 1),
  ]),

  # script_cf_siege_move_belfry
  # Input: none
  # Output: none (required for siege mission templates)
  ("cf_siege_move_belfry",
   [(neq, "$last_belfry_object_pos", slot_scene_belfry_props_begin), # if there are some belfry objects to move...
    (entry_point_get_position,pos1,50), # pos1 = starting waypoint position
    (entry_point_get_position,pos4,55), # pos4 = destination waypoint position
    (get_distance_between_positions, ":total_distance", pos4, pos1), # Total distance to move
    (store_current_scene, ":cur_scene"),
    (scene_get_slot, ":first_belfry_object", ":cur_scene", slot_scene_belfry_props_begin), # Main belfry prop
    (prop_instance_get_position, pos2, ":first_belfry_object"), # pos2 = Current belfry position
    (entry_point_get_position,pos1,"$cur_belfry_pos"), # pos1 = Current waypoint position
    (position_transform_position_to_parent, pos3, pos1, pos_belfry_begin), # pos3 = belfry calculated position at current waypoint
    (position_transform_position_to_parent, pos5, pos4, pos_belfry_begin), # pos5 = belfry calculated position at destination waypoint
    (get_distance_between_positions, ":cur_distance", pos2, pos3), # distance between current position and calculated position at current waypoint
    (get_distance_between_positions, ":distance_left", pos2, pos5), # distance between current position and calculated position at destination waypoint
    (try_begin),
      (le, ":cur_distance", 10), # If we reached current waypoint...
      (val_add, "$cur_belfry_pos", 1), # Advance to next waypoint
      (entry_point_get_position,pos1,"$cur_belfry_pos"), # pos1 = next waypoint position
      (position_transform_position_to_parent, pos3, pos1, pos_belfry_begin), # pos3 = belfry calculated position at current waypoint
      (get_distance_between_positions, ":cur_distance", pos2, pos3), # distance between current position and calculated position at current waypoint
    (try_end),
    (neq, "$cur_belfry_pos", 50), # If current waypoint is greater than 50 (i.e. not first)

    (assign, ":base_speed", 20), # Base speed is 20
    (store_div, ":slow_range", ":total_distance", 60), # slow_range = total_distance / 60
    (store_sub, ":distance_moved", ":total_distance", ":distance_left"), # calculate how much already moved

    (try_begin),
      (lt, ":distance_moved", ":slow_range"), # If we moved less than 1/60th of entire distance
      (store_mul, ":base_speed", ":distance_moved", -60),
      (val_div, ":base_speed", ":slow_range"),
      (val_add, ":base_speed", 80), # base_speed = 80 - 3600 * distance_moved / total_distance ===> speed will start at 80 but regress to 20
    (else_try),
      (lt, ":distance_left", ":slow_range"),
      (store_mul, ":base_speed", ":distance_left", -60),
      (val_div, ":base_speed", ":slow_range"),
      (val_add, ":base_speed", 80), # ===> speed will start at 20 but increase to 80
    (try_end),
    (store_mul, ":belfry_speed", ":cur_distance", ":base_speed"), # belfry_speed = (20..80) * distance to current waypoint
    (try_begin),
      (eq, "$belfry_num_men_pushing", 0), # If nobody's pushing...
      (assign, ":belfry_speed", 1000000), # Speed is 1 mln
    (else_try),
      (val_div, ":belfry_speed", "$belfry_num_men_pushing"), # belfry_speed = (20..80) * distance_to_current_waypoint / number_of_men_pushing
    (try_end),

    # NE Building
    (try_begin), # University upgrade stuff - Jinnai
      (faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
      (faction_slot_eq, "fac_player_supporters_faction", slot_faction_univ_belfry, 1),
      (val_div, ":belfry_speed", 2), # If there's a university, belfry_speed is halved
    (try_end),
    # NE end building

    (try_begin),
      (le, "$cur_belfry_pos", 55), # If current waypoint less than 56
      (init_position, pos3),
      (position_rotate_x, pos3, ":distance_moved"), # pos3 = zero with rotation along x proportional to distance_moved
      (scene_get_slot, ":base_belfry_object", ":cur_scene", slot_scene_belfry_props_begin), # first belfry object
      (prop_instance_get_position, pos4, ":base_belfry_object"), # current belfry position
      (entry_point_get_position,pos1,"$cur_belfry_pos"), # position of current waypoint
      (try_for_range, ":i_belfry_object_pos", slot_scene_belfry_props_begin, "$last_belfry_object_pos"), # for all active belfry objects
        (scene_get_slot, ":cur_belfry_object", ":cur_scene", ":i_belfry_object_pos"), # get belfry object
        (try_begin),
          (ge, ":i_belfry_object_pos", "$belfry_rotating_objects_begin"), # If it's rotating object (wheel)...
          (prop_instance_get_starting_position, pos5, ":base_belfry_object"),
          (prop_instance_get_starting_position, pos6, ":cur_belfry_object"),
          (position_transform_position_to_local, pos7, pos5, pos6),
          (position_transform_position_to_parent, pos5, pos4, pos7),
          (position_transform_position_to_parent, pos6, pos5, pos3),
          (prop_instance_set_position, ":cur_belfry_object", pos6),
        (else_try),
          (assign, ":pos_no", pos_belfry_begin),
          (val_add, ":pos_no", ":i_belfry_object_pos"),
          (val_sub, ":pos_no", slot_scene_belfry_props_begin), # relative position of current object
          (position_transform_position_to_parent, pos2, pos1, ":pos_no"), # calculated position of current object at current waypoint
          (prop_instance_animate_to_position, ":cur_belfry_object", pos2, ":belfry_speed"), # animate from current position to calculated position in specified time
        (try_end),
      (try_end),
    (try_end),
    (gt, "$cur_belfry_pos", 55),
    (assign, "$belfry_positioned", 1),
  ]),

  # script_cf_siege_rotate_belfry_platform
  # Input: none
  # Output: none (required for siege mission templates)
  ("cf_siege_rotate_belfry_platform",
   [(eq, "$belfry_positioned", 1),
    (scene_prop_get_instance, ":belfry_object", "spr_belfry_platform_a", 0),
    (prop_instance_get_position, pos1, ":belfry_object"),
    (position_rotate_x, pos1, -90),
    (prop_instance_animate_to_position, ":belfry_object", pos1, 400),
    (assign, "$belfry_positioned", 2),
  ]),

  # script_cf_siege_assign_men_to_belfry
  # Input: none
  # Output: none (required for siege mission templates)
  ("cf_siege_assign_men_to_belfry",
   [
##    (store_mission_timer_a, ":cur_seconds"),
    (neq, "$last_belfry_object_pos", slot_scene_belfry_props_begin),
    (assign, ":end_trigger", 0),
    (try_begin),
      (lt, "$belfry_positioned", 3),
      (get_player_agent_no, ":player_agent"),
      (store_current_scene, ":cur_scene"),
      (scene_get_slot, ":first_belfry_object", ":cur_scene", slot_scene_belfry_props_begin),
      (prop_instance_get_position, pos2, ":first_belfry_object"),
      (assign, ":slot_1_positioned", 0),
      (assign, ":slot_2_positioned", 0),
      (assign, ":slot_3_positioned", 0),
      (assign, ":slot_4_positioned", 0),
      (assign, ":slot_5_positioned", 0),
      (assign, ":slot_6_positioned", 0),
      (assign, "$belfry_num_slots_positioned", 0),
      (assign, "$belfry_num_men_pushing", 0),
      (try_for_agents, ":cur_agent"),
        (agent_is_alive, ":cur_agent"),
        (agent_is_human, ":cur_agent"),
        (try_begin),
          (agent_get_slot, ":x_pos", ":cur_agent", slot_agent_target_x_pos),
          (neq, ":x_pos", 0),
          (agent_get_slot, ":y_pos", ":cur_agent", slot_agent_target_y_pos),
          (try_begin),
            (eq, ":x_pos", -600),
            (try_begin),
              (eq, ":y_pos", 0),
              (assign, ":slot_1_positioned", 1),
            (else_try),
              (eq, ":y_pos", -200),
              (assign, ":slot_2_positioned", 1),
            (else_try),
              (assign, ":slot_3_positioned", 1),
            (try_end),
          (else_try),
            (try_begin),
              (eq, ":y_pos", 0),
              (assign, ":slot_4_positioned", 1),
            (else_try),
              (eq, ":y_pos", -200),
              (assign, ":slot_5_positioned", 1),
            (else_try),
              (assign, ":slot_6_positioned", 1),
            (try_end),
          (try_end),
          (val_add, "$belfry_num_slots_positioned", 1),
          (init_position, pos1),
          (position_move_x, pos1, ":x_pos"),
          (position_move_y, pos1, ":y_pos"),
          (init_position, pos3),
          (position_move_x, pos3, ":x_pos"),
          (position_move_y, pos3, -1000),
          (position_transform_position_to_parent, pos4, pos2, pos1),
          (position_transform_position_to_parent, pos5, pos2, pos3),
          (agent_get_position, pos6, ":cur_agent"),
          (get_distance_between_positions, ":target_distance", pos6, pos4),
          (get_distance_between_positions, ":waypoint_distance", pos6, pos5),
          (try_begin),
            (this_or_next|lt, ":target_distance", ":waypoint_distance"),
            (lt, ":waypoint_distance", 600),
            (agent_set_scripted_destination, ":cur_agent", pos4, 1),
          (else_try),
            (agent_set_scripted_destination, ":cur_agent", pos5, 1),
          (try_end),
          (try_begin),
            (le, ":target_distance", 300),
            (val_add, "$belfry_num_men_pushing", 1),
          (try_end),
##        (else_try),
##          (agent_get_team, ":cur_agent_team", ":cur_agent"),
##          (this_or_next|eq, "$attacker_team", ":cur_agent_team"),
##          (             eq, "$attacker_team_2", ":cur_agent_team"),
##          (try_begin),
##            (gt, ":cur_seconds", 20),
##            (agent_get_position, pos1, ":cur_agent"),
##            (agent_set_scripted_destination, ":cur_agent", pos1, 0),
##          (else_try),
##            (try_begin),
##              (team_get_movement_order, ":order1", "$attacker_team", grc_infantry),
##              (team_get_movement_order, ":order2", "$attacker_team", grc_cavalry),
##              (team_get_movement_order, ":order3", "$attacker_team", grc_archers),
##              (this_or_next|neq, ":order1", mordr_stand_ground),
##              (this_or_next|neq, ":order2", mordr_stand_ground),
##              (neq, ":order3", mordr_stand_ground),
##              (set_show_messages, 0),
##              (team_give_order, "$attacker_team", grc_everyone, mordr_stand_ground),
##              (set_show_messages, 1),
##            (try_end),
##          (try_end),
        (try_end),
      (try_end),
      (try_begin),
        (lt, "$belfry_num_slots_positioned", 6),
        (try_for_agents, ":cur_agent"),
          (agent_is_alive, ":cur_agent"),
          (agent_get_team, ":cur_agent_team", ":cur_agent"),
          (this_or_next|eq, "$attacker_team", ":cur_agent_team"),
          (eq, "$attacker_team_2", ":cur_agent_team"),
          (neq, ":player_agent", ":cur_agent"),
          (agent_get_class, ":agent_class", ":cur_agent"),
          (this_or_next|eq, ":agent_class", grc_infantry),
          (eq, ":agent_class", grc_cavalry),
          (agent_get_slot, ":x_pos", ":cur_agent", 1),
          (eq, ":x_pos", 0),
          (assign, ":y_pos", 0),
          (try_begin),
            (eq, ":slot_1_positioned", 0),
            (assign, ":x_pos", -600),
            (assign, ":y_pos", 0),
            (val_add, ":slot_1_positioned", 1),
          (else_try),
            (eq, ":slot_2_positioned", 0),
            (assign, ":x_pos", -600),
            (assign, ":y_pos", -200),
            (val_add, ":slot_2_positioned", 1),
          (else_try),
            (eq, ":slot_3_positioned", 0),
            (assign, ":x_pos", -600),
            (assign, ":y_pos", -400),
            (val_add, ":slot_3_positioned", 1),
          (else_try),
            (eq, ":slot_4_positioned", 0),
            (assign, ":x_pos", 600),
            (assign, ":y_pos", 0),
            (val_add, ":slot_4_positioned", 1),
          (else_try),
            (eq, ":slot_5_positioned", 0),
            (assign, ":x_pos", 600),
            (assign, ":y_pos", -200),
            (val_add, ":slot_5_positioned", 1),
          (else_try),
            (eq, ":slot_6_positioned", 0),
            (assign, ":x_pos", 600),
            (assign, ":y_pos", -400),
            (val_add, ":slot_6_positioned", 1),
          (try_end),
          (val_add, "$belfry_num_slots_positioned", 1),
          (agent_set_slot, ":cur_agent", 1, ":x_pos"),
          (agent_set_slot, ":cur_agent", 2, ":y_pos"),
        (try_end),
      (try_end),
      (try_begin),
        (store_mission_timer_a, ":cur_timer"),
        (gt, ":cur_timer", 20),
        (lt, "$belfry_num_slots_positioned", 6),
        (try_for_agents, ":cur_agent"),
          (agent_is_alive, ":cur_agent"),
          (agent_get_team, ":cur_agent_team", ":cur_agent"),
          (this_or_next|eq, "$attacker_team", ":cur_agent_team"),
          (             eq, "$attacker_team_2", ":cur_agent_team"),
          (neq, ":player_agent", ":cur_agent"),
          (agent_get_slot, ":x_pos", ":cur_agent", 1),
          (eq, ":x_pos", 0),
          (assign, ":y_pos", 0),
          (try_begin),
            (eq, ":slot_1_positioned", 0),
            (assign, ":x_pos", -600),
            (assign, ":y_pos", 0),
            (val_add, ":slot_1_positioned", 1),
          (else_try),
            (eq, ":slot_2_positioned", 0),
            (assign, ":x_pos", -600),
            (assign, ":y_pos", -200),
            (val_add, ":slot_2_positioned", 1),
          (else_try),
            (eq, ":slot_3_positioned", 0),
            (assign, ":x_pos", -600),
            (assign, ":y_pos", -400),
            (val_add, ":slot_3_positioned", 1),
          (else_try),
            (eq, ":slot_4_positioned", 0),
            (assign, ":x_pos", 600),
            (assign, ":y_pos", 0),
            (val_add, ":slot_4_positioned", 1),
          (else_try),
            (eq, ":slot_5_positioned", 0),
            (assign, ":x_pos", 600),
            (assign, ":y_pos", -200),
            (val_add, ":slot_5_positioned", 1),
          (else_try),
            (eq, ":slot_6_positioned", 0),
            (assign, ":x_pos", 600),
            (assign, ":y_pos", -400),
            (val_add, ":slot_6_positioned", 1),
          (try_end),
          (val_add, "$belfry_num_slots_positioned", 1),
          (agent_set_slot, ":cur_agent", 1, ":x_pos"),
          (agent_set_slot, ":cur_agent", 2, ":y_pos"),
        (try_end),
      (try_end),
    (else_try),
      (assign, ":end_trigger", 1),
      (try_for_agents, ":cur_agent"),
        (agent_clear_scripted_mode, ":cur_agent"),
      (try_end),
      (set_show_messages, 0),
      (team_give_order, "$attacker_team", grc_everyone, mordr_charge),
      (set_show_messages, 1),
    (try_end),
    (eq, ":end_trigger", 1),
  ]),

]

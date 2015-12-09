from compiler import *
from include_mission_triggers import *

####################################################################################################################
#   Each mission-template is a tuple that contains the following fields:
#  1) Mission-template id (string): used for referencing mission-templates in other files.
#     The prefix mt_ is automatically added before each mission-template id
#
#  2) Mission-template flags (int): See header_mission-templates.py for a list of available flags
#  3) Mission-type(int): Which mission types this mission template matches.
#     For mission-types to be used with the default party-meeting system,
#     this should be 'charge' or 'charge_with_ally' otherwise must be -1.
#     
#  4) Mission description text (string).
#  5) List of spawn records (list): Each spawn record is a tuple that contains the following fields:
#    5.1) entry-no: Troops spawned from this spawn record will use this entry
#    5.2) spawn flags.
#    5.3) alter flags. which equipment will be overriden
#    5.4) ai flags.
#    5.5) Number of troops to spawn.
#    5.6) list of equipment to add to troops spawned from here (maximum 8).
#  6) List of triggers (list).
#     See module_triggers.py for infomation about triggers.
#
#  Please note that mission templates is work in progress and can be changed in the future versions.
# 
####################################################################################################################

mission_templates = [
  (
    "town_default",0,-1,
    "Default town visit",
    [(0,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (1,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (3,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (4,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (5,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (6,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (7,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (8,mtef_scene_source,af_override_horse,0,1,[]),
     (9,mtef_scene_source,af_override_horse,0,1,[]),
     (10,mtef_scene_source,af_override_horse,0,1,[]),
     (11,mtef_scene_source,af_override_horse,0,1,[]),
     (12,mtef_scene_source,af_override_horse,0,1,[]),
     (13,mtef_scene_source,0,0,1,[]),
     (14,mtef_scene_source,0,0,1,[]),
     (15,mtef_scene_source,0,0,1,[]),
     (16,mtef_visitor_source,af_override_horse,0,1,[]),
     (17,mtef_visitor_source,af_override_horse,0,1,[]),
     (18,mtef_visitor_source,af_override_horse,0,1,[]),
     (19,mtef_visitor_source,af_override_horse,0,1,[]),
     (20,mtef_visitor_source,af_override_horse,0,1,[]),
     (21,mtef_visitor_source,af_override_horse,0,1,[]),
     (22,mtef_visitor_source,af_override_horse,0,1,[]),
     (23,mtef_visitor_source,af_override_horse,0,1,[]),
     (24,mtef_visitor_source,af_override_horse,0,1,[]),
     (25,mtef_visitor_source,af_override_horse,0,1,[]),
     (26,mtef_visitor_source,af_override_horse,0,1,[]),
     (27,mtef_visitor_source,af_override_horse,0,1,[]),
     (28,mtef_visitor_source,af_override_horse,0,1,[]),
     (29,mtef_visitor_source,af_override_horse,0,1,[]),
     (30,mtef_visitor_source,af_override_horse,0,1,[]),
     (31,mtef_visitor_source,af_override_horse,0,1,[]),
     ],     
     [
      lav_situational_damage_modifiers,
      (1, 0, ti_once, [], 
      [
        (store_current_scene, ":cur_scene"),
        (scene_set_slot, ":cur_scene", slot_scene_visited, 1),
        (try_begin),
          (eq, "$sneaked_into_town", 1),
          (call_script, "script_music_set_situation_with_culture", mtf_sit_town_infiltrate),
        (else_try),
          (eq, "$talk_context", tc_tavern_talk),
          (call_script, "script_music_set_situation_with_culture", mtf_sit_tavern),
        (else_try),
          (call_script, "script_music_set_situation_with_culture", mtf_sit_town),
        (try_end),
      ]),

# NE minstrel 
# Josef v586 - minstrel attack		   # NE Minstrel potential issue
		
   # TODO: MINSTREL ATTACK
   #(0.40, 0, 0, [], [
   # (try_for_agents, ":agent"),
   #   (agent_is_alive, ":agent"),
   #   (agent_is_human, ":agent"),
   #   (agent_get_wielded_item, ":handone", ":agent", 0),
   #   (agent_get_wielded_item, ":handtwo", ":agent", 1),
   #   (this_or_next|eq, ":handone", "itm_mandolin"),
   #   (eq, ":handtwo", "itm_mandolin"),
   #   (agent_get_combat_state, ":state", ":agent"),
   #   (try_begin),
   #     (eq,":state",4), #This is the combat state for melee swing
   #     (agent_slot_eq,":agent",slot_agent_attack_sound, 0),
   #     (agent_set_slot, ":agent", slot_agent_attack_sound, 1),
   #     (agent_play_sound,":agent","snd_gsh"),
   #   (else_try),
   #     (neq,":state",4),
   #     (agent_set_slot, ":agent", slot_agent_attack_sound, 0),
   #   (try_end),
   # (try_end),
   #]),
# NE End

   
      (ti_before_mission_start, 0, 0, [], 
      [
        (call_script, "script_change_banners_and_chest"),
        (call_script, "script_initialize_tavern_variables"),
	  ]),

      (ti_inventory_key_pressed, 0, 0, 
      [
        (set_trigger_result,1)
      ], []),
      
      #tavern - belligerent drunk leaving/fading out
      (1, 0, 0, 
      [
        (gt, "$g_belligerent_drunk_leaving", 0),
        (entry_point_get_position, pos0, 0),
        (agent_get_position, pos1, "$g_belligerent_drunk_leaving"),
        (get_distance_between_positions, ":dist", pos0, pos1),
        (le, ":dist", 150),
      ],
      [
        (agent_fade_out, "$g_belligerent_drunk_leaving"),
        (assign, "$g_belligerent_drunk_leaving", 0),
      ]),
      
      (ti_tab_pressed, 0, 0, 
      [
        (try_begin),
          (eq, "$g_main_attacker_agent", 0),
          (set_trigger_result, 1),
        (try_end),  
      ], []),

	  #tavern brawl triggers - drunk
      (2, 0, 0, 
      [
	    (neg|conversation_screen_is_active),

		(eq, "$talk_context", tc_tavern_talk),
		
		(neg|troop_slot_eq, "trp_hired_assassin", slot_troop_cur_center, "$g_encountered_party"),		
		(troop_slot_eq, "trp_belligerent_drunk", slot_troop_cur_center, "$g_encountered_party"),		
		(eq, "$drunks_dont_pick_fights", 0),		
	  ], 
	  [	  
	    (try_begin),
	      (eq, "$g_start_belligerent_drunk_fight", 0),
	      (assign, "$g_start_belligerent_drunk_fight", 1),
	      
	      (try_for_agents, ":cur_agent"),
	        (agent_get_troop_id, ":cur_agent_troop", ":cur_agent"),
	        (eq, ":cur_agent_troop", "trp_belligerent_drunk"),
	        (assign, "$g_belligerent_drunk", ":cur_agent"),
	      (try_end),
	    (else_try),
	      (eq, "$g_start_belligerent_drunk_fight", 1),	 
	           
	      (agent_is_active, "$g_belligerent_drunk"),
	      (agent_is_alive, "$g_belligerent_drunk"),
	      (get_player_agent_no, ":player_agent"),
	      (agent_get_position, pos0, ":player_agent"),
	      (agent_get_position, pos1, "$g_belligerent_drunk"),
	      (get_distance_between_positions, ":dist", pos0, pos1),
	      (position_get_z, ":pos0_z", pos0),
	      (position_get_z, ":pos1_z", pos1),
	      (store_sub, ":z_difference", ":pos1_z", ":pos0_z"),
	      (try_begin),
	        (le, ":z_difference", 0),
	        (val_mul, ":z_difference", -1),
	      (try_end),
	      (store_mul, ":z_difference_mul_3", ":z_difference", 3),
	      (val_add, ":dist", ":z_difference_mul_3"),
	      (store_random_in_range, ":random_value", 0, 200),
	      (store_add, ":400_plus_random_200", 400, ":random_value"),
	      (le, ":dist", ":400_plus_random_200"),
	      
 		  (call_script, "script_activate_tavern_attackers"),
  		  (start_mission_conversation, "trp_belligerent_drunk"),
  		  (assign, "$g_start_belligerent_drunk_fight", 2),
	    (try_end),  
	  ]),
	  	  
	  #tavern brawl triggers - assassin
      (2, 0, 0, [
	    (neg|conversation_screen_is_active),
		(eq, "$talk_context", tc_tavern_talk),
		(troop_slot_eq, "trp_hired_assassin", slot_troop_cur_center, "$g_encountered_party"),		
	  ], 
	  [
	    (try_begin),
	      (eq, "$g_start_hired_assassin_fight", 0),
	      (assign, "$g_start_hired_assassin_fight", 1),
	      
	      (try_for_agents, ":cur_agent"),
	        (agent_get_troop_id, ":cur_agent_troop", ":cur_agent"),
	        (eq, ":cur_agent_troop", "trp_hired_assassin"),
	        (assign, "$g_hired_assassin", ":cur_agent"),
	      (try_end),	      
	    (else_try),  
	      (eq, "$g_start_hired_assassin_fight", 1),

	      (agent_is_active, "$g_hired_assassin"),
	      (agent_is_alive, "$g_hired_assassin"),
	      (get_player_agent_no, ":player_agent"),
	      (agent_get_position, pos0, ":player_agent"),
	      (agent_get_position, pos1, "$g_hired_assassin"),
	      (get_distance_between_positions, ":dist", pos0, pos1),
	      (position_get_z, ":pos0_z", pos0),
	      (position_get_z, ":pos1_z", pos1),
	      (store_sub, ":z_difference", ":pos1_z", ":pos0_z"),
	      (try_begin),
	        (le, ":z_difference", 0),
	        (val_mul, ":z_difference", -1),
	      (try_end),
	      (store_mul, ":z_difference_mul_3", ":z_difference", 3),
	      (val_add, ":dist", ":z_difference_mul_3"),
	      (store_random_in_range, ":random_value", 0, 200),
	      (store_add, ":400_plus_random_200", 400, ":random_value"),
	      (le, ":dist", ":400_plus_random_200"),

		  (call_script, "script_activate_tavern_attackers"),
		  (assign, "$g_start_hired_assassin_fight", 2),
		(try_end),  
	  ]),
	  	  
	  #Aftermath talks
      (3, 0, ti_once, 
      [
	    (neg|conversation_screen_is_active),
		(eq, "$talk_context", tc_tavern_talk),
		(gt, "$g_main_attacker_agent", 0),
				
		(this_or_next|neg|agent_is_alive, "$g_main_attacker_agent"),
		(agent_is_wounded, "$g_main_attacker_agent"),
      ],
      [
        (mission_enable_talk),
      
		(try_for_agents, ":agent"),
		  (agent_is_alive, ":agent"),
		  (agent_get_position, pos4, ":agent"),
		  (agent_set_scripted_destination, ":agent", pos4),
		(try_end),
		
		(party_get_slot, ":tavernkeeper", "$g_encountered_party", slot_town_tavernkeeper),
		(start_mission_conversation, ":tavernkeeper"),	 
	  ]),

	  
	  #Aftermath talks
      (3, 0, ti_once, 
      [
	    (neg|conversation_screen_is_active),
		(eq, "$talk_context", tc_tavern_talk),
		(gt, "$g_main_attacker_agent", 0),
		(main_hero_fallen),		
      ],
      [
	  (jump_to_menu, "mnu_lost_tavern_duel"),
	  (finish_mission,0)
	  
	  ]),	  
	  
	  
	  #No shooting in the tavern
      (1, 0, 0, 
      [
	    (neg|conversation_screen_is_active),
		(eq, "$talk_context", tc_tavern_talk),
		(gt, "$g_main_attacker_agent", 0),
		
		(get_player_agent_no, ":player_agent"),
		(agent_is_alive, ":player_agent"),
		
		(agent_get_wielded_item, ":wielded_item", ":player_agent", 0),
		(item_get_type, ":item_type", ":wielded_item"),
		(this_or_next|eq, ":item_type", itp_type_bow),
		(this_or_next|eq, ":item_type", itp_type_crossbow),
		(             eq, ":item_type", itp_type_thrown),
      ], 
      [
		(party_get_slot, ":tavernkeeper", "$g_encountered_party", slot_town_tavernkeeper),
		(start_mission_conversation, ":tavernkeeper"),	 
	  ]),
	  	  	  
	  #Check for weapon in hand of attacker, also, everyone gets out of the way
      (1, 0, 0, 
      [
		(gt, "$g_main_attacker_agent", 0),	
      ],
      [
        (agent_get_wielded_item, ":wielded_item", "$g_main_attacker_agent", 0),
        (val_max, "$g_attacker_drawn_weapon", ":wielded_item"),               
        
        (call_script, "script_neutral_behavior_in_fight"),
      ]),	  			
    ],
  ),

  

   # NE Minstrel potential issue
      # (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),
      # (ti_inventory_key_pressed, 0, 0, [(set_trigger_result,1)], []),
      # (ti_tab_pressed, 0, 0, [(set_trigger_result,1)], []),
    # ],
  # ),

# NE end minstrel
# This template is used in party encounters and such.
# 
  (
    "conversation_encounter",0,-1,
    "Conversation_encounter",
    [( 0,mtef_visitor_source,af_override_fullhelm,0,1,[]),( 1,mtef_visitor_source,af_override_fullhelm,0,1,[]),
     ( 2,mtef_visitor_source,af_override_fullhelm,0,1,[]),( 3,mtef_visitor_source,af_override_fullhelm,0,1,[]),( 4,mtef_visitor_source,af_override_fullhelm,0,1,[]),( 5,mtef_visitor_source,af_override_fullhelm,0,1,[]),( 6,mtef_visitor_source,af_override_fullhelm,0,1,[]),
     ( 7,mtef_visitor_source,af_override_fullhelm,0,1,[]),( 8,mtef_visitor_source,af_override_fullhelm,0,1,[]),( 9,mtef_visitor_source,af_override_fullhelm,0,1,[]),(10,mtef_visitor_source,af_override_fullhelm,0,1,[]),(11,mtef_visitor_source,af_override_fullhelm,0,1,[]),
    #prisoners now...
     (12,mtef_visitor_source,af_override_fullhelm,0,1,[]),(13,mtef_visitor_source,af_override_fullhelm,0,1,[]),(14,mtef_visitor_source,af_override_fullhelm,0,1,[]),(15,mtef_visitor_source,af_override_fullhelm,0,1,[]),(16,mtef_visitor_source,af_override_fullhelm,0,1,[]),
    #Other party
     (17,mtef_visitor_source,af_override_fullhelm,0,1,[]),(18,mtef_visitor_source,af_override_fullhelm,0,1,[]),(19,mtef_visitor_source,af_override_fullhelm,0,1,[]),(20,mtef_visitor_source,af_override_fullhelm,0,1,[]),(21,mtef_visitor_source,af_override_fullhelm,0,1,[]),
     (22,mtef_visitor_source,af_override_fullhelm,0,1,[]),(23,mtef_visitor_source,af_override_fullhelm,0,1,[]),(24,mtef_visitor_source,af_override_fullhelm,0,1,[]),(25,mtef_visitor_source,af_override_fullhelm,0,1,[]),(26,mtef_visitor_source,af_override_fullhelm,0,1,[]),
     (27,mtef_visitor_source,af_override_fullhelm,0,1,[]),(28,mtef_visitor_source,af_override_fullhelm,0,1,[]),(29,mtef_visitor_source,af_override_fullhelm,0,1,[]),(30,mtef_visitor_source,af_override_fullhelm,0,1,[]),(31,mtef_visitor_source,af_override_fullhelm,0,1,[]),
     ],
    [],
  ),
  
#----------------------------------------------------------------
#mission templates before this point are hardwired into the game.
#-----------------------------------------------------------------

  (
    "town_center",0,-1,
    "Default town visit",
    [(0,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (1,mtef_scene_source|mtef_team_0,0,0,1,[]),
     (2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (3,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (4,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (5,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (6,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (7,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),     
     (8,mtef_visitor_source,af_override_horse,0,1,[]),
     (9,mtef_visitor_source,af_override_horse,0,1,[]),(10,mtef_visitor_source,af_override_horse,0,1,[]),(11,mtef_visitor_source,af_override_horse,0,1,[]),(12,mtef_visitor_source,af_override_horse,0,1,[]),(13,mtef_visitor_source,0,0,1,[]),(14,mtef_scene_source,0,0,1,[]),(15,mtef_scene_source,0,0,1,[]),
     (16,mtef_visitor_source,af_override_horse,0,1,[]),(17,mtef_visitor_source,af_override_horse,0,1,[]),(18,mtef_visitor_source,af_override_horse,0,1,[]),(19,mtef_visitor_source,af_override_horse,0,1,[]),(20,mtef_visitor_source,af_override_horse,0,1,[]),(21,mtef_visitor_source,af_override_horse,0,1,[]),(22,mtef_visitor_source,af_override_horse,0,1,[]),
	 (23,mtef_visitor_source,af_override_horse,0,1,[]), #guard
     (24,mtef_visitor_source,af_override_horse,0,1,[]), #guard
	 (25,mtef_visitor_source,af_override_horse,0,1,[]), #guard
	 (26,mtef_visitor_source,af_override_horse,0,1,[]), #guard
	 (27,mtef_visitor_source,af_override_horse,0,1,[]), #guard
	 (28,mtef_visitor_source,af_override_horse,0,1,[]), #guard
	 (29,mtef_visitor_source,af_override_horse,0,1,[]),
	 (30,mtef_visitor_source,af_override_horse,0,1,[]),
	 (31,mtef_visitor_source,af_override_horse,0,1,[]),
     (32,mtef_visitor_source,af_override_horse,0,1,[]),
	 (33,mtef_visitor_source,af_override_horse,0,1,[]),
	 (34,mtef_visitor_source,af_override_horse,0,1,[]),
	 (35,mtef_visitor_source,af_override_horse,0,1,[]),
	 (36,mtef_visitor_source,af_override_horse,0,1,[]), #town walker point
	 (37,mtef_visitor_source,af_override_horse,0,1,[]), #town walker point
	 (38,mtef_visitor_source,af_override_horse,0,1,[]),
	 (39,mtef_visitor_source,af_override_horse,0,1,[]),
     (40,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]), #in towns, can be used for guard reinforcements
	 (41,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]), #in towns, can be used for guard reinforcements
	 (42,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]), #in towns, can be used for guard reinforcements
	 (43,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]), #in towns, can be used for guard reinforcements
     (44,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (45,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (46,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (47,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     ],
    [
      lav_situational_damage_modifiers,
      lav_replace_horse_props_with_spawn_markers,
      lav_activate_spawn_markers,

      #common_init_deathcam,
      #manual_start_deathcam,
      #common_move_deathcam,
      #common_rotate_deathcam,

      (ti_on_agent_spawn, 0, 0, [],
      [
        (store_trigger_param_1, ":agent_no"),
        (call_script, "script_init_town_agent", ":agent_no"),
        (try_begin),
          (this_or_next|eq, "$talk_context", tc_escape),
          (eq, "$talk_context", tc_prison_break),
          (agent_get_troop_id, ":troop_no", ":agent_no"),		  
          (troop_slot_eq, ":troop_no", slot_troop_will_join_prison_break, 1),
          (agent_set_team, ":agent_no", 0),
          (agent_ai_set_aggressiveness, ":agent_no", 5),
          (troop_set_slot, ":troop_no", slot_troop_will_join_prison_break, 0),
          (try_begin),
            (troop_slot_eq, ":troop_no", slot_troop_mission_participation, mp_prison_break_stand_back),
            (agent_get_position, pos1, ":agent_no"),            
            (agent_set_scripted_destination, ":agent_no", pos1),
          (try_end),
        (try_end),         
      ]),

      (ti_before_mission_start, 0, 0, [],
      [
        (assign, "$g_main_attacker_agent", 0),
	  ]),
		 
      (1, 0, ti_once, 
      [],
      [
        (try_begin),
          (eq, "$g_mt_mode", tcm_default),
          (store_current_scene, ":cur_scene"),
          (scene_set_slot, ":cur_scene", slot_scene_visited, 1),
        (try_end),
        (call_script, "script_init_town_walker_agents"),
        (try_begin),
          (eq, "$sneaked_into_town", 1),
          (call_script, "script_music_set_situation_with_culture", mtf_sit_town_infiltrate),
        (else_try),
          (call_script, "script_music_set_situation_with_culture", mtf_sit_town),
        (try_end),
      ]),

	  # NE minstrel
# Josef v586 - blong for mandolin	
		
   # TODO: MINSTREL ATTACK
   #(0.40, 0, 0, [], [
   # (try_for_agents, ":agent"),
   #   (agent_is_alive, ":agent"),
   #   (agent_is_human, ":agent"),
   #   (agent_get_wielded_item, ":handone", ":agent", 0),
   #   (agent_get_wielded_item, ":handtwo", ":agent", 1),
   #   (this_or_next|eq, ":handone", "itm_mandolin"),
   #   (eq, ":handtwo", "itm_mandolin"),
   #   (agent_get_combat_state, ":state", ":agent"),
   #   (try_begin),
   #     (eq,":state",4), #This is the combat state for melee swing
   #     (agent_slot_eq,":agent",slot_agent_attack_sound, 0),
   #     (agent_set_slot, ":agent", slot_agent_attack_sound, 1),
   #     (agent_play_sound,":agent","snd_gsh"),
   #   (else_try),
   #     (neq,":state",4),
   #     (agent_set_slot, ":agent", slot_agent_attack_sound, 0),
   #   (try_end),
   # (try_end),
   #]),	  
	  # nE end minstrel
	  
      (ti_before_mission_start, 0, 0, 
      [], 
      [
        (call_script, "script_change_banners_and_chest")
      ]),
        
      (ti_inventory_key_pressed, 0, 0,
      [
        (try_begin),
          (eq, "$g_mt_mode", tcm_default),
          (set_trigger_result,1),
        (else_try),
          (eq, "$g_mt_mode", tcm_disguised),
          (display_message,"str_cant_use_inventory_disguised"),
        (else_try),
          (display_message, "str_cant_use_inventory_now"),
        (try_end),
      ], 
      []),
       
      (ti_tab_pressed, 0, 0,
      [
        (try_begin),
          (this_or_next|eq, "$talk_context", tc_escape),
          (eq, "$talk_context", tc_prison_break),
          (display_message, "str_cannot_leave_now"),
        (else_try),
          (this_or_next|eq, "$g_mt_mode", tcm_default),
          (eq, "$g_mt_mode", tcm_disguised),
          (mission_enable_talk),
          (set_trigger_result,1),
        (else_try),
          (display_message, "str_cannot_leave_now"),
        (try_end),
      ], 
      []),

      (ti_on_leave_area, 0, 0,
      [
        (try_begin),
          (eq, "$g_defending_against_siege", 0),
          (assign,"$g_leave_town",1),
        (try_end),			
      ], 
      [
        (try_begin),
          (eq, "$talk_context", tc_escape),
          (call_script, "script_deduct_casualties_from_garrison"),
          (jump_to_menu,"mnu_sneak_into_town_caught_dispersed_guards"),
        (try_end),
        
        (mission_enable_talk),
      ]),            

     (0, 0, ti_once, 
     [], 
     [
       (party_slot_eq, "$current_town", slot_party_type, spt_town),
       (call_script, "script_town_init_doors", 0),
       (try_begin),
         (eq, "$town_nighttime", 0),
         (play_sound, "snd_town_ambiance", sf_looping),
       (try_end),
     ]),

	(3, 0, 0, 
	[
	  (call_script, "script_tick_town_walkers")
	], 
	[]),
	
    (2, 0, 0, 
    [
      (call_script, "script_center_ambiance_sounds")
    ], 
    []),
		
	#JAILBREAK TRIGGERS 
	#Civilians get out of the way
    (1, 0, 0,
	[
	  (this_or_next|eq, "$talk_context", tc_prison_break),
      (eq, "$talk_context", tc_escape),		
	],
	[
	  #(agent_get_team, ":prisoner_agent", 0),
	  (call_script, "script_neutral_behavior_in_fight"),
	  (mission_disable_talk),	  	  
	]),

	#The game begins with the town alerted
    (1, 0, ti_once, 
      [
        #If I set this to 1, 0, ti_once, then the prisoner spawns twice
        (eq, "$talk_context", tc_escape),
	  ],	  
	  [
		(get_player_agent_no, ":player_agent"),
	    (assign, reg6, ":player_agent"),
		(call_script, "script_activate_town_guard"),		
		
		(get_player_agent_no, ":player_agent"),
		(agent_get_position, pos4, ":player_agent"),
		
		(try_for_range, ":prisoner", active_npcs_begin, kingdom_ladies_end),		
		  (troop_slot_ge, ":prisoner", slot_troop_mission_participation, mp_prison_break_fight),

		  (str_store_troop_name, s4, ":prisoner"),
		  (display_message, "str_s4_joins_prison_break"),
			
		  (store_current_scene, ":cur_scene"), #this might be a better option?
		  (modify_visitors_at_site, ":cur_scene"),
			            
          #<entry_no>,<troop_id>,<number_of_troops>, <team_no>, <group_no>), 
          #team no and group no are used in multiplayer mode only. default team in entry is used in single player mode            
          (store_current_scene, ":cur_scene"),
          (modify_visitors_at_site, ":cur_scene"),                      
          (add_visitors_to_current_scene, 24, ":prisoner", 1, 0, 0),
          (troop_set_slot, ":prisoner", slot_troop_will_join_prison_break, 1),					          
        (try_end),
	  ]),
	
   (3, 0, 0, 
   [     
     (main_hero_fallen, 0),
   ],	  
   [
     (try_begin),
       (this_or_next|eq, "$talk_context", tc_prison_break),
       (eq, "$talk_context", tc_escape),
       
       (call_script, "script_deduct_casualties_from_garrison"),
	   (jump_to_menu,"mnu_captivity_start_castle_defeat"), 
	 
	   (assign, ":end_cond", kingdom_ladies_end),
       (try_for_range, ":prisoner", active_npcs_begin, ":end_cond"),
  	     (troop_set_slot, ":prisoner", slot_troop_mission_participation, 0), #new	  
  	   (try_end),  
	 
	   (mission_enable_talk),
	   (finish_mission, 0),
	 (else_try),  
	   (set_trigger_result,1),
	 (try_end),	 	 
   ]),
		
   (3, 0, 0, 
   [
     (eq, "$talk_context", tc_escape),
	 (neg|main_hero_fallen,0),
     (store_mission_timer_a, ":time"),
     (ge, ":time", 10),
		
     (all_enemies_defeated), #1 is default enemy team for in-town battles
   ],	  
   [
     (call_script, "script_deduct_casualties_from_garrison"),
	 (try_for_agents, ":agent"),
	 (agent_get_troop_id, ":troop", ":agent"),
       (troop_slot_ge, ":troop", slot_troop_mission_participation, mp_prison_break_fight),
       (try_begin),
         (agent_is_alive, ":agent"),
         (troop_set_slot, ":troop", slot_troop_mission_participation, mp_prison_break_escaped),
       (else_try),	
         (troop_set_slot, ":troop", slot_troop_mission_participation, mp_prison_break_caught),
       (try_end),
     (try_end),
     (jump_to_menu,"mnu_sneak_into_town_caught_ran_away"),
     
     (mission_enable_talk),
     (finish_mission,0)
   ]),
   
   (ti_on_agent_killed_or_wounded, 0, 0, [],
   [
     (store_trigger_param_1, ":dead_agent_no"),
     (store_trigger_param_2, ":killer_agent_no"),
     #(store_trigger_param_3, ":is_wounded"),
        
     (agent_get_troop_id, ":dead_agent_troop_no", ":dead_agent_no"),
     (agent_get_troop_id, ":killer_agent_troop_no", ":killer_agent_no"),
                
     (try_begin), 
       (this_or_next|eq, ":dead_agent_troop_no", "trp_swadian_prison_guard"),
       (this_or_next|eq, ":dead_agent_troop_no", "trp_vaegir_prison_guard"),
       (this_or_next|eq, ":dead_agent_troop_no", "trp_khergit_prison_guard"),
       (this_or_next|eq, ":dead_agent_troop_no", "trp_nord_prison_guard"),
       (this_or_next|eq, ":dead_agent_troop_no", "trp_rhodok_prison_guard"),
       (eq, ":dead_agent_troop_no", "trp_sarranid_prison_guard"),
          
       (eq, ":killer_agent_troop_no", "trp_player"),
          
       (display_message, "@You got keys of dungeon."),
     (try_end),
   ]),     
  ]),

  (
    "village_center",0,-1,
    "village center",
    [(0,mtef_scene_source|mtef_team_0,0,0,1,[]),
     (1,mtef_scene_source|mtef_team_0,0,0,1,[]),
     (2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (3,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (4,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (5,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (6,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (7,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     
     (8,mtef_visitor_source,af_override_horse,0,1,[]),
     (9,mtef_visitor_source,af_override_horse,0,1,[]),(10,mtef_visitor_source,af_override_horse,0,1,[]),(11,mtef_visitor_source,af_override_horse,0,1,[]),(12,mtef_visitor_source,af_override_horse,0,1,[]),(13,mtef_visitor_source,0,0,1,[]),(14,mtef_visitor_source,0,0,1,[]),(15,mtef_visitor_source,0,0,1,[]),
     (16,mtef_visitor_source,af_override_horse,0,1,[]),(17,mtef_visitor_source,af_override_horse,0,1,[]),(18,mtef_visitor_source,af_override_horse,0,1,[]),(19,mtef_visitor_source,af_override_horse,0,1,[]),(20,mtef_visitor_source,af_override_horse,0,1,[]),(21,mtef_visitor_source,af_override_horse,0,1,[]),(22,mtef_visitor_source,af_override_horse,0,1,[]),(23,mtef_visitor_source,af_override_horse,0,1,[]),
     (24,mtef_visitor_source,af_override_horse,0,1,[]),(25,mtef_visitor_source,af_override_horse,0,1,[]),(26,mtef_visitor_source,af_override_horse,0,1,[]),(27,mtef_visitor_source,af_override_horse,0,1,[]),(28,mtef_visitor_source,af_override_horse,0,1,[]),(29,mtef_visitor_source,af_override_horse,0,1,[]),(30,mtef_visitor_source,af_override_horse,0,1,[]),(31,mtef_visitor_source,af_override_horse,0,1,[]),
     (32,mtef_visitor_source,af_override_horse,0,1,[]),(33,mtef_visitor_source,af_override_horse,0,1,[]),(34,mtef_visitor_source,af_override_horse,0,1,[]),(35,mtef_visitor_source,af_override_horse,0,1,[]),(36,mtef_visitor_source,af_override_horse,0,1,[]),(37,mtef_visitor_source,af_override_horse,0,1,[]),(38,mtef_visitor_source,af_override_horse,0,1,[]),(39,mtef_visitor_source,af_override_horse,0,1,[]),
     (40,mtef_visitor_source,af_override_horse,0,1,[]),(41,mtef_visitor_source,af_override_horse,0,1,[]),(42,mtef_visitor_source,af_override_horse,0,1,[]),(43,mtef_visitor_source,af_override_horse,0,1,[]),(44,mtef_visitor_source,af_override_horse,0,1,[]),(45,mtef_visitor_source,af_override_horse,0,1,[]),(46,mtef_visitor_source,af_override_horse,0,1,[]),(47,mtef_visitor_source,af_override_horse,0,1,[]),
     ],
    [

      lav_situational_damage_modifiers,
      lav_replace_horse_props_with_spawn_markers,
      lav_activate_spawn_markers,



      (1, 0, ti_once, [], [
          (store_current_scene, ":cur_scene"),
          (scene_set_slot, ":cur_scene", slot_scene_visited, 1),
          (call_script, "script_init_town_walker_agents"),
          (call_script, "script_music_set_situation_with_culture", mtf_sit_travel),
        ]),
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),
      (ti_inventory_key_pressed, 0, 0, [(set_trigger_result,1)], []),
      (ti_tab_pressed, 0, 0, [(try_begin),
                                (check_quest_active, "qst_hunt_down_fugitive"),
                                (neg|check_quest_succeeded, "qst_hunt_down_fugitive"),
                                (neg|check_quest_failed, "qst_hunt_down_fugitive"),
                                (quest_slot_eq, "qst_hunt_down_fugitive", slot_quest_current_state, 1),
                                (try_begin),
                                  (call_script, "script_cf_troop_agent_is_alive", "trp_fugitive"),
                                  (call_script, "script_fail_quest", "qst_hunt_down_fugitive"),
                                (else_try),
                                  (call_script, "script_succeed_quest", "qst_hunt_down_fugitive"),
                                (try_end),
                              (try_end),
                              (set_trigger_result,1)], []),
      (ti_on_leave_area, 0, 0, [
          (try_begin),
            (assign,"$g_leave_town",1),
          (try_end),
          ], []),
      (3, 0, 0, [(call_script, "script_tick_town_walkers")], []),
      (2, 0, 0, [(call_script, "script_center_ambiance_sounds")], []),

      (1, 0, ti_once, [(check_quest_active, "qst_hunt_down_fugitive"),
                       (neg|check_quest_succeeded, "qst_hunt_down_fugitive"),
                       (neg|check_quest_failed, "qst_hunt_down_fugitive"),
                       (quest_slot_eq, "qst_hunt_down_fugitive", slot_quest_current_state, 1),
                       (assign, ":not_alive", 0),
                       (try_begin),
                         (call_script, "script_cf_troop_agent_is_alive", "trp_fugitive"),
                       (else_try),
                         (assign, ":not_alive", 1),
                       (try_end),
                       (this_or_next|main_hero_fallen),
                       (eq, ":not_alive", 1),
                       ],
       [(try_begin),
          (main_hero_fallen),
          (jump_to_menu, "mnu_village_hunt_down_fugitive_defeated"),
          (call_script, "script_fail_quest", "qst_hunt_down_fugitive"),
          (finish_mission, 4),
        (else_try),
          (call_script, "script_change_player_relation_with_center", "$current_town", -2),
          (call_script, "script_succeed_quest", "qst_hunt_down_fugitive"),
        (try_end),
        ]),
    ],
  ),

  (
    "bandits_at_night",0,-1,
    "Default town visit",
    # Begin NE Bandit ambush reinforcements
    # The first entry point is used for the player, and also controls how many agents spawn on your team. Just adding the mtef_use_exact_number directive, however,
    # results in duplicates of the player spawning. You also need to use directive mtef_use_exact_number and remove mtef_scene_source. The last item in the tuple
    # is a list and seems to be unused in this template. The item just before last is the number of player agents. Original line:
    # [(0,mtef_scene_source|mtef_team_0, af_override_horse, aif_start_alarmed, 1, pilgrim_disguise),
    # Our change begins:
    [(0,mtef_team_0|mtef_use_exact_number, af_override_horse, aif_start_alarmed, 3, []),
     (1,mtef_scene_source|mtef_team_0,0,0,1,[]),
     (2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (3,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (4,mtef_visitor_source|mtef_team_0, af_override_horse, aif_start_alarmed, 1, []),
     (5,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (6,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (7,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     
     (8,mtef_scene_source,af_override_horse,0,1,[]),
     (9,mtef_visitor_source,af_override_horse,0,1,[]),(10,mtef_visitor_source,af_override_horse,0,1,[]),(11,mtef_visitor_source,af_override_horse,aif_start_alarmed,1,[]),(12,mtef_visitor_source,af_override_horse,0,1,[]),(13,mtef_scene_source,0,0,1,[]),(14,mtef_scene_source,0,0,1,[]),(15,mtef_scene_source,0,0,1,[]),
     (16,mtef_visitor_source,af_override_horse,0,1,[]),(17,mtef_visitor_source,af_override_horse,0,1,[]),(18,mtef_visitor_source,af_override_horse,0,1,[]),(19,mtef_visitor_source,af_override_horse,0,1,[]),(20,mtef_visitor_source,af_override_horse,0,1,[]),(21,mtef_visitor_source,af_override_horse,0,1,[]),(22,mtef_visitor_source,af_override_horse,0,1,[]),(23,mtef_visitor_source,af_override_horse,0,1,[]),
     (24,mtef_visitor_source,af_override_horse,0,1,[]),(25,mtef_visitor_source,af_override_horse,0,1,[]),(26,mtef_visitor_source,af_override_horse,0,1,[]),(27,mtef_visitor_source,af_override_horse,aif_start_alarmed,1,[]),(28,mtef_visitor_source,af_override_horse,aif_start_alarmed,1,[]),(29,mtef_visitor_source,af_override_horse,0,1,[]),(30,mtef_visitor_source,af_override_horse,0,1,[]),(31,mtef_visitor_source,af_override_horse,0,1,[]),
     (32,mtef_visitor_source,af_override_horse,0,1,[]),(33,mtef_visitor_source,af_override_horse,0,1,[]),(34,mtef_visitor_source,af_override_horse,0,1,[]),(35,mtef_visitor_source,af_override_horse,0,1,[]),(36,mtef_visitor_source,af_override_horse,0,1,[]),(37,mtef_visitor_source,af_override_horse,0,1,[]),(38,mtef_visitor_source,af_override_horse,0,1,[]),(39,mtef_visitor_source,af_override_horse,0,1,[]),
     (40,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(41,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(42,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(43,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (44,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(45,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(46,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(47,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     ],
    [
      lav_situational_damage_modifiers,
      (ti_on_agent_spawn, 0, 0, [],
       [
         # We also need to change the spawn code. By default it just assigns any agent who isn't the player to team 1 (default enemy team)
         # Instead we need to inspect each agent and assign them a team appropriately
         # Original code:
         # (store_trigger_param_1, ":agent_no"),
         # (agent_get_troop_id, ":troop_no", ":agent_no"),
         # (neq, ":troop_no", "trp_player"),
         # (agent_set_team, ":agent_no", 1),
         (store_trigger_param_1, ":agent_no"),
         (agent_get_troop_id, ":troop_no", ":agent_no"),
         (try_begin),
           (main_party_has_troop, ":troop_no"), # troop is present in our party
           (agent_set_team, ":agent_no", 0),
         (try_end),
         (try_begin),
           (neg|main_party_has_troop, ":troop_no"), # troop isn't in our party
           (agent_set_team, ":agent_no", 1),
         (try_end),
         ]),
    # End NE Bandit ambush reinforcements


		 
		 	  # NE minstrel
# Josef v586 - blong for mandolin	
		
   # TODO: MINSTREL ATTACK
   #(0.40, 0, 0, [], [
   # (try_for_agents, ":agent"),
   #   (agent_is_alive, ":agent"),
   #   (agent_is_human, ":agent"),
   #   (agent_get_wielded_item, ":handone", ":agent", 0),
   #   (agent_get_wielded_item, ":handtwo", ":agent", 1),
   #   (this_or_next|eq, ":handone", "itm_mandolin"),
   #   (eq, ":handtwo", "itm_mandolin"),
   #   (agent_get_combat_state, ":state", ":agent"),
   #   (try_begin),
   #     (eq,":state",4), #This is the combat state for melee swing
   #     (agent_slot_eq,":agent",slot_agent_attack_sound, 0),
   #     (agent_set_slot, ":agent", slot_agent_attack_sound, 1),
   #     (agent_play_sound,":agent","snd_gsh"),
   #   (else_try),
   #     (neq,":state",4),
   #     (agent_set_slot, ":agent", slot_agent_attack_sound, 0),
   #   (try_end),
   # (try_end),
   #]),	  
	  # nE end minstrel
	  
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),

      common_inventory_not_available,
      
      (ti_tab_pressed, 0, 0,
       [
         (display_message, "str_cannot_leave_now"),
         ], []),
      (ti_on_leave_area, 0, 0,
       [
         (try_begin),
           (eq, "$g_defending_against_siege", 0),
           (assign,"$g_leave_town",1),
         (try_end),
         ], []),

      (0, 0, ti_once, [],
       [
         (call_script, "script_music_set_situation_with_culture", mtf_sit_ambushed),
         (set_party_battle_mode),
         (party_slot_eq, "$current_town", slot_party_type, spt_town),
         (call_script, "script_town_init_doors", 0),
        ]),

      (1, 4, ti_once,
       [
         (store_mission_timer_a,":cur_time"),
         (ge, ":cur_time", 5),
         (this_or_next|main_hero_fallen),
         (num_active_teams_le,1)
         ],
       [
         (try_begin),
           (main_hero_fallen),
           (jump_to_menu, "mnu_town_bandits_failed"),
         (else_try),
           (jump_to_menu, "mnu_town_bandits_succeeded"),
         (try_end),
         (finish_mission),
         ]),
      ],
    ),

	# NE assassins
	# Josef 586 Assassins! 
  (
    "assassins",0,-1,
    "Default town visit",
    [#(0,mtef_scene_source|mtef_team_0, af_override_horse, 0, 1, pilgrim_disguise), # change this to override horse only.
	 (0,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (1,mtef_scene_source|mtef_team_0,0,0,1,[]),
     (2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (3,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (4,mtef_visitor_source|mtef_team_0, af_override_horse, aif_start_alarmed, 1, []),
     (5,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (6,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (7,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     
     (8,mtef_scene_source,af_override_horse,0,1,[]),
     (9,mtef_visitor_source,af_override_horse,0,1,[]),(10,mtef_visitor_source,af_override_horse,0,1,[]),(11,mtef_visitor_source,af_override_horse,aif_start_alarmed,1,[]),(12,mtef_visitor_source,af_override_horse,0,1,[]),(13,mtef_scene_source,0,0,1,[]),(14,mtef_scene_source,0,0,1,[]),(15,mtef_scene_source,0,0,1,[]),
     (16,mtef_visitor_source,af_override_horse,0,1,[]),(17,mtef_visitor_source,af_override_horse,0,1,[]),(18,mtef_visitor_source,af_override_horse,0,1,[]),(19,mtef_visitor_source,af_override_horse,0,1,[]),(20,mtef_visitor_source,af_override_horse,0,1,[]),(21,mtef_visitor_source,af_override_horse,0,1,[]),(22,mtef_visitor_source,af_override_horse,0,1,[]),(23,mtef_visitor_source,af_override_horse,0,1,[]),
     (24,mtef_visitor_source,af_override_horse,0,1,[]),(25,mtef_visitor_source,af_override_horse,0,1,[]),(26,mtef_visitor_source,af_override_horse,0,1,[]),(27,mtef_visitor_source,af_override_horse,aif_start_alarmed,1,[]),(28,mtef_visitor_source,af_override_horse,aif_start_alarmed,1,[]),(29,mtef_visitor_source,af_override_horse,0,1,[]),(30,mtef_visitor_source,af_override_horse,0,1,[]),(31,mtef_visitor_source,af_override_horse,0,1,[]),
     (32,mtef_visitor_source,af_override_horse,0,1,[]),(33,mtef_visitor_source,af_override_horse,0,1,[]),(34,mtef_visitor_source,af_override_horse,0,1,[]),(35,mtef_visitor_source,af_override_horse,0,1,[]),(36,mtef_visitor_source,af_override_horse,0,1,[]),(37,mtef_visitor_source,af_override_horse,0,1,[]),(38,mtef_visitor_source,af_override_horse,0,1,[]),(39,mtef_visitor_source,af_override_horse,0,1,[]),
     (40,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(41,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(42,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(43,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (44,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(45,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(46,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(47,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     ],
    [
      lav_situational_damage_modifiers,
      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (agent_get_troop_id, ":troop_no", ":agent_no"),
         (neq, ":troop_no", "trp_player"),
         (neg|is_between, ":troop_no", walkers_begin, walkers_end),
         (agent_set_team, ":agent_no", 1),
         ]),

		 # Josef v586 - blong for mandolin	
		
   # (0.40, 0, 0, [], [
    # (try_for_agents, ":agent"),
      # (agent_is_alive, ":agent"),
      # (agent_is_human, ":agent"),
      # (agent_get_wielded_item, ":handone", ":agent", 0),
      # (agent_get_wielded_item, ":handtwo", ":agent", 1),
      # (this_or_next|eq, ":handone", "itm_mandolin"),
      # (eq, ":handtwo", "itm_mandolin"),
      # (agent_get_combat_state, ":state", ":agent"),
      # (try_begin),
        # (eq,":state",4), #This is the combat state for melee swing
        # (agent_slot_eq,":agent",slot_agent_attack_sound, 0),
        # (agent_set_slot, ":agent", slot_agent_attack_sound, 1),
        # (agent_play_sound,":agent","snd_gsh"),
      # (else_try),
        # (neq,":state",4),
        # (agent_set_slot, ":agent", slot_agent_attack_sound, 0),
      # (try_end),
    # (try_end),
   # ]),
   
   
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest"),
	                                       (call_script, "script_remove_siege_objects"),]),

	  
	  

										   
										   
      common_inventory_not_available,
      
      (ti_tab_pressed, 0, 0,
       [
         (display_message, "@Cannot leave now."),
         ], []),
      (ti_on_leave_area, 0, 0,
       [
         (try_begin),
           (eq, "$g_defending_against_siege", 0),
           (assign,"$g_leave_town",1),
         (try_end),
         ], []),

      (0, 0, ti_once, [],
       [
         (call_script, "script_music_set_situation_with_culture", mtf_sit_ambushed),
         (set_party_battle_mode),
         (party_slot_eq, "$current_town", slot_party_type, spt_town),
         (call_script, "script_town_init_doors", 0),
        ]),

      (1, 4, ti_once,
       [
         (store_mission_timer_a,":cur_time"),
         (ge, ":cur_time", 5),
         (this_or_next|main_hero_fallen),
         (num_active_teams_le,1)
         ],
       [
         (try_begin),
           (main_hero_fallen),
           (jump_to_menu, "mnu_town_assassins_failed"),
		   (rest_for_hours, 2, 4, 0),
		   (display_message, "@You spend some time recovering from the attack..", 0xFFFF2222),
		   (rest_for_hours, 50, 4, 0),
         (else_try),		 
           (jump_to_menu, "mnu_town_assassins_succeeded"),
		   (rest_for_hours, 0, 0, 1),
         (try_end),
		
    
         (finish_mission),
         ]),
      ],
    ),


# end Josef 586 assassins! 	
	# Ne end assassins
  
  (
    "village_training", mtf_arena_fight, -1,
    "village_training",
    [(2,mtef_visitor_source|mtef_team_0,af_override_everything,aif_start_alarmed,1,[itm.practice_staff, itm.practice_boots]),
     (4,mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[itm.practice_staff, itm.practice_boots]),
     ],
    [
      lav_situational_damage_modifiers,
      (ti_before_mission_start, 0, 0, [],
       [
         (assign, "$g_train_peasants_against_bandits_training_succeeded", 0),
         (call_script, "script_change_banners_and_chest"),
         ]),
      
      common_arena_fight_tab_press,
      
      (ti_question_answered, 0, 0, [],
       [
         (store_trigger_param_1,":answer"),
         (eq,":answer",0),
         (finish_mission),
         ]),
      
      common_inventory_not_available,

      (1, 4, ti_once,
       [
         (this_or_next|main_hero_fallen),
         (num_active_teams_le, 1)
         ],
       [
         (try_begin),
           (neg|main_hero_fallen),
           (assign, "$g_train_peasants_against_bandits_training_succeeded", 1),
         (try_end),
         (finish_mission),
         ]),
      ],
    ),
    
  (
    "visit_town_castle",0,-1,
    "You enter the halls of the lord.",
    [(0,mtef_scene_source|mtef_team_0,af_override_horse|af_override_weapons|af_override_head,0,1,[]),
     (1,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (3,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]), 
     (4,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]), #for doors
     (5,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (6,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (7,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (8,mtef_visitor_source,af_override_horse,0,1,[]),
     (9,mtef_visitor_source,af_override_horse,0,1,[]),
     (10,mtef_scene_source,af_override_horse,0,1,[]),
     (11,mtef_scene_source,af_override_horse,0,1,[]),
     (12,mtef_visitor_source,af_override_horse,0,1,[]),
     (13,mtef_visitor_source,0,0,1,[]),
     (14,mtef_visitor_source,0,0,1,[]),
     (15,mtef_visitor_source,0,0,1,[]),
     (16,mtef_visitor_source,af_castle_lord,0,1,[]),
     (17,mtef_visitor_source,af_castle_lord,0,1,[]),
     (18,mtef_visitor_source,af_castle_lord,0,1,[]),
     (19,mtef_visitor_source,af_castle_lord,0,1,[]),
     (20,mtef_visitor_source,af_castle_lord,0,1,[]),
     (21,mtef_visitor_source,af_castle_lord,0,1,[]),
     (22,mtef_visitor_source,af_castle_lord,0,1,[]),
     (23,mtef_visitor_source,af_castle_lord,0,1,[]),
     (24,mtef_visitor_source,af_castle_lord,0,1,[]),
     (25,mtef_visitor_source,af_castle_lord,0,1,[]),
     (26,mtef_visitor_source,af_castle_lord,0,1,[]),
     (27,mtef_visitor_source,af_castle_lord,0,1,[]),
     (28,mtef_visitor_source,af_castle_lord,0,1,[]),
     (29,mtef_visitor_source,af_castle_lord,0,1,[]),
     (30,mtef_visitor_source,af_castle_lord,0,1,[]),
     (31,mtef_visitor_source,af_castle_lord,0,1,[])
     ],
    [
      lav_situational_damage_modifiers,
      (ti_on_agent_spawn, 0, 0, [],
      [
        (store_trigger_param_1, ":agent_no"),
        (call_script, "script_init_town_agent", ":agent_no"),
      ]),
      
      (ti_before_mission_start, 0, 0, [],
      [
        (call_script, "script_change_banners_and_chest"),
      ]),
       
      (ti_inventory_key_pressed, 0, 0, 
      [
        (set_trigger_result,1)
      ], []),
	  
	  #adjust for prison break
      (ti_tab_pressed, 0, 0,
	  [
	    (neq, "$talk_context", tc_prison_break),
	    (set_trigger_result,1)
	  ], []),
	  
      (ti_on_leave_area, 0, 0,
      [
 	    (eq, "$talk_context", tc_prison_break),
 	  ], 
	  [
	    (display_message, "str_leaving_area_during_prison_break"),
	    (set_jump_mission, "mt_sneak_caught_fight"),
	  ]),
	 	  
      (0, 0, ti_once, [], [
        #(set_fog_distance, 150, 0xFF736252)
        (try_begin),
          (eq, "$talk_context", tc_court_talk),
          (try_begin),
            (store_faction_of_party, ":center_faction", "$current_town"),
            (faction_slot_eq, ":center_faction", slot_faction_ai_state, sfai_feast),
            (faction_slot_eq, ":center_faction", slot_faction_ai_object, "$current_town"),
            (call_script, "script_music_set_situation_with_culture", mtf_sit_feast),
            #(call_script, "script_music_set_situation_with_culture", mtf_sit_lords_hall),
          (try_end),
        (else_try),
          (call_script, "script_music_set_situation_with_culture", 0), #prison
        (try_end),
        ]),
    ],
  ),

		  
  (
    "back_alley_kill_local_merchant",mtf_battle_mode,-1,
    "You enter the back alley",
    [
      (0,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (3,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
    ],
    [
      lav_situational_damage_modifiers,
      common_inventory_not_available,
      (ti_tab_pressed, 0, 0, [(display_message,"str_cannot_leave_now")], []),
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),

      (0, 0, ti_once, [],
       [
         (call_script, "script_music_set_situation_with_culture", mtf_sit_ambushed),
         ]),

      (0, 0, ti_once, [
          (store_mission_timer_a,":cur_time"),
          (ge,":cur_time",1), 
          (assign, ":merchant_hp", 0),
          (assign, ":player_hp", 0),
          (assign, ":merchant_hp", 0),
          (assign, ":merchant_agent", -1),
          (assign, ":player_agent", -1),
          (try_for_agents, ":agent_no"),
            (agent_get_troop_id, ":troop_id", ":agent_no"),
            (try_begin),
              (eq, ":troop_id", "trp_local_merchant"),
              (store_agent_hit_points, ":merchant_hp", ":agent_no"),
              (assign, ":merchant_agent", ":agent_no"),
            (else_try),
              (eq, ":troop_id", "trp_player"),
              (store_agent_hit_points, ":player_hp",":agent_no"),
              (assign, ":player_agent", ":agent_no"),
            (try_end),
          (try_end),
          (ge, ":player_agent", 0),
          (ge, ":merchant_agent", 0),
          (agent_is_alive, ":player_agent"),
          (agent_is_alive, ":merchant_agent"),
          (is_between, ":merchant_hp", 1, 30),
          (gt, ":player_hp", 50),
          (start_mission_conversation, "trp_local_merchant"),
          ], []),
      
      (1, 4, ti_once, [(assign, ":not_alive", 0),
                       (try_begin),
                         (call_script, "script_cf_troop_agent_is_alive", "trp_local_merchant"),
                       (else_try),
                         (assign, ":not_alive", 1),
                       (try_end),
                       (this_or_next|main_hero_fallen),
                       (eq, ":not_alive", 1)],
       [
           (try_begin),
             (main_hero_fallen),
             (call_script, "script_fail_quest", "qst_kill_local_merchant"),
           (else_try),
             (call_script, "script_change_player_relation_with_center", "$current_town", -4),
             (call_script, "script_succeed_quest", "qst_kill_local_merchant"),
           (try_end),
           (finish_mission),
           ]),
    ],
  ),

  
 # NE quests 
  # v585 Josef Bar Brawl
  (
    "back_alley_bar_brawl",mtf_arena_fight,-1,
    "You make your way to the town centre",
    [ 
	  # spawn the brawlers in the merchant 1,2,3 entry points. 
      (0,mtef_visitor_source|mtef_team_1|mtef_use_exact_number,af_override_everything,aif_start_alarmed,1,[itm.linen_tunic, itm.leather_boots]),
      (10,mtef_visitor_source|mtef_team_0|mtef_use_exact_number,af_override_everything,aif_start_alarmed,1,[itm.coarse_tunic, itm.hide_boots]),
      (11,mtef_visitor_source|mtef_team_0|mtef_use_exact_number,af_override_everything,aif_start_alarmed,1,[itm.rawhide_coat, itm.hide_boots]),
      (12,mtef_visitor_source|mtef_team_0|mtef_use_exact_number,af_override_everything,aif_start_alarmed,1,[itm.leather_jerkin, itm.leather_boots]),
       

   ],
    [
      lav_situational_damage_modifiers,
      common_inventory_not_available,
      (ti_tab_pressed, 0, 0, [(display_message,"@Cannot leave now.")], []),
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),
		 
		 
      (0, 0, ti_once, [],
       [
         (call_script, "script_music_set_situation_with_culture", mtf_sit_ambushed),
         ]),

		   
		   
     ( 1, 4, ti_once,
       [
         (store_mission_timer_a,":cur_time"),
         (ge, ":cur_time", 5),
         (this_or_next|main_hero_fallen),
         (num_active_teams_le,1)
         ],
       [ 

         (try_begin),
           (main_hero_fallen),
		   (call_script, "script_fail_quest", "qst_bar_brawl"),
         (else_try),
             (call_script, "script_succeed_quest", "qst_bar_brawl"),
         (try_end),
         (finish_mission),
         ]),
		 
    ],
  ), 
 

  # v585 Josef Bar Brawl - higher level
  (
    "back_alley_bar_brawl2",mtf_arena_fight,-1,
    "You make your way to the town centre",
    [   
	
	 
	  (0,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm.broken_bottle, itm.linen_tunic, itm.leather_boots]),	
      (10,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[itm.broken_bottle, itm.coarse_tunic,itm.hide_boots]),
      (11,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[itm.broken_bottle, itm.rawhide_coat, itm.hide_boots]),
      (12,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[itm.broken_bottle, itm.leather_jerkin, itm.leather_boots]),
     ],
    [
      lav_situational_damage_modifiers,
      common_inventory_not_available,
      (ti_tab_pressed, 0, 0, [(display_message,"@Cannot leave now.")], []),
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),

      (0, 0, ti_once, [],
       [
         (call_script, "script_music_set_situation_with_culture", mtf_sit_ambushed),
         (set_party_battle_mode),
         (party_slot_eq, "$current_town", slot_party_type, spt_town),
         (call_script, "script_town_init_doors", -1),
         ]),
		 
		   
     ( 1, 4, ti_once,
       [
         (store_mission_timer_a,":cur_time"),
         (ge, ":cur_time", 5),
         (this_or_next|main_hero_fallen),
         (num_active_teams_le,1)
         ],
       [
         (try_begin),
           (main_hero_fallen),
		   (call_script, "script_fail_quest", "qst_bar_brawl"),
         (else_try),
             (call_script, "script_succeed_quest", "qst_bar_brawl"),
         (try_end),
         (finish_mission),
         ]),
		 
    ],
  ), 
  

  
  #end v585 Josef
# Ne end quests 
  
  
  
  
  (
    "back_alley_revolt",mtf_battle_mode,charge,
    "You lead your men to battle.",
    [(0,mtef_team_0|mtef_use_exact_number,af_override_horse|af_override_weapons|af_override_head,aif_start_alarmed,4,[itm.staff]),
     (3,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     ],
    [
      lav_situational_damage_modifiers,
      common_inventory_not_available,

      common_battle_init_banner,

      (ti_tab_pressed, 0, 0, [],
       [(question_box,"str_do_you_want_to_retreat"),
        ]),
      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (jump_to_menu, "mnu_collect_taxes_failed"),
        (finish_mission),]),

      (ti_tab_pressed, 0, 0, [(display_message,"str_cannot_leave_now")], []),
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),

      (0, 0, ti_once, [],
       [
         (call_script, "script_music_set_situation_with_culture", mtf_sit_fight),
         ]),

      (1, 4, ti_once, [(this_or_next|main_hero_fallen),(num_active_teams_le,1)],
       [
           (try_begin),
             (main_hero_fallen),
             (jump_to_menu, "mnu_collect_taxes_failed"),
           (else_try),
             (jump_to_menu, "mnu_collect_taxes_rebels_killed"),
           (try_end),
           (finish_mission),
           ]),
    ],
  ),

# Lead charge

  (
    "lead_charge",mtf_battle_mode,charge,
    "You lead your men to battle.",
    [
     (1,mtef_defenders|mtef_team_0,0,aif_start_alarmed,12,[]),
     (0,mtef_defenders|mtef_team_0,0,aif_start_alarmed,0,[]),
     (4,mtef_attackers|mtef_team_1,0,aif_start_alarmed,12,[]),
     (4,mtef_attackers|mtef_team_1,0,aif_start_alarmed,0,[]),
     ],
    [
      lav_situational_damage_modifiers,
      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (call_script, "script_agent_reassign_team", ":agent_no"),

         (assign, ":initial_courage_score", 5000),
                  
         (agent_get_troop_id, ":troop_id", ":agent_no"),
         (store_character_level, ":troop_level", ":troop_id"),
         (val_mul, ":troop_level", 35),
         (val_add, ":initial_courage_score", ":troop_level"), #average : 20 * 35 = 700
         
         (store_random_in_range, ":randomized_addition_courage", 0, 3000), #average : 1500
         (val_add, ":initial_courage_score", ":randomized_addition_courage"), 
                   
         (agent_get_party_id, ":agent_party", ":agent_no"),         
         (party_get_morale, ":cur_morale", ":agent_party"),
         
         (store_sub, ":morale_effect_on_courage", ":cur_morale", 70),
         (val_mul, ":morale_effect_on_courage", 30), #this can effect morale with -2100..900
         (val_add, ":initial_courage_score", ":morale_effect_on_courage"), 
         
         #average = 5000 + 700 + 1500 = 7200; min : 5700, max : 8700
         #morale effect = min : -2100(party morale is 0), average : 0(party morale is 70), max : 900(party morale is 100)
         #min starting : 3600, max starting  : 9600, average starting : 7200
         (agent_set_slot, ":agent_no", slot_agent_courage_score, ":initial_courage_score"), 
         ]),

      common_battle_init_banner,
		 
      (ti_on_agent_killed_or_wounded, 0, 0, [],
       [
        (store_trigger_param_1, ":dead_agent_no"),
        (store_trigger_param_2, ":killer_agent_no"),
        (store_trigger_param_3, ":is_wounded"),

        (try_begin),
          (ge, ":dead_agent_no", 0),
          (neg|agent_is_ally, ":dead_agent_no"),
          (agent_is_human, ":dead_agent_no"),
          (agent_get_troop_id, ":dead_agent_troop_id", ":dead_agent_no"),
##          (str_store_troop_name, s6, ":dead_agent_troop_id"),
##          (assign, reg0, ":dead_agent_no"),
##          (assign, reg1, ":killer_agent_no"),
##          (assign, reg2, ":is_wounded"),
##          (agent_get_team, reg3, ":dead_agent_no"),          
          #(display_message, "@{!}dead agent no : {reg0} ; killer agent no : {reg1} ; is_wounded : {reg2} ; dead agent team : {reg3} ; {s6} is added"), 
          (party_add_members, "p_total_enemy_casualties", ":dead_agent_troop_id", 1), #addition_to_p_total_enemy_casualties
          (eq, ":is_wounded", 1),
          (party_wound_members, "p_total_enemy_casualties", ":dead_agent_troop_id", 1), 
        (try_end),

        (call_script, "script_apply_death_effect_on_courage_scores", ":dead_agent_no", ":killer_agent_no"),
       ]),

      common_battle_tab_press,

      # (ti_question_answered, 0, 0, [],
       # [(store_trigger_param_1,":answer"),
        # (eq,":answer",0),
        # (assign, "$pin_player_fallen", 0),
        # (try_begin),
          # (store_mission_timer_a, ":elapsed_time"),
          # (gt, ":elapsed_time", 20),
          # (str_store_string, s5, "str_retreat"),
          # (call_script, "script_simulate_retreat", 10, 20, 1),
        # (try_end),
        # (call_script, "script_count_mission_casualties_from_agents"),
        # (finish_mission,0),]),
		
		
	      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
	     (eq,":answer",0),
	   # NE cam
        # (assign, "$pin_player_fallen", 0),
	    (try_begin),  ## Let the battle continue after the player is down - Jinnai
          (main_hero_fallen),
          (assign, "$pin_player_fallen", 1),
          (assign, "$g_battle_result", -1),
          (set_mission_result,-1),
        (else_try),
          (assign, "$pin_player_fallen", 0),
        (try_end),
		
        (try_begin),
          (store_mission_timer_a, ":elapsed_time"),
          (gt, ":elapsed_time", 20),
          (str_store_string, s5, "str_retreat"),
          (call_script, "script_simulate_retreat", 10, 20, 1),
        (try_end),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),]),	
		
		

      (ti_before_mission_start, 0, 0, [],
       [
         (team_set_relation, 0, 2, 1),
         (team_set_relation, 1, 3, 1),
         (call_script, "script_place_player_banner_near_inventory_bms"),

         (party_clear, "p_routed_enemies"),

         (assign, "$g_latest_order_1", 1), 
         (assign, "$g_latest_order_2", 1), 
         (assign, "$g_latest_order_3", 1), 
         (assign, "$g_latest_order_4", 1), 
         ]),

      
      (0, 0, ti_once, [], [(assign,"$g_battle_won",0),
                           (assign,"$defender_reinforcement_stage",0),
                           (assign,"$attacker_reinforcement_stage",0),
                           (call_script, "script_place_player_banner_near_inventory"),
                           (call_script, "script_combat_music_set_situation_with_culture"),
                           (assign, "$g_defender_reinforcement_limit", 2),
                           ]),

      common_music_situation_update,
      common_battle_check_friendly_kills,

      (1, 0, 5, [
                              
      #new (25.11.09) starts (sdsd = TODO : make a similar code to also helping ally encounters)
      #count all total (not dead) enemy soldiers (in battle area + not currently placed in battle area)
      (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
      (assign, ":total_enemy_soldiers", reg0),
      
      #decrease number of agents already in battle area to find all number of reinforcement enemies
      (assign, ":enemy_soldiers_in_battle_area", 0),
      (try_for_agents,":cur_agent"),
        (agent_is_human, ":cur_agent"),
        (agent_get_party_id, ":agent_party", ":cur_agent"),
        (try_begin),
          (neq, ":agent_party", "p_main_party"),
          (neg|agent_is_ally, ":cur_agent"),
          (val_add, ":enemy_soldiers_in_battle_area", 1),
        (try_end),
      (try_end),
      (store_sub, ":total_enemy_reinforcements", ":total_enemy_soldiers", ":enemy_soldiers_in_battle_area"),

      (try_begin),
        (lt, ":total_enemy_reinforcements", 15),
        (ge, "$defender_reinforcement_stage", 2),
        (eq, "$defender_reinforcement_limit_increased", 0),
        (val_add, "$g_defender_reinforcement_limit", 1),                    
        (assign, "$defender_reinforcement_limit_increased", 1),
      (try_end),    
      #new (25.11.09) ends
      
      
      
      
      
      
      (lt,"$defender_reinforcement_stage","$g_defender_reinforcement_limit"),
                 (store_mission_timer_a,":mission_time"),
                 (ge,":mission_time",10),
                 (store_normalized_team_count,":num_defenders", 0),
                 (lt,":num_defenders",6)],
           [(add_reinforcements_to_entry,0,7),(assign, "$defender_reinforcement_limit_increased", 0),(val_add,"$defender_reinforcement_stage",1)]),
      
      (1, 0, 5, [(lt,"$attacker_reinforcement_stage",2),
                 (store_mission_timer_a,":mission_time"),
                 (ge,":mission_time",10),
                 (store_normalized_team_count,":num_attackers", 1),
                 (lt,":num_attackers",6)],
           [(add_reinforcements_to_entry,3,7),(val_add,"$attacker_reinforcement_stage",1)]),

      common_battle_check_victory_condition,
      common_battle_victory_display,

	  # NE cam
      # (1, 4, ti_once, [(main_hero_fallen)],
          # [
              # (assign, "$pin_player_fallen", 1),
              # (str_store_string, s5, "str_retreat"),
              # (call_script, "script_simulate_retreat", 10, 20, 1),
              # (assign, "$g_battle_result", -1),
              # (set_mission_result,-1),
              # (call_script, "script_count_mission_casualties_from_agents"),
              # (finish_mission,0)]),
      # NE cam
      (1, 4, ti_once,
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
        ]),
	 
      common_battle_inventory,


      #AI Triggers
      (0, 0, ti_once, [
          (store_mission_timer_a,":mission_time"),(ge,":mission_time",2),
          ],
       [(call_script, "script_select_battle_tactic"),
        (call_script, "script_battle_tactic_init"),
        #(call_script, "script_battle_calculate_initial_powers"), #deciding run away method changed and that line is erased
        ]),
      
      (3, 0, 0, [
          (call_script, "script_apply_effect_of_other_people_on_courage_scores"),
              ], []), #calculating and applying effect of people on others courage scores

      (3, 0, 0, [
          (try_for_agents, ":agent_no"),
            (agent_is_human, ":agent_no"),
            (agent_is_alive, ":agent_no"),          
            (store_mission_timer_a,":mission_time"),
            (ge,":mission_time",3),     
            # Fleeing check 
            (eq, "$setting_troops_flee",1),		
            # end fleeing check 				
            (call_script, "script_decide_run_away_or_not", ":agent_no", ":mission_time"),
          (try_end),          
              ], []), #controlling courage score and if needed deciding to run away for each agent

      (5, 0, 0, [
          (store_mission_timer_a,":mission_time"),

          (ge,":mission_time",3),
          
          (call_script, "script_battle_tactic_apply"),
          ], []), #applying battle tactic

      common_battle_order_panel,
      common_battle_order_panel_tick,

# NE 

## Ne cam
########Tactical triggers below##########

(ti_before_mission_start, 0, 0, [],
##(ti_before_mission_start, 0, 0, [(eq,"$setting_troops_form",1)],
   [
     (assign,"$rout",0),
    ## (assign,"$airout",0),
    (assign,"$formation",0),
    (assign,"$infantryformationtype",0),
    (assign,"$archerformationtype",0),
    (assign,"$cavalryformationtype",0),
    (get_player_agent_kill_count,"$base_kills",0),
    (assign,"$new_kills_a",0),
    (assign,"$new_kills",0)]),


     (0, 0, 0,
##      [(eq,"$setting_troops_form",1), (key_clicked, key_2), 
      [(key_clicked, key_2),       
       (assign,"$formation",grc_infantry),
        ], []),
     (0, 0, 0,
      [(key_clicked, key_3),       
       (assign,"$formation",grc_archers),
        ], []),
     (0, 0, 0,
      [(key_clicked, key_4),       
       (assign,"$formation",grc_cavalry),
        ], []),


     (0, 0, 0,
      [(eq,"$setting_troops_form",1), (gt, "$ne_key_ranks", 0), (key_clicked, "$ne_key_ranks"),       
       (get_player_agent_no,":player"),
       (agent_get_team  ,reg0, ":player"),
       (assign,reg1,"$formation"),
       (call_script,"script_cf_formation"),
       (try_begin),
          (eq,"$formation",grc_infantry),
          (assign,"$infantryformationtype",1),
       (else_try),
          (eq,"$formation",grc_archers),
          (assign,"$archerformationtype",1),
       (else_try),
          (eq,"$formation",grc_cavalry),
          (assign,"$cavalryformationtype",1),
       (end_try),
       (display_message,"@Forming_ranks."),
        ], []),

     (0, 0, 0,
      [(eq,"$setting_troops_form",1), (gt, "$ne_key_line", 0), (key_clicked, "$ne_key_line"),
       (get_player_agent_no,":player"),
       (agent_get_team  ,reg0, ":player"),
       (assign,reg1,"$formation"),
       (call_script,"script_cf_formation_stagger"),
       (call_script,"script_cf_formation"),
       (try_begin),
          (eq,"$formation",grc_infantry),
          (assign,"$infantryformationtype",3),
       (else_try),
          (eq,"$formation",grc_archers),
          (assign,"$archerformationtype",3),
       (else_try),
          (eq,"$formation",grc_cavalry),
          (assign,"$cavalryformationtype",3),
       (end_try),
       (display_message,"@Forming_a_line."),
        ], []),

     (0, 0, 0,
      [(eq,"$setting_troops_form",1), (gt, "$ne_key_wedge", 0), (key_clicked, "$ne_key_wedge"),
       (get_player_agent_no,":player"),
       (agent_get_team  ,reg0, ":player"),
       (assign,reg1,"$formation"),
       (call_script,"script_cf_formation_wedge"),
       (call_script,"script_cf_formation"),
       (try_begin),
          (eq,"$formation",grc_infantry),
          (assign,"$infantryformationtype",2),
       (else_try),
          (eq,"$formation",grc_archers),
          (assign,"$archerformationtype",2),
       (else_try),
          (eq,"$formation",grc_cavalry),
          (assign,"$cavalryformationtype",2),
       (end_try),
       (display_message,"@Forming_a_wedge."),
        ], []),

     (0, 0, 0,
      [(eq,"$setting_troops_form",1), (gt, "$ne_key_unform", 0), (key_clicked, "$ne_key_unform"),
       (get_player_agent_no,":player"),
       (agent_get_team  ,reg0, ":player"),
       (assign,reg1,"$formation"),
       (call_script,"script_formation_end"),
       (call_script,"script_cf_formation"),
       (try_begin),
          (eq,"$formation",grc_infantry),
          (assign,"$infantryformationtype",0),
       (else_try),
          (eq,"$formation",grc_archers),
          (assign,"$archerformationtype",0),
       (else_try),
          (eq,"$formation",grc_cavalry),
          (assign,"$cavalryformationtype",0),
       (end_try),
       (display_message,"@Formation_disassembled."),
        ], []),

     (5.0, 0, 0,
      [(eq,"$setting_troops_form",1), (try_for_agents,":agent"),
         (agent_is_human,":agent"),
         (neg|agent_is_ally,":agent"),
         (assign,":enemy",":agent"),
       (end_try),
       (gt,":enemy",-1),
       (eq,"$airout",0),
       (agent_get_team  ,reg0, ":enemy"),
       (assign,reg1,grc_cavalry),
       (call_script,"script_formation_end"),
       (assign,reg1,grc_infantry),
       (call_script,"script_formation_end"),
       (assign,reg1,grc_archers),
       (call_script,"script_formation_end"),], []),


     (5.0, 0, 0,
      [(eq,"$setting_troops_form",1), (eq,"$rout",0),
       (get_player_agent_no,":player"),
       (agent_get_team  ,reg0, ":player"),
       (val_add,reg0,2),
       (assign,reg1,grc_cavalry),
       (call_script,"script_formation_end"),
       (assign,reg1,grc_infantry),
       (call_script,"script_formation_end"),
       (assign,reg1,grc_archers),
       (call_script,"script_formation_end"),], []),

     (0.2, 0, 0,
      [(eq,"$setting_troops_form",1), (eq,"$rout",0),
       (get_player_agent_no,":player"),
       (agent_get_team  ,reg0, ":player"),
       (assign,reg1,grc_infantry),
       (try_begin),
          (eq,"$infantryformationtype",1),
          (call_script,"script_cf_formation"),
       (else_try),
          (eq,"$infantryformationtype",2),
          (call_script,"script_cf_formation_wedge"),
       (else_try),
          (eq,"$infantryformationtype",3),
          (call_script,"script_cf_formation_stagger"),
       (else_try),
          (call_script,"script_formation_end"),
       (end_try),], []),

     (0.2, 0, 0,
      [(eq,"$setting_troops_form",1), (eq,"$rout",0),
       (get_player_agent_no,":player"),
       (agent_get_team  ,reg0, ":player"),
       (assign,reg1,grc_archers),
       (try_begin),
          (eq,"$archerformationtype",1),
          (call_script,"script_cf_formation"),
       (else_try),
          (eq,"$archerformationtype",2),
          (call_script,"script_cf_formation_wedge"),
       (else_try),
          (eq,"$archerformationtype",3),
          (call_script,"script_cf_formation_stagger"),
       (else_try),
          (call_script,"script_formation_end"),
       (end_try),], []),

     (0.2, 0, 0,
      [(eq,"$setting_troops_form",1), (eq,"$rout",0),
       (get_player_agent_no,":player"),
       (agent_get_team  ,reg0, ":player"),
       (assign,reg1,grc_cavalry),
       (try_begin),
          (eq,"$cavalryformationtype",1),
          (call_script,"script_cf_formation"),
       (else_try),
          (eq,"$cavalryformationtype",2),
          (call_script,"script_cf_formation_wedge"),
       (else_try),
          (eq,"$cavalryformationtype",3),
          (call_script,"script_cf_formation_stagger"),
       (else_try),
          (call_script,"script_formation_end"),
       (end_try),], []),

     (0.2, 0, 0,
      [(eq,"$setting_troops_form",1), (eq,"$airout",0),
       (try_for_agents,":agent"),
         (agent_is_human,":agent"),
         (neg|agent_is_ally,":agent"),
         (assign,":enemy",":agent"),
       (end_try),
       (gt,":enemy",-1),
       (agent_get_team  ,reg0, ":enemy"),
       (store_normalized_team_count,":num", reg0), 
       (gt,":num",5),
       (assign,reg1,grc_infantry),
       (call_script,"script_cf_formation"),
        ], []),

     (0.2, 0, 0,
      [(eq,"$setting_troops_form",1), (eq,"$airout",0),
       (try_for_agents,":agent"),
         (agent_is_human,":agent"),
         (neg|agent_is_ally,":agent"),
         (assign,":enemy",":agent"),
       (end_try),
       (gt,":enemy",-1),
       (agent_get_team  ,reg0, ":enemy"),
       (store_normalized_team_count,":num", reg0), 
       (gt,":num",5),
       (assign,reg1,grc_archers),
       (call_script,"script_cf_formation_stagger"),
        ], []),

     (0.2, 0, 0,
      [(eq,"$setting_troops_form",1), (eq,"$airout",0),
       (try_for_agents,":agent"),
         (agent_is_human,":agent"),
         (neg|agent_is_ally,":agent"),
         (assign,":enemy",":agent"),
       (end_try),
       (gt,":enemy",-1),
       (agent_get_team  ,reg0, ":enemy"),
       (store_normalized_team_count,":num", reg0), 
       (gt,":num",5),
       (assign,reg1,grc_cavalry),
       (call_script,"script_cf_formation_wedge"),
        ], []),

     (0.2, 0, 0,
      [(eq,"$setting_troops_form",1),(eq,"$rout",0),
       (neq, "$battle_won", 1),
       (eq,"$rout",0),
       (get_player_agent_no,":player"),
       (agent_get_team  ,reg0, ":player"),
       (val_add,reg0,2),
       (store_normalized_team_count,":num", reg0), 
       (gt,":num",5),
       (assign,reg1,grc_infantry),
       (call_script,"script_cf_formation"),
        ], []),

     (0.2, 0, 0,
      [(eq,"$setting_troops_form",1),(eq,"$rout",0),
       (neq, "$battle_won", 1),
       (eq,"$rout",0),
       (get_player_agent_no,":player"),
       (agent_get_team  ,reg0, ":player"),
       (val_add,reg0,2),
       (store_normalized_team_count,":num", reg0), 
       (gt,":num",5),
       (assign,reg1,grc_archers),
       (call_script,"script_cf_formation_stagger"),
        ], []),

     (0.2, 0, 0,
      [(eq,"$setting_troops_form",1),
	  (eq,"$rout",0),
       (neq, "$battle_won", 1),
       (eq,"$rout",0),
       (get_player_agent_no,":player"),
       (agent_get_team  ,reg0, ":player"),
       (val_add,reg0,2),
       (store_normalized_team_count,":num", reg0), 
       (gt,":num",5),
       (assign,reg1,grc_cavalry),
       (call_script,"script_cf_formation_wedge"),
        ], []),

     (3, 0, 3, [(eq,"$setting_troops_form",1)], [
        (get_player_agent_kill_count,":more_kills",0),
        (val_sub,":more_kills","$base_kills"),
(try_begin),
            (gt,":more_kills","$new_kills_a"),
            (assign,"$new_kills_a",":more_kills"),
(assign,"$new_kills",":more_kills"),
(val_div,"$new_kills",2),
            (assign,reg1,":more_kills"),
            (display_message,"@You have killed {reg1} enemies in this battle!",0x6495ed),         
            (display_message,"@Your bravery inspires your troops!",0x6495ed),
        (try_end),
         ]),



     (0, 0, 2, [(eq,"$setting_troops_form",1), (gt, "$ne_key_cohesion", 0), (key_clicked, "$ne_key_cohesion")], [
(call_script, "script_coherence"),   
(call_script, "script_healthbars"),       
         ]),

     (0, 0, ti_once, [(eq,"$setting_troops_form",1),(gt, "$ne_key_rally", 0),(key_clicked, "$ne_key_rally")], [
#(play_sound,"snd_battle_cry_n"),
(display_message,"@You rally your men!",0x7ccd7c),
(call_script, "script_battle_cry"),
(call_script, "script_hero_exp_penalty"),       
         ]),
     (10, 0, 20, [ (eq,"$setting_troops_form",1)], [
(call_script, "script_rally"),       
         ]),
     (0, 10, 100, [(eq,"$setting_troops_form",1),(gt, "$ne_key_reinforce", 0),(key_clicked, "$ne_key_reinforce"),(display_message,"@You call for reinforcements!",0x6495ed) ], [
(display_message,"@Reinforcements arrive!",0x6495ed),
(add_reinforcements_to_entry,0,7),
(add_reinforcements_to_entry,3,7),
(call_script, "script_hero_exp_penalty"),       
         ]),     

     
(1, 0, ti_once, [], [
#(1, 0, ti_once, [(eq,"$setting_troops_form",1) ], [
(call_script, "script_coherence"),   
         ]),

## Maybe later
     
(15, 0, 10, [(eq,"$setting_troops_flee",1)], [
(call_script, "script_coherence"),   
(call_script, "script_morale_check"),   
         ]),
(5, 0, 3, [(eq,"$setting_troops_flee",1)], [
(call_script, "script_coherence"),   
(call_script, "script_rout_check"),       
         ]),




###########Tactical triggers above#########

      call_horse_trigger_1,
      call_horse_trigger_2,
      shield_bash_trigger_1,
      shield_bash_trigger_2,
      shield_bash_trigger_3,
      shield_bash_trigger_4,
      common_battle_order_panel,
      common_battle_order_panel_tick,
      spearwall_trigger_1,
      spearwall_trigger_2,
      spearwall_trigger_3,
      spearwall_trigger_4,
      spearwall_trigger_5,
      spearwall_trigger_6,
      spearwall_trigger_7,
      spearwall_trigger_8,
      spearwall_trigger_9,
      #camera_trigger_1,
      #camera_trigger_2,
      #camera_trigger_3,
      #camera_trigger_4,
      #camera_trigger_5,
      #camera_trigger_6,
      #camera_trigger_7,
      #camera_trigger_8,
      common_init_deathcam,
      common_start_deathcam,
      common_move_deathcam,
      common_rotate_deathcam,

	  ## NE end cam

	  (ti_once, 0.2, 0, [], [
	      (get_player_agent_no, ":player_agent"),
	      (agent_get_team, ":team_id", ":player_agent"),
          (team_give_order, ":team_id", grc_everyone, mordr_stand_ground),
	  ]),


# NE 	  
	  
	  
	  
	  
	  
    ],
  ),






# end lead charge


  (
    "village_attack_bandits",mtf_battle_mode,charge,
    "You lead your men to battle.",
    [
     (3,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
     (1,mtef_team_0|mtef_use_exact_number,0,aif_start_alarmed, 7,[]),
     (1,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
     ],
    [
      lav_situational_damage_modifiers,
      common_battle_tab_press,
      common_battle_init_banner,

      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
		# ne cam
		(try_begin), #More letting the battle continue after the player is knocked out - Jinnai
          (main_hero_fallen),
          (assign, "$pin_player_fallen", 1),
          (assign, "$g_battle_result", -1),
          (set_mission_result, -1),
        (else_try),
        (assign, "$pin_player_fallen", 0),
		(try_end), 
		# ne end cam
        (str_store_string, s5, "str_retreat"),
        (call_script, "script_simulate_retreat", 10, 20, 1),
        (assign, "$g_battle_result", -1),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),]),

      (0, 0, ti_once, [], [(assign, "$g_battle_won", 0),
                           (assign, "$defender_reinforcement_stage", 0),
                           (assign, "$attacker_reinforcement_stage", 0),
                           (try_begin),
                             (eq, "$g_mt_mode", vba_after_training),
                             (add_reinforcements_to_entry, 1, 6),
                           (else_try),
                             (add_reinforcements_to_entry, 1, 29),
                           (try_end),
                           (call_script, "script_combat_music_set_situation_with_culture"),
                           ]),

      common_music_situation_update,
      common_battle_check_friendly_kills,
      common_battle_check_victory_condition,
      #common_battle_victory_display,

	  # NE cam
      # (1, 4, ti_once, [(main_hero_fallen)],
          # [
              # (assign, "$pin_player_fallen", 1),
              # (str_store_string, s5, "str_retreat"),
              # (call_script, "script_simulate_retreat", 10, 20, 1),
              # (assign, "$g_battle_result", -1),
              # (set_mission_result, -1),
              # (call_script, "script_count_mission_casualties_from_agents"),
              # (finish_mission, 0)]),
	 # ne end cam
      (1, 4, ti_once,
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
      ]),

      common_battle_inventory,      
      common_battle_order_panel,
      common_battle_order_panel_tick,
      
	  #camera_trigger_1,
      #camera_trigger_2,
      #camera_trigger_3,
      #camera_trigger_4,
      #camera_trigger_5,
      #camera_trigger_6,
      #camera_trigger_7,
      #camera_trigger_8,
      common_init_deathcam,
      common_start_deathcam,
      common_move_deathcam,
      common_rotate_deathcam,
	  
    ],
  ),

# NE rebellion
  ( # Village rebellion suppression - Jinnai
    "village_rebellion",mtf_battle_mode,charge,
    "You lead your men in attempting to suppress the rebellion.",
    [
     (3,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
     (1,mtef_team_0|mtef_use_exact_number,0,aif_start_alarmed, 7,[]),
     (3,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
     ],
    [
      lav_situational_damage_modifiers,
      common_battle_tab_press,

      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (try_begin), # Continue battle after the player is out - Jinnai
          (main_hero_fallen),
          (assign, "$pin_player_fallen", 1),
          (assign, "$g_battle_result", -1),
          (set_mission_result, -1),
        (else_try),
          (assign, "$pin_player_fallen", 0),
        (try_end),
        (str_store_string, s5, "str_retreat"),
        (call_script, "script_simulate_retreat", 10, 20),
        (assign, "$g_battle_result", -1),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),]),

      (0, 0, ti_once, [], [(assign, "$battle_won", 0),
                           (assign, "$defender_reinforcement_stage", 0),
                           (assign, "$attacker_reinforcement_stage", 0),
                           #(assign, "$g_presentation_battle_active", 0),
                           (try_begin),
                             (eq, "$g_mt_mode", vba_after_training),
                             (add_reinforcements_to_entry, 1, 6),
                           (else_try),
                             (add_reinforcements_to_entry, 1, 29),
                           (try_end),
                           (call_script, "script_combat_music_set_situation_with_culture"),
                           ]),

      common_music_situation_update,
      common_battle_check_friendly_kills,
      common_battle_check_victory_condition,
      #common_battle_victory_display,

#      (1, 4, ti_once, [(main_hero_fallen)],
#          [
#              (assign, "$pin_player_fallen", 1),
#              (str_store_string, s5, "str_retreat"),
#              (call_script, "script_simulate_retreat", 10, 20),
#              (assign, "$g_battle_result", -1),
#              (set_mission_result, -1),
#              (call_script, "script_count_mission_casualties_from_agents"),
#              (finish_mission, 0)]),
      (1, 4, ti_once,
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
      ]),

      common_battle_inventory,      
      common_battle_order_panel,
      common_battle_order_panel_tick,
      #camera_trigger_1,
      #camera_trigger_2,
      #camera_trigger_3,
      #camera_trigger_4,
      #camera_trigger_5,
      #camera_trigger_6,
      #camera_trigger_7,
      #camera_trigger_8,
      common_init_deathcam,
      common_start_deathcam,
      common_move_deathcam,
      common_rotate_deathcam,
      
    ],
  ),

# NE end rebellion
# NE quests 

    #v585 Josefgirl
	# Scene processing for fight with wedding guests
  (
    "village_attack_wedding",mtf_battle_mode,charge,
    "You lead your men to deal with the angry mob.",
    [
     (3,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
     (1,mtef_team_0|mtef_use_exact_number,0,aif_start_alarmed, 7,[]),
     (1,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
     ],
    [
      lav_situational_damage_modifiers,
      common_battle_tab_press,


      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (try_begin), #More letting the battle continue after the player is knocked out - Jinnai
          (main_hero_fallen),
          (assign, "$pin_player_fallen", 1),
          (assign, "$g_battle_result", -1),
          (set_mission_result, -1),
        (else_try),
          (assign, "$pin_player_fallen", 0),
        (try_end),
        (str_store_string, s5, "str_retreat"),
        (call_script, "script_simulate_retreat", 10, 20),
        (assign, "$g_battle_result", -1),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),]),

      (0, 0, ti_once, [], [(assign, "$battle_won", 0),
                           (assign, "$defender_reinforcement_stage", 0),
                           (assign, "$attacker_reinforcement_stage", 0),
                           #(assign, "$g_presentation_battle_active", 0),
                           (try_begin),
                             (eq, "$g_mt_mode", vba_after_training),
                             (add_reinforcements_to_entry, 1, 6),
                           (else_try),
                             (add_reinforcements_to_entry, 1, 29),
                           (try_end),
                           (call_script, "script_combat_music_set_situation_with_culture"),
                           ]),

      common_music_situation_update,
      common_battle_check_friendly_kills,
      common_battle_check_victory_condition,
      # common_battle_victory_display,

#      (1, 4, ti_once, [(main_hero_fallen)],
#          [
#              (assign, "$pin_player_fallen", 1),
#              (str_store_string, s5, "str_retreat"),
#              (call_script, "script_simulate_retreat", 10, 20),
#              (assign, "$g_battle_result", -1),
#              (set_mission_result, -1),
#              (call_script, "script_count_mission_casualties_from_agents"),
#              (finish_mission, 0)]),
      (1, 4, ti_once,
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
      ]),

      common_battle_inventory,      
      common_battle_order_panel,
      common_battle_order_panel_tick,
      #camera_trigger_1,
      #camera_trigger_2,
      #camera_trigger_3,
      #camera_trigger_4,
      #camera_trigger_5,
      #camera_trigger_6,
      #camera_trigger_7,
      #camera_trigger_8,
      common_init_deathcam,
      common_start_deathcam,
      common_move_deathcam,
      common_rotate_deathcam,
      
    ],
  ),
	
    #end v585 Josef

# NE end quests
  (
    "village_raid",mtf_battle_mode,charge,
    "You lead your men to battle.",
    [
     (3,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,12,[]),
     (3,mtef_defenders|mtef_team_0,0,aif_start_alarmed,0,[]),
     (1,mtef_attackers|mtef_team_1,0,aif_start_alarmed,12,[]),
     (1,mtef_attackers|mtef_team_1,0,aif_start_alarmed,0,[]),
     ],
    [
      lav_situational_damage_modifiers,
      common_battle_tab_press,
      common_battle_init_banner,

      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
		# ne cam
		(try_begin), #More stuff for the battle continuing after the player - Jinnai
          (main_hero_fallen),
          (assign, "$pin_player_fallen", 1),
          (assign, "$g_battle_result", -1),
          (set_mission_result,-1),
        (else_try),
        (assign, "$pin_player_fallen", 0),
		(try_end), 
		# ne end cam
        (str_store_string, s5, "str_retreat"),
        (call_script, "script_simulate_retreat", 10, 20, 1),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),]),

      (0, 0, ti_once, [], [(assign,"$g_battle_won",0),
                           (assign,"$defender_reinforcement_stage",0),
                           (assign,"$attacker_reinforcement_stage",0),
                           (call_script, "script_combat_music_set_situation_with_culture"),
                           ]),

      common_music_situation_update,
      common_battle_check_friendly_kills,

      (1, 0, 5, [(lt,"$defender_reinforcement_stage",2),
                 (store_mission_timer_a,":mission_time"),
                 (ge,":mission_time",10),
                 (store_normalized_team_count,":num_defenders", 0),
                 (lt,":num_defenders",6)],
           [(add_reinforcements_to_entry,0,6),(val_add,"$defender_reinforcement_stage",1)]),
      (1, 0, 5, [(lt,"$attacker_reinforcement_stage",2),
                 (store_mission_timer_a,":mission_time"),
                 (ge,":mission_time",10),
                 (store_normalized_team_count,":num_attackers", 1),
                 (lt,":num_attackers",6)],
           [(add_reinforcements_to_entry,3,6),(val_add,"$attacker_reinforcement_stage",1)]),

      (1, 60, ti_once,
       [
         (store_mission_timer_a,reg(1)),
         (ge,reg(1),10),
         (all_enemies_defeated, 5),
         (neg|main_hero_fallen, 0),
         (set_mission_result,1),
         (display_message,"str_msg_battle_won"),
         (assign,"$g_battle_won",1),
         (assign, "$g_battle_result", 1),
         (try_begin),
           (eq, "$g_village_raid_evil", 0),
           (call_script, "script_play_victorious_sound"),
         (else_try),
           (play_track, "track_victorious_evil", 1),
         (try_end),
         ],
       [
         (call_script, "script_count_mission_casualties_from_agents"),
         (finish_mission, 1),
         ]),

      #common_battle_victory_display,
      common_battle_check_victory_condition,
	  # ne cam 
      # (1, 4, ti_once, [(main_hero_fallen)],
          # [
              # (assign, "$pin_player_fallen", 1),
              # (str_store_string, s5, "str_retreat"),
              # (call_script, "script_simulate_retreat", 10, 20, 1),
              # (assign, "$g_battle_result", -1),
              # (set_mission_result,-1),
              # (call_script, "script_count_mission_casualties_from_agents"),
              # (finish_mission,0)]),
	   # ne end cam
      (1, 4, ti_once,
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
      ]),

      common_battle_inventory,
      common_battle_order_panel,
      common_battle_order_panel_tick,
	  
	  #camera_trigger_1,
      #camera_trigger_2,
      #camera_trigger_3,
      #camera_trigger_4,
      #camera_trigger_5,
      #camera_trigger_6,
      #camera_trigger_7,
      #camera_trigger_8,
      common_init_deathcam,
      common_start_deathcam,
      common_move_deathcam,
      common_rotate_deathcam,
	  

##      #AI Tiggers
##      (0, 0, ti_once, [
##          (store_mission_timer_a,reg(1)),(ge,reg(1),4),
##          (call_script, "script_select_battle_tactic"),
##          (call_script, "script_battle_tactic_init"),
##          ], []),
##      (1, 0, 0, [
##          (store_mission_timer_a,reg(1)),(ge,reg(1),4),
##          (call_script, "script_battle_tactic_apply"),
##          ], []),
    ],
  ),

  
  #  NE building
  
## Caltrop battle scene - Jinnai
  (
    "village_raid_no_horses",mtf_battle_mode,charge,
    "You lead your men to battle.",
    [
     (3,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,12,[]),
     (3,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),
     (1,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,12,[]),
     (1,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,0,[]),
     ],
    [
      lav_situational_damage_modifiers,
      common_battle_tab_press,

      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (try_begin), #Let the battle continue after the player is out - Jinnai
          (main_hero_fallen),
          (assign, "$pin_player_fallen", 1),
          (assign, "$g_battle_result", -1),
          (set_mission_result,-1),
        (else_try),
          (assign, "$pin_player_fallen", 0),
        (try_end),
        (str_store_string, s5, "str_retreat"),
        (call_script, "script_simulate_retreat", 10, 20),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),]),

      (0, 0, ti_once, [], [(assign,"$battle_won",0),
                           (assign,"$defender_reinforcement_stage",0),
                           (assign,"$attacker_reinforcement_stage",0),
                           #(assign, "$g_presentation_battle_active", 0),
                           (call_script, "script_combat_music_set_situation_with_culture"),
                           ]),

      common_music_situation_update,
      common_battle_check_friendly_kills,

      (1, 0, 5, [(lt,"$defender_reinforcement_stage",2),
                 (store_mission_timer_a,":mission_time"),
                 (ge,":mission_time",10),
                 (store_normalized_team_count,":num_defenders", 0),
                 (lt,":num_defenders",6)],
           [(add_reinforcements_to_entry,0,6),(val_add,"$defender_reinforcement_stage",1)]),
      (1, 0, 5, [(lt,"$attacker_reinforcement_stage",2),
                 (store_mission_timer_a,":mission_time"),
                 (ge,":mission_time",10),
                 (store_normalized_team_count,":num_attackers", 1),
                 (lt,":num_attackers",6)],
           [(add_reinforcements_to_entry,3,6),(val_add,"$attacker_reinforcement_stage",1)]),

      (1, 60, ti_once,
       [
         (store_mission_timer_a,reg(1)),
         (ge,reg(1),10),
         (all_enemies_defeated, 5),
         (neg|main_hero_fallen, 0),
         (set_mission_result,1),
         (display_message,"str_msg_battle_won"),
         (assign,"$battle_won",1),
         (assign, "$g_battle_result", 1),
         (try_begin),
           (eq, "$g_village_raid_evil", 0),
           (call_script, "script_play_victorious_sound"),
         (else_try),
           (play_track, "track_victorious_evil", 1),
         (try_end),
         ],
       [
         (call_script, "script_count_mission_casualties_from_agents"),
         (finish_mission, 1),
         ]),

      #common_battle_victory_display,
      common_battle_check_victory_condition,
#      (1, 4, ti_once, [(main_hero_fallen)],
#         [
#              (assign, "$pin_player_fallen", 1),
#              (str_store_string, s5, "str_retreat"),
#              (call_script, "script_simulate_retreat", 10, 20),
#              (assign, "$g_battle_result", -1),
#              (set_mission_result,-1),
#              (call_script, "script_count_mission_casualties_from_agents"),
#              (finish_mission,0)]),
      (1, 4, ti_once,
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
      ]),

      common_battle_inventory,
      common_battle_order_panel,
      common_battle_order_panel_tick,
      #camera_trigger_1,
      #camera_trigger_2,
      #camera_trigger_3,
      #camera_trigger_4,
      #camera_trigger_5,
      #camera_trigger_6,
      #camera_trigger_7,
      #camera_trigger_8,
      common_init_deathcam,
      common_start_deathcam,
      common_move_deathcam,
      common_rotate_deathcam,

    ],
  ),

# NE end building

##  (
##    "charge_with_allies",mtf_battle_mode,charge_with_ally,
##    "Taking a handful of fighters with you, you set off to patrol the area.",
##    [
##     (1,mtef_defenders,0,0|aif_start_alarmed,8,[]),
##     (0,mtef_defenders,0,0|aif_start_alarmed,0,[]),
##     (4,mtef_attackers,0,aif_start_alarmed,8,[]),
##     (4,mtef_attackers,0,aif_start_alarmed,0,[]),
##     ],
##    [
##      (ti_tab_pressed, 0, 0, [],
##       [
##           (try_begin),
##             (eq, "$battle_won", 1),
##             (finish_mission,0),
##           (else_try),
##             (call_script, "script_cf_check_enemies_nearby"),
##             (question_box,"str_do_you_want_to_retreat"),
##           (else_try),
##             (display_message,"str_can_not_retreat"),
##           (try_end),
##        ]),
##      (ti_question_answered, 0, 0, [],
##       [(store_trigger_param_1,":answer"),
##        (eq,":answer",0),
##        (assign, "$pin_player_fallen", 0),
##        (str_store_string, s5, "str_retreat"),
##        (call_script, "script_simulate_retreat", 10, 30),
##        (finish_mission,0),]),
##
##      (0, 0, ti_once, [], [(assign,"$battle_won",0),(assign,"$defender_reinforcement_stage",0),(assign,"$attacker_reinforcement_stage",0)]),
##      (1, 0, 5, [(lt,"$defender_reinforcement_stage",2),(store_mission_timer_a,reg(1)),(ge,reg(1),10),(store_defender_count,reg(2)),(lt,reg(2),3)],
##           [(add_reinforcements_to_entry,0,4),(val_add,"$defender_reinforcement_stage",1)]),
##      (1, 0, 5, [(lt,"$attacker_reinforcement_stage",2),(store_mission_timer_a,reg(1)),(ge,reg(1),10),(store_attacker_count,reg(2)),(lt,reg(2),3)],
##           [(add_reinforcements_to_entry,3,4),(val_add,"$attacker_reinforcement_stage",1)]),
##      (1, 60, ti_once, [(store_mission_timer_a,reg(1)),
##                        (ge,reg(1),10),(all_enemies_defeated,2),
##                        (neg|main_hero_fallen,0),
##                        (set_mission_result,1),
##                        (assign, "$g_battle_result", 1),
##                        (display_message,"str_msg_battle_won"),
##                        (assign,"$battle_won",1)],
##           [(finish_mission,1)]),
##      (10, 0, 0, [], [(eq,"$battle_won",1),(display_message,"str_msg_battle_won")]),
##
##      (1, 4, ti_once, [(main_hero_fallen)],
##          [
##              (assign, "$pin_player_fallen", 1),
##              (str_store_string, s5, "str_retreat"),
##              (call_script, "script_simulate_retreat", 20, 30),
##              (assign, "$g_battle_result", -1),
##              (set_mission_result,-1),(finish_mission,0)]),
##      (ti_inventory_key_pressed, 0, 0, [(display_message,"str_use_baggage_for_inventory")], []),
##    ],
##  ),

##  (
##    "charge_with_allies_old",mtf_battle_mode,charge_with_ally,
##    "Taking a handful of fighters with you, you set off to patrol the area.",
##    [(1,mtef_leader_only,0,0,1,[]),
##     (1,mtef_no_leader,0,0|aif_start_alarmed,2,[]),
##     (1,mtef_reverse_order|mtef_ally_party,0,0|aif_start_alarmed,3,[]),
##     (0,mtef_no_leader,0,0|aif_start_alarmed,0,[]),
##     (0,mtef_reverse_order|mtef_ally_party,0,0|aif_start_alarmed,0,[]),
##     (3,mtef_reverse_order|mtef_enemy_party,0,aif_start_alarmed,6,[]),
##     (4,mtef_reverse_order|mtef_enemy_party,0,aif_start_alarmed,0,[])],
##    [
##      (ti_tab_pressed, 0, 0, [],
##       [
##           (try_begin),
##             (eq, "$battle_won", 1),
##             (finish_mission,0),
##           (else_try),
##             (call_script, "script_cf_check_enemies_nearby"),
##             (question_box,"str_do_you_want_to_retreat"),
##           (else_try),
##             (display_message,"str_can_not_retreat"),
##           (try_end),
##        ]),
##      (ti_question_answered, 0, 0, [],
##       [(store_trigger_param_1,":answer"),(eq,":answer",0),(finish_mission,0),]),
##
##      (0, 0, ti_once, [], [(assign,"$battle_won",0),(assign,"$enemy_reinforcement_stage",0),(assign,"$friend_reinforcement_stage",0),(assign,"$ally_reinforcement_stage",0)]),
##      
##      (1, 0, 5, [(lt,"$enemy_reinforcement_stage",2),(store_mission_timer_a,reg(1)),(ge,reg(1),10),(store_enemy_count,reg(2)),(lt,reg(2),3)],
##       [(add_reinforcements_to_entry,6,3),(val_add,"$enemy_reinforcement_stage",1)]),
##      (1, 0, 5, [(lt,"$friend_reinforcement_stage",2),(store_mission_timer_a,reg(1)),(ge,reg(1),10),(store_friend_count,reg(2)),(lt,reg(2),2)],
##       [(add_reinforcements_to_entry,3,1),(val_add,"$friend_reinforcement_stage",1)]),
##      (1, 0, 5, [(lt,"$ally_reinforcement_stage",2),(store_mission_timer_a,reg(1)),(ge,reg(1),10),(store_ally_count,reg(2)),  (lt,reg(2),2)],
##       [(add_reinforcements_to_entry,4,2),(val_add,"$ally_reinforcement_stage",1)]),
##      (1, 60, ti_once, [(store_mission_timer_a,reg(1)),
##                        (ge,reg(1),10),
##                        (all_enemies_defeated,2),
##                        (neg|main_hero_fallen,0),
##                        (set_mission_result,1),
##                        (assign, "$g_battle_result", 1),
##                        (display_message,"str_msg_battle_won"),
##                        (assign,"$battle_won",1),
##                        ],
##       [(finish_mission,1)]),
##      (10, 0, 0, [], [(eq,"$battle_won",1),(display_message,"str_msg_battle_won")]),
##      (1, 4, ti_once, [(main_hero_fallen,0)],
##       [(set_mission_result,-1),(finish_mission,1)]),
##      (ti_inventory_key_pressed, 0, 0, [(display_message,"str_use_baggage_for_inventory")], []),
##    ],
##  ),
##  (
##    "lead_charge_old",mtf_battle_mode,charge,
##    "You lead your men to battle.",
##    [
##     (1,mtef_leader_only,0,0,1,[]),
##     (1,mtef_no_leader,0,0|aif_start_alarmed,5,[]),
##     (0,mtef_no_leader,0,0|aif_start_alarmed,0,[]),
##     (3,mtef_enemy_party|mtef_reverse_order,0,aif_start_alarmed,6,[]),
##     (4,mtef_enemy_party|mtef_reverse_order,0,aif_start_alarmed,0,[]),
##     ],
##    [
##      (ti_tab_pressed, 0, 0, [],
##       [
##           (try_begin),
##             (eq, "$battle_won", 1),
##             (finish_mission,0),
##           (else_try),
##             (call_script, "script_cf_check_enemies_nearby"),
##             (question_box,"str_do_you_want_to_retreat"),
##           (else_try),
##             (display_message,"str_can_not_retreat"),
##           (try_end),
##        ]),
##      (ti_question_answered, 0, 0, [],
##       [(store_trigger_param_1,":answer"),(eq,":answer",0),(finish_mission,0),]),
##
##      (0, 0, ti_once, [], [(assign,"$battle_won",0),(assign,"$enemy_reinforcement_stage",0),(assign,"$friend_reinforcement_stage",0)]),
##      (1, 0, 5, [(lt,"$enemy_reinforcement_stage",2),(store_mission_timer_a,reg(1)),(ge,reg(1),10),(store_enemy_count,reg(2)),(lt,reg(2),3)],
##           [(add_reinforcements_to_entry,4,3),(val_add,"$enemy_reinforcement_stage",1)]),
##      (1, 0, 5, [(lt,"$friend_reinforcement_stage",2),(store_mission_timer_a,reg(1)),(ge,reg(1),10),(store_friend_count,reg(2)),(lt,reg(2),3)],
##           [(add_reinforcements_to_entry,2,3),(val_add,"$friend_reinforcement_stage",1)]),
##      (1, 60, ti_once, [(store_mission_timer_a,reg(1)),
##                        (ge,reg(1),10),(all_enemies_defeated,2),
##                        (neg|main_hero_fallen,0),
##                        (set_mission_result,1),
##                        (assign, "$g_battle_result", 1),
##                        (display_message,"str_msg_battle_won"),
##                        (assign,"$battle_won",1)],
##           [(finish_mission,1)]),
##      (10, 0, 0, [], [(eq,"$battle_won",1),(display_message,"str_msg_battle_won")]),
##      (1, 4, ti_once, [(main_hero_fallen)],
##          [
##              (assign, "$g_battle_result", -1),
##              (set_mission_result,-1),(finish_mission,1)]),
##      (ti_inventory_key_pressed, 0, 0, [(display_message,"str_use_baggage_for_inventory")], []),
##    ],
##  ),



  (
    "besiege_inner_battle_castle",mtf_battle_mode,-1,
    "You attack the walls of the castle...",
    [
     (0, mtef_attackers|mtef_use_exact_number|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (6, mtef_attackers|mtef_use_exact_number|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (7, mtef_attackers|mtef_use_exact_number|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (16, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (17, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (18, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (19, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (20, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     ],
    [
      lav_situational_damage_modifiers,
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),

      common_battle_tab_press,
      common_battle_init_banner,

      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
		# ne cam
		 (try_begin), #Let the battle continue after the player is out - Jinnai
          (main_hero_fallen),
          (assign, "$pin_player_fallen", 1),
        (else_try),
          (assign, "$pin_player_fallen", 0),
        (try_end),
		# ne end cam
		
        (str_store_string, s5, "str_retreat"),
        (call_script, "script_simulate_retreat", 5, 20, 0),
        (assign, "$g_battle_result", -1),
        (set_mission_result,-1),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),
        ]),
        
      (0, 0, ti_once, [], [(assign,"$g_battle_won",0),
                           (call_script, "script_music_set_situation_with_culture", mtf_sit_ambushed),
                           ]),
      
      #AI Tiggers
      (0, 0, ti_once, [
          (assign, "$defender_team", 0),
          (assign, "$attacker_team", 1),
          (assign, "$defender_team_2", 2),
          (assign, "$attacker_team_2", 3),
          ], []),

      common_battle_check_friendly_kills,
      common_battle_check_victory_condition,
      common_battle_victory_display,

      # (1, 4, ti_once, [(main_hero_fallen)],
          # [
              # (assign, "$pin_player_fallen", 1),
              # (str_store_string, s5, "str_retreat"),
              # (call_script, "script_simulate_retreat", 5, 20, 0),
              # (assign, "$g_battle_result", -1),
              # (set_mission_result,-1),
              # (call_script, "script_count_mission_casualties_from_agents"),
              # (finish_mission,0)
              # ]),
      (1, 4, ti_once,
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
      ]),
      
      common_battle_order_panel,
      common_battle_order_panel_tick,
      common_battle_inventory,
	  
	  # ne cam
	  #camera_trigger_1,
      #camera_trigger_2,
      #camera_trigger_3,
      #camera_trigger_4,
      #camera_trigger_5,
      #camera_trigger_6,
      #camera_trigger_7,
      #camera_trigger_8,
	  ## ne end cam
      common_init_deathcam,
      common_start_deathcam,
      common_move_deathcam,
      common_rotate_deathcam,
	  
    ],
  ),

  (
    "besiege_inner_battle_town_center",mtf_battle_mode,-1,
    "You attack the walls of the castle...",
    [
     (0, mtef_attackers|mtef_use_exact_number|mtef_team_1,af_override_horse,aif_start_alarmed,4,[]),
     (2, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (23, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (24, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (25, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (26, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (27, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (28, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     ],
    [
      lav_situational_damage_modifiers,
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),

      common_battle_tab_press,
      common_battle_init_banner,

      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
		# ne cam
        (try_begin), #Let the battle continue after the player is out - Jinnai
          (main_hero_fallen),
          (assign, "$pin_player_fallen", 1),
        (else_try),
          (assign, "$pin_player_fallen", 0),
        (try_end),
		# ne end cam 
        (str_store_string, s5, "str_retreat"),
        (call_script, "script_simulate_retreat", 5, 20, 0),
        (assign, "$g_battle_result", -1),
        (set_mission_result,-1),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),
        ]),
        
      (0, 0, ti_once, [], [(assign,"$g_battle_won",0),
                           (call_script, "script_music_set_situation_with_culture", mtf_sit_ambushed),
                           ]),
      
      #AI Tiggers
      (0, 0, ti_once, [
          (assign, "$defender_team", 0),
          (assign, "$attacker_team", 1),
          (assign, "$defender_team_2", 2),
          (assign, "$attacker_team_2", 3),
          ], []),

      common_battle_check_friendly_kills,
      common_battle_check_victory_condition,
      common_battle_victory_display,

      # (1, 4, ti_once, [(main_hero_fallen)],
          # [
              # (assign, "$pin_player_fallen", 1),
              # (str_store_string, s5, "str_retreat"),
              # (call_script, "script_simulate_retreat", 5, 20, 0),
              # (assign, "$g_battle_result", -1),
              # (set_mission_result,-1),
              # (call_script, "script_count_mission_casualties_from_agents"),
              # (finish_mission,0)
              # ]),
      (1, 4, ti_once,
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
      ]),

      common_battle_order_panel,
      common_battle_order_panel_tick,
      common_battle_inventory,
	  
	  # ne cam
	  #camera_trigger_1,
      #camera_trigger_2,
      #camera_trigger_3,
      #camera_trigger_4,
      #camera_trigger_5,
      #camera_trigger_6,
      #camera_trigger_7,
      #camera_trigger_8,
	  # ne cam
      common_init_deathcam,
      common_start_deathcam,
      common_move_deathcam,
      common_rotate_deathcam,
	  
    ],
  ),

  (
    "castle_attack_walls_defenders_sally",mtf_battle_mode,-1,
    "You attack the walls of the castle...",
    [
     (0,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,12,[]),
     (0,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,0,[]),
     (3,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,12,[]),
     (3,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),
     ],
    [
      lav_situational_damage_modifiers,
      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (call_script, "script_agent_reassign_team", ":agent_no"),
         ]),
      
      (ti_before_mission_start, 0, 0, [],
       [
         (team_set_relation, 0, 2, 1),
         (team_set_relation, 1, 3, 1),
         (call_script, "script_change_banners_and_chest"),
         (call_script, "script_remove_siege_objects"),
         ]),

      common_battle_tab_press,
      common_battle_init_banner,

      (ti_on_agent_killed_or_wounded, 0, 0, [], #new
       [
        (store_trigger_param_1, ":dead_agent_no"),
        (store_trigger_param_2, ":killer_agent_no"),
        (store_trigger_param_3, ":is_wounded"),

        (try_begin),
          (ge, ":dead_agent_no", 0),
          (neg|agent_is_ally, ":dead_agent_no"),
          (agent_is_human, ":dead_agent_no"),
          (agent_get_troop_id, ":dead_agent_troop_id", ":dead_agent_no"),
          (str_store_troop_name, s6, ":dead_agent_troop_id"),
          (assign, reg0, ":dead_agent_no"),
          (assign, reg1, ":killer_agent_no"),
          (assign, reg2, ":is_wounded"),
          (agent_get_team, reg3, ":dead_agent_no"),          
          #(display_message, "@{!}dead agent no : {reg0} ; killer agent no : {reg1} ; is_wounded : {reg2} ; dead agent team : {reg3} ; {s6} is added"), 
          (party_add_members, "p_total_enemy_casualties", ":dead_agent_troop_id", 1), #addition_to_p_total_enemy_casualties
          (eq, ":is_wounded", 1),
          (party_wound_members, "p_total_enemy_casualties", ":dead_agent_troop_id", 1), 
        (try_end),
       ]),

      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
		# ne cam
        (try_begin), #Let the battle continue after the player is out - Jinnai
          (main_hero_fallen),
          (assign, "$pin_player_fallen", 1),
          (assign, "$g_battle_result", -1),
          (set_mission_result, -1),		  
		  
        (else_try),
          (assign, "$pin_player_fallen", 0),
        (try_end),
		# ne end cam 
        (str_store_string, s5, "str_retreat"),
        (call_script, "script_simulate_retreat", 5, 20, 0),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),]),
        
      (0, 0, ti_once, [], [(assign,"$g_battle_won",0),
                           (call_script, "script_combat_music_set_situation_with_culture"),
                           ]),
      
      common_music_situation_update,
      common_battle_check_friendly_kills,

      (1, 60, ti_once, [(store_mission_timer_a, reg(1)),
                        (ge, reg(1), 10),
                        (all_enemies_defeated, 2),
                        #(neg|main_hero_fallen,0),
                        (set_mission_result,1),
                        (display_message,"str_msg_battle_won"),
                        (assign, "$g_battle_won", 1),
                        (assign, "$g_battle_result", 1),
                        (assign, "$g_siege_sallied_out_once", 1),
                        (assign, "$g_siege_method", 1), #reset siege timer
                        (call_script, "script_play_victorious_sound"),
                        ],
           [(call_script, "script_count_mission_casualties_from_agents"),
            (finish_mission,1)]),

      common_battle_victory_display,

      # (1, 4, ti_once, [(main_hero_fallen)],
          # [
              # (assign, "$pin_player_fallen", 1),
              # (str_store_string, s5, "str_retreat"),
              # (call_script, "script_simulate_retreat", 5, 20, 0),
              # (assign, "$g_battle_result", -1),
              # (set_mission_result, -1),
              # (call_script, "script_count_mission_casualties_from_agents"),
              # (finish_mission,0)]),
      (1, 4, ti_once,
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
      ]),

      common_battle_order_panel,
      common_battle_order_panel_tick,
      common_battle_inventory,
	  
	  	  # ne cam
	  #camera_trigger_1,
      #camera_trigger_2,
      #camera_trigger_3,
      #camera_trigger_4,
      #camera_trigger_5,
      #camera_trigger_6,
      #camera_trigger_7,
      #camera_trigger_8,
	  # ne cam
      common_init_deathcam,
      common_start_deathcam,
      common_move_deathcam,
      common_rotate_deathcam,
	  
    ],
  ),


  (
    "castle_attack_walls_belfry",mtf_battle_mode,-1,
    "You attack the walls of the castle...",
    [
     (0,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,12,[]),
     (0,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,0,[]),
     (10,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),
     (11,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,7,[]),
     (15,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),

     (40,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (41,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (42,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (43,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (44,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (45,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (46,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (47,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     ],
    [
      lav_situational_damage_modifiers,
      common_battle_mission_start,
      common_battle_tab_press,
      common_battle_init_banner,
      common_siege_question_answered,
      common_siege_init,
      common_music_situation_update,
      common_siege_ai_trigger_init,
      common_siege_ai_trigger_init_2,
	  
	  # NE building
	        common_siege_refill_arrows,
	  # NE end

      (0, 0, ti_once,
       [
         (set_show_messages, 0),
         (team_give_order, "$attacker_team", grc_everyone, mordr_spread_out),
         (team_give_order, "$attacker_team", grc_everyone, mordr_spread_out),
         (team_give_order, "$attacker_team", grc_everyone, mordr_spread_out),
         (set_show_messages, 1),
         ], []),
      
      (ti_on_agent_killed_or_wounded, 0, 0, [],
       [
        (store_trigger_param_1, ":dead_agent_no"),
        (store_trigger_param_2, ":killer_agent_no"),
        (store_trigger_param_3, ":is_wounded"),

        (try_begin),
          (ge, ":dead_agent_no", 0),
          (neg|agent_is_ally, ":dead_agent_no"),
          (agent_is_human, ":dead_agent_no"),
          (agent_get_troop_id, ":dead_agent_troop_id", ":dead_agent_no"),
          (str_store_troop_name, s6, ":dead_agent_troop_id"),
          (assign, reg0, ":dead_agent_no"),
          (assign, reg1, ":killer_agent_no"),
          (assign, reg2, ":is_wounded"),
          (agent_get_team, reg3, ":dead_agent_no"),          
          #(display_message, "@{!}dead agent no : {reg0} ; killer agent no : {reg1} ; is_wounded : {reg2} ; dead agent team : {reg3} ; {s6} is added"), 
          (party_add_members, "p_total_enemy_casualties", ":dead_agent_troop_id", 1), #addition_to_p_total_enemy_casualties
          (eq, ":is_wounded", 1),
          (party_wound_members, "p_total_enemy_casualties", ":dead_agent_troop_id", 1), 
        (try_end),
       ]),

      common_siege_ai_trigger_init_after_2_secs,
      common_siege_defender_reinforcement_check,
      common_siege_defender_reinforcement_archer_reposition,
      common_siege_attacker_reinforcement_check,
      common_siege_attacker_do_not_stall,
      common_battle_check_friendly_kills,
      common_battle_check_victory_condition,
      common_battle_victory_display,
      common_siege_refill_ammo,
      common_siege_check_defeat_condition,
      common_battle_order_panel,
      common_battle_order_panel_tick,
      common_inventory_not_available,
      common_siege_init_ai_and_belfry,
      common_siege_move_belfry,
      common_siege_rotate_belfry,
      common_siege_assign_men_to_belfry,
    ],
  ),

  (
    "castle_attack_walls_ladder",mtf_battle_mode,-1,
    "You attack the walls of the castle...",
    [
     (0,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,12,[]),
     (0,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,0,[]),
     (10,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),
     (11,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,7,[]),
     (15,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),

     (40,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (41,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (42,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (43,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (44,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (45,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (46,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     ],
    [
      lav_situational_damage_modifiers,
	
	# NE settings
	  shield_bash_trigger_1,
      shield_bash_trigger_2,
      shield_bash_trigger_3,
      shield_bash_trigger_4,
	# Ne end settings
      common_battle_mission_start,
      common_battle_tab_press,
      common_battle_init_banner,
      common_siege_question_answered,
      common_siege_init,
      common_music_situation_update,
      common_siege_ai_trigger_init,
      common_siege_ai_trigger_init_2,
      common_siege_ai_trigger_init_after_2_secs,
      common_siege_defender_reinforcement_check,
      common_siege_defender_reinforcement_archer_reposition,
      common_siege_attacker_reinforcement_check,
      common_siege_attacker_do_not_stall,
      common_battle_check_friendly_kills,
      common_battle_check_victory_condition,
      common_battle_victory_display,
      common_siege_refill_ammo,
      common_siege_check_defeat_condition,
      common_battle_order_panel,
      common_battle_order_panel_tick,
      common_inventory_not_available,
	  
	  	  # NE building
	        common_siege_refill_arrows,
	  # NE end
	  

      (ti_on_agent_killed_or_wounded, 0, 0, [],
       [
        (store_trigger_param_1, ":dead_agent_no"),
        (store_trigger_param_2, ":killer_agent_no"),
        (store_trigger_param_3, ":is_wounded"),

        (try_begin),
          (ge, ":dead_agent_no", 0),
          (neg|agent_is_ally, ":dead_agent_no"),
          (agent_is_human, ":dead_agent_no"),
          (agent_get_troop_id, ":dead_agent_troop_id", ":dead_agent_no"),
          (str_store_troop_name, s6, ":dead_agent_troop_id"),
          (assign, reg0, ":dead_agent_no"),
          (assign, reg1, ":killer_agent_no"),
          (assign, reg2, ":is_wounded"),
          (agent_get_team, reg3, ":dead_agent_no"),          
          #(display_message, "@{!}dead agent no : {reg0} ; killer agent no : {reg1} ; is_wounded : {reg2} ; dead agent team : {reg3} ; {s6} is added"), 
          (party_add_members, "p_total_enemy_casualties", ":dead_agent_troop_id", 1), #addition_to_p_total_enemy_casualties
          (eq, ":is_wounded", 1),
          (party_wound_members, "p_total_enemy_casualties", ":dead_agent_troop_id", 1), 
        (try_end),
       ]),

##      (15, 0, 0,
##       [
##         (get_player_agent_no, ":player_agent"),
##         (agent_get_team, ":agent_team", ":player_agent"),
##         (neq, "$attacker_team", ":agent_team"),
##         (assign, ":non_ranged", 0),
##         (assign, ":ranged", 0),
##         (assign, ":ranged_pos_x", 0),
##         (assign, ":ranged_pos_y", 0),
##         (set_fixed_point_multiplier, 100),
##         (try_for_agents, ":agent_no"),
##           (eq, ":non_ranged", 0),
##           (agent_is_human, ":agent_no"),
##           (agent_is_alive, ":agent_no"),
##           (neg|agent_is_defender, ":agent_no"),
##           (agent_get_class, ":agent_class", ":agent_no"),
##           (try_begin),
##             (neq, ":agent_class", grc_archers),
##             (val_add, ":non_ranged", 1),
##           (else_try),
##             (val_add, ":ranged", 1),
##             (agent_get_position, pos0, ":agent_no"),
##             (position_get_x, ":pos_x", pos0),
##             (position_get_y, ":pos_y", pos0),
##             (val_add, ":ranged_pos_x", ":pos_x"),
##             (val_add, ":ranged_pos_y", ":pos_y"),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (eq, ":non_ranged", 0),
##           (gt, ":ranged", 0),
##           (val_div, ":ranged_pos_x", ":ranged"),
##           (val_div, ":ranged_pos_y", ":ranged"),
##           (entry_point_get_position, pos0, 10),
##           (init_position, pos1),
##           (position_set_x, pos1, ":ranged_pos_x"),
##           (position_set_y, pos1, ":ranged_pos_y"),
##           (position_get_z, ":pos_z", pos0),
##           (position_set_z, pos1, ":pos_z"),
##           (get_distance_between_positions, ":dist", pos0, pos1),
##           (gt, ":dist", 1000), #average position of archers is more than 10 meters far from entry point 10
##           (team_give_order, "$attacker_team", grc_archers, mordr_hold),
##           (team_set_order_position, "$attacker_team", grc_archers, pos0),
##         (else_try),
##           (team_give_order, "$attacker_team", grc_everyone, mordr_charge),
##         (try_end),
##         ],
##       []),
    ],
  ),
  

  (
    "castle_visit",0,-1,
    "Castle visit",
    [(0,mtef_scene_source|mtef_team_0,af_override_horse|af_override_weapons|af_override_head,0,1,pilgrim_disguise),
     (1,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (3,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise), 
     (4,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise), #for doors
     (5,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (6,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (7,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (8,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(9,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(10,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(11,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (12,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(13,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(14,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(15,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (16,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(17,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(18,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(19,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (20,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(21,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(22,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(23,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (24,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(25,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(26,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(27,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (28,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(29,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(30,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(31,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (32,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(33,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(34,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(35,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (36,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(37,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(38,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(39,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     # Party members
     (40,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (41,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (42,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (43,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (44,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (45,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (46,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     ],
    [    
      lav_situational_damage_modifiers,
      (ti_on_agent_spawn, 0, 0, [],
      [
        (store_trigger_param_1, ":agent_no"),
        (call_script, "script_init_town_agent", ":agent_no"),
        (get_player_agent_no, ":player_agent"),
        (try_begin),
          (neq, ":player_agent", ":agent_no"),
          (agent_set_team, ":agent_no", 7),
        (try_end),
        
        (try_begin),
          (this_or_next|eq, "$talk_context", tc_escape),
          (eq, "$talk_context", tc_prison_break),
          (agent_get_troop_id, ":troop_no", ":agent_no"),
          (troop_get_slot, ":will_join_prison_break", ":troop_no", slot_troop_will_join_prison_break),
          (eq, ":will_join_prison_break", 1),
          (agent_set_team, ":agent_no", 0),
          (agent_ai_set_aggressiveness, ":agent_no", 5),
          (troop_set_slot, ":troop_no", slot_troop_will_join_prison_break, 0),

          (try_begin),
            (troop_slot_eq, ":troop_no", slot_troop_mission_participation, mp_prison_break_stand_back),
            (agent_get_position, pos1, ":agent_no"),                        
            (agent_set_scripted_destination, ":agent_no", pos1),
          (try_end),
        (try_end),
      ]),
      
      (ti_on_agent_killed_or_wounded, 0, 0, [],
      [
        (store_trigger_param_1, ":dead_agent_no"),
        (store_trigger_param_2, ":killer_agent_no"),
        #(store_trigger_param_3, ":is_wounded"),
        
        (agent_get_troop_id, ":dead_agent_troop_no", ":dead_agent_no"),
        (agent_get_troop_id, ":killer_agent_troop_no", ":killer_agent_no"),
                
        (try_begin), 
          (this_or_next|eq, ":dead_agent_troop_no", "trp_swadian_prison_guard"),
          (this_or_next|eq, ":dead_agent_troop_no", "trp_vaegir_prison_guard"),
          (this_or_next|eq, ":dead_agent_troop_no", "trp_khergit_prison_guard"),
          (this_or_next|eq, ":dead_agent_troop_no", "trp_nord_prison_guard"),
          (this_or_next|eq, ":dead_agent_troop_no", "trp_rhodok_prison_guard"),
          (eq, ":dead_agent_troop_no", "trp_sarranid_prison_guard"),
          
          (eq, ":killer_agent_troop_no", "trp_player"),
          
          (display_message, "@You got keys of dungeon."),
        (try_end),
      ]),     

      #JAILBREAK TRIGGERS 
      #Civilians get out of the way
      (1, 0, 0,
      [
        (this_or_next|eq, "$talk_context", tc_prison_break),
        (eq, "$talk_context", tc_escape),
      ],
      [
        #(agent_get_team, ":prisoner_agent", 0),
        (call_script, "script_neutral_behavior_in_fight"),
        (mission_disable_talk),
      ]),
      
      #The game begins with the town alerted
      (1, 0, ti_once,
      [
        #If I set this to 1, 0, ti_once, then the prisoner spawns twice
        (eq, "$talk_context", tc_escape),
      ],
      [
        (get_player_agent_no, ":player_agent"),
        (assign, reg6, ":player_agent"),
        (call_script, "script_activate_town_guard"),		
        
        (get_player_agent_no, ":player_agent"),
        (agent_get_position, pos4, ":player_agent"),
        
        (try_for_range, ":prisoner", active_npcs_begin, kingdom_ladies_end),
          (troop_slot_ge, ":prisoner", slot_troop_mission_participation, 1),
          
          (str_store_troop_name, s4, ":prisoner"),
          (display_message, "str_s4_joins_prison_break"),
          
          (store_current_scene, ":cur_scene"), #this might be a better option?
          (modify_visitors_at_site, ":cur_scene"),
          #<entry_no>,<troop_id>,<number_of_troops>, <team_no>, <group_no>), 
          #team no and group no are used in multiplayer mode only. default team in entry is used in single player mode
          (store_current_scene, ":cur_scene"),
          (modify_visitors_at_site, ":cur_scene"),
          (assign, ":nearest_entry_no", 24),
          (add_visitors_to_current_scene, ":nearest_entry_no", ":prisoner", 1, 0, 0),
          (troop_set_slot, ":prisoner", slot_troop_will_join_prison_break, 1),          
        (try_end),
	  ]),

      (ti_tab_pressed, 0, 0,
      [
        (try_begin),
          (this_or_next|eq, "$talk_context", tc_escape),
          (eq, "$talk_context", tc_prison_break),
          (display_message, "str_cannot_leave_now"),
        (else_try),
          (this_or_next|eq, "$g_mt_mode", tcm_default),
          (eq, "$g_mt_mode", tcm_disguised),
          (set_trigger_result, 1),
          (mission_enable_talk),
        (else_try),
          (display_message, "str_cannot_leave_now"),
        (try_end),
      ], 
      []),
            
      (ti_before_mission_start, 0, 0, [], 
      [
        (call_script, "script_change_banners_and_chest"),
        (call_script, "script_remove_siege_objects"),
      ]),
      
      (3, 0, 0, 
      [     
        (main_hero_fallen, 0),
      ],	  
      [
        (try_begin),
          (this_or_next|eq, "$talk_context", tc_prison_break),
          (eq, "$talk_context", tc_escape),
       
          (call_script, "script_deduct_casualties_from_garrison"),
	      (jump_to_menu,"mnu_captivity_start_castle_defeat"), 
	 
	      (assign, ":end_cond", kingdom_ladies_end),
          (try_for_range, ":prisoner", active_npcs_begin, ":end_cond"),
  	        (troop_set_slot, ":prisoner", slot_troop_mission_participation, 0), #new	  
  	      (try_end),  
	 
	      (mission_enable_talk),
	      (finish_mission, 0),
	    (else_try),  
	      (mission_enable_talk),
	      (finish_mission, 0),
	      (set_trigger_result, 1),
        (try_end),	 	 
      ]),
      
      (3, 0, 0, 
      [
        (eq, "$talk_context", tc_escape),
        (neg|main_hero_fallen,0),
        (store_mission_timer_a, ":time"),
        (ge, ":time", 10),      
        (all_enemies_defeated), #1 is default enemy team for in-town battles
      ],
      [
        (call_script, "script_deduct_casualties_from_garrison"),
        (try_for_agents, ":agent"),
          (agent_get_troop_id, ":troop", ":agent"),
          (troop_slot_ge, ":troop", slot_troop_mission_participation, mp_prison_break_fight),
          (try_begin),
            (agent_is_alive, ":agent"),
            (troop_set_slot, ":troop", slot_troop_mission_participation, mp_prison_break_escaped),
          (else_try),
            (troop_set_slot, ":troop", slot_troop_mission_participation, mp_prison_break_caught),
          (try_end),
        (try_end),
        (jump_to_menu, "mnu_sneak_into_town_caught_ran_away"),
        (mission_enable_talk),
        (finish_mission, 0),
      ]),
    ],
  ),


  (
    "training_ground_trainer_talk", 0, -1,
    "Training.",
    [
      (0,mtef_scene_source|mtef_team_0,af_override_horse|af_override_weapons,0,1,[]),
      (1,mtef_scene_source|mtef_team_0,af_override_horse|af_override_weapons,0,1,[]),
      (2,mtef_scene_source|mtef_team_0,af_override_horse|af_override_weapons,0,1,[]),
      (3,mtef_scene_source|mtef_team_0,af_override_horse|af_override_weapons,0,1,[]),
      (4,mtef_scene_source|mtef_team_0,af_override_horse|af_override_weapons,0,1,[]),
      (5,mtef_scene_source|mtef_team_0,af_override_horse|af_override_weapons,0,1,[]),
      (6,mtef_scene_source|mtef_team_0,0,0,1,[]),
    ],
    [
      lav_situational_damage_modifiers,
      (ti_before_mission_start, 0, 0, [],
       [
         (call_script, "script_change_banners_and_chest"),
         ]),
      (ti_inventory_key_pressed, 0, 0,
       [
         (set_trigger_result,1),
         ], []),
      (ti_tab_pressed, 0, 0,
       [
         (set_trigger_result,1),
         ], []),
    ],
  ),

  (
    "training_ground_trainer_training",mtf_arena_fight,-1,
    "You will fight a match in the arena.",
    [
      (16, mtef_visitor_source|mtef_team_0,af_override_everything,aif_start_alarmed,1,[itm.practice_shield,itm.practice_sword,itm.practice_boots]),
      (17, mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[itm.practice_staff,itm.practice_boots]),
      (18, mtef_visitor_source|mtef_team_2,af_override_everything,aif_start_alarmed,1,[itm.practice_staff,itm.practice_boots]),
      (19, mtef_visitor_source|mtef_team_3,af_override_everything,aif_start_alarmed,1,[itm.heavy_practice_sword,itm.practice_boots]),
      (20, mtef_visitor_source,0,0,1,[]),
    ],
    [
      lav_situational_damage_modifiers,
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),
      
      common_arena_fight_tab_press,
      
      (ti_question_answered, 0, 0, [],
       [
         (store_trigger_param_1, ":answer"),
         (eq, ":answer", 0),
         (set_jump_mission, "mt_training_ground_trainer_talk"),
         (modify_visitors_at_site, "$g_training_ground_melee_training_scene"),
         (reset_visitors),
         (set_jump_entry, 5),
         (jump_to_scene, "$g_training_ground_melee_training_scene"),
         ]),
      (1, 3, ti_once, [(main_hero_fallen,0)],
       [
         (set_jump_mission, "mt_training_ground_trainer_talk"),
         (modify_visitors_at_site, "$g_training_ground_melee_training_scene"),
         (reset_visitors),
         (set_jump_entry, 5),
         (jump_to_scene, "$g_training_ground_melee_training_scene"),
         ]),
      (1, 3, ti_once,
       [
         (store_mission_timer_a, reg1),
         (ge, reg1, 1),
         (num_active_teams_le, 1),
         (neg|main_hero_fallen),
         (assign, "$training_fight_won", 1),
         ],
       [
         (set_jump_mission, "mt_training_ground_trainer_talk"),
         (modify_visitors_at_site, "$g_training_ground_melee_training_scene"),
         (reset_visitors),
         (set_jump_entry, 5),
         (jump_to_scene, "$g_training_ground_melee_training_scene"),
         ]),
      (ti_inventory_key_pressed, 0, 0, [(display_message,"str_cant_use_inventory_arena")], []),
    ],
  ),


  (
    "training_ground_training", mtf_arena_fight, -1,
    "Training.",
    [
      (0,mtef_visitor_source|mtef_team_0,af_override_everything,aif_start_alarmed,1,[itm.practice_staff]),
      (1,mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[itm.practice_staff]),
      (2,mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[itm.practice_staff]),
      (3,mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[itm.practice_staff]),
      (4,mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[itm.practice_staff]),
      (8,mtef_visitor_source,af_override_weapons|af_override_horse|af_override_head,0,1,[]),
      (9,mtef_visitor_source,af_override_weapons|af_override_horse|af_override_head,0,1,[]),
      (10,mtef_visitor_source,af_override_weapons|af_override_horse|af_override_head,0,1,[]),
      (11,mtef_visitor_source,af_override_weapons|af_override_horse|af_override_head,0,1,[]),
      (12,mtef_visitor_source,af_override_weapons|af_override_horse|af_override_head,0,1,[]),
      (13,mtef_visitor_source,af_override_weapons|af_override_horse|af_override_head,0,1,[]),
      (14,mtef_visitor_source,af_override_weapons|af_override_horse|af_override_head,0,1,[]),
      (15,mtef_visitor_source,af_override_weapons|af_override_horse|af_override_head,0,1,[]),
    ],
    [
      lav_situational_damage_modifiers,
      (ti_before_mission_start, 0, 0, [],
       [
         (assign, "$g_last_destroyed_gourds", 0),
         (call_script, "script_change_banners_and_chest")]),
      
      common_arena_fight_tab_press,
      
      (ti_question_answered, 0, 0, [],
       [
         (store_trigger_param_1,":answer"),
         (eq,":answer",0),
         (assign, "$g_training_ground_training_success_ratio", 0),
         (jump_to_menu, "mnu_training_ground_training_result"),
         (finish_mission),
         ]),
      
      common_inventory_not_available,

      (0, 0, ti_once,
       [
         (try_begin),
           (eq, "$g_mt_mode", ctm_ranged),
           (set_fixed_point_multiplier, 100),
           (entry_point_get_position, pos1, 0),
           (init_position, pos2),
           (position_set_y, pos2, "$g_training_ground_ranged_distance"),
           (position_transform_position_to_parent, pos3, pos1, pos2),
           (copy_position, pos1, pos3),
           (assign, ":end_cond", 10),
           (assign, ":shift_value", 0),
           (try_for_range, ":cur_i", 0, ":end_cond"),
             (store_sub, ":cur_instance", ":cur_i", ":shift_value"),
             (scene_prop_get_instance, ":target_object", "spr_gourd", ":cur_instance"),
             (copy_position, pos2, pos1),
             (init_position, pos0),
             (store_random_in_range, ":random_no", 0, 360),
             (position_rotate_z, pos2, ":random_no"),
             (store_random_in_range, ":random_no", 50, 600),
             (position_move_x, pos2, ":random_no"),
             (store_random_in_range, ":random_no", 0, 360),
             (position_transform_position_to_local, pos3, pos1, pos2),
             (position_rotate_z, pos0, ":random_no"),
             (position_transform_position_to_parent, pos4, pos0, pos3),
             (position_transform_position_to_parent, pos2, pos1, pos4),
             (position_set_z_to_ground_level, pos2),
             (position_move_z, pos2, 150),
             (assign, ":valid", 1),
             (try_for_range, ":cur_instance_2", 0, 10),
               (eq, ":valid", 1),
               (neq, ":cur_instance", ":cur_instance_2"),
               (scene_prop_get_instance, ":target_object_2", "spr_gourd", ":cur_instance_2"),
               (prop_instance_get_position, pos3, ":target_object_2"),
               (get_distance_between_positions, ":dist", pos2, pos3),
               (lt, ":dist", 100),
               (assign, ":valid", 0),
             (try_end),
             (try_begin),
               (eq, ":valid", 0),
               (val_add, ":end_cond", 1),
               (val_add, ":shift_value", 1),
             (else_try),
               (prop_instance_set_position, ":target_object", pos2),
               (prop_instance_animate_to_position, ":target_object", pos2, 1),
               (scene_prop_get_instance, ":target_object_2", "spr_gourd_spike", ":cur_instance"),
               (position_move_z, pos2, -150), #moving back to ground level
               (prop_instance_set_position, ":target_object_2", pos2),
               (prop_instance_animate_to_position, ":target_object_2", pos2, 1),
             (try_end),
           (try_end),
         (else_try),
           (eq, "$g_mt_mode", ctm_mounted),
           (assign, ":num_gourds", 0),
           #First, placing gourds on the spikes
           (try_for_range, ":cur_i", 0, 100),
             (scene_prop_get_instance, ":target_object", "spr_gourd", ":cur_i"),
             (scene_prop_get_instance, ":target_object_2", "spr_gourd_spike", ":cur_i"),
             (ge, ":target_object", 0),
             (ge, ":target_object_2", 0),
             (val_add, ":num_gourds", 1),
             (prop_instance_get_position, pos0, ":target_object_2"),
             (position_move_z, pos0, 150),
             (prop_instance_set_position, ":target_object", pos0),
             (prop_instance_animate_to_position, ":target_object", pos0, 1),
           (try_end),
           (store_sub, ":end_cond", ":num_gourds", "$g_training_ground_training_num_gourds_to_destroy"),
           #Second, removing gourds and their spikes randomly
           (try_for_range, ":cur_i", 0, ":end_cond"),
             (store_random_in_range, ":random_instance", 0, ":num_gourds"),
             (scene_prop_get_instance, ":target_object", "spr_gourd", ":random_instance"),
             (prop_instance_get_position, pos0, ":target_object"),
             (position_get_z, ":pos_z", pos0),
             (try_begin),
               (lt, ":pos_z", -50000),
#               (val_add, ":end_cond", 1), #removed already, try again
             (else_try),
               (position_set_z, pos0, -100000),
               (prop_instance_set_position, ":target_object", pos0),
               (prop_instance_animate_to_position, ":target_object", pos0, 1),
               (scene_prop_get_instance, ":target_object_2", "spr_gourd_spike", ":random_instance"),
               (prop_instance_set_position, ":target_object_2", pos0),
               (prop_instance_animate_to_position, ":target_object_2", pos0, 1),
             (try_end),
           (try_end),
         (try_end),
         ],
       []),

      (1, 3, ti_once,
       [
         (eq, "$g_mt_mode", ctm_melee),
         (this_or_next|main_hero_fallen),
         (num_active_teams_le, 1)
         ],
       [
         (try_begin),
           (neg|main_hero_fallen),
           (assign, "$g_training_ground_training_success_ratio", 100),
         (else_try),
           (assign, ":alive_enemies", 0),
           (try_for_agents, ":agent_no"),
             (agent_is_alive, ":agent_no"),
             (agent_is_human, ":agent_no"),
             (agent_get_team, ":team_no", ":agent_no"),
             (eq, ":team_no", 1),
             (val_add, ":alive_enemies", 1),
           (try_end),
           (store_sub, ":dead_enemies", "$g_training_ground_training_num_enemies", ":alive_enemies"),
           (store_mul, "$g_training_ground_training_success_ratio", ":dead_enemies", 100),
           (val_div, "$g_training_ground_training_success_ratio", "$g_training_ground_training_num_enemies"),
         (try_end),
         (jump_to_menu, "mnu_training_ground_training_result"),
         (finish_mission),
         ]),

      (1, 3, ti_once,
       [
         (eq, "$g_mt_mode", ctm_ranged),
         (get_player_agent_no, ":player_agent"),
         (agent_get_ammo, ":ammo", ":player_agent"),
         (store_mission_timer_a, ":cur_seconds"),
         (this_or_next|main_hero_fallen),
         (this_or_next|eq, ":ammo", 0),
         (gt, ":cur_seconds", 116), 
         ],
       [
         (store_mul, "$g_training_ground_training_success_ratio", "$scene_num_total_gourds_destroyed", 10),
         (jump_to_menu, "mnu_training_ground_training_result"),
         (finish_mission),
         ]),

      (1, 3, ti_once,
       [
         (eq, "$g_mt_mode", ctm_mounted),
         (get_player_agent_no, ":player_agent"),
         (agent_get_horse, ":player_horse", ":player_agent"),
         (store_mission_timer_a, ":cur_seconds"),
         (this_or_next|lt, ":player_horse", 0),
         (this_or_next|main_hero_fallen),
         (this_or_next|ge, "$scene_num_total_gourds_destroyed", "$g_training_ground_training_num_gourds_to_destroy"),
         (gt, ":cur_seconds", 120),
         ],
       [
         (store_mul, "$g_training_ground_training_success_ratio", "$scene_num_total_gourds_destroyed", 100),
         (val_div, "$g_training_ground_training_success_ratio", "$g_training_ground_training_num_gourds_to_destroy"),
         (jump_to_menu, "mnu_training_ground_training_result"),
         (finish_mission),
         ]),

      (0, 0, 0,
       [
         (gt, "$g_last_destroyed_gourds", 0),
         (try_begin),
           (eq, "$g_mt_mode", ctm_ranged),
           (entry_point_get_position, pos1, 0),
           (position_move_y, pos1, 100, 0),
           (get_player_agent_no, ":player_agent"),
           (agent_get_position, pos2, ":player_agent"),
           (try_begin),
             (position_is_behind_position, pos2, pos1),
             (val_add, "$scene_num_total_gourds_destroyed", "$g_last_destroyed_gourds"),
           (else_try),
             (display_message, "@You must stay behind the line on the ground! Point is not counted."),
           (try_end),
         (else_try),
           (val_add, "$scene_num_total_gourds_destroyed", "$g_last_destroyed_gourds"),
         (try_end),
         (assign, "$g_last_destroyed_gourds", 0),
         ],
       []),
    ],
  ),

  (
    "sneak_caught_fight",mtf_battle_mode,-1,
    "You must fight your way out!",
    [
     (0,mtef_scene_source|mtef_team_0,af_override_all,aif_start_alarmed,1,pilgrim_disguise),
     (1,mtef_scene_source|mtef_team_0,af_override_all,aif_start_alarmed,1,pilgrim_disguise),
     (2,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (3,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (4,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (5,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (6,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (7,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (8,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (9,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (10,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (11,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (12,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (13,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (14,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (15,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (16,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (17,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (18,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (19,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (20,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (21,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (22,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (23,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (24,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (25,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (26,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (27,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (28,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (29,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (30,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (31,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (32,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (33,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (34,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (35,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (36,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (37,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (38,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (39,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (40,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (41,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (42,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (43,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (44,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (45,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (46,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (47,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (48,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (49,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (50,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (51,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (52,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (53,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (54,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (55,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (56,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (57,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (58,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (59,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (60,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (61,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (62,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (63,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (64,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     
     # (0,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,pilgrim_disguise),
     # (25,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     # (26,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     # (27,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     # (28,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     # (29,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     # (30,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     # (31,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     # (32,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
    ],
    [    
      lav_situational_damage_modifiers,
      (ti_before_mission_start, 0, 0, [], 
      [
        (call_script, "script_change_banners_and_chest"),
      ]),
      
      (ti_after_mission_start, 0, 0, [],
       [
        (assign, ":num_guards", 5),
        
        (try_begin),
          (party_get_slot, ":last_nearby_fire_time", "$current_town", slot_town_last_nearby_fire_time),                          
          (store_current_hours, ":cur_time"),
          (store_add, ":fire_finish_time", ":last_nearby_fire_time", 4),                          
          (is_between, ":cur_time", ":fire_finish_time", ":last_nearby_fire_time"),
          (assign, ":num_guards", 2),
        (else_try),  
          (this_or_next|eq, "$talk_context", tc_escape),
          (eq, "$talk_context", tc_prison_break),

          (assign, ":num_guards", 4),
        (try_end),
        
        (try_begin),
          (this_or_next|eq, "$talk_context", tc_escape),
          (eq, "$talk_context", tc_prison_break),
          (entry_point_get_position, pos0, 7), 
        (else_try),          
          (party_slot_eq, "$current_town", slot_party_type, spt_town),
          (entry_point_get_position, pos0, 0), 
        (else_try),  
          (entry_point_get_position, pos0, 1), 
        (try_end),
                        
        (assign, ":last_nearest_entry_distance", -1),
        (assign, ":last_nearest_entry_point", -1),
        (try_for_range, ":guard_no", 0, ":num_guards"),
          (assign, ":smallest_dist", 100000),
          (try_for_range, ":guard_entry_point", 2, 64),
            (neq, ":last_nearest_entry_point", ":guard_entry_point"),
            (entry_point_get_position, pos1, ":guard_entry_point"), 
            (get_distance_between_positions, ":dist", pos0, pos1),
            (lt, ":dist", ":smallest_dist"),
            (gt, ":dist", ":last_nearest_entry_distance"),
            (assign, ":smallest_dist", ":dist"),
            (assign, ":nearest_entry_point", ":guard_entry_point"),
          (try_end),  
          
          (store_faction_of_party, ":town_faction","$current_town"),
          (try_begin),
            (this_or_next|eq, ":guard_no", 0),
            (eq, ":guard_no", 2),
            (faction_get_slot, ":troop_of_guard", ":town_faction", slot_faction_tier_2_troop),
          (else_try),  
            (faction_get_slot, ":troop_of_guard", ":town_faction", slot_faction_tier_2_troop),
          (try_end),
          
          (assign, ":last_nearest_entry_point", ":nearest_entry_point"),
          (assign, ":last_nearest_entry_distance", ":smallest_dist"),
                    
          (add_visitors_to_current_scene, ":nearest_entry_point", ":troop_of_guard", 1, 0),                      
        (try_end),
      ]),
      
      (ti_tab_pressed, 0, 0, [],
       [(question_box,"str_do_you_wish_to_surrender")]),
       
      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),(eq,":answer",0),(jump_to_menu,"mnu_captivity_start_castle_defeat"),(finish_mission,0),]),
      
      (1, 0, ti_once, [],
       [
         (play_sound,"snd_sneak_town_halt"),
         (call_script, "script_music_set_situation_with_culture", mtf_sit_fight),
         ]),
         
      (0, 3, 0,
       [
          (main_hero_fallen,0),
        ],
       [
         (jump_to_menu,"mnu_captivity_start_castle_defeat"),
         (finish_mission,0),
       ]),
       
      (1, 0, 0, [], 
       [
	    (get_player_agent_no, ":player_agent"),
	    (agent_get_position, pos0, ":player_agent"),
	    	    
        (try_for_agents, ":agent_no"),
          (neq, ":agent_no", ":player_agent"),
          (agent_is_alive, ":agent_no"),
          (agent_get_team, ":agent_team", ":agent_no"),
          (eq, ":agent_team", 1),
          
          (agent_get_position, pos1, ":agent_no"),
        
          (get_distance_between_positions, ":dist", pos0, pos1),
         
          (try_begin),
            (le, ":dist", 800),
            (agent_clear_scripted_mode, ":agent_no"),
          (else_try),  
            (agent_set_scripted_destination, ":agent_no", pos0, 0),
          (try_end),
        (try_end),                  	      
       ]), 

	   (5, 1, ti_once, 
	   [
	     (num_active_teams_le,1),
	     (neg|main_hero_fallen),

         (store_mission_timer_a,":cur_time"),
         (ge, ":cur_time", 5),
	   ],
       [
         (assign,"$auto_menu",-1),
         (jump_to_menu,"mnu_sneak_into_town_caught_dispersed_guards"),
         (finish_mission,1),
       ]),
       
	   (ti_on_leave_area, 0, ti_once, [],
       [(assign,"$auto_menu",-1),(jump_to_menu,"mnu_sneak_into_town_caught_ran_away"),(finish_mission,0)]),

      (ti_inventory_key_pressed, 0, 0, [(display_message,"str_cant_use_inventory_arena")], []),
      
    ],
  ),

   (
    "ai_training",0,-1,
    "You start training.",
    [
#     (0,0,af_override_horse,aif_start_alarmed,1,[]),
     (0,0,0,aif_start_alarmed,30,[]),
#     (1,mtef_no_leader,0,0|aif_start_alarmed,5,[]),
#     (0,mtef_no_leader,0,0|aif_start_alarmed,0,[]),
#     (3,mtef_enemy_party|mtef_reverse_order,0,aif_start_alarmed,6,[]),
#     (4,mtef_enemy_party|mtef_reverse_order,0,aif_start_alarmed,0,[]),
     ],
    [
      lav_situational_damage_modifiers,
#      (ti_before_mission_start, 0, 0, [], [(set_rain, 1,100), (set_fog_distance, 10)]),
      (ti_tab_pressed, 0, 0, [],
       [(finish_mission,0)]),

      common_battle_order_panel,
      common_battle_order_panel_tick,

##      (0, 0, ti_once,
##       [
##         (key_clicked, key_numpad_7),
##        (mission_cam_set_mode,1),
##        (get_player_agent_no, ":player_agent"),
##        (mission_cam_set_target_agent, ":player_agent", 1),
##        (mission_cam_set_animation, "anim_test_cam"),], []),
    ],
  ),

  (
    "arena_melee_fight",mtf_arena_fight,-1,
    "You enter a melee fight in the arena.",
    [
      (0,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[itm.practice_bow,itm.practice_arrows,itm.practice_horse,itm.arena_tunic_red, itm.red_tourney_helmet]),
      (1,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[itm.heavy_practice_sword, itm.arena_tunic_red]),
      (2,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[itm.heavy_practice_sword,itm.practice_horse,itm.arena_tunic_red, itm.red_tourney_helmet]),
      (3,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[itm.practice_lance,itm.practice_shield,itm.practice_horse,itm.arena_tunic_red, itm.red_tourney_helmet]),
      (4,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[itm.practice_bow,itm.practice_arrows, itm.practice_dagger, itm.arena_tunic_red]),
      (5,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[itm.practice_sword,itm.practice_shield,itm.arena_tunic_red]),
      (6,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[itm.heavy_practice_sword,itm.practice_horse,itm.arena_tunic_red]),
      (7,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[itm.practice_lance,itm.practice_shield,itm.practice_horse,itm.arena_tunic_red, itm.red_tourney_helmet]),

      (8,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm.practice_bow,itm.practice_arrows,itm.practice_dagger, itm.arena_tunic_blue]),
      (9,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm.practice_lance,itm.practice_shield,itm.practice_horse,itm.arena_tunic_blue,itm.blue_tourney_helmet]),
      (10,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm.heavy_practice_sword,itm.arena_tunic_blue]),
      (11,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm.practice_sword,itm.practice_shield,itm.arena_tunic_blue, itm.blue_tourney_helmet]),
      (12,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm.practice_bow,itm.practice_arrows,itm.practice_horse,itm.arena_tunic_blue]),
      (13,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm.practice_lance,itm.practice_shield,itm.practice_horse,itm.arena_tunic_blue,itm.blue_tourney_helmet]),
      (14,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm.heavy_practice_sword,itm.arena_tunic_blue]),
      (15,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm.practice_sword,itm.practice_shield,itm.arena_tunic_blue]),

      (16,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[itm.practice_bow,itm.practice_arrows,itm.practice_horse,itm.arena_tunic_green, itm.green_tourney_helmet]),
      (17,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[itm.heavy_practice_sword,itm.arena_tunic_green, itm.green_tourney_helmet]),
      (18,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[itm.heavy_practice_sword,itm.practice_horse,itm.arena_tunic_green, itm.green_tourney_helmet]),
      (19,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[itm.practice_lance,itm.practice_shield,itm.practice_horse,itm.arena_tunic_green, itm.green_tourney_helmet]),
      (20,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[itm.practice_bow,itm.practice_arrows,itm.practice_dagger, itm.arena_tunic_green, itm.green_tourney_helmet]),
      (21,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[itm.practice_sword,itm.practice_shield,itm.arena_tunic_green]),
      (22,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[itm.heavy_practice_sword,itm.practice_horse,itm.arena_tunic_green]),
      (23,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[itm.practice_lance,itm.practice_shield,itm.practice_horse,itm.arena_tunic_green, itm.green_tourney_helmet]),

      (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm.practice_bow,itm.practice_arrows,itm.practice_horse,itm.arena_tunic_yellow, itm.gold_tourney_helmet]),
      (25,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm.heavy_practice_sword,itm.arena_tunic_yellow, itm.gold_tourney_helmet]),
      (26,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm.heavy_practice_sword,itm.practice_horse,itm.arena_tunic_yellow, itm.gold_tourney_helmet]),
      (27,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm.practice_lance,itm.practice_shield,itm.practice_horse,itm.arena_tunic_yellow, itm.gold_tourney_helmet]),
      (28,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm.practice_bow,itm.practice_arrows,itm.practice_dagger, itm.arena_tunic_yellow, itm.gold_tourney_helmet]),
      (29,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm.practice_sword,itm.practice_shield,itm.arena_tunic_yellow]),
      (30,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm.heavy_practice_sword,itm.practice_horse,itm.arena_tunic_yellow]),
      (31,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm.practice_lance,itm.practice_shield,itm.practice_horse,itm.arena_tunic_yellow, itm.gold_tourney_helmet]),
#32
      (32, mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm.heavy_practice_sword]),
      (33,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[itm.practice_staff]),
      (34,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm.practice_sword, itm.practice_shield]),
      (35,mtef_visitor_source|mtef_team_4,af_override_all,aif_start_alarmed,1,[itm.practice_staff]),
      (36, mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm.practice_horse,itm.practice_sword]),#[itm.practice_bow,itm.practice_arrows, itm.practice_dagger]),
      (37,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[itm.practice_sword, itm.practice_shield]),
      (38,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm.heavy_practice_sword]),
      (39,mtef_visitor_source|mtef_team_4,af_override_all,aif_start_alarmed,1,[itm.practice_staff]),
#40-49 not used yet
      (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm.practice_bow,itm.practice_arrows,itm.practice_horse,itm.arena_tunic_yellow, itm.gold_tourney_helmet]),
      (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm.heavy_practice_sword,itm.arena_tunic_yellow, itm.gold_tourney_helmet]),
      (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm.heavy_practice_sword,itm.practice_horse,itm.arena_tunic_yellow, itm.gold_tourney_helmet]),
      (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm.practice_lance,itm.practice_shield,itm.practice_horse,itm.arena_tunic_yellow, itm.gold_tourney_helmet]),
      (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm.practice_bow,itm.practice_arrows,itm.practice_dagger, itm.arena_tunic_yellow, itm.gold_tourney_helmet]),
      (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm.practice_sword,itm.practice_shield,itm.arena_tunic_yellow]),
      (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm.heavy_practice_sword,itm.practice_horse,itm.arena_tunic_yellow]),
      (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm.practice_lance,itm.practice_shield,itm.practice_horse,itm.arena_tunic_yellow, itm.gold_tourney_helmet]),
      (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm.practice_bow,itm.practice_arrows,itm.practice_horse,itm.arena_tunic_yellow, itm.gold_tourney_helmet]),
      (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm.practice_bow,itm.practice_arrows,itm.practice_horse,itm.arena_tunic_yellow, itm.gold_tourney_helmet]),

      (50, mtef_scene_source,af_override_horse|af_override_weapons|af_override_head,0,1,[]),
      (51, mtef_visitor_source,af_override_horse|af_override_weapons|af_override_head,0,1,[]),
      (52, mtef_scene_source,af_override_horse,0,1,[]),
#not used yet:
      (53, mtef_scene_source,af_override_horse,0,1,[]),(54, mtef_scene_source,af_override_horse,0,1,[]),(55, mtef_scene_source,af_override_horse,0,1,[]),
#used for torunament master scene

      (56, mtef_visitor_source|mtef_team_0, af_override_all, aif_start_alarmed, 1, [itm.practice_sword, itm.practice_shield, itm.padded_cloth, itm.segmented_helmet]),
      (57, mtef_visitor_source|mtef_team_0, af_override_all, aif_start_alarmed, 1, [itm.practice_sword, itm.practice_shield, itm.padded_cloth, itm.segmented_helmet]),
    ],
    [
      lav_situational_damage_modifiers,
    ] + tournament_triggers
  ),

  # NE arena
## Created a new template for sparring, just for simplicity - Jinnai
  ("arena_spar_fight",mtf_arena_fight,-1,
    "You enter a sparring match in the arena.",
    [
      (0,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (1,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (2,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (3,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (4,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (5,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (6,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (7,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (8,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (9,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (10,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (11,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (12,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (13,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (14,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (15,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

      (16,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),
      (17,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),
      (18,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),
      (19,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),
      (20,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),
      (21,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),
      (22,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),
      (23,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),

      (24,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),
      (25,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),
      (26,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),
      (27,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),
      (28,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),
      (29,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),
      (30,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),
      (31,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),

      (50, mtef_scene_source,af_override_horse|af_override_weapons|af_override_head,0,1,[]),
      (52, mtef_scene_source,af_override_horse,0,1,[]),
      (53, mtef_scene_source,af_override_horse,0,1,[]),
      (54, mtef_scene_source,af_override_horse,0,1,[]),
      (55, mtef_scene_source,af_override_horse,0,1,[]),
    ],
    [
      lav_situational_damage_modifiers,
      call_horse_trigger_1,
      call_horse_trigger_2,
      shield_bash_trigger_1,
      shield_bash_trigger_2,
      shield_bash_trigger_3,
      shield_bash_trigger_4,
      spearwall_trigger_1,
      spearwall_trigger_2,
      spearwall_trigger_3,
      spearwall_trigger_4,
      spearwall_trigger_5,
      spearwall_trigger_6,
      spearwall_trigger_7,
      spearwall_trigger_8,
      spearwall_trigger_9,
      #camera_trigger_1,
      #camera_trigger_2,
      #camera_trigger_3,
      #camera_trigger_4,
      #camera_trigger_5,
      #camera_trigger_6,
      #camera_trigger_7,
      #camera_trigger_8,

    (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),
    (ti_inventory_key_pressed, 0, 0, [(display_message,"str_cant_use_inventory_arena")], []),
    (ti_tab_pressed, 0, 0, [],
      [(question_box,"@End the sparring match?")]),
    (ti_question_answered, 0, 0, [],
      [(store_trigger_param_1,":answer"),
       (eq,":answer",0),
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

    (0, 0, ti_once, [],
      [(play_sound, "snd_arena_ambiance", sf_looping),
     (call_script, "script_music_set_situation_with_culture", mtf_sit_arena),
      ]),

    (0.1, 0, 0, [],
      [
        (try_for_agents,":agent"),
          (agent_is_alive,":agent"),
          (agent_is_human,":agent"),
          (agent_get_position,pos1,":agent"),
          (position_set_z_to_ground_level, pos1),
          (agent_get_horse,":horse",":agent"),
          (try_begin),
            (gt,":horse",0),
            (position_move_z,pos1,300),
          (else_try),
            (position_move_z,pos1,225),
          (try_end),
          (agent_get_team, ":team", ":agent"),
          (try_begin),
            (eq,":team",0),
            (particle_system_burst,"psys_team_0",pos1,30),
          (else_try),
            (eq,":team",1),
            (particle_system_burst,"psys_team_1",pos1,30),
          (else_try),
            (eq,":team",2),
            (particle_system_burst,"psys_team_2",pos1,30),
          (else_try),
            (eq,":team",3),
            (particle_system_burst,"psys_team_3",pos1,30),
          (try_end),
        (try_end),
      ]),

    (1, 4, ti_once, [(num_active_teams_le, 1)],
      [
       (try_begin),
         (neg|main_hero_fallen),
         (call_script, "script_play_victorious_sound"),
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
    ],
  ),

  # NE end arena
  (
    "arena_challenge_fight",mtf_arena_fight|mtf_commit_casualties,-1,
    "You enter a melee fight in the arena.",
    [
      (56, mtef_visitor_source|mtef_team_0, 0, aif_start_alarmed, 1, []),
      (58, mtef_visitor_source|mtef_team_2, 0, aif_start_alarmed, 1, []),
    ],
    [
      lav_situational_damage_modifiers,
      common_inventory_not_available,
      (ti_tab_pressed, 0, 0, [(display_message, "str_cannot_leave_now")], []),
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),

      (0, 0, ti_once, [],
       [
         (call_script, "script_music_set_situation_with_culture", mtf_sit_arena),
         ]),

		 
	#NOTE -- THIS IS A VESTIGIAL SCRIPT. FOR LORD DUELS, USE THE NEXT SCRIPT DOWN 	 
      (1, 4, ti_once, [
	  (this_or_next|main_hero_fallen),
		(num_active_teams_le,1)],
       [
           (try_begin),
             (main_hero_fallen),
			 (check_quest_active, "qst_duel_for_lady"),
			 (quest_slot_eq, "qst_duel_for_lady", slot_quest_target_troop, "$g_duel_troop"),
             (call_script, "script_fail_quest", "qst_duel_for_lady"),
           (else_try),
			 (check_quest_active, "qst_duel_for_lady"),
			 (quest_slot_eq, "qst_duel_for_lady", slot_quest_target_troop, "$g_duel_troop"),
             (call_script, "script_succeed_quest", "qst_duel_for_lady"),
		   (else_try),
             (main_hero_fallen),
			 (check_quest_active, "qst_duel_courtship_rival"),
			 (quest_slot_eq, "qst_duel_courtship_rival", slot_quest_target_troop, "$g_duel_troop"),
             (call_script, "script_fail_quest", "qst_duel_courtship_rival"),
           (else_try),
			 (check_quest_active, "qst_duel_courtship_rival"),
			 (quest_slot_eq, "qst_duel_courtship_rival", slot_quest_target_troop, "$g_duel_troop"),
             (call_script, "script_succeed_quest", "qst_duel_courtship_rival"),
		   (else_try),	 
             (main_hero_fallen),
			 (check_quest_active, "qst_duel_avenge_insult"),
			 (quest_slot_eq, "qst_duel_avenge_insult", slot_quest_target_troop, "$g_duel_troop"),
             (call_script, "script_fail_quest", "qst_duel_avenge_insult"),
           (else_try),
			 (check_quest_active, "qst_duel_avenge_insult"),
			 (quest_slot_eq, "qst_duel_avenge_insult", slot_quest_target_troop, "$g_duel_troop"),
             (call_script, "script_succeed_quest", "qst_duel_avenge_insult"),
		   (else_try),	 
             (main_hero_fallen),
			 (check_quest_active, "qst_denounce_lord"),
			 (quest_slot_eq, "qst_denounce_lord", slot_quest_target_troop, "$g_duel_troop"),
             (call_script, "script_fail_quest", "qst_denounce_lord"),
           (else_try),
			 (check_quest_active, "qst_denounce_lord"),
			 (quest_slot_eq, "qst_denounce_lord", slot_quest_target_troop, "$g_duel_troop"),
             (call_script, "script_succeed_quest", "qst_denounce_lord"),
		   (else_try),
			 (quest_get_slot, ":target_troop", "qst_denounce_lord", slot_quest_target_troop),
		     (str_store_troop_name, s4, ":target_troop"),
		   (try_end),
           (finish_mission),
           ]),
    ],
  ),

  (
    "duel_with_lord",mtf_arena_fight|mtf_commit_casualties,-1,
    "You enter a melee fight in the arena.",
    [    
	  (0, mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[itm.sword_medieval_a,itm.arena_tunic_blue]),
	  (16, mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm.sword_medieval_a,itm.arena_tunic_blue]),
    ],
    [
      lav_situational_damage_modifiers,
      common_inventory_not_available,
	  	  	# NE settings
	  shield_bash_trigger_1,
      shield_bash_trigger_2,
      shield_bash_trigger_3,
      shield_bash_trigger_4,
	# Ne end settings
      (ti_tab_pressed, 0, 0, [(display_message, "str_cannot_leave_now")], []),
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),

      (0, 0, ti_once, [],
       [
         (call_script, "script_music_set_situation_with_culture", mtf_sit_arena),
         ]),


      (1, 4, ti_once, [
	  (this_or_next|main_hero_fallen),
		(num_active_teams_le,1)],
       [
           (try_begin),
             (main_hero_fallen),
			 (check_quest_active, "qst_duel_for_lady"),
			 (quest_slot_eq, "qst_duel_for_lady", slot_quest_target_troop, "$g_duel_troop"),
             (call_script, "script_fail_quest", "qst_duel_for_lady"),
           (else_try),
			 (check_quest_active, "qst_duel_for_lady"),
			 (quest_slot_eq, "qst_duel_for_lady", slot_quest_target_troop, "$g_duel_troop"),
             (call_script, "script_succeed_quest", "qst_duel_for_lady"),
		   (else_try),
             (main_hero_fallen),
			 (check_quest_active, "qst_duel_courtship_rival"),
			 (quest_slot_eq, "qst_duel_courtship_rival", slot_quest_target_troop, "$g_duel_troop"),
             (call_script, "script_fail_quest", "qst_duel_courtship_rival"),
           (else_try),
			 (check_quest_active, "qst_duel_courtship_rival"),
			 (quest_slot_eq, "qst_duel_courtship_rival", slot_quest_target_troop, "$g_duel_troop"),
             (call_script, "script_succeed_quest", "qst_duel_courtship_rival"),
		   (else_try),	 
             (main_hero_fallen),
			 (check_quest_active, "qst_duel_avenge_insult"),
			 (quest_slot_eq, "qst_duel_avenge_insult", slot_quest_target_troop, "$g_duel_troop"),
             (call_script, "script_fail_quest", "qst_duel_avenge_insult"),
           (else_try),
			 (check_quest_active, "qst_duel_avenge_insult"),
			 (quest_slot_eq, "qst_duel_avenge_insult", slot_quest_target_troop, "$g_duel_troop"),
             (call_script, "script_succeed_quest", "qst_duel_avenge_insult"),
		   (else_try),	 
             (main_hero_fallen),
			 (check_quest_active, "qst_denounce_lord"),
			 (quest_slot_eq, "qst_denounce_lord", slot_quest_target_troop, "$g_duel_troop"),
             (call_script, "script_fail_quest", "qst_denounce_lord"),
           (else_try),
			 (check_quest_active, "qst_denounce_lord"),
			 (quest_slot_eq, "qst_denounce_lord", slot_quest_target_troop, "$g_duel_troop"),
             (call_script, "script_succeed_quest", "qst_denounce_lord"),
		   (else_try),
			 (quest_get_slot, ":target_troop", "qst_denounce_lord", slot_quest_target_troop),
		     (str_store_troop_name, s4, ":target_troop"),
		   (try_end),
           (finish_mission),
           ]),
    ],
  ),  
  
 
# NE quests
   
 # v585 Josef fight king start
  (
    "arena_challenge_king",mtf_arena_fight|mtf_commit_casualties,-1,
    "You enter a melee fight in the arena.",
    [
      (56, mtef_visitor_source|mtef_team_0, 0, aif_start_alarmed, 1, []),
      (58, mtef_visitor_source|mtef_team_2, 0, aif_start_alarmed, 1, []),
    ],
    [
      lav_situational_damage_modifiers,
      common_inventory_not_available,
	  
	 # NE settings
	  shield_bash_trigger_1,
      shield_bash_trigger_2,
      shield_bash_trigger_3,
      shield_bash_trigger_4,
	# Ne end settings
	
      (ti_tab_pressed, 0, 0, [(display_message, "@Cannot leave now.")], []),
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),

      (0, 0, ti_once, [],
       [
         (call_script, "script_music_set_situation_with_culture", mtf_sit_arena),
         ]),

      (1, 4, ti_once, [(this_or_next|main_hero_fallen),(num_active_teams_le,1)],
       [
           (try_begin),
             (main_hero_fallen),
             (call_script, "script_fail_quest", "qst_fight_king"),
			 (jump_to_menu,"mnu_king_duel_lost"),
           (else_try),
             (call_script, "script_succeed_quest", "qst_fight_king"),
			 (jump_to_menu,"mnu_king_duel_won"),
           (try_end),
		   (finish_mission),
           ]),
    ],
  ), 
 
 # end
  
  
  
   # NE kingdom
  
## Lord dueling here - Jinnai
  ("arena_lord_duel",mtf_arena_fight|mtf_commit_casualties,-1,
    "You face off against your opponent in single combat.",
    [
	  
      (0,mtef_visitor_source|mtef_team_0,af_override_horse|af_override_weapons, aif_start_alarmed, 1, [itm.shield_common_round_a,itm.sword_medieval_a]),
      (8,mtef_visitor_source|mtef_team_1,af_override_horse|af_override_weapons, aif_start_alarmed, 1, [itm.shield_common_round_a,itm.sword_medieval_a]),
	       
    ],
    [
      lav_situational_damage_modifiers,
      common_inventory_not_available,
	  	# NE settings
	  shield_bash_trigger_1,
      shield_bash_trigger_2,
      shield_bash_trigger_3,
      shield_bash_trigger_4,
	# Ne end settings
	
     (ti_tab_pressed, 0, 0, [],
     [(question_box,"@Acknowledge your opponent as the victor?"),
      ]),
    (ti_question_answered, 0, 0, [],
     [(store_trigger_param_1,":answer"),
      (eq,":answer",0),
      (assign,"$g_tournament_player_team_won",0),
      (finish_mission,0),
      ]),

      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),

      (0, 0, ti_once, [],
       [
         (play_sound, "snd_arena_ambiance", sf_looping),
         (call_script, "script_music_set_situation_with_culture", mtf_sit_arena),
		 		 
         ]),

      (1, 4, ti_once, [(this_or_next|main_hero_fallen),(num_active_teams_le,1)],
       [
           (try_begin),
             (main_hero_fallen),
             (assign,"$g_tournament_player_team_won",0),
           (else_try),
             (assign,"$g_tournament_player_team_won",1),
           (try_end),
           (finish_mission),
           ]),
    ],
  ),

 
 # NE kingdom end 

  (
    "wedding",0,-1,
    "Wedding",
    [
        (0,mtef_visitor_source,af_override_everything,0,1,[itm.tabard, itm.ankle_boots]),
        (1,mtef_visitor_source,af_override_everything,0,1,[itm.bride_dress, itm.bride_crown, itm.bride_shoes]),
        (2,mtef_visitor_source,af_castle_lord,0,1,[]),
        (3,mtef_visitor_source,af_override_everything,0,1,[itm.courtly_outfit, itm.blue_hose]),
        (4,mtef_visitor_source,af_castle_lord,0,1,[]),
        (5,mtef_visitor_source,af_castle_lord,0,1,[]),
        (6,mtef_visitor_source,af_castle_lord,0,1,[]),
        (7,mtef_visitor_source,af_castle_lord,0,1,[]),
        (8,mtef_visitor_source,af_castle_lord,0,1,[]),
        (9,mtef_visitor_source,af_castle_lord,0,1,[]),
        (10,mtef_visitor_source,af_castle_lord,0,1,[]),
        (11,mtef_visitor_source,af_castle_lord,0,1,[]),
        (12,mtef_visitor_source,af_castle_lord,0,1,[]),
        (13,mtef_visitor_source,af_castle_lord,0,1,[]),
        (14,mtef_visitor_source,af_castle_lord,0,1,[]),
        (15,mtef_visitor_source,af_castle_lord,0,1,[]),
        (16,mtef_visitor_source,af_castle_lord,0,1,[]),
        (17,mtef_visitor_source,af_castle_lord,0,1,[]),
        (18,mtef_visitor_source,af_castle_lord,0,1,[]),
        (19,mtef_visitor_source,af_castle_lord,0,1,[]),
        (20,mtef_visitor_source,af_castle_lord,0,1,[]),
        (21,mtef_visitor_source,af_castle_lord,0,1,[]),
        (22,mtef_visitor_source,af_castle_lord,0,1,[]),
        (23,mtef_visitor_source,af_castle_lord,0,1,[]),
        (24,mtef_visitor_source,af_castle_lord,0,1,[]),
        (25,mtef_visitor_source,af_castle_lord,0,1,[]),
        (26,mtef_visitor_source,af_castle_lord,0,1,[]),
        (27,mtef_visitor_source,af_castle_lord,0,1,[]),
        (28,mtef_visitor_source,af_castle_lord,0,1,[]),
        (29,mtef_visitor_source,af_castle_lord,0,1,[]),
        (30,mtef_visitor_source,af_castle_lord,0,1,[]),
        (31,mtef_visitor_source,af_castle_lord,0,1,[]),
     ],
    [
      lav_situational_damage_modifiers,
      (ti_tab_pressed, 0, 0, [],
       [
         (show_object_details_overlay, 1),
         (finish_mission,0),
        ]),
      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (show_object_details_overlay, 1),
        (finish_mission,0),
        ]),

      (ti_after_mission_start, 0, 0, [],
       [
        (assign, "$g_wedding_state", 0),
        (play_track, "track_wedding", 2),
        (show_object_details_overlay, 0),
         ]),

      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (agent_get_troop_id, ":troop_no", ":agent_no"),
         (troop_get_type, ":gender", ":troop_no"),
         (set_fixed_point_multiplier, 100),
         (try_begin),
           (eq, ":troop_no", "$g_wedding_bishop_troop"),
         (else_try),
           (eq, ":troop_no", "$g_wedding_bride_troop"),
           (agent_set_no_dynamics, ":agent_no", 1),
           (init_position, pos1),
           (position_set_z, pos1, -1000),
           (agent_set_position, ":agent_no", pos1),
         (else_try),
           (eq, ":troop_no", "$g_wedding_brides_dad_troop"),
           (agent_set_no_dynamics, ":agent_no", 1),
           (init_position, pos1),
           (position_set_z, pos1, -1000),
           (agent_set_position, ":agent_no", pos1),
         (else_try),
           (eq, ":troop_no", "$g_wedding_groom_troop"),
           (agent_set_no_dynamics, ":agent_no", 1),
           (init_position, pos1),
           (position_move_x, pos1, 175),
           (position_move_z, pos1, 10),
           (position_rotate_z, pos1, 180),
           (agent_set_position, ":agent_no", pos1),
           (agent_set_animation, ":agent_no", "anim_wedding_groom_wait"),
         (else_try),
           (try_begin),
             (eq, ":gender", 0), #male
             (store_random_in_range, ":random_no", 0, 3),
             (try_begin),
               (eq, ":random_no", 0),
               (agent_set_slot, ":agent_no", slot_agent_cur_animation, "anim_wedding_guest_notr"),
               (agent_set_animation, ":agent_no", "anim_wedding_guest_notr"),
             (else_try),
               (agent_set_slot, ":agent_no", slot_agent_cur_animation, "anim_wedding_guest"),
               (agent_set_animation, ":agent_no", "anim_wedding_guest"),
             (try_end),
           (else_try), #female
             (agent_set_slot, ":agent_no", slot_agent_cur_animation, "anim_wedding_guest_woman"),
             (agent_set_animation, ":agent_no", "anim_wedding_guest_woman"),
           (try_end),
           (store_random_in_range, ":progress", 0, 100),
           (agent_set_animation_progress, ":agent_no", ":progress"),
         (try_end),
         ]),

      (0, 0, 0,
       [
         (store_mission_timer_a, ":cur_time"),
         (set_fixed_point_multiplier, 100),
         (try_for_agents, ":agent_no"),
           (agent_get_troop_id, ":troop_no", ":agent_no"),
           (try_begin),
             (eq, ":troop_no", "$g_wedding_groom_troop"),
           (else_try),
             (eq, ":troop_no", "$g_wedding_bride_troop"),
           (else_try),
             (eq, ":troop_no", "$g_wedding_brides_dad_troop"),
           (else_try),
             (eq, ":troop_no", "$g_wedding_bishop_troop"),
           (else_try),
             (agent_get_slot, ":cur_animation", ":agent_no", slot_agent_cur_animation),
             (agent_set_animation, ":agent_no", ":cur_animation"),
           (try_end),
         (try_end),
         (try_begin),
           (eq, "$g_wedding_state", 0),
           (mission_cam_set_mode, 1, 0, 0),
           (init_position, pos1),
           (position_rotate_z, pos1, 180),
           (position_rotate_x, pos1, 5),
           (position_set_x, pos1, -500),
           (position_set_y, pos1, 1000),
           (position_set_z, pos1, 600),
           (mission_cam_set_position, pos1),
           (init_position, pos1),
           (position_rotate_z, pos1, 180),
           (position_rotate_x, pos1, -15),
           (position_set_x, pos1, -500),
           (position_set_y, pos1, 1000),
           (position_set_z, pos1, 600),
           (mission_cam_animate_to_position, pos1, 4000, 0),
           (val_add, "$g_wedding_state", 1),
         (else_try),
           (eq, "$g_wedding_state", 1),
           (ge, ":cur_time", 4),
           (init_position, pos1),
           (position_rotate_z, pos1, 90),
           (position_rotate_x, pos1, -10),
           (position_set_x, pos1, -580),
           (position_set_y, pos1, 700),
           (position_set_z, pos1, 200),
           (mission_cam_set_position, pos1),
           (init_position, pos1),
           (position_rotate_z, pos1, 150),
           (position_rotate_x, pos1, -10),
           (position_set_x, pos1, -580),
           (position_set_y, pos1, 100),
           (position_set_z, pos1, 200),
           (mission_cam_animate_to_position, pos1, 6000, 1),
           (val_add, "$g_wedding_state", 1),
         (else_try),
           (eq, "$g_wedding_state", 2),
           (ge, ":cur_time", 9),
           (mission_cam_animate_to_screen_color, 0xFF000000, 1000),
           (val_add, "$g_wedding_state", 1),
         (else_try),
           (eq, "$g_wedding_state", 3),
           (ge, ":cur_time", 10),
           (init_position, pos1),
           (position_move_x, pos1, 175),
           (position_move_z, pos1, 10),
           (position_rotate_z, pos1, 180),
           (try_for_agents, ":agent_no"),
             (agent_get_troop_id, ":agent_troop", ":agent_no"),
             (try_begin),
               (eq, ":agent_troop", "$g_wedding_bride_troop"),
               (agent_set_position, ":agent_no", pos1),
               (agent_set_animation, ":agent_no", "anim_wedding_bride_stairs"),
             (else_try),
               (eq, ":agent_troop", "$g_wedding_brides_dad_troop"),
               (agent_set_position, ":agent_no", pos1),
               (agent_set_animation, ":agent_no", "anim_wedding_dad_stairs"),
             (try_end),
           (try_end),
           (init_position, pos1),
           (position_rotate_z, pos1, -90),
           (position_set_x, pos1, 300),
           (position_set_y, pos1, 950),
           (position_set_z, pos1, 420),
           (mission_cam_set_position, pos1),
           (position_set_x, pos1, 175),
           (position_set_y, pos1, 950),
           (position_set_z, pos1, 320),
           (mission_cam_animate_to_position, pos1, 4000, 0),
           (mission_cam_animate_to_screen_color, 0x00000000, 500),
           (val_add, "$g_wedding_state", 1),
         (else_try),
           (eq, "$g_wedding_state", 4),
           (ge, ":cur_time", 14),
           (init_position, pos1),
           (position_rotate_z, pos1, -60),
           (position_rotate_x, pos1, 10),
           (position_set_x, pos1, -400),
           (position_set_y, pos1, 200),
           (position_set_z, pos1, 115),
           (mission_cam_set_position, pos1),
           (val_add, "$g_wedding_state", 1),
         (else_try),
           (eq, "$g_wedding_state", 5),
           (ge, ":cur_time", 20),
           (init_position, pos1),
           (position_move_x, pos1, 175),
           (position_move_z, pos1, 10),
           (position_rotate_z, pos1, 180),
           (try_for_agents, ":agent_no"),
             (agent_get_troop_id, ":agent_troop", ":agent_no"),
             (try_begin),
               (eq, ":agent_troop", "$g_wedding_bride_troop"),
               (agent_set_position, ":agent_no", pos1),
               (agent_set_animation, ":agent_no", "anim_wedding_bride_walk"),
             (else_try),
               (eq, ":agent_troop", "$g_wedding_brides_dad_troop"),
               (agent_set_position, ":agent_no", pos1),
               (agent_set_animation, ":agent_no", "anim_wedding_dad_walk"),
             (try_end),
           (try_end),
           (init_position, pos1),
           (position_rotate_z, pos1, -140),
           (position_rotate_x, pos1, -15),
           (position_set_x, pos1, -625),
           (position_set_y, pos1, -530),
           (position_set_z, pos1, 180),
           (mission_cam_set_position, pos1),
           (val_add, "$g_wedding_state", 1),
         (else_try),
           (eq, "$g_wedding_state", 6),
           (ge, ":cur_time", 22),
           (init_position, pos1),
           (position_rotate_z, pos1, 45),
           (position_rotate_x, pos1, -10),
           (position_set_x, pos1, -260),
           (position_set_y, pos1, 120),
           (position_set_z, pos1, 275),
           (mission_cam_set_position, pos1),
           (position_rotate_z, pos1, 10),
           (mission_cam_animate_to_position, pos1, 2000, 0),
           (val_add, "$g_wedding_state", 1),
         (else_try),
           (eq, "$g_wedding_state", 7),
           (ge, ":cur_time", 24),
           (init_position, pos1),
           (position_move_x, pos1, 175),
           (position_move_z, pos1, 10),
           (position_rotate_z, pos1, 180),
           (try_for_agents, ":agent_no"),
             (agent_get_troop_id, ":agent_troop", ":agent_no"),
             (try_begin),
               (eq, ":agent_troop", "$g_wedding_bride_troop"),
               (agent_set_position, ":agent_no", pos1),
               (agent_set_animation, ":agent_no", "anim_wedding_bride_last"),
             (else_try),
               (eq, ":agent_troop", "$g_wedding_brides_dad_troop"),
               (agent_set_position, ":agent_no", pos1),
               (agent_set_animation, ":agent_no", "anim_wedding_dad_last"),
             (else_try),
               (eq, ":agent_troop", "$g_wedding_groom_troop"),
               (agent_set_position, ":agent_no", pos1),
               (agent_set_animation, ":agent_no", "anim_wedding_groom_last"),
             (try_end),
           (try_end),
           (init_position, pos1),
           (position_rotate_z, pos1, -45),
           (position_rotate_x, pos1, -10),
           (position_set_x, pos1, -900),
           (position_set_y, pos1, -850),
           (position_set_z, pos1, 230),
           (mission_cam_set_position, pos1),
           (val_add, "$g_wedding_state", 1),
         (else_try),
           (eq, "$g_wedding_state", 8),
           (ge, ":cur_time", 31),
           (init_position, pos1),
           (position_set_x, pos1, -550),
           (position_set_y, pos1, -625),
           (position_set_z, pos1, 1500),
           (particle_system_burst, "psys_wedding_rose", pos1, 750),
           (val_add, "$g_wedding_state", 1),
         (else_try),
           (eq, "$g_wedding_state", 9),
           (ge, ":cur_time", 33),
           (init_position, pos1),
           (position_rotate_z, pos1, 180),
           (position_set_x, pos1, -536),
           (position_set_y, pos1, -415),
           (position_set_z, pos1, 135),
           (mission_cam_set_position, pos1),
           (position_rotate_z, pos1, -8),
           (position_set_z, pos1, 350),
           (position_rotate_x, pos1, 35),
           (mission_cam_animate_to_position_and_aperture, pos1, 10, 9000, 1),
           (val_add, "$g_wedding_state", 1),
         (else_try),
           (eq, "$g_wedding_state", 10),
           (ge, ":cur_time", 41),
           (mission_cam_set_screen_color, 0x00FFFFFF),
           (mission_cam_animate_to_screen_color, 0xFFFFFFFF, 3000),
           (val_add, "$g_wedding_state", 1),
         (else_try),
           (eq, "$g_wedding_state", 11),
           (ge, ":cur_time", 48),
           (show_object_details_overlay, 1),
           (finish_mission,0),
         (try_end),
         ], []),
    ],
  ),

  (
	"bandit_lair",mtf_battle_mode,charge,
    "Ambushing a bandit lair",
    [
      (0,mtef_team_0|mtef_use_exact_number,af_override_horse, aif_start_alarmed, 7,[]),
      (1,mtef_visitor_source|mtef_team_1,af_override_horse, aif_start_alarmed,20,[]),
      (2,mtef_visitor_source|mtef_team_1,af_override_horse, aif_start_alarmed,20,[]),
      (3,mtef_visitor_source|mtef_team_1,af_override_horse, aif_start_alarmed,20,[]),
      (4,mtef_visitor_source|mtef_team_1,af_override_horse, aif_start_alarmed,20,[]),
      (5,mtef_visitor_source|mtef_team_1,af_override_horse, aif_start_alarmed,20,[]),
      (6,mtef_visitor_source|mtef_team_1,af_override_horse, aif_start_alarmed,20,[]),
      (7,mtef_visitor_source|mtef_team_1,af_override_horse, aif_start_alarmed,20,[]),
      (8,mtef_visitor_source|mtef_team_1,af_override_horse, aif_start_alarmed,20,[]),
      (9,mtef_visitor_source|mtef_team_1,af_override_horse, aif_start_alarmed,20,[]),
      (10,mtef_visitor_source|mtef_team_1,af_override_horse, aif_start_alarmed,20,[]),
    ],
    [
      lav_situational_damage_modifiers,
      common_battle_init_banner,
    
      common_inventory_not_available,
      
      (ti_on_agent_spawn, 0, 0, [],
      [
        (store_trigger_param_1, ":agent_no"),
        
        (assign, "$relative_of_merchant_is_found", 0),
              
        (try_begin),
          (agent_is_human, ":agent_no"),
          (agent_is_alive, ":agent_no"),
          (agent_get_team, ":agent_team", ":agent_no"),
          (eq, ":agent_team", 1),

          (agent_get_position, pos4, ":agent_no"),
          (agent_set_scripted_destination, ":agent_no", pos4, 1),
        (try_end),  
        
        (try_begin),
          (agent_get_troop_id, ":troop_no", ":agent_no"),
          (is_between, ":troop_no", "trp_relative_of_merchant", "trp_relative_of_merchants_end"),
          (agent_set_team, ":agent_no", 7),
          (team_set_relation, 0, 7, 0),          
        (try_end),                
        ]),
        
	   (0, 0, 0, 
	   [	     
         (party_get_template_id, ":template", "$g_encountered_party"),
         (eq, ":template", "pt_looter_lair"),
         (check_quest_active, "qst_save_relative_of_merchant"),	   
         (eq, "$relative_of_merchant_is_found", 0),
	   ],
	   [
        (get_player_agent_no, ":player_agent"),
        (agent_get_position, pos0, ":player_agent"),

        (try_for_agents, ":agent_no"),
          (agent_get_troop_id, ":troop_no", ":agent_no"),
          (is_between, ":troop_no", "trp_relative_of_merchant", "trp_relative_of_merchants_end"),    
          (agent_set_scripted_destination, ":agent_no", pos0),
          (agent_get_position, pos1, ":agent_no"),
          (get_distance_between_positions, ":dist", pos0, pos1),
          (le, ":dist", 200),
          #(assign, "$g_talk_troop", "trp_relative_of_merchant"),
          (start_mission_conversation, "trp_relative_of_merchant"),
        (try_end),
	   ]),
        
      (ti_tab_pressed, 0, 0,
       [
        (display_message, "str_cannot_leave_now"),
       ], []),
     
      (1, 0, ti_once, [],
       [
        (assign, "$defender_reinforcement_stage", 0),
        (assign, "$bandits_spawned_extra", 0),
	   ]),
	   
	   (1, 0, 0, [],
	   [
        (try_for_agents, ":bandit_id"),
          (agent_is_alive, ":bandit_id"),          
          (agent_get_team, ":agent_team_1", ":bandit_id"),
          (eq, ":agent_team_1", 1),
          (agent_is_in_special_mode, ":bandit_id"),
          (agent_is_human, ":bandit_id"),
          
          (agent_get_position, pos0, ":bandit_id"),
          (try_for_agents, ":player_team_agent_id"),
            (agent_is_alive, ":player_team_agent_id"),
            (agent_get_team, ":agent_team_2", ":player_team_agent_id"),
            (eq, ":agent_team_2", 0),
            (agent_is_human, ":player_team_agent_id"),
                      
            (store_agent_hit_points, ":bandit_hit_points", ":bandit_id"),
            
            (assign, ":continue", 0),
            (try_begin),
              (lt, ":bandit_hit_points", 100),
                            
              (try_for_agents, ":bandit_2_id"),
                (agent_is_alive, ":bandit_2_id"),  
                (agent_get_team, ":bandit_2_team", ":bandit_2_id"),
                (eq, ":bandit_2_team", 1),
                (neq, ":bandit_id", ":bandit_2_id"),
                (agent_is_in_special_mode, ":bandit_2_id"),
                (agent_is_human, ":bandit_2_id"),
                
                (agent_get_position, pos1, ":bandit_id"),
                (agent_get_position, pos2, ":bandit_2_id"),                        
                (get_distance_between_positions, ":distance", pos1, pos2),
                (le, ":distance", 1000),

                (agent_clear_scripted_mode, ":bandit_2_id"),  
              (try_end),                             
              
              (assign, ":continue", 1),
            (else_try),  
              (agent_get_position, pos1, ":bandit_id"),
              (agent_get_position, pos2, ":player_team_agent_id"),                        
              (get_distance_between_positions, ":distance", pos1, pos2),                                                                        
              (le, ":distance", 4000),
              
              (try_for_agents, ":bandit_2_id"),
                (agent_is_alive, ":bandit_2_id"),  
                (agent_get_team, ":bandit_2_team", ":bandit_2_id"),
                (eq, ":bandit_2_team", 1),
                (neq, ":bandit_id", ":bandit_2_id"),
                (agent_is_in_special_mode, ":bandit_2_id"),
                (agent_is_human, ":bandit_2_id"),
                
                (agent_get_position, pos1, ":bandit_id"),
                (agent_get_position, pos2, ":bandit_2_id"),                        
                (get_distance_between_positions, ":distance", pos1, pos2),
                (le, ":distance", 1000),
                
                (agent_clear_scripted_mode, ":bandit_2_id"),  
              (try_end),                

              (assign, ":continue", 1),
            (try_end),  
            
            (eq, ":continue", 1),
            
            (agent_clear_scripted_mode, ":bandit_id"),            
          (try_end),
        (try_end),
	   ]),
	   
	   (30, 0, 0, 
	   [
	     (le, "$defender_reinforcement_stage", 1),
	   ],
	   [          
          (store_character_level, ":player_level", "trp_player"),                   
          (store_add, ":number_of_bandits_will_be_spawned_at_each_period", 5, ":player_level"),
          (val_div, ":number_of_bandits_will_be_spawned_at_each_period", 3),

          (lt, "$bandits_spawned_extra", ":number_of_bandits_will_be_spawned_at_each_period"),
          (val_add, "$bandits_spawned_extra", 1),                   

          (party_get_template_id, ":template", "$g_encountered_party"),
          (store_random_in_range, ":random_value", 0, 2),
          
          (try_begin),
            (eq, ":template", "pt_sea_raider_lair"),
            (eq, ":random_value", 0),
            (assign, ":bandit_troop", "trp_sea_raider"),
          (else_try),
            (eq, ":template", "pt_forest_bandit_lair"),
            (eq, ":random_value", 0),
            (assign, ":bandit_troop", "trp_forest_bandit"),
          (else_try),
            (eq, ":template", "pt_desert_bandit_lair"),
            (eq, ":random_value", 0),
            (assign, ":bandit_troop", "trp_desert_bandit"),
          (else_try),
            (eq, ":template", "pt_mountain_bandit_lair"),
            (eq, ":random_value", 0),
            (assign, ":bandit_troop", "trp_mountain_bandit"),
          (else_try),
            (eq, ":template", "pt_taiga_bandit_lair"),
            (eq, ":random_value", 0),
            (assign, ":bandit_troop", "trp_taiga_bandit"),
          (else_try),
            (eq, ":template", "pt_steppe_bandit_lair"),
            (eq, ":random_value", 0),
            (assign, ":bandit_troop", "trp_steppe_bandit"),
          (else_try),
            (this_or_next|eq, ":template", "pt_looter_lair"),
            (neq, ":random_value", 0),
            (assign, ":bandit_troop", "trp_looter"),
          (try_end),

          (store_current_scene, ":cur_scene"), 
          (modify_visitors_at_site, ":cur_scene"),
          (store_random_in_range, ":random_entry_point", 2, 11),
          (add_visitors_to_current_scene, ":random_entry_point", ":bandit_troop", 1),
       ]),	   	   

      (ti_on_agent_killed_or_wounded, 0, 0, [],
       [
        (store_trigger_param_1, ":dead_agent_no"),
        #(store_trigger_param_2, ":killer_agent_no"),
        (store_trigger_param_3, ":is_wounded"),

        (try_begin),
          (ge, ":dead_agent_no", 0),
          (agent_is_human, ":dead_agent_no"),
          (agent_get_troop_id, ":dead_agent_troop_id", ":dead_agent_no"),
          (str_store_troop_name, s6, ":dead_agent_troop_id"),
          (try_begin),
            (neg|agent_is_ally, ":dead_agent_no"),
            (party_add_members, "p_total_enemy_casualties", ":dead_agent_troop_id", 1), #addition_to_p_total_enemy_casualties            
            (try_begin),
              (eq, ":is_wounded", 1),
              (party_wound_members, "p_total_enemy_casualties", ":dead_agent_troop_id", 1), 
            (try_end),  
          (try_end),  
          
          (party_add_members, "p_temp_casualties", ":dead_agent_troop_id", 1), #addition_to_p_total_enemy_casualties            
          
          (eq, ":is_wounded", 1),
          (party_wound_members, "p_temp_casualties", ":dead_agent_troop_id", 1), 
        (try_end),
        
        (assign, ":number_of_enemies", 0),
        (try_for_agents, ":cur_agent"),
          (agent_is_non_player, ":cur_agent"),
          (agent_is_human, ":cur_agent"),
          (agent_is_alive, ":cur_agent"),
          (neg|agent_is_ally, ":cur_agent"),
          (val_add, ":number_of_enemies", 1),
        (try_end),
        
        (try_begin),
          (le, ":number_of_enemies", 2),
          (le, "$defender_reinforcement_stage", 1),
          (val_add, "$defender_reinforcement_stage", 1),

          (store_character_level, ":player_level", "trp_player"),                   
          (store_add, ":number_of_bandits_will_be_spawned_at_each_period", 5, ":player_level"),
          (val_div, ":number_of_bandits_will_be_spawned_at_each_period", 3),
          (try_begin),
            (ge, "$defender_reinforcement_stage", 2),
            (val_sub, ":number_of_bandits_will_be_spawned_at_each_period", "$bandits_spawned_extra"),
          (try_end),
          
          (party_get_template_id, ":template", "$g_encountered_party"),          
          (store_random_in_range, ":random_value", 0, 2),
          
          (try_begin),
            (eq, ":template", "pt_sea_raider_lair"),
            (eq, ":random_value", 0),
            (assign, ":bandit_troop", "trp_sea_raider"),
          (else_try),
            (eq, ":template", "pt_forest_bandit_lair"),
            (eq, ":random_value", 0),
            (assign, ":bandit_troop", "trp_forest_bandit"),
          (else_try),
            (eq, ":template", "pt_desert_bandit_lair"),
            (eq, ":random_value", 0),
            (assign, ":bandit_troop", "trp_desert_bandit"),
          (else_try),
            (eq, ":template", "pt_mountain_bandit_lair"),
            (eq, ":random_value", 0),
            (assign, ":bandit_troop", "trp_mountain_bandit"),
          (else_try),
            (eq, ":template", "pt_taiga_bandit_lair"),
            (eq, ":random_value", 0),
            (assign, ":bandit_troop", "trp_taiga_bandit"),
          (else_try),
            (eq, ":template", "pt_steppe_bandit_lair"),
            (eq, ":random_value", 0),
            (assign, ":bandit_troop", "trp_steppe_bandit"),
          (else_try),
            (this_or_next|eq, ":template", "pt_looter_lair"),
            (neq, ":random_value", 0),
            (assign, ":bandit_troop", "trp_looter"),
          (try_end),
                                                                       
          (store_current_scene, ":cur_scene"), 
          (modify_visitors_at_site, ":cur_scene"),
          (try_for_range, ":unused", 0, ":number_of_bandits_will_be_spawned_at_each_period"),            
            (store_random_in_range, ":random_entry_point", 2, 11),
            (add_visitors_to_current_scene, ":random_entry_point", ":bandit_troop", 1),
          (try_end),
        (try_end),

        #no need to adjust courage in bandit lair for now
        #(call_script, "script_apply_death_effect_on_courage_scores", ":dead_agent_no", ":killer_agent_no"),
       ]),

      (0, 0, ti_once, [],
       [
         (call_script, "script_music_set_situation_with_culture", mtf_sit_ambushed),
         (set_party_battle_mode),
        ]),

      (2, 0, ti_once, 
       [
         (neg|main_hero_fallen),
         (num_active_teams_le, 1),         
       ],
       [
         (party_get_template_id, ":template", "$g_encountered_party"),
         (try_begin),
           (eq, ":template", "pt_looter_lair"),
           (check_quest_active, "qst_save_relative_of_merchant"),

           (store_faction_of_party, ":starting_town_faction", "$g_starting_town"),
           
           (try_begin),
             (eq, ":starting_town_faction", "fac_kingdom_1"),
             (assign, ":troop_of_merchant", "trp_relative_of_merchant"),
           (else_try),  
             (eq, ":starting_town_faction", "fac_kingdom_2"),
             (assign, ":troop_of_merchant", "trp_relative_of_merchant"),
           (else_try),                   
             (eq, ":starting_town_faction", "fac_kingdom_3"),
             (assign, ":troop_of_merchant", "trp_relative_of_merchant"),
           (else_try),  
             (eq, ":starting_town_faction", "fac_kingdom_4"),
             (assign, ":troop_of_merchant", "trp_relative_of_merchant"),
           (else_try),  
             (eq, ":starting_town_faction", "fac_kingdom_5"),
             (assign, ":troop_of_merchant", "trp_relative_of_merchant"),
           (else_try),  
             (eq, ":starting_town_faction", "fac_kingdom_6"),
             (assign, ":troop_of_merchant", "trp_relative_of_merchant"),
           (try_end),
           
           (get_player_agent_no, ":player_agent"),
           (agent_get_position, pos0, ":player_agent"),
           (assign, ":minimum_distance", 100000),
           (try_for_range, ":entry_no", 1, 10),
             (entry_point_get_position, pos1, ":entry_no"),
             (get_distance_between_positions, ":dist", pos0, pos1),
             (le, ":dist", ":minimum_distance"),
             (ge, ":dist", 1000),
             (assign, ":nearest_entry_point", ":entry_no"),
             (assign, ":minimum_distance", ":dist"),
           (try_end),                     
                          
           (add_visitors_to_current_scene, ":nearest_entry_point", ":troop_of_merchant", 1, 0),                      
         (try_end),
       ]),

       common_battle_order_panel,
       common_battle_order_panel_tick,

       (1, 4, ti_once,
       [
         (assign, ":continue", 0),
       
         (party_get_template_id, ":template", "$g_encountered_party"),
         (try_begin),       
           (eq, ":template", "pt_looter_lair"),
           (check_quest_active, "qst_save_relative_of_merchant"),
           
           (this_or_next|main_hero_fallen),
           (eq, "$relative_of_merchant_is_found", 1),
           
           (assign, ":continue", 1),
         (else_try),
           (this_or_next|neq|eq, ":template", "pt_looter_lair"),
           (neg|check_quest_active, "qst_save_relative_of_merchant"),

           (store_mission_timer_a,":cur_time"),
           (ge, ":cur_time", 5),
           
           (this_or_next|main_hero_fallen),
           (num_active_teams_le, 1),
           
           (assign, ":continue", 1),
         (try_end),  
         
         (eq, ":continue", 1),
       ],
       [
         (try_begin),
           (main_hero_fallen),
         (else_try),
           (party_set_slot, "$g_encountered_party", slot_party_ai_substate, 2),
         (try_end),
         
         (finish_mission),
         ]),
      ]),
        
  (
	"alley_fight", mtf_battle_mode,charge,
    "Alley fight",
    [    
      (0,mtef_team_0|mtef_use_exact_number,af_override_horse,aif_start_alarmed,7,[]),
      (1,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,20,[]),
      (2,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,20,[]),
      (3,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,20,[]),
    ],    
    [
      lav_situational_damage_modifiers,
      common_battle_init_banner,
    
      common_inventory_not_available,
      
      (ti_on_agent_spawn, 0, 0, [],
      [              
        (store_trigger_param_1, ":agent_no"),
        (get_player_agent_no, ":player_agent"),
        (neq, ":agent_no", ":player_agent"),
        (assign, "$g_main_attacker_agent", ":agent_no"),
        (agent_ai_set_aggressiveness, ":agent_no", 199),
        
        (try_begin),
          (agent_get_troop_id, ":troop_no", ":agent_no"),
          (is_between, ":troop_no", "trp_swadian_merchant", "trp_startup_merchants_end"),
          (agent_set_team, ":agent_no", 7),          
          (team_set_relation, 0, 7, 0), 
        (try_end),                
      ]),
              
	   (0, 0, 0, 
	   [
	     (eq, "$talked_with_merchant", 0), 
	   ],
	   [
        (get_player_agent_no, ":player_agent"),
        (agent_get_position, pos0, ":player_agent"),

        (try_for_agents, ":agent_no"),
          (agent_get_troop_id, ":troop_no", ":agent_no"),
          (is_between, ":troop_no", "trp_swadian_merchant", "trp_startup_merchants_end"),
          (agent_set_scripted_destination, ":agent_no", pos0),
          (agent_get_position, pos1, ":agent_no"),
          (get_distance_between_positions, ":dist", pos0, pos1),
          (le, ":dist", 200),     
          (assign, "$talk_context", tc_back_alley),     
          (start_mission_conversation, ":troop_no"),
        (try_end),
	   ]),
     
      (1, 0, 0, [], 
      [      
        (get_player_agent_no, ":player_agent"),       
        (ge, "$g_main_attacker_agent", 0),
        (ge, ":player_agent", 0),
        (agent_is_active, "$g_main_attacker_agent"),
        (agent_is_active, ":player_agent"),
        (agent_get_position, pos0, ":player_agent"),
        (agent_get_position, pos1, "$g_main_attacker_agent"),
        (get_distance_between_positions, ":dist", pos0, pos1),
        (ge, ":dist", 5),
        (agent_set_scripted_destination, "$g_main_attacker_agent", pos0),
      ]),

      (ti_tab_pressed, 0, 0, [], 
      [
        (display_message, "str_cannot_leave_now"),
      ]),

      (0, 0, ti_once, [],
       [
         (call_script, "script_music_set_situation_with_culture", mtf_sit_ambushed),
         (set_party_battle_mode),
        ]),

      (0, 0, ti_once, 
       [
         (neg|main_hero_fallen),
         (num_active_teams_le, 1),
       ],
       [
         (store_faction_of_party, ":starting_town_faction", "$g_starting_town"),
           
         (try_begin),
           (eq, ":starting_town_faction", "fac_kingdom_1"),
           (assign, ":troop_of_merchant", "trp_swadian_merchant"),
         (else_try),  
           (eq, ":starting_town_faction", "fac_kingdom_2"),
           (assign, ":troop_of_merchant", "trp_vaegir_merchant"),
         (else_try),                   
           (eq, ":starting_town_faction", "fac_kingdom_3"),
           (assign, ":troop_of_merchant", "trp_khergit_merchant"),
         (else_try),  
           (eq, ":starting_town_faction", "fac_kingdom_4"),
           (assign, ":troop_of_merchant", "trp_nord_merchant"),
         (else_try),  
           (eq, ":starting_town_faction", "fac_kingdom_5"),
           (assign, ":troop_of_merchant", "trp_rhodok_merchant"),
         (else_try),  
           (eq, ":starting_town_faction", "fac_kingdom_6"),
           (assign, ":troop_of_merchant", "trp_sarranid_merchant"),
         (try_end),
                                     
         (add_visitors_to_current_scene, 3, ":troop_of_merchant", 1, 0),                      
       ]),
       
      (1, 0, ti_once,
       [        
         (eq, "$talked_with_merchant", 1),         
       ],
       [         
         (try_begin),
           (main_hero_fallen),
           (assign, "$g_killed_first_bandit", 0),
         (else_try),  
           (assign, "$g_killed_first_bandit", 1),
         (try_end),

         (finish_mission),
         (assign, "$g_main_attacker_agent", 0),
         (assign, "$talked_with_merchant", 1),  
         
         (assign, "$current_startup_quest_phase", 1),                  
                  
         (change_screen_return),
         (set_trigger_result, 1),
         
         (get_player_agent_no, ":player_agent"),
         (store_agent_hit_points, ":hit_points", ":player_agent"),
         
         (try_begin),
           (lt, ":hit_points", 90),
           (agent_set_hit_points, ":player_agent", 90),
         (try_end),  
       ]),

      (1, 3, ti_once,
       [        
         (main_hero_fallen),         
       ],
       [         
         (try_begin),
           (main_hero_fallen),
           (assign, "$g_killed_first_bandit", 0),
         (else_try),  
           (assign, "$g_killed_first_bandit", 1),
         (try_end),

         (finish_mission),
         (assign, "$g_main_attacker_agent", 0),
         (assign, "$talked_with_merchant", 1),  
         
         (assign, "$current_startup_quest_phase", 1),                  
                  
         (change_screen_return),
         (set_trigger_result, 1),    
         
         (get_player_agent_no, ":player_agent"),
         (store_agent_hit_points, ":hit_points", ":player_agent"),
         
         (try_begin),
           (lt, ":hit_points", 90),
           (agent_set_hit_points, ":player_agent", 90),
         (try_end),                
       ]),
     ]),
     
  (
    "meeting_merchant",0,-1,
    "Meeting with the merchant",
    [
      (0,mtef_team_0,af_override_horse,0,1,[]),
      (1,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
      (2,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
      (3,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
      (4,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
      (5,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
      (6,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
      (7,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
      (8,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
      (9,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
    ],
    [
      lav_situational_damage_modifiers,
      (ti_on_agent_spawn, 0, 0, [],
      [              
        (store_trigger_param_1, ":agent_no"),

        (try_begin),
          (agent_get_troop_id, ":troop_no", ":agent_no"),
          (is_between, ":troop_no", "trp_swadian_merchant", "trp_startup_merchants_end"),
          (agent_set_team, ":agent_no", 7),          
          (team_set_relation, 0, 7, 0), 
        (try_end),                
      ]),

      (1, 0, ti_once, [], 
      [
        (assign, "$dialog_with_merchant_ended", 0),
        (store_current_scene, ":cur_scene"),
        (scene_set_slot, ":cur_scene", slot_scene_visited, 1),
        (try_begin),
          (eq, "$sneaked_into_town", 1),
          (call_script, "script_music_set_situation_with_culture", mtf_sit_town_infiltrate),
        (else_try),
          (eq, "$talk_context", tc_tavern_talk),
          (call_script, "script_music_set_situation_with_culture", mtf_sit_tavern),
        (else_try),
          (call_script, "script_music_set_situation_with_culture", mtf_sit_town),
        (try_end),
      ]),
      
      (1, 0, 0, 
      [        
        (assign, ":continue", 0),
        (try_begin),
          (ge, "$dialog_with_merchant_ended", 6),
          (assign, ":continue", 1),
        (else_try),
          (ge, "$dialog_with_merchant_ended", 1),
		  (neg|conversation_screen_is_active),          

          (try_begin),
            (eq, "$dialog_with_merchant_ended", 1),
            (check_quest_active, "qst_collect_men"),
            (tutorial_box, "str_start_up_first_quest", "@Tutorial"),
          (try_end),  

          (val_add, "$dialog_with_merchant_ended", 1),
          (assign, ":continue", 0),
        (try_end),  
        
        (try_begin),
          (conversation_screen_is_active), 
          (tutorial_message, -1),
          (assign, ":continue", 0),
        (try_end),
        
        (eq, ":continue", 1),                        
      ],
      [
        (tutorial_message_set_size, 17, 17),
        (tutorial_message_set_position, 500, 650),
        (tutorial_message_set_center_justify, 0),
        (tutorial_message_set_background, 1),
        (tutorial_message, "str_press_tab_to_exit_from_town"),
      ]),
      	  	
      (ti_before_mission_start, 0, 0, [], 
      [      
        #(call_script, "script_change_banners_and_chest"),
	  ]),

      (ti_inventory_key_pressed, 0, 0, 
      [
        (set_trigger_result, 1),        
      ], []),           
            
      (ti_tab_pressed, 0, 0, 
      [ 
        (try_begin),          
          (gt, "$dialog_with_merchant_ended", 0),          

          (assign, ":max_dist", 0),
          (party_get_position, pos1, "$current_town"),
          (try_for_range, ":unused", 0, 10),
            (map_get_random_position_around_position, pos0, pos1, 2),
            (get_distance_between_positions, ":dist", pos0, pos1),
            (ge, ":dist", ":max_dist"),
            (assign, ":max_dist", ":dist"),
            (copy_position, pos2, pos0),
          (try_end),  
    
          (party_set_position, "p_main_party", pos2),          
                            
          (finish_mission),
          
          (assign, "$current_startup_quest_phase", 2),
          
          (tutorial_message, -1),
          
          (tutorial_message_set_background, 0),
          
          (change_screen_map),
          
          (try_begin),
            (check_quest_finished, "qst_save_town_from_bandits"),
            (assign, "$g_do_one_more_meeting_with_merchant", 1),
          # Disabled by Lav: there shouldn't be a horde of mercenary war bands when player is just starting.
          #(else_try),  
          #  #will do this at first spawning in the map          
          #  (set_spawn_radius, 50),
          #  (try_for_range, ":unused", 0, 20),
          #    (spawn_around_party, "p_main_party", "pt_looters"),
          #  (try_end),          
          (try_end),  

          (set_trigger_result, 1),
        (else_try),
          (display_message, "str_cannot_leave_now"),
        (try_end),
      ], []),
    ]),

  (
    "town_fight",0,-1,
    "Town Fight",
    [
      (0,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
      (1,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
      (2,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
      (3,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
      (4,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
      (5,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
      (6,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
      (7,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),          
      (8,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
      (9,mtef_visitor_source,af_override_horse,0,1,[]),
      (10,mtef_visitor_source,af_override_horse,0,1,[]),
      (11,mtef_visitor_source|mtef_team_1,af_override_horse,0,1,[]),
      (12,mtef_visitor_source|mtef_team_1,af_override_horse,0,1,[]),
      (13,mtef_visitor_source|mtef_team_1,af_override_horse,0,1,[]),
      (14,mtef_visitor_source,af_override_horse,0,1,[]),
      (15,mtef_visitor_source,af_override_horse,0,1,[]),
      (16,mtef_visitor_source,af_override_horse,0,1,[]),
      (17,mtef_visitor_source,af_override_horse,0,1,[]),
      (18,mtef_visitor_source,af_override_horse,0,1,[]),
      (19,mtef_visitor_source,af_override_horse,0,1,[]),
      (20,mtef_visitor_source,af_override_horse,0,1,[]),
      (21,mtef_visitor_source|mtef_team_1,af_override_horse,0,1,[]),
      (22,mtef_visitor_source|mtef_team_1,af_override_horse,0,1,[]),
	  (23,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]), #guard
      (24,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]), #guard
	  (25,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]), #guard
	  (26,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]), #guard
	  (27,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]), #guard
	  (28,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]), #guard
	  (29,mtef_visitor_source,af_override_horse,0,1,[]),
	  (30,mtef_visitor_source,af_override_horse,0,1,[]), 
	  (31,mtef_visitor_source,af_override_horse,0,1,[]), 
      (32,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]), #town walker point
	  (33,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]), #town walker point
	  (34,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]), #town walker point
	  (35,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]), #town walker point
	  (36,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]), #town walker point
	  (37,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]), #town walker point
	  (38,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]), #town walker point
	  (39,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]), #town walker point
      (40,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]), #in towns, can be used for guard reinforcements
	  (41,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]), #in towns, can be used for guard reinforcements
	  (42,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]), #in towns, can be used for guard reinforcements
	  (43,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]), #in towns, can be used for guard reinforcements
      (44,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	  (45,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	  (46,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	  (47,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
    ],
    [
      lav_situational_damage_modifiers,
      common_battle_init_banner,
    
      (ti_on_agent_spawn, 0, 0, [],
      [
        (store_trigger_param_1, ":agent_no"),
        
        (agent_set_team, ":agent_no", 0),
      ]),

      (ti_before_mission_start, 0, 0, [],
      [
        (mission_disable_talk),        
      
        (assign, "$g_main_attacker_agent", 0),
        (set_party_battle_mode),
        
        (assign, "$number_of_bandits_killed_by_player", 0),
        (assign, "$number_of_civilian_loses", 0),
        
        (set_fixed_point_multiplier, 100),
	  ]),
		 
      (1, 0, ti_once, 
      [
        (call_script, "script_init_town_walker_agents"),
      ], 
      []),
      
      (ti_on_agent_killed_or_wounded, 0, 0, [],
      [
        (store_trigger_param_1, ":dead_agent_no"),
        (store_trigger_param_2, ":killer_agent_no"),
        #(store_trigger_param_3, ":is_wounded"),
        
        (try_begin),
          (agent_get_team, ":dead_agent_team_no", ":dead_agent_no"),
          (eq, ":dead_agent_team_no", 1),

          (get_player_agent_no, ":player_agent"),
          (eq, ":player_agent", ":killer_agent_no"),
                
          (val_add, "$number_of_bandits_killed_by_player", 1),
        (else_try),
          (eq, ":dead_agent_team_no", 0),
          
          (val_add, "$number_of_civilian_loses", 1),
        (try_end),  
      ]),
            
      (1, 0, 0, 
      [
        (lt, "$merchant_sign_count", 8),
  	    (val_add, "$merchant_sign_count", 1),
  	    
  	    (try_begin),
  	      (eq, "$merchant_sign_count", 2),
          (get_player_agent_no, ":player_agent"),
  	      (try_for_agents, ":agent_no"),
  	        (agent_get_troop_id, ":agent_troop_id", ":agent_no"),
  	        (ge, ":agent_troop_id", "trp_swadian_merchant"),
  	        (lt, ":agent_troop_id", "trp_startup_merchants_end"),
  	        
  	        (assign, "$g_city_merchant_troop_id", ":agent_troop_id"),
  	        (assign, "$g_city_merchant_agent_id", ":agent_no"),
  	        
  	        (agent_get_position, pos0, ":player_agent"),
  	        (agent_get_position, pos1, ":agent_no"),
  	                    
  	        (assign, ":max_dif", -1000),
            (try_for_range, ":target_entry_point", 0, 64),
              #(neg|entry_point_is_auto_generated, ":target_entry_point"),
              (entry_point_get_position, pos6, ":target_entry_point"),
              (get_distance_between_positions, ":dist_to_player", pos0, pos6),
              (get_distance_between_positions, ":dist_to_merchant", pos1, pos6),
              (store_sub, ":dif", ":dist_to_merchant", ":dist_to_player"),
              (ge, ":dist_to_merchant", 15),
              (ge, ":dif", ":max_dif"),
              (copy_position, pos2, pos6),
              (assign, ":max_dif", ":dif"),
            (try_end),
  	      	    
    	    (agent_set_scripted_destination, ":agent_no", pos2, 0),
            (agent_set_speed_limit, ":agent_no", 10),
          (try_end),
        (else_try),
  	      (eq, "$merchant_sign_count", 5),
  	                 
          (get_player_agent_no, ":player_agent"),
	      (agent_get_position, pos0, ":player_agent"),

  	      (agent_set_scripted_destination, "$g_city_merchant_agent_id", pos0, 0),
          (agent_set_speed_limit, "$g_city_merchant_agent_id", 10),
        (else_try),
  	      (eq, "$merchant_sign_count", 7),
  	      
  	      (agent_clear_scripted_mode, "$g_city_merchant_agent_id"),
  	                 
  	      (assign, "$talk_context", tc_town_talk),
  	      (start_mission_conversation, "$g_city_merchant_troop_id"),  	        	      
  	    (try_end),  	      
  	  ], 
	  []),
	  
	  (1, 0, 0, [],
	  [	  
	    (ge, "$merchant_sign_count", 8),
	   
	    (get_player_agent_no, ":player_agent"),
	    	    
        (try_for_agents, ":agent_no"),
          (neq, ":agent_no", ":player_agent"),
          (agent_is_alive, ":agent_no"),
          (agent_get_team, ":agent_team", ":agent_no"),
          (eq, ":agent_team", 0),
          
          (agent_get_position, pos0, ":agent_no"),
        
          (assign, ":minimum_distance", 10000),  
          (try_for_agents, ":bandit_no"),
            (agent_is_alive, ":bandit_no"),
            (agent_get_team, ":bandit_team", ":bandit_no"),
            (eq, ":bandit_team", 1),
            
            (agent_get_position, pos1, ":bandit_no"),
  
            (get_distance_between_positions, ":dist", pos0, pos1),
            (le, ":dist", ":minimum_distance"),
            (assign, ":minimum_distance", ":dist"),
            (copy_position, pos2, pos1),
          (try_end),
         
          (assign, reg1, ":dist"),
          (try_begin),
            (le, ":minimum_distance", 500),
            (agent_clear_scripted_mode, ":agent_no"),
          (else_try),  
            (lt, ":minimum_distance", 10000),
            (agent_set_scripted_destination, ":agent_no", pos2, 0),
          (try_end),
        (try_end),                  	      
      ]),

      (3, 0, 0, 
      [
        (lt, "$merchant_sign_count", 8),
  	    (call_script, "script_tick_town_walkers")
  	  ], 
	  []),	  	  
	
      (2, 0, 0, 
      [
        (call_script, "script_center_ambiance_sounds")
      ], 
      []),
    
      (ti_before_mission_start, 0, 0, 
      [], 
      [
        (call_script, "script_change_banners_and_chest")
      ]),
        
      (1, 4, ti_once,
       [                  
         (this_or_next|main_hero_fallen),
         (num_active_teams_le, 1),
         
         (ge, "$merchant_sign_count", 8),
       ],
       [         
         (try_begin),
           (main_hero_fallen),
           (assign, "$g_killed_first_bandit", 0),
         (else_try),  
           (assign, "$g_killed_first_bandit", 1),
         (try_end),
         
         (assign, "$current_startup_quest_phase", 4),

         (mission_enable_talk),        

         (finish_mission),         
         
         (unlock_achievement, ACHIEVEMENT_GET_UP_STAND_UP),        
                  
         (change_screen_return),
         (set_trigger_result, 1),         
       ]),

      (ti_inventory_key_pressed, 0, 0,
      [
        (try_begin),
          (eq, "$g_mt_mode", tcm_default),
          (set_trigger_result,1),
        (else_try),
          (eq, "$g_mt_mode", tcm_disguised),
          (display_message,"str_cant_use_inventory_disguised"),
        (else_try),
          (display_message, "str_cant_use_inventory_now"),
        (try_end),
      ], []),
       
      (ti_tab_pressed, 0, 0,
      [
        (display_message, "str_cannot_leave_now"),
      ], []),
  ]),


# PLUGIN_MULTIPLAYER

]

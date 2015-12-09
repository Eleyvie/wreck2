from compiler import *
register_plugin()
from plugin_multiplayer_const import *


def_attrib = str_7 | agi_5 | int_4 | cha_4
def_attrib_multiplayer = str_14 | agi_14 | int_4 | cha_4


meshes = [
  ("mp_ui_host_maps_1", 0, "mp_ui_host_maps_a1", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_2", 0, "mp_ui_host_maps_a2", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_3", 0, "mp_ui_host_maps_c", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_4", 0, "mp_ui_host_maps_ruinedf", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_5", 0, "mp_ui_host_maps_a1", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_6", 0, "mp_ui_host_maps_a1", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_7", 0, "mp_ui_host_maps_fieldby", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_8", 0, "mp_ui_host_maps_castle2", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_9", 0, "mp_ui_host_maps_snovyv", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_10", 0, "mp_ui_host_maps_castle3", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_11", 0, "mp_ui_host_maps_c1", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_12", 0, "mp_ui_host_maps_c2", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_13", 0, "mp_ui_host_maps_c3", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_randomp", 0, "mp_ui_host_maps_randomp", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_randoms", 0, "mp_ui_host_maps_randoms", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_command_panel", 0, "mp_ui_command_panel", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_command_border_l", 0, "mp_ui_command_border_l", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_command_border_r", 0, "mp_ui_command_border_r", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_welcome_panel", 0, "mp_ui_welcome_panel", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("flag_project_sw", 0, "flag_project_sw", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_vg", 0, "flag_project_vg", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_kh", 0, "flag_project_kh", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_nd", 0, "flag_project_nd", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_rh", 0, "flag_project_rh", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_sr", 0, "flag_project_sr", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("flag_projects_end", 0, "0", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("flag_project_sw_miss", 0, "flag_project_sw_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_vg_miss", 0, "flag_project_vg_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_kh_miss", 0, "flag_project_kh_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_nd_miss", 0, "flag_project_nd_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_rh_miss", 0, "flag_project_rh_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_sr_miss", 0, "flag_project_sr_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("flag_project_misses_end", 0, "0", 0, 0, 0, 0, 0, 0, 1, 1, 1),
]


strings = [
#multiplayer scene names
  ("multi_scene_1", "Ruins"),
  ("multi_scene_2", "Village"),
  ("multi_scene_3", "Hailes Castle"), #Castle 1
  ("multi_scene_4", "Ruined Fort"),
  ("multi_scene_5", "Scene 5"), #not ready yet
  ("multi_scene_6", "Scene 6"), #not ready yet
  ("multi_scene_7", "Field by the River"),
  ("multi_scene_8", "Rudkhan Castle"), #Castle 2
  ("multi_scene_9", "Snowy Village"),
  ("multi_scene_10", "Turin Castle"), #Castle 3
  ("multi_scene_11", "Nord Town"),
  ("multi_scene_16", "Port Assault"),
  ("multi_scene_17", "Brunwud Castle"), #Castle 4
  ("multi_scene_18", "Battle on Ice"),
  ("multi_scene_19", "Mahdaar Castle"), #Castle 5
  ("multi_scene_20", "Jameyyed Castle"), #Castle 6
  ("multi_scene_21", "The Arena"),
  ("multi_scene_22", "Forest Hideout"),
  ("multi_scene_23", "Canyon"),
  ("multi_scene_24", "Desert Town"),
  ("multi_scene_12", "Random Plains (Medium)"),
  ("multi_scene_13", "Random Plains (Large)"),
  ("multi_scene_14", "Random Steppe (Medium)"),
  ("multi_scene_15", "Random Steppe (Large)"),
  ("multi_scene_end", "multi_scene_end"),

#multiplayer game type names
  ("multi_game_type_1", "Deathmatch"),
  ("multi_game_type_2", "Team Deathmatch"),
  ("multi_game_type_3", "Battle"),
  ("multi_game_type_4", "Fight and Destroy"),
  ("multi_game_type_5", "Capture the Flag"),
  ("multi_game_type_6", "Conquest"),
  ("multi_game_type_7", "Siege"),
  ("multi_game_type_8", "Duel"),
  ("multi_game_types_end", "multi_game_types_end"),

  ("poll_kick_player_s1_by_s0", "{s0} started a poll to kick player {s1}."),
  ("poll_ban_player_s1_by_s0", "{s0} started a poll to ban player {s1}."),
  ("poll_change_map_to_s1_by_s0", "{s0} started a poll to change map to {s1}."),
  ("poll_change_map_to_s1_and_factions_to_s2_and_s3_by_s0", "{s0} started a poll to change map to {s1} and factions to {s2} and {s3}."),
  ("poll_change_number_of_bots_to_reg0_and_reg1_by_s0", "{s0} started a poll to change bot counts to {reg0} and {reg1}."),

  ("poll_kick_player", "Poll to kick player {s0}: 1 = Accept, 2 = Decline"),
  ("poll_ban_player", "Poll to ban player {s0}: 1 = Accept, 2 = Decline"),
  ("poll_change_map", "Poll to change map to {s0}: 1 = Accept, 2 = Decline"),
  ("poll_change_map_with_faction", "Poll to change map to {s0} and factions to {s1} versus {s2}: 1 = Accept, 2 = Decline"),
  ("poll_change_number_of_bots", "Poll to change number of bots to {reg0} for {s0} and {reg1} for {s1}: 1 = Accept, 2 = Decline"),
  ("poll_time_left", "({reg0} seconds left)"),
  ("poll_result_yes", "The poll is accepted by the majority."),
  ("poll_result_no", "The poll is rejected by the majority."),

  ("total_item_cost_reg0", "Total cost: {reg0}"),

  ("server_name", "Server name:"),
  ("game_password", "Game password:"),
  ("map", "Map:"),
  ("game_type", "Game type:"),
  ("max_number_of_players", "Maximum number of players:"),
  ("number_of_bots_in_team_reg1", "Number of bots in team {reg1}:"), 
  ("team_reg1_faction", "Team {reg1} faction:"),
  ("enable_valve_anti_cheat", "Enable Valve Anti-cheat (Requires valid Steam account)"),
  ("allow_friendly_fire", "Allow ranged friendly fire"),
  ("allow_melee_friendly_fire", "Allow melee friendly fire"),
  ("friendly_fire_damage_self_ratio", "Friendly fire damage self (%):"),
  ("friendly_fire_damage_friend_ratio", "Friendly fire damage friend (%):"),
  ("spectator_camera", "Spectator camera:"),
  ("control_block_direction", "Control block direction:"),
  ("map_time_limit", "Map time limit (minutes):"),
  ("round_time_limit", "Round time limit (seconds):"),
  ("players_take_control_of_a_bot_after_death", "Switch to bot on death:"),
  ("team_points_limit", "Team point limit:"),
  ("point_gained_from_flags", "Team points gained for flags (%):"),
  ("point_gained_from_capturing_flag", "Points gained for capturing flags:"),
  ("respawn_period", "Respawn period (seconds):"),
  ("add_to_official_game_servers_list", "Add to official game servers list"),
  ("combat_speed", "Combat_speed:"),
  ("combat_speed_0", "Slowest"),
  ("combat_speed_1", "Slower"),
  ("combat_speed_2", "Medium"),
  ("combat_speed_3", "Faster"),
  ("combat_speed_4", "Fastest"),
  ("off", "Off"),
  ("on", "On"),
  ("defender_spawn_count_limit", "Defender spawn count:"),
  ("unlimited", "Unlimited"),
  ("automatic", "Automatic"),
  ("by_mouse_movement", "By mouse movement"),
  ("free", "Free"),
  ("stick_to_any_player", "Lock to any player"),
  ("stick_to_team_members", "Lock to team members"),
  ("stick_to_team_members_view", "Lock to team members' view"),
  ("make_factions_voteable", "Allow polls to change factions"),
  ("make_kick_voteable", "Allow polls to kick players"),
  ("make_ban_voteable", "Allow polls to ban players"),
  ("bots_upper_limit_for_votes", "Bot count limit for polls:"),
  ("make_maps_voteable", "Allow polls to change maps"),
  ("valid_vote_ratio", "Poll accept threshold (%):"),
  ("auto_team_balance_limit", "Auto team balance threshold (diff.):"),
  ("welcome_message", "Welcome message:"),
  ("initial_gold_multiplier", "Starting gold (%):"),
  ("battle_earnings_multiplier", "Combat gold bonus (%):"),
  ("round_earnings_multiplier", "Round gold bonus (%):"),
  ("allow_player_banners", "Allow individual banners"),
  ("force_default_armor", "Force minimum armor"),
  
  ("reg0", "{!}{reg0}"),
  ("s0_reg0", "{!}{s0} {reg0}"),
  ("s0_s1", "{!}{s0} {s1}"),
  ("reg0_dd_reg1reg2", "{!}{reg0}:{reg1}{reg2}"),
  ("s0_dd_reg0", "{!}{s0}: {reg0}"),
  ("respawning_in_reg0_seconds", "Respawning in {reg0} seconds..."),
  ("no_more_respawns_remained_this_round", "No lives left for this round"),
  ("reg0_respawns_remained", "({reg0} lives remaining)"),
  ("this_is_your_last_respawn", "(This is your last life)"),
  ("wait_next_round", "(Wait for the next round)"),

  ("yes_wo_dot", "Yes"),
  ("no_wo_dot", "No"),

  ("s1_returned_flag", "{s1} has returned their flag to their base!"),
  ("s1_auto_returned_flag", "{s1} flag automatically returned to their base!"),
  ("s1_captured_flag", "{s1} has captured the enemy flag!"),
  ("s1_taken_flag", "{s1} has taken the enemy flag!"),
  ("s1_neutralized_flag_reg0", "{s1} has neutralized flag {reg0}."),
  ("s1_captured_flag_reg0", "{s1} has captured flag {reg0}!"),
  ("s1_pulling_flag_reg0", "{s1} has started pulling flag {reg0}."),

  ("s1_destroyed_target_0", "{s1} destroyed target A!"),
  ("s1_destroyed_target_1", "{s1} destroyed target B!"),
  ("s1_destroyed_catapult", "{s1} destroyed the catapult!"),
  ("s1_destroyed_trebuchet", "{s1} destroyed the trebuchet!"),
  ("s1_destroyed_all_targets", "{s1} destroyed all targets!"),
  ("s1_saved_1_target", "{s1} saved one target."),
  ("s1_saved_2_targets", "{s1} saved all targets."),
  
  ("s1_defended_castle", "{s1} defended their castle!"),
  ("s1_captured_castle", "{s1} captured the castle!"),
  
  ("auto_team_balance_in_20_seconds", "Auto-balance will be done in 20 seconds."),
  ("auto_team_balance_next_round", "Auto-balance will be done next round."),
  ("auto_team_balance_done", "Teams have been auto-balanced."),
  ("s1_won_round", "{s1} has won the round!"),
  ("round_draw", "Time is up. Round draw."),
  ("round_draw_no_one_remained", "No one left. Round draw."),
  ("death_mode_started", "Hurry! Become master of the field!"),  

  ("reset_to_default", "Reset to Default"),
  ("done", "Done"),
  ("player_name", "Player Name"),
  ("kills", "Kills"),
  ("deaths", "Deaths"),
  ("ping", "Ping"),
  ("dead", "Dead"),
  ("reg0_dead", "{reg0} Dead"),
  ("bots_reg0_agents", "Bots ({reg0} agents)"),
  ("bot_1_agent", "Bot (1 agent)"),
  ("score", "Score"),
  ("score_reg0", "Score: {reg0}"),
  ("flags_reg0", "(Flags: {reg0})"),
  ("reg0_players", "({reg0} players)"),
  ("reg0_player", "({reg0} player)"),

  ("start_map", "Start Map"),

  ("choose_an_option", "Choose an option:"),
  ("choose_a_poll_type", "Choose a poll type:"),
  ("choose_faction", "Choose Faction"),
  ("choose_a_faction", "Choose a faction:"),
  ("choose_troop", "Choose Troop"),
  ("choose_a_troop", "Choose a troop class:"),
  ("choose_items", "Choose Equipment"),
  ("options", "Options"),
  ("redefine_keys", "Redefine Keys"),
  ("submit_a_poll", "Submit a Poll"),
  ("administrator_panel", "Administrator Panel"),
  ("kick_player", "Kick Player"),
  ("ban_player", "Ban Player"),
  ("mute_player", "Mute Player"),
  ("unmute_player", "Unmute Player"),
  ("quit", "Quit"),
  ("poll_for_changing_the_map", "Change the map"),
  ("poll_for_changing_the_map_and_factions", "Change the map and factions"),
  ("poll_for_changing_number_of_bots", "Change number of bots in teams"),
  ("poll_for_kicking_a_player", "Kick a player"),
  ("poll_for_banning_a_player", "Ban a player"),
  ("choose_a_player", "Choose a player:"),
  ("choose_a_map", "Choose a map:"),
  ("choose_a_faction_for_team_reg0", "Choose a faction for team {reg0}:"),
  ("choose_number_of_bots_for_team_reg0", "Choose number of bots for team {reg0}:"),
  ("spectator", "Spectator"),
  ("spectators", "Spectators"),
  #("score", "Score"),
  ("command", "Command:"),
  ("profile_banner_selection_text", "Choose a banner for your profile:"),
  ("use_default_banner", "Use Faction's Banner"),
]


def wp(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
#  n |= wp_archery(x + random.randrange(r))
#  n |= wp_crossbow(x + random.randrange(r))
#  n |= wp_throwing(x + random.randrange(r))
  n |= wp_one_handed(x)
  n |= wp_two_handed(x)
  n |= wp_polearm(x)
  n |= wp_archery(x)
  n |= wp_crossbow(x)
  n |= wp_throwing(x)
  return n

def wpe(m,a,c,t):
   n = 0
   n |= wp_one_handed(m)
   n |= wp_two_handed(m)
   n |= wp_polearm(m)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n

def wpex(o,w,p,a,c,t):
   n = 0
   n |= wp_one_handed(o)
   n |= wp_two_handed(w)
   n |= wp_polearm(p)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n

def wp_melee(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
  n |= wp_one_handed(x + 20)
  n |= wp_two_handed(x)
  n |= wp_polearm(x + 10)
  return n

swadian_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
swadian_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
swadian_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
swadian_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
swadian_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

swadian_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

vaegir_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
vaegir_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
vaegir_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
vaegir_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
vaegir_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

vaegir_face_younger_2 = 0x000000003f00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_young_2   = 0x00000003bf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_middle_2  = 0x00000007bf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_old_2     = 0x0000000cbf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_older_2   = 0x0000000ff100230c4deeffffffffffff00000000001efff90000000000000000

khergit_face_younger_1 = 0x0000000009003109207000000000000000000000001c80470000000000000000
khergit_face_young_1   = 0x00000003c9003109207000000000000000000000001c80470000000000000000
khergit_face_middle_1  = 0x00000007c9003109207000000000000000000000001c80470000000000000000
khergit_face_old_1     = 0x0000000b89003109207000000000000000000000001c80470000000000000000
khergit_face_older_1   = 0x0000000fc9003109207000000000000000000000001c80470000000000000000

khergit_face_younger_2 = 0x000000003f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_young_2   = 0x00000003bf0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_middle_2  = 0x000000077f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_old_2     = 0x0000000b3f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_older_2   = 0x0000000fff0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000

nord_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
nord_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
nord_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
nord_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
nord_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

nord_face_younger_2 = 0x00000000310023084deeffffffffffff00000000001efff90000000000000000
nord_face_young_2   = 0x00000003b10023084deeffffffffffff00000000001efff90000000000000000
nord_face_middle_2  = 0x00000008310023084deeffffffffffff00000000001efff90000000000000000
nord_face_old_2     = 0x0000000c710023084deeffffffffffff00000000001efff90000000000000000
nord_face_older_2   = 0x0000000ff10023084deeffffffffffff00000000001efff90000000000000000

rhodok_face_younger_1 = 0x0000000009002003140000000000000000000000001c80400000000000000000
rhodok_face_young_1   = 0x0000000449002003140000000000000000000000001c80400000000000000000
rhodok_face_middle_1  = 0x0000000849002003140000000000000000000000001c80400000000000000000
rhodok_face_old_1     = 0x0000000cc9002003140000000000000000000000001c80400000000000000000
rhodok_face_older_1   = 0x0000000fc9002003140000000000000000000000001c80400000000000000000

rhodok_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

sarranid_face_younger_1 = 0x000000018a0075c519244a730360e1e100000000001ca71c0000000000000000
sarranid_face_young_1   = 0x000000015c08338a34b3896d8c8ac62200000000001e5b590000000000000000
sarranid_face_middle_1 = 0x00000000040c6593130da5c8d332343400000000001e58f40000000000000000
sarranid_face_old_1 = 0x0000000f0a00700019244a630360e1e100000000001ca71c0000000000000000
sarranid_face_older_1   = 0x0000000f040c6553130da5c8d332343400000000001e58cc0000000000000000

sarranid_face_younger_2 = 0x000000017a00224469a6854a9c6d3d5400000000001f36e50000000000000000
sarranid_face_young_2   = 0x000000016b0c72d156d9b2631162d2d100000000001d386c0000000000000000
sarranid_face_middle_2  = 0x00000007570075013a5d71371389ba8d00000000001c39140000000000000000
sarranid_face_old_2   = 0x0000000f0a00601419244a630360e1e100000000001ca71c0000000000000000
sarranid_face_older_2   = 0x0000000fd70075013a5d71371389ba8d00000000001c39140000000000000000

troops = [
  ["multiplayer_data", "{!}multiplayer_data", "{!}multiplayer_data", tf_hero|tf_inactive, 0, 0, fac.neutral, [], def_attrib, 0, SKILLS(riding=1,trade=2,inventory_management=2,prisoner_management=1,leadership=1), 0],

  #Multiplayer ai troops

  ["swadian_crossbowman_multiplayer_ai", "Swadian Crossbowman", "Swadian Crossbowmen", tf_guarantee_all, 0, 0, fac.kingdom_1, [], level(19)|def_attrib, wp_melee(90)|wp_crossbow(100), SKILLS(riding=1,trade=2,inventory_management=2,prisoner_management=1,leadership=1,ironflesh=4,athletics=6,shield=5,power_strike=3), swadian_face_young_1, swadian_face_old_2],
  ["swadian_infantry_multiplayer_ai", "Swadian Infantry", "Swadian Infantry", tf_guarantee_all_wo_ranged, 0, 0, fac.kingdom_1, [], level(19)|def_attrib, wp_melee(105), SKILLS(riding=1,trade=2,inventory_management=2,prisoner_management=1,leadership=1,ironflesh=5,shield=4,power_strike=5,athletics=4), swadian_face_middle_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer_ai", "Swadian Man at Arms", "Swadian Men at Arms", tf_mounted|tf_guarantee_all_wo_ranged, 0, 0, fac.kingdom_1, [], level(19)|def_attrib, wp_melee(100), SKILLS(trade=2,inventory_management=2,prisoner_management=1,leadership=1,riding=5,ironflesh=4,shield=4,power_strike=4,athletics=1), swadian_face_young_1, swadian_face_old_2],
  ["vaegir_archer_multiplayer_ai", "Vaegir Archer", "Vaegir Archers", tf_guarantee_all, 0, 0, fac.kingdom_2, [], level(19)|def_attrib|str_12, wp_melee(70), SKILLS(ironflesh=4,power_draw=5,athletics=6,shield=2), vaegir_face_young_1, vaegir_face_older_2 ],
  ["vaegir_spearman_multiplayer_ai", "Vaegir Spearman", "Vaegir Spearmen", tf_guarantee_all_wo_ranged, 0, 0, fac.kingdom_2, [], level(19)|def_attrib|str_12, wp_melee(90), SKILLS(ironflesh=4,athletics=6,power_throw=3,power_strike=3,shield=2), vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_horseman_multiplayer_ai", "Vaegir Horseman", "Vaegir Horsemen", tf_mounted|tf_guarantee_all_wo_ranged, 0, 0, fac.kingdom_2, [], level(19)|def_attrib, wp(100), SKILLS(riding=4,ironflesh=4,power_strike=4,shield=3), vaegir_face_young_1, vaegir_face_older_2],
  ["khergit_dismounted_lancer_multiplayer_ai", "Khergit Dismounted Lancer", "Khergit Dismounted Lancer", tf_guarantee_all_wo_ranged, 0, 0, fac.kingdom_3, [], level(23)|def_attrib, wp(150), SKILLS(riding=7,power_strike=5,power_draw=4,power_throw=2,ironflesh=5,horse_archery=1), khergit_face_middle_1, khergit_face_older_2],
  ["khergit_veteran_horse_archer_multiplayer_ai", "Khergit Horse Archer", "Khergit Horse Archers", tf_mounted|tf_guarantee_all, 0, 0, fac.kingdom_3, [], level(21)|def_attrib, wp(90)|wp_archery(150), SKILLS(riding=6,power_draw=5,shield=2,horse_archery=5), khergit_face_middle_1, khergit_face_older_2],
  ["khergit_lancer_multiplayer_ai", "Khergit Lancer", "Khergit Lancers", tf_guarantee_all_wo_ranged, 0, 0, fac.kingdom_3, [], level(23)|def_attrib, wp(130), SKILLS(riding=7,power_strike=5,power_draw=4,power_throw=2,ironflesh=5,horse_archery=1), khergit_face_middle_1, khergit_face_older_2],
  ["nord_veteran_multiplayer_ai", "Nord Footman", "Nord Footmen", tf_guarantee_all_wo_ranged, 0, 0, fac.kingdom_4, [], level(19)|def_attrib, wp(130), SKILLS(ironflesh=3,power_strike=5,power_throw=3,athletics=5,shield=3), nord_face_young_1, nord_face_older_2],
  ["nord_scout_multiplayer_ai", "Nord Scout", "Nord Scouts", tf_mounted|tf_guarantee_all, 0, 0, fac.kingdom_4, [], level(19)|def_attrib, wp(100), SKILLS(riding=5,ironflesh=2,power_strike=2,shield=1,horse_archery=2,power_throw=3), nord_face_young_1, nord_face_older_2],
  ["nord_archer_multiplayer_ai", "Nord Archer", "Nord Archers", tf_guarantee_all, 0, 0, fac.kingdom_4, [], level(19)|def_attrib|str_11, wp_melee(80)|wp_archery(110), SKILLS(ironflesh=4,power_strike=2,shield=1,power_draw=5,athletics=6), nord_face_young_1, nord_face_old_2],
  ["rhodok_veteran_crossbowman_multiplayer_ai", "Rhodok Crossbowman", "Rhodok Crossbowmen", tf_guarantee_all, 0, 0, fac.kingdom_5, [], level(19)|def_attrib, wp_melee(100)|wp_crossbow(120), SKILLS(riding=1,trade=2,inventory_management=2,prisoner_management=1,leadership=1,ironflesh=4,shield=5,power_strike=3,athletics=6), rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_veteran_spearman_multiplayer_ai", "Rhodok Spearman", "Rhodok Spearmen", tf_guarantee_all_wo_ranged, 0, 0, fac.kingdom_5, [], level(19)|def_attrib, wp(115), SKILLS(riding=1,trade=2,inventory_management=2,prisoner_management=1,leadership=1,ironflesh=5,shield=3,power_strike=4,athletics=3), rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_scout_multiplayer_ai", "Rhodok Scout", "Rhodok Scouts", tf_mounted|tf_guarantee_all, 0, 0, fac.kingdom_5, [], level(19)|def_attrib, wp(100), SKILLS(riding=5,ironflesh=2,power_strike=2,shield=1,horse_archery=2,power_throw=3), rhodok_face_young_1, rhodok_face_older_2],
  ["sarranid_infantry_multiplayer_ai", "Sarranid Infantry", "Sarranid Infantries", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, 0, 0, fac.kingdom_6, [], level(20)|def_attrib, wp_melee(105), SKILLS(trade=2,inventory_management=2,prisoner_management=1,leadership=1,riding=3,ironflesh=2,shield=3), swadian_face_middle_1, swadian_face_old_2],
  ["sarranid_archer_multiplayer_ai", "Sarranid Archer", "Sarranid Archers", tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.kingdom_6, [], level(19)|def_attrib, wp_melee(90)|wp_archery(100), SKILLS(trade=2,inventory_management=2,prisoner_management=1,leadership=1,riding=3,ironflesh=1), swadian_face_young_1, swadian_face_old_2],
  ["sarranid_horseman_multiplayer_ai", "Sarranid Horseman", "Sarranid Horsemen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield, 0, 0, fac.kingdom_6, [], level(20)|def_attrib, wp_melee(100), SKILLS(trade=2,inventory_management=2,prisoner_management=1,leadership=1,riding=5,ironflesh=2,shield=2,power_strike=3), swadian_face_young_1, swadian_face_old_2],

  #Multiplayer troops (they must have the base items only, nothing else)
  ["swadian_crossbowman_multiplayer", "Swadian Crossbowman", "Swadian Crossbowmen", tf_guarantee_all, 0, 0, fac.kingdom_1, [], level(19)|def_attrib_multiplayer, wpe(90, 60, 180, 90), SKILLS(trade=2,inventory_management=2,prisoner_management=1,leadership=1,ironflesh=2,athletics=5,shield=5,power_strike=2,riding=1), swadian_face_young_1, swadian_face_old_2],
  ["swadian_infantry_multiplayer", "Swadian Infantry", "Swadian Infantry", tf_guarantee_all, 0, 0, fac.kingdom_1, [], level(20)|def_attrib_multiplayer, wpex(105, 130, 110, 40, 60, 110), SKILLS(trade=2,inventory_management=2,prisoner_management=1,leadership=1,ironflesh=5,shield=4,power_strike=4,power_throw=2,athletics=6,riding=1), swadian_face_middle_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer", "Swadian Man at Arms", "Swadian Men at Arms", tf_mounted|tf_guarantee_all, 0, 0, fac.kingdom_1, [], level(20)|def_attrib_multiplayer, wp_melee(110), SKILLS(trade=2,inventory_management=2,prisoner_management=1,leadership=1,riding=5,ironflesh=3,shield=2,power_throw=2,power_strike=3,athletics=3), swadian_face_young_1, swadian_face_old_2],
  ["vaegir_archer_multiplayer", "Vaegir Archer", "Vaegir Archers", tf_guarantee_all, 0, 0, fac.kingdom_2, [], level(19)|def_attrib_multiplayer|str_12, wpe(80, 150, 60, 80), SKILLS(ironflesh=2,power_draw=6,athletics=4,shield=2,riding=1), vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_spearman_multiplayer", "Vaegir Spearman", "Vaegir spearman", tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield, 0, 0, fac.kingdom_2, [], level(19)|def_attrib_multiplayer|str_12, wpex(110, 100, 130, 30, 50, 120), SKILLS(ironflesh=4,shield=2,power_throw=3,power_strike=3,athletics=6,riding=1), vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_horseman_multiplayer", "Vaegir Horseman", "Vaegir Horsemen", tf_mounted|tf_guarantee_all, 0, 0, fac.kingdom_2, [], level(19)|def_attrib_multiplayer, wpe(110, 90, 60, 110), SKILLS(riding=5,ironflesh=3,power_strike=2,shield=3,power_throw=2), vaegir_face_young_1, vaegir_face_older_2],
  ["khergit_veteran_horse_archer_multiplayer", "Khergit Horse Archer", "Khergit Horse Archers", tf_mounted|tf_guarantee_all, 0, 0, fac.kingdom_3, [], level(21)|def_attrib_multiplayer, wpe(80, 150, 60, 100), SKILLS(riding=6,power_draw=5,shield=2,horse_archery=5,athletics=3), khergit_face_middle_1, khergit_face_older_2],
  ["khergit_lancer_multiplayer", "Khergit Lancer", "Khergit Lancers", tf_mounted|tf_guarantee_all, 0, 0, fac.kingdom_3, [], level(21)|def_attrib_multiplayer, wp(115), SKILLS(riding=6,ironflesh=3,power_throw=3,shield=2,horse_archery=1,power_strike=2,athletics=5), khergit_face_middle_1, khergit_face_older_2],
  ["nord_archer_multiplayer", "Nord Archer", "Nord Archers", tf_guarantee_all, 0, 0, fac.kingdom_4, [], level(15)|def_attrib_multiplayer|str_11, wpe(90, 150, 60, 80), SKILLS(ironflesh=2,power_strike=2,shield=2,power_draw=5,athletics=4,riding=1), nord_face_young_1, nord_face_old_2],
  ["nord_veteran_multiplayer", "Nord Huscarl", "Nord Huscarls", tf_guarantee_all, 0, 0, fac.kingdom_4, [], level(24)|def_attrib_multiplayer, wpex(110, 135, 100, 40, 60, 140), SKILLS(ironflesh=4,power_strike=5,power_throw=4,athletics=6,shield=3,riding=1), nord_face_young_1, nord_face_older_2],
  ["nord_scout_multiplayer", "Nord Scout", "Nord Scouts", tf_mounted|tf_guarantee_all, 0, 0, fac.kingdom_4, [], level(19)|def_attrib_multiplayer, wp(105), SKILLS(riding=6,ironflesh=2,power_strike=2,shield=1,horse_archery=2,power_throw=3,athletics=3), vaegir_face_young_1, vaegir_face_older_2],
  ["rhodok_veteran_crossbowman_multiplayer", "Rhodok Crossbowman", "Rhodok Crossbowmen", tf_guarantee_all, 0, 0, fac.kingdom_5, [], level(20)|def_attrib_multiplayer, wpe(100, 60, 180, 90), SKILLS(riding=1,trade=2,inventory_management=2,prisoner_management=1,leadership=1,ironflesh=2,shield=2,power_strike=2,athletics=5), rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_sergeant_multiplayer", "Rhodok Sergeant", "Rhodok Sergeants", tf_guarantee_all, 0, 0, fac.kingdom_5, [], level(20)|def_attrib_multiplayer, wpex(110, 100, 140, 30, 50, 110), SKILLS(riding=1,trade=2,inventory_management=2,prisoner_management=1,leadership=1,ironflesh=4,shield=5,power_strike=4,power_throw=1,athletics=6), rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_horseman_multiplayer", "Rhodok Horseman", "Rhodok Horsemen", tf_guarantee_all, 0, 0, fac.kingdom_5, [], level(20)|def_attrib_multiplayer, wp(100), SKILLS(riding=4,ironflesh=3,shield=2,power_strike=2,power_throw=1,athletics=3), rhodok_face_middle_1, rhodok_face_older_2],
  ["sarranid_archer_multiplayer", "Sarranid Archer", "Sarranid Archers", tf_guarantee_all, 0, 0, fac.kingdom_6, [], level(19)|def_attrib_multiplayer|str_12, wpe(80, 150, 60, 80), SKILLS(ironflesh=2,power_draw=5,athletics=5,shield=2,riding=1), vaegir_face_young_1, vaegir_face_older_2],
  ["sarranid_footman_multiplayer", "Sarranid Footman", "Sarranid footman", tf_guarantee_all, 0, 0, fac.kingdom_6, [], level(19)|def_attrib_multiplayer|str_12, wpex(110, 100, 130, 30, 50, 120), SKILLS(ironflesh=4,shield=2,power_throw=3,power_strike=3,athletics=6,riding=1), vaegir_face_young_1, vaegir_face_older_2],
  ["sarranid_mamluke_multiplayer", "Sarranid Mamluke", "Sarranid Mamluke", tf_mounted|tf_guarantee_all, 0, 0, fac.kingdom_6, [], level(19)|def_attrib_multiplayer, wpe(110, 90, 60, 110), SKILLS(riding=5,ironflesh=3,power_strike=2,shield=3,power_throw=2), vaegir_face_young_1, vaegir_face_older_2],

  ["multiplayer_end", "{!}multiplayer_end", "{!}multiplayer_end", 0, 0, 0, fac.kingdom_5, [], 0, 0, 0, 0, 0],
]


scenes = [
  ("multi_scene_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b", [],[],"outer_terrain_plain"),
  ("multi_scene_2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000012002a0b20004992700006e54000007fe00001fd2", [],[],"outer_terrain_steppe"),
  ("multi_scene_3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002e0b20005154500006e540000235600007b55", [],[],"outer_terrain_plain"),
  ("multi_scene_4",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300659630003c8f300003ca000006a8900003c89", [],[],"outer_terrain_plain"),
  ("multi_scene_5",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002a1ba0004210900003ca000006a8900007a7b", [],[],"outer_terrain_plain"),
  ("multi_scene_6",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300494b200048524000059e80000453300001d32", [],[],"outer_terrain_plain"),
  ("multi_scene_7",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130010e0e0005fd84000011c60000285b00005cbe", [],[],"outer_terrain_plain"),
  ("multi_scene_8",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000020004db18004611400005c918000397b00004c2e", [],[],"outer_terrain_plain"),
  ("multi_scene_9",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000400032320003c0f300001f9e000011180000031c", [],[],"outer_terrain_snow"),
  ("multi_scene_10",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003009cde1000599630000423b00005756000000af", [],[],"outer_terrain_plain"),
  ("multi_scene_11",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030015f2b000350d4000011a4000017ee000054af", [],[],"outer_terrain_plain"),
  ("multi_scene_12",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013003d7e30005053f00003b4e0000146300006e84", [],[],"outer_terrain_beach"),
  ("multi_scene_13",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b", [],[],"outer_terrain_plain"),
  ("multi_scene_14",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000040000c910003e8fa0000538900003e9e00005301", [],[],"outer_terrain_snow"),
  ("multi_scene_15",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000500b1d158005394c00001230800072880000018f", [],[],"outer_terrain_desert"),       
  ("multi_scene_16",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000d007abd20002c8b1000050c50000752a0000788c", [],[],"outer_terrain_desert"),
  ("multi_scene_17",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200005000005f57b00005885000046bd00006d9c", [],[],"outer_terrain_plain"),
  ("multi_scene_18",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0x00000000b00037630002308c00000c9400005d4c00000f3a", [],[],"outer_terrain_plain"),
  ("multi_scene_19",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b", [],[],"outer_terrain_plain"),
  ("multi_scene_20",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002ab630004651800000d7a00007f3100002701", [],[],"outer_terrain_plain"),
  
  ("random_multi_plain_medium",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000001394018dd000649920004406900002920000056d7", [],[], "outer_terrain_plain"),
  ("random_multi_plain_large",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000013a001853000aa6a40004406900002920001e4f81", [],[], "outer_terrain_plain"),
  ("random_multi_steppe_medium", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0,0),(100, 100), -0.5, "0x0000000128601ae300063d8f0004406900002920001e4f81", [],[], "outer_terrain_steppe"),
  ("random_multi_steppe_large", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0,0),(100, 100), -0.5, "0x000000012a00d8630009fe7f0004406900002920001e4f81", [],[], "outer_terrain_steppe"),

  ("multiplayer_maps_end",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b", [],[],"outer_terrain_plain"),
]

from plugin_multiplayer_script import *
from plugin_multiplayer_prsnt import *
from plugin_multiplayer_mt import *

injection = {
	'script_game_quick_start': [
        #for multiplayer mode
        (assign, "$g_multiplayer_selected_map", multiplayer_scenes_begin),
        (assign, "$g_multiplayer_respawn_period", 5),
        (assign, "$g_multiplayer_round_max_seconds", 300),
        (assign, "$g_multiplayer_game_max_minutes", 30),
        (assign, "$g_multiplayer_game_max_points", 300),

        (server_get_renaming_server_allowed, "$g_multiplayer_renaming_server_allowed"),
        (server_get_changing_game_type_allowed, "$g_multiplayer_changing_game_type_allowed"),
        (assign, "$g_multiplayer_point_gained_from_flags", 100),
        (assign, "$g_multiplayer_point_gained_from_capturing_flag", 5),
        (assign, "$g_multiplayer_game_type", 0),
        (assign, "$g_multiplayer_team_1_faction", "fac_kingdom_1"),
        (assign, "$g_multiplayer_team_2_faction", "fac_kingdom_2"),
        (assign, "$g_multiplayer_next_team_1_faction", "$g_multiplayer_team_1_faction"),
        (assign, "$g_multiplayer_next_team_2_faction", "$g_multiplayer_team_2_faction"),
        (assign, "$g_multiplayer_num_bots_team_1", 0),
        (assign, "$g_multiplayer_num_bots_team_2", 0),
        (assign, "$g_multiplayer_number_of_respawn_count", 0),
        (assign, "$g_multiplayer_num_bots_voteable", 50),
        (assign, "$g_multiplayer_max_num_bots", 101),
        (assign, "$g_multiplayer_factions_voteable", 1),
        (assign, "$g_multiplayer_maps_voteable", 1),
        (assign, "$g_multiplayer_kick_voteable", 1),
        (assign, "$g_multiplayer_ban_voteable", 1),
        (assign, "$g_multiplayer_valid_vote_ratio", 51), #more than 50 percent
        (assign, "$g_multiplayer_auto_team_balance_limit", 3), #auto balance when difference is more than 2
        (assign, "$g_multiplayer_player_respawn_as_bot", 1),
        (assign, "$g_multiplayer_stats_chart_opened_manually", 0),
        (assign, "$g_multiplayer_mission_end_screen", 0),
        (assign, "$g_multiplayer_ready_for_spawning_agent", 1),
        (assign, "$g_multiplayer_welcome_message_shown", 0),
        (assign, "$g_multiplayer_allow_player_banners", 1),
        (assign, "$g_multiplayer_force_default_armor", 1),
        (assign, "$g_multiplayer_disallow_ranged_weapons", 0),

        (assign, "$g_multiplayer_initial_gold_multiplier", 100),
        (assign, "$g_multiplayer_battle_earnings_multiplier", 100),
        (assign, "$g_multiplayer_round_earnings_multiplier", 100),

        (try_for_range, ":cur_item", all_items_begin, all_items_end),
          (try_for_range, ":cur_faction", npc_kingdoms_begin, npc_kingdoms_end),
            (store_sub, ":faction_index", ":cur_faction", npc_kingdoms_begin),
            (val_add, ":faction_index", slot_item_multiplayer_faction_price_multipliers_begin),
            (item_set_slot, ":cur_item", ":faction_index", 100), #100 is the default price multiplier
          (try_end),
        (try_end),
        (store_sub, ":swadian_price_slot", "fac_kingdom_1", npc_kingdoms_begin),
        (val_add, ":swadian_price_slot", slot_item_multiplayer_faction_price_multipliers_begin),
        (store_sub, ":vaegir_price_slot", "fac_kingdom_2", npc_kingdoms_begin),
        (val_add, ":vaegir_price_slot", slot_item_multiplayer_faction_price_multipliers_begin),
        (store_sub, ":khergit_price_slot", "fac_kingdom_3", npc_kingdoms_begin),
        (val_add, ":khergit_price_slot", slot_item_multiplayer_faction_price_multipliers_begin),
        (store_sub, ":nord_price_slot", "fac_kingdom_4", npc_kingdoms_begin),
        (val_add, ":nord_price_slot", slot_item_multiplayer_faction_price_multipliers_begin),
        (store_sub, ":rhodok_price_slot", "fac_kingdom_5", npc_kingdoms_begin),
        (val_add, ":rhodok_price_slot", slot_item_multiplayer_faction_price_multipliers_begin),
        (store_sub, ":sarranid_price_slot", "fac_kingdom_6", npc_kingdoms_begin),
        (val_add, ":sarranid_price_slot", slot_item_multiplayer_faction_price_multipliers_begin),

#      (item_set_slot, "itm_steppe_horse", ":khergit_price_slot", 50),

#      #arrows
#      (item_set_slot, "itm_arrows", slot_item_multiplayer_item_class, multi_item_class_type_arrow),
#      (item_set_slot, "itm_barbed_arrows", slot_item_multiplayer_item_class, multi_item_class_type_arrow),
#      (item_set_slot, "itm_bodkin_arrows", slot_item_multiplayer_item_class, multi_item_class_type_arrow),
#      (item_set_slot, "itm_khergit_arrows", slot_item_multiplayer_item_class, multi_item_class_type_arrow),
#      #bolts
#      (item_set_slot, "itm_bolts", slot_item_multiplayer_item_class, multi_item_class_type_bolt),
#      (item_set_slot, "itm_steel_bolts", slot_item_multiplayer_item_class, multi_item_class_type_bolt),
#      #bows
#      (item_set_slot, "itm_crossbow", slot_item_multiplayer_item_class, multi_item_class_type_bow),
#      (item_set_slot, "itm_heavy_crossbow", slot_item_multiplayer_item_class, multi_item_class_type_bow),
#      (item_set_slot, "itm_sniper_crossbow", slot_item_multiplayer_item_class, multi_item_class_type_bow),
#      (item_set_slot, "itm_nomad_bow", slot_item_multiplayer_item_class, multi_item_class_type_bow),
#      (item_set_slot, "itm_khergit_bow", slot_item_multiplayer_item_class, multi_item_class_type_bow),
#      (item_set_slot, "itm_strong_bow", slot_item_multiplayer_item_class, multi_item_class_type_bow),
#      (item_set_slot, "itm_war_bow", slot_item_multiplayer_item_class, multi_item_class_type_bow),
#      (item_set_slot, "itm_short_bow", slot_item_multiplayer_item_class, multi_item_class_type_bow),
#      (item_set_slot, "itm_long_bow", slot_item_multiplayer_item_class, multi_item_class_type_bow),
#      (item_set_slot, "itm_light_crossbow", slot_item_multiplayer_item_class, multi_item_class_type_bow),
#      #swords
#      (item_set_slot, "itm_sword_medieval_a", slot_item_multiplayer_item_class, multi_item_class_type_sword),
#      (item_set_slot, "itm_sword_medieval_b", slot_item_multiplayer_item_class, multi_item_class_type_sword),
#      (item_set_slot, "itm_sword_medieval_b_small", slot_item_multiplayer_item_class, multi_item_class_type_sword),
#      (item_set_slot, "itm_sword_medieval_c", slot_item_multiplayer_item_class, multi_item_class_type_sword),
#      (item_set_slot, "itm_sword_medieval_c_small", slot_item_multiplayer_item_class, multi_item_class_type_sword),
#      (item_set_slot, "itm_scimitar_a", slot_item_multiplayer_item_class, multi_item_class_type_sword),
#      (item_set_slot, "itm_scimitar_b", slot_item_multiplayer_item_class, multi_item_class_type_sword),
#      (item_set_slot, "itm_dagger", slot_item_multiplayer_item_class, multi_item_class_type_sword),
#      (item_set_slot, "itm_sword_khergit_1", slot_item_multiplayer_item_class, multi_item_class_type_sword),
#      (item_set_slot, "itm_sword_khergit_2", slot_item_multiplayer_item_class, multi_item_class_type_sword),
#      (item_set_slot, "itm_sword_khergit_3", slot_item_multiplayer_item_class, multi_item_class_type_sword),
#      (item_set_slot, "itm_sword_khergit_4", slot_item_multiplayer_item_class, multi_item_class_type_sword),
#      (item_set_slot, "itm_sword_viking_1", slot_item_multiplayer_item_class, multi_item_class_type_sword),
#      (item_set_slot, "itm_sword_viking_2", slot_item_multiplayer_item_class, multi_item_class_type_sword),
#      (item_set_slot, "itm_sword_viking_2_small", slot_item_multiplayer_item_class, multi_item_class_type_sword),
#      (item_set_slot, "itm_sword_viking_3", slot_item_multiplayer_item_class, multi_item_class_type_sword),
#      (item_set_slot, "itm_sword_viking_3_small", slot_item_multiplayer_item_class, multi_item_class_type_sword),
#      (item_set_slot, "itm_bastard_sword_a", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_sword),
#      (item_set_slot, "itm_bastard_sword_b", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_sword),
#      (item_set_slot, "itm_sword_two_handed_a", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_sword),
#      (item_set_slot, "itm_sword_two_handed_b", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_sword),
#      (item_set_slot, "itm_arabian_sword_a", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_sword),
#      (item_set_slot, "itm_arabian_sword_b", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_sword),
#      (item_set_slot, "itm_sarranid_cavalry_sword", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_sword),
#      (item_set_slot, "itm_arabian_sword_d", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_sword),
#
#      #axe
#      (item_set_slot, "itm_axe", slot_item_multiplayer_item_class, multi_item_class_type_axe),
#      (item_set_slot, "itm_battle_axe", slot_item_multiplayer_item_class, multi_item_class_type_axe),
#      (item_set_slot, "itm_one_handed_war_axe_a", slot_item_multiplayer_item_class, multi_item_class_type_axe),
#      (item_set_slot, "itm_one_handed_war_axe_b", slot_item_multiplayer_item_class, multi_item_class_type_axe),
#      (item_set_slot, "itm_one_handed_battle_axe_a", slot_item_multiplayer_item_class, multi_item_class_type_axe),
#      (item_set_slot, "itm_one_handed_battle_axe_b", slot_item_multiplayer_item_class, multi_item_class_type_axe),
#      (item_set_slot, "itm_one_handed_battle_axe_c", slot_item_multiplayer_item_class, multi_item_class_type_axe),
#
#      (item_set_slot, "itm_two_handed_axe", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
#      (item_set_slot, "itm_two_handed_battle_axe_2", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
#      (item_set_slot, "itm_shortened_voulge", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
#      (item_set_slot, "itm_bardiche", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
#      (item_set_slot, "itm_great_axe_new", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
#      (item_set_slot, "itm_great_bardiche", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
#      (item_set_slot, "itm_long_axe", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
#      (item_set_slot, "itm_long_axe_b", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
#      (item_set_slot, "itm_long_axe_c", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
#      (item_set_slot, "itm_voulge", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
#      (item_set_slot, "itm_long_bardiche", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
#      (item_set_slot, "itm_great_long_bardiche", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
#
#      #blunt
#      (item_set_slot, "itm_mace_1", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
#      (item_set_slot, "itm_mace_2", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
#      (item_set_slot, "itm_mace_3", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
#      (item_set_slot, "itm_mace_4", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
#      (item_set_slot, "itm_long_spiked_club", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
#      (item_set_slot, "itm_long_hafted_spiked_mace", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
#
#      (item_set_slot, "itm_maul", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
#      (item_set_slot, "itm_sledgehammer", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
#      (item_set_slot, "itm_warhammer", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
#      (item_set_slot, "itm_morningstar", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
#      #picks
#      (item_set_slot, "itm_military_sickle_a", slot_item_multiplayer_item_class, multi_item_class_type_war_picks),
#      (item_set_slot, "itm_fighting_pick", slot_item_multiplayer_item_class, multi_item_class_type_war_picks),
#      (item_set_slot, "itm_military_pick", slot_item_multiplayer_item_class, multi_item_class_type_war_picks),
#      (item_set_slot, "itm_club_with_spike_head", slot_item_multiplayer_item_class, multi_item_class_type_war_picks),
#
#      #Cleavers
#      (item_set_slot, "itm_military_cleaver_b", slot_item_multiplayer_item_class, multi_item_class_type_cleavers),
#      (item_set_slot, "itm_military_cleaver_c", slot_item_multiplayer_item_class, multi_item_class_type_cleavers),
#      (item_set_slot, "itm_two_handed_cleaver", slot_item_multiplayer_item_class, multi_item_class_type_cleavers),
#      (item_set_slot, "itm_hafted_blade_a", slot_item_multiplayer_item_class, multi_item_class_type_cleavers),
#      (item_set_slot, "itm_hafted_blade_b", slot_item_multiplayer_item_class, multi_item_class_type_cleavers),
#      (item_set_slot, "itm_shortened_military_scythe", slot_item_multiplayer_item_class, multi_item_class_type_cleavers),
#
#      (item_set_slot, "itm_sarranid_mace_1", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
#      (item_set_slot, "itm_sarranid_axe_a", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
#      (item_set_slot, "itm_sarranid_axe_b", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
#      (item_set_slot, "itm_sarranid_two_handed_axe_a", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
#      (item_set_slot, "itm_sarranid_two_handed_axe_b", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
#      (item_set_slot, "itm_sarranid_two_handed_mace_1", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
#      (item_set_slot, "itm_bamboo_spear", slot_item_multiplayer_item_class, multi_item_class_type_spear),
#
#
#
#      #spears
#      (item_set_slot, "itm_double_sided_lance", slot_item_multiplayer_item_class, multi_item_class_type_spear),
#      (item_set_slot, "itm_glaive", slot_item_multiplayer_item_class, multi_item_class_type_spear),
#      (item_set_slot, "itm_poleaxe", slot_item_multiplayer_item_class, multi_item_class_type_spear),
#      (item_set_slot, "itm_polehammer", slot_item_multiplayer_item_class, multi_item_class_type_spear),
#      (item_set_slot, "itm_staff", slot_item_multiplayer_item_class, multi_item_class_type_spear),
#      (item_set_slot, "itm_quarter_staff", slot_item_multiplayer_item_class, multi_item_class_type_spear),
#      (item_set_slot, "itm_iron_staff", slot_item_multiplayer_item_class, multi_item_class_type_spear),
#
#      (item_set_slot, "itm_shortened_spear", slot_item_multiplayer_item_class, multi_item_class_type_spear),
#      (item_set_slot, "itm_spear", slot_item_multiplayer_item_class, multi_item_class_type_spear),
#      (item_set_slot, "itm_war_spear", slot_item_multiplayer_item_class, multi_item_class_type_spear),
#      (item_set_slot, "itm_military_scythe", slot_item_multiplayer_item_class, multi_item_class_type_spear),
#      (item_set_slot, "itm_pike", slot_item_multiplayer_item_class, multi_item_class_type_spear),
#      (item_set_slot, "itm_ashwood_pike", slot_item_multiplayer_item_class, multi_item_class_type_spear),
#      (item_set_slot, "itm_awlpike", slot_item_multiplayer_item_class, multi_item_class_type_spear),
#      (item_set_slot, "itm_awlpike_long", slot_item_multiplayer_item_class, multi_item_class_type_spear),
#      #lance
#      (item_set_slot, "itm_light_lance", slot_item_multiplayer_item_class, multi_item_class_type_lance),
#      (item_set_slot, "itm_lance", slot_item_multiplayer_item_class, multi_item_class_type_lance),
#      (item_set_slot, "itm_heavy_lance", slot_item_multiplayer_item_class, multi_item_class_type_lance),
#      (item_set_slot, "itm_great_lance", slot_item_multiplayer_item_class, multi_item_class_type_lance),
#      #shields
#
#      #(item_set_slot, "itm_tab_shield_round_a", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
#      #(item_set_slot, "itm_tab_shield_round_b", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
#      #(item_set_slot, "itm_tab_shield_round_c", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
#      #(item_set_slot, "itm_tab_shield_round_d", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
#      #(item_set_slot, "itm_tab_shield_round_e", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
#      #(item_set_slot, "itm_tab_shield_kite_a", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
#      #(item_set_slot, "itm_tab_shield_kite_b", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
#      #(item_set_slot, "itm_tab_shield_kite_c", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
#      #(item_set_slot, "itm_tab_shield_kite_d", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
#      #(item_set_slot, "itm_tab_shield_kite_cav_a", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
#      #(item_set_slot, "itm_tab_shield_kite_cav_b", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
#      #(item_set_slot, "itm_tab_shield_heater_a", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
#      #(item_set_slot, "itm_tab_shield_heater_b", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
#      #(item_set_slot, "itm_tab_shield_heater_c", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
#      #(item_set_slot, "itm_tab_shield_heater_d", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
#      #(item_set_slot, "itm_tab_shield_heater_cav_a", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
#      #(item_set_slot, "itm_tab_shield_heater_cav_b", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
#      #(item_set_slot, "itm_tab_shield_pavise_a", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
#      #(item_set_slot, "itm_tab_shield_pavise_b", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
#      #(item_set_slot, "itm_tab_shield_pavise_c", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
#      #(item_set_slot, "itm_tab_shield_pavise_d", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
#      #(item_set_slot, "itm_tab_shield_small_round_a", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
#      #(item_set_slot, "itm_tab_shield_small_round_b", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
#      #(item_set_slot, "itm_tab_shield_small_round_c", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
#      (item_set_slot, "itm_spear", slot_item_multiplayer_item_class, multi_item_class_type_spear),
#      #throwing
#      (item_set_slot, "itm_darts", slot_item_multiplayer_item_class, multi_item_class_type_throwing),
#      (item_set_slot, "itm_war_darts", slot_item_multiplayer_item_class, multi_item_class_type_throwing),
#      (item_set_slot, "itm_javelin", slot_item_multiplayer_item_class, multi_item_class_type_throwing),
#      (item_set_slot, "itm_jarid", slot_item_multiplayer_item_class, multi_item_class_type_throwing),
#      (item_set_slot, "itm_throwing_spears", slot_item_multiplayer_item_class, multi_item_class_type_throwing),
#
#      (item_set_slot, "itm_throwing_axes", slot_item_multiplayer_item_class, multi_item_class_type_throwing_axe),
#      (item_set_slot, "itm_light_throwing_axes", slot_item_multiplayer_item_class, multi_item_class_type_throwing_axe),
#      (item_set_slot, "itm_heavy_throwing_axes", slot_item_multiplayer_item_class, multi_item_class_type_throwing_axe),
#       #armors
#      (item_set_slot, "itm_red_shirt", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_red_tunic", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_aketon_green", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_padded_cloth", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_red_gambeson", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_leather_armor", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_haubergeon", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_coat_of_plates_red", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_brigandine_red", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_mail_with_surcoat", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_linen_tunic", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_leather_vest", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_leather_jerkin", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_studded_leather_coat", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_lamellar_vest", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_lamellar_armor", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_coarse_tunic", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_tribal_warrior_outfit", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_tarkhan_lamellar", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_blue_tunic", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_mail_hauberk", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_mail_shirt", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_byrnie", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_lamellar_vest_khergit", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_steppe_armor", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#
#
#      (item_set_slot, "itm_banded_armor", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_cuir_bouilli", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_scale_armor", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#
#      (item_set_slot, "itm_padded_leather", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_green_tunic", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_tunic_with_green_cape", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_aketon_green", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_ragged_outfit", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_surcoat_over_mail", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#
#      (item_set_slot, "itm_sarranid_elite_armor", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_skirmisher_armor", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_archers_vest", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_sarranid_leather_armor", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_sarranid_cloth_robe", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_sarranid_mail_shirt", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_sarranid_cavalry_robe", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_khergit_mail_plate_a", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_mamluke_mail", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_khergit_elite_armor", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_vaegir_elite_armor", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#      (item_set_slot, "itm_khergit_armor", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
#
#
#
#
#
#      #boots
#      (item_set_slot, "itm_hide_boots", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
#      (item_set_slot, "itm_ankle_boots", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
#      (item_set_slot, "itm_nomad_boots", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
#      (item_set_slot, "itm_leather_boots", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
#      (item_set_slot, "itm_splinted_leather_greaves", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
#      (item_set_slot, "itm_mail_chausses", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
#      (item_set_slot, "itm_splinted_leather_greaves", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
#      (item_set_slot, "itm_splinted_greaves", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
#      (item_set_slot, "itm_mail_boots", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
#      (item_set_slot, "itm_iron_greaves", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
#      (item_set_slot, "itm_sarranid_boots_b", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
#      (item_set_slot, "itm_sarranid_boots_c", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
#      (item_set_slot, "itm_sarranid_boots_d", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
#      (item_set_slot, "itm_plate_boots", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
#      (item_set_slot, "itm_khergit_leather_boots", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
#      (item_set_slot, "itm_tarkhan_boots", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
#
#
#
#
#
#
#
#
#      #helmets
#
#
#      (item_set_slot, "itm_leather_steppe_cap_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_leather_steppe_cap_b", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_steppe_cap", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_khergit_war_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_tarkhan_helm", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#
#
#
#      (item_set_slot, "itm_arming_cap", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_padded_coif", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_mail_coif", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_footman_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_norman_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_kettle_hat", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_helmet_with_neckguard", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#
#      (item_set_slot, "itm_bascinet_2", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_bascinet_3", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#
#
#
#      (item_set_slot, "itm_flat_topped_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_guard_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_full_helm", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_great_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_nomad_cap_b", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_skullcap", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_leather_cap", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#
#      (item_set_slot, "itm_spiked_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
##      (item_set_slot, "itm_nasal_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_nordic_archer_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_nordic_veteran_archer_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_nordic_footman_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_nordic_fighter_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_nordic_huscarl_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_nordic_warlord_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#
#      (item_set_slot, "itm_sarranid_helmet1", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_sarranid_horseman_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_sarranid_felt_hat", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_sarranid_veiled_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_turban", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_desert_turban", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_sarranid_warrior_cap", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_sarranid_mail_coif", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#
#      (item_set_slot, "itm_vaegir_fur_cap", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_vaegir_fur_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_vaegir_spiked_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_vaegir_lamellar_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_vaegir_noble_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_vaegir_war_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_vaegir_mask", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#
#
#      #gloves
#      (item_set_slot, "itm_leather_gloves", slot_item_multiplayer_item_class, multi_item_class_type_glove),
#      (item_set_slot, "itm_mail_mittens", slot_item_multiplayer_item_class, multi_item_class_type_glove),
#      (item_set_slot, "itm_scale_gauntlets", slot_item_multiplayer_item_class, multi_item_class_type_glove),
#      (item_set_slot, "itm_lamellar_gauntlets", slot_item_multiplayer_item_class, multi_item_class_type_glove),
#      (item_set_slot, "itm_gauntlets", slot_item_multiplayer_item_class, multi_item_class_type_glove),
#
#      #horses
#      (item_set_slot, "itm_saddle_horse", slot_item_multiplayer_item_class, multi_item_class_type_horse),
#      (item_set_slot, "itm_hunter", slot_item_multiplayer_item_class, multi_item_class_type_horse),
#      (item_set_slot, "itm_courser", slot_item_multiplayer_item_class, multi_item_class_type_horse),
#      (item_set_slot, "itm_hunter", slot_item_multiplayer_item_class, multi_item_class_type_horse),
#      (item_set_slot, "itm_sarranid_warhorse_b", slot_item_multiplayer_item_class, multi_item_class_type_horse),
#      (item_set_slot, "itm_khergit_charger_b", slot_item_multiplayer_item_class, multi_item_class_type_horse),
#      (item_set_slot, "itm_steppe_horse", slot_item_multiplayer_item_class, multi_item_class_type_horse),
#      (item_set_slot, "itm_arabian_horse_a", slot_item_multiplayer_item_class, multi_item_class_type_horse),
#      (item_set_slot, "itm_arabian_horse_b", slot_item_multiplayer_item_class, multi_item_class_type_horse),
#      (item_set_slot, "itm_warhorse_steppe", slot_item_multiplayer_item_class, multi_item_class_type_horse),
#      (item_set_slot, "itm_warhorse_sarranid", slot_item_multiplayer_item_class, multi_item_class_type_horse),
#
#
#      #1-Swadian Warriors
#      #1a-Swadian Crossbowman
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bolts", "trp_swadian_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_steel_bolts", "trp_swadian_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_crossbow", "trp_swadian_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_heavy_crossbow", "trp_swadian_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sniper_crossbow", "trp_swadian_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_a", "trp_swadian_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_b", "trp_swadian_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_b_small", "trp_swadian_crossbowman_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_heater_a", "trp_swadian_crossbowman_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_heater_b", "trp_swadian_crossbowman_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_heater_c", "trp_swadian_crossbowman_multiplayer"),
#
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_red_shirt", "trp_swadian_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_padded_cloth", "trp_swadian_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_armor", "trp_swadian_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_haubergeon", "trp_swadian_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankle_boots", "trp_swadian_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_boots", "trp_swadian_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_chausses", "trp_swadian_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves", "trp_swadian_crossbowman_multiplayer"),
#
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_swadian_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_norman_helmet", "trp_swadian_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_helmet_with_neckguard", "trp_swadian_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_flat_topped_helmet", "trp_swadian_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_guard_helmet", "trp_swadian_crossbowman_multiplayer"),
#
#      #1b-Swadian Infantry
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_awlpike", "trp_swadian_infantry_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_awlpike_long", "trp_swadian_infantry_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_a", "trp_swadian_infantry_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_b", "trp_swadian_infantry_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_b_small", "trp_swadian_infantry_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_c", "trp_swadian_infantry_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_c_small", "trp_swadian_infantry_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bastard_sword_a", "trp_swadian_infantry_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bastard_sword_b", "trp_swadian_infantry_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_two_handed_a", "trp_swadian_infantry_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_two_handed_b", "trp_swadian_infantry_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_swadian_infantry_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_war_darts", "trp_swadian_infantry_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_heater_a", "trp_swadian_infantry_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_heater_b", "trp_swadian_infantry_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_heater_c", "trp_swadian_infantry_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_heater_d", "trp_swadian_infantry_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_red_tunic", "trp_swadian_infantry_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_red_gambeson", "trp_swadian_infantry_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_armor", "trp_swadian_infantry_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_haubergeon", "trp_swadian_infantry_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_brigandine_red", "trp_swadian_infantry_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankle_boots", "trp_swadian_infantry_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_boots", "trp_swadian_infantry_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_chausses", "trp_swadian_infantry_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_greaves", "trp_swadian_infantry_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_swadian_infantry_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_norman_helmet", "trp_swadian_infantry_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_helmet_with_neckguard", "trp_swadian_infantry_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_flat_topped_helmet", "trp_swadian_infantry_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_guard_helmet", "trp_swadian_infantry_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_great_helmet", "trp_swadian_infantry_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves", "trp_swadian_infantry_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_mittens", "trp_swadian_infantry_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_gauntlets", "trp_swadian_infantry_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gauntlets", "trp_swadian_infantry_multiplayer"),
#
#      #1c-Swadian Man At Arms
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_war_darts", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lance", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_heavy_lance", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_great_lance", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_a", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_b", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_b_small", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_c", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_c_small", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bastard_sword_a", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bastard_sword_b", "trp_swadian_man_at_arms_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_heater_a", "trp_swadian_man_at_arms_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_heater_b", "trp_swadian_man_at_arms_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_heater_c", "trp_swadian_man_at_arms_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_heater_d", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_red_tunic", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_padded_cloth", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_armor", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_with_surcoat", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_coat_of_plates_red", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankle_boots", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_boots", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_chausses", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_greaves", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plate_boots", "trp_swadian_man_at_arms_multiplayer"),
#
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_norman_helmet", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_helmet_with_neckguard", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_flat_topped_helmet", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_guard_helmet", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_great_helmet", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_mittens", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_gauntlets", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gauntlets", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saddle_horse", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_courser", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunter", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_warhorse_b", "trp_swadian_man_at_arms_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_khergit_charger_b", "trp_swadian_man_at_arms_multiplayer"),
#
#      # #1d-Swadian Mounted Crossbowman
#      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bolts", "trp_swadian_mounted_crossbowman_multiplayer"),
#      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_light_crossbow", "trp_swadian_mounted_crossbowman_multiplayer"),
#      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_crossbow", "trp_swadian_mounted_crossbowman_multiplayer"),
#      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_heavy_crossbow", "trp_swadian_mounted_crossbowman_multiplayer"),
#      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_heater_cav_a", "trp_swadian_mounted_crossbowman_multiplayer"),
#      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_heater_cav_b", "trp_swadian_mounted_crossbowman_multiplayer"),
#      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bastard_sword_a", "trp_swadian_mounted_crossbowman_multiplayer"),
#      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_red_shirt", "trp_swadian_mounted_crossbowman_multiplayer"),
#      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_padded_cloth", "trp_swadian_mounted_crossbowman_multiplayer"),
#      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_armor", "trp_swadian_mounted_crossbowman_multiplayer"),
#      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_with_surcoat", "trp_swadian_mounted_crossbowman_multiplayer"),
#      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_coat_of_plates_red", "trp_swadian_mounted_crossbowman_multiplayer"),
#      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hide_boots", "trp_swadian_mounted_crossbowman_multiplayer"),
#      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_swadian_mounted_crossbowman_multiplayer"),
#      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_norman_helmet", "trp_swadian_mounted_crossbowman_multiplayer"),
#      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_helmet_with_neckguard", "trp_swadian_mounted_crossbowman_multiplayer"),
#      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_flat_topped_helmet", "trp_swadian_mounted_crossbowman_multiplayer"),
#      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_guard_helmet", "trp_swadian_mounted_crossbowman_multiplayer"),
#      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves", "trp_swadian_mounted_crossbowman_multiplayer"),
#      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saddle_horse", "trp_swadian_mounted_crossbowman_multiplayer"),
#      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_courser", "trp_swadian_mounted_crossbowman_multiplayer"),
#      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunter", "trp_swadian_mounted_crossbowman_multiplayer"),
#
#      #2-Vaegir Warriors
#      #2a-Vaegir Archer
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows", "trp_vaegir_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_barbed_arrows", "trp_vaegir_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scimitar_a", "trp_vaegir_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mace_1", "trp_vaegir_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mace_2", "trp_vaegir_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nomad_bow", "trp_vaegir_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_khergit_bow", "trp_vaegir_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_strong_bow", "trp_vaegir_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_war_bow", "trp_vaegir_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_tunic", "trp_vaegir_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_jerkin", "trp_vaegir_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_vest", "trp_vaegir_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lamellar_vest", "trp_vaegir_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hide_boots", "trp_vaegir_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nomad_boots", "trp_vaegir_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_vaegir_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nomad_cap", "trp_vaegir_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_fur_cap", "trp_vaegir_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_fur_helmet", "trp_vaegir_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_spiked_helmet", "trp_vaegir_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_lamellar_helmet", "trp_vaegir_archer_multiplayer"),
#
#      #2b-Vaegir Spearman
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_war_spear", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_awlpike", "trp_vaegir_spearman_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_kite_a", "trp_vaegir_spearman_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_kite_b", "trp_vaegir_spearman_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_kite_c", "trp_vaegir_spearman_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_kite_d", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mace_1", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mace_2", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mace_3", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mace_4", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_long_hafted_spiked_mace", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_long_spiked_club", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scimitar_a", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scimitar_b", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bardiche", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_great_bardiche", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_long_bardiche", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_great_long_bardiche", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelin", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_tunic", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_jerkin", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_vest", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lamellar_vest", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lamellar_armor", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_elite_armor", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hide_boots", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nomad_boots", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_greaves", "trp_vaegir_spearman_multiplayer"),
##      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spiked_helmet", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_fur_cap", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_fur_helmet", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_spiked_helmet", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_lamellar_helmet", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_noble_helmet", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_war_helmet", "trp_vaegir_spearman_multiplayer"),
#      #      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nasal_helmet", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_mittens", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_gauntlets", "trp_vaegir_spearman_multiplayer"),
#
#      #2c-Vaegir Horseman
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_war_darts", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bardiche", "trp_vaegir_horseman_multiplayer"),
##      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_great_bardiche", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scimitar_a", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scimitar_b", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lance", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_heavy_lance", "trp_vaegir_horseman_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_kite_cav_a", "trp_vaegir_horseman_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_kite_cav_b", "trp_vaegir_horseman_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_kite_c", "trp_vaegir_horseman_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_kite_d", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_tunic", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_vest", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lamellar_vest", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_studded_leather_coat", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lamellar_armor", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_elite_armor", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hide_boots", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nomad_boots", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_greaves", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plate_boots", "trp_vaegir_horseman_multiplayer"),
##      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spiked_helmet", "trp_vaegir_horseman_multiplayer"),
##      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nasal_helmet", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_fur_cap", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_fur_helmet", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_spiked_helmet", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_lamellar_helmet", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_noble_helmet", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_war_helmet", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_mask", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_mittens", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_gauntlets", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saddle_horse", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_courser", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunter", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_warhorse_steppe", "trp_vaegir_horseman_multiplayer"),
#
#      #3-Khergit Warriors
#      #3a-Khergit Veteran Horse Archer
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_khergit_1", "trp_khergit_veteran_horse_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_khergit_2", "trp_khergit_veteran_horse_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_khergit_3", "trp_khergit_veteran_horse_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_khergit_4", "trp_khergit_veteran_horse_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nomad_bow", "trp_khergit_veteran_horse_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_khergit_bow", "trp_khergit_veteran_horse_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_strong_bow", "trp_khergit_veteran_horse_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows", "trp_khergit_veteran_horse_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_khergit_arrows", "trp_khergit_veteran_horse_archer_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_small_round_a", "trp_khergit_veteran_horse_archer_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_small_round_b", "trp_khergit_veteran_horse_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_steppe_cap_a", "trp_khergit_veteran_horse_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nomad_cap_b", "trp_khergit_veteran_horse_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_steppe_cap_b", "trp_khergit_veteran_horse_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_steppe_cap", "trp_khergit_veteran_horse_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_khergit_armor", "trp_khergit_veteran_horse_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_steppe_armor", "trp_khergit_veteran_horse_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tribal_warrior_outfit", "trp_khergit_veteran_horse_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lamellar_vest_khergit", "trp_khergit_veteran_horse_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hide_boots", "trp_khergit_veteran_horse_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nomad_boots", "trp_khergit_veteran_horse_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_khergit_leather_boots", "trp_khergit_veteran_horse_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_khergit_veteran_horse_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_greaves", "trp_khergit_veteran_horse_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_steppe_horse", "trp_khergit_veteran_horse_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves", "trp_khergit_veteran_horse_archer_multiplayer"),
#      #3a-Khergit Lancer
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelin", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_khergit_1", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_khergit_2", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_khergit_3", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_khergit_4", "trp_khergit_lancer_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_small_round_a", "trp_khergit_lancer_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_small_round_b", "trp_khergit_lancer_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_small_round_c", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lance", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_heavy_lance", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hafted_blade_a", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hafted_blade_b", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mace_1", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mace_2", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mace_3", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_one_handed_war_axe_a", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_one_handed_war_axe_b", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_steppe_cap_a", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nomad_cap_b", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_steppe_cap_b", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_steppe_cap", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_khergit_war_helmet", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tarkhan_helm", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_khergit_armor", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_steppe_armor", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tribal_warrior_outfit", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lamellar_armor", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_khergit_elite_armor", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hide_boots", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nomad_boots", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_khergit_leather_boots", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_greaves", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_mittens", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_gauntlets", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lamellar_gauntlets", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_steppe_horse", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_courser", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunter", "trp_khergit_lancer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_warhorse_steppe", "trp_khergit_lancer_multiplayer"),
#
#      #Nord Warriors
#
#      #4c-Nord Archer
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows", "trp_nord_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_barbed_arrows", "trp_nord_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bodkin_arrows", "trp_nord_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_viking_1", "trp_nord_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_viking_2", "trp_nord_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_viking_2_small", "trp_nord_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_viking_3", "trp_nord_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_viking_3_small", "trp_nord_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_one_handed_war_axe_a", "trp_nord_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_one_handed_war_axe_b", "trp_nord_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_two_handed_axe", "trp_nord_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_short_bow", "trp_nord_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_long_bow", "trp_nord_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blue_tunic", "trp_nord_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_jerkin", "trp_nord_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_byrnie", "trp_nord_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_boots", "trp_nord_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_nord_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_chausses", "trp_nord_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_boots", "trp_nord_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nordic_archer_helmet", "trp_nord_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nordic_veteran_archer_helmet", "trp_nord_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nordic_footman_helmet", "trp_nord_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nordic_fighter_helmet", "trp_nord_archer_multiplayer"),
#
#      #4a-Nord Veteran
##      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_nord_veteran_multiplayer"),
##      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_war_darts", "trp_nord_veteran_multiplayer"),
##      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelin", "trp_nord_veteran_multiplayer"),
##      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spears", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_viking_1", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_viking_2", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_viking_2_small", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_viking_3", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_viking_3_small", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_one_handed_war_axe_a", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_one_handed_war_axe_b", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_one_handed_battle_axe_a", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_one_handed_battle_axe_b", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_one_handed_battle_axe_c", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_two_handed_axe", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_two_handed_battle_axe_2", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_great_axe_new", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_long_axe", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_long_axe_b", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_long_axe_c", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_war_spear", "trp_nord_veteran_multiplayer"),
#
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_round_a", "trp_nord_veteran_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_round_b", "trp_nord_veteran_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_round_c", "trp_nord_veteran_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_round_d", "trp_nord_veteran_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_round_e", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_light_throwing_axes", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_axes", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_heavy_throwing_axes", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nordic_veteran_archer_helmet", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nordic_footman_helmet", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nordic_fighter_helmet", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nordic_huscarl_helmet", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nordic_warlord_helmet", "trp_nord_veteran_multiplayer"),
#
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blue_tunic", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_jerkin", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_shirt", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_hauberk", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_banded_armor", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_boots", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_chausses", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_boots", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_mittens", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_gauntlets", "trp_nord_veteran_multiplayer"),
#
#      #4b-Nord Scout
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_nord_scout_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_war_darts", "trp_nord_scout_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelin", "trp_nord_scout_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spears", "trp_nord_scout_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_light_throwing_axes", "trp_nord_scout_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_axes", "trp_nord_scout_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_viking_1", "trp_nord_scout_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_viking_2", "trp_nord_scout_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_viking_3", "trp_nord_scout_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_two_handed_axe", "trp_nord_scout_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_two_handed_battle_axe_2", "trp_nord_scout_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortened_voulge", "trp_nord_scout_multiplayer"),
#
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear", "trp_nord_scout_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_war_spear", "trp_nord_scout_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_light_lance", "trp_nord_scout_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lance", "trp_nord_scout_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_small_round_a", "trp_nord_scout_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_small_round_b", "trp_nord_scout_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_small_round_c", "trp_nord_scout_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nordic_archer_helmet", "trp_nord_scout_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nordic_veteran_archer_helmet", "trp_nord_scout_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nordic_footman_helmet", "trp_nord_scout_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nordic_fighter_helmet", "trp_nord_scout_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nordic_huscarl_helmet", "trp_nord_scout_multiplayer"),
#
#
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blue_tunic", "trp_nord_scout_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_jerkin", "trp_nord_scout_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_shirt", "trp_nord_scout_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_hauberk", "trp_nord_scout_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_boots", "trp_nord_scout_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_nord_scout_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_chausses", "trp_nord_scout_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_boots", "trp_nord_scout_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves", "trp_nord_scout_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_mittens", "trp_nord_scout_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_gauntlets", "trp_nord_scout_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saddle_horse", "trp_nord_scout_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_courser", "trp_nord_scout_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunter", "trp_nord_scout_multiplayer"),
#
#
#      #5-Rhodok Warriors
#      #5a-Rhodok Veteran Crossbowman
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_crossbow", "trp_rhodok_veteran_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_heavy_crossbow", "trp_rhodok_veteran_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sniper_crossbow", "trp_rhodok_veteran_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bolts", "trp_rhodok_veteran_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_steel_bolts", "trp_rhodok_veteran_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_fighting_pick", "trp_rhodok_veteran_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_military_pick", "trp_rhodok_veteran_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_club_with_spike_head", "trp_rhodok_veteran_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_maul", "trp_rhodok_veteran_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sledgehammer", "trp_rhodok_veteran_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_a", "trp_rhodok_veteran_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_b", "trp_rhodok_veteran_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_b_small", "trp_rhodok_veteran_crossbowman_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_pavise_a", "trp_rhodok_veteran_crossbowman_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_pavise_b", "trp_rhodok_veteran_crossbowman_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_pavise_c", "trp_rhodok_veteran_crossbowman_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_pavise_d", "trp_rhodok_veteran_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_cap", "trp_rhodok_veteran_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_padded_coif", "trp_rhodok_veteran_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_footman_helmet", "trp_rhodok_veteran_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_kettle_hat", "trp_rhodok_veteran_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tunic_with_green_cape", "trp_rhodok_veteran_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_aketon_green", "trp_rhodok_veteran_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_armor", "trp_rhodok_veteran_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankle_boots", "trp_rhodok_veteran_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_boots", "trp_rhodok_veteran_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_greaves", "trp_rhodok_veteran_crossbowman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves", "trp_rhodok_veteran_crossbowman_multiplayer"),
#
#      #5b-Rhodok Sergeant
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_war_darts", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelin", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_fighting_pick", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_military_pick", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_morningstar", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_club_with_spike_head", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_military_cleaver_b", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_military_cleaver_c", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_two_handed_cleaver", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_military_sickle_a", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_maul", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sledgehammer", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_warhammer", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pike", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ashwood_pike", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_war_spear", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_glaive", "trp_rhodok_sergeant_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_pavise_a", "trp_rhodok_sergeant_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_pavise_b", "trp_rhodok_sergeant_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_pavise_c", "trp_rhodok_sergeant_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_pavise_d", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_cap", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_padded_coif", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_footman_helmet", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_kettle_hat", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bascinet_2", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_full_helm", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_green_tunic", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_aketon_green", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ragged_outfit", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_armor", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_surcoat_over_mail", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankle_boots", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_boots", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_greaves", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_iron_greaves", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_mittens", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_gauntlets", "trp_rhodok_sergeant_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gauntlets", "trp_rhodok_sergeant_multiplayer"),
#
#      #5c-Rhodok Horseman
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_war_darts", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelin", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_a", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_b", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_c", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_fighting_pick", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_military_pick", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_morningstar", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_military_cleaver_b", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_military_cleaver_c", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_two_handed_cleaver", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortened_military_scythe", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_light_lance", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lance", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_heavy_lance", "trp_rhodok_horseman_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_heater_cav_a", "trp_rhodok_horseman_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_heater_cav_b", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_padded_coif", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_footman_helmet", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_kettle_hat", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bascinet_3", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_green_tunic", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_aketon_green", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ragged_outfit", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_armor", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_surcoat_over_mail", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankle_boots", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_boots", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_greaves", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plate_boots", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_mittens", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_gauntlets", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gauntlets", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saddle_horse", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_courser", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunter", "trp_rhodok_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_warhorse_b", "trp_rhodok_horseman_multiplayer"),
#
#
#
#      #6-Sarranid Warriors
#      #5a-Sarranid archer
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_cloth_robe", "trp_sarranid_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skirmisher_armor", "trp_sarranid_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_archers_vest", "trp_sarranid_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_khergit_mail_plate_a", "trp_sarranid_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_felt_hat", "trp_sarranid_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_turban", "trp_sarranid_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_desert_turban", "trp_sarranid_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_mail_coif", "trp_sarranid_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_horseman_helmet", "trp_sarranid_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_warrior_cap", "trp_sarranid_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_boots_b", "trp_sarranid_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_boots_c", "trp_sarranid_archer_multiplayer"),
#
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_short_bow", "trp_sarranid_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nomad_bow", "trp_sarranid_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows", "trp_sarranid_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_barbed_arrows", "trp_sarranid_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scimitar_a", "trp_sarranid_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mace_1", "trp_sarranid_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arabian_sword_a", "trp_sarranid_archer_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arabian_sword_b", "trp_sarranid_archer_multiplayer"),
#
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves", "trp_sarranid_archer_multiplayer"),
#
#
#
#      #Sarranid footman
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_cloth_robe", "trp_sarranid_footman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skirmisher_armor", "trp_sarranid_footman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_archers_vest", "trp_sarranid_footman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_leather_armor", "trp_sarranid_footman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_khergit_mail_plate_a", "trp_sarranid_footman_multiplayer"),
#
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_elite_armor", "trp_sarranid_footman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_felt_hat", "trp_sarranid_footman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_turban", "trp_sarranid_footman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_desert_turban", "trp_sarranid_footman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_mail_coif", "trp_sarranid_footman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_warrior_cap", "trp_sarranid_footman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_veiled_helmet", "trp_sarranid_footman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_boots_b", "trp_sarranid_footman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_boots_c", "trp_sarranid_footman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_boots_d", "trp_sarranid_footman_multiplayer"),
#
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arabian_sword_a", "trp_sarranid_footman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arabian_sword_b", "trp_sarranid_footman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arabian_sword_d", "trp_sarranid_footman_multiplayer"),
#
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_mace_1", "trp_sarranid_footman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_axe_a", "trp_sarranid_footman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_axe_b", "trp_sarranid_footman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_two_handed_axe_a", "trp_sarranid_footman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_two_handed_axe_b", "trp_sarranid_footman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_two_handed_mace_1", "trp_sarranid_footman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bamboo_spear", "trp_sarranid_footman_multiplayer"),
#
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear", "trp_sarranid_footman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jarid", "trp_sarranid_footman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelin", "trp_sarranid_footman_multiplayer"),
#
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_kite_a", "trp_sarranid_footman_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_kite_b", "trp_sarranid_footman_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_kite_c", "trp_sarranid_footman_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_kite_d", "trp_sarranid_footman_multiplayer"),
#
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves", "trp_sarranid_footman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_mittens", "trp_sarranid_footman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_gauntlets", "trp_sarranid_footman_multiplayer"),
#
#
#
#
#      #Sarranid mamluke
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_cloth_robe", "trp_sarranid_mamluke_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skirmisher_armor", "trp_sarranid_mamluke_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_archers_vest", "trp_sarranid_mamluke_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_mail_shirt", "trp_sarranid_mamluke_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_cavalry_robe", "trp_sarranid_mamluke_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mamluke_mail", "trp_sarranid_mamluke_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_elite_armor", "trp_sarranid_mamluke_multiplayer"),
#
#
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_turban", "trp_sarranid_mamluke_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_desert_turban", "trp_sarranid_mamluke_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_horseman_helmet", "trp_sarranid_mamluke_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_mail_coif", "trp_sarranid_mamluke_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_veiled_helmet", "trp_sarranid_mamluke_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_boots_b", "trp_sarranid_mamluke_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_boots_c", "trp_sarranid_mamluke_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_boots_d", "trp_sarranid_mamluke_multiplayer"),
#
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arabian_sword_a", "trp_sarranid_mamluke_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arabian_sword_b", "trp_sarranid_mamluke_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_cavalry_sword", "trp_sarranid_mamluke_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arabian_sword_d", "trp_sarranid_mamluke_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_mace_1", "trp_sarranid_mamluke_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_axe_a", "trp_sarranid_mamluke_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_axe_b", "trp_sarranid_mamluke_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_two_handed_axe_a", "trp_sarranid_mamluke_multiplayer"),
#
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lance", "trp_sarranid_mamluke_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_heavy_lance", "trp_sarranid_mamluke_multiplayer"),
#
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jarid", "trp_sarranid_mamluke_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelin", "trp_sarranid_mamluke_multiplayer"),
#
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_small_round_a", "trp_sarranid_mamluke_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_small_round_b", "trp_sarranid_mamluke_multiplayer"),
#      #(call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_small_round_c", "trp_sarranid_mamluke_multiplayer"),
#
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saddle_horse", "trp_sarranid_mamluke_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arabian_horse_a", "trp_sarranid_mamluke_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arabian_horse_b", "trp_sarranid_mamluke_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_warhorse_sarranid", "trp_sarranid_mamluke_multiplayer"),
#
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves", "trp_sarranid_mamluke_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_mittens", "trp_sarranid_mamluke_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_gauntlets", "trp_sarranid_mamluke_multiplayer"),

	],

	'script_get_banner_mesh': [
         (game_in_multiplayer_mode),
         (agent_get_group, ":agent_group", ":agent_no"),
         (try_begin),
           (neg|player_is_active, ":agent_group"),
           (agent_get_player_id, ":agent_group", ":agent_no"),
         (try_end),
         (try_begin),
           #if player banners are not allowed, use the default banner mesh
           (eq, "$g_multiplayer_allow_player_banners", 1),
           (player_is_active, ":agent_group"),
           (player_get_banner_id, ":player_banner", ":agent_group"),
           (ge, ":player_banner", 0),
           (store_add, ":banner_mesh", ":player_banner", banner_meshes_begin),
           (assign, ":already_used", 0),
           (try_for_range, ":cur_faction", npc_kingdoms_begin, npc_kingdoms_end), #wrong client data check
             (faction_slot_eq, ":cur_faction", slot_faction_banner, ":banner_mesh"),
             (assign, ":already_used", 1),
           (try_end),
           (eq, ":already_used", 0), #otherwise use the default banner mesh
         (else_try),
           (agent_get_team, ":agent_team", ":agent_no"),
           (team_get_faction, ":team_faction_no", ":agent_team"),

           (try_begin),
             (agent_is_human, ":agent_no"),
             (faction_get_slot, ":banner_mesh", ":team_faction_no", slot_faction_banner),
           (else_try),
             (agent_get_rider, ":rider_agent_no", ":agent_no"),
             #(agent_get_position, pos1, ":agent_no"),
             #(position_get_x, ":pos_x", pos1),
             #(position_get_y, ":pos_y", pos1),
             #(assign, reg0, ":pos_x"),
             #(assign, reg1, ":pos_y"),
             #(assign, reg2, ":agent_no"),
             #(display_message, "@{!}agent_no:{reg2}, pos_x:{reg0} , posy:{reg1}"),
             (try_begin),
               (ge, ":rider_agent_no", 0),
               (agent_is_active, ":rider_agent_no"),
               (agent_get_team, ":rider_agent_team", ":rider_agent_no"),
               (team_get_faction, ":rider_team_faction_no", ":rider_agent_team"),
               (faction_get_slot, ":banner_mesh", ":rider_team_faction_no", slot_faction_banner),
             (else_try),
               (assign, ":banner_mesh", "mesh_banners_default_c"),
             (try_end),
           (try_end),
         (try_end),
       (else_try),
	],
}

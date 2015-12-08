from ID_items import *
from ID_quests import *
from ID_factions import *
##############################################################
# These constants are used in various files.
# If you need to define a value that will be used in those files,
# just define it here rather than copying it across each file, so
# that it will be easy to change it if you need to.
##############################################################

########################################################
##  ITEM SLOTS             #############################
########################################################

slot_item_multiplayer_item_class   = 1 #temporary, can be moved to higher values
slot_item_multiplayer_availability_linked_list_begin = 2 #temporary, can be moved to higher values


########################################################
##  AGENT SLOTS            #############################
########################################################

slot_agent_last_voice_at          = 1
slot_agent_last_sound_at          = 2
slot_agent_underwater_time        = 3
slot_agent_underwater_now         = 4
slot_agent_frizzle_times          = 5
slot_agent_current_command        = 6
slot_agent_current_control_prop   = 7
slot_agent_used_prop_instance     = 8
slot_agent_alone                  = 9
slot_agent_cur_damage_modifier    = 10
slot_agent_cur_accuracy_modifier  = 11
slot_agent_cur_reload_speed_modifier = 12
slot_agent_cur_use_speed_modifier = 13
slot_agent_cur_speed_modifier     = 14
slot_agent_music_play_together    = 15
slot_agent_base_speed_mod         = 16
# slot_agent_teleport_pos_x         = 17
# slot_agent_teleport_pos_y         = 18
# slot_agent_teleport_pos_z         = 19
# slot_agent_teleport_pos_z_rot     = 20
slot_agent_flag_target            = 17
slot_agent_behaviour              = 18
slot_agent_in_duel_with           = 19
slot_agent_duel_start_time        = 20
slot_agent_map_overlay_id         = 21
slot_agent_is_running_away        = 22
slot_agent_courage_score          = 23
slot_agent_state                  = 24
slot_agent_walker_occupation      = 25

########################################################
##  FACTION SLOTS          #############################
########################################################

slot_faction_banner                     = 1


########################################################
##  TROOP SLOTS            #############################
########################################################

slot_troop_occupation          = 2  # 0 = free, 1 = merchant
#slot_troop_banner_scene_prop    = 3 # important for kingdom heroes and player only


# MM added
slot_troop_initial_morale              = 5
slot_troop_officer_troop               = 6
slot_troop_scale_factor                = 7
slot_troop_base_type                   = 8


slot_troop_custom_banner_bg_color_1      = 10
slot_troop_custom_banner_bg_color_2      = 11
slot_troop_custom_banner_charge_color_1  = 12
slot_troop_custom_banner_charge_color_2  = 13
slot_troop_custom_banner_charge_color_3  = 14
slot_troop_custom_banner_charge_color_4  = 15
slot_troop_custom_banner_bg_type         = 16
slot_troop_custom_banner_charge_type_1   = 17
slot_troop_custom_banner_charge_type_2   = 18
slot_troop_custom_banner_charge_type_3   = 19
slot_troop_custom_banner_charge_type_4   = 20
slot_troop_custom_banner_flag_type       = 21
slot_troop_custom_banner_num_charges     = 22
slot_troop_custom_banner_positioning     = 23
slot_troop_custom_banner_map_flag_type   = 24



slot_troop_button_id              = 30
slot_troop_button_2_id            = 31
slot_troop_active_this_mission    = 32


########################################################
##  PLAYER SLOTS           #############################
########################################################

slot_player_spawned_this_round                 = 0
slot_player_selected_item_indices_begin        = 2
slot_player_selected_item_indices_end          = 11
slot_player_cur_selected_item_indices_begin    = slot_player_selected_item_indices_end
slot_player_cur_selected_item_indices_end      = slot_player_selected_item_indices_end + 9
slot_player_join_time                          = 21
slot_player_button_index                       = 22 #used for presentations
slot_player_can_answer_poll                    = 23
slot_player_first_spawn                        = 24
slot_player_spawned_at_siege_round             = 25
slot_player_poll_disabled_until_time           = 26
slot_player_last_team_select_time              = 27
slot_player_death_pos_x                        = 28
slot_player_death_pos_y                        = 29
slot_player_death_pos_z                        = 30
slot_player_last_bot_count                     = 31
slot_player_bot_type_1_wanted                  = 32
slot_player_bot_type_2_wanted                  = 33
slot_player_bot_type_3_wanted                  = 34
slot_player_bot_type_4_wanted                  = 35
slot_player_spawn_count                        = 36

# MM
slot_player_selected_flag                      = 40
slot_player_bot_type_wanted                    = 41
slot_player_bot_type_spawned                   = 42
slot_player_teamkills                          = 43
slot_player_last_teamkill_at                   = 44

########################################################
##  TEAM SLOTS             #############################
########################################################

slot_team_flag_situation                       = 0


### Troop occupations slot_troop_occupation
##slto_merchant           = 1
slto_inactive           = 0 #for companions at the beginning of the game

slto_player_companion   = 5 #This is specifically for companions in the employ of the player -- ie, in the party, or on a mission


########################################################
##  SCENE PROP SLOTS       #############################
########################################################

scene_prop_open_or_close_slot       = 1
scene_prop_smoke_effect_done        = 2
# MM
scene_prop_slot_is_spawned          = 3
scene_prop_slot_in_use              = 4
scene_prop_slot_x_value             = 5
scene_prop_slot_y_value             = 6
scene_prop_slot_z_value             = 7
scene_prop_slot_x_rot               = 8
scene_prop_slot_y_rot               = 9
scene_prop_slot_z_rot               = 10
scene_prop_slot_z_rotation_limit    = 11
scene_prop_slot_x_scale             = 12
scene_prop_slot_y_scale             = 13
scene_prop_slot_z_scale             = 14
scene_prop_slot_x_extra             = 15
scene_prop_slot_y_extra             = 16
scene_prop_slot_z_extra             = 17
scene_prop_slot_time                = 18
scene_prop_slot_bounces             = 19
scene_prop_slot_times_hit           = 20
scene_prop_slot_owner_team          = 21
scene_prop_slot_time_left           = 22
scene_prop_slot_has_ball            = 23
scene_prop_slot_is_loaded           = 24
scene_prop_slot_is_active           = 25
scene_prop_slot_just_fired          = 26
scene_prop_slot_health              = 27
scene_prop_slot_max_health          = 28
scene_prop_slot_displayed_particle  = 29
scene_prop_slot_ammo_type           = 30
scene_prop_slot_ignore_inherit_movement = 31
scene_prop_slot_float_ground        = 32
scene_prop_slot_ground_offset       = 33
scene_prop_slot_spawned_at          = 34
scene_prop_slot_is_not_pushed_back  = 35
scene_prop_slot_just_pushed_back    = 36

# under here slots that need -1 as default
scene_prop_slot_replaced_by         = 37
scene_prop_slot_replacing           = 38
scene_prop_slot_last_hit_by         = 39
scene_prop_slot_user_agent          = 40
scene_prop_slot_controller_agent    = 41
scene_prop_slot_carrier_agent       = 42
scene_prop_slot_linked_prop         = 43

scene_prop_slot_sound_effect        = 45
scene_prop_slot_particle_effect1    = 46
scene_prop_slot_particle_effect2    = 47
scene_prop_slot_particle_effect3    = 48
scene_prop_slot_particle_effect4    = 49

scene_prop_slot_parent_prop         = 50
scene_prop_slot_child_prop1         = 51
scene_prop_slot_child_prop2         = 52
scene_prop_slot_child_prop3         = 53
scene_prop_slot_child_prop4         = 54
scene_prop_slot_child_prop5         = 55
scene_prop_slot_child_prop6         = 56
scene_prop_slot_child_prop7         = 57
scene_prop_slot_child_prop8         = 58
scene_prop_slot_child_prop9         = 59
scene_prop_slot_child_prop10        = 60
scene_prop_slot_child_prop11        = 61
scene_prop_slot_child_prop12        = 62
scene_prop_slot_child_prop13        = 63
scene_prop_slot_child_prop14        = 64
scene_prop_slot_child_prop15        = 65
scene_prop_slot_child_prop16        = 66

scene_prop_slots_begin              = scene_prop_open_or_close_slot
scene_prop_slots_end                = 67

scene_prop_slots_defmin_begin       = scene_prop_slot_replaced_by


########################################################

factions_begin = "fac_britain"
factions_end = "fac_kingdoms_end"

# MM
faction_name_strings_begin = "str_britain_name"

companions_begin = "trp_companion_1"
companions_end = "trp_companions_end"

multiplayer_troops_begin = "trp_british_infantry"
multiplayer_troops_end = "trp_multiplayer_end"

# MM
multiplayer_ai_troops_begin = "trp_british_infantry_ai"
multiplayer_ai_troops_end = multiplayer_troops_begin

multiplayer_scenes_begin = "scn_mp_arabian_harbour"
multiplayer_scenes_end = "scn_multiplayer_maps_end"

multiplayer_scene_names_begin = "str_mp_arabian_harbour"
multiplayer_scene_names_end = "str_multi_scene_end"

multiplayer_flag_projections_begin = "mesh_flag_project_sw"
multiplayer_flag_projections_end = "mesh_flag_projects_end"

multiplayer_flag_taken_projections_begin = "mesh_flag_project_sw_miss"
multiplayer_flag_taken_projections_end = "mesh_flag_project_misses_end"

multiplayer_game_type_names_begin = "str_multi_game_type_1"
multiplayer_game_type_names_end = "str_multi_game_types_end"

#MM Begin
quick_battle_troops_begin = "trp_quick_battle_troop_britain_1"
quick_battle_troops_end = "trp_quick_battle_troops_end"
#MM End

quick_battle_scenes_begin = "scn_quick_battle_french_farm"
quick_battle_scenes_end = "scn_quick_battle_maps_end"

quick_battle_scene_images_begin = "mesh_cb_ui_maps_scene_french_farm"

quick_battle_battle_scenes_begin = quick_battle_scenes_begin
quick_battle_battle_scenes_end = "scn_quick_battle_scene_4"

quick_battle_siege_scenes_begin = quick_battle_battle_scenes_end
quick_battle_siege_scenes_end = quick_battle_scenes_end

quick_battle_scene_names_begin = "str_quick_battle_french_farm"

all_items_begin = 0
all_items_end = "itm_items_end"



walkers_begin =  "trp_walker_french_infantry"
walkers_end   = "trp_walkers_end"

armor_merchants_begin  = "trp_camp_armorer"
armor_merchants_end    = "trp_camp_weaponsmith"

weapon_merchants_begin = "trp_camp_weaponsmith"
weapon_merchants_end   = "trp_camp_horse_merchant"

horse_merchants_begin  = "trp_camp_horse_merchant"
horse_merchants_end    = "trp_merchants_end"


num_max_items = 10000 #used for multiplayer mode



# Banner constants

banner_meshes_begin = "mesh_banner_a01"
banner_meshes_end_minus_one = "mesh_banner_f21"

arms_meshes_begin = "mesh_banner_a01"
arms_meshes_end_minus_one = "mesh_banner_f21"

#banner_scene_props_begin = 99 #"spr_banner_a"
#banner_scene_props_end_minus_one = 100#"spr_banner_f21"


# Some constants for merchant invenotries
merchant_inventory_space = 30


# AI Tactics

#battle tactics
btactic_defense = 1
btactic_attack = 2
btactic_charge = 3
btactic_probe = 4

#unit tactics
utactic_hold = 1
utactic_advance = 2
utactic_charge = 3
utactic_retreat = 4

#(unit) combat status
cstatus_ready = 1
cstatus_engaged_balanced = 2
cstatus_engaged_losing = 3
cstatus_engaged_winning = 4
cstatus_dead = 5
cstatus_advancing = 6

#unit type
utype_inf_line = 1
utype_inf_skirmish = 2
utype_inf_flanker = 3
utype_inf_reserve = 4
utype_cav_line = 5
utype_cav_skirmish = 6
utype_cav_flanker = 7
utype_cav_reserve = 8

#unit use weapon type
unit_use_firearms = 1
unit_use_melee = 2

#base troop slots
basetroop_infantry = 1
basetroop_guard = 2
basetroop_skirmisher = 3
basetroop_hussar = 4
basetroop_dragoon = 5
basetroop_light_cav = 6
basetroop_lancer = 7
basetroop_heavy_cav = 8

slot_team1_base_troops_begin = 0
slot_team2_base_troops_begin = slot_team1_base_troops_begin + 9
slot_team1_utypes_begin = slot_team2_base_troops_begin + 9
slot_team2_utypes_begin = slot_team1_utypes_begin + 9
slot_team1_cstatus_begin = slot_team2_utypes_begin + 9
slot_team2_cstatus_begin = slot_team1_cstatus_begin + 9
slot_team1_utactic_begin = slot_team2_cstatus_begin + 9
slot_team2_utactic_begin = slot_team1_utactic_begin + 9
slot_team1_amount_of_troops = slot_team2_utactic_begin + 9
slot_team2_amount_of_troops = slot_team1_amount_of_troops + 9
slot_team1_unit_use_weapon = slot_team2_amount_of_troops + 9
slot_team2_unit_use_weapon = slot_team1_unit_use_weapon+ 9


#NORMAL ACHIEVEMENTS
ACHIEVEMENT_NONE_SHALL_PASS = 1,
ACHIEVEMENT_MAN_EATER = 2,
ACHIEVEMENT_THE_HOLY_HAND_GRENADE = 3,
ACHIEVEMENT_LOOK_AT_THE_BONES = 4,
ACHIEVEMENT_KHAAAN = 5,
ACHIEVEMENT_GET_UP_STAND_UP = 6,
ACHIEVEMENT_BARON_GOT_BACK = 7,
ACHIEVEMENT_BEST_SERVED_COLD = 8,
ACHIEVEMENT_TRICK_SHOT = 9,
ACHIEVEMENT_GAMBIT = 10,
ACHIEVEMENT_OLD_SCHOOL_SNIPER = 11,
ACHIEVEMENT_CALRADIAN_ARMY_KNIFE = 12,
ACHIEVEMENT_MOUNTAIN_BLADE = 13,
ACHIEVEMENT_HOLY_DIVER = 14,
ACHIEVEMENT_FORCE_OF_NATURE = 15,

#SKILL RELATED ACHIEVEMENTS:
ACHIEVEMENT_BRING_OUT_YOUR_DEAD = 16,
ACHIEVEMENT_MIGHT_MAKES_RIGHT = 17,
ACHIEVEMENT_COMMUNITY_SERVICE = 18,
ACHIEVEMENT_AGILE_WARRIOR = 19,
ACHIEVEMENT_MELEE_MASTER = 20,
ACHIEVEMENT_DEXTEROUS_DASTARD = 21,
ACHIEVEMENT_MIND_ON_THE_MONEY = 22,
ACHIEVEMENT_ART_OF_WAR = 23,
ACHIEVEMENT_THE_RANGER = 24,
ACHIEVEMENT_TROJAN_BUNNY_MAKER = 25,

#MAP RELATED ACHIEVEMENTS:
ACHIEVEMENT_MIGRATING_COCONUTS = 26,
ACHIEVEMENT_HELP_HELP_IM_BEING_REPRESSED = 27,
ACHIEVEMENT_SARRANIDIAN_NIGHTS = 28,
ACHIEVEMENT_OLD_DIRTY_SCOUNDREL = 29,
ACHIEVEMENT_THE_BANDIT = 30,
ACHIEVEMENT_GOT_MILK = 31,
ACHIEVEMENT_SOLD_INTO_SLAVERY = 32,
ACHIEVEMENT_MEDIEVAL_TIMES = 33,
ACHIEVEMENT_GOOD_SAMARITAN = 34,
ACHIEVEMENT_MORALE_LEADER = 35,
ACHIEVEMENT_ABUNDANT_FEAST = 36,
ACHIEVEMENT_BOOK_WORM = 37,
ACHIEVEMENT_ROMANTIC_WARRIOR = 38,

#POLITICALLY ORIENTED ACHIEVEMENTS:
ACHIEVEMENT_HAPPILY_EVER_AFTER = 39,
ACHIEVEMENT_HEART_BREAKER = 40,
ACHIEVEMENT_AUTONOMOUS_COLLECTIVE = 41,
ACHIEVEMENT_I_DUB_THEE = 42,
ACHIEVEMENT_SASSY = 43,
ACHIEVEMENT_THE_GOLDEN_THRONE = 44,
ACHIEVEMENT_KNIGHTS_OF_THE_ROUND = 45,
ACHIEVEMENT_TALKING_HELPS = 46,
ACHIEVEMENT_KINGMAKER = 47,
ACHIEVEMENT_PUGNACIOUS_D = 48,
ACHIEVEMENT_GOLD_FARMER = 49,
ACHIEVEMENT_ROYALITY_PAYMENT = 50,
ACHIEVEMENT_MEDIEVAL_EMLAK = 51,
ACHIEVEMENT_CALRADIAN_TEA_PARTY = 52,
ACHIEVEMENT_MANIFEST_DESTINY = 53,
ACHIEVEMENT_CONCILIO_CALRADI = 54,
ACHIEVEMENT_VICTUM_SEQUENS = 55,

#MULTIPLAYER ACHIEVEMENTS:
ACHIEVEMENT_THIS_IS_OUR_LAND = 56,
ACHIEVEMENT_SPOIL_THE_CHARGE = 57,
ACHIEVEMENT_HARASSING_HORSEMAN = 58,
ACHIEVEMENT_THROWING_STAR = 59,
ACHIEVEMENT_SHISH_KEBAB = 60,
ACHIEVEMENT_RUIN_THE_RAID = 61,
ACHIEVEMENT_LAST_MAN_STANDING = 62,
ACHIEVEMENT_EVERY_BREATH_YOU_TAKE = 63,
ACHIEVEMENT_CHOPPY_CHOP_CHOP = 64,
ACHIEVEMENT_MACE_IN_YER_FACE = 65,
ACHIEVEMENT_THE_HUSCARL = 66,
ACHIEVEMENT_GLORIOUS_MOTHER_FACTION = 67,
ACHIEVEMENT_ELITE_WARRIOR = 68,

#COMBINED ACHIEVEMENTS
ACHIEVEMENT_SON_OF_ODIN = 69,
ACHIEVEMENT_KING_ARTHUR = 70,
ACHIEVEMENT_KASSAI_MASTER = 71,
ACHIEVEMENT_IRON_BEAR = 72,
ACHIEVEMENT_LEGENDARY_RASTAM = 73,
ACHIEVEMENT_SVAROG_THE_MIGHTY = 74,


# MM
multiplayer_player_loops_end      = 250

multiplayer_game_max_minutes_min  = 5
multiplayer_game_max_minutes_max  = 241

multiplayer_game_max_points       = 10001


mm_destructible_props_begin  = "spr_mm_house_wall_1"
mm_destructible_props_end    = "spr_mm_destructible_props_end"

mm_destroyed_props_begin     = "spr_mm_house_wall_2dd"
mm_destroyed_props_end       = "spr_mm_destroyed_props_end"

mm_cannon_types_begin        = "spr_mm_cannon_12pdr"
mm_cannon_types_end          = "spr_mm_cannons_end"
 
mm_cannon_wood_types_begin   = "spr_mm_cannon_12pdr_wood"
mm_cannon_wood_types_end     = "spr_mm_cannon_12pdr_wheels"

mm_cannon_wheel_types_begin  = "spr_mm_cannon_12pdr_wheels"
mm_cannon_wheel_types_end    = "spr_mm_cannon_12pdr_barrel"

mm_cannon_barrel_types_begin = "spr_mm_cannon_12pdr_barrel"
mm_cannon_barrel_types_end   = "spr_mm_cannon_12pdr_limber_wheels"

mm_unlimber_button_types_begin = "spr_mm_cannon_12pdr_limber"
mm_unlimber_button_types_end   = "spr_mm_limber_button"

mm_cannon_button_types_begin   = "spr_mm_limber_button"
mm_cannon_button_types_end     = "spr_mm_round_button"

mm_button_types_begin       = "spr_mm_cannon_12pdr_limber"
mm_button_types_end         = "spr_mm_buttons_end"

mm_explosive_props_begin       = "spr_crate_explosive_fra"
mm_explosive_props_end         = "spr_crate_explosive_end"

mm_construct_props_begin       = "spr_mm_stakes_construct"
mm_construct_props_end         = "spr_mm_construct_props_end"

mm_construct_props_strings     = "str_mm_stakes_construct"

mm_construct_props_meshes     = "mesh_construct_mesh_stakes"

firearm_type_pistol         = 1
firearm_type_carabine       = 2
firearm_type_rifle          = 3
firearm_type_musket         = 4

firearm_types_begin        = 1
firearm_types_end          = firearm_type_musket + 1 # + 1 cause loops are -1


mod_variable_use_class_limits  = 1
mod_variable_class_limit_player_count = 2
mod_variable_limit_grenadier   = 3
mod_variable_limit_skirmisher  = 4
mod_variable_limit_rifle       = 5
mod_variable_limit_cavalry     = 6
mod_variable_limit_lancer      = 7
mod_variable_limit_hussar      = 8
mod_variable_limit_dragoon     = 9
mod_variable_limit_cuirassier  = 10
mod_variable_limit_heavycav    = 11
mod_variable_limit_artillery   = 12
mod_variable_limit_rocket      = 13
mod_variable_limit_sapper      = 14
mod_variable_limit_musician    = 15
mod_variable_limit_sergeant    = 16
mod_variable_limit_officer     = 17
mod_variable_limit_general     = 18
mod_variable_squad_size        = 19
mod_variable_scale_squad       = 20
mod_variable_max_num_bots      = 21
mod_variable_build_points_1    = 22
mod_variable_build_points_2    = 23
mod_variable_allow_multiple_firearms = 24
mod_variable_enable_bonuses    = 25
mod_variable_bonus_strength    = 26
mod_variable_bonus_range       = 27
mod_variable_fall_off_horse    = 28
mod_variable_horse_dying       = 29
mod_variable_auto_kick         = 30
mod_variable_max_teamkills_before_kick = 31
mod_variable_auto_horse        = 32
mod_variable_auto_swap         = 33
mod_variable_beaconed_player   = 34

mod_variables_begin        = mod_variable_use_class_limits
mod_variables_end          = mod_variable_beaconed_player + 1


construct_item_bomb_brit   = 1
construct_item_bomb_fren   = 2
construct_item_bomb_prus   = 3

construct_items_begin      = 1
construct_items_end        = 4


mm_rank_ranker            = 1
mm_rank_musician          = 2
mm_rank_sergeant          = 3
mm_rank_officer           = 4
mm_rank_general           = 5

mm_ranks_begin            = mm_rank_ranker
mm_ranks_end              = mm_rank_general + 1

player_list_player         = 0
player_list_all            = 1

player_list_targets_begin  = 0
player_list_targets_end    = 2


player_list_admin_ban_player_temp    = 0
player_list_admin_slay_player        = 1
player_list_admin_freeze_player      = 2
player_list_admin_swap_player        = 3
player_list_admin_spec_player        = 4
player_list_admin_cheat_heal_player  = 5
player_list_admin_cheat_ammo_player  = 6
player_list_admin_autobalance_player = 7
player_list_admin_beacon_player      = 8

player_list_commands_begin  = player_list_admin_ban_player_temp
player_list_commands_end    = 9


cheat_item_hammer          = 1
cheat_item_shotgun         = 2
cheat_item_rocketlauncher  = 3
cheat_item_grenade         = 4
cheat_item_horse           = 5

cheat_items_begin          = cheat_item_hammer
cheat_items_end            = 6


cheat_tele_to              = 0
cheat_tele_bring           = 1
cheat_tele_wall            = 2

cheat_teles_begin          = cheat_tele_to
cheat_teles_end            = 3
# Vincenzo end

#Beaver
instrument_max_tracks = 20 #if adding more than 20 tracks in any list you need to increase this number

drum_sounds_britain_begin = "snd_drum_britain_1"
drum_sounds_britain_end   = "snd_drum_france_1"
drum_sounds_france_begin = drum_sounds_britain_end
drum_sounds_france_end   = "snd_drum_prussia_1"
drum_sounds_prussia_begin = drum_sounds_france_end
drum_sounds_prussia_end   = "snd_drum_russia_1"
drum_sounds_russia_begin = drum_sounds_prussia_end
drum_sounds_russia_end   = "snd_drum_austria_1"
drum_sounds_austria_begin = drum_sounds_russia_end
drum_sounds_austria_end   = "snd_drum_highland_1"
drum_sounds_highland_begin = drum_sounds_austria_end
drum_sounds_highland_end   = "snd_drum_signal_1"
drum_sounds_calls_begin = drum_sounds_highland_end
drum_sounds_calls_end   = "snd_fife_britain_1"

fife_sounds_britain_begin = drum_sounds_calls_end
fife_sounds_britain_end   = "snd_fife_france_1"
fife_sounds_france_begin = fife_sounds_britain_end
fife_sounds_france_end   = "snd_fife_prussia_1"
fife_sounds_prussia_begin = fife_sounds_france_end
fife_sounds_prussia_end   = "snd_fife_russia_1"
fife_sounds_russia_begin = fife_sounds_prussia_end
fife_sounds_russia_end   = "snd_fife_austria_1"
fife_sounds_austria_begin = fife_sounds_russia_end
fife_sounds_austria_end   = "snd_bugle_britain_1"

bugle_sounds_britain_begin = fife_sounds_austria_end
bugle_sounds_britain_end   = "snd_bugle_france_1"
bugle_sounds_france_begin = bugle_sounds_britain_end
bugle_sounds_france_end   = "snd_bugle_prussia_1"
bugle_sounds_prussia_begin = bugle_sounds_france_end
bugle_sounds_prussia_end   = "snd_bugle_russia_1"
bugle_sounds_russia_begin = bugle_sounds_prussia_end
bugle_sounds_russia_end   = "snd_bugle_austria_1"
bugle_sounds_austria_begin = bugle_sounds_russia_end
bugle_sounds_austria_end   = "snd_bugle_signal_1"
bugle_sounds_calls_begin = bugle_sounds_austria_end
bugle_sounds_calls_end   = "snd_bagpipes_britain_1"

bagpipes_sounds_britain_begin = bugle_sounds_calls_end
bagpipes_sounds_britain_end   = "snd_bagpipes_extra_1"
bagpipes_sounds_extra_begin = bagpipes_sounds_britain_end
bagpipes_sounds_extra_end   = "snd_piano_loop_1"

piano_sounds_begin = bagpipes_sounds_extra_end
piano_sounds_end   = "snd_organ_loop_1"

organ_sounds_begin = piano_sounds_end
organ_sounds_end   = "snd_instruments_end"

instrument_sounds_begin   = drum_sounds_britain_begin
instruments_sounds_end    = organ_sounds_end

drum_strings_britain_begin = "str_drum_britain_1"
drum_strings_france_begin = "str_drum_france_1"
drum_strings_prussia_begin = "str_drum_prussia_1"
drum_strings_russia_begin = "str_drum_russia_1"
drum_strings_austria_begin = "str_drum_austria_1"
drum_strings_highland_begin = "str_drum_highland_1"
drum_strings_calls_begin = "str_drum_signal_1"

fife_strings_britain_begin = "str_fife_britain_1"
fife_strings_france_begin = "str_fife_france_1"
fife_strings_prussia_begin = "str_fife_prussia_1"
fife_strings_russia_begin = "str_fife_russia_1"
fife_strings_austria_begin = "str_fife_austria_1"

bugle_strings_britain_begin = "str_bugle_britain_1"
bugle_strings_france_begin = "str_bugle_france_1"
bugle_strings_prussia_begin = "str_bugle_prussia_1"
bugle_strings_russia_begin = "str_bugle_russia_1"
bugle_strings_austria_begin = "str_bugle_austria_1"
bugle_strings_calls_begin = "str_bugle_signal_1"

bagpipes_strings_britain_begin = "str_bagpipes_britain_1"
bagpipes_strings_extra_begin = "str_bagpipes_extra_1"

piano_strings_begin   = "str_piano_tune_1"
organ_strings_begin   = "str_organ_tune_1"

construct_costs_offset    = 50
construct_button_offset   = construct_costs_offset + 20
construct_display_offset  = construct_button_offset + 20
construct_offset_end      = construct_display_offset + 20

troop_select_type_infantry  = 1
troop_select_type_cavalry   = 2
troop_select_type_artillery = 3

command_type_cannon         = 1
command_type_ship           = 2

command_types_begin         = command_type_cannon
command_types_end           = 3

ship_command_forward        = 1
ship_command_back           = 2
ship_command_left           = 3
ship_command_right          = 4
ship_command_forward_left   = 5
ship_command_forward_right  = 6
ship_command_back_left      = 7
ship_command_back_right     = 8

ship_commands_begin         = ship_command_forward
ship_commands_end           = 9


cannon_command_up           = 1
cannon_command_down         = 2
cannon_command_right        = 3
cannon_command_left         = 4
cannon_command_fire         = 5
cannon_command_stop_aim     = 6

cannon_commands_begin         = cannon_command_up
cannon_commands_end           = 7 


kill_type_self          = 1
kill_type_team          = 2
kill_type_enemy         = 3

kill_types_begin        = kill_type_self
kill_types_end          = 4


players_list_action_poll_kick   = 1
players_list_action_poll_ban    = 2
players_list_action_kick        = 3
players_list_action_slay        = 4
players_list_action_freeze      = 5
players_list_action_ban         = 6
players_list_action_ban_temp    = 7
players_list_action_swap        = 8
players_list_action_spec        = 9
players_list_action_mute        = 10
players_list_action_unmute      = 11
players_list_action_heal        = 12
players_list_action_ammo        = 13
players_list_action_beacon      = 14
players_list_action_tele_to     = 15
players_list_action_tele_bring  = 16


players_list_actions_begin      = players_list_action_poll_kick
players_list_actions_end        = 17


cannon_ammo_type_round      = 1
cannon_ammo_type_shell      = 2
cannon_ammo_type_canister   = 3
cannon_ammo_type_bomb       = 4
cannon_ammo_type_rocket     = 5

cannon_ammo_types_begin     = cannon_ammo_type_round
cannon_ammo_types_end       = 6

server_action_force_music_selection = 1

server_actions_begin                = server_action_force_music_selection
server_actions_end                  = 2

player_action_voice         = 1
player_action_music         = 2
player_action_spyglass      = 3
player_action_place_rocket  = 4
player_action_toggle_walk   = 5
player_action_has_cheat     = 6
player_action_surrender = 7

player_actions_begin        = player_action_voice
player_actions_end          = 9


voice_type_cry                = 1
voice_type_surrender          = 2
voice_type_comm_ready         = 3
voice_type_comm_present       = 4
voice_type_comm_fire          = 5
voice_type_comm_charge        = 6
voice_type_comm_advance       = 7
voice_type_comm_hold          = 8
voice_type_comm_fire_at_will  = 9
voice_type_comm_on_me         = 10
voice_type_comm_fall_back     = 11

voice_types_begin             = voice_type_cry
voice_types_end               = 12

music_type_start              = 1
music_type_stop               = 2
music_type_toggle_together    = 3

music_types_begin             = music_type_start
music_types_end               = music_type_toggle_together + 1

spyglass_type_start           = 1
spyglass_type_stop            = 2

colour_white      = 0
colour_red        = 1
colour_green      = 2
colour_blue       = 3
colour_yellow     = 4
colour_purple     = 5
colour_pink       = 6
colour_magenta    = 7
colour_invisible  = 8

## ORDERS
#Order types
mm_order_type_move      = 0
mm_order_type_formation = 1
mm_order_type_fire      = 2

#Move orders
mm_order_hold       = 0
mm_order_follow     = 1
mm_order_charge     = 2
mm_order_advance    = 3
mm_order_halt       = 4
mm_order_fallback   = 5
mm_order_retreat    = 6
mm_order_slow       = 7
mm_order_quick      = 8
#Formation orders
mm_order_line       = 0
mm_order_column     = 1
mm_order_square     = 2
mm_order_skirmish   = 3
mm_order_wheelleft  = 4
mm_order_wheelright = 5
mm_order_adjust     = 6
#Fire orders
mm_order_holdfire   = 0
mm_order_fireatwill = 1
mm_order_volley     = 2
mm_order_targetpos  = 3
mm_order_targetfree = 4
#Common
mm_order_none       = 10

#Division slots
slot_troop_no_begin_team1 = 0
slot_troop_no_begin_team2 = 10
slot_troops_in_division_begin_team1 = 20
slot_troops_in_division_begin_team2 = 30
slot_formation_order_begin_team1 = 40
slot_formation_order_begin_team2 = 50
slot_fire_order_begin_team1 = 60
slot_fire_order_begin_team2 = 70
slot_volley_state_begin_team1 = 80
slot_volley_state_begin_team2 = 90
slot_move_order_begin_team1 = 100
slot_move_order_begin_team2 = 110

#Agent Behaviour Types
bot_type_attacker   = 0
bot_type_defender   = 1
bot_type_skirmish   = 2

prop_effect_type_sound     = 1
prop_effect_type_particle  = 2
prop_effect_type_stop_all  = 3

prop_effect_types_begin  = prop_effect_type_sound
prop_effect_types_end    = 4

prop_effect_handle_start   = 1
prop_effect_handle_stop    = 2

prop_effect_handles_begin  = prop_effect_handle_start
prop_effect_handles_end    = 3

admin_chat_type_everyone   = 1
admin_chat_type_inter      = 2

admin_chat_types_begin  = admin_chat_type_everyone
admin_chat_types_end    = 3

debug_mode = 1

cannon_hit_effect_event_type_explosion = 1
cannon_hit_effect_event_type_ground = 2

cannon_hit_effect_event_types_begin = cannon_hit_effect_event_type_explosion
cannon_hit_effect_event_types_end = 3
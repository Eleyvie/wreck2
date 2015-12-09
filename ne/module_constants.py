from compiler import *

##############################################################
# These constants are used in various files.
# If you need to define a value that will be used in those files,
# just define it here rather than copying it across each file, so
# that it will be easy to change it if you need to.
##############################################################

PATCH_VERSION = 620
PATCH_SUBVERSION = 0

# NE building
## Finance slots - Jinnai
slot_finance_items                = 0
slot_finance_cattle_bought        = 1
slot_finance_taxes_collected      = 2
slot_finance_quest_rewards        = 3
slot_finance_center_upgrades      = 4
slot_finance_lost_in_combat       = 5
slot_finance_from_battles         = 6
slot_finance_wages                = 7
slot_finance_tournament           = 8
slot_finance_prisoners            = 9

finances_begin = 0
finances_end = 10


########################################################
##  SHARED SLOTS           #############################
########################################################

slot_subtype = 0 # Entity additional categorization, if necessary. Values are negative! Value >= 0 means the entity does not conform with NE unified slots system.

slot_temp_1 = 1
slot_temp_2 = 2
slot_temp_3 = 3

slot_tag_mask_0 = 4 # 4 fields of 64 bits each, for a max of 256 tags per entity. Not used currently.
slot_tag_mask_1 = 5
slot_tag_mask_2 = 6
slot_tag_mask_3 = 7


########################################################
##  ITEM SLOTS             #############################
########################################################

# Unified slot system [0..15]

slot_item_subtype                  = slot_subtype

sst_item_book_attribute   = -10
sst_item_book_skill       = -11
sst_item_book_reference   = -12
sst_item_book_proficiency = -13
sst_item_book_experience  = -14
sst_item_book_parameter   = -15
sst_item_book_culture     = -16
sst_item_book_family      = -17

sst_item_goods_food       = -20
sst_item_goods_drink      = -21
sst_item_goods_generic    = -22

slot_item_is_checked               = slot_temp_1 # Temporary slots used in food consumption calculations (including feasts).
slot_item_amount_available         = slot_temp_2

slot_item_popup_lines_begin        = 8 # Temporary slots used in item popup window extra lines generation. Require a range of 8 slots max, i.e. [8..15]

# Item additional properties [16..31]

SLOT_ITEM_PARAMS = 16

# Equipment skill bonusses
slot_equipment_skill               = SLOT_ITEM_PARAMS + 0 # Equipment skill modifiers
slot_equipment_skill_bonus         = SLOT_ITEM_PARAMS + 1 # Equipment skill modifiers
slot_equipment_feminine            = SLOT_ITEM_PARAMS + 2 # Equipment is dintinctly feminine, and men will get skill penalties for wearing it

# Foods
slot_item_food_bonus               = SLOT_ITEM_PARAMS + 0

# Books (new)
slot_item_book_param               = SLOT_ITEM_PARAMS + 0 # Parameter affected by book
slot_item_book_bonus               = SLOT_ITEM_PARAMS + 1 # Strength of effect
slot_item_book_min_req             = SLOT_ITEM_PARAMS + 2 # Required INT to read the book at all
slot_item_book_opt_req             = SLOT_ITEM_PARAMS + 3 # Required INT to read the book at 100% speed
slot_item_book_readtime            = SLOT_ITEM_PARAMS + 4 # Amount of time normally required to read this book
slot_item_book_abundance           = SLOT_ITEM_PARAMS + 5 # Percentile modifier to book abundance
slot_item_book_price               = SLOT_ITEM_PARAMS + 6 # Percentile modifier to book price
slot_item_book_author              = SLOT_ITEM_PARAMS + 7 # Author name offset in authors string array
slot_item_book_title               = SLOT_ITEM_PARAMS + 8 # Book title offset within title string array specified by book type and affected param

# Books (old) - planned for deprecation
slot_item_book_reading_progress    = SLOT_ITEM_PARAMS + 13
slot_item_book_read                = SLOT_ITEM_PARAMS + 14
slot_item_intelligence_requirement = SLOT_ITEM_PARAMS + 15


# Economy-related slots [32..47]

SLOT_ITEM_ECONOMY = 32

slot_item_urban_demand             = SLOT_ITEM_ECONOMY +  0 #consumer demand for a good in town, measured in abstract units. The more essential the item (ie, like grain) the higher the price
slot_item_rural_demand             = SLOT_ITEM_ECONOMY +  1 #consumer demand in villages, measured in abstract units
slot_item_desert_demand            = SLOT_ITEM_ECONOMY +  2 #consumer demand in villages, measured in abstract units

slot_item_production_slot          = SLOT_ITEM_ECONOMY +  3 
slot_item_production_string        = SLOT_ITEM_ECONOMY +  4 

slot_item_primary_raw_material     = SLOT_ITEM_ECONOMY +  5 
slot_item_is_raw_material_only_for = SLOT_ITEM_ECONOMY +  6 
slot_item_input_number             = SLOT_ITEM_ECONOMY +  7 #ie, how many items of inputs consumed per run
slot_item_base_price               = SLOT_ITEM_ECONOMY +  8 #taken from module_items
slot_item_output_per_run           = SLOT_ITEM_ECONOMY +  9 #number of items produced per run
slot_item_overhead_per_run         = SLOT_ITEM_ECONOMY + 10 #labor and overhead per run
slot_item_secondary_raw_material   = SLOT_ITEM_ECONOMY + 11 #in this case, the amount used is only one
slot_item_enterprise_building_cost = SLOT_ITEM_ECONOMY + 12 #enterprise building cost

## Multiplayer item slots [48..infinity]
#
#SLOT_ITEM_MULTIPLAYER = 48
#
#slot_item_multiplayer_item_class                      = SLOT_ITEM_MULTIPLAYER +  0 #temporary, can be moved to higher values
#slot_item_multiplayer_faction_price_multipliers_begin = SLOT_ITEM_MULTIPLAYER +  1 #reserve around 10 slots after this
#slot_item_multiplayer_availability_linked_list_begin  = SLOT_ITEM_MULTIPLAYER + 16 #temporary, can be moved to higher values


########################################################
##  AGENT SLOTS            #############################
########################################################

# Unified slot system [0..15]

slot_agent_subtype                 = slot_subtype # Not used yet.

slot_agent_is_alive_before_retreat = slot_temp_1 # Used in scripts "simulate_retreat" and "simulate_battle_with_agents_aux".
slot_agent_arena_team_set          = slot_temp_1 # Used in tournament triggers to assign agents to teams.
slot_agent_tournament_point        = slot_temp_1 # Used in script "end_tournament_fight".

# Mission-time agent slots [16..31]

SLOT_AGENT_GENERIC = 16

slot_agent_target_entry_point      = SLOT_AGENT_GENERIC +  0 # Used in script "siege_move_archers_to_archer_positions" and tutorial.
slot_agent_target_x_pos            = SLOT_AGENT_GENERIC +  1 # Used in script "cf_siege_assign_men_to_belfry".
slot_agent_target_y_pos            = SLOT_AGENT_GENERIC +  2 # Used in script "cf_siege_assign_men_to_belfry".
slot_agent_is_in_scripted_mode     = SLOT_AGENT_GENERIC +  3 # Used in script "siege_move_archers_to_archer_positions".
slot_agent_is_not_reinforcement    = SLOT_AGENT_GENERIC +  4 # Initialized in module_mission_templates.py and used in script "siege_move_archers_to_archer_positions".
slot_agent_map_overlay_id          = SLOT_AGENT_GENERIC +  5 # Used in script "update_agent_position_on_map" called from "prsnt_battle", to link agent and his dot on tactical map.
slot_agent_is_running_away         = SLOT_AGENT_GENERIC +  6 # Used in scripts "battle_tactic_init", "apply_effect_of_other_people_on_courage_scores", "apply_death_effect_on_courage_scores", "decide_run_away_or_not", "#script_count_mission_casualties_from_agents" and "neutral_behavior_in_fight".
slot_agent_courage_score           = SLOT_AGENT_GENERIC +  7 # Used in morale scripts and mission template triggers.
slot_agent_cur_animation           = SLOT_AGENT_GENERIC +  8 # Used in "wedding" mission template.

slot_agent_spearwall               = SLOT_AGENT_GENERIC + 11 # Used in spearwall code.
slot_agent_x                       = SLOT_AGENT_GENERIC + 12 # Used to track agent speed in spearwall code.
slot_agent_y                       = SLOT_AGENT_GENERIC + 13 
slot_agent_z                       = SLOT_AGENT_GENERIC + 14 
slot_agent_speed                   = SLOT_AGENT_GENERIC + 15 

#slot_agent_spawn_entry_point       = 8  # Used in tutorial to remember agent entry point and then move him back to it when he's no longer active. Apparently deprecated as there are operations for this kind of thing.
#slot_agent_target_prop_instance    = 9  # Used extensively in tutorial, mostly to track archer's chosen target.
#slot_agent_next_action_time        = 19 # Used in tutorial to decide when archers are going to fire at target again.
#slot_agent_in_duel_with            = 21 # Used in multiplayer only.
#slot_agent_duel_start_time         = 22 # Used in multiplayer only.


########################################################
##  FACTION SLOTS          #############################
########################################################

# Unified slot system [0..15]

slot_faction_subtype                      = slot_subtype # Not used at the moment

slot_faction_temp_slot                    = slot_temp_1

slot_faction_num_routed_agents            =  8 # Used to calculate faction for "routed troops" party through battle, based on what faction agents were the most prevalent.
slot_faction_player_alarm                 =  9 # Used to track alarms when player is near hostile towns and calculate player's infiltration chance.
slot_faction_last_mercenary_offer_time    = 10 # When player was last offered to become a merc for a lord, used to calculate if there will be another offer or not yet.

slot_faction_quick_battle_tier_1_infantry =  8 # overriding troop info for factions in quick start mode.
slot_faction_quick_battle_tier_2_infantry =  9
slot_faction_quick_battle_tier_1_archer   = 10
slot_faction_quick_battle_tier_2_archer   = 11
slot_faction_quick_battle_tier_1_cavalry  = 12
slot_faction_quick_battle_tier_2_cavalry  = 13


SLOT_FACTION_REFS = 16 # 32 slots reserved for faction references storage.

slot_faction_marshall         = SLOT_FACTION_REFS + 0
slot_faction_culture          = SLOT_FACTION_REFS + 1
slot_faction_leader           = SLOT_FACTION_REFS + 2
slot_faction_banner           = SLOT_FACTION_REFS + 3
slot_faction_adjective        = SLOT_FACTION_REFS + 4

slot_faction_tier_1_troop     = SLOT_FACTION_REFS + 5
slot_faction_tier_2_troop     = SLOT_FACTION_REFS + 6
slot_faction_tier_3_troop     = SLOT_FACTION_REFS + 7
slot_faction_tier_4_troop     = SLOT_FACTION_REFS + 8
slot_faction_tier_5_troop     = SLOT_FACTION_REFS + 9
slot_faction_noble_troop      = SLOT_FACTION_REFS + 10 # Jinnai

slot_faction_reinforcements_a = SLOT_FACTION_REFS + 11
slot_faction_reinforcements_b = SLOT_FACTION_REFS + 12
slot_faction_reinforcements_c = SLOT_FACTION_REFS + 13

slot_faction_deserter_troop              = SLOT_FACTION_REFS + 16
slot_faction_guard_troop                 = SLOT_FACTION_REFS + 17
slot_faction_messenger_troop             = SLOT_FACTION_REFS + 18
slot_faction_prison_guard_troop          = SLOT_FACTION_REFS + 19
slot_faction_castle_guard_troop          = SLOT_FACTION_REFS + 20

slot_faction_town_walker_male_troop      = SLOT_FACTION_REFS + 21
slot_faction_town_walker_female_troop    = SLOT_FACTION_REFS + 22
slot_faction_village_walker_male_troop   = SLOT_FACTION_REFS + 23
slot_faction_village_walker_female_troop = SLOT_FACTION_REFS + 24
slot_faction_town_spy_male_troop         = SLOT_FACTION_REFS + 25
slot_faction_town_spy_female_troop       = SLOT_FACTION_REFS + 26


SLOT_FACTION_POLITICS = 48 # 16 slots reserved for various faction states, diplomacy and political information.

slot_faction_state                                  = SLOT_FACTION_POLITICS + 0

sfs_active              = 0
sfs_defeated            = 1
sfs_inactive            = 2
sfs_inactive_rebellion  = 3
sfs_beginning_rebellion = 4

slot_faction_has_rebellion_chance                   = SLOT_FACTION_POLITICS + 1
slot_faction_instability                            = SLOT_FACTION_POLITICS + 2 # Last time measured

slot_faction_recognized_player                      = SLOT_FACTION_POLITICS + 3 # Used for diplomacy to track what kingdoms have recognized player as a fellow monarch.

slot_faction_truce_days_with_factions_begin         = SLOT_FACTION_POLITICS + 4 # moved from 120 as Spec Building B is 120
slot_faction_provocation_days_with_factions_begin   = SLOT_FACTION_POLITICS + 5
slot_faction_war_damage_inflicted_on_factions_begin = SLOT_FACTION_POLITICS + 6
slot_faction_sum_advice_about_factions_begin        = SLOT_FACTION_POLITICS + 7

slot_faction_morale_of_player_troops                = SLOT_FACTION_POLITICS + 15 # Faction modifier for player's party morale.


SLOT_FACTION_AI = 64 # 16 slots reserved for AI-related information storage.

slot_faction_ai_state                   = SLOT_FACTION_AI +  0

sfai_default                         = 0 #also defending
sfai_gathering_army                  = 1
sfai_attacking_center                = 2
sfai_raiding_village                 = 3
sfai_attacking_enemy_army            = 4
sfai_attacking_enemies_around_center = 5
sfai_feast                           = 6 #can be feast, wedding, or major tournament
#Social events are a generic aristocratic gathering. Tournaments take place if they are in a town, and hunts take place if they are at a castle.
#Weddings will take place at social events between betrothed couples if they have been engaged for at least a month, if the lady's guardian is the town lord, and if both bride and groom are present
sfai_nascent_rebellion               = 7


slot_faction_ai_object                  = SLOT_FACTION_AI +  1
slot_faction_ai_rationale               = SLOT_FACTION_AI +  2 # Currently unused, can be linked to strings generated from decision checklists
slot_faction_ai_offensive_max_followers = SLOT_FACTION_AI +  3

slot_faction_political_issue            = SLOT_FACTION_AI +  4 # Center or marshal appointment
slot_faction_political_issue_time       = SLOT_FACTION_AI +  5 # Now is used

slot_faction_last_attacked_center       = SLOT_FACTION_AI +  6 # Used in decision making
slot_faction_last_attacked_hours        = SLOT_FACTION_AI +  7 # Used in decision making
slot_faction_last_safe_hours            = SLOT_FACTION_AI +  8 # Used in decision making

slot_faction_last_feast_start_time      = SLOT_FACTION_AI +  9 # Used to determine if it's time to end current feast or start a new one.

slot_faction_ai_last_offensive_time     = SLOT_FACTION_AI + 10 # Set when an offensive concludes
slot_faction_last_offensive_concluded   = SLOT_FACTION_AI + 11 # Set when an offensive concludes

slot_faction_ai_last_rest_time          = SLOT_FACTION_AI + 12 # The last time that the faction has had default or feast AI -- this determines lords' dissatisfaction with the campaign. Set during faction_ai script
slot_faction_ai_current_state_started   = SLOT_FACTION_AI + 13 #

slot_faction_ai_last_decisive_event     = SLOT_FACTION_AI + 14 # Capture a fortress or declaration of war


SLOT_FACTION_STATS = 80 # 16 slots reserved for various statistical information storage.

slot_faction_number_of_parties = SLOT_FACTION_STATS + 0
slot_faction_num_armies        = SLOT_FACTION_STATS + 1
slot_faction_num_castles       = SLOT_FACTION_STATS + 2
slot_faction_num_towns         = SLOT_FACTION_STATS + 3


# FOR REFACTORING:

# Native Expansion Court system (to be expanded greatly). Currently fits into REFS slot range. Expected to receive it's own slot range later.

slot_faction_civil_adviser     = SLOT_FACTION_REFS + 27
slot_faction_financial_adviser = SLOT_FACTION_REFS + 28
slot_faction_logistics_adviser = SLOT_FACTION_REFS + 29
slot_faction_intel_adviser     = SLOT_FACTION_REFS + 30

# Native Expansion university upgrades system (to be refactored using a single bitmask).

SLOT_FACTION_UNIVERSITY = 96 # 16 slots reserved for university-related information storage. Expected to shrink to a couple slots after refactoring buildings arc is complete.

slot_faction_university       = SLOT_FACTION_UNIVERSITY + 0
slot_faction_univ_pathfinding = SLOT_FACTION_UNIVERSITY + 1
slot_faction_univ_spotting    = SLOT_FACTION_UNIVERSITY + 2
slot_faction_univ_surgery     = SLOT_FACTION_UNIVERSITY + 3
slot_faction_univ_wound       = SLOT_FACTION_UNIVERSITY + 4
slot_faction_univ_tactics     = SLOT_FACTION_UNIVERSITY + 5
slot_faction_univ_engineering = SLOT_FACTION_UNIVERSITY + 6
slot_faction_univ_belfry      = SLOT_FACTION_UNIVERSITY + 7
slot_faction_univ_repair      = SLOT_FACTION_UNIVERSITY + 8

university_upgrades_begin = slot_faction_univ_pathfinding
university_upgrades_end   = slot_faction_univ_repair + 1

slot_faction_capital          = SLOT_FACTION_UNIVERSITY + 10 # DEPRECATED. FOR REMOVAL. Some unused code in game_menus still relies on this.
slot_faction_capital_moved    = SLOT_FACTION_UNIVERSITY + 11 # DEPRECATED. FOR REMOVAL. Some unused code in game_menus still relies on this.

# Native Expansion elite troops (to be refactored using party slots).

SLOT_FACTION_ELITES = 112

slot_faction_special_troop_1      = SLOT_FACTION_ELITES +  0
slot_faction_special_troop_2      = SLOT_FACTION_ELITES +  1
slot_faction_special_troop_3      = SLOT_FACTION_ELITES +  2
slot_faction_special_troop_num_1a = SLOT_FACTION_ELITES +  3
slot_faction_special_troop_num_2a = SLOT_FACTION_ELITES +  4
slot_faction_special_troop_num_3a = SLOT_FACTION_ELITES +  5
slot_faction_special_troop_num_1b = SLOT_FACTION_ELITES +  6
slot_faction_special_troop_num_2b = SLOT_FACTION_ELITES +  7
slot_faction_special_troop_num_3b = SLOT_FACTION_ELITES +  8
slot_faction_special_building_a   = SLOT_FACTION_ELITES +  9
slot_faction_special_building_b   = SLOT_FACTION_ELITES + 10


    
########################################################
##  PARTY SLOTS            #############################
########################################################

slot_party_type        = 0  #spt_caravan, spt_town, spt_castle

spt_castle             = -20
spt_town               = -19
spt_village            = -18
spt_kingdom_caravan    = -17
spt_kingdom_hero_party = -16
spt_village_farmer     = -15
spt_ship               = -14
spt_cattle_herd        = -13
spt_bandit_lair        = -12

kingdom_party_types_begin = spt_kingdom_caravan
kingdom_party_types_end   = spt_kingdom_hero_party + 1

slot_party_temp_slot_1 = slot_temp_1 #right now used only within a single script, merchant_road_info_to_s42, to denote closed roads. Now also used in comparative scripts


SLOT_PARTY_SCENES = 16

slot_town_center         = SLOT_PARTY_SCENES +  0
slot_town_castle         = SLOT_PARTY_SCENES +  1
slot_town_prison         = SLOT_PARTY_SCENES +  2
slot_town_tavern         = SLOT_PARTY_SCENES +  3
slot_town_store          = SLOT_PARTY_SCENES +  4
slot_town_arena          = SLOT_PARTY_SCENES +  5
slot_town_alley          = SLOT_PARTY_SCENES +  6
slot_town_walls          = SLOT_PARTY_SCENES +  7
slot_castle_exterior     = slot_town_center

slot_town_tavernkeeper   = SLOT_PARTY_SCENES +  8
slot_town_weaponsmith    = SLOT_PARTY_SCENES +  9
slot_town_armorer        = SLOT_PARTY_SCENES + 10
slot_town_merchant       = SLOT_PARTY_SCENES + 11
slot_town_horse_merchant = SLOT_PARTY_SCENES + 12
slot_town_elder          = SLOT_PARTY_SCENES + 13


SLOT_PARTY_REFS = 32

slot_town_lord                          = SLOT_PARTY_REFS + 0
slot_cattle_driven_by_player            = slot_town_lord #hack

stl_unassigned          = -1
stl_reserved_for_player = -2
stl_rejected_by_player  = -3

slot_center_culture                     = SLOT_PARTY_REFS + 1
slot_center_original_faction            = SLOT_PARTY_REFS + 2
slot_center_ex_faction                  = SLOT_PARTY_REFS + 3
slot_center_faction_when_oath_renounced = SLOT_PARTY_REFS + 4 # Determines how difficult it will be to rejoin previous faction.

slot_village_bound_center               = SLOT_PARTY_REFS + 5
slot_village_market_town                = SLOT_PARTY_REFS + 6
slot_village_farmer_party               = SLOT_PARTY_REFS + 7
slot_party_home_center                  = SLOT_PARTY_REFS + 8 #Only use with caravans and villagers

slot_center_ransom_broker               = SLOT_PARTY_REFS + 11
slot_center_tavern_traveler             = SLOT_PARTY_REFS + 12
slot_center_traveler_info_faction       = SLOT_PARTY_REFS + 13
slot_center_tavern_bookseller           = SLOT_PARTY_REFS + 14
slot_center_tavern_minstrel             = SLOT_PARTY_REFS + 15


SLOT_PARTY_INFO = 48

slot_town_claimed_by_player     = SLOT_PARTY_INFO + 0
slot_center_siege_with_belfry   = SLOT_PARTY_INFO + 1
slot_center_last_taken_by_troop = SLOT_PARTY_INFO + 2
slot_center_player_relation     = SLOT_PARTY_INFO + 3

slot_town_horse_available       = SLOT_PARTY_INFO + 4
slot_center_has_bandits         = SLOT_PARTY_INFO + 5
slot_town_last_nearby_fire_time = SLOT_PARTY_INFO + 6 # Used in quest


SLOT_PARTY_AI = 64

slot_party_ai_state                      = SLOT_PARTY_AI + 0

spai_undefined                  = -1
spai_besieging_center           = 1
spai_patrolling_around_center   = 4
spai_raiding_around_center      = 5
spai_holding_center             = 7
spai_engaging_army              = 10
spai_accompanying_army          = 11
spai_screening_army             = 12
spai_trading_with_town          = 13
spai_retreating_to_center       = 14
spai_visiting_village           = 16 #same thing, I think. Recruiting differs from holding because NPC parties don't actually enter villages

slot_party_retreat_flag                  = SLOT_PARTY_AI + 1 # Denotes that the party is withdrawing from battle.
slot_party_ignore_player_until           = SLOT_PARTY_AI + 2
slot_party_ai_object                     = SLOT_PARTY_AI + 3
slot_party_ai_rationale                  = SLOT_PARTY_AI + 4 # Currently unused, but can be used to save a string explaining the lord's thinking
slot_party_ai_substate                   = SLOT_PARTY_AI + 5

slot_party_last_in_combat                = SLOT_PARTY_AI + 6 #used for AI
slot_party_last_in_home_center           = SLOT_PARTY_AI + 7 #used for AI
slot_party_leader_last_courted           = SLOT_PARTY_AI + 8 #used for AI
slot_party_last_in_any_center            = SLOT_PARTY_AI + 9 #used for AI

slot_party_commander_party               = SLOT_PARTY_AI + 10 # party will follow this party if set. #default -1   #Deprecate
slot_party_following_player              = SLOT_PARTY_AI + 11
slot_party_follow_player_until_time      = SLOT_PARTY_AI + 12
slot_party_dont_follow_player_until_time = SLOT_PARTY_AI + 13

slot_party_following_orders_of_troop     = SLOT_PARTY_AI + 14
slot_party_orders_type                   = SLOT_PARTY_AI + 15
slot_party_orders_object                 = SLOT_PARTY_AI + 16
slot_party_orders_time                   = SLOT_PARTY_AI + 17

slot_party_under_player_suggestion       = SLOT_PARTY_AI + 18 #move this up a bit


SLOT_PARTY_ECONOMY = 96

slot_center_accumulated_rents   = SLOT_PARTY_ECONOMY + 0 #collected automatically by NPC lords
slot_center_accumulated_tariffs = SLOT_PARTY_ECONOMY + 1 #collected automatically by NPC lords
slot_town_wealth                = SLOT_PARTY_ECONOMY + 2 #total amount of accumulated wealth in the center, pays for the garrison
slot_town_prosperity            = SLOT_PARTY_ECONOMY + 3 #affects the amount of wealth generated
slot_town_player_odds           = SLOT_PARTY_ECONOMY + 4


SLOT_PARTY_RECRUITMENT = 96

slot_center_npc_volunteer_troop_type   = SLOT_PARTY_RECRUITMENT + 10
slot_center_npc_volunteer_troop_amount = SLOT_PARTY_RECRUITMENT + 11

slot_center_mercenary_troop_type       = SLOT_PARTY_RECRUITMENT + 12
slot_center_mercenary_troop_amount     = SLOT_PARTY_RECRUITMENT + 13
slot_center_volunteer_troop_type       = SLOT_PARTY_RECRUITMENT + 14
slot_center_volunteer_troop_amount     = SLOT_PARTY_RECRUITMENT + 15


SLOT_PARTY_VILLAGE = 112

slot_village_state                       = SLOT_PARTY_VILLAGE + 0# svs_normal, svs_being_raided, svs_looted, svs_recovering, svs_deserted

svs_normal                      = 0
svs_being_raided                = 1
svs_looted                      = 2
svs_recovering                  = 3
svs_deserted                    = 4
svs_under_siege                 = 5

slot_village_raided_by                   = SLOT_PARTY_VILLAGE + 1
slot_village_raid_progress               = SLOT_PARTY_VILLAGE + 2
slot_village_recover_progress            = SLOT_PARTY_VILLAGE + 3
slot_village_smoke_added                 = SLOT_PARTY_VILLAGE + 4

slot_village_infested_by_bandits         = SLOT_PARTY_VILLAGE + 5
slot_village_infested_by_wedding         = SLOT_PARTY_VILLAGE + 6

slot_village_player_can_not_steal_cattle = SLOT_PARTY_VILLAGE + 7


SLOT_PARTY_TOWN_ARENA = 112

slot_town_has_tournament           = SLOT_PARTY_TOWN_ARENA +  0
slot_town_tournament_max_teams     = SLOT_PARTY_TOWN_ARENA +  1
slot_town_tournament_max_team_size = SLOT_PARTY_TOWN_ARENA +  2

slot_town_arena_melee_mission_tpl  = SLOT_PARTY_TOWN_ARENA +  3
slot_town_arena_torny_mission_tpl  = SLOT_PARTY_TOWN_ARENA +  4
slot_town_arena_melee_1_num_teams  = SLOT_PARTY_TOWN_ARENA +  5
slot_town_arena_melee_1_team_size  = SLOT_PARTY_TOWN_ARENA +  6
slot_town_arena_melee_2_num_teams  = SLOT_PARTY_TOWN_ARENA +  7
slot_town_arena_melee_2_team_size  = SLOT_PARTY_TOWN_ARENA +  8
slot_town_arena_melee_3_num_teams  = SLOT_PARTY_TOWN_ARENA +  9
slot_town_arena_melee_3_team_size  = SLOT_PARTY_TOWN_ARENA + 10
slot_town_arena_melee_cur_tier     = SLOT_PARTY_TOWN_ARENA + 11


SLOT_PARTY_BUILDINGS = 128 # For major refactoring.

slot_center_current_improvement    = SLOT_PARTY_BUILDINGS +  0
slot_center_improvement_end_hour   = SLOT_PARTY_BUILDINGS +  1

slot_center_university_placeholder = SLOT_PARTY_BUILDINGS +  2

slot_center_has_manor              = SLOT_PARTY_BUILDINGS +  3 # village
slot_center_has_fish_pond          = SLOT_PARTY_BUILDINGS +  4 # village
slot_center_has_watch_tower        = SLOT_PARTY_BUILDINGS +  5 # village
slot_center_has_school             = SLOT_PARTY_BUILDINGS +  6 # village
slot_center_has_palisade           = SLOT_PARTY_BUILDINGS +  7 # village
slot_center_has_horse_ranch        = SLOT_PARTY_BUILDINGS +  8 # village
slot_center_has_distillery         = SLOT_PARTY_BUILDINGS +  9 # village
slot_center_has_caltrops           = SLOT_PARTY_BUILDINGS + 10 # village
slot_center_has_cattle_ranch       = SLOT_PARTY_BUILDINGS + 11 # village
slot_center_has_messenger_post     = SLOT_PARTY_BUILDINGS + 12 # village, town, castle
slot_center_has_bugged_building    = SLOT_PARTY_BUILDINGS + 13 #          town, castle BUG: this was called slot_center_has_prisoner_tower and overridden a few lines below, resulting in duplicate listing
slot_center_has_caravan_escort     = SLOT_PARTY_BUILDINGS + 13 #          town
slot_center_has_bookstore          = SLOT_PARTY_BUILDINGS + 14 #          town
slot_center_has_festival_square    = SLOT_PARTY_BUILDINGS + 15 #          town
slot_center_has_blacksmith         = SLOT_PARTY_BUILDINGS + 16 #          town, castle
slot_center_has_prisoner_tower     = SLOT_PARTY_BUILDINGS + 17 #          town, castle
slot_center_has_cathedral          = SLOT_PARTY_BUILDINGS + 18 #          town - SPECIAL: Swadian Elite Building (Cathedral)
slot_center_has_ivory_temple       = SLOT_PARTY_BUILDINGS + 19 #          town - SPECIAL: Vaegir Elite Building (Ivory Temple)
slot_center_has_palace             = SLOT_PARTY_BUILDINGS + 20 #          town - SPECIAL: Khergit Elite Building (Palace)
slot_center_has_hall               = SLOT_PARTY_BUILDINGS + 21 #          town - SPECIAL: Nord Elite Building (Halls of Glory)
slot_center_has_chambers           = SLOT_PARTY_BUILDINGS + 22 #          town - SPECIAL: Rhodok Elite Building (Council Chambers)
slot_center_has_baths              = SLOT_PARTY_BUILDINGS + 23 #          town - SPECIAL: Sarranid Elite Building (House of Swords)

village_improvements_begin = slot_center_has_manor
village_improvements_end   = slot_center_has_cattle_ranch + 1

walled_center_improvements_begin             = slot_center_has_messenger_post
walled_center_improvements_end               = slot_center_has_prisoner_tower + 1
walled_center_improvements_and_specials_end  = slot_center_has_baths + 1


SLOT_PARTY_ENTERPRISE = 128 # Combined with buildings for now.

slot_center_player_enterprise                     = SLOT_PARTY_ENTERPRISE + 25 #noted with the item produced
slot_center_player_enterprise_production_order    = SLOT_PARTY_ENTERPRISE + 26
slot_center_player_enterprise_consumption_order   = SLOT_PARTY_ENTERPRISE + 27 #not used
slot_center_player_enterprise_days_until_complete = SLOT_PARTY_ENTERPRISE + 28 #Used instead

slot_center_player_enterprise_balance             = SLOT_PARTY_ENTERPRISE + 29 #not used
slot_center_player_enterprise_input_price         = SLOT_PARTY_ENTERPRISE + 30 #not used
slot_center_player_enterprise_output_price        = SLOT_PARTY_ENTERPRISE + 31 #not used


SLOT_PARTY_LOOT = 160

num_party_loot_slots    = 5

slot_party_next_looted_item_slot  = SLOT_PARTY_LOOT + 15

slot_party_looted_item_1          = SLOT_PARTY_LOOT + 0
slot_party_looted_item_2          = SLOT_PARTY_LOOT + 1
slot_party_looted_item_3          = SLOT_PARTY_LOOT + 2
slot_party_looted_item_4          = SLOT_PARTY_LOOT + 3
slot_party_looted_item_5          = SLOT_PARTY_LOOT + 4
slot_party_looted_item_1_modifier = SLOT_PARTY_LOOT + 5
slot_party_looted_item_2_modifier = SLOT_PARTY_LOOT + 6
slot_party_looted_item_3_modifier = SLOT_PARTY_LOOT + 7
slot_party_looted_item_4_modifier = SLOT_PARTY_LOOT + 8
slot_party_looted_item_5_modifier = SLOT_PARTY_LOOT + 9


SLOT_PARTY_WALKERS = 176 # For deprecation.

slot_center_walker_0_troop = SLOT_PARTY_WALKERS + 0
slot_center_walker_1_troop = SLOT_PARTY_WALKERS + 1
slot_center_walker_2_troop = SLOT_PARTY_WALKERS + 2
slot_center_walker_3_troop = SLOT_PARTY_WALKERS + 3
slot_center_walker_4_troop = SLOT_PARTY_WALKERS + 4
slot_center_walker_5_troop = SLOT_PARTY_WALKERS + 5
slot_center_walker_6_troop = SLOT_PARTY_WALKERS + 6
slot_center_walker_7_troop = SLOT_PARTY_WALKERS + 7
slot_center_walker_8_troop = SLOT_PARTY_WALKERS + 8
slot_center_walker_9_troop = SLOT_PARTY_WALKERS + 9

slot_center_walker_0_dna   = SLOT_PARTY_WALKERS + 10
slot_center_walker_1_dna   = SLOT_PARTY_WALKERS + 11
slot_center_walker_2_dna   = SLOT_PARTY_WALKERS + 12
slot_center_walker_3_dna   = SLOT_PARTY_WALKERS + 13
slot_center_walker_4_dna   = SLOT_PARTY_WALKERS + 14
slot_center_walker_5_dna   = SLOT_PARTY_WALKERS + 15
slot_center_walker_6_dna   = SLOT_PARTY_WALKERS + 16
slot_center_walker_7_dna   = SLOT_PARTY_WALKERS + 17
slot_center_walker_8_dna   = SLOT_PARTY_WALKERS + 18
slot_center_walker_9_dna   = SLOT_PARTY_WALKERS + 19

slot_center_walker_0_type  = SLOT_PARTY_WALKERS + 20
slot_center_walker_1_type  = SLOT_PARTY_WALKERS + 21
slot_center_walker_2_type  = SLOT_PARTY_WALKERS + 22
slot_center_walker_3_type  = SLOT_PARTY_WALKERS + 23
slot_center_walker_4_type  = SLOT_PARTY_WALKERS + 24
slot_center_walker_5_type  = SLOT_PARTY_WALKERS + 25
slot_center_walker_6_type  = SLOT_PARTY_WALKERS + 26
slot_center_walker_7_type  = SLOT_PARTY_WALKERS + 27
slot_center_walker_8_type  = SLOT_PARTY_WALKERS + 28
slot_center_walker_9_type  = SLOT_PARTY_WALKERS + 29

walkert_default            = 0
walkert_needs_money        = 1
walkert_needs_money_helped = 2
walkert_spy                = 3


SLOT_PARTY_COMBAT = 192

slot_center_last_player_alarm_hour             = SLOT_PARTY_COMBAT +  0

slot_party_last_toll_paid_hours                = SLOT_PARTY_COMBAT +  1
slot_party_food_store                          = SLOT_PARTY_COMBAT +  2 #used for sieges
slot_center_is_besieged_by                     = SLOT_PARTY_COMBAT +  3 #used for sieges
slot_center_last_spotted_enemy                 = SLOT_PARTY_COMBAT +  4

slot_party_cached_strength                     = SLOT_PARTY_COMBAT +  5
slot_party_nearby_friend_strength              = SLOT_PARTY_COMBAT +  6
slot_party_nearby_enemy_strength               = SLOT_PARTY_COMBAT +  7
slot_party_follower_strength                   = SLOT_PARTY_COMBAT +  8

slot_party_follow_me                           = SLOT_PARTY_COMBAT +  9
slot_center_siege_begin_hours                  = SLOT_PARTY_COMBAT + 10 #used for sieges
slot_center_siege_hardness                     = SLOT_PARTY_COMBAT + 11

slot_center_sortie_strength                    = SLOT_PARTY_COMBAT + 12
slot_center_sortie_enemy_strength              = SLOT_PARTY_COMBAT + 13

slot_center_last_reconnoitered_by_faction_time = SLOT_PARTY_COMBAT + 16 # Reserve ~8 slot range after this (depends on number of factions).


SLOT_PARTY_TRADE = 240

slot_party_last_traded_center     = SLOT_PARTY_TRADE +  0

slot_town_trade_route_1           = SLOT_PARTY_TRADE +  1
slot_town_trade_route_2           = SLOT_PARTY_TRADE +  2
slot_town_trade_route_3           = SLOT_PARTY_TRADE +  3
slot_town_trade_route_4           = SLOT_PARTY_TRADE +  4
slot_town_trade_route_5           = SLOT_PARTY_TRADE +  5
slot_town_trade_route_6           = SLOT_PARTY_TRADE +  6
slot_town_trade_route_7           = SLOT_PARTY_TRADE +  7
slot_town_trade_route_8           = SLOT_PARTY_TRADE +  8
slot_town_trade_route_9           = SLOT_PARTY_TRADE +  9
slot_town_trade_route_10          = SLOT_PARTY_TRADE + 10
slot_town_trade_route_11          = SLOT_PARTY_TRADE + 11
slot_town_trade_route_12          = SLOT_PARTY_TRADE + 12
slot_town_trade_route_13          = SLOT_PARTY_TRADE + 13
slot_town_trade_route_14          = SLOT_PARTY_TRADE + 14
slot_town_trade_route_15          = SLOT_PARTY_TRADE + 15

slot_town_trade_routes_begin      = slot_town_trade_route_1
slot_town_trade_routes_end        = slot_town_trade_route_15 + 1


SLOT_PARTY_INDUSTRY = 256

#These affect production but in some cases also demand, so it is perhaps easier to itemize them than to have separate 
slot_village_number_of_cattle          = SLOT_PARTY_INDUSTRY +  0
slot_center_head_cattle                = SLOT_PARTY_INDUSTRY +  1 #dried meat, cheese, hides, butter
slot_center_head_sheep                 = SLOT_PARTY_INDUSTRY +  2 #sausages, wool
slot_center_head_horses                = SLOT_PARTY_INDUSTRY +  3 #horses can be a trade item used in tracking ,but which are never offered for sale

slot_center_acres_pasture              = SLOT_PARTY_INDUSTRY +  4
slot_production_sources_begin          = SLOT_PARTY_INDUSTRY +  5
slot_production_sources_end            = SLOT_PARTY_INDUSTRY +  6
slot_center_acres_grain                = SLOT_PARTY_INDUSTRY +  7 #grain
slot_center_acres_olives               = SLOT_PARTY_INDUSTRY +  8 #nothing for now
slot_center_acres_vineyard             = SLOT_PARTY_INDUSTRY +  9 #fruit
slot_center_acres_flax                 = SLOT_PARTY_INDUSTRY + 10 #flax - can be used for sailcloth
slot_center_acres_dates                = SLOT_PARTY_INDUSTRY + 11 #dates

slot_center_fishing_fleet              = SLOT_PARTY_INDUSTRY + 12 #smoked fish
slot_center_salt_pans                  = SLOT_PARTY_INDUSTRY + 13 #salt

slot_center_apiaries                   = SLOT_PARTY_INDUSTRY + 14 #honey
slot_center_silk_farms                 = SLOT_PARTY_INDUSTRY + 15 #silk
slot_center_kirmiz_farms               = SLOT_PARTY_INDUSTRY + 16 #dyes

slot_center_iron_deposits              = SLOT_PARTY_INDUSTRY + 17 #iron
slot_center_fur_traps                  = SLOT_PARTY_INDUSTRY + 18 #furs
#timber
#pitch

slot_center_mills                      = SLOT_PARTY_INDUSTRY + 19 #bread
slot_center_breweries                  = SLOT_PARTY_INDUSTRY + 20 #ale
slot_center_wine_presses               = SLOT_PARTY_INDUSTRY + 21 #wine
slot_center_olive_presses              = SLOT_PARTY_INDUSTRY + 22 #oil

slot_center_linen_looms                = SLOT_PARTY_INDUSTRY + 23 #linen
slot_center_silk_looms                 = SLOT_PARTY_INDUSTRY + 24 #velvet
slot_center_wool_looms                 = SLOT_PARTY_INDUSTRY + 25 #wool cloth

slot_center_pottery_kilns              = SLOT_PARTY_INDUSTRY + 26 #pottery
slot_center_smithies                   = SLOT_PARTY_INDUSTRY + 27 #tools
slot_center_tanneries                  = SLOT_PARTY_INDUSTRY + 28 #leatherwork
slot_center_shipyards                  = SLOT_PARTY_INDUSTRY + 29 #naval stores - uses timber, pitch, and linen

slot_center_household_gardens          = SLOT_PARTY_INDUSTRY + 30 #cabbages

#all spice comes overland to Tulga
#all dyes come by sea to Jelkala

#chicken and pork are perishable and non-tradeable, and based on grain production
#timber and pitch if we ever have a shipbuilding industry
#limestone and timber for mortar, if we allow building

slot_town_trade_good_prices_begin      = 288 # Reserve a number of slots depending on number of trade goods. Currently 64 slots reserved.
slot_town_trade_good_productions_begin = 352 # Reserve a number of slots depending on number of trade goods. Currently 64 slots reserved.

num_trade_goods = itm.goods_end - itm.goods_begin - 1

SLOT_PARTY_FREE_SLOTS_START_AT = 416


########################################################
##  SCENE SLOTS            #############################
########################################################

slot_scene_subtype            = slot_subtype # Not used.
slot_scene_visited            = slot_temp_1 # Set in lots of places, but not used anywhere.

slot_scene_belfry_props_begin = 16



########################################################
##  TROOP SLOTS            #############################
########################################################

slot_troop_occupation          = 2  # 0 = free, 1 = merchant

slto_inactive           = 0 # for companions at the beginning of the game
#slto_merchant           = 1
slto_kingdom_hero       = 2
slto_player_companion   = 5 # This is specifically for companions in the employ of the player -- ie, in the party, or on a mission
slto_kingdom_lady       = 6 # Usually inactive (Calradia is a traditional place). However, can be made potentially active if active_npcs are expanded to include ladies
slto_kingdom_seneschal  = 7
slto_robber_knight      = 8
slto_inactive_pretender = 9
slto_retirement      = 11

slot_troop_tmp1 = 162
slot_troop_tmp2 = 163
slot_troop_tmp3 = 164

slot_troop_temp_slot           = 46


SLOT_TROOP_LOCATION = 0

slot_troop_location_hours  = 160 # Time when info was updated
slot_troop_location_center = 158 # When updating info about troop location, contains center troop is inside or nearby. Zero means unknown.
slot_troop_location_status = 159 # How to interpret center slot: inside, nearby, imprisoned in or unknown.

tls_unknown    = 0
tls_garrisoned = 1
tls_nearby     = 2
tls_imprisoned = 3

slot_troop_prisoner_of_party   = 8  # important for heroes only
slot_troop_present_at_event    = 9
slot_troop_leaded_party         = 10 # important for kingdom heroes only
slot_troop_cur_center           = 12 # important for royal family members only (non-kingdom heroes)


SLOT_TROOP_REFS = 0

slot_troop_banner_scene_prop    = 13 # important for kingdom heroes and player only
slot_troop_original_faction     = 14 # for pretenders

slot_troop_first_encountered          = 59 # Assumed to always be a town
slot_troop_home                       = 60 # Any center

slot_troop_town_with_contacts  = 67
slot_troop_town_contact_type   = 68 #1 are nobles, 2 are commons


SLOT_TROOP_INFO = 0

slot_troop_state               = 3  
slot_troop_last_talk_time      = 4
slot_troop_met                 = 5 #i also use this for the courtship state -- may become cumbersome
slot_troop_renown              = 7
slot_troop_wealth               = 11 # important for kingdom heroes only
slot_troop_controversy                     = 150 #Determines whether or not a troop is likely to receive fief or marshalship

slot_troop_age                 =  18
slot_troop_age_appearance      =  19

slot_troop_spawned_before      = 28 # Used at script "create_kingdom_hero_party{_dk}" to add extra troops to lords at first spawn.

slot_lord_reputation_type               = 52

#lord reputation type, for commentaries
#"Martial" will be twice as common as the other types
lrep_none           = 0 
lrep_martial        = 1 #chivalrous but not terribly empathetic or introspective, - eg Richard Lionheart, your average 14th century French baron
lrep_quarrelsome    = 2 #spiteful, cynical, a bit paranoid, possibly hotheaded - eg Robert Graves' Tiberius, some of Charles VI's uncles
lrep_selfrighteous  = 3 #coldblooded, moralizing, often cruel - eg William the Conqueror, Timur, Octavian, Aurangzeb (although he is arguably upstanding instead, particularly after his accession)
lrep_cunning        = 4 #coldblooded, pragmatic, amoral - eg Louis XI, Guiscard, Akbar Khan, Abd al-Aziz Ibn Saud
lrep_debauched      = 5 #spiteful, amoral, sadistic - eg Caligula, Tuchman's Charles of Navarre
lrep_goodnatured    = 6 #chivalrous, benevolent, perhaps a little too decent to be a good warlord - eg Hussein ibn Ali. Few well-known historical examples maybe. because many lack the drive to rise to faction leadership. Ranjit Singh has aspects
lrep_upstanding     = 7 #moralizing, benevolent, pragmatic, - eg Bernard Cornwell's Alfred, Charlemagne, Salah al-Din, Sher Shah Suri

lrep_roguish        = 8 #used for commons, specifically ex-companions. Tries to live life as a lord to the full
lrep_benefactor     = 9 #used for commons, specifically ex-companions. Tries to improve lot of folks on land
lrep_custodian      = 10 #used for commons, specifically ex-companions. Tries to maximize fief's earning potential

#lreps specific to dependent noblewomen
lrep_conventional    = 21 #Charlotte York in SATC seasons 1-2, probably most medieval aristocrats
lrep_adventurous     = 22 #Tomboyish. However, this basically means that she likes to travel and hunt, and perhaps yearn for wider adventures. However, medieval noblewomen who fight are rare, and those that attempt to live independently of a man are rarer still, and best represented by pre-scripted individuals like companions
lrep_otherworldly    = 23 #Prone to mysticism, romantic. 
lrep_ambitious       = 24 #Lady Macbeth
lrep_moralist        = 25 #Equivalent of upstanding or benefactor -- takes nobless oblige, and her traditional role as repository of morality, very seriously. Based loosely on Christine de Pisa 

#a more complicated system of reputation could include the following...

#successful vs unlucky -- basic gauge of success
#daring vs cautious -- maybe not necessary
#honorable/pious/ideological vs unscrupulous -- character's adherance to an external code of conduct. Fails to capture complexity of people like Aurangzeb, maybe, but good for NPCs
    #(visionary/altruist and orthodox/unorthodox could be a subset of the above, or the specific external code could be another tag)
#generous/loyal vs manipulative/exploitative -- character's sense of duty to specific individuals, based on their relationship. Affects loyalty of troops, etc
#merciful vs cruel/ruthless/sociopathic -- character's general sense of compassion. Sher Shah is example of unscrupulous and merciful (the latter to a degree).
#dignified vs unconventional -- character's adherance to social conventions. Very important, given the times

slot_troop_home_speech_delivered = 78 #only for companions
slot_troop_discussed_rebellion   = 78 #only for pretenders

slot_troop_met_previously        = 80
slot_troop_turned_down_twice     = 81
slot_troop_playerparty_history   = 82 # Last event that happened to NPC in player's party

pp_history_scattered         = 1
pp_history_dismissed         = 2
pp_history_quit              = 3
pp_history_indeterminate     = 4

slot_troop_playerparty_history_string   = 83 # Actually faction reference for when NPC has been scattered due to military defeat.
slot_troop_return_renown        = 84 # Amount of player renown required for NPC to return to party after (s)he quit due to grievances.

slot_troop_payment_request                 = 141 # Amount of money NPC requests for joining
slot_troop_honor_req = 301
slot_troop_renown_req = 302


SLOT_TROOP_AI = 0

slot_troop_promised_fief       = 47

slot_troop_set_decision_seed       = 48 #Does not change
slot_troop_temp_decision_seed      = 49 #Resets at recalculate_ai
slot_troop_recruitment_random      = 50 #used in a number of different places in the intrigue procedures to overcome intermediate hurdles, although not for the final calculation, might be replaced at some point by the global decision seed
#Decision seeds can be used so that some randomness can be added to NPC decisions, without allowing the player to spam the NPC with suggestions
#The temp decision seed is reset 24 to 48 hours after the NPC last spoke to the player, while the set seed only changes in special occasions
#The single seed is used with varying modula to give high/low outcomes on different issues, without using a separate slot for each issue

slot_troop_intrigue_impatience = 51

slot_troop_morality_type = 62
slot_troop_morality_state       = 61
slot_troop_morality_value = 63
slot_troop_2ary_morality_type  = 64
slot_troop_2ary_morality_state = 65
slot_troop_2ary_morality_value = 66

tms_no_problem         = 0
tms_acknowledged       = 1
tms_dismissed          = 2

tmt_aristocratic = 1
tmt_egalitarian = 2
tmt_humanitarian = 3
tmt_honest = 4
tmt_pious = 5

slot_troop_morality_penalties =  69 ### accumulated grievances from morality conflicts

slot_troop_personalityclash_object     = 71 # (0 - they have no problem, 1 - they have a problem)
slot_troop_personalityclash_state    = 72 # 1 = pclash_penalty_to_self, 2 = pclash_penalty_to_other, 3 = pclash_penalty_to_other,

pclash_penalty_to_self  = 1
pclash_penalty_to_other = 2
pclash_penalty_to_both  = 3

#(a string)
slot_troop_personalityclash2_object   = 73
slot_troop_personalityclash2_state    = 74

slot_troop_personalitymatch_object   =  75
slot_troop_personalitymatch_state   =  76

slot_troop_personalityclash_penalties = 77 ### accumulated grievances from personality clash
slot_troop_personalityclash_penalties = 77 ### accumulated grievances from personality clash


SLOT_TROOP_FAMILY = 0

slot_troop_spouse              = 30
slot_troop_father              = 31
slot_troop_mother              = 32
slot_troop_guardian            = 33 #Usually siblings are identified by a common parent.This is used for brothers if the father is not an active npc. At some point we might introduce geneologies
slot_troop_betrothed           = 34 #Obviously superseded once slot_troop_spouse is filled
#other relations are derived from one's parents 
#slot_troop_daughter            = 33
#slot_troop_son                 = 34
#slot_troop_sibling             = 35
slot_troop_love_interest_1     = 35 #each unmarried lord has three love interests
slot_troop_love_interest_2     = 36
slot_troop_love_interest_3     = 37
slot_troop_love_interests_end  = 38
#ways to court -- discuss a book, commission/compose a poem, present a gift, recount your exploits, fulfil a specific quest, appear at a tournament
#preferences for women - (conventional - father's friends)
slot_lady_no_messages                          = 37
slot_lady_last_suitor                          = 38
slot_lord_granted_courtship_permission      = 38

slot_troop_courtship_state     = 5 #2 professed admiration, 3 agreed to seek a marriage, 4 ended relationship
slot_troop_betrothal_time                   = 39 #used in scheduling the wedding

slot_lady_used_tournament = 40 # Set to 1 when player has dedicated his tournament success to lady, reducing effectiveness of all later attempts to do so.

#courtship slots
slot_lady_courtship_heroic_recited         = 74
slot_lady_courtship_allegoric_recited     = 75
slot_lady_courtship_comic_recited         = 76
slot_lady_courtship_mystic_recited         = 77
slot_lady_courtship_tragic_recited         = 78


SLOT_TROOP_QUESTS = 0

slot_troop_does_not_give_quest = 20 # 1/0 flag
slot_troop_player_debt         = 21
slot_troop_player_relation     = 22

slot_troop_last_quest          = 24
slot_troop_last_quest_betrayed = 25
slot_troop_last_persuasion_time= 26

#slot_troop_last_comment_time   = 27


SLOT_TROOP_NOTES = 0

slot_troop_last_comment_slot   = 29 # For troop notes
slot_troop_current_rumor       = 45


SLOT_TROOP_DIPLOMACY = 0

slot_lord_recruitment_argument        = 53 # the last argument proposed by the player to the lord
slot_lord_recruitment_candidate       = 54 # the last candidate proposed by the player to the lord

slot_troop_change_to_faction          = 55

slot_troop_kingsupport_state            = 142
slot_troop_kingsupport_argument            = 143
slot_troop_kingsupport_opponent            = 144
slot_troop_kingsupport_objection_state  = 145 #0, default, 1, needs to voice, 2, has voiced

slot_troop_days_on_mission                = 150
slot_troop_current_mission                = 151
slot_troop_mission_object               = 152

npc_mission_kingsupport                    = 1
npc_mission_gather_intel                = 2
npc_mission_peace_request               = 3
npc_mission_pledge_vassal               = 4
npc_mission_seek_recognition            = 5
npc_mission_test_waters                 = 6
npc_mission_non_aggression              = 7
npc_mission_rejoin_when_possible        = 8

slot_troop_recent_offense_type                = 151 #failure to join army, failure to support colleague

tro_failed_to_join_army                    = 1
tro_failed_to_support_colleague            = 2

slot_troop_recent_offense_object           = 152 #to whom it happened
slot_troop_recent_offense_time             = 153
slot_troop_stance_on_faction_issue         = 154 #when it happened

slot_troop_relations_begin                = 0 # This creates an array for relations between troops. TODO: refactor this properly.
troop_slots_reserved_for_relations_start        = 165 # This is based on id_troops, and might change. Actually it's closer to 333 ATM. TODO: refactor this properly

slot_troop_discussed_rebellion = 170
slot_troop_support_base = 171

slot_troop_no_rebellion = 303 # NE code. For lords that are nurturing ideas for rebellion.
slot_troop_requested_duel = 304 # NE code. For lords who have requested a duel with player.
slot_troop_requested_war = 305 # NE code. Used to ask kings to join player in a war.


SLOT_TROOP_CBANNER = 0 # Deprecated, for removal.

slot_troop_custom_banner_bg_color_1      = 85
slot_troop_custom_banner_bg_color_2      = 86
slot_troop_custom_banner_charge_color_1  = 87
slot_troop_custom_banner_charge_color_2  = 88
slot_troop_custom_banner_charge_color_3  = 89
slot_troop_custom_banner_charge_color_4  = 90
slot_troop_custom_banner_bg_type         = 91
slot_troop_custom_banner_charge_type_1   = 92
slot_troop_custom_banner_charge_type_2   = 93
slot_troop_custom_banner_charge_type_3   = 94
slot_troop_custom_banner_charge_type_4   = 95
slot_troop_custom_banner_flag_type       = 96
slot_troop_custom_banner_num_charges     = 97
slot_troop_custom_banner_positioning     = 98
slot_troop_custom_banner_map_flag_type   = 99


SLOT_TROOP_CONVERSATION = 0 # Their relative order is important due to current code structure.

slot_troop_intro                         = 101
slot_troop_intro_response_1             = 102
slot_troop_intro_response_2             = 103
slot_troop_backstory_a                     = 104
slot_troop_backstory_b                     = 105
slot_troop_backstory_c                     = 106
slot_troop_backstory_delayed             = 107
slot_troop_backstory_response_1         = 108
slot_troop_backstory_response_2         = 109
slot_troop_signup                       = 110
slot_troop_signup_2                     = 111
slot_troop_signup_response_1             = 112
slot_troop_signup_response_2             = 113
slot_troop_mentions_payment             = 114 #Not actually used
slot_troop_payment_response             = 115 #Not actually used
slot_troop_morality_speech               = 116
slot_troop_2ary_morality_speech         = 117
slot_troop_personalityclash_speech         = 118
slot_troop_personalityclash_speech_b     = 119
slot_troop_personalityclash2_speech     = 120
slot_troop_personalityclash2_speech_b     = 121
slot_troop_personalitymatch_speech         = 122
slot_troop_personalitymatch_speech_b     = 123
slot_troop_retirement_speech             = 124
slot_troop_rehire_speech                 = 125
slot_troop_home_intro                   = 126
slot_troop_home_description                = 127
slot_troop_home_description_2             = 128
slot_troop_home_recap                     = 129
slot_troop_honorific                       = 130
slot_troop_kingsupport_string_1            = 131
slot_troop_kingsupport_string_2            = 132
slot_troop_kingsupport_string_2a        = 133
slot_troop_kingsupport_string_2b        = 134
slot_troop_kingsupport_string_3            = 135
slot_troop_kingsupport_objection_string    = 136
slot_troop_intel_gathering_string        = 137
slot_troop_fief_acceptance_string        = 138
slot_troop_woman_to_woman_string        = 139
slot_troop_turn_against_string            = 140

slot_troop_strings_end                     = 141


SLOT_TROOP_BATTLE = 0

slot_troop_player_routed_agents                 = 146 # Number of routed agents from player party after battle ends.
slot_troop_ally_routed_agents                   = 147 # From allied parties.
slot_troop_enemy_routed_agents                  = 148 # From enemy parties.

slot_troop_mission_participation        = 149 # Used for lords during prison break

mp_unaware                              = 0 
mp_stay_out                             = 1 
mp_prison_break_fight                   = 2 
mp_prison_break_stand_back              = 3 
mp_prison_break_escaped                 = 4 
mp_prison_break_caught                  = 5 

slot_troop_will_join_prison_break      = 161

kt_slot_troop_o_val = 230
kt_slot_troop_d_val = 231
kt_slot_troop_h_val = 232
kt_slot_troop_type = 233

kt_troop_type_footsoldier = 0   # !tf_guarantee_horse AND !tf_guarantee_ranged
kt_troop_type_cavalry = 1     # !tf_guarantee_ranged AND tf_guarantee_horse
kt_troop_type_archer = 2      # tf_guarantee_ranged AND !tf_guarnatee_horse
kt_troop_type_mtdarcher = 3   # tf_guarantee_ranged AND tf_guarantee_horse

slot_troop_horse = 306 # For horse whistle code.
slot_troop_wound_int = 307 # For wounding system.
slot_troop_wound_cha = 308 # For wounding system.
slot_troop_wound_str = 309 # For wounding system.
slot_troop_wound_agi = 310 # For wounding system.



########################################################
##  QUEST SLOTS            #############################
########################################################

slot_quest_subtype        = slot_subtype # Not used

slot_quest_temp_slot      = slot_temp_1

slot_quest_target_state   =  8
slot_quest_current_state  =  9


SLOT_QUEST_REFS = 16

slot_quest_target_center         = SLOT_QUEST_REFS +  0
slot_quest_target_troop          = SLOT_QUEST_REFS +  1
slot_quest_target_faction        = SLOT_QUEST_REFS +  2
slot_quest_target_party          = SLOT_QUEST_REFS +  3
slot_quest_target_party_template = SLOT_QUEST_REFS +  4
slot_quest_target_amount         = SLOT_QUEST_REFS +  5
slot_quest_target_dna            = SLOT_QUEST_REFS +  6
slot_quest_target_item           = SLOT_QUEST_REFS +  7

slot_quest_object_troop          = SLOT_QUEST_REFS +  8
slot_quest_object_center         = SLOT_QUEST_REFS +  9
slot_quest_object_faction        = SLOT_QUEST_REFS + 10
slot_quest_object_state          = SLOT_QUEST_REFS + 11

slot_quest_giver_troop           = SLOT_QUEST_REFS + 12
slot_quest_giver_center          = SLOT_QUEST_REFS + 13

slot_quest_convince_value        = SLOT_QUEST_REFS + 14


SLOT_QUEST_PARAMS = 32

slot_quest_importance                     = SLOT_QUEST_PARAMS + 0
slot_quest_xp_reward                      = SLOT_QUEST_PARAMS + 1
slot_quest_gold_reward                    = SLOT_QUEST_PARAMS + 2
slot_quest_expiration_days                = SLOT_QUEST_PARAMS + 3
slot_quest_dont_give_again_period         = SLOT_QUEST_PARAMS + 4
slot_quest_dont_give_again_remaining_days = SLOT_QUEST_PARAMS + 5
slot_quest_failure_consequence            = SLOT_QUEST_PARAMS + 6



########################################################
##  PARTY TEMPLATE SLOTS   #############################
########################################################

slot_party_template_num_killed      =  8

slot_party_template_lair_type       =  9
slot_party_template_lair_party      = 10
slot_party_template_lair_spawnpoint = 11



########################################################
##  SCENE PROP SLOTS       #############################
########################################################

slot_spawn_object_type              = slot_subtype # For dynamic object placement

ldop_scene_prop = -10
ldop_agent      = -11
ldop_horse      = -12
ldop_item       = -13

slot_spawn_object_id                =  8 # For dynamic object placement

scene_prop_open_or_close_slot       = 10
scene_prop_smoke_effect_done        = 11
scene_prop_number_of_agents_pushing = 12 #for belfries only
scene_prop_next_entry_point_id      = 13 #for belfries only
scene_prop_belfry_platform_moved    = 14 #for belfries only

scene_prop_slots_end                = 16




########################################################

#rel_enemy   = 0
#rel_neutral = 1
#rel_ally    = 2

# character backgrounds
cb_noble = 1
cb_merchant = 2
cb_guard = 3
cb_forester = 4
cb_nomad = 5
cb_thief = 6
cb_priest = 7

cb2_page = 0
cb2_apprentice = 1
cb2_urchin  = 2
cb2_steppe_child = 3
cb2_merchants_helper = 4

cb3_poacher = 3
cb3_craftsman = 4
cb3_peddler = 5
cb3_troubadour = 7
cb3_squire = 8
cb3_lady_in_waiting = 9
cb3_student = 10

cb4_revenge = 1
cb4_loss    = 2
cb4_wanderlust =  3
cb4_disown  = 5
cb4_greed  = 6

#Encounter types
enctype_fighting_against_village_raid = 1
enctype_catched_during_village_raid   = 2

#Talk contexts
tc_town_talk                  = 0
tc_court_talk                   = 1
tc_party_encounter            = 2
tc_castle_gate                = 3
tc_siege_commander            = 4
tc_join_battle_ally           = 5
tc_join_battle_enemy          = 6
tc_castle_commander           = 7
tc_hero_freed                 = 8
tc_hero_defeated              = 9
tc_entering_center_quest_talk = 10
tc_back_alley                 = 11
tc_siege_won_seneschal        = 12
tc_ally_thanks                = 13
tc_tavern_talk                = 14
tc_rebel_thanks               = 15
tc_garden                      = 16
tc_courtship                  = 16
tc_after_duel                  = 17
tc_prison_break               = 18
tc_escape                     = 19
tc_give_center_to_fief        = 20
tc_merchants_house            = 21


#Troop Commentaries begin
#Log entry types
#civilian
logent_village_raided            = 1
logent_village_extorted          = 2
logent_caravan_accosted          = 3 #in caravan accosted, center and troop object are -1, and the defender's faction is the object
logent_traveller_attacked        = 3 #in traveller attacked, origin and destination are center and troop object, and the attacker's faction is the object

logent_helped_peasants           = 4 

logent_party_traded              = 5

logent_castle_captured_by_player              = 10
logent_lord_defeated_by_player                = 11
logent_lord_captured_by_player                = 12
logent_lord_defeated_but_let_go_by_player     = 13
logent_player_defeated_by_lord                = 14
logent_player_retreated_from_lord             = 15
logent_player_retreated_from_lord_cowardly    = 16
logent_lord_helped_by_player                  = 17
logent_player_participated_in_siege           = 18
logent_player_participated_in_major_battle    = 19
logent_castle_given_to_lord_by_player         = 20

logent_pledged_allegiance          = 21
logent_liege_grants_fief_to_vassal = 22


logent_renounced_allegiance      = 23 

logent_player_claims_throne_1                           = 24
logent_player_claims_throne_2                           = 25


logent_troop_feels_cheated_by_troop_over_land           = 26
logent_ruler_intervenes_in_quarrel                     = 27
logent_lords_quarrel_over_land                         = 28
logent_lords_quarrel_over_insult                       = 29
logent_marshal_vs_lord_quarrel                         = 30
logent_lords_quarrel_over_woman                        = 31

logent_lord_protests_marshall_appointment               = 32
logent_lord_blames_defeat                                  = 33

logent_player_suggestion_succeeded                       = 35
logent_player_suggestion_failed                           = 36

logent_liege_promises_fief_to_vassal                   = 37

logent_lord_insults_lord_for_cowardice                 = 38
logent_lord_insults_lord_for_rashness                  = 39
logent_lord_insults_lord_for_abandonment               = 40
logent_lord_insults_lord_for_indecision                = 41
logent_lord_insults_lord_for_cruelty                   = 42
logent_lord_insults_lord_for_dishonor                  = 43




logent_game_start                           = 45 
logent_poem_composed                        = 46 ##Not added
logent_tournament_distinguished             = 47 ##Not added
logent_tournament_won                       = 48 ##Not added

#logent courtship - lady is always actor, suitor is always troop object
logent_lady_favors_suitor                   = 51 #basically for gossip
logent_lady_betrothed_to_suitor_by_choice   = 52
logent_lady_betrothed_to_suitor_by_family   = 53
logent_lady_rejects_suitor                  = 54
logent_lady_father_rejects_suitor           = 55
logent_lady_marries_lord                    = 56
logent_lady_elopes_with_lord                = 57
logent_lady_rejected_by_suitor              = 58
logent_lady_betrothed_to_suitor_by_pressure = 59 #mostly for gossip

logent_lady_and_suitor_break_engagement        = 60
logent_lady_marries_suitor                    = 61

logent_lord_holds_lady_hostages             = 62
logent_challenger_defeats_lord_in_duel      = 63
logent_challenger_loses_to_lord_in_duel     = 64

logent_player_stole_cattles_from_village    = 66

logent_party_spots_wanted_bandits           = 70


logent_border_incident_cattle_stolen          = 72 #possibly add this to rumors for non-player faction
logent_border_incident_bride_abducted         = 73 #possibly add this to rumors for non-player faction
logent_border_incident_villagers_killed       = 74 #possibly add this to rumors for non-player faction
logent_border_incident_subjects_mistreated    = 75 #possibly add this to rumors for non-player faction

#These supplement caravans accosted and villages burnt, in that they create a provocation. So far, they only refer to the player
logent_border_incident_troop_attacks_neutral  = 76
logent_border_incident_troop_breaks_truce     = 77
logent_border_incident_troop_suborns_lord   = 78


logent_policy_ruler_attacks_without_provocation             = 80
logent_policy_ruler_ignores_provocation                     = 81 #possibly add this to rumors for non-player factions
logent_policy_ruler_makes_peace_too_soon                    = 82
logent_policy_ruler_declares_war_with_justification         = 83
logent_policy_ruler_breaks_truce                            = 84
logent_policy_ruler_issues_indictment_just                  = 85 #possibly add this to rumors for non-player faction
logent_policy_ruler_issues_indictment_questionable          = 86 #possibly add this to rumors for non-player faction

logent_player_faction_declares_war                            = 90 #this doubles for declare war to extend power
logent_faction_declares_war_out_of_personal_enmity            = 91
logent_faction_declares_war_to_regain_territory             = 92
logent_faction_declares_war_to_curb_power                    = 93
logent_faction_declares_war_to_respond_to_provocation        = 94
logent_war_declaration_types_end                            = 95


#logent_lady_breaks_betrothal_with_lord      = 58
#logent_lady_betrothal_broken_by_lord        = 59



courtship_poem_tragic      = 1 #Emphasizes longing, Laila and Majnoon
courtship_poem_heroic      = 2 #Norse sagas with female heroines
courtship_poem_comic       = 3 #Emphasis on witty repartee -- Contrasto (Sicilian school satire) 
courtship_poem_mystic      = 4 #Sufi poetry. Song of Songs
courtship_poem_allegoric   = 5 #Idealizes woman as a civilizing force -- the Romance of the Rose, Siege of the Castle of Love

#courtship gifts currently deprecated


#Troop Commentaries end

#Walker types: 
num_town_walkers = 8
town_walker_entries_start = 32 # Entry point references starting from 32 are used for walkers

reinforcement_cost_easy = 600
reinforcement_cost_moderate = 450
reinforcement_cost_hard = 300

merchant_toll_duration        = 72 #Tolls are valid for 72 hours

hero_escape_after_defeat_chance = 70


raid_distance = 4

surnames_begin = "str_surname_1"
surnames_end = "str_surnames_end"
names_begin = "str_name_1"
names_end = surnames_begin
countersigns_begin = "str_countersign_1"
countersigns_end = names_begin
secret_signs_begin = "str_secret_sign_1"
secret_signs_end = countersigns_begin

# NE quests
girl_surnames_begin = "str_girl_surname_1"
girl_surnames_end = "str_girl_surnames_end"
girl_names_begin = "str_girl_name_2"
girl_names_end = "str_girl_surname_1"
# NE end quests 


kingdom_titles_male_begin = "str_faction_title_male_player"
kingdom_titles_female_begin = "str_faction_title_female_player"

kingdoms_begin = "fac_player_supporters_faction"
kingdoms_end = "fac_kingdoms_end"

npc_kingdoms_begin = "fac_kingdom_1"
npc_kingdoms_end = kingdoms_end

outlaws_begin = "trp_looter"
outlaws_end = "trp_black_khergit_horseman"

bandits_begin = "trp_bandit"
bandits_end = "trp_black_khergit_horseman"

kingdom_ladies_begin = "trp_knight_1_1_wife"
kingdom_ladies_end = "trp_heroes_end"

#active NPCs in order: companions, kings, lords, pretenders

pretenders_begin = "trp_kingdom_1_pretender"
pretenders_end = kingdom_ladies_begin

lords_begin = "trp_knight_1_1"
lords_end = pretenders_begin

kings_begin = "trp_kingdom_1_lord"
kings_end = lords_begin

companions_begin = "trp_npc1"
companions_end = kings_begin

active_npcs_begin = "trp_npc1"
active_npcs_end = kingdom_ladies_begin
#"active_npcs_begin replaces kingdom_heroes_begin to allow for companions to become lords. Includes anyone who may at some point lead their own party: the original kingdom heroes, companions who may become kingdom heroes, and pretenders. (slto_kingdom_hero as an occupation means that you lead a party on the map. Pretenders have the occupation "slto_inactive_pretender", even if they are part of a player's party, until they have their own independent party)
#If you're a modder and you don't want to go through and switch every kingdom_heroes to active_npcs, simply define a constant: kingdom_heroes_begin = active_npcs_begin., and kingdom_heroes_end = active_npcs_end. I haven't tested for that, but I think it should work.

active_npcs_including_player_begin = "trp_kingdom_heroes_including_player_begin"
original_kingdom_heroes_begin = "trp_kingdom_1_lord"

heroes_begin = active_npcs_begin
heroes_end = kingdom_ladies_end

soldiers_begin = trp.soldiers_begin + 1
soldiers_end = trp.soldiers_end

regular_soldiers_begin = trp.regular_soldiers_begin + 1
regular_soldiers_end   = trp.regular_soldiers_end

#Rebellion changes

# NE quests
peasants_begin = "trp_peasant_woman"
peasants_end = "trp_peasant_woman"
# NE end quests 


##rebel_factions_begin = "fac_kingdom_1_rebels"
##rebel_factions_end =   "fac_kingdoms_end"

pretenders_begin = "trp_kingdom_1_pretender"
pretenders_end = active_npcs_end
#Rebellion changes

tavern_minstrels_begin = "trp_tavern_minstrel_1"
tavern_minstrels_end   = "trp_kingdom_heroes_including_player_begin"

tavern_booksellers_begin = "trp_tavern_bookseller_1"
tavern_booksellers_end   = tavern_minstrels_begin

tavern_travelers_begin = "trp_tavern_traveler_1"
tavern_travelers_end   = tavern_booksellers_begin

ransom_brokers_begin = "trp_ransom_broker_1"
ransom_brokers_end   = tavern_travelers_begin

mercenary_troops_begin = trp.soldiers_begin + 2 # Skipping farmer troop
mercenary_troops_end = trp.mercenaries_end

lord_quests_begin = "qst_deliver_message"
lord_quests_end   = "qst_follow_army"

lord_quests_begin_2 = "qst_destroy_bandit_lair"
lord_quests_end_2   = "qst_blank_quest_2"

enemy_lord_quests_begin = "qst_lend_surgeon"
enemy_lord_quests_end   = lord_quests_end

village_elder_quests_begin = "qst_deliver_grain"
village_elder_quests_end = "qst_eliminate_bandits_infesting_village"

village_elder_quests_begin_2 = "qst_blank_quest_6"
village_elder_quests_end_2   = "qst_blank_quest_6"

mayor_quests_begin  = "qst_move_cattle_herd"
mayor_quests_end    = village_elder_quests_begin

mayor_quests_begin_2 = "qst_blank_quest_11"
mayor_quests_end_2   = "qst_blank_quest_11"

lady_quests_begin = "qst_rescue_lord_by_replace"
lady_quests_end   = mayor_quests_begin

lady_quests_begin_2 = "qst_blank_quest_16"
lady_quests_end_2   = "qst_blank_quest_16"

army_quests_begin = "qst_deliver_cattle_to_army"
army_quests_end   = lady_quests_begin

army_quests_begin_2 = "qst_blank_quest_21"
army_quests_end_2   = "qst_blank_quest_21"

player_realm_quests_begin = "qst_resolve_dispute"
player_realm_quests_end = "qst_blank_quest_1"

player_realm_quests_begin_2 = "qst_blank_quest_26"
player_realm_quests_end_2 = "qst_blank_quest_26"

all_items_begin = 0
all_items_end = "itm_items_end"

all_quests_begin = 0
all_quests_end = "qst_quests_end"

towns_begin = p.town_1
towns_end   = p.town_22 + 1
castles_begin = p.castle_1
castles_end   = p.castle_48 + 1
villages_begin = p.village_1
villages_end   = p.village_110 + 1

walled_centers_begin = towns_begin
walled_centers_end   = castles_end

centers_begin = towns_begin
centers_end   = villages_end

training_grounds_begin   = "p_training_ground_1"
training_grounds_end     = "p_Bridge_1"

scenes_begin = "scn_town_1_center"
scenes_end = "scn_castle_1_exterior"

spawn_points_begin = "p_town_1" # "p_zendar"
spawn_points_end = "p_spawn_points_end"

regular_troops_begin       = "trp_novice_fighter"
regular_troops_end         = trp.spy_walker_2 + 1

swadian_merc_parties_begin = "p_town_1_mercs"
swadian_merc_parties_end   = "p_town_8_mercs"

vaegir_merc_parties_begin  = "p_town_8_mercs"
vaegir_merc_parties_end    = "p_town_1" # "p_zendar"

arena_masters_begin    = "trp_town_1_arena_master"
arena_masters_end      = "trp_town_1_armorer"

training_gound_trainers_begin    = "trp_trainer_1"
training_gound_trainers_end      = "trp_ransom_broker_1"

#town_walkers_begin = "trp_town_walker_1"
#town_walkers_end = "trp_village_walker_1"

#village_walkers_begin = "trp_village_walker_1"
#village_walkers_end   = "trp_spy_walker_1"

town_walkers_begin = trp.town_walker_swa_m
town_walkers_end   = trp.town_walker_sar_f + 1

village_walkers_begin = trp.village_walker_swa_m
village_walkers_end   = trp.village_walker_sar_f + 1

spy_walkers_begin = trp.spy_walker_1
spy_walkers_end   = trp.spy_walker_2 + 1

walkers_begin = town_walkers_begin
walkers_end   = spy_walkers_end

armor_merchants_begin  = "trp_town_1_armorer"
armor_merchants_end    = "trp_town_1_weaponsmith"

weapon_merchants_begin = "trp_town_1_weaponsmith"
weapon_merchants_end   = "trp_town_1_tavernkeeper"

tavernkeepers_begin    = "trp_town_1_tavernkeeper"
tavernkeepers_end      = "trp_town_1_merchant"

goods_merchants_begin  = "trp_town_1_merchant"
goods_merchants_end    = "trp_town_1_horse_merchant"

horse_merchants_begin  = "trp_town_1_horse_merchant"
horse_merchants_end    = "trp_town_1_mayor"

mayors_begin           = "trp_town_1_mayor"
mayors_end             = "trp_village_1_elder"

village_elders_begin   = "trp_village_1_elder"
village_elders_end     = "trp_merchants_end"

startup_merchants_begin = "trp_swadian_merchant"
startup_merchants_end = "trp_startup_merchants_end"

num_max_items = 10000 #used for multiplayer mode

average_price_factor = 1000
minimum_price_factor = 100
maximum_price_factor = 10000

village_prod_min = 0 #was -5
village_prod_max = 20 #was 20

trade_goods_begin = itm.goods_begin + 1
trade_goods_end = itm.goods_end
food_begin = itm.food_apples
food_end = itm.goods_end
reference_books_begin = itm.book_wound_treatment_reference
reference_books_end   = itm.books_end
readable_books_begin = itm.book_tactics
readable_books_end   = reference_books_begin
books_begin = itm.books_begin + 1
books_end = itm.books_end
horses_begin = itm.horses_begin + 1
horses_end = itm.horses_end
weapons_begin = itm.weapons_begin + 1
weapons_end = itm.weapons_end
ranged_weapons_begin = itm.ranged_begin + 1
ranged_weapons_end = itm.ranged_end
armors_begin = itm.armors_begin + 1
armors_end = itm.armors_end
shields_begin = itm.shields_begin + 1
shields_end = itm.shields_end

# Banner constants

banner_meshes_begin = mesh.banner_a01
banner_lord_meshes_end = mesh.banners_default_a
banner_meshes_end_minus_one = mesh.banner_end_marker

#arms_meshes_begin = mesh.banner_a01
#arms_meshes_end_minus_one = mesh.banner_end_marker

banner_map_icons_begin = icon.banner_a01
banner_map_icons_end_minus_one = icon.banner_end_marker

banner_scene_props_begin = spr.banner_a
banner_scene_props_end_minus_one = spr.banner_end_marker

lord_fallback_map_icon = icon.banner_default_c
lord_fallback_scene_prop = spr.banner_default_c

khergit_banners_begin_offset = mesh.banner_d01 - banner_meshes_begin
khergit_banners_end_offset = mesh.banner_d21 - banner_meshes_begin + 1

sarranid_banners_begin_offset = mesh.banner_g01 - banner_meshes_begin
sarranid_banners_end_offset = mesh.banner_g21 - banner_meshes_begin + 1

banners_end_offset = mesh.banner_end_marker - banner_meshes_begin

custom_banner_charges_begin = "mesh_custom_banner_charge_01"
custom_banner_charges_end = "mesh_tableau_mesh_custom_banner"

custom_banner_backgrounds_begin = "mesh_custom_banner_bg"
custom_banner_backgrounds_end = custom_banner_charges_begin

custom_banner_flag_types_begin = "mesh_custom_banner_01"
custom_banner_flag_types_end = custom_banner_backgrounds_begin

custom_banner_flag_map_types_begin = "mesh_custom_map_banner_01"
custom_banner_flag_map_types_end = custom_banner_flag_types_begin

custom_banner_flag_scene_props_begin = "spr_custom_banner_01"
custom_banner_flag_scene_props_end = "spr_banner_a"

custom_banner_map_icons_begin = "icon_custom_banner_01"
custom_banner_map_icons_end = "icon_banner_01"

# Some constants for merchant invenotries
merchant_inventory_space = 30
num_merchandise_goods = 40

num_max_river_pirates = 25
num_max_zendar_peasants = 25
num_max_zendar_manhunters = 10

num_max_dp_bandits = 10
num_max_refugees = 10
num_max_deserters = 10

num_max_militia_bands = 15
num_max_armed_bands = 12

num_max_vaegir_punishing_parties = 20
num_max_rebel_peasants = 25

num_max_frightened_farmers = 50
num_max_undead_messengers  = 20

num_forest_bandit_spawn_points = 1
num_mountain_bandit_spawn_points = 1
num_steppe_bandit_spawn_points = 1
num_taiga_bandit_spawn_points = 1
num_desert_bandit_spawn_points = 1
num_black_khergit_spawn_points = 1
num_sea_raider_spawn_points = 2

peak_prisoner_trains = 4
peak_kingdom_caravans = 12
peak_kingdom_messengers = 3


# Note positions
note_troop_location = 3

#battle tactics
btactic_hold = 1
btactic_follow_leader = 2
btactic_charge = 3
btactic_stand_ground = 4

#default right mouse menu orders
cmenu_move = -7
cmenu_follow = -6

# Town center modes - resets in game menus during the options
tcm_default         = 0
tcm_disguised         = 1
tcm_prison_break     = 2
tcm_escape          = 3


# Arena battle modes
#abm_fight = 0
abm_training = 1
abm_visit = 2
abm_tournament = 3

# Camp training modes
ctm_melee    = 1
ctm_ranged   = 2
ctm_mounted  = 3
ctm_training = 4

# Village bandits attack modes
vba_normal          = 1
vba_after_training  = 2

arena_tier1_opponents_to_beat = 3
arena_tier1_prize = 1
arena_tier2_opponents_to_beat = 6
arena_tier2_prize = 2
arena_tier3_opponents_to_beat = 10
arena_tier3_prize = 3
arena_tier4_opponents_to_beat = 20
arena_tier4_prize = 4
arena_grand_prize = 5


#Additions
price_adjustment = 25 #the percent by which a trade at a center alters price

fire_duration = 4 #fires takes 4 hours


#$g_player_icon_state values
pis_normal                      = 0
pis_camping                     = 1
pis_ship                        = 2

argument_none         = 0
argument_claim        = 1 #deprecate for legal
argument_legal        = 1

argument_ruler        = 2 #deprecate for commons
argument_commons      = 2

argument_benefit      = 3 #deprecate for reward
argument_reward       = 3 

argument_victory      = 4
argument_lords        = 5
argument_rivalries    = 6 #new - needs to be added



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

ACHIEVEMENT_MEN_HANDLER = 75,
ACHIEVEMENT_GIRL_POWER = 76,
ACHIEVEMENT_QUEEN = 77,
ACHIEVEMENT_EMPRESS = 78,
ACHIEVEMENT_TALK_OF_THE_TOWN = 79,
ACHIEVEMENT_LADY_OF_THE_LAKE = 80,

####################################################################################################################################
# NE 600 series constants begin
####################################################################################################################################
slot_militia_quest_completed = 601

####################################################################################################################################
# NE 600 series constants end
####################################################################################################################################

# 0.608b5 new stuff

# Troop tree presentation
title_pos_x   = 500
title_pos_y   = 650
title_size    = 2000
title_black   = 0x000000
title_red     = 0xFF0000
title_yellow  = 0xFFFF00
working_pos_y = 560
large_size    = 1500
medium_size   = 1200
normal_size   = 1000
small_size    = 800
smaller_size  = 650
tinny_size    = 450
troop_tree_size_x  = 375
troop_tree_size_y  = 500
troop_tree_space_x = 160 # 170
troop_tree_space_y = 140
troop_tree_left    = 80  # 60

# 0.608b7 new stuff

# Fancy nobility titles
noble_titles_begin = "str_noble_title_1_1"
noble_titles_end   = "str_noble_title_a_1"
custom_titles_begin = noble_titles_end
custom_titles_end   = "str_noble_title_h_1" # Currently 7 custom title sets are filled, with 9 more in reserve

# 0.610b new stuff

# "$town_menu_manage_items"
# "$town_menu_manage_count"

town_menu_item_court      = 0x0001 # Player is town lord AND NOT faction leader.
town_menu_item_recruit_n  = 0x0010 # Player can recruit AND troops are available
town_menu_item_recruit_e1 = 0x0020 # Player can recruit AND troops are available
town_menu_item_recruit_e2 = 0x0040 # Player can recruit AND troops are available
town_menu_item_recruit_m  = 0x0080 # Mercenaries are available in town
town_menu_item_build      = 0x0100 # Player is town lord AND no current construction AND something can be built
town_menu_item_sponsor    = 0x0200 # Player is marshal or leader AND NOT player is town lord AND same faction AND no current construction AND something can be built
town_menu_item_demolish   = 0x0400 # currently always unavailable
town_menu_item_station    = 0x1000 # Player is town lord OR center captured by player AND player claimed it OR player is leader AND center is not owned
town_menu_item_reinforce  = 0x2000 # Same faction AND player is leader or marshal AND center owned by someone AND NOT center owned by player

tma_leave        = -1
tma_presentation = 0
tma_mission      = 1
tma_trade        = 2
tma_loot         = 3
tma_conversation = 4


# PLUGIN_MULTIPLAYER


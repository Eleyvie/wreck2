from compiler import *

####################################################################################################################
#  Each item record contains the following fields:
#  1) Item id: used for referencing items in other files.
#     The prefix itm_ is automatically added before each item id.
#  2) Item name. Name of item as it'll appear in inventory window
#  3) List of meshes.  Each mesh record is a tuple containing the following fields:
#    3.1) Mesh name.
#    3.2) Modifier bits that this mesh matches.
#     Note that the first mesh record is the default.
#  4) Item flags. See header_items.py for a list of available flags.
#  5) Item capabilities. Used for which animations this item is used with. See header_items.py for a list of available flags.
#  6) Item value.
#  7) Item stats: Bitwise-or of various stats about the item such as:
#      weight, abundance, difficulty, head_armor, body_armor,leg_armor, etc...
#  8) Modifier bits: Modifiers that can be applied to this item.
#  9) [Optional] Triggers: List of simple triggers to be associated with the item.
#  10) [Optional] Factions: List of factions that item can be found as merchandise.
####################################################################################################################

imodbits_none = 0

itp_type_food  = itp_type_goods|itp_consumable|itp_food
itp_type_drink = itp_type_goods|itp_consumable

imodbits_horse_negative  = imodbit.battered | imodbit.old | imodbit.lame | imodbit.shabby
imodbits_horse_positive  = imodbit.tough | imodbit.heavy | imodbit.superior | imodbit.lordly | imodbit.restless | imodbit.spirited
imodbits_armor_negative  = imodbit.battered | imodbit.makeshift | imodbit.old | imodbit.tarnished
imodbits_armor_positive  = imodbit.sturdy | imodbit.tough | imodbit.hardened | imodbit.heavy | imodbit.superior | imodbit.lordly
imodbits_shield_negative = imodbit.battered | imodbit.makeshift | imodbit.old | imodbit.crude | imodbit.tarnished
imodbits_shield_positive = imodbit.sturdy | imodbit.tough | imodbit.hardened | imodbit.heavy | imodbit.superior | imodbit.lordly
imodbits_weapon_negative = imodbit.battered | imodbit.bent | imodbit.cracked | imodbit.tarnished | imodbit.chipped
imodbits_weapon_positive = imodbit.fine | imodbit.powerful | imodbit.deadly | imodbit.tempered | imodbit.masterwork
imodbits_ranged_negative = imodbit.battered | imodbit.bent | imodbit.cracked | imodbit.tarnished | imodbit.chipped
imodbits_ranged_positive = imodbit.fine | imodbit.powerful | imodbit.deadly | imodbit.tempered | imodbit.masterwork
imodbits_ammo_negative   = imodbit.battered | imodbit.bent | imodbit.cracked | imodbit.chipped
imodbits_ammo_positive   = imodbit.fine | imodbit.heavy | imodbit.deadly | imodbit.tempered | imodbit.masterwork | imodbit.large_bag

imodbits_prerequisites   = imodbit.unwieldy | imodbit.balanced

imodbits_armor  = imodbits_armor_negative | imodbits_armor_positive
imodbits_horse  = imodbits_horse_negative | imodbits_horse_positive
imodbits_shield = imodbits_shield_negative | imodbits_shield_positive
imodbits_weapon = imodbits_weapon_negative | imodbits_weapon_positive
imodbits_ranged = imodbits_ranged_negative | imodbits_ranged_positive
imodbits_ammo   = imodbits_ammo_negative | imodbits_ammo_positive

imodbits_horse_basic = imodbits_horse_negative | imodbit.tough | imodbit.heavy
imodbits_horse_good  = imodbits_horse

imodbits_cloth_low  = imodbit.battered | imodbit.makeshift | imodbit.shabby | imodbit.old | imodbit.crude | imodbit.tarnished | imodbit.decent | imodbit.sturdy | imodbit.fine | imodbit.hardened
imodbits_cloth_high = imodbit.old | imodbit.tarnished | imodbit.decent | imodbit.fine | imodbit.refined | imodbit.elegant | imodbit.flawless | imodbit.exquisite | imodbit.lordly
imodbits_cloth_med  = imodbit.old | imodbit.tarnished | imodbit.decent | imodbit.sturdy | imodbit.fine | imodbit.hardened


items = [

########################################################################################################################
# HARDCODED ITEMS - LEAVING AS IS
########################################################################################################################

    ["no_item", "INVALID ITEM", [("invalid_item", 0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_sword_1h, 3, weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16, blunt)|thrust_damage(10, blunt), imodbits_none], 

    ["tutorial_spear", "Spear", [("spear_i_2-3m", 0)], itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear, 0, weight(4.5)|difficulty(0)|spd_rtng(80)|weapon_length(158)|swing_damage(0, cut)|thrust_damage(19, pierce), imodbits_none], 
    ["tutorial_club", "Club", [("lav_club", 0)], itp_type_one_handed_wpn|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_sabre_1h, 0, weight(2.5)|difficulty(0)|spd_rtng(95)|weapon_length(95)|swing_damage(11, blunt)|thrust_damage(0, pierce), imodbits_none], 
    ["tutorial_battle_axe", "Battle Axe", [("two_handed_battle_axe_b", 0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_sabre_2h|itcf_carry_axe_back, 0, weight(5)|difficulty(0)|spd_rtng(88)|weapon_length(108)|swing_damage(27, cut)|thrust_damage(0, pierce), imodbits_none], 
    ["tutorial_arrows", "Arrows", [("arrow", 0), ("flying_missile", ixmesh_flying_ammo), ("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0, weight(3)|abundance(160)|weapon_length(95)|thrust_damage(0, pierce)|max_ammo(20), imodbits_none], 
    ["tutorial_bolts", "Bolts", [("bolt", 0), ("flying_missile", ixmesh_flying_ammo), ("bolt_bag", ixmesh_carry), ("bolt_bag_b", ixmesh_carry|imodbit.large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0, weight(2.25)|abundance(90)|weapon_length(55)|thrust_damage(0, pierce)|max_ammo(18), imodbits_none], 
    ["tutorial_short_bow", "Short Bow", [("lav_bow_common_short", 0), ("lav_bow_common_short_carry", ixmesh_carry)], itp_type_bow|itp_primary|itp_two_handed, itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1)|difficulty(0)|spd_rtng(98)|shoot_speed(49)|thrust_damage(12, pierce ), imodbits_none], 
    ["tutorial_crossbow", "Crossbow", [("native_crossbow_b", 0)], itp_type_crossbow|itp_primary|itp_two_handed|itp_cant_reload_on_horseback, itcf_shoot_crossbow|itcf_carry_crossbow_back, 0, weight(3)|difficulty(0)|spd_rtng(42)|shoot_speed(68)|thrust_damage(32, pierce)|max_ammo(1), imodbits_none], 
    ["tutorial_throwing_daggers", "Throwing Daggers", [("throwing_dagger", 0)], itp_type_thrown|itp_primary, itcf_throw_knife, 0, weight(3.5)|difficulty(0)|spd_rtng(102)|shoot_speed(25)|thrust_damage(16, cut)|max_ammo(14)|weapon_length(0), imodbits_none], 
    ["tutorial_saddle_horse", "Saddle Horse", [("saddle_horse", 0)], itp_type_horse, 0, 0, abundance(90)|body_armor(3)|difficulty(0)|horse_speed(40)|horse_maneuver(38)|horse_charge(8), imodbits_none], 
    ["tutorial_shield", "Kite Shield", [("shield_kite_g", 0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 118, weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(150), imodbits_none], 
    ["tutorial_staff_no_attack", "Staff", [("luc2_wooden_staff", 0)], itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_polearm_parry|itcf_carry_sword_back, 9, weight(3.5)|spd_rtng(120)|weapon_length(127)|swing_damage(0, blunt)|thrust_damage(0, blunt), imodbits_none], 
    ["tutorial_staff", "Staff", [("luc2_wooden_staff", 0)], itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_sword_back, 9, weight(3.5)|spd_rtng(120)|weapon_length(127)|swing_damage(16, blunt)|thrust_damage(16, blunt), imodbits_none], 
    ["tutorial_sword", "Sword", [("sword_medieval_a", 0), ("sword_medieval_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 0, weight(1.5)|difficulty(0)|spd_rtng(100)|weapon_length(102)|swing_damage(18, cut)|thrust_damage(15, pierce), imodbits_none], 
    ["tutorial_axe", "Axe", [("two_handed_battle_axe_e", 0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_sabre_2h|itcf_carry_axe_back, 0, weight(4)|difficulty(0)|spd_rtng(91)|weapon_length(108)|swing_damage(19, cut)|thrust_damage(0, pierce), imodbits_none], 
    ["tutorial_dagger", "Dagger", [("practice_dagger", 0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_sword_1h, 3, weight(1.5)|spd_rtng(103)|weapon_length(40)|swing_damage(16, blunt)|thrust_damage(10, blunt), imodbits_none], 

    ["horse_meat", "Horse Meat", [("raw_meat", 0)], itp_type_goods|itp_consumable|itp_food, 0, 12, weight(40)|food_quality(30)|max_ammo(40), imodbits_none], 

########################################################################################################################
# DUMMY ITEM RECORDS (THESE ITEMS ARE REFERENCES BY WARBAND SCENES SO WE'RE KEEPING THEM WITH INTACT IDS)
########################################################################################################################

    # Goods

    ["ale", "ale_barrel", [("ale_barrel",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["apples", "apple_basket", [("apple_basket",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["bread", "bread_a", [("bread_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["butter", "butter_pot", [("butter_pot",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["cattle_meat", "raw_meat", [("raw_meat",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["cheese", "cheese_b", [("cheese_b",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["dried_meat", "smoked_meat", [("smoked_meat",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["flour", "salt_sack", [("salt_sack",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["furs", "fur_pack", [("fur_pack",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["grain", "wheat_sack", [("wheat_sack",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["honey", "honey_pot", [("honey_pot",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["iron", "iron", [("iron",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["leatherwork", "leatherwork_frame", [("leatherwork_frame",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["linen", "linen", [("linen",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["lute", "lute", [("lute",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["oil", "oil", [("oil",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["pork", "pork", [("pork",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["pottery", "jug", [("jug",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["quest_ale", "ale_barrel", [("ale_barrel",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["quest_wine", "amphora_slim", [("amphora_slim",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["raw_dyes", "dyes", [("dyes",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["raw_leather", "leatherwork_inventory", [("leatherwork_inventory",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["raw_silk", "raw_silk_bundle", [("raw_silk_bundle",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["salt", "salt_sack", [("salt_sack",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["sausages", "sausages", [("sausages",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["siege_supply", "ale_barrel", [("ale_barrel",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["smoked_fish", "smoked_fish", [("smoked_fish",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["spice", "spice_sack", [("spice_sack",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["tools", "iron_hammer", [("bb_smith_hammer",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["velvet", "velvet", [("velvet",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["wine", "amphora_slim", [("amphora_slim",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["wool", "wool_sack", [("wool_sack",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["wool_cloth", "wool_cloth", [("wool_cloth",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["raw_date_fruit", "date_inventory", [("date_inventory",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],

    # Books

    #["book_engineering", "book_open", [("book_open",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["book_intelligence", "book_e", [("book_e",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["book_leadership", "book_d", [("book_d",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["book_persuasion", "book_b", [("book_b",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["book_surgery_reference", "book_c", [("book_c",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["book_tactics", "book_a", [("book_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["book_trade", "book_f", [("book_f",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["book_training_reference", "book_open", [("book_open",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["book_weapon_mastery", "book_d", [("book_d",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["book_wound_treatment_reference", "book_c", [("book_c",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],

    # Horses

    ["arabian_horse_a", "Arabian Horse", [("arabian_horse_a",0)], itp_type_horse, 0, 0, hit_points(100)|difficulty(20)|horse_speed(40)|horse_maneuver(40), imodbits_none],
    ["arabian_horse_b", "Arabian Horse", [("arabian_horse_b",0)], itp_type_horse, 0, 0, hit_points(100)|difficulty(20)|horse_speed(40)|horse_maneuver(40), imodbits_none],
    ["charger", "Charger", [("charger_new",0)],                   itp_type_horse, 0, 0, hit_points(100)|difficulty(20)|horse_speed(40)|horse_maneuver(40), imodbits_none],
    ["courser", "Courser", [("courser",0)],                       itp_type_horse, 0, 0, hit_points(100)|difficulty(20)|horse_speed(40)|horse_maneuver(40), imodbits_none],
    ["hunter", "Hunting Horse", [("hunting_horse",0)],            itp_type_horse, 0, 0, hit_points(100)|difficulty(20)|horse_speed(40)|horse_maneuver(40), imodbits_none],
    ["saddle_horse", "Saddle Horse", [("saddle_horse",0)],        itp_type_horse, 0, 0, hit_points(100)|difficulty(20)|horse_speed(40)|horse_maneuver(40), imodbits_none],
    ["steppe_horse", "Steppe Horse", [("steppe_horse",0)],        itp_type_horse, 0, 0, hit_points(100)|difficulty(20)|horse_speed(40)|horse_maneuver(40), imodbits_none],
    ["sumpter_horse", "Sumpter Horse", [("sumpter_horse",0)],     itp_type_horse, 0, 0, hit_points(100)|difficulty(20)|horse_speed(40)|horse_maneuver(40), imodbits_none],
    ["warhorse", "Warhorse", [("warhorse_chain",0)],              itp_type_horse, 0, 0, hit_points(100)|difficulty(20)|horse_speed(40)|horse_maneuver(40), imodbits_none],

    # Practice Equipment

    #["practice_arrows", "arena_arrow", [("arena_arrow",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["practice_arrows_2", "arena_arrow", [("arena_arrow",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["practice_axe", "hatchet", [("hatchet",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["practice_bolts", "bolt", [("bolt",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["practice_bow", "hunting_bow", [("hunting_bow",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["practice_bow_2", "hunting_bow", [("hunting_bow",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["practice_crossbow", "crossbow_a", [("crossbow_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["practice_horse", "saddle_horse", [("saddle_horse",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["practice_javelin", "javelin", [("javelin",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["practice_lance", "joust_of_peace", [("joust_of_peace",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["practice_shield", "shield_round_a", [("shield_round_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["practice_staff", "wooden_staff", [("wooden_staff",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["practice_throwing_daggers", "throwing_dagger", [("throwing_dagger",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],

    # Arena Equipment

    ["arena_axe", "arena_axe", [("arena_axe",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["arena_helmet_blue", "arena_helmetB", [("arena_helmetB",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["arena_helmet_green", "arena_helmetG", [("arena_helmetG",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["arena_helmet_red", "arena_helmetR", [("arena_helmetR",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["arena_helmet_yellow", "arena_helmetY", [("arena_helmetY",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["arena_lance", "arena_lance", [("arena_lance",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["arena_shield_blue", "arena_shield_blue", [("arena_shield_blue",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["arena_shield_green", "arena_shield_green", [("arena_shield_green",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["blue_tourney_helmet", "segmented_helm", [("segmented_helm",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["gold_tourney_helmet", "hood_a", [("hood_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["red_tourney_helmet", "flattop_helmet", [("flattop_helmet",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["tourney_helm_white", "tourney_helmR", [("tourney_helmR",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["steppe_helmet_white", "steppe_helmetW", [("steppe_helmetW",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],

    # Shields

    ["steel_shield", "shield_dragon", [("spak_shield_wood3",0)], itp_type_goods, 0, 0, weight(1), imodbits_none], # OK (replaced)

    ["heater_shield", "shield_heater_a",   [("shield_heater_c",0)], itp_type_goods, 0, 0, weight(1), imodbits_none], # OK (replaced)
    ["shield_heater_c", "shield_heater_c", [("shield_heater_c",0)], itp_type_goods, 0, 0, weight(1), imodbits_none], # OK
    ["shield_heater_d", "shield_heater_d", [("shield_heater_d",0)], itp_type_goods, 0, 0, weight(1), imodbits_none], # OK

    ["kite_shield_", "shield_kite_b",       [("shield_kite_i",0)], itp_type_goods, 0, 0, weight(1), imodbits_none], # OK (replaced)
    ["large_shield", "shield_kite_c",       [("shield_kite_k",0)], itp_type_goods, 0, 0, weight(1), imodbits_none], # OK (replaced)
    ["battle_shield", "shield_kite_d",      [("shield_kite_h",0)], itp_type_goods, 0, 0, weight(1), imodbits_none], # OK (replaced)
    ["fur_covered_shield", "shield_kite_m", [("shield_kite_m",0)], itp_type_goods, 0, 0, weight(1), imodbits_none], # OK

    ["wooden_shield", "shield_round_a",                [("kovas_shield_13",0)], itp_type_goods, 0, 0, weight(1), imodbits_none], # OK (replaced)
    ["nordic_shield", "shield_round_b",                [("kovas_shield_15",0)], itp_type_goods, 0, 0, weight(1), imodbits_none], # OK (replaced)
    ["round_shield", "shield_round_c",                 [("ad_viking_shield_round_04",0)], itp_type_goods, 0, 0, weight(1), imodbits_none], # OK (replaced)
    ["leather_covered_round_shield", "shield_round_d", [("shield_round_d",0)], itp_type_goods, 0, 0, weight(1), imodbits_none], # OK
    ["shield_round_e", "shield_round_e",               [("shield_round_e",0)], itp_type_goods, 0, 0, weight(1), imodbits_none], # OK
    ["plate_covered_round_shield", "shield_round_e",   [("shield_round_e",0)], itp_type_goods, 0, 0, weight(1), imodbits_none], # OK
    ["hide_covered_round_shield", "shield_round_f",    [("shield_round_f",0)], itp_type_goods, 0, 0, weight(1), imodbits_none], # OK

    ["nomad_shield", "shield_wood_b", [("spak_shield_wood2",0)], itp_type_goods, 0, 0, weight(1), imodbits_none], # OK (replaced)

    #["norman_shield_1", "norman_shield_1", [("norman_shield_1",0)], itp_type_goods, 0, 0, weight(1), imodbits_none], # OK
    #["norman_shield_2", "norman_shield_2", [("norman_shield_2",0)], itp_type_goods, 0, 0, weight(1), imodbits_none], # OK
    #["norman_shield_3", "norman_shield_3", [("norman_shield_3",0)], itp_type_goods, 0, 0, weight(1), imodbits_none], # OK
    #["norman_shield_5", "norman_shield_5", [("norman_shield_5",0)], itp_type_goods, 0, 0, weight(1), imodbits_none], # OK
    #["norman_shield_6", "norman_shield_6", [("norman_shield_6",0)], itp_type_goods, 0, 0, weight(1), imodbits_none], # OK
    #["norman_shield_7", "norman_shield_7", [("norman_shield_7",0)], itp_type_goods, 0, 0, weight(1), imodbits_none], # OK
    #["norman_shield_8", "norman_shield_8", [("norman_shield_8",0)], itp_type_goods, 0, 0, weight(1), imodbits_none], # OK

    ["tab_shield_heater_a", "tableau_shield_heater_1", [("tableau_shield_heater_1",0)], itp_type_goods, 0, 0, weight(1), imodbits_none, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"), (store_trigger_param_2, ":troop_no"), (call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")]), ]],
    ["tab_shield_heater_c", "tableau_shield_heater_1", [("tableau_shield_heater_1",0)], itp_type_goods, 0, 0, weight(1), imodbits_none, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"), (store_trigger_param_2, ":troop_no"), (call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")]), ]],
    ["tab_shield_heater_cav_b", "tableau_shield_heater_2", [("tableau_shield_heater_2",0)], itp_type_goods, 0, 0, weight(1), imodbits_none, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"), (store_trigger_param_2, ":troop_no"), (call_script, "script_shield_item_set_banner", "tableau_heater_shield_2", ":agent_no", ":troop_no")]), ]],
    ["tab_shield_kite_a", "tableau_shield_kite_1", [("tableau_shield_kite_1",0)], itp_type_goods, 0, 0, weight(1), imodbits_none, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"), (store_trigger_param_2, ":troop_no"), (call_script, "script_shield_item_set_banner", "tableau_kite_shield_1", ":agent_no", ":troop_no")]), ]],
    ["tab_shield_pavise_c", "tableau_shield_pavise_1", [("tableau_shield_pavise_1",0)], itp_type_goods, 0, 0, weight(1), imodbits_none, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"), (store_trigger_param_2, ":troop_no"), (call_script, "script_shield_item_set_banner", "tableau_pavise_shield_1", ":agent_no", ":troop_no")]), ]],
    ["tab_shield_small_round_b", "tableau_shield_small_round_1", [("tableau_shield_small_round_1",0)], itp_type_goods, 0, 0, weight(1), imodbits_none, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"), (store_trigger_param_2, ":troop_no"), (call_script, "script_shield_item_set_banner", "tableau_small_round_shield_1", ":agent_no", ":troop_no")]), ]],
    ["tab_shield_small_round_c", "tableau_shield_small_round_2", [("tableau_shield_small_round_2",0)], itp_type_goods, 0, 0, weight(1), imodbits_none, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"), (store_trigger_param_2, ":troop_no"), (call_script, "script_shield_item_set_banner", "tableau_small_round_shield_2", ":agent_no", ":troop_no")]), ]],

    # Weapons

    # NEED REPLACEMENTS:

    #["axe", "iron_ax", [("iron_ax",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["battle_axe", "battle_ax", [("battle_ax",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["double_axe", "dblhead_ax", [("dblhead_ax",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["fighting_axe", "fighting_ax", [("fighting_ax",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["great_axe", "great_ax", [("great_ax",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["war_axe", "war_ax", [("war_ax",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],

    # FIX: rename base items:
    ["sword_khergit_1", "khergit_sword_b", [("khergit_sword_b",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["sword_khergit_2", "khergit_sword_c", [("khergit_sword_c",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["sword_khergit_3", "khergit_sword_a", [("khergit_sword_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["sword_khergit_4", "khergit_sword_d", [("khergit_sword_d",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["sword_of_war", "sword_of_war", [("sword_two_handed_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["bastard_sword", "bastard_sword", [("sword_two_handed_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["broadsword", "broadsword", [("sword_medieval_a_long",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["falchion", "falchion_new", [("falchion_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["sword", "sword", [("bb_serbian_sword_1",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["great_sword", "great_sword", [("sword_two_handed_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["sword_viking_2", "sword_viking_b", [("sword_viking_b",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["sword_viking_2_small", "sword_viking_b_small", [("sword_viking_b_small",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["sword_viking_3", "sword_viking_a", [("sword_viking_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["sword_viking_3_small", "sword_viking_a_small", [("sword_viking_a_small",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["arming_sword", "arming_sword", [("bb_serbian_sword_2",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["nordic_sword", "nordic_sword", [("sword_viking_a_long",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["two_handed_cleaver", "military_cleaver_a", [("military_cleaver_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["warhammer", "maul_d", [("maul_d",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],

    ["felt_steppe_cap", "felt_steppe_cap", [("steppe_cap_a_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["woolen_hood", "woolen_hood", [("hood_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],

    # TODO: add these for Veidar village
    # black_armor
    # face_helm

    # PROCESSED:

    #["club", "club", [("club",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["cudgel", "club", [("club",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["sickle", "sickle", [("sickle",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["jousting_lance", "joust_of_peace", [("lav_lance_joust_f230",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["double_sided_lance", "lance_dblhead", [("bb_serbian_spear_1",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["great_lance", "heavy_lance", [("heavy_lance",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["light_lance", "spear_b_2", [("spear_b_2",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["staff", "wooden_staff", [("wooden_staff",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["iron_staff", "iron_staff", [("iron_staff",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["awlpike", "awl_pike_b", [("awl_pike_b",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["awlpike_long", "awl_pike_a", [("awl_pike_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["bardiche", "two_handed_battle_axe_d", [("two_handed_battle_axe_d",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["great_bardiche", "two_handed_battle_axe_f", [("two_handed_battle_axe_f",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["hafted_blade_b", "khergit_pike_b", [("khergit_pike_b",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["ashwood_pike", "pike", [("bb_ashwood_pike",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["bamboo_spear", "arabian_spear_a_3m", [("arabian_spear_a_3m",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["boar_spear", "spear", [("spear_h_2-15m",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["shortened_spear", "spear_g_1-9m", [("spear_g_1",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["spear", "spear", [("spear_i_2-3m",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["war_spear", "spear_i_2-3m", [("spear_i_2-3m",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["pitch_fork", "pitch_fork", [("pitch_fork",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["scythe", "scythe", [("scythe",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["shortened_military_scythe", "two_handed_battle_scythe_a", [("two_handed_battle_scythe_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["glaive", "glaive_b", [("glaive_b",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["battle_fork", "battle_fork", [("battle_fork",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["military_fork", "military_fork", [("military_fork",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["voulge", "voulge", [("luc3_wagoners_axe_no2",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["butchering_knife", "khyber_knife_new", [("khyber_knife_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["cleaver", "cleaver_new", [("cleaver_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["bec_de_corbin_a", "bec_de_corbin_a", [("bec_de_corbin_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["club_with_spike_head", "mace_e", [("mace_e",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["dagger", "dagger_b", [("dagger_b",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["hammer", "iron_hammer_new", [("iron_hammer_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["fighting_pick", "fighting_pick_new", [("fighting_pick_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["hatchet", "hatchet", [("hatchet",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["military_pick", "steel_pick_new", [("steel_pick_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["pickaxe", "fighting_pick_new", [("fighting_pick_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["torch", "club", [("club",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["wooden_stick", "wooden_stick", [("wooden_stick",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["spiked_club", "spiked_club", [("mace_d",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["spiked_mace", "spiked_mace_new", [("spiked_mace_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["winged_mace", "flanged_mace", [("flanged_mace",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["mace_2", "mace_a", [("mace_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["mace_4", "mace_b", [("mace_b",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["sarranid_mace_1", "mace_small_d", [("mace_small_d",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["morningstar", "mace_morningstar_new", [("mace_morningstar_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["maul", "maul_b", [("maul_b",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["sledgehammer", "maul_c", [("maul_c",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["hand_axe", "hatchet", [("bb_serbian_hatchet",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["long_axe", "long_axe_a", [("long_axe_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["long_axe_c_alt", "long_axe_c", [("long_axe_c",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["one_handed_battle_axe_a", "one_handed_battle_axe_a", [("one_handed_battle_axe_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["one_handed_battle_axe_c", "one_handed_battle_axe_c", [("one_handed_battle_axe_c",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["one_handed_war_axe_a", "one_handed_war_axe_a", [("one_handed_war_axe_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["one_handed_war_axe_b", "one_handed_war_axe_b", [("one_handed_war_axe_b",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["sarranid_axe_a", "one_handed_battle_axe_g", [("one_handed_battle_axe_g",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["sarranid_axe_b", "one_handed_battle_axe_h", [("one_handed_battle_axe_h",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["two_handed_axe", "two_handed_battle_axe_a", [("two_handed_battle_axe_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["two_handed_battle_axe_2", "two_handed_battle_axe_b", [("two_handed_battle_axe_b",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],

    # PLANNED:

    #["arabian_sword_c", "arabian_sword_c", [("arabian_sword_c",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["bastard_sword_a", "bastard_sword_a", [("bastard_sword_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["bastard_sword_b", "bastard_sword_b", [("bastard_sword_b",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["khergit_sword", "khergit_sword", [("khergit_sword",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["scimitar", "scimeter", [("scimeter",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["scimitar_b", "scimitar_b", [("scimitar_b",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["sword_medieval_a", "sword_medieval_a", [("sword_medieval_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["sword_medieval_a_long", "sword_medieval_a_long", [("sword_medieval_a_long",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["sword_medieval_b", "sword_medieval_b", [("sword_medieval_b",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["sword_medieval_c", "sword_medieval_c", [("sword_medieval_c",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["sword_medieval_c_long", "sword_medieval_c_long", [("sword_medieval_c_long",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["sword_medieval_c_small", "sword_medieval_c_small", [("sword_medieval_c_small",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["sword_two_handed_a", "sword_two_handed_a", [("sword_two_handed_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["sword_two_handed_b", "sword_two_handed_b", [("sword_two_handed_b",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],

    # Ranged Weapons and Ammo

    #["arrows", "arrow", [("arrow",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["barbed_arrows", "barbed_arrow", [("barbed_arrow",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["bodkin_arrows", "piercing_arrow", [("piercing_arrow",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["bolts", "bolt", [("bolt",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["crossbow", "crossbow_a", [("crossbow_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["heavy_crossbow", "crossbow_c", [("crossbow_c",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["heavy_throwing_axes", "throwing_axe_b", [("throwing_axe_b",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["heavy_throwing_axes_melee", "throwing_axe_b", [("throwing_axe_b",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["hunting_bow", "hunting_bow", [("hunting_bow",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["hunting_crossbow", "crossbow_a", [("crossbow_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["jarid", "jarid_new", [("jarid_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["javelin", "javelin", [("javelin",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["khergit_bow", "khergit_bow", [("lav_bow_common_curved",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["light_crossbow", "crossbow_b", [("crossbow_b",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["light_throwing_axes", "francisca", [("francisca",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["long_bow", "long_bow", [("long_bow",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["nomad_bow", "nomad_bow", [("nomad_bow",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["short_bow", "short_bow", [("short_bow",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["sniper_crossbow", "crossbow_c", [("crossbow_c",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["strong_bow", "strong_bow", [("lav_bow_common_strong",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["throwing_axes", "throwing_axe_a", [("throwing_axe_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["throwing_axes_melee", "throwing_axe_a", [("throwing_axe_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["throwing_knives", "throwing_knife", [("throwing_knife",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["throwing_spear_melee", "jarid_new_b", [("jarid_new_b",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["war_bow", "war_bow", [("lav_bow_common_war",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],

    # Armor

    #["arming_cap", "arming_cap_a_new", [("arming_cap_a_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["bascinet", "bascinet_avt_new", [("bascinet_avt_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["bascinet_2", "bascinet_new_a", [("bascinet_new_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["bascinet_3", "bascinet_new_b", [("bascinet_new_b",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["black_helmet", "black_helm", [("zottlm_hounskull_plain",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["black_hood", "hood_black", [("hood_black",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["byzantion_helmet_a", "byzantion_helmet_a", [("vaeg_helmet5",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["desert_turban", "tuareg", [("tuareg",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["felt_hat", "felt_hat_a_new", [("felt_hat_a_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["felt_hat_b", "felt_hat_b_new", [("felt_hat_b_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["female_hood", "ladys_hood_new", [("ladys_hood_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["flat_topped_helmet", "flattop_helmet_new", [("flattop_helmet_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["footman_helmet", "skull_cap_new", [("skull_cap_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["full_helm", "great_helmet_new_b", [("great_helmet_new_b",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["fur_hat", "fur_hat_a_new", [("fur_hat_a_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["great_helmet", "great_helmet_new", [("great_helmet_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["guard_helmet", "reinf_helmet_new", [("reinf_helmet_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["headcloth", "headcloth_a_new", [("headcloth_a_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["helmet_with_neckguard", "neckguard_helm_new", [("neckguard_helm_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["kettle_hat", "kettle_hat_new", [("kettle_hat_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["khergit_cavalry_helmet", "lamellar_helmet_b", [("lamellar_helmet_b",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["khergit_guard_helmet", "lamellar_helmet_a", [("lamellar_helmet_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["leather_cap", "leather_cap_a_new", [("leather_cap_a_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["leather_steppe_cap_a", "leather_steppe_cap_a_new", [("leather_steppe_cap_a_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["leather_warrior_cap", "skull_cap_new_b", [("skull_cap_new_b",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["magyar_helmet_a", "magyar_helmet_a", [("alman_flat_helmet",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["mail_coif", "mail_coif_new", [("mail_coif_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["nasal_helmet", "nasal_helmet_b", [("nasal_helmet_b",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["nomad_cap", "nomad_cap_a_new", [("nomad_cap_a_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["nordic_fighter_helmet", "Helmet_B", [("Helmet_B",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["nordic_helmet", "helmet_w_eyeguard_new", [("helmet_w_eyeguard_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["norman_helmet", "norman_helmet_a", [("norman_helmet_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["padded_coif", "padded_coif_a_new", [("padded_coif_a_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["rus_helmet_a", "rus_helmet_a", [("vaeg_helmet9",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["segmented_helmet", "segmented_helm_new", [("segmented_helm_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["skullcap", "skull_cap_new_a", [("skull_cap_new_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["straw_hat", "straw_hat_new", [("straw_hat_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["turret_hat_green", "barbette_new", [("barbette_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["vaegir_mask", "vaeg_helmet9", [("vaeg_helmet9",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["vaegir_war_helmet", "vaeg_helmet6", [("vaeg_helmet6",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["winged_great_helmet", "maciejowski_helmet_new", [("maciejowski_helmet_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["woolen_cap", "woolen_cap_new", [("woolen_cap_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],

    #["ankle_boots", "ankle_boots_a_new", [("ankle_boots_a_new",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["black_greaves", "black_greaves", [("iron_greaves_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["blue_hose", "blue_hose_a", [("blue_hose_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["bride_shoes", "bride_shoes", [("bride_shoes",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["hide_boots", "hide_boots_a", [("hide_boots_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["hunter_boots", "hunter_boots_a", [("hunter_boots_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["iron_greaves", "iron_greaves_a", [("iron_greaves_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    ["khergit_guard_boots", "lamellar_boots_a", [("lamellar_boots_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["khergit_leather_boots", "khergit_leather_boots", [("khergit_leather_boots",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["leather_boots", "leather_boots_a", [("leather_boots_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["mail_boots", "mail_boots_a", [("mail_boots_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["mail_chausses", "mail_chausses_a", [("mail_chausses_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["nomad_boots", "nomad_boots_a", [("nomad_boots_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["plate_boots", "plate_boots", [("plate_boots",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["sarranid_boots_a", "sarranid_shoes", [("sarranid_shoes",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["sarranid_boots_b", "sarranid_boots", [("sarranid_boots",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["splinted_greaves", "splinted_greaves_a", [("splinted_greaves_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["splinted_leather_greaves", "leather_greaves_a", [("leather_greaves_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["woolen_hose", "woolen_hose_a", [("woolen_hose_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["wrapping_boots", "wrapping_boots_a", [("wrapping_boots_a",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],

    #["gauntlets", "gauntlets_L", [("gauntlets_L",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["lamellar_gauntlets", "scale_gauntlets_a_L", [("scale_gauntlets_a_L",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["leather_gloves", "leather_gloves_L", [("leather_gloves_L",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["mail_mittens", "mail_mittens_L", [("mail_mittens_L",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],
    #["scale_gauntlets", "scale_gauntlets_b_L", [("scale_gauntlets_b_L",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],

########################################################################################################################
# SPECIAL ITEMS USED BY THE GAME IN UNIQUE CIRCUMSTANCES
########################################################################################################################

    ["mail_boots_for_tableau", "{!}Boots", [("mail_boots_a",0)], itp_type_foot_armor|itp_attach_armature, 0, 1, weight(1), imodbits_none],
    ["heraldic_mail_with_surcoat_for_tableau", "{!}Mail", [("heraldic_armor_new_a",0)], itp_type_body_armor|itp_covers_legs, 0, 1, weight(1), imodbits_none, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":agent_no", ":troop_no")])]],

    ["bride_crown", "{!}Crown", [("bride_crown",0)], itp_type_head_armor|itp_civilian|itp_attach_armature|itp_doesnt_cover_hair, 0, 1, weight(1), imodbits_none],
    ["bride_dress", "{!}Dress", [("bride_dress",0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 1, weight(1), imodbits_none],
    ["bride_shoes", "{!}Shoes", [("bride_shoes",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 1, weight(1), imodbits_none],

    #["strange_helmet", "Strange Helmet", [("samurai_helmet",0)], itp_type_head_armor, 0, 455, weight(3.5)|head_armor(26)|difficulty( 8), imodbits_armor],
    #["strange_armor", "Strange Armor", [("samurai_armor",0)], itp_type_body_armor|itp_covers_legs, 0, 1620, weight(18)|body_armor(36)|leg_armor(8)|difficulty(10), imodbits_armor],
    #["strange_boots", "Strange Boots", [("samurai_boots",0)], itp_type_foot_armor|itp_attach_armature, 0, 840, weight(7)|abundance(50)|leg_armor(24)|difficulty(8), imodbits_armor],
    #["strange_short_sword", "Strange Short Sword", [("wakizashi",0), ("wakizashi_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_wakizashi|itcf_show_holster_when_drawn, 321, weight(1.25)|spd_rtng(108)|weapon_length(65)|swing_damage(25, cut)|thrust_damage(19, pierce),imodbits_weapon],
    #["strange_sword", "Strange Sword", [("katana",0), ("katana_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_primary, itc_bastardsword|itcf_carry_katana|itcf_show_holster_when_drawn, 679, weight(2.0)|difficulty(8)|spd_rtng(108)|weapon_length(95)|swing_damage(32 , cut)|thrust_damage(18, pierce),imodbits_weapon],
    #["strange_great_sword", "Strange Great Sword", [("no_dachi",0), ("no_dachi_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back|itcf_show_holster_when_drawn, 920, weight(3.5)|difficulty(11)|spd_rtng(92)|weapon_length(125)|swing_damage(38, cut),imodbits_weapon],

    ["lyre", "Lyre", [("lyre",0)], itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back, 510, weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90), imodbits_none],
    ["lute", "Lute", [("lute",0)], itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back, 450, weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90), imodbits_none],
    ["mandolin", "Mandolin", [("pellagus_mandolin", 0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itcf_carry_sword_back|itc_sabre_2h, 720, weight(1.50)|spd_rtng(110)|weapon_length(65)|swing_damage(15, blunt), imodbits_none, [
      (ti_on_weapon_attack, [
        (play_sound_at_position, "snd_gsh", pos1),
      ]),
    ], []],

    ["torch","Torch",[("rathos_torch",0)],itp_type_one_handed_wpn|itp_secondary|itp_wooden_parry|itp_wooden_attack,itc_sabre_1h,1,abundance(100)|weight(1.50)|difficulty(0)|spd_rtng(100)|weapon_length(64)|swing_damage(12,blunt),imodbits_none,[
      (ti_on_init_item, [
        (set_position_delta,0,60,0),
        (particle_system_add_new, "psys_torch_fire"),
        (particle_system_add_new, "psys_torch_smoke"),
        (set_current_color,150, 130, 70),
        (add_point_light, 10, 30),
      ]),
    ], []],

    # Loot generation items (one for each set of imodbit constants).
    # We're using itp_type_animal item type (which is not used anywhere in the game).
    ["loot_generator_horse",  "loot_generator_horse",  [("invalid_item", 0)], itp_type_animal|itp_merchandise, 0, 1000, abundance(100), imodbits_horse],
    ["loot_generator_weapon", "loot_generator_weapon", [("invalid_item", 0)], itp_type_animal|itp_merchandise, 0, 1000, abundance(100), imodbits_weapon],
    ["loot_generator_ammo",   "loot_generator_ammo",   [("invalid_item", 0)], itp_type_animal|itp_merchandise, 0, 1000, abundance(100), imodbits_ammo],
    ["loot_generator_shield", "loot_generator_shield", [("invalid_item", 0)], itp_type_animal|itp_merchandise, 0, 1000, abundance(100), imodbits_shield],
    ["loot_generator_ranged", "loot_generator_ranged", [("invalid_item", 0)], itp_type_animal|itp_merchandise, 0, 1000, abundance(100), imodbits_ranged],
    ["loot_generator_armor",  "loot_generator_armor",  [("invalid_item", 0)], itp_type_animal|itp_merchandise, 0, 1000, abundance(100), imodbits_armor],
    ["loot_generator_cloth",  "loot_generator_cloth",  [("invalid_item", 0)], itp_type_animal|itp_merchandise, 0, 1000, abundance(100), imodbits_cloth_low],

########################################################################################################################
# PRACTICE, ARENA AND TOURNAMENT ITEMS
########################################################################################################################

    ["practice_sword","Practice Sword", [("lav_practice_sword_1h",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack, itc_sword_1h, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(22,blunt)|thrust_damage(20,blunt),imodbits_none],
    ["heavy_practice_sword","Heavy Practice Sword", [("lav_practice_sword_2h",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_sword_2h,    21, weight(6.25)|spd_rtng(94)|weapon_length(128)|swing_damage(30,blunt)|thrust_damage(24,blunt),imodbits_none],
    ["practice_dagger","Practice Dagger", [("practice_dagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry|itp_wooden_attack, itc_dagger|itcf_carry_dagger_front_left, 2,weight(0.5)|spd_rtng(110)|weapon_length(47)|swing_damage(16,blunt)|thrust_damage(14,blunt),imodbits_none],
    ["practice_axe", "Practice Axe", [("one_handed_war_axe_a",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_sabre_1h|itcf_carry_axe_left_hip, 24 , weight(2) | spd_rtng(95) | weapon_length(75) | swing_damage(24, blunt) | thrust_damage(0, pierce), imodbits_weapon],
    ["practice_staff","Practice Staff", [("luc2_wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(2.5)|spd_rtng(103) | weapon_length(118)|swing_damage(18,blunt) | thrust_damage(18,blunt),imodbits_none],
    ["practice_lance","Practice Lance", [("lav_lance_joust_f230",0)], itp_couchable|itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_lance, 18,weight(4.25)|spd_rtng(58)|weapon_length(240)|swing_damage(0,blunt)|thrust_damage(15,blunt),imodbits_none],
    ["practice_shield","Practice Shield", [("shield_round_g",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 20,weight(3.5)|body_armor(1)|hit_points(200)|spd_rtng(100)|shield_width(50),imodbits_none],
    ["practice_bow","Practice Bow", [("lav_bow_common_hunting",0), ("hunting_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1.5)|spd_rtng(90) | shoot_speed(40) | thrust_damage(21, blunt),imodbits_weapon ],
    ["practice_crossbow", "Practice Crossbow", [("crossbow_a",0)], itp_type_crossbow |itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0, weight(3)|spd_rtng(42)| shoot_speed(68) | thrust_damage(32,blunt)|max_ammo(1),imodbits_weapon],
    ["practice_javelin", "Practice Javelins", [("javelin",0),("javelins_quiver_new", ixmesh_carry)], itp_type_thrown |itp_primary|itp_next_item_as_melee,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 0, weight(5) | spd_rtng(91) | shoot_speed(28) | thrust_damage(27, blunt) | max_ammo(50) | weapon_length(75), imodbits_none],
    ["practice_javelin_melee", "practice_javelin_melee", [("javelin",0)], itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry , itc_halberd, 0, weight(1)|difficulty(0)|spd_rtng(91) |swing_damage(12, blunt)| thrust_damage(14,  blunt)|weapon_length(75),imodbits_weapon ],
    ["practice_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16, blunt)|max_ammo(10)|weapon_length(0),imodbits_none],
    ["practice_throwing_daggers_100_amount", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16, blunt)|max_ammo(100)|weapon_length(0),imodbits_none],
    ["practice_horse","Practice Horse", [("saddle_horse",0)], itp_type_horse, 0, 37,body_armor(10)|horse_speed(40)|horse_maneuver(37)|horse_charge(14),imodbits_none],
    ["practice_arrows","Practice Arrows", [("arena_arrow",0),("flying_missile",ixmesh_flying_ammo),("arena_quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_none],
    ["practice_bolts","Practice Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit.large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|weapon_length(55)|max_ammo(49),imodbits_none],
    ["practice_arrows_10_amount","Practice Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("arena_quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(10),imodbits_none],
    ["practice_arrows_100_amount","Practice Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("arena_quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(100),imodbits_none],
    ["practice_bolts_9_amount","Practice Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit.large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|weapon_length(55)|max_ammo(9),imodbits_none],
    ["practice_boots", "Practice Boots", [("hide_boots_a",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 40, weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4), imodbits_armor ],
    ["practice_bow_2","Practice Bow", [("lav_bow_common_hunting",0), ("hunting_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1.5)|spd_rtng(90) | shoot_speed(40) | thrust_damage(21, blunt),imodbits_weapon ],
    ["practice_arrows_2","Practice Arrows", [("arena_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_none],

    ["arena_lance", "Lance", [("arena_lance",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_lance|itcf_carry_spear, 90 , weight(2.5)|spd_rtng(96) | weapon_length(150)|swing_damage(20 , blunt) | thrust_damage(25 ,  blunt),imodbits_weapon ],

    ["arena_armor_red", "Arena Armor Red", [("arena_armorR_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
    ["arena_armor_blue", "Arena Armor Blue", [("arena_armorB_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
    ["arena_armor_green", "Arena Armor Green", [("arena_armorG_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
    ["arena_armor_yellow", "Arena Armor Yellow", [("arena_armorY_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
    ["arena_tunic_white", "Arena Tunic White ", [("arena_tunicW_new",0)], itp_type_body_armor |itp_covers_legs ,0, 47 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_armor ],
    ["arena_tunic_red", "Arena Tunic Red", [("arena_tunicR_new",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_armor ],
    ["arena_tunic_blue", "Arena Tunic Blue", [("arena_tunicB_new",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_armor ],
    ["arena_tunic_green", "Arena Tunic Green", [("arena_tunicG_new",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_armor ],
    ["arena_tunic_yellow", "Arena Tunic Yellow", [("arena_tunicY_new",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_armor ],

    ["red_tourney_helmet","Red Tourney Helmet",[("arena_helmetR",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
    ["blue_tourney_helmet","Blue Tourney Helmet",[("arena_helmetB",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
    ["green_tourney_helmet","Green Tourney Helmet",[("arena_helmetG",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
    ["gold_tourney_helmet","Gold Tourney Helmet",[("arena_helmetY",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
    ["arena_helmet_red", "Arena Helmet Red", [("arena_helmetR",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_armor ],
    ["arena_helmet_blue", "Arena Helmet Blue", [("arena_helmetB",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_armor ],
    ["arena_helmet_green", "Arena Helmet Green", [("arena_helmetG",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_armor ],
    ["arena_helmet_yellow", "Arena Helmet Yellow", [("arena_helmetY",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_armor ],
    ["steppe_helmet_red", "Steppe Helmet Red", [("steppe_helmetR",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_armor ],
    ["steppe_helmet_blue", "Steppe Helmet Blue", [("steppe_helmetB",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_armor ],
    ["steppe_helmet_green", "Steppe Helmet Green", [("steppe_helmetG",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_armor ],
    ["steppe_helmet_yellow", "Steppe Helmet Yellow", [("steppe_helmetY",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_armor ],
    ["tourney_helm_red", "Tourney Helm Red", [("tourney_helmR",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_armor ],
    ["tourney_helm_blue", "Tourney Helm Blue", [("tourney_helmB",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_armor ],
    ["tourney_helm_green", "Tourney Helm Green", [("tourney_helmG",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_armor ],
    ["tourney_helm_yellow", "Tourney Helm Yellow", [("tourney_helmY",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_armor ],
    ["arena_turban_red", "Arena Turban", [("tuareg_open",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_armor ],
    ["arena_turban_blue", "Arena Turban", [("tuareg_open",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_armor ],
    ["arena_turban_green", "Arena Turban", [("tuareg_open",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_armor ],
    ["arena_turban_yellow", "Arena Turban", [("tuareg_open",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_armor ],

    ["arena_shield_red", "Shield", [("arena_shield_red",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|shield_width(60),imodbits_shield ],
    ["arena_shield_blue", "Shield", [("arena_shield_blue",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|shield_width(60),imodbits_shield ],
    ["arena_shield_green", "Shield", [("arena_shield_green",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|shield_width(60),imodbits_shield ],
    ["arena_shield_yellow", "Shield", [("arena_shield_yellow",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|shield_width(60),imodbits_shield ],

    #["arena_axe", "Axe", [("arena_axe",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 137 , weight(1.5)|spd_rtng(100) | weapon_length(69)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_weapon ],
    #["arena_sword", "Sword", [("arena_sword_one_handed",0),("sword_medieval_b_scabbard", ixmesh_carry),], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 243 , weight(1.5)|spd_rtng(99) | weapon_length(95)|swing_damage(22 , blunt) | thrust_damage(20 ,  blunt),imodbits_weapon ],
    #["arena_sword_two_handed", "Two Handed Sword", [("arena_sword_two_handed",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 670 , weight(2.75)|spd_rtng(93) | weapon_length(110)|swing_damage(30 , blunt) | thrust_damage(24 ,  blunt),imodbits_weapon ],
    #["red_tourney_armor","Red Tourney Armor", [("tourn_armor_a",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
    #["blue_tourney_armor","Blue Tourney Armor", [("mail_shirt",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
    #["green_tourney_armor","Green Tourney Armor", [("leather_vest",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
    #["gold_tourney_armor","Gold Tourney Armor", [("padded_armor",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
    #["arena_armor_white", "Arena Armor White", [("arena_armorW_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
    #["steppe_helmet_white", "Steppe Helmet White", [("steppe_helmetW",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_armor ],
    #["tourney_helm_white", "Tourney Helm White", [("tourney_helmR",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_armor ],

########################################################################################################################
# BOOKS
########################################################################################################################

    ["books_begin", "{!}marker", [("invalid_item", 0)], itp_type_goods, 0, 0, weight(1), imodbits_none], 

    # Skill books

    ["book_tactics","De Re Militari", [("book_a",0)], itp_type_book|itp_merchandise, 0, 4000,weight(2)|abundance(100),imodbits_none],
    ["book_persuasion","Rhetorica ad Herennium", [("book_b",0)], itp_type_book|itp_merchandise, 0, 5000,weight(2)|abundance(100),imodbits_none],
    ["book_leadership","The Life of Alixenus the Great", [("book_d",0)], itp_type_book|itp_merchandise, 0, 4200,weight(2)|abundance(100),imodbits_none],
    ["book_intelligence","Essays on Logic", [("book_e",0)], itp_type_book|itp_merchandise, 0, 2900,weight(2)|abundance(100),imodbits_none],
    ["book_trade","A Treatise on the Value of Things", [("book_f",0)], itp_type_book|itp_merchandise, 0, 3100,weight(2)|abundance(100),imodbits_none],
    ["book_weapon_mastery", "On the Art of Fighting with Swords", [("book_d",0)], itp_type_book|itp_merchandise, 0, 4200,weight(2)|abundance(100),imodbits_none],
    ["book_engineering","Method of Mechanical Theorems", [("book_open",0)], itp_type_book|itp_merchandise, 0, 4000,weight(2)|abundance(100),imodbits_none],

    # Reference books

    ["book_wound_treatment_reference","The Book of Healing", [("book_c",0)], itp_type_book|itp_merchandise, 0, 3500,weight(2)|abundance(10),imodbits_none],
    ["book_training_reference","Manual of Arms", [("book_open",0)], itp_type_book|itp_merchandise, 0, 3500,weight(2)|abundance(10),imodbits_none],
    ["book_surgery_reference","The Great Book of Surgery", [("book_c",0)], itp_type_book|itp_merchandise, 0, 3500,weight(2)|abundance(10),imodbits_none],

    ["books_end", "{!}endmarker", [("invalid_item", 0)], itp_type_goods, 0, 0, weight(1), imodbits_none], 

########################################################################################################################
# GOODS AND FOODS
########################################################################################################################

    ["goods_begin", "{!}marker", [("invalid_item", 0)], itp_type_goods, 0, 0, weight(1), imodbits_none], 

    # Trade Goods

    ["goods_spice",   "Spice",       [("spice_sack",0)],            itp_merchandise|itp_type_goods, 0,  880, weight(40)|abundance( 25), imodbit.pungent|imodbit.old|imodbit.decent|imodbit.fine|imodbit.appetizing|imodbit.refined|imodbit.delicious|imodbit.exquisite|imodbit.delectable|imodbit.lordly|imodbit.exotic|imodbit.large_bag],
    ["goods_salt",    "Salt",        [("salt_sack",0)],             itp_merchandise|itp_type_goods, 0,  255, weight(50)|abundance(120), imodbit.fine|imodbit.refined|imodbit.flavored|imodbit.large_bag],
    ["goods_oil",     "Oil",         [("oil",0)],                   itp_merchandise|itp_type_goods, 0,  450, weight(50)|abundance( 60), imodbit.pungent|imodbit.crude|imodbit.old|imodbit.decent|imodbit.fine|imodbit.appetizing|imodbit.refined|imodbit.flavored|imodbit.delicious|imodbit.exquisite|imodbit.delectable|imodbit.lordly|imodbit.exotic],
    ["goods_pottery", "Pottery",     [("jug",0)],                   itp_merchandise|itp_type_goods, 0,  100, weight(50)|abundance( 90), imodbit.battered|imodbit.cracked|imodbit.makeshift|imodbit.shabby|imodbit.crude|imodbit.old|imodbit.tarnished|imodbit.chipped|imodbit.decent|imodbit.sturdy|imodbit.fine|imodbit.tough|imodbit.elegant|imodbit.hardened|imodbit.flawless|imodbit.superior|imodbit.exquisite|imodbit.tempered|imodbit.lordly|imodbit.masterwork],
    ["goods_flax",    "Flax Bundle", [("raw_flax",0)],              itp_merchandise|itp_type_goods, 0,  150, weight(40)|abundance( 90), imodbit.battered|imodbit.shabby|imodbit.crude|imodbit.old|imodbit.decent|imodbit.sturdy|imodbit.fine|imodbit.refined|imodbit.superior],
    ["goods_linen",   "Linen",       [("linen",0)],                 itp_merchandise|itp_type_goods, 0,  250, weight(40)|abundance( 90), imodbit.battered|imodbit.shabby|imodbit.crude|imodbit.old|imodbit.tarnished|imodbit.decent|imodbit.sturdy|imodbit.fine|imodbit.tough|imodbit.elegant|imodbit.hardened],
    ["goods_wool",    "Wool",        [("wool_sack",0)],             itp_merchandise|itp_type_goods, 0,  130, weight(40)|abundance( 90), imodbit.shabby|imodbit.crude|imodbit.old|imodbit.decent|imodbit.sturdy|imodbit.fine|imodbit.refined|imodbit.superior|imodbit.large_bag],
    ["goods_cloth",   "Wool Cloth",  [("wool_cloth",0)],            itp_merchandise|itp_type_goods, 0,  250, weight(40)|abundance( 90), imodbit.battered|imodbit.shabby|imodbit.crude|imodbit.old|imodbit.tarnished|imodbit.decent|imodbit.sturdy|imodbit.fine|imodbit.tough|imodbit.elegant|imodbit.hardened],
    ["goods_silk",    "Raw Silk",    [("raw_silk_bundle",0)],       itp_merchandise|itp_type_goods, 0,  600, weight(30)|abundance( 90), imodbit.old|imodbit.tarnished|imodbit.decent|imodbit.sturdy|imodbit.fine|imodbit.refined|imodbit.tough|imodbit.flawless|imodbit.superior|imodbit.exquisite|imodbit.lordly],
    ["goods_dyes",    "Dyes",        [("dyes",0)],                  itp_merchandise|itp_type_goods, 0,  200, weight(10)|abundance( 90), imodbit.old|imodbit.tarnished|imodbit.decent|imodbit.fine|imodbit.refined|imodbit.flawless|imodbit.superior|imodbit.exquisite|imodbit.exotic],
    ["goods_velvet",  "Velvet",      [("velvet",0)],                itp_merchandise|itp_type_goods, 0, 1025, weight(40)|abundance( 30), imodbit.battered|imodbit.old|imodbit.tarnished|imodbit.decent|imodbit.sturdy|imodbit.fine|imodbit.elegant|imodbit.flawless|imodbit.superior|imodbit.exquisite|imodbit.lordly|imodbit.masterwork],
    ["goods_iron",    "Iron",        [("iron",0)],                  itp_merchandise|itp_type_goods, 0,  264, weight(60)|abundance( 60), imodbit.battered|imodbit.crude|imodbit.old|imodbit.decent|imodbit.sturdy|imodbit.fine|imodbit.refined|imodbit.tough|imodbit.hardened|imodbit.tempered],
    ["goods_tools",   "Tools",       [("bb_smith_hammer",0)],       itp_merchandise|itp_type_goods, 0,  410, weight(50)|abundance( 90), imodbit.battered|imodbit.bent|imodbit.cracked|imodbit.makeshift|imodbit.shabby|imodbit.crude|imodbit.old|imodbit.tarnished|imodbit.chipped|imodbit.decent|imodbit.fine|imodbit.hardened|imodbit.flawless|imodbit.superior|imodbit.tempered|imodbit.masterwork],
    ["goods_lumber",  "Lumber",      [("pellagus_timber", 0)],      itp_merchandise|itp_type_goods, 0,  204, weight(60)|abundance( 80), imodbit.battered|imodbit.cracked|imodbit.shabby|imodbit.crude|imodbit.old|imodbit.tarnished|imodbit.decent|imodbit.sturdy|imodbit.fine|imodbit.refined|imodbit.tough|imodbit.hardened|imodbit.flawless],
    ["goods_hides",   "Hides",       [("leatherwork_inventory",0)], itp_merchandise|itp_type_goods, 0,  120, weight(40)|abundance( 90), imodbit.battered|imodbit.shabby|imodbit.old|imodbit.tarnished|imodbit.decent|imodbit.sturdy|imodbit.fine|imodbit.tough|imodbit.hardened],
    ["goods_leather", "Leatherwork", [("leatherwork_frame",0)],     itp_merchandise|itp_type_goods, 0,  220, weight(40)|abundance( 90), imodbit.battered|imodbit.shabby|imodbit.crude|imodbit.old|imodbit.tarnished|imodbit.decent|imodbit.sturdy|imodbit.fine|imodbit.hardened|imodbit.flawless|imodbit.superior|imodbit.exquisite|imodbit.lordly|imodbit.masterwork],
    ["goods_furs",    "Furs",        [("fur_pack",0)],              itp_merchandise|itp_type_goods, 0,  391, weight(40)|abundance( 90), imodbit.battered|imodbit.shabby|imodbit.old|imodbit.tarnished|imodbit.decent|imodbit.sturdy|imodbit.fine|imodbit.tough|imodbit.elegant|imodbit.flawless|imodbit.superior|imodbit.exquisite|imodbit.lordly|imodbit.exotic|imodbit.large_bag],
    ["goods_gems",    "Gems",        [("pellagus_gems", 0)],                        itp_type_goods, 0, 7780, weight( 1),                imodbit.cracked|imodbit.crude|imodbit.tarnished|imodbit.chipped|imodbit.decent|imodbit.fine|imodbit.elegant|imodbit.flawless|imodbit.exquisite|imodbit.large_bag],
    ["goods_gold",    "Gold",        [("pellagus_gold_ingot", 0)],                  itp_type_goods, 0, 6000, weight(60),                imodbit.crude|imodbit.tarnished|imodbit.refined|imodbit.flawless],

    # Drinks

    ["drink_water",   "Water",   [("barrel", 0)],      itp_merchandise|itp_type_drink, 0,   25, weight(40)|abundance(100)|max_ammo(50), imodbit.pungent|imodbit.flavored|imodbit.delicious],
    ["drink_ale",     "Ale",     [("ale_barrel",0)],   itp_merchandise|itp_type_drink, 0,  120, weight(40)|abundance( 70)|max_ammo(50), imodbit.pungent|imodbit.old|imodbit.decent|imodbit.fine|imodbit.flavored|imodbit.delicious|imodbit.exquisite|imodbit.delectable|imodbit.lordly],
    ["drink_wine",    "Wine",    [("amphora_slim",0)], itp_merchandise|itp_type_drink, 0,  220, weight(30)|abundance( 60)|max_ammo(50), imodbit.pungent|imodbit.decent|imodbit.fine|imodbit.flavored|imodbit.delicious|imodbit.exquisite|imodbit.delectable|imodbit.lordly|imodbit.exotic],
    ["drink_whiskey", "Whiskey", [("pellagus_whiskey", 0)],            itp_type_drink, 0, 3910, weight(30)|               max_ammo(30), imodbits_none],

    # Foods

    ["food_apples",      "Fruits",      [("apple_basket",0)],      itp_merchandise|itp_type_food, 0,  44, weight(20)|abundance(110)|max_ammo( 50), imodbit.pungent|imodbit.old|imodbit.fine|imodbit.appetizing|imodbit.flavored|imodbit.delicious|imodbit.exquisite|imodbit.delectable|imodbit.lordly],
    ["food_grapes",      "Grapes",      [("lav_grapes_basket",0)], itp_merchandise|itp_type_food, 0,  75, weight(20)|abundance( 90)|max_ammo( 40), imodbit.pungent|imodbit.old|imodbit.fine|imodbit.appetizing|imodbit.delicious|imodbit.exquisite|imodbit.delectable|imodbit.lordly],
    ["food_olives",      "Olives",      [("lav_olives_basket",0)], itp_merchandise|itp_type_food, 0, 100, weight(15)|abundance( 90)|max_ammo( 35), imodbit.pungent|imodbit.old|imodbit.fine|imodbit.appetizing|imodbit.flavored|imodbit.delicious|imodbit.exquisite|imodbit.delectable|imodbit.lordly],
    ["food_dates",       "Dates",       [("lav_dates_basket",0)],  itp_merchandise|itp_type_food, 0, 120, weight(25)|abundance(100)|max_ammo( 50), imodbit.pungent|imodbit.old|imodbit.fine|imodbit.appetizing|imodbit.flavored|imodbit.delicious|imodbit.exquisite|imodbit.delectable|imodbit.lordly],
    ["food_garlic",      "Garlic",      [("garlic", 0)],           itp_merchandise|itp_type_food, 0,  83, weight( 5)|abundance(100)|max_ammo( 10), imodbit.old|imodbit.decent|imodbit.fine|imodbit.delicious],
    ["food_grain",       "Grain",       [("wheat_sack",0)],        itp_merchandise|itp_type_food, 0,  30, weight(30)|abundance(110)|max_ammo( 50), imodbit.pungent|imodbit.old|imodbit.fine|imodbit.refined|imodbit.large_bag],
    ["food_flour",       "Flour",       [("salt_sack",0)],         itp_merchandise|itp_type_food, 0,  40, weight(30)|abundance(120)|max_ammo( 50), imodbit.pungent|imodbit.old|imodbit.fine|imodbit.refined|imodbit.flavored|imodbit.exquisite|imodbit.large_bag],
    ["food_bread",       "Bread",       [("bread_a",0)],           itp_merchandise|itp_type_food, 0,  50, weight(30)|abundance(110)|max_ammo( 50), imodbit.old|imodbit.decent|imodbit.fine|imodbit.appetizing|imodbit.flavored|imodbit.delicious|imodbit.exquisite],
    ["food_fish_fresh",  "Fish",        [("fish_a", 0)],           itp_merchandise|itp_type_food, 0,   1, weight(15)|abundance(100)|max_ammo( 40), imodbit.pungent|imodbit.old|imodbit.fine|imodbit.appetizing|imodbit.delicious|imodbit.exquisite|imodbit.delectable|imodbit.lordly|imodbit.exotic],
    ["food_fish_fried",  "Fried Fish",  [("fish_roasted_a", 0)],   itp_merchandise|itp_type_food, 0,   1, weight(15)|abundance(100)|max_ammo( 40), imodbit.pungent|imodbit.old|imodbit.fine|imodbit.appetizing|imodbit.flavored|imodbit.delicious|imodbit.exquisite|imodbit.delectable|imodbit.lordly|imodbit.exotic],
    ["food_fish_smoked", "Smoked Fish", [("smoked_fish",0)],       itp_merchandise|itp_type_food, 0,  65, weight(15)|abundance(110)|max_ammo( 50), imodbit.old|imodbit.fine|imodbit.appetizing|imodbit.delicious|imodbit.exquisite],
    ["food_cheese",      "Cheese",      [("cheese_b",0)],          itp_merchandise|itp_type_food, 0,  75, weight( 6)|abundance(110)|max_ammo( 30), imodbit.pungent|imodbit.old|imodbit.decent|imodbit.fine|imodbit.appetizing|imodbit.refined|imodbit.flavored|imodbit.delicious|imodbit.exquisite|imodbit.delectable|imodbit.lordly],
    ["food_honey",       "Honey",       [("honey_pot",0)],         itp_merchandise|itp_type_food, 0, 220, weight( 5)|abundance(110)|max_ammo( 30), imodbit.old|imodbit.fine|imodbit.appetizing|imodbit.flavored|imodbit.delicious|imodbit.exquisite|imodbit.delectable|imodbit.lordly],
    ["food_sausages",    "Sausages",    [("sausages",0)],          itp_merchandise|itp_type_food, 0,  85, weight(10)|abundance(110)|max_ammo( 40), imodbit.pungent|imodbit.old|imodbit.decent|imodbit.fine|imodbit.appetizing|imodbit.flavored|imodbit.delicious|imodbit.exquisite|imodbit.delectable|imodbit.lordly],
    ["food_cabbages",    "Cabbages",    [("cabbage",0)],           itp_merchandise|itp_type_food, 0,  30, weight(15)|abundance(110)|max_ammo( 50), imodbit.pungent|imodbit.old|imodbit.fine|imodbit.appetizing],
    ["food_meat_dry",    "Dried Meat",  [("smoked_meat",0)],       itp_merchandise|itp_type_food, 0,  85, weight(15)|abundance(100)|max_ammo( 50), imodbit.pungent|imodbit.old|imodbit.fine|imodbit.appetizing|imodbit.flavored|imodbit.delicious],
    ["food_hardtack",    "Hardtack",    [("bread_slice_a", 0)],    itp_merchandise|itp_type_food, 0, 100, weight( 5)|abundance(110)|max_ammo(150), imodbit.fine|imodbit.flavored],
    ["food_beef",        "Beef",        [("raw_meat",0)],          itp_merchandise|itp_type_food, 0,  80, weight(20)|abundance(100)|max_ammo( 50), imodbits_none],
    ["food_chicken",     "Chicken",     [("chicken",0)],           itp_merchandise|itp_type_food, 0,  95, weight(10)|abundance(110)|max_ammo( 50), imodbit.pungent|imodbit.old|imodbit.fine|imodbit.appetizing|imodbit.delicious|imodbit.exquisite],
    ["food_pork",        "Pork",        [("pork",0)],              itp_merchandise|itp_type_food, 0,  75, weight(15)|abundance(100)|max_ammo( 50), imodbit.pungent|imodbit.old|imodbit.fine|imodbit.appetizing|imodbit.flavored|imodbit.delicious|imodbit.exquisite|imodbit.delectable|imodbit.lordly],
    ["food_butter",      "Butter",      [("butter_pot",0)],        itp_merchandise|itp_type_food, 0, 150, weight( 6)|abundance(110)|max_ammo( 30), imodbit.pungent|imodbit.old|imodbit.fine|imodbit.appetizing|imodbit.refined|imodbit.flavored|imodbit.delicious|imodbit.exquisite|imodbit.delectable|imodbit.lordly],

    ["goods_end", "{!}endmarker", [("invalid_item", 0)], itp_type_goods, 0, 0, weight(1), imodbits_none], 

    # Quest Items

    ["quest_supply",   "Supplies",         [("box_a",0)],                      itp_type_goods, 0,   96, weight(50), imodbits_none],
    ["quest_wine",     "Wine Delivery",    [("amphora_slim",0)],               itp_type_goods, 0,   46, weight(30), imodbits_none],
    ["quest_ale",      "Ale Delivery",     [("wine_barrel",0)],                itp_type_goods, 0,   31, weight(40), imodbits_none],
    ["quest_portrait", "Strange Portrait", [("pellagus_strange_portrait", 0)], itp_type_goods, 0, 7215, weight( 2), imodbits_none],

########################################################################################################################
# HORSES
########################################################################################################################

    ["horses_begin", "{!}marker", [("invalid_item", 0)], itp_type_goods, 0, 0, weight(1), imodbits_none], 

    # Common horses
    ["donkey_a","Donkey",[("wanderer_donkey_mount",0)],itp_type_horse|itp_merchandise,0,210,abundance(100)|hit_points(90)|body_armor(15)|difficulty(0)|horse_speed(30)|horse_maneuver(54)|horse_charge(8)|horse_scale(80),imodbits_horse_basic,[],[]],
    ["donkey_b","Donkey",[("wanderer_donkey_mount2",0)],itp_type_horse|itp_merchandise,0,210,abundance(100)|hit_points(90)|body_armor(15)|difficulty(0)|horse_speed(30)|horse_maneuver(54)|horse_charge(8)|horse_scale(80),imodbits_horse_basic,[],[]],
    ["mule","Mule",[("wanderer_mule",0)],itp_type_horse|itp_merchandise,0,250,abundance(100)|hit_points(100)|body_armor(14)|difficulty(0)|horse_speed(35)|horse_maneuver(46)|horse_charge(10)|horse_scale(90),imodbits_horse_basic,[],[]],
    ["farm_horse","Farm Horse",[("sumpter_horse",0)],itp_type_horse|itp_merchandise,0,290,abundance(100)|hit_points(120)|body_armor(12)|difficulty(1)|horse_speed(34)|horse_maneuver(44)|horse_charge(12)|horse_scale(105),imodbits_horse_basic,[],[]],
    ["riding_horse","Riding Horse",[("saddle_horse",0)],itp_type_horse|itp_merchandise,0,410,abundance(100)|hit_points(100)|body_armor(10)|difficulty(1)|horse_speed(48)|horse_maneuver(48)|horse_charge(14)|horse_scale(100),imodbits_horse_basic,[],[]],
    ["courser_horse","Courser",[("courser",0)],itp_type_horse|itp_merchandise,0,520,abundance(90)|hit_points(100)|body_armor(14)|difficulty(2)|horse_speed(52)|horse_maneuver(42)|horse_charge(15)|horse_scale(100),imodbits_horse_basic,[],[]],
    ["hunter_horse","Hunter",[("hunting_horse",0)],itp_type_horse|itp_merchandise,0,630,abundance(80)|hit_points(110)|body_armor(18)|difficulty(3)|horse_speed(40)|horse_maneuver(50)|horse_charge(20)|horse_scale(100),imodbits_horse_basic,[],[]],
    ["armored_courser","Armored Courser",[("pellagus_new_courser_1",0)],itp_type_horse|itp_merchandise,0,690,abundance(80)|hit_points(100)|body_armor(20)|difficulty(2)|horse_speed(50)|horse_maneuver(42)|horse_charge(18)|horse_scale(100),imodbits_horse_basic,[],[]],
    ["armored_hunter","Armored Hunter",[("pellagus_new_hunting_horse_1",0)],itp_type_horse|itp_merchandise,0,960,abundance(70)|hit_points(110)|body_armor(28)|difficulty(3)|horse_speed(39)|horse_maneuver(50)|horse_charge(24)|horse_scale(100),imodbits_horse_basic,[],[]],

    # Swadian horses
    ["swadian_warhorse_a","Swadian Cavalry Warhorse",[("pellagus_barded_charger1",0)],itp_type_horse|itp_merchandise,0,1580,abundance(60)|hit_points(110)|body_armor(37)|difficulty(3)|horse_speed(40)|horse_maneuver(44)|horse_charge(35)|horse_scale(105),imodbits_horse_basic,[],[fac.kingdom_1]],
    ["swadian_warhorse_b","Swadian Squire Warhorse",[("pellagus_barded_charger2",0)],itp_type_horse|itp_merchandise,0,2040,abundance(50)|hit_points(110)|body_armor(41)|difficulty(4)|horse_speed(40)|horse_maneuver(46)|horse_charge(38)|horse_scale(108),imodbits_horse_basic,[],[fac.kingdom_1]],
    ["swadian_warhorse_c","Swadian Knight Warhorse",[("pellagus_barded_charger4",0)],itp_type_horse|itp_merchandise,0,2670,abundance(40)|hit_points(110)|body_armor(45)|difficulty(4)|horse_speed(42)|horse_maneuver(45)|horse_charge(42)|horse_scale(110),imodbits_horse_basic,[],[fac.kingdom_1]],
    ["swadian_warhorse_d","Templar Warhorse",[("pellagus_barded_charger3",0)],itp_type_horse|itp_merchandise,0,3310,abundance(20)|hit_points(110)|body_armor(48)|difficulty(5)|horse_speed(44)|horse_maneuver(48)|horse_charge(40)|horse_scale(111),imodbits_horse_basic,[],[fac.kingdom_1]],
    ["swadian_warhorse_e","Templar Warhorse",[("pellagus_barded_charger5",0)],itp_type_horse|itp_merchandise,0,3670,abundance(20)|hit_points(110)|body_armor(50)|difficulty(5)|horse_speed(45)|horse_maneuver(42)|horse_charge(46)|horse_scale(111),imodbits_horse_basic,[],[fac.kingdom_1]],
    ["swadian_charger_a","Swadian Charger",[("charger_plate",0)],itp_type_horse|itp_merchandise,0,3980,abundance(30)|hit_points(120)|body_armor(58)|difficulty(5)|horse_speed(39)|horse_maneuver(38)|horse_charge(52)|horse_scale(110),imodbits_horse_basic,[],[fac.kingdom_1]],
    ["swadian_charger_b","Swadian Noble Charger",[("njunja_charger_plate_white",0)],itp_type_horse,0,5890,abundance(10)|hit_points(120)|body_armor(65)|difficulty(6)|horse_speed(40)|horse_maneuver(40)|horse_charge(58)|horse_scale(113),imodbits_horse_basic,[],[fac.kingdom_1]],
    ["swadian_horse_royal","Katilus' Royal Charger",[("spak_horny_charger_plate",0)],itp_type_horse|itp_unique,0,8730,abundance(0)|hit_points(150)|body_armor(70)|difficulty(6)|horse_speed(45)|horse_maneuver(44)|horse_charge(60)|horse_scale(115),imodbits_horse_basic,[],[fac.kingdom_1]],

    # Vaegir horses
    ["vaegir_warhorse_a","Vaegir Warhorse",[("pellagus_scale_armour_charger_silver",0)],itp_type_horse|itp_merchandise,0,1860,abundance(60)|hit_points(110)|body_armor(40)|difficulty(3)|horse_speed(41)|horse_maneuver(48)|horse_charge(36)|horse_scale(106),imodbits_horse_basic,[],[fac.kingdom_2]],
    ["vaegir_warhorse_b","Vaegir Noble Warhorse",[("pellagus_scale_armour_charger_gold",0)],itp_type_horse|itp_merchandise,0,2720,abundance(40)|hit_points(110)|body_armor(48)|difficulty(4)|horse_speed(44)|horse_maneuver(46)|horse_charge(38)|horse_scale(107),imodbits_horse_basic,[],[fac.kingdom_2]],
    ["vaegir_warhorse_c","Vaegir Lamellar Warhorse",[("lucas_lamellar_armor_horse",0)],itp_type_horse|itp_merchandise,0,3700,abundance(20)|hit_points(110)|body_armor(56)|difficulty(5)|horse_speed(42)|horse_maneuver(40)|horse_charge(45)|horse_scale(109),imodbits_horse_basic,[],[fac.kingdom_2]],
    ["vaegir_horse_royal","Yaroglek's Battle Horse",[("spak_2imperial_warhorse",0)],itp_type_horse|itp_unique,0,6440,abundance(0)|hit_points(140)|body_armor(52)|difficulty(4)|horse_speed(53)|horse_maneuver(52)|horse_charge(50)|horse_scale(108),imodbits_horse_basic,[],[fac.kingdom_2]],

    # Khergit horses
    ["khergit_horse","Steppe Horse",[("steppe_horse",0)],itp_type_horse|itp_merchandise,0,570,abundance(80)|hit_points(100)|body_armor(15)|difficulty(2)|horse_speed(45)|horse_maneuver(54)|horse_charge(14)|horse_scale(98),imodbits_horse_basic,[],[fac.kingdom_3]],
    ["khergit_warhorse_a","Khergit Warhorse",[("warhorse",0)],itp_type_horse|itp_merchandise,0,1650,abundance(60)|hit_points(100)|body_armor(38)|difficulty(3)|horse_speed(42)|horse_maneuver(48)|horse_charge(34)|horse_scale(103),imodbits_horse_basic,[],[fac.kingdom_3]],
    ["khergit_warhorse_b","Khergit Lamellar Warhorse",[("warhorse_steppe",0)],itp_type_horse|itp_merchandise,0,3140,abundance(50)|hit_points(120)|body_armor(58)|difficulty(4)|horse_speed(40)|horse_maneuver(45)|horse_charge(41)|horse_scale(109),imodbits_horse_basic,[],[fac.kingdom_3]],
    ["khergit_warhorse_c","Khergit Noble Warhorse",[("njunja_steppe_charger_iron",0)],itp_type_horse,0,5160,abundance(10)|hit_points(130)|body_armor(64)|difficulty(5)|horse_speed(38)|horse_maneuver(45)|horse_charge(48)|horse_scale(115),imodbits_horse_basic,[],[fac.kingdom_3]],
    ["khergit_charger_a","Khergit Charger",[("charger",0)],itp_type_horse|itp_merchandise,0,2400,abundance(50)|hit_points(110)|body_armor(42)|difficulty(3)|horse_speed(40)|horse_maneuver(43)|horse_charge(47)|horse_scale(106),imodbits_horse_basic,[],[fac.kingdom_3]],
    ["khergit_charger_b","Khergit Cataphract",[("charger_new",0)],itp_type_horse|itp_merchandise,0,3000,abundance(40)|hit_points(120)|body_armor(46)|difficulty(4)|horse_speed(39)|horse_maneuver(40)|horse_charge(51)|horse_scale(110),imodbits_horse_basic,[],[fac.kingdom_3]],
    ["khergit_charger_c","Khergit Lamellar Cataphract",[("njunja_charger_new_steel",0)],itp_type_horse|itp_merchandise,0,3860,abundance(20)|hit_points(120)|body_armor(52)|difficulty(5)|horse_speed(38)|horse_maneuver(39)|horse_charge(53)|horse_scale(113),imodbits_horse_basic,[],[fac.kingdom_3]],
    ["khergit_horse_royal","Sanjar's Steppe Horse",[("spak_horse_03",0)],itp_type_horse|itp_unique,0,3990,abundance(0)|hit_points(120)|body_armor(42)|difficulty(3)|horse_speed(58)|horse_maneuver(58)|horse_charge(30)|horse_scale(102),imodbits_horse_basic,[],[fac.kingdom_3]],

    # Nord horses
    ["nordic_warhorse_a","Nord Warhorse",[("pellagus_mail_armour_charger1",0)],itp_type_horse|itp_merchandise,0,1700,abundance(50)|hit_points(120)|body_armor(36)|difficulty(3)|horse_speed(38)|horse_maneuver(46)|horse_charge(36)|horse_scale(100),imodbits_horse_basic,[],[fac.kingdom_4]],
    ["nordic_warhorse_b","Nord Noble Warhorse",[("pellagus_mail_armour_charger2",0)],itp_type_horse,0,2700,abundance(20)|hit_points(120)|body_armor(44)|difficulty(4)|horse_speed(38)|horse_maneuver(46)|horse_charge(40)|horse_scale(106),imodbits_horse_basic,[],[fac.kingdom_4]],
    ["nordic_horse_royal","Ragnar's Charger",[("myriliam_WHeavyCharger1",0)],itp_type_horse|itp_unique,0,6270,abundance(0)|hit_points(180)|body_armor(55)|difficulty(4)|horse_speed(44)|horse_maneuver(36)|horse_charge(55)|horse_scale(113),imodbits_horse_basic,[],[fac.kingdom_4]],

    # Rhodok horses
    ["rhodok_warhorse_a","Rhodok Leather Warhorse",[("pellagus_plated_charger1",0)],itp_type_horse|itp_merchandise,0,1480,abundance(60)|hit_points(110)|body_armor(37)|difficulty(3)|horse_speed(40)|horse_maneuver(40)|horse_charge(35)|horse_scale(102),imodbits_horse_basic,[],[fac.kingdom_5]],
    ["rhodok_warhorse_b","Rhodok Noble Warhorse",[("pellagus_plated_charger2",0)],itp_type_horse|itp_merchandise,0,2320,abundance(40)|hit_points(110)|body_armor(45)|difficulty(4)|horse_speed(38)|horse_maneuver(38)|horse_charge(45)|horse_scale(102),imodbits_horse_basic,[],[fac.kingdom_5]],
    ["rhodok_warhorse_c","Rhodok Plated Warhorse",[("pellagus_plated_charger3",0)],itp_type_horse|itp_merchandise,0,4200,abundance(20)|hit_points(120)|body_armor(62)|difficulty(4)|horse_speed(37)|horse_maneuver(36)|horse_charge(52)|horse_scale(105),imodbits_horse_basic,[],[fac.kingdom_5]],
    ["rhodok_horse_royal","Graveth's Warhorse",[("spak_eagle_on_yellow",0)],itp_type_horse|itp_unique,0,6040,abundance(0)|hit_points(140)|body_armor(58)|difficulty(4)|horse_speed(47)|horse_maneuver(50)|horse_charge(48)|horse_scale(105),imodbits_horse_basic,[],[fac.kingdom_5]],

    # Sarranid horses
    ["sarranid_horse_a","Sarranid Horse",[("arabian_horse_a",0)],itp_type_horse|itp_merchandise,0,430,abundance(90)|hit_points(100)|body_armor(12)|difficulty(2)|horse_speed(46)|horse_maneuver(50)|horse_charge(12)|horse_scale(95),imodbits_horse_basic,[],[fac.kingdom_6]],
    ["sarranid_horse_b","Sarranid Horse",[("arabian_horse_b",0)],itp_type_horse|itp_merchandise,0,430,abundance(90)|hit_points(100)|body_armor(12)|difficulty(2)|horse_speed(46)|horse_maneuver(50)|horse_charge(12)|horse_scale(95),imodbits_horse_basic,[],[fac.kingdom_6]],
    ["sarranid_camel_a","Sarranid Riding Camel",[("wanderer_camel",0)],itp_type_horse|itp_merchandise,0,890,abundance(60)|hit_points(120)|body_armor(22)|difficulty(2)|horse_speed(44)|horse_maneuver(40)|horse_charge(22)|horse_scale(106),imodbits_horse_basic,[],[fac.kingdom_6]],
    ["sarranid_camel_b","Sarranid Riding Camel",[("wanderer_camel2",0)],itp_type_horse|itp_merchandise,0,890,abundance(60)|hit_points(120)|body_armor(22)|difficulty(2)|horse_speed(44)|horse_maneuver(40)|horse_charge(22)|horse_scale(106),imodbits_horse_basic,[],[fac.kingdom_6]],
    ["sarranid_warhorse_a","Sarranid Barded Warhorse",[("njunja_sarranid_warhorse1",0)],itp_type_horse|itp_merchandise,0,1520,abundance(60)|hit_points(110)|body_armor(36)|difficulty(3)|horse_speed(42)|horse_maneuver(46)|horse_charge(32)|horse_scale(100),imodbits_horse_basic,[],[fac.kingdom_6]],
    ["sarranid_warhorse_b","Sarranid Mail Warhorse",[("warhorse_chain",0)],itp_type_horse|itp_merchandise,0,2060,abundance(40)|hit_points(110)|body_armor(46)|difficulty(4)|horse_speed(38)|horse_maneuver(45)|horse_charge(34)|horse_scale(103),imodbits_horse_basic,[],[fac.kingdom_6]],
    ["sarranid_warhorse_c","Sarranid Lamellar Warhorse",[("warhorse_sarranid",0)],itp_type_horse|itp_merchandise,0,3630,abundance(20)|hit_points(120)|body_armor(58)|difficulty(5)|horse_speed(40)|horse_maneuver(42)|horse_charge(41)|horse_scale(108),imodbits_horse_basic,[],[fac.kingdom_6]],
    ["sarranid_horse_royal","Hakim's Desert Charger",[("njunja_sarranid_charger_brass",0)],itp_type_horse|itp_unique,0,7530,abundance(0)|hit_points(160)|body_armor(66)|difficulty(5)|horse_speed(44)|horse_maneuver(44)|horse_charge(54)|horse_scale(114),imodbits_horse_basic,[],[fac.kingdom_6]],

    # Dark Knight horses
    ["dk_warhorse","Dark Knight Warhorse",[("pellagus_dk_armour_charger",0)],itp_type_horse,0,3980,abundance(50)|hit_points(160)|body_armor(50)|difficulty(4)|horse_speed(46)|horse_maneuver(45)|horse_charge(48)|horse_scale(108),imodbits_horse_basic,[],[fac.dark_knights]],
    ["dk_charger","Dark Knight Charger",[("myriliam_WHeavyCharger7",0)],itp_type_horse,0,9380,abundance(10)|hit_points(200)|body_armor(70)|difficulty(5)|horse_speed(42)|horse_maneuver(40)|horse_charge(64)|horse_scale(112),imodbits_horse_basic,[],[fac.dark_knights]],
    ["dk_horse_royal","Larktin's Warhorse",[("spak_twilight_horse",0)],itp_type_horse|itp_unique,0,24110,abundance(0)|hit_points(250)|body_armor(90)|difficulty(6)|horse_speed(55)|horse_maneuver(50)|horse_charge(80)|horse_scale(115),imodbits_horse_basic,[],[fac.dark_knights]],

    # Outlaw horses
    ["mountain_horse","Mountain Horse",[("kovas_rus_horse",0)],itp_type_horse,0,680,abundance(80)|hit_points(110)|body_armor(18)|difficulty(1)|horse_speed(42)|horse_maneuver(60)|horse_charge(17)|horse_scale(90),imodbits_horse_basic,[],[fac.outlaws]],
    ["tribal_horse_a","Tribal Horse",[("wanderer_WTribal1",0)],itp_type_horse,0,660,abundance(40)|hit_points(90)|body_armor(11)|difficulty(2)|horse_speed(50)|horse_maneuver(53)|horse_charge(12)|horse_scale(90),imodbits_horse_basic,[],[fac.outlaws]],
    ["tribal_horse_b","Tribal Horse",[("wanderer_WTribal2",0)],itp_type_horse,0,660,abundance(40)|hit_points(90)|body_armor(11)|difficulty(2)|horse_speed(50)|horse_maneuver(53)|horse_charge(12)|horse_scale(90),imodbits_horse_basic,[],[fac.outlaws]],
    ["heavy_camel_a","Thracian Camel",[("xenoargh_camel",0)],itp_type_horse,0,2120,abundance(20)|hit_points(140)|body_armor(28)|difficulty(3)|horse_speed(45)|horse_maneuver(49)|horse_charge(31)|horse_scale(110),imodbits_horse_basic,[],[fac.outlaws]],
    ["heavy_camel_b","Thracian Camel",[("xenoargh_camel2",0)],itp_type_horse,0,2120,abundance(20)|hit_points(140)|body_armor(28)|difficulty(3)|horse_speed(45)|horse_maneuver(49)|horse_charge(31)|horse_scale(110),imodbits_horse_basic,[],[fac.outlaws]],

    ["horses_end", "{!}endmarker", [("invalid_item", 0)], itp_type_goods, 0, 0, weight(1), imodbits_none], 

########################################################################################################################
# SHIELDS
########################################################################################################################

    ["shields_begin", "{!}marker", [("invalid_item", 0)], itp_type_goods, 0, 0, weight(1), imodbits_none], 

    # Common shields
    ["shield_common_round_a", "Leather Round Shield", [("shield_round_d", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 140, abundance(100)|weight(2.50)|difficulty(1)|hit_points(300)|body_armor(6)|spd_rtng(90)|shield_width(35), imodbits_shield, [], []],
    ["shield_common_round_b", "Steel Round Shield", [("shield_round_e", 0)], itp_type_shield|itp_merchandise, itcf_carry_round_shield, 960, abundance(20)|weight(5.00)|difficulty(4)|hit_points(580)|body_armor(16)|spd_rtng(75)|shield_width(30), imodbits_shield, [], []],
    ["shield_common_round_c", "Hide-Bound Round Shield", [("shield_round_f", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 110, abundance(25)|weight(2.50)|difficulty(0)|hit_points(320)|body_armor(4)|spd_rtng(95)|shield_width(33), imodbits_shield, [], []],
    ["shield_common_round_d", "Wooden Round Shield", [("shield_round_g", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 100, abundance(100)|weight(2.00)|difficulty(0)|hit_points(280)|body_armor(5)|spd_rtng(100)|shield_width(35), imodbits_shield, [], []],
    ["shield_common_kite_a", "Dhirim Guard Shield", [("shield_kite_g", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 280, abundance(40)|weight(3.00)|difficulty(1)|hit_points(440)|body_armor(8)|spd_rtng(85)|shield_width(25)|shield_height(85), imodbits_shield, [], []],
    ["shield_common_kite_b", "Khudan Militia Shield", [("shield_kite_h", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 240, abundance(40)|weight(3.00)|difficulty(1)|hit_points(380)|body_armor(10)|spd_rtng(90)|shield_width(25)|shield_height(95), imodbits_shield, [], []],
    ["shield_common_kite_c", "Manhunter Shield", [("shield_kite_i", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 250, abundance(60)|weight(2.50)|difficulty(0)|hit_points(320)|body_armor(8)|spd_rtng(100)|shield_width(25)|shield_height(75), imodbits_shield, [], [fac.manhunters]],
    ["shield_common_kite_d", "Slaver Shield", [("shield_kite_k", 0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 360, abundance(10)|weight(2.50)|difficulty(2)|hit_points(350)|body_armor(12)|spd_rtng(100)|shield_width(25)|shield_height(80), imodbits_shield, [], [fac.outlaws]],
    ["shield_common_kite_e", "Hide-Bound Kite Shield", [("shield_kite_m", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 140, abundance(15)|weight(3.00)|difficulty(1)|hit_points(370)|body_armor(5)|spd_rtng(90)|shield_width(25)|shield_height(90), imodbits_shield, [], []],
    ["shield_common_heater_a", "Mountain Bandit Shield", [("shield_heater_c", 0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 170, abundance(25)|weight(1.50)|difficulty(0)|hit_points(240)|body_armor(7)|spd_rtng(100)|shield_width(25)|shield_height(55), imodbits_shield, [], [fac.outlaws]],
    ["shield_common_heater_b", "Mamluke Training Shield", [("shield_heater_d", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 200, abundance(50)|weight(2.00)|difficulty(0)|hit_points(300)|body_armor(9)|spd_rtng(110)|shield_width(28)|shield_height(52), imodbits_shield, [], []],
    ["norman_shield_2", "Sea Raider Shield", [("norman_shield_2", 0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 250, abundance(100)|weight(3.00)|difficulty(1)|hit_points(340)|body_armor(6)|spd_rtng(80)|shield_width(23)|shield_height(97), imodbits_shield, [], [fac.outlaws]],
    ["norman_shield_4", "Sea Raider Shield", [("norman_shield_4", 0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 250, abundance(100)|weight(3.00)|difficulty(1)|hit_points(340)|body_armor(6)|spd_rtng(80)|shield_width(23)|shield_height(97), imodbits_shield, [], [fac.outlaws]],
    ["norman_shield_8", "Sea Raider Shield", [("norman_shield_8", 0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 250, abundance(100)|weight(3.00)|difficulty(1)|hit_points(340)|body_armor(6)|spd_rtng(80)|shield_width(23)|shield_height(97), imodbits_shield, [], [fac.outlaws]],
    ["norman_shield_1", "Sea Raider War Shield", [("norman_shield_1", 0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 370, abundance(100)|weight(3.50)|difficulty(2)|hit_points(410)|body_armor(10)|spd_rtng(75)|shield_width(23)|shield_height(97), imodbits_shield, [], [fac.outlaws]],
    ["norman_shield_3", "Sea Raider War Shield", [("norman_shield_3", 0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 370, abundance(100)|weight(3.50)|difficulty(2)|hit_points(410)|body_armor(10)|spd_rtng(75)|shield_width(23)|shield_height(97), imodbits_shield, [], [fac.outlaws]],
    ["norman_shield_5", "Sea Raider War Shield", [("norman_shield_5", 0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 370, abundance(100)|weight(3.50)|difficulty(2)|hit_points(410)|body_armor(10)|spd_rtng(75)|shield_width(23)|shield_height(97), imodbits_shield, [], [fac.outlaws]],
    ["norman_shield_6", "Sea Raider War Shield", [("norman_shield_6", 0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 370, abundance(100)|weight(3.50)|difficulty(2)|hit_points(410)|body_armor(10)|spd_rtng(75)|shield_width(23)|shield_height(97), imodbits_shield, [], [fac.outlaws]],
    ["norman_shield_7", "Sea Raider War Shield", [("norman_shield_7", 0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 370, abundance(100)|weight(3.50)|difficulty(2)|hit_points(410)|body_armor(10)|spd_rtng(75)|shield_width(23)|shield_height(97), imodbits_shield, [], [fac.outlaws]],
    ["mercenary_shield_a", "Mercenary Shield", [("spak_shield_wood2", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 210, abundance(80)|weight(3.00)|difficulty(1)|hit_points(380)|body_armor(6)|spd_rtng(100)|shield_width(35), imodbits_shield, [], []],
    ["mercenary_shield_b", "Mercenary Sergeant Shield", [("spak_shield_wood", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 380, abundance(60)|weight(3.00)|difficulty(2)|hit_points(420)|body_armor(10)|spd_rtng(100)|shield_width(35), imodbits_shield, [], []],
    ["mercenary_shield_c", "Mercenary Captain Shield", [("spak_shield_wood3", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 560, abundance(40)|weight(3.25)|difficulty(3)|hit_points(460)|body_armor(14)|spd_rtng(100)|shield_width(35), imodbits_shield, [], []],

    # Swadian shields
    ["hera_swadian_inf_shield_a", "Swadian Recruit Shield", [("tableau_shield_heater_1", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 80, abundance(100)|weight(2.50)|difficulty(0)|hit_points(180)|body_armor(3)|spd_rtng(80)|shield_width(23)|shield_height(92), imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.heater_shield_1, l.agent_id, l.troop_id)])], [fac.kingdom_1]],
    ["hera_swadian_inf_shield_b", "Swadian Regular Shield", [("tableau_shield_heater_1", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 140, abundance(100)|weight(3.00)|difficulty(1)|hit_points(230)|body_armor(6)|spd_rtng(80)|shield_width(23)|shield_height(92), imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.heater_shield_1, l.agent_id, l.troop_id)])], [fac.kingdom_1]],
    ["hera_swadian_inf_shield_c", "Swadian Officer Shield", [("tableau_shield_heater_1", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 210, abundance(80)|weight(3.50)|difficulty(2)|hit_points(280)|body_armor(9)|spd_rtng(80)|shield_width(23)|shield_height(92), imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.heater_shield_1, l.agent_id, l.troop_id)])], [fac.kingdom_1]],
    ["hera_swadian_cav_shield_a", "Swadian Page Shield", [("tableau_shield_heater_2", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 130, abundance(90)|weight(2.00)|difficulty(1)|hit_points(200)|body_armor(5)|spd_rtng(105)|shield_width(25)|shield_height(55), imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.heater_shield_2, l.agent_id, l.troop_id)])], [fac.kingdom_1]],
    ["hera_swadian_cav_shield_b", "Swadian Cavalry Shield", [("tableau_shield_heater_2", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 240, abundance(70)|weight(2.50)|difficulty(2)|hit_points(240)|body_armor(8)|spd_rtng(105)|shield_width(25)|shield_height(55), imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.heater_shield_2, l.agent_id, l.troop_id)])], [fac.kingdom_1]],
    ["hera_swadian_cav_shield_c", "Swadian Knightly Shield", [("tableau_shield_heater_2", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 350, abundance(50)|weight(3.00)|difficulty(3)|hit_points(280)|body_armor(12)|spd_rtng(105)|shield_width(25)|shield_height(55), imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.heater_shield_2, l.agent_id, l.troop_id)])], [fac.kingdom_1]],
    ["swadian_shield_royal", "Katilus' Knightly Shield", [("spak_knightsh", 0)], itp_type_shield|itp_unique, itcf_carry_kite_shield, 1100, abundance(0)|weight(5.00)|difficulty(4)|hit_points(460)|body_armor(15)|spd_rtng(115)|shield_width(25)|shield_height(60), imodbits_none, [], [fac.kingdom_1]],

    # Vaegir shields
    ["hera_vaegir_inf_shield_a", "Vaegir Footman Shield", [("tableau_shield_kite_1", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 100, abundance(100)|weight(3.00)|difficulty(0)|hit_points(200)|body_armor(4)|spd_rtng(85)|shield_width(23)|shield_height(94), imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.kite_shield_1, l.agent_id, l.troop_id)])], [fac.kingdom_2]],
    ["hera_vaegir_inf_shield_b", "Vaegir Infantry Shield", [("tableau_shield_kite_3", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 150, abundance(90)|weight(3.50)|difficulty(1)|hit_points(260)|body_armor(7)|spd_rtng(85)|shield_width(23)|shield_height(94), imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.kite_shield_3, l.agent_id, l.troop_id)])], [fac.kingdom_2]],
    ["hera_vaegir_inf_shield_c", "Vaegir Lineman Shield", [("tableau_shield_kite_2", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 240, abundance(80)|weight(4.00)|difficulty(2)|hit_points(320)|body_armor(10)|spd_rtng(85)|shield_width(23)|shield_height(94), imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.kite_shield_2, l.agent_id, l.troop_id)])], [fac.kingdom_2]],
    ["hera_vaegir_cav_shield_a", "Vaegir Scout Shield", [("tableau_shield_kite_4", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 120, abundance(80)|weight(2.00)|difficulty(0)|hit_points(170)|body_armor(5)|spd_rtng(100)|shield_width(23)|shield_height(67), imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.kite_shield_4, l.agent_id, l.troop_id)])], [fac.kingdom_2]],
    ["hera_vaegir_cav_shield_b", "Vaegir Cavalry Shield", [("tableau_shield_kite_4", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 210, abundance(60)|weight(2.50)|difficulty(1)|hit_points(210)|body_armor(8)|spd_rtng(100)|shield_width(23)|shield_height(67), imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.kite_shield_4, l.agent_id, l.troop_id)])], [fac.kingdom_2]],
    ["hera_vaegir_cav_shield_c", "Vaegir Druzhina Shield", [("tableau_shield_kite_4", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 280, abundance(40)|weight(3.00)|difficulty(2)|hit_points(250)|body_armor(12)|spd_rtng(100)|shield_width(23)|shield_height(67), imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.kite_shield_4, l.agent_id, l.troop_id)])], [fac.kingdom_2]],
    ["vaegir_shield_royal", "Yaroglek's Bear Shield", [("spak_sh_oval", 0)], itp_type_shield|itp_unique, itcf_carry_round_shield, 950, abundance(0)|weight(3.00)|difficulty(3)|hit_points(500)|body_armor(14)|spd_rtng(90)|shield_width(40), imodbits_none, [], [fac.kingdom_2]],

    # Khergit shields
    ["khergit_shield_a1", "Khergit Leather Shield", [("sonyer_saracenshielss", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 140, abundance(60)|weight(2.50)|difficulty(1)|hit_points(220)|body_armor(6)|spd_rtng(110)|shield_width(35), imodbits_shield, [], [fac.kingdom_3]],
    ["khergit_shield_a2", "Khergit Leather Shield", [("sonyer_saracenshs", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 140, abundance(60)|weight(2.50)|difficulty(1)|hit_points(220)|body_armor(6)|spd_rtng(110)|shield_width(35), imodbits_shield, [], [fac.kingdom_3]],
    ["khergit_shield_a3", "Khergit Leather Shield", [("sonyer_saracenshsss", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 140, abundance(60)|weight(2.50)|difficulty(1)|hit_points(220)|body_armor(6)|spd_rtng(110)|shield_width(35), imodbits_shield, [], [fac.kingdom_3]],
    ["khergit_shield_b1", "Khergit Cavalry Shield", [("njunja_brass_shield3", 0)], itp_type_shield|itp_merchandise, itcf_carry_round_shield, 410, abundance(40)|weight(5.50)|difficulty(2)|hit_points(340)|body_armor(15)|spd_rtng(95)|shield_width(35), imodbits_shield, [], [fac.kingdom_3]],
    ["khergit_shield_b2", "Khergit Cavalry Shield", [("njunja_brass_shield7", 0)], itp_type_shield|itp_merchandise, itcf_carry_round_shield, 410, abundance(40)|weight(5.50)|difficulty(2)|hit_points(340)|body_armor(15)|spd_rtng(95)|shield_width(35), imodbits_shield, [], [fac.kingdom_3]],
    ["khergit_shield_c1", "Khergit Ornate Shield", [("njunja_brass_shield", 0)], itp_type_shield|itp_merchandise, itcf_carry_round_shield, 750, abundance(20)|weight(6.00)|difficulty(3)|hit_points(410)|body_armor(18)|spd_rtng(85)|shield_width(35), imodbits_shield, [], [fac.kingdom_3]],
    ["khergit_shield_c2", "Khergit Ornate Shield", [("njunja_brass_shield1", 0)], itp_type_shield|itp_merchandise, itcf_carry_round_shield, 750, abundance(20)|weight(6.00)|difficulty(3)|hit_points(410)|body_armor(18)|spd_rtng(85)|shield_width(35), imodbits_shield, [], [fac.kingdom_3]],
    ["khergit_shield_c3", "Khergit Ornate Shield", [("njunja_brass_shield2", 0)], itp_type_shield|itp_merchandise, itcf_carry_round_shield, 750, abundance(20)|weight(6.00)|difficulty(3)|hit_points(410)|body_armor(18)|spd_rtng(85)|shield_width(35), imodbits_shield, [], [fac.kingdom_3]],
    ["khergit_noble_shield", "Khan Dragon Shield", [("spak_round_dragon_shield2", 0)], itp_type_shield, itcf_carry_round_shield, 900, abundance(5)|weight(5.00)|difficulty(4)|hit_points(520)|body_armor(21)|spd_rtng(90)|shield_width(35), imodbits_shield, [], [fac.kingdom_3]],
    ["khergit_shield_royal", "Sanjar's Dragon Shield", [("spak_round_dragon_shield", 0)], itp_type_shield|itp_unique, itcf_carry_round_shield, 1250, abundance(0)|weight(5.00)|difficulty(5)|hit_points(600)|body_armor(22)|spd_rtng(100)|shield_width(35), imodbits_none, [], [fac.kingdom_3]],

    # Nordic shields
    ["nord_round_shield_a1", "Nord Thrall Shield", [("ad_viking_shield_round_01", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 160, abundance(100)|weight(1.50)|difficulty(1)|hit_points(340)|body_armor(8)|spd_rtng(90)|shield_width(40), imodbits_shield, [], [fac.kingdom_4]],
    ["nord_round_shield_a2", "Nord Thrall Shield", [("ad_viking_shield_round_02", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 160, abundance(100)|weight(1.50)|difficulty(1)|hit_points(340)|body_armor(8)|spd_rtng(90)|shield_width(40), imodbits_shield, [], [fac.kingdom_4]],
    ["nord_round_shield_a3", "Nord Thrall Shield", [("ad_viking_shield_round_03", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 160, abundance(100)|weight(1.50)|difficulty(1)|hit_points(340)|body_armor(8)|spd_rtng(90)|shield_width(40), imodbits_shield, [], [fac.kingdom_4]],
    ["nord_round_shield_b1", "Nord Warrior Shield", [("ad_viking_shield_round_04", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 240, abundance(75)|weight(2.00)|difficulty(2)|hit_points(410)|body_armor(12)|spd_rtng(85)|shield_width(40), imodbits_shield, [], [fac.kingdom_4]],
    ["nord_round_shield_b2", "Nord Warrior Shield", [("ad_viking_shield_round_06", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 240, abundance(75)|weight(2.00)|difficulty(2)|hit_points(410)|body_armor(12)|spd_rtng(85)|shield_width(40), imodbits_shield, [], [fac.kingdom_4]],
    ["nord_round_shield_b3", "Nord Warrior Shield", [("ad_viking_shield_round_10", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 240, abundance(75)|weight(2.00)|difficulty(2)|hit_points(410)|body_armor(12)|spd_rtng(85)|shield_width(40), imodbits_shield, [], [fac.kingdom_4]],
    ["nord_round_shield_c1", "Nord Leader Shield", [("ad_viking_shield_round_13", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 370, abundance(50)|weight(2.25)|difficulty(3)|hit_points(480)|body_armor(16)|spd_rtng(80)|shield_width(40), imodbits_shield, [], [fac.kingdom_4]],
    ["nord_round_shield_c2", "Nord Leader Shield", [("ad_viking_shield_round_14", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 370, abundance(50)|weight(2.25)|difficulty(3)|hit_points(480)|body_armor(16)|spd_rtng(80)|shield_width(40), imodbits_shield, [], [fac.kingdom_4]],
    ["nord_round_shield_c3", "Nord Leader Shield", [("ad_viking_shield_round_15", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 370, abundance(50)|weight(2.25)|difficulty(3)|hit_points(480)|body_armor(16)|spd_rtng(80)|shield_width(40), imodbits_shield, [], [fac.kingdom_4]],
    ["nord_round_shield_d1", "Nord Butsecarl Shield", [("kovas_shield_13", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 250, abundance(60)|weight(2.75)|difficulty(2)|hit_points(350)|body_armor(14)|spd_rtng(95)|shield_width(40), imodbits_shield, [], [fac.kingdom_4]],
    ["nord_round_shield_d2", "Nord Butsecarl Shield", [("kovas_shield_14", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 250, abundance(60)|weight(2.75)|difficulty(2)|hit_points(350)|body_armor(14)|spd_rtng(95)|shield_width(40), imodbits_shield, [], [fac.kingdom_4]],
    ["nord_round_shield_d3", "Nord Butsecarl Shield", [("kovas_shield_15", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 250, abundance(60)|weight(2.75)|difficulty(2)|hit_points(350)|body_armor(14)|spd_rtng(95)|shield_width(40), imodbits_shield, [], [fac.kingdom_4]],
    ["nord_shield_royal", "Ragnar's Moon-Eye Shield", [("talak_jomsviking_shield", 0)], itp_type_shield|itp_unique|itp_wooden_parry, itcf_carry_round_shield, 780, abundance(0)|weight(2.50)|difficulty(2)|hit_points(460)|body_armor(20)|spd_rtng(75)|shield_width(38), imodbits_none, [], [fac.kingdom_4]],

    # Rhodok shields
    ["hera_rhodok_pavise_a", "Rhodok Militia Pavise", [("tableau_shield_pavise_2", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry|itp_cant_use_on_horseback, itcf_carry_board_shield, 280, abundance(100)|weight(9.00)|difficulty(2)|hit_points(520)|body_armor(4)|spd_rtng(70)|shield_width(28)|shield_height(92), imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.pavise_shield_2, l.agent_id, l.troop_id)])], [fac.kingdom_5]],
    ["hera_rhodok_pavise_b", "Rhodok Regular Pavise", [("tableau_shield_pavise_1", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry|itp_cant_use_on_horseback, itcf_carry_board_shield, 430, abundance(80)|weight(10.00)|difficulty(3)|hit_points(600)|body_armor(8)|spd_rtng(65)|shield_width(28)|shield_height(92), imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.pavise_shield_1, l.agent_id, l.troop_id)])], [fac.kingdom_5]],
    ["hera_rhodok_pavise_c", "Rhodok Master Pavise", [("lav_heraldic_shield_pavise_3", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry|itp_cant_use_on_horseback, itcf_carry_board_shield, 660, abundance(50)|weight(12.00)|difficulty(4)|hit_points(740)|body_armor(12)|spd_rtng(60)|shield_width(28)|shield_height(92), imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.pavise_shield_3, l.agent_id, l.troop_id)])], [fac.kingdom_5]],
    ["rhodok_shield_royal", "Graveth's Tower Shield", [("spak_pavise_1", 0)], itp_type_shield|itp_unique, itcf_carry_board_shield, 1650, abundance(0)|weight(15.00)|difficulty(6)|hit_points(1260)|body_armor(24)|spd_rtng(50)|shield_width(28)|shield_height(92), imodbits_none, [], [fac.kingdom_5]],

    # Sarranid shields
    ["hera_sarranid_small_shield_a", "Sarranid Rider Shield", [("tableau_shield_small_round_3", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 60, abundance(80)|weight(1.50)|difficulty(1)|hit_points(150)|body_armor(7)|spd_rtng(120)|shield_width(35), imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.small_round_shield_3, l.agent_id, l.troop_id)])], [fac.kingdom_6]],
    ["hera_sarranid_small_shield_b", "Sarranid Akinci Shield", [("tableau_shield_small_round_1", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 140, abundance(65)|weight(1.75)|difficulty(2)|hit_points(190)|body_armor(10)|spd_rtng(115)|shield_width(35), imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.small_round_shield_1, l.agent_id, l.troop_id)])], [fac.kingdom_6]],
    ["hera_sarranid_small_shield_c", "Sarranid Cavalry Shield", [("tableau_shield_small_round_2", 0)], itp_type_shield|itp_merchandise, itcf_carry_round_shield, 280, abundance(50)|weight(2.00)|difficulty(3)|hit_points(230)|body_armor(13)|spd_rtng(115)|shield_width(35), imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.small_round_shield_2, l.agent_id, l.troop_id)])], [fac.kingdom_6]],
    ["hera_sarranid_large_shield_a", "Sarranid Recruit Shield", [("tableau_shield_round_5", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 40, abundance(100)|weight(2.50)|difficulty(0)|hit_points(190)|body_armor(6)|spd_rtng(100)|shield_width(38), imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.round_shield_5, l.agent_id, l.troop_id)])], [fac.kingdom_6]],
    ["hera_sarranid_large_shield_b", "Sarranid Infantry Shield", [("tableau_shield_round_3", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 75, abundance(90)|weight(2.75)|difficulty(1)|hit_points(220)|body_armor(8)|spd_rtng(105)|shield_width(40), imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.round_shield_3, l.agent_id, l.troop_id)])], [fac.kingdom_6]],
    ["hera_sarranid_large_shield_c", "Sarranid Janissar Shield", [("tableau_shield_round_2", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 140, abundance(80)|weight(3.00)|difficulty(2)|hit_points(260)|body_armor(10)|spd_rtng(105)|shield_width(40), imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.round_shield_2, l.agent_id, l.troop_id)])], [fac.kingdom_6]],
    ["hera_sarranid_large_shield_d", "Sarranid Dervish Shield", [("tableau_shield_round_1", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 270, abundance(70)|weight(3.25)|difficulty(3)|hit_points(300)|body_armor(12)|spd_rtng(100)|shield_width(40), imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.round_shield_1, l.agent_id, l.troop_id)])], [fac.kingdom_6]],
    ["hera_sarranid_large_shield_e", "Sarranid Ghazi Shield", [("tableau_shield_round_4", 0)], itp_type_shield|itp_merchandise, itcf_carry_round_shield, 460, abundance(60)|weight(3.50)|difficulty(4)|hit_points(350)|body_armor(14)|spd_rtng(95)|shield_width(43), imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.round_shield_4, l.agent_id, l.troop_id)])], [fac.kingdom_6]],
    ["sarranid_shield_royal", "Hakim's Golden Shield", [("spak_towershield_steel", 0)], itp_type_shield|itp_unique, itcf_carry_board_shield, 1300, abundance(0)|weight(11.00)|difficulty(5)|hit_points(800)|body_armor(20)|spd_rtng(60)|shield_width(28)|shield_height(87), imodbits_none, [], [fac.kingdom_6]],

    # Dark Knight shields
    ["hera_dk_inf_shield_c", "Dark Infantry Shield", [("tableau_shield_heater_1", 0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 590, abundance(100)|weight(4.00)|difficulty(3)|hit_points(500)|body_armor(12)|spd_rtng(100)|shield_width(25)|shield_height(95), imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.heater_shield_1, l.agent_id, l.troop_id)])], [fac.dark_knights]],
    ["hera_dk_cav_shield_c", "Dark Knight Shield", [("tableau_shield_heater_2", 0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 640, abundance(100)|weight(3.00)|difficulty(4)|hit_points(420)|body_armor(18)|spd_rtng(110)|shield_width(28)|shield_height(57), imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.heater_shield_2, l.agent_id, l.troop_id)])], [fac.dark_knights]],
    ["dk_shield_royal", "Larktin's Phoenix Shield", [("spak_sp_newsh", 0)], itp_type_shield|itp_unique, itcf_carry_kite_shield, 3420, abundance(0)|weight(2.50)|difficulty(6)|hit_points(1000)|body_armor(25)|spd_rtng(105)|shield_width(28)|shield_height(62), imodbits_none, [], [fac.dark_knights]],

    ["shields_end", "{!}endmarker", [("invalid_item", 0)], itp_type_goods, 0, 0, weight(1), imodbits_none], 

########################################################################################################################
# ARMORS
########################################################################################################################

    ["armors_begin", "{!}marker", [("invalid_item", 0)], itp_type_goods, 0, 0, weight(1), imodbits_none], 

    # HEAD ARMORS

    # Special helmets
    ["crown_diadem", "Royal Crown", [("pellagus_crown_non_armour2", 0)], itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair, 0, 2400, abundance(100)|weight(1.50)|difficulty(0)|head_armor(8)|body_armor(0)|leg_armor(0), imodbits_none, [], []],
    ["crown_coif", "Crown Chain Coif", [("njunja_crown_coif", 0)], itp_type_head_armor, 0, 3600, abundance(100)|weight(5.00)|difficulty(10)|head_armor(36)|body_armor(0)|leg_armor(0), imodbits_none, [], []],
    ["crown_helm", "Crown War Helm", [("talak_crown_ornate", 0)], itp_type_head_armor|itp_covers_head, 0, 5200, abundance(100)|weight(8.00)|difficulty(15)|head_armor(52)|body_armor(0)|leg_armor(0), imodbits_none, [], []],
    ["manhunter_helmet", "Manhunter Masked Helm", [("spak_g_helm_spak2", 0)], itp_type_head_armor, 0, 790, abundance(100)|weight(5.00)|difficulty(17)|head_armor(36)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.manhunters]],
    ["assassin_hood", "Assassin Hood", [("cpoint_hood_mask", 0)], itp_type_head_armor|itp_covers_beard, 0, 150, abundance(100)|weight(1.00)|difficulty(0)|head_armor(10)|body_armor(0)|leg_armor(0), imodbits_none, [], [fac.outlaws]],

    # Female civilian headwear
    ["sarranid_head_cloth", "Lady Head Cloth", [("tulbent", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_attach_armature|itp_doesnt_cover_hair|itp_covers_legs, 0, 230, abundance(20)|weight(1.00)|difficulty(0)|head_armor(4)|body_armor(0)|leg_armor(0), imodbits_cloth_high, [], [fac.kingdom_6]],
    ["sarranid_head_cloth_b", "Lady Head Cloth", [("tulbent_b", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_attach_armature|itp_doesnt_cover_hair|itp_covers_legs, 0, 230, abundance(20)|weight(1.00)|difficulty(0)|head_armor(4)|body_armor(0)|leg_armor(0), imodbits_cloth_high, [], [fac.kingdom_6]],
    ["sarranid_felt_head_cloth", "Head Cloth", [("common_tulbent", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_attach_armature, 0, 30, abundance(100)|weight(1.00)|difficulty(0)|head_armor(5)|body_armor(0)|leg_armor(0), imodbits_cloth_med, [], [fac.kingdom_6]],
    ["sarranid_felt_head_cloth_b", "Head Cloth", [("common_tulbent_b", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_attach_armature, 0, 30, abundance(100)|weight(1.00)|difficulty(0)|head_armor(5)|body_armor(0)|leg_armor(0), imodbits_cloth_med, [], [fac.kingdom_6]],
    ["turret_hat_ruby", "Turret Hat", [("turret_hat_r", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_fit_to_head, 0, 340, abundance(20)|weight(1.00)|difficulty(0)|head_armor(6)|body_armor(0)|leg_armor(0), imodbits_cloth_high, [], []],
    ["turret_hat_blue", "Turret Hat", [("turret_hat_b", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_fit_to_head, 0, 340, abundance(20)|weight(1.00)|difficulty(0)|head_armor(6)|body_armor(0)|leg_armor(0), imodbits_cloth_high, [], []],
    ["turret_hat_green", "Barbette", [("barbette_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_fit_to_head, 0, 280, abundance(20)|weight(1.00)|difficulty(0)|head_armor(6)|body_armor(0)|leg_armor(0), imodbits_cloth_high, [], []],
    ["court_hat", "Turret Hat", [("court_hat", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_fit_to_head, 0, 160, abundance(20)|weight(1.00)|difficulty(0)|head_armor(6)|body_armor(0)|leg_armor(0), imodbits_cloth_high, [], []],
    ["wimple_a", "Wimple", [("wimple_a_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_fit_to_head, 0, 20, abundance(70)|weight(1.00)|difficulty(0)|head_armor(3)|body_armor(0)|leg_armor(0), imodbits_cloth_med, [], []],
    ["wimple_with_veil", "Wimple with Veil", [("wimple_b_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_fit_to_head, 0, 30, abundance(70)|weight(1.00)|difficulty(0)|head_armor(3)|body_armor(0)|leg_armor(0), imodbits_cloth_med, [], []],
    ["khergit_lady_hat", "Khergit Lady Hat", [("khergit_lady_hat", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_fit_to_head|itp_doesnt_cover_hair|itp_covers_legs, 0, 300, abundance(20)|weight(1.00)|difficulty(0)|head_armor(2)|body_armor(0)|leg_armor(0), imodbits_cloth_high, [], [fac.kingdom_3]],
    ["khergit_lady_hat_b", "Khergit Lady Leather Hat", [("khergit_lady_hat_b", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_fit_to_head|itp_doesnt_cover_hair|itp_covers_legs, 0, 260, abundance(20)|weight(1.00)|difficulty(0)|head_armor(4)|body_armor(0)|leg_armor(0), imodbits_cloth_high, [], [fac.kingdom_3]],
    ["female_hood", "Lady's Hood", [("ladys_hood_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 50, abundance(40)|weight(1.00)|difficulty(0)|head_armor(5)|body_armor(0)|leg_armor(0), imodbits_cloth_med, [], []],
    #court_hat_b

    # Unisex and male civilian headwear
    ["pilgrim_hood", "Grey Hood", [("lav_ladys_hood_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 20, abundance(50)|weight(1.00)|difficulty(0)|head_armor(5)|body_armor(0)|leg_armor(0), imodbits_cloth_low, [], []],
    ["common_hood", "Hood", [("hood_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 25, abundance(100)|weight(1.00)|difficulty(0)|head_armor(4)|body_armor(0)|leg_armor(0), imodbits_cloth_low, [], []],
    ["common_hood_b", "Hood", [("lav_hood_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 25, abundance(100)|weight(1.00)|difficulty(0)|head_armor(4)|body_armor(0)|leg_armor(0), imodbits_cloth_low, [], []],
    ["black_hood", "Black Hood", [("hood_black", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 20, abundance(100)|weight(1.00)|difficulty(0)|head_armor(4)|body_armor(0)|leg_armor(0), imodbits_cloth_low, [], []],
    ["head_wrappings", "Head Wrapping", [("head_wrapping", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_fit_to_head, 0, 5, abundance(100)|weight(1.00)|difficulty(0)|head_armor(3)|body_armor(0)|leg_armor(0), imodbits_cloth_low, [], []],
    ["headcloth", "Headcloth", [("headcloth_a_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 10, abundance(100)|weight(1.00)|difficulty(0)|head_armor(2)|body_armor(0)|leg_armor(0), imodbits_cloth_low, [], []],
    ["straw_hat", "Straw Hat", [("straw_hat_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 10, abundance(100)|weight(1.00)|difficulty(0)|head_armor(4)|body_armor(0)|leg_armor(0), imodbits_cloth_med, [], []],
    ["arming_cap", "Arming Cap", [("arming_cap_a_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 20, abundance(100)|weight(1.00)|difficulty(0)|head_armor(3)|body_armor(0)|leg_armor(0), imodbits_cloth_med, [], []],
    ["woolen_cap", "Woolen Cap", [("woolen_cap_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 20, abundance(100)|weight(1.00)|difficulty(0)|head_armor(4)|body_armor(0)|leg_armor(0), imodbits_cloth_med, [], []],
    ["woolen_cap_b", "Woolen Cap", [("lav_woolen_cap_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 20, abundance(100)|weight(1.00)|difficulty(0)|head_armor(4)|body_armor(0)|leg_armor(0), imodbits_cloth_med, [], []],
    ["felt_hat", "Felt Hat", [("felt_hat_a_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 20, abundance(100)|weight(1.00)|difficulty(0)|head_armor(6)|body_armor(0)|leg_armor(0), imodbits_cloth_med, [], []],
    ["felt_hat_b", "Felt Beret", [("felt_hat_b_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 20, abundance(100)|weight(1.00)|difficulty(0)|head_armor(4)|body_armor(0)|leg_armor(0), imodbits_cloth_med, [], []],
    ["turban", "Turban", [("tuareg_open", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 20, abundance(100)|weight(2.00)|difficulty(0)|head_armor(6)|body_armor(0)|leg_armor(0), imodbits_cloth_med, [], [fac.kingdom_6]],
    ["desert_turban", "Desert Turban", [("tuareg", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_covers_beard, 0, 20, abundance(100)|weight(2.00)|difficulty(0)|head_armor(7)|body_armor(0)|leg_armor(0), imodbits_cloth_med, [], [fac.kingdom_6]],

    # Demi-military headwear
    ["padded_coif", "Padded Coif", [("padded_coif_a_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 60, abundance(100)|weight(2.00)|difficulty(0)|head_armor(10)|body_armor(0)|leg_armor(0), imodbits_cloth_med, [], []],
    ["fur_hat", "Fur Hat", [("fur_hat_a_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 110, abundance(100)|weight(2.00)|difficulty(0)|head_armor(12)|body_armor(0)|leg_armor(0), imodbits_armor, [], []],
    ["nomad_cap_b", "Nomad Leather Cap", [("nomad_cap_b_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 150, abundance(100)|weight(2.00)|difficulty(0)|head_armor(14)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_3]],
    ["leather_steppe_cap_a", "Steppe Fur Cap", [("leather_steppe_cap_a_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 80, abundance(100)|weight(2.00)|difficulty(0)|head_armor(10)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_3]],
    ["leather_cap", "Leather Cap", [("leather_cap_a_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 110, abundance(100)|weight(2.00)|difficulty(0)|head_armor(12)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_1, fac.kingdom_5]],

    # Swadian helms
    ["skullcap", "Skullcap", [("skull_cap_new_a", 0)], itp_type_head_armor|itp_merchandise, 0, 260, abundance(120)|weight(3.00)|difficulty(0)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_armor, [], []],
    ["footman_helmet", "Footman's Helmet", [("skull_cap_new", 0)], itp_type_head_armor|itp_merchandise, 0, 390, abundance(100)|weight(4.00)|difficulty(0)|head_armor(24)|body_armor(0)|leg_armor(0), imodbits_armor, [], []],
    ["segmented_helmet", "Segmented Helmet", [("segmented_helm_new", 0)], itp_type_head_armor|itp_merchandise, 0, 510, abundance(80)|weight(4.00)|difficulty(8)|head_armor(27)|body_armor(0)|leg_armor(0), imodbits_armor, [], []],
    ["mail_coif", "Mail Coif", [("mail_coif_new", 0)], itp_type_head_armor|itp_merchandise, 0, 540, abundance(80)|weight(4.00)|difficulty(9)|head_armor(28)|body_armor(0)|leg_armor(0), imodbits_armor, [], []],
    ["helmet_with_neckguard", "Helmet with Neckguard", [("neckguard_helm_new", 0)], itp_type_head_armor|itp_merchandise, 0, 610, abundance(80)|weight(4.00)|difficulty(10)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_armor, [], []],
    ["guard_helmet", "Guard Helmet", [("reinf_helmet_new", 0)], itp_type_head_armor|itp_merchandise, 0, 730, abundance(60)|weight(5.00)|difficulty(11)|head_armor(32)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_1]],
    ["bascinet", "Bascinet", [("bascinet_avt_new", 0)], itp_type_head_armor|itp_merchandise, 0, 890, abundance(60)|weight(5.00)|difficulty(12)|head_armor(36)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_1]],
    ["bascinet_2", "Bascinet with Aventail", [("bascinet_new_a", 0)], itp_type_head_armor|itp_merchandise, 0, 980, abundance(60)|weight(5.00)|difficulty(12)|head_armor(38)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_1]],
    ["bascinet_3", "Bascinet with Nose Guard", [("bascinet_new_b", 0)], itp_type_head_armor|itp_merchandise, 0, 1080, abundance(60)|weight(5.00)|difficulty(12)|head_armor(40)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_1]],
    ["great_helmet", "Great Helmet", [("great_helmet_new", 0)], itp_type_head_armor|itp_merchandise|itp_covers_head, 0, 1420, abundance(20)|weight(6.50)|difficulty(13)|head_armor(44)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_1]],
    ["winged_great_helmet", "Winged Great Helmet", [("maciejowski_helmet_new", 0)], itp_type_head_armor|itp_covers_head, 0, 1540, abundance(20)|weight(6.50)|difficulty(14)|head_armor(46)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_1]],
    ["knight_helm", "Knight Full Helm", [("zottlm_hounskull_plain", 0)], itp_type_head_armor|itp_covers_head, 0, 1720, abundance(5)|weight(7.00)|difficulty(15)|head_armor(48)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_1]],
    ["swadian_helm_royal", "Katilus' Royal Helm", [("narf_hounskull", 0)], itp_type_head_armor|itp_unique|itp_covers_head, 0, 2150, abundance(0)|weight(7.00)|difficulty(17)|head_armor(54)|body_armor(0)|leg_armor(0), imodbits_none, [], [fac.kingdom_1]],

    # Vaegir helms
    ["leather_warrior_cap", "Leather Warrior Cap", [("skull_cap_new_b", 0)], itp_type_head_armor|itp_merchandise, 0, 170, abundance(100)|weight(2.50)|difficulty(0)|head_armor(15)|body_armor(0)|leg_armor(0), imodbits_armor, [], []],
    ["vaegir_fur_cap", "Vaegir Leather Helmet", [("vaeg_helmet3", 0)], itp_type_head_armor|itp_merchandise, 0, 410, abundance(100)|weight(3.00)|difficulty(0)|head_armor(25)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_2]],
    ["vaegir_fur_helmet", "Vaegir Chain Helmet", [("vaeg_helmet2", 0)], itp_type_head_armor|itp_merchandise, 0, 560, abundance(90)|weight(3.50)|difficulty(0)|head_armor(29)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_2]],
    ["vaegir_lamellar_helmet", "Vaegir Lamellar Helmet", [("vaeg_helmet4", 0)], itp_type_head_armor|itp_merchandise, 0, 660, abundance(75)|weight(4.00)|difficulty(8)|head_armor(31)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_2]],
    ["vaegir_spiked_helmet", "Vaegir Spiked Cap", [("vaeg_helmet1", 0)], itp_type_head_armor|itp_merchandise, 0, 680, abundance(80)|weight(3.50)|difficulty(9)|head_armor(32)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_2]],
    ["vaegir_army_helm", "Vaegir Army Helm", [("vaeg_helmet5", 0)], itp_type_head_armor|itp_merchandise, 0, 710, abundance(70)|weight(3.50)|difficulty(9)|head_armor(32)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_2]],
    ["vaegir_noble_helmet", "Vaegir Guard Helm", [("vaeg_helmet7", 0)], itp_type_head_armor|itp_merchandise, 0, 920, abundance(50)|weight(4.00)|difficulty(10)|head_armor(36)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_2]],
    ["vaegir_war_mask", "Vaegir War Mask", [("vaeg_helmet8", 0)], itp_type_head_armor|itp_merchandise, 0, 1090, abundance(25)|weight(4.50)|difficulty(11)|head_armor(38)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_2]],
    ["vaegir_war_helmet", "Vaegir War Helm", [("vaeg_helmet6", 0)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 1090, abundance(40)|weight(4.50)|difficulty(11)|head_armor(39)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_2]],
    ["vaegir_noble_helm", "Vaegir Noble Helm", [("narf_tagancha_helm_a", 0), ("narf_tagancha_helm_a_inv", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature, 0, 1240, abundance(10)|weight(4.00)|difficulty(12)|head_armor(40)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_2]],
    ["vaegir_mask", "Vaegir Masked Helm", [("vaeg_helmet9", 0)], itp_type_head_armor|itp_covers_beard, 0, 1330, abundance(15)|weight(5.50)|difficulty(12)|head_armor(42)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_2]],
    ["vaegir_leader_helm", "Vaegir Leader Helm", [("narf_novgorod_helm", 0), ("narf_novgorod_helm_inv", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_covers_beard, 0, 1420, abundance(20)|weight(5.00)|difficulty(13)|head_armor(44)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_2]],
    ["vaegir_noble_fullhelm", "Vaegir Noble Full Helm", [("narf_tagancha_helm_b", 0), ("narf_tagancha_helm_b_inv", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_covers_beard, 0, 1540, abundance(5)|weight(5.00)|difficulty(13)|head_armor(45)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_2]],
    ["vaegir_lichina_helm", "Vaegir Litchina Helm", [("narf_litchina_helm", 0), ("narf_litchina_helm_inv", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_covers_beard, 0, 1640, abundance(10)|weight(6.00)|difficulty(15)|head_armor(47)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_2]],

    # Khergit helms
    ["steppe_cap", "Steppe Cap", [("steppe_cap_a_new", 0)], itp_type_head_armor|itp_merchandise, 0, 150, abundance(100)|weight(2.00)|difficulty(0)|head_armor(14)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_3]],
    ["khergit_leather_helmet", "Khergit Leather Helmet", [("sms_skin_helmet", 0)], itp_type_head_armor|itp_merchandise, 0, 190, abundance(100)|weight(2.50)|difficulty(0)|head_armor(16)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_3]],
    ["leather_steppe_cap_b", "Steppe Helmet", [("tattered_steppe_cap_b_new", 0)], itp_type_head_armor|itp_merchandise, 0, 230, abundance(100)|weight(2.00)|difficulty(0)|head_armor(18)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_3]],
    ["nomad_cap", "Nomad Fur Cap", [("nomad_cap_a_new", 0)], itp_type_head_armor|itp_merchandise, 0, 330, abundance(100)|weight(2.00)|difficulty(0)|head_armor(22)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_3]],
    ["khergit_cavalry_helmet", "Khergit Rider Helmet", [("lamellar_helmet_b", 0)], itp_type_head_armor|itp_merchandise, 0, 460, abundance(90)|weight(3.50)|difficulty(0)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_3]],
    ["khergit_war_helmet", "Khergit Cavalry Helmet", [("tattered_steppe_cap_a_new", 0)], itp_type_head_armor|itp_merchandise, 0, 610, abundance(80)|weight(4.50)|difficulty(9)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_3]],
    ["khergit_covered_helm", "Khergit War Helmet", [("dia151_arhelm_norig", 0)], itp_type_head_armor|itp_merchandise, 0, 850, abundance(60)|weight(5.00)|difficulty(10)|head_armor(35)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_3]],
    ["tarkhan_helm", "Tarkhan Helmet", [("lamellar_helmet_a", 0)], itp_type_head_armor, 0, 1040, abundance(40)|weight(4.50)|difficulty(11)|head_armor(38)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_3]],
    ["khergit_noble_helm", "Khergit Noble Helm", [("sonyer_ghulssss", 0)], itp_type_head_armor|itp_covers_beard, 0, 1350, abundance(10)|weight(6.00)|difficulty(12)|head_armor(42)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_3]],

    # Nordic helms
    ["nordic_archer_helmet", "Nordic Archer Helmet", [("Helmet_A_vs2", 0)], itp_type_head_armor|itp_merchandise, 0, 280, abundance(100)|weight(2.50)|difficulty(0)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_4]],
    ["nordic_veteran_archer_helmet", "Nordic Leather Helmet", [("Helmet_A", 0)], itp_type_head_armor|itp_merchandise, 0, 330, abundance(100)|weight(3.00)|difficulty(0)|head_armor(22)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_4]],
    ["nordic_skullcap", "Nordic Skullcap", [("ad_viking_helmet_03", 0)], itp_type_head_armor|itp_merchandise, 0, 330, abundance(100)|weight(2.00)|difficulty(0)|head_armor(22)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_4]],
    ["norman_helmet", "Helmet with Cap", [("norman_helmet_a", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0, 440, abundance(100)|weight(3.50)|difficulty(0)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_4]],
    ["nasal_helmet", "Nasal Helmet", [("nasal_helmet_b", 0)], itp_type_head_armor|itp_merchandise, 0, 510, abundance(100)|weight(3.00)|difficulty(0)|head_armor(28)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_4]],
    ["spiked_helmet", "Spiked Helmet", [("spiked_helmet_new", 0)], itp_type_head_armor|itp_merchandise, 0, 570, abundance(100)|weight(4.00)|difficulty(0)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_4]],
    ["nordic_raider_Helmet", "Nordic Raider Helmet", [("ad_viking_helmet_01", 0)], itp_type_head_armor|itp_merchandise, 0, 680, abundance(80)|weight(3.00)|difficulty(8)|head_armor(32)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_4]],
    ["nordic_footman_helmet", "Nordic Footman Helmet", [("Helmet_B_vs2", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0, 710, abundance(85)|weight(3.50)|difficulty(9)|head_armor(33)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_4]],
    ["nordic_fighter_helmet", "Nordic Fighter Helmet", [("Helmet_B", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0, 870, abundance(70)|weight(4.00)|difficulty(10)|head_armor(36)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_4]],
    ["nordic_helmet", "Nordic Helmet", [("helmet_w_eyeguard_new", 0)], itp_type_head_armor|itp_merchandise, 0, 970, abundance(65)|weight(4.50)|difficulty(11)|head_armor(38)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_4]],
    ["nordic_helmet_b", "Nordic Helmet", [("helmet_w_eyeguard_new", 0)], itp_type_head_armor|itp_merchandise, 0, 1040, abundance(55)|weight(4.50)|difficulty(11)|head_armor(39)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_4]],
    ["nordic_huscarl_helmet", "Nordic Battle Helmet", [("Helmet_C_vs2", 0)], itp_type_head_armor|itp_merchandise, 0, 1210, abundance(50)|weight(4.50)|difficulty(12)|head_armor(42)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_4]],
    ["nordic_warlord_helmet", "Nordic War Helmet", [("Helmet_C", 0)], itp_type_head_armor, 0, 1280, abundance(30)|weight(5.00)|difficulty(13)|head_armor(42)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_4]],
    ["nordic_noble_helm", "Housecarl Helm", [("barf_helm", 0)], itp_type_head_armor, 0, 1460, abundance(10)|weight(5.00)|difficulty(13)|head_armor(44)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_4]],
    ["nordic_helm_royal", "Ragnar's Royal Helm", [("ssh_nord_ornate_visored_helmet", 0), ("ssh_nord_ornate_visored_helmet_inv", ixmesh_inventory)], itp_type_head_armor|itp_unique|itp_attach_armature, 0, 2290, abundance(0)|weight(5.50)|difficulty(17)|head_armor(52)|body_armor(4)|leg_armor(0), imodbits_none, [], [fac.kingdom_4]],

    # Rhodok helms
    ["rhodok_infantry_cap", "Rhodok Infantry Cap", [("alman_simple_iberian_helmet", 0)], itp_type_head_armor|itp_merchandise, 0, 330, abundance(100)|weight(2.00)|difficulty(0)|head_armor(22)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_5]],
    ["rhodok_kettle_hat", "Kettle Hat", [("baraban_kettle_helm_01", 0)], itp_type_head_armor|itp_merchandise, 0, 440, abundance(100)|weight(3.00)|difficulty(0)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_5]],
    ["rhodok_army_cap", "Rhodok Army Cap", [("alman_iberian_helmet", 0)], itp_type_head_armor|itp_merchandise, 0, 510, abundance(100)|weight(3.50)|difficulty(8)|head_armor(28)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_5]],
    ["kettle_hat", "Kettle Hat with Coif", [("kettle_hat_new", 0)], itp_type_head_armor|itp_merchandise, 0, 660, abundance(90)|weight(4.50)|difficulty(10)|head_armor(32)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_5]],
    ["rhodok_flattop", "Flat Topped Helm", [("alman_flat_helmet", 0)], itp_type_head_armor|itp_merchandise, 0, 720, abundance(80)|weight(4.00)|difficulty(11)|head_armor(33)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_5]],
    ["flat_topped_helmet", "Rhodok Cavalry Helm", [("flattop_helmet_new", 0)], itp_type_head_armor|itp_merchandise, 0, 910, abundance(70)|weight(4.25)|difficulty(12)|head_armor(37)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_5]],
    ["rhodok_open_sallet", "Open Sallet", [("narf_open_salet_coif", 0)], itp_type_head_armor|itp_merchandise, 0, 1260, abundance(50)|weight(5.00)|difficulty(15)|head_armor(43)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_5]],
    ["full_helm", "Full Helm", [("great_helmet_new_b", 0)], itp_type_head_armor|itp_covers_head|itp_covers_beard, 0, 1440, abundance(30)|weight(5.50)|difficulty(15)|head_armor(45)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_5]],
    ["rhodok_visored_sallet", "Visored Sallet", [("narf_visored_salet_coif", 0)], itp_type_head_armor, 0, 1700, abundance(10)|weight(6.00)|difficulty(16)|head_armor(48)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_5]],

    # Sarranid helms
    ["sarranid_felt_hat", "Sarranid Felt Hat", [("sar_helmet3", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 210, abundance(100)|weight(2.00)|difficulty(0)|head_armor(17)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_6]],
    ["sarranid_helmet1", "Sarranid Keffiyeh Helmet", [("sar_helmet1", 0)], itp_type_head_armor|itp_merchandise, 0, 330, abundance(100)|weight(3.00)|difficulty(0)|head_armor(22)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_6]],
    ["sarranid_spiked_helmet", "Sarranid Spiked Helmet", [("alman_saracen_helmet_a", 0)], itp_type_head_armor|itp_merchandise, 0, 400, abundance(90)|weight(2.50)|difficulty(0)|head_armor(24)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_6]],
    ["sarranid_warrior_cap", "Sarranid Warrior Cap", [("tuareg_helmet", 0)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 470, abundance(80)|weight(3.00)|difficulty(0)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_6]],
    ["sarranid_mail_helmet", "Sarranid Turban Mail", [("alman_turban_mail_a", 0)], itp_type_head_armor|itp_merchandise, 0, 590, abundance(70)|weight(3.00)|difficulty(8)|head_armor(29)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_6]],
    ["sarranid_horseman_helmet", "Sarranid Horseman Helmet", [("sar_helmet2", 0)], itp_type_head_armor|itp_merchandise, 0, 740, abundance(55)|weight(4.00)|difficulty(9)|head_armor(32)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_6]],
    ["sarranid_warrior_helm", "Sarranid Warrior Helm", [("lucas_facecovermail_turban_1_red", 0)], itp_type_head_armor|itp_merchandise, 0, 870, abundance(35)|weight(4.50)|difficulty(9)|head_armor(34)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_6]],
    ["sarranid_mail_coif", "Sarranid Helm with Coif", [("tuareg_helmet2", 0)], itp_type_head_armor|itp_merchandise, 0, 950, abundance(40)|weight(4.50)|difficulty(10)|head_armor(36)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_6]],
    ["sarranid_full_keffiyeh", "Sarranid Full Keffiyeh Helm", [("lucas_facecovermail_turban_black", 0)], itp_type_head_armor|itp_merchandise, 0, 1170, abundance(15)|weight(5.00)|difficulty(11)|head_armor(39)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_6]],
    ["sarranid_veiled_helmet", "Sarranid Veiled Helmet", [("sar_helmet4", 0)], itp_type_head_armor|itp_covers_beard, 0, 1420, abundance(5)|weight(5.50)|difficulty(12)|head_armor(43)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.kingdom_6]],
    ["sarranid_helm_royal", "Hakim's Royal Helmet", [("njunja_brass_veil_helm", 0)], itp_type_head_armor|itp_unique|itp_covers_beard, 0, 1880, abundance(0)|weight(6.00)|difficulty(14)|head_armor(48)|body_armor(2)|leg_armor(0), imodbits_none, [], [fac.kingdom_6]],

    # Dark Knight helms
    ["dk_helm_a", "Black Iron Helm", [("pellagus_dk_helm", 0)], itp_type_head_armor, 0, 1110, abundance(50)|weight(4.00)|difficulty(12)|head_armor(40)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.dark_knights]],
    ["dk_helm_b", "Black Full Helm", [("pellagus_dk_black_helm", 0)], itp_type_head_armor, 0, 1500, abundance(30)|weight(4.00)|difficulty(14)|head_armor(46)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.dark_knights]],
    ["dk_helm_c", "Black Horned Helm", [("pellagus_dk_helm_horned03", 0)], itp_type_head_armor, 0, 1660, abundance(20)|weight(4.00)|difficulty(15)|head_armor(48)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.dark_knights]],
    ["dk_helm_d", "Black Horned Helm", [("pellagus_dk_helm_horned01", 0)], itp_type_head_armor, 0, 1830, abundance(10)|weight(4.50)|difficulty(15)|head_armor(50)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.dark_knights]],
    ["dk_helm_lord_a", "Dark Brother Open Helm", [("tumajan_sturmhaube_6b", 0)], itp_type_head_armor, 0, 2120, abundance(5)|weight(5.00)|difficulty(17)|head_armor(54)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.dark_knights]],
    ["dk_helm_lord_b", "Dark Brother Noseguard Helm", [("tumajan_sturmhaube_7b", 0)], itp_type_head_armor, 0, 2260, abundance(5)|weight(5.25)|difficulty(17)|head_armor(56)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac.dark_knights]],
    ["dk_helm_royal", "Lady Larktin's Helm", [("spak_twilighthelm", 0)], itp_type_head_armor|itp_unique, 0, 2580, abundance(0)|weight(6.00)|difficulty(18)|head_armor(60)|body_armor(0)|leg_armor(0), imodbits_none, [], [fac.dark_knights]],

    # BOOTS

    # Special boots
    ["assassin_boots", "Assassin Boots", [("lav_assassin_boots", 0)], itp_type_foot_armor|itp_civilian|itp_attach_armature, 0, 120, abundance(100)|weight(2.00)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(6), imodbits_none, [], [fac.outlaws]],

    # Regular boots
    ["wrapping_boots", "Wrapping Boots", [("wrapping_boots_a", 0)], itp_type_foot_armor|itp_merchandise|itp_civilian|itp_attach_armature, 0, 40, abundance(100)|weight(2.00)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(4), imodbits_cloth_med, [], []],
    ["woolen_hose", "Woolen Hose", [("woolen_hose_a", 0)], itp_type_foot_armor|itp_merchandise|itp_civilian|itp_attach_armature, 0, 20, abundance(100)|weight(2.00)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(4), imodbits_cloth_med, [], []],
    ["blue_hose", "Blue Hose", [("blue_hose_a", 0)], itp_type_foot_armor|itp_merchandise|itp_civilian|itp_attach_armature, 0, 20, abundance(100)|weight(2.00)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(4), imodbits_cloth_med, [], []],
    ["ankle_boots", "Ankle Boots", [("ankle_boots_a_new", 0)], itp_type_foot_armor|itp_merchandise|itp_civilian|itp_attach_armature, 0, 40, abundance(100)|weight(2.00)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(4), imodbits_cloth_med, [], []],
    ["sarranid_boots_a", "Sarranid Shoes", [("sarranid_shoes", 0)], itp_type_foot_armor|itp_merchandise|itp_civilian|itp_attach_armature, 0, 20, abundance(100)|weight(2.00)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(4), imodbits_cloth_med, [], [fac.kingdom_6]],
    ["nomad_boots", "Nomad Boots", [("nomad_boots_a", 0)], itp_type_foot_armor|itp_merchandise|itp_civilian|itp_attach_armature, 0, 60, abundance(100)|weight(2.00)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(6), imodbits_cloth_med, [], []],
    ["hunter_boots", "Hunter Boots", [("hunter_boots_a", 0)], itp_type_foot_armor|itp_merchandise|itp_civilian|itp_attach_armature, 0, 140, abundance(100)|weight(3.00)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(8), imodbits_armor, [], []],
    ["hide_boots", "Hide Boots", [("hide_boots_a", 0)], itp_type_foot_armor|itp_merchandise|itp_civilian|itp_attach_armature, 0, 210, abundance(100)|weight(3.00)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(10), imodbits_armor, [], []],
    ["light_leather_boots", "Studded Greaves", [("light_leather_boots", 0)], itp_type_foot_armor|itp_merchandise|itp_attach_armature, 0, 290, abundance(100)|weight(3.50)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(12), imodbits_armor, [], []],
    ["leather_boots", "Leather Boots", [("leather_boots_a", 0)], itp_type_foot_armor|itp_merchandise|itp_civilian|itp_attach_armature, 0, 370, abundance(100)|weight(4.00)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(14), imodbits_armor, [], []],
    ["khergit_leather_boots", "Khergit Leather Boots", [("khergit_leather_boots", 0)], itp_type_foot_armor|itp_merchandise|itp_civilian|itp_attach_armature, 0, 400, abundance(80)|weight(4.00)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(14), imodbits_armor, [], [fac.kingdom_3]],
    ["sarranid_boots_b", "Sarranid Leather Boots", [("sarranid_boots", 0)], itp_type_foot_armor|itp_merchandise|itp_civilian|itp_attach_armature, 0, 510, abundance(80)|weight(4.00)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(16), imodbits_armor, [], [fac.kingdom_6]],
    ["splinted_greaves", "Splinted Greaves", [("splinted_greaves_a", 0)], itp_type_foot_armor|itp_merchandise|itp_attach_armature, 0, 520, abundance(70)|weight(6.00)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(16), imodbits_armor, [], []],
    ["sarranid_boots_d", "Sarranid Mail Boots", [("sarranid_mail_chausses", 0)], itp_type_foot_armor|itp_merchandise|itp_attach_armature, 0, 660, abundance(60)|weight(5.50)|difficulty(8)|head_armor(0)|body_armor(0)|leg_armor(18), imodbits_armor, [], [fac.kingdom_6]],
    ["mail_chausses", "Mail Chausses", [("mail_chausses_a", 0)], itp_type_foot_armor|itp_merchandise|itp_attach_armature, 0, 800, abundance(60)|weight(6.00)|difficulty(9)|head_armor(0)|body_armor(0)|leg_armor(20), imodbits_armor, [], []],
    ["mail_boots", "Mail Boots", [("mail_boots_a", 0)], itp_type_foot_armor|itp_merchandise|itp_attach_armature, 0, 1100, abundance(60)|weight(6.50)|difficulty(11)|head_armor(0)|body_armor(0)|leg_armor(24), imodbits_armor, [], []],
    ["sarranid_boots_c", "Sarranid Splinted Greaves", [("sarranid_camel_boots", 0)], itp_type_foot_armor|itp_merchandise|itp_attach_armature, 0, 1130, abundance(50)|weight(5.50)|difficulty(12)|head_armor(0)|body_armor(0)|leg_armor(24), imodbits_armor, [], [fac.kingdom_6]],
    ["splinted_leather_greaves", "Splinted Leather Greaves", [("leather_greaves_a", 0)], itp_type_foot_armor|itp_merchandise|itp_attach_armature, 0, 1360, abundance(35)|weight(7.00)|difficulty(12)|head_armor(0)|body_armor(0)|leg_armor(26), imodbits_armor, [], []],
    ["iron_greaves", "Iron Greaves", [("iron_greaves_a", 0)], itp_type_foot_armor|itp_merchandise|itp_attach_armature, 0, 1610, abundance(20)|weight(8.00)|difficulty(13)|head_armor(0)|body_armor(0)|leg_armor(28), imodbits_armor, [], []],
    ["tarkhan_boots", "Tarkhan Boots", [("lamellar_boots_a", 0)], itp_type_foot_armor|itp_attach_armature, 0, 1890, abundance(5)|weight(6.50)|difficulty(13)|head_armor(0)|body_armor(0)|leg_armor(30), imodbits_armor, [], [fac.kingdom_3]],
    ["plate_boots", "Plate Boots", [("plate_boots", 0)], itp_type_foot_armor|itp_attach_armature, 0, 2090, abundance(10)|weight(8.00)|difficulty(15)|head_armor(0)|body_armor(0)|leg_armor(32), imodbits_armor, [], []],
    ["elite_plate_boots", "Elite Plate Boots", [("narf_steel_greaves", 0)], itp_type_foot_armor|itp_attach_armature, 0, 3000, abundance(5)|weight(9.00)|difficulty(18)|head_armor(0)|body_armor(0)|leg_armor(39), imodbits_armor, [], [fac.kingdom_5]],
    ["steel_shynbaulds", "Steel Shynbaulds", [("narf_shynbaulds", 0)], itp_type_foot_armor|itp_attach_armature, 0, 2480, abundance(5)|weight(8.50)|difficulty(17)|head_armor(0)|body_armor(0)|leg_armor(35), imodbits_armor, [], [fac.kingdom_1]],
    ["vaegir_boots_royal", "Yaroglek's Bear Boots", [("spak_bear_boots", 0)], itp_type_foot_armor|itp_unique|itp_attach_armature, 0, 2150, abundance(0)|weight(5.50)|difficulty(12)|head_armor(0)|body_armor(0)|leg_armor(32), imodbits_none, [], [fac.kingdom_2]],
    ["swadian_boots_royal", "Katilus' Ornate Boots", [("spak_plate_boots2", 0)], itp_type_foot_armor|itp_unique|itp_attach_armature, 0, 3180, abundance(0)|weight(7.50)|difficulty(15)|head_armor(0)|body_armor(0)|leg_armor(40), imodbits_none, [], [fac.kingdom_1]],
    ["nord_boots_royal", "Ragnar' Splinted Greaves", [("ssh_nord_splinted_greaves", 0)], itp_type_foot_armor|itp_unique|itp_attach_armature, 0, 2640, abundance(0)|weight(6.50)|difficulty(14)|head_armor(0)|body_armor(0)|leg_armor(36), imodbits_none, [], [fac.kingdom_4]],
    ["khergit_boots_royal", "Sanjar' Trophy Boots", [("ssh_suneate", 0)], itp_type_foot_armor|itp_unique|itp_attach_armature, 0, 2150, abundance(0)|weight(4.50)|difficulty(10)|head_armor(0)|body_armor(0)|leg_armor(32), imodbits_none, [], [fac.kingdom_3]],

    # Dark Knight boots
    ["wb_dk_plate_boots", "Dark Plate Boots", [("pellagus_dk_plate_boots", 0)], itp_type_foot_armor|itp_civilian|itp_attach_armature, 0, 2830, abundance(10)|weight(9.00)|difficulty(15)|head_armor(0)|body_armor(0)|leg_armor(38), imodbits_armor, [], [fac.dark_knights]],
    ["larktin_black_greaves", "Lady Larktin's Boots", [("spak_twilight_boots", 0)], itp_type_foot_armor|itp_unique|itp_civilian|itp_attach_armature, 0, 5370, abundance(0)|weight(9.00)|difficulty(15)|head_armor(0)|body_armor(0)|leg_armor(54), imodbits_none, [], [fac.dark_knights]],

    # GAUNTLETS

    # Regular gauntlets
    ["leather_gloves", "Leather Gloves", [("leather_gloves_L", 0)], itp_type_hand_armor|itp_merchandise, 0, 90, abundance(100)|weight(0.25)|difficulty(0)|head_armor(0)|body_armor(2)|leg_armor(0), imodbits_armor, [], []],
    ["mail_mittens", "Mail Mittens", [("mail_mittens_L", 0)], itp_type_hand_armor|itp_merchandise, 0, 260, abundance(100)|weight(1.00)|difficulty(0)|head_armor(0)|body_armor(4)|leg_armor(0), imodbits_armor, [], []],
    ["scale_gauntlets", "Scale Gauntlets", [("scale_gauntlets_b_L", 0)], itp_type_hand_armor|itp_merchandise, 0, 520, abundance(80)|weight(1.50)|difficulty(8)|head_armor(0)|body_armor(6)|leg_armor(0), imodbits_armor, [], []],
    ["lamellar_gauntlets", "Lamellar Gauntlets", [("scale_gauntlets_a_L", 0)], itp_type_hand_armor|itp_merchandise, 0, 870, abundance(50)|weight(2.00)|difficulty(10)|head_armor(0)|body_armor(8)|leg_armor(0), imodbits_armor, [], []],
    ["gauntlets", "Gauntlets", [("gauntlets_L", 0)], itp_type_hand_armor|itp_merchandise, 0, 1330, abundance(20)|weight(2.50)|difficulty(12)|head_armor(0)|body_armor(10)|leg_armor(0), imodbits_armor, [], []],
    ["mail_gauntlets", "Mail Gauntlets", [("narf_mail_gauntlets_L", 0)], itp_type_hand_armor|itp_merchandise, 0, 170, abundance(90)|weight(0.75)|difficulty(0)|head_armor(0)|body_armor(3)|leg_armor(0), imodbits_armor, [], []],
    ["plated_gauntlets", "Plated Gauntlets", [("narf_hourglass_gauntlets_L", 0)], itp_type_hand_armor, 0, 1800, abundance(10)|weight(2.50)|difficulty(14)|head_armor(0)|body_armor(12)|leg_armor(0), imodbits_armor, [], []],
    ["ornate_gauntlets", "Ornate Gauntlets", [("narf_hourglass_gauntlets_ornate_L", 0)], itp_type_hand_armor, 0, 2290, abundance(5)|weight(2.50)|difficulty(15)|head_armor(0)|body_armor(14)|leg_armor(0), imodbits_armor, [], []],
    ["mail_mittens_gilded", "Gilded Mail Mittens", [("njunja_brass_mail_mittens_L", 0)], itp_type_hand_armor, 0, 310, abundance(50)|weight(1.00)|difficulty(0)|head_armor(0)|body_armor(4)|leg_armor(0), imodbits_armor, [], []],
    ["scale_gauntlets_gilded", "Gilded Scale Gauntlets", [("njunja_brass_s_gauntlets_L", 0)], itp_type_hand_armor, 0, 580, abundance(40)|weight(1.50)|difficulty(8)|head_armor(0)|body_armor(6)|leg_armor(0), imodbits_armor, [], []],
    ["archer_gloves", "Vaegir Archer Gloves", [("tg_st_leatherglove_L", 0)], itp_type_hand_armor|itp_merchandise, 0, 100, abundance(60)|weight(0.25)|difficulty(0)|head_armor(0)|body_armor(2)|leg_armor(0), imodbits_armor, [], [fac.kingdom_2]],
    ["archer_vambraces", "Vaegir Archer Vambraces", [("tg_glovevambrace_set1_L", 0)], itp_type_hand_armor|itp_merchandise, 0, 320, abundance(30)|weight(0.50)|difficulty(0)|head_armor(0)|body_armor(4)|leg_armor(0), imodbits_armor, [], [fac.kingdom_2]],
    ["vaegir_gauntlets_royal", "Yaroglek's Bear Gauntlets", [("spak_beargauntlets_L", 0)], itp_type_hand_armor|itp_unique, 0, 2580, abundance(0)|weight(2.25)|difficulty(0)|head_armor(0)|body_armor(15)|leg_armor(0), imodbits_none, [], [fac.kingdom_2]],
    ["khergit_gauntlets_royal", "Sanjar's Trophy Gauntlets", [("ssh_kote_L", 0)], itp_type_hand_armor|itp_unique, 0, 2440, abundance(0)|weight(1.50)|difficulty(0)|head_armor(0)|body_armor(10)|leg_armor(0), imodbits_none, [], [fac.kingdom_3]],
    ["sarranid_gauntlets_royal", "Hakim's Gilded Gauntlets", [("njunja_brass_l_gauntlets_L", 0)], itp_type_hand_armor|itp_unique, 0, 2320, abundance(0)|weight(2.00)|difficulty(14)|head_armor(0)|body_armor(14)|leg_armor(0), imodbits_none, [], [fac.kingdom_6]],

    # Dark Knight gauntlets
    ["dark_gauntlet", "Dark Plate Gauntlets", [("spak_11gauntlets_L", 0)], itp_type_hand_armor, 0, 1380, abundance(100)|weight(2.50)|difficulty(12)|head_armor(0)|body_armor(12)|leg_armor(0), imodbits_armor, [], [fac.dark_knights]],
    ["dk_gauntlet", "Dark Knight Gauntlets", [("akosmo_czarne_gauntlets_L", 0)], itp_type_hand_armor, 0, 2030, abundance(50)|weight(3.00)|difficulty(13)|head_armor(0)|body_armor(14)|leg_armor(0), imodbits_armor, [], [fac.dark_knights]],
    ["larktin_gauntlets", "Lady Larktin's Gauntlets", [("spak_twilight_gloves_L", 0)], itp_type_hand_armor|itp_unique|itp_civilian, 0, 3970, abundance(0)|weight(2.00)|difficulty(18)|head_armor(0)|body_armor(20)|leg_armor(0), imodbits_none, [], [fac.dark_knights]],

    # BODY ARMORS

    # Female clothing
    ["lady_dress_ruby", "Lady Dress", [("lady_dress_r", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 1120, abundance(10)|weight(5.00)|difficulty(0)|head_armor(0)|body_armor(6)|leg_armor(1), imodbits_cloth_high, [], []],
    ["lady_dress_green", "Lady Dress", [("lady_dress_g", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 1120, abundance(10)|weight(5.00)|difficulty(0)|head_armor(0)|body_armor(6)|leg_armor(1), imodbits_cloth_high, [], []],
    ["lady_dress_blue", "Lady Dress", [("lady_dress_b", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 1120, abundance(10)|weight(5.00)|difficulty(0)|head_armor(0)|body_armor(6)|leg_armor(1), imodbits_cloth_high, [], []],
    ["red_dress", "Red Dress", [("red_dress", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 680, abundance(40)|weight(5.00)|difficulty(0)|head_armor(0)|body_armor(6)|leg_armor(1), imodbits_cloth_high, [], []],
    ["brown_dress", "Brown Dress", [("brown_dress", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 940, abundance(40)|weight(5.00)|difficulty(0)|head_armor(0)|body_armor(6)|leg_armor(1), imodbits_cloth_high, [], []],
    ["green_dress", "Green Dress", [("green_dress", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 780, abundance(40)|weight(5.00)|difficulty(0)|head_armor(0)|body_armor(6)|leg_armor(1), imodbits_cloth_high, [], []],
    ["khergit_lady_dress", "Khergit Lady Dress", [("khergit_lady_dress", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 1220, abundance(10)|weight(5.00)|difficulty(0)|head_armor(0)|body_armor(6)|leg_armor(1), imodbits_cloth_high, [], [fac.kingdom_3]],
    ["khergit_lady_dress_b", "Khergit Lady Dress", [("khergit_lady_dress_b", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 1410, abundance(10)|weight(6.50)|difficulty(0)|head_armor(0)|body_armor(12)|leg_armor(2), imodbits_cloth_high, [], [fac.kingdom_3]],
    ["sarranid_lady_dress", "Sarranid Lady Dress", [("sarranid_lady_dress", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 1290, abundance(10)|weight(5.00)|difficulty(0)|head_armor(0)|body_armor(6)|leg_armor(1), imodbits_cloth_high, [], [fac.kingdom_6]],
    ["sarranid_lady_dress_b", "Sarranid Lady Dress", [("sarranid_lady_dress_b", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 1290, abundance(10)|weight(5.00)|difficulty(0)|head_armor(0)|body_armor(6)|leg_armor(1), imodbits_cloth_high, [], [fac.kingdom_6]],
    ["sarranid_common_dress", "Sarranid Dress", [("sarranid_common_dress", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 260, abundance(70)|weight(5.00)|difficulty(0)|head_armor(0)|body_armor(6)|leg_armor(1), imodbits_cloth_med, [], [fac.kingdom_6]],
    ["sarranid_common_dress_b", "Sarranid Dress", [("sarranid_common_dress_b", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 260, abundance(70)|weight(5.00)|difficulty(0)|head_armor(0)|body_armor(6)|leg_armor(1), imodbits_cloth_med, [], [fac.kingdom_6]],
    ["dress", "Dress", [("dress", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 250, abundance(100)|weight(5.00)|difficulty(0)|head_armor(0)|body_armor(6)|leg_armor(1), imodbits_cloth_low, [], []],
    ["blue_dress", "Blue Dress", [("blue_dress_new", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 380, abundance(100)|weight(5.00)|difficulty(0)|head_armor(0)|body_armor(6)|leg_armor(1), imodbits_cloth_med, [], []],
    ["peasant_dress", "Peasant Dress", [("peasant_dress_b_new", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 250, abundance(100)|weight(5.00)|difficulty(0)|head_armor(0)|body_armor(6)|leg_armor(1), imodbits_cloth_low, [], []],
    ["woolen_dress", "Woolen Dress", [("woolen_dress", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 250, abundance(100)|weight(5.50)|difficulty(0)|head_armor(0)|body_armor(6)|leg_armor(1), imodbits_cloth_low, [], []],
    ["court_dress", "Court Dress", [("court_dress", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 1350, abundance(10)|weight(5.00)|difficulty(0)|head_armor(0)|body_armor(6)|leg_armor(1), imodbits_cloth_high, [], []],

    # Unisex and male clothing
    ["pilgrim_disguise", "Pilgrim Outfit", [("pilgrim_outfit", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 200, abundance(100)|weight(6.00)|difficulty(0)|head_armor(0)|body_armor(6)|leg_armor(2), imodbits_cloth_low, [], []],
    ["fur_coat", "Fur Coat", [("fur_coat", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 450, abundance(100)|weight(9.00)|difficulty(0)|head_armor(2)|body_armor(16)|leg_armor(4), imodbits_cloth_med, [], []],
    ["linen_tunic", "Cotton Shirt", [("shirt_a", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 240, abundance(100)|weight(4.00)|difficulty(0)|head_armor(0)|body_armor(5)|leg_armor(1), imodbits_cloth_med, [], []],
    ["red_shirt", "Noble Shirt", [("rich_tunic_a", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 670, abundance(40)|weight(4.50)|difficulty(0)|head_armor(0)|body_armor(5)|leg_armor(1), imodbits_cloth_high, [], []],
    ["red_tunic", "Plain Tunic (Red)", [("arena_tunicR_new", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 240, abundance(50)|weight(4.00)|difficulty(0)|head_armor(0)|body_armor(5)|leg_armor(1), imodbits_cloth_med, [], []],
    ["green_tunic", "Plain Tunic (Green)", [("arena_tunicG_new", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 240, abundance(50)|weight(4.00)|difficulty(0)|head_armor(0)|body_armor(5)|leg_armor(1), imodbits_cloth_med, [], []],
    ["blue_tunic", "Plain Tunic (Blue)", [("arena_tunicB_new", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 240, abundance(50)|weight(4.00)|difficulty(0)|head_armor(0)|body_armor(5)|leg_armor(1), imodbits_cloth_med, [], []],
    ["white_tunic", "Plain Tunic (White)", [("arena_tunicW_new", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 220, abundance(90)|weight(4.00)|difficulty(0)|head_armor(0)|body_armor(5)|leg_armor(1), imodbits_cloth_med, [], []],
    ["yellow_tunic", "Plain Tunic (Yellow)", [("arena_tunicY_new", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 240, abundance(50)|weight(4.00)|difficulty(0)|head_armor(0)|body_armor(5)|leg_armor(1), imodbits_cloth_med, [], []],
    #["robe", "Black Robe", [("robe", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 200, abundance(100)|weight(6.00)|difficulty(0)|head_armor(0)|body_armor(6)|leg_armor(2), imodbits_cloth_low, [], []],
    ["coarse_tunic", "Townsman Vest", [("coarse_tunic_a", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 260, abundance(80)|weight(5.00)|difficulty(0)|head_armor(0)|body_armor(7)|leg_armor(1), imodbits_cloth_med, [], []],
    ["leather_apron", "Leather Apron", [("leather_apron", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 280, abundance(100)|weight(6.00)|difficulty(0)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth_low, [], []],
    ["tabard", "Tabard", [("tabard_b", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 280, abundance(100)|weight(5.00)|difficulty(0)|head_armor(0)|body_armor(6)|leg_armor(1), imodbits_cloth_med, [], []],
    ["tunic_with_green_cape", "Tunic with Green Cape", [("peasant_man_a", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 250, abundance(100)|weight(4.50)|difficulty(0)|head_armor(0)|body_armor(6)|leg_armor(1), imodbits_cloth_med, [], []],
    ["ragged_outfit", "Ragged Outfit", [("ragged_outfit_a_new", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 180, abundance(50)|weight(5.50)|difficulty(0)|head_armor(1)|body_armor(11)|leg_armor(2), imodbits_cloth_low, [], []],
    ["rich_outfit", "Merchant Outfit", [("merchant_outf", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 550, abundance(20)|weight(6.00)|difficulty(0)|head_armor(0)|body_armor(6)|leg_armor(0), imodbits_cloth_high, [], []],
    ["nobleman_outfit", "Nobleman Outfit", [("nobleman_outfit_b_new", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 820, abundance(10)|weight(6.00)|difficulty(0)|head_armor(0)|body_armor(6)|leg_armor(0), imodbits_cloth_high, [], []],
    ["courtly_outfit", "Courtly Outfit", [("nobleman_outf", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 770, abundance(10)|weight(6.00)|difficulty(0)|head_armor(0)|body_armor(6)|leg_armor(0), imodbits_cloth_high, [], []],
    ["leather_jacket", "Leather Jacket", [("leather_jacket_new", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 360, abundance(100)|weight(11.00)|difficulty(0)|head_armor(2)|body_armor(18)|leg_armor(2), imodbits_cloth_med, [], []],
    ["pelt_coat", "Pelt Coat", [("thick_coat_a", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 200, abundance(100)|weight(10.00)|difficulty(0)|head_armor(1)|body_armor(16)|leg_armor(1), imodbits_cloth_med, [], []],
    ["rawhide_coat", "Rawhide Coat", [("coat_of_plates_b", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 300, abundance(100)|weight(10.00)|difficulty(0)|head_armor(2)|body_armor(16)|leg_armor(2), imodbits_cloth_med, [], []],
    ["nomad_vest", "Nomad Vest", [("nomad_vest_new", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 280, abundance(100)|weight(8.50)|difficulty(0)|head_armor(2)|body_armor(13)|leg_armor(3), imodbits_cloth_med, [], [fac.kingdom_3]],
    ["nomad_robe", "Nomad Robe", [("nomad_robe_a", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 280, abundance(100)|weight(7.50)|difficulty(0)|head_armor(1)|body_armor(15)|leg_armor(2), imodbits_cloth_med, [], [fac.kingdom_3]],
    ["sarranid_cloth_robe", "Sarranid Robe", [("sar_robe", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 300, abundance(50)|weight(6.00)|difficulty(0)|head_armor(1)|body_armor(9)|leg_armor(2), imodbits_cloth_med, [], [fac.kingdom_6]],
    ["sarranid_cloth_robe_b", "Sarranid Robe", [("sar_robe_b", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 300, abundance(50)|weight(6.00)|difficulty(0)|head_armor(1)|body_armor(9)|leg_armor(2), imodbits_cloth_med, [], [fac.kingdom_6]],
    ["sarranid_cloth_robe_c", "Sarranid Robe", [("pellagus_sarranid_cloth_robe_p1", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 300, abundance(50)|weight(6.00)|difficulty(0)|head_armor(1)|body_armor(9)|leg_armor(2), imodbits_cloth_med, [], [fac.kingdom_6]],
    ["sarranid_cloth_robe_d", "Sarranid Robe", [("pellagus_sarranid_cloth_robe_p2", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 300, abundance(50)|weight(6.00)|difficulty(0)|head_armor(1)|body_armor(9)|leg_armor(2), imodbits_cloth_med, [], [fac.kingdom_6]],
    ["sarranid_cloth_robe_e", "Sarranid Robe", [("pellagus_sarranid_cloth_robe_p3", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 300, abundance(50)|weight(6.00)|difficulty(0)|head_armor(1)|body_armor(9)|leg_armor(2), imodbits_cloth_med, [], [fac.kingdom_6]],
    ["gambeson", "White Gambeson", [("lav_gambeson_a_white", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 330, abundance(100)|weight(8.50)|difficulty(0)|head_armor(0)|body_armor(10)|leg_armor(1), imodbits_cloth_med, [], []],
    ["blue_gambeson", "Blue Gambeson", [("lav_gambeson_a_blue", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 330, abundance(100)|weight(8.50)|difficulty(0)|head_armor(0)|body_armor(10)|leg_armor(1), imodbits_cloth_med, [], []],
    ["red_gambeson", "Red Gambeson", [("lav_gambeson_a_red", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 330, abundance(100)|weight(8.50)|difficulty(0)|head_armor(0)|body_armor(10)|leg_armor(1), imodbits_cloth_med, [], []],
    ["nordic_shirt_01", "Nordic Shirt", [("ad_nordic_shirt_01", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 250, abundance(40)|weight(4.00)|difficulty(0)|head_armor(0)|body_armor(5)|leg_armor(1), imodbits_cloth_med, [], [fac.kingdom_4]],
    ["nordic_shirt_02", "Nordic Shirt", [("ad_nordic_shirt_02", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 250, abundance(40)|weight(4.00)|difficulty(0)|head_armor(0)|body_armor(5)|leg_armor(1), imodbits_cloth_med, [], [fac.kingdom_4]],
    ["nordic_shirt_03", "Nordic Shirt", [("ad_nordic_shirt_03", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 250, abundance(40)|weight(4.00)|difficulty(0)|head_armor(0)|body_armor(5)|leg_armor(1), imodbits_cloth_med, [], [fac.kingdom_4]],
    ["nordic_shirt_04", "Nordic Shirt", [("ad_nordic_shirt_04", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 250, abundance(40)|weight(4.00)|difficulty(0)|head_armor(0)|body_armor(5)|leg_armor(1), imodbits_cloth_med, [], [fac.kingdom_4]],
    ["nordic_shirt_05", "Nordic Shirt", [("ad_nordic_shirt_05", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 250, abundance(40)|weight(4.00)|difficulty(0)|head_armor(0)|body_armor(5)|leg_armor(1), imodbits_cloth_med, [], [fac.kingdom_4]],
    ["nordic_shirt_06", "Nordic Shirt", [("ad_nordic_shirt_06", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 250, abundance(40)|weight(4.00)|difficulty(0)|head_armor(0)|body_armor(5)|leg_armor(1), imodbits_cloth_med, [], [fac.kingdom_4]],
    ["sarranid_vest_a", "Sarranid Vest", [("wei_xiadi_archers_vest01", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 260, abundance(90)|weight(6.50)|difficulty(0)|head_armor(2)|body_armor(12)|leg_armor(2), imodbits_cloth_med, [], [fac.kingdom_6]],
    ["sarranid_vest_b", "Sarranid Vest", [("wei_xiadi_archers_vest02", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 260, abundance(90)|weight(6.50)|difficulty(0)|head_armor(2)|body_armor(12)|leg_armor(2), imodbits_cloth_med, [], [fac.kingdom_6]],
    ["leather_vest", "Leather Vest", [("leather_vest_a", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 440, abundance(100)|weight(9.00)|difficulty(0)|head_armor(0)|body_armor(16)|leg_armor(3), imodbits_armor, [], []],
    ["padded_cloth", "Aketon", [("padded_cloth_a", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 640, abundance(100)|weight(12.00)|difficulty(0)|head_armor(3)|body_armor(17)|leg_armor(3), imodbits_armor, [], []],
    ["aketon_green", "Padded Cloth", [("padded_cloth_b", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 470, abundance(100)|weight(10.00)|difficulty(0)|head_armor(2)|body_armor(15)|leg_armor(2), imodbits_armor, [], []],
    ["leather_jerkin", "Leather Jerkin", [("ragged_leather_jerkin", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 670, abundance(100)|weight(9.00)|difficulty(0)|head_armor(1)|body_armor(20)|leg_armor(2), imodbits_armor, [], []],
    ["tribal_warrior_outfit", "Tribal Warrior Outfit", [("tribal_warrior_outfit_a_new", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 860, abundance(90)|weight(13.50)|difficulty(0)|head_armor(3)|body_armor(20)|leg_armor(4), imodbits_armor, [], [fac.kingdom_3]],
    ["khergit_leather_a", "Khergit Hard Leather", [("wei_xiadi_lamellar_armor_a_b_1", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 1570, abundance(80)|weight(9.00)|difficulty(7)|head_armor(4)|body_armor(28)|leg_armor(5), imodbits_armor, [], [fac.kingdom_3]],
    ["khergit_leather_b", "Khergit Hard Leather", [("wei_xiadi_lamellar_armor_ab", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 1570, abundance(80)|weight(9.00)|difficulty(7)|head_armor(4)|body_armor(28)|leg_armor(5), imodbits_armor, [], [fac.kingdom_3]],
    ["nordic_courtly_shirt_a", "Nordic Courtly Outfit", [("bwl_nordiclightarmor4", 0)], itp_type_body_armor|itp_civilian|itp_covers_legs, 0, 920, abundance(10)|weight(5.00)|difficulty(0)|head_armor(1)|body_armor(7)|leg_armor(1), imodbits_cloth_high, [], [fac.kingdom_4]],
    ["nordic_courtly_shirt_b", "Nordic Courtly Outfit", [("bwl_nordiclightarmor5", 0)], itp_type_body_armor|itp_civilian|itp_covers_legs, 0, 920, abundance(10)|weight(5.00)|difficulty(0)|head_armor(1)|body_armor(7)|leg_armor(1), imodbits_cloth_high, [], [fac.kingdom_4]],
    ["nordic_courtly_shirt_c", "Nordic Courtly Outfit", [("bwl_nordiclightarmor6", 0)], itp_type_body_armor|itp_civilian|itp_covers_legs, 0, 920, abundance(10)|weight(5.00)|difficulty(0)|head_armor(1)|body_armor(7)|leg_armor(1), imodbits_cloth_high, [], [fac.kingdom_4]],

    # Special body armors
    ["wedding_dress", "Wedding Dress", [("pellagus_wedding_dress", 0)], itp_type_body_armor|itp_civilian|itp_covers_legs, 0, 1250, abundance(100)|weight(6.00)|difficulty(0)|head_armor(0)|body_armor(6)|leg_armor(0), imodbits_none, [], []],
    ["ssin_low_armour", "Novice Assassin's Armour", [("pellagus_assassin_low_armour", 0)], itp_type_body_armor|itp_covers_legs, 0, 480, abundance(25)|weight(7.50)|difficulty(0)|head_armor(0)|body_armor(16)|leg_armor(0), imodbits_cloth_low, [], [fac.outlaws]],
    ["ssin_med_armour", "Assassin's Armour", [("pellagus_assassin_med_armour", 0)], itp_type_body_armor|itp_covers_legs, 0, 1120, abundance(25)|weight(10.50)|difficulty(8)|head_armor(0)|body_armor(26)|leg_armor(0), imodbits_armor, [], [fac.outlaws]],
    ["ssin_high_armour", "Royal Assassin's Armour", [("pellagus_assassin_high_armour", 0)], itp_type_body_armor|itp_covers_legs, 0, 2380, abundance(25)|weight(18.00)|difficulty(11)|head_armor(0)|body_armor(36)|leg_armor(8), imodbits_armor, [], [fac.outlaws]],

    # Common body armors
    ["light_leather", "Light Leather", [("light_leather", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 640, abundance(100)|weight(10.00)|difficulty(0)|head_armor(2)|body_armor(19)|leg_armor(1), imodbits_armor, [], []],
    ["leather_armor", "Leather Armor Vest", [("tattered_leather_armor_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 780, abundance(100)|weight(12.00)|difficulty(0)|head_armor(2)|body_armor(21)|leg_armor(2), imodbits_armor, [], []],
    ["padded_leather", "Padded Leather Vest", [("leather_armor_b", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1020, abundance(100)|weight(12.50)|difficulty(0)|head_armor(3)|body_armor(24)|leg_armor(2), imodbits_armor, [], []],
    ["leather_armor_shirt", "Padded Leather Armor", [("pino_shirt_leather_plate", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1360, abundance(100)|weight(14.00)|difficulty(0)|head_armor(3)|body_armor(28)|leg_armor(4), imodbits_armor, [], []],
    ["studded_leather_coat", "Studded Leather Coat", [("leather_armor_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1580, abundance(100)|weight(17.00)|difficulty(11)|head_armor(2)|body_armor(32)|leg_armor(4), imodbits_armor, [], []],
    ["light_mail_and_plate", "Light Mail and Plate", [("light_mail_and_plate", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2290, abundance(40)|weight(17.50)|difficulty(12)|head_armor(4)|body_armor(32)|leg_armor(8), imodbits_armor, [], []],
    ["haubergeon", "Haubergeon", [("haubergeon_c", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1990, abundance(100)|weight(16.00)|difficulty(10)|head_armor(6)|body_armor(34)|leg_armor(2), imodbits_armor, [], []],
    ["mail_shirt", "Mail Shirt", [("mail_shirt_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1900, abundance(100)|weight(20.00)|difficulty(12)|head_armor(2)|body_armor(35)|leg_armor(6), imodbits_armor, [], []],
    ["mail_and_plate", "Mail and Plate", [("mail_and_plate", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2420, abundance(50)|weight(19.00)|difficulty(12)|head_armor(4)|body_armor(35)|leg_armor(6), imodbits_armor, [], []],
    ["mail_hauberk", "Mail Hauberk", [("hauberk_a_new", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2160, abundance(100)|weight(20.00)|difficulty(12)|head_armor(4)|body_armor(35)|leg_armor(8), imodbits_armor, [], []],
    ["mail_hauberk_b", "Mail Hauberk", [("bwl_hauberk5", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2160, abundance(100)|weight(20.00)|difficulty(12)|head_armor(4)|body_armor(35)|leg_armor(8), imodbits_armor, [], []],
    ["mail_with_surcoat", "Mail with Surcoat", [("mail_long_surcoat_new", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2180, abundance(85)|weight(21.00)|difficulty(13)|head_armor(2)|body_armor(36)|leg_armor(8), imodbits_armor, [], []],
    ["surcoat_over_mail", "Surcoat over Mail", [("surcoat_over_mail_new", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2180, abundance(85)|weight(21.00)|difficulty(13)|head_armor(2)|body_armor(36)|leg_armor(8), imodbits_armor, [], []],

    # Heraldic body armors
    ["hera_arena_tunic", "Heraldic Plane Tunic", [("arena_tunicW_new", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 270, abundance(50)|weight(4.00)|difficulty(0)|head_armor(0)|body_armor(5)|leg_armor(1), imodbits_cloth_med, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.heraldic_arena_tunic_new, l.agent_id, l.troop_id)])], []],
    ["hera_shirt_a", "Heraldic Linen Tunic", [("shirt_a", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 290, abundance(100)|weight(4.00)|difficulty(0)|head_armor(0)|body_armor(5)|leg_armor(1), imodbits_cloth_med, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.heraldic_shirt_a, l.agent_id, l.troop_id)])], []],
    ["hera_tabard_b", "Heraldic Tabard", [("tabard_b", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 340, abundance(100)|weight(5.00)|difficulty(0)|head_armor(0)|body_armor(6)|leg_armor(1), imodbits_cloth_med, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.heraldic_tabard_b, l.agent_id, l.troop_id)])], []],
    ["hera_rich_tunic_a", "Heraldic Tunic", [("rich_tunic_a", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 750, abundance(40)|weight(4.50)|difficulty(0)|head_armor(0)|body_armor(5)|leg_armor(1), imodbits_cloth_high, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.heraldic_rich_tunic_a, l.agent_id, l.troop_id)])], []],
    ["hera_archers_vest", "Heraldic Archer's Padded Vest", [("archers_vest", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 460, abundance(90)|weight(8.00)|difficulty(0)|head_armor(2)|body_armor(15)|leg_armor(1), imodbits_armor, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.heraldic_archers_vest, l.agent_id, l.troop_id)])], [fac.kingdom_6]],
    ["hera_padded_cloth_b", "Heraldic Padded Cloth", [("padded_cloth_b", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 480, abundance(90)|weight(10.00)|difficulty(0)|head_armor(2)|body_armor(15)|leg_armor(2), imodbits_armor, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.heraldic_padded_cloth_b, l.agent_id, l.troop_id)])], []],
    ["hera_leather_vest", "Heraldic Leather Vest", [("leather_vest_a", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 560, abundance(90)|weight(9.00)|difficulty(0)|head_armor(0)|body_armor(18)|leg_armor(3), imodbits_armor, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.heraldic_leather_vest_a, l.agent_id, l.troop_id)])], []],
    ["hera_leather_armor_shirt", "Heraldic Leather Armor", [("pino_shirt_leather_plate", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1400, abundance(90)|weight(14.00)|difficulty(0)|head_armor(3)|body_armor(28)|leg_armor(4), imodbits_armor, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.heraldic_shirt_leather_plate, l.agent_id, l.troop_id)])], []],
    ["hera_padded_cloth_a", "Heraldic Aketon", [("padded_cloth_a", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 660, abundance(90)|weight(12.00)|difficulty(0)|head_armor(3)|body_armor(17)|leg_armor(3), imodbits_armor, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.heraldic_padded_cloth_a, l.agent_id, l.troop_id)])], []],
    ["hera_tribal_warrior_outfit_a_new", "Heraldic Tribal Warrior Outfit", [("tribal_warrior_outfit_a_new", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 860, abundance(90)|weight(13.50)|difficulty(0)|head_armor(3)|body_armor(20)|leg_armor(4), imodbits_armor, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.heraldic_tribal_warrior_outfit_a_new, l.agent_id, l.troop_id)])], [fac.kingdom_3]],
    ["hera_sarranid_leather_armor", "Heraldic Sarranid Leather Armor", [("sarranid_leather_armor", 0)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_covers_legs, 0, 1400, abundance(90)|weight(14.00)|difficulty(0)|head_armor(4)|body_armor(26)|leg_armor(6), imodbits_armor, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.heraldic_sarranid_leather_armor, l.agent_id, l.troop_id)])], [fac.kingdom_6]],
    ["heraldic_mail_with_tunic_b", "Heraldic Mail Tunic", [("heraldic_armor_new_c", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1560, abundance(90)|weight(18.00)|difficulty(12)|head_armor(2)|body_armor(32)|leg_armor(2), imodbits_armor, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.heraldic_armor_c, l.agent_id, l.troop_id)])], [fac.kingdom_1]],
    ["hera_arena_armor", "Heraldic Mail Shirt", [("arena_armorW_new", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2210, abundance(80)|weight(20.00)|difficulty(12)|head_armor(2)|body_armor(36)|leg_armor(8), imodbits_armor, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.heraldic_arena_armor_new, l.agent_id, l.troop_id)])], [fac.kingdom_1]],
    ["hera_brigandine_b", "Heraldic Brigandine", [("brigandine_b", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2310, abundance(80)|weight(19.00)|difficulty(12)|head_armor(2)|body_armor(40)|leg_armor(2), imodbits_armor, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.heraldic_brigandine_b, l.agent_id, l.troop_id)])], [fac.kingdom_5]],
    ["hera_light_mail_and_plate", "Heraldic Light Mail and Plate", [("light_mail_and_plate", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2290, abundance(40)|weight(17.50)|difficulty(12)|head_armor(4)|body_armor(32)|leg_armor(8), imodbits_armor, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.heraldic_light_mail_and_plate, l.agent_id, l.troop_id)])], [fac.kingdom_1]],
    ["heraldic_mail_with_tabard", "Heraldic Mail with Tabard", [("heraldic_armor_new_d", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2480, abundance(70)|weight(21.00)|difficulty(12)|head_armor(2)|body_armor(38)|leg_armor(8), imodbits_armor, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.heraldic_armor_d, l.agent_id, l.troop_id)])], [fac.kingdom_1]],
    ["hera_mail_long_surcoat", "Heraldic Mail with Surcoat", [("mail_long_surcoat_new", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2480, abundance(70)|weight(22.00)|difficulty(12)|head_armor(2)|body_armor(38)|leg_armor(8), imodbits_armor, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.heraldic_mail_long_surcoat_new, l.agent_id, l.troop_id)])], [fac.kingdom_1]],
    ["hera_mail_and_plate", "Heraldic Mail and Plate", [("mail_and_plate", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2420, abundance(50)|weight(19.00)|difficulty(12)|head_armor(4)|body_armor(35)|leg_armor(6), imodbits_armor, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.heraldic_mail_and_plate, l.agent_id, l.troop_id)])], [fac.kingdom_1]],
    ["hera_cuir_bouilli_a", "Heraldic Cuir Bouilli", [("cuir_bouilli_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3520, abundance(50)|weight(26.00)|difficulty(14)|head_armor(4)|body_armor(43)|leg_armor(10), imodbits_armor, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.heraldic_cuir_bouilli_a, l.agent_id, l.troop_id)])], [fac.kingdom_1]],
    ["hera_plate_armor", "Heraldic Plate Armor", [("full_plate_armor", 0)], itp_type_body_armor|itp_covers_legs, 0, 5350, abundance(30)|weight(38.00)|difficulty(15)|head_armor(4)|body_armor(52)|leg_armor(16), imodbits_armor, [(ti_on_init_item, [(store_trigger_param_1, l.agent_id), (store_trigger_param_2, l.troop_id), (call_script, script.shield_item_set_banner, tableau.heraldic_full_plate_armor, l.agent_id, l.troop_id)])], [fac.kingdom_1]],

    # Swadian armors
    ["cuir_bouilli", "Cuir Bouilli", [("cuir_bouilli_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3520, abundance(50)|weight(26.00)|difficulty(14)|head_armor(4)|body_armor(43)|leg_armor(10), imodbits_armor, [], [fac.kingdom_1]],
    ["plate_armor", "Plate Armor", [("full_plate_armor", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 5500, abundance(20)|weight(38.00)|difficulty(15)|head_armor(4)|body_armor(52)|leg_armor(16), imodbits_armor, [], [fac.kingdom_1]],
    ["swadian_armor_lord_a", "Swadian Ornate Plate", [("pellagus_full_plate_rhodok", 0)], itp_type_body_armor|itp_covers_legs, 0, 8630, abundance(5)|weight(43.00)|difficulty(18)|head_armor(14)|body_armor(58)|leg_armor(18), imodbits_armor, [], [fac.kingdom_1]],
    ["swadian_armor_lord_b", "Swadian Ornate Plate", [("pellagus_full_plate_rhodok2", 0)], itp_type_body_armor|itp_covers_legs, 0, 8630, abundance(5)|weight(43.00)|difficulty(18)|head_armor(14)|body_armor(58)|leg_armor(18), imodbits_armor, [], [fac.kingdom_1]],
    ["swadian_armor_royal", "Queen Katilus' Armor", [("pellagus_full_plate_swadian", 0)], itp_type_body_armor|itp_unique|itp_covers_legs, 0, 9320, abundance(0)|weight(42.00)|difficulty(18)|head_armor(15)|body_armor(60)|leg_armor(18), imodbits_armor, [], [fac.kingdom_1]],

    # Vaegir armors
    ["vaegir_inf_armor_a", "Vaegir Leather Armor", [("kovas_armor_17", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1330, abundance(90)|weight(16.00)|difficulty(9)|head_armor(2)|body_armor(28)|leg_armor(4), imodbits_armor, [], [fac.kingdom_2]],
    ["vaegir_chain", "Vaegir Chain Mail", [("narf_rus_chain", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2030, abundance(80)|weight(23.00)|difficulty(12)|head_armor(2)|body_armor(36)|leg_armor(4), imodbits_armor, [], [fac.kingdom_2]],
    ["coat_of_plates", "Coat of Plates (Black)", [("coat_of_plates_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2340, abundance(75)|weight(26.50)|difficulty(13)|head_armor(4)|body_armor(35)|leg_armor(8), imodbits_armor, [], [fac.kingdom_2]],
    ["coat_of_plates_red", "Coat of Plates (Red)", [("coat_of_plates_red", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2340, abundance(75)|weight(26.50)|difficulty(13)|head_armor(4)|body_armor(35)|leg_armor(8), imodbits_armor, [], [fac.kingdom_2]],
    ["vaegir_inf_armor_b", "Vaegir Infantry Cuirass", [("kovas_armor_18", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2540, abundance(75)|weight(21.00)|difficulty(11)|head_armor(6)|body_armor(37)|leg_armor(4), imodbits_armor, [], [fac.kingdom_2]],
    ["vaegir_lamellar_a", "Vaegir Lamellar Chain", [("narf_rus_lamellar_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2730, abundance(50)|weight(29.00)|difficulty(14)|head_armor(2)|body_armor(41)|leg_armor(4), imodbits_armor, [], [fac.kingdom_2]],
    ["vaegir_lamellar_b", "Vaegir Lamellar Chain", [("narf_rus_lamellar_b", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2730, abundance(50)|weight(29.00)|difficulty(14)|head_armor(2)|body_armor(41)|leg_armor(4), imodbits_armor, [], [fac.kingdom_2]],
    ["banded_armor", "Banded Armor", [("banded_armor_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3880, abundance(50)|weight(32.00)|difficulty(14)|head_armor(6)|body_armor(43)|leg_armor(12), imodbits_armor, [], [fac.kingdom_2]],
    ["vaegir_scaled_cuirass", "Vaegir Scaled Cuirass", [("narf_rus_scale", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3770, abundance(25)|weight(27.00)|difficulty(14)|head_armor(6)|body_armor(45)|leg_armor(2), imodbits_armor, [], [fac.kingdom_2]],
    ["vaegir_inf_armor_c", "Vaegir Infantry Armor", [("kovas_armor_19", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 4010, abundance(50)|weight(31.00)|difficulty(16)|head_armor(8)|body_armor(45)|leg_armor(6), imodbits_armor, [], [fac.kingdom_2]],
    ["vaegir_kuyak_c", "Kuyak", [("narf_kuyak_c", 0)], itp_type_body_armor|itp_covers_legs, 0, 2290, abundance(40)|weight(21.00)|difficulty(12)|head_armor(4)|body_armor(34)|leg_armor(4), imodbits_armor, [], [fac.kingdom_2]],
    ["vaegir_kuyak_d", "Reinforced Kuyak", [("narf_kuyak_d", 0)], itp_type_body_armor|itp_covers_legs, 0, 3000, abundance(30)|weight(24.00)|difficulty(14)|head_armor(4)|body_armor(40)|leg_armor(4), imodbits_armor, [], [fac.kingdom_2]],
    ["vaegir_kuyak_a", "Studded Kuyak", [("narf_kuyak_a", 0)], itp_type_body_armor|itp_covers_legs, 0, 3820, abundance(20)|weight(28.00)|difficulty(15)|head_armor(4)|body_armor(46)|leg_armor(4), imodbits_armor, [], [fac.kingdom_2]],
    ["vaegir_kuyak_b", "Studded Kuyak", [("narf_kuyak_b", 0)], itp_type_body_armor|itp_covers_legs, 0, 3820, abundance(20)|weight(28.00)|difficulty(15)|head_armor(4)|body_armor(46)|leg_armor(4), imodbits_armor, [], [fac.kingdom_2]],
    ["vaegir_armor_lord_a", "Knyaz Banded Armor", [("bwl_banded_armor_heavy1", 0)], itp_type_body_armor|itp_covers_legs, 0, 5040, abundance(10)|weight(31.00)|difficulty(15)|head_armor(6)|body_armor(50)|leg_armor(8), imodbits_armor, [], [fac.kingdom_2]],
    ["vaegir_armor_royal", "Yaroglek's Bear Armor", [("spak_bear_warrior", 0)], itp_type_body_armor|itp_unique|itp_covers_legs, 0, 8000, abundance(0)|weight(32.00)|difficulty(17)|head_armor(14)|body_armor(58)|leg_armor(10), imodbits_none, [], [fac.kingdom_2]],

    # Khergit armors
    ["nomad_armor", "Khergit Armor Shirt", [("nomad_armor_new", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 400, abundance(100)|weight(9.00)|difficulty(0)|head_armor(4)|body_armor(12)|leg_armor(1), imodbits_armor, [], [fac.kingdom_3]],
    ["khergit_armor", "Khergit Armor Vest", [("khergit_armor_new", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 610, abundance(100)|weight(7.00)|difficulty(0)|head_armor(6)|body_armor(14)|leg_armor(2), imodbits_armor, [], [fac.kingdom_3]],
    ["steppe_armor", "Khergit Leather Cuirass", [("lamellar_leather", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 640, abundance(100)|weight(9.00)|difficulty(0)|head_armor(1)|body_armor(20)|leg_armor(1), imodbits_armor, [], [fac.kingdom_3]],
    ["lamellar_vest", "Khergit Breastplate", [("lamellar_vest_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1330, abundance(90)|weight(15.00)|difficulty(8)|head_armor(1)|body_armor(30)|leg_armor(2), imodbits_armor, [], [fac.kingdom_3]],
    ["lamellar_vest_khergit", "Khergit Breastplate", [("lamellar_vest_b", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1330, abundance(90)|weight(15.00)|difficulty(8)|head_armor(1)|body_armor(30)|leg_armor(2), imodbits_armor, [], [fac.kingdom_3]],
    ["khergit_clansman_vest", "Khergit Clansman Vest", [("wei_xiadi_kher_lamellar_vest01", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1510, abundance(100)|weight(14.50)|difficulty(8)|head_armor(4)|body_armor(29)|leg_armor(4), imodbits_armor, [], [fac.kingdom_3]],
    ["khergit_chain", "Khergit Rider Chain", [("kovas_armor_48", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1880, abundance(90)|weight(16.00)|difficulty(9)|head_armor(6)|body_armor(32)|leg_armor(2), imodbits_armor, [], [fac.kingdom_3]],
    ["khergit_kharash_vest", "Khergit Kharash Vest", [("wei_xiadi_kher_lamellar_vest02", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2160, abundance(100)|weight(19.00)|difficulty(10)|head_armor(4)|body_armor(37)|leg_armor(4), imodbits_armor, [], [fac.kingdom_3]],
    ["khergit_clansman_armor", "Khergit Clansman Armor", [("wei_xiadi_lamellar_chainmail", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2720, abundance(100)|weight(24.00)|difficulty(13)|head_armor(10)|body_armor(36)|leg_armor(6), imodbits_armor, [], [fac.kingdom_3]],
    ["khergit_mail_plate_a", "Khergit Mail Plate", [("arabian_armor_b", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3090, abundance(65)|weight(22.00)|difficulty(12)|head_armor(4)|body_armor(44)|leg_armor(3), imodbits_armor, [], [fac.kingdom_3]],
    ["khergit_mail_plate_b", "Khergit Mail Plate", [("pellagus_arabian_armor_p3", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3090, abundance(65)|weight(22.00)|difficulty(12)|head_armor(4)|body_armor(44)|leg_armor(3), imodbits_armor, [], [fac.kingdom_3]],
    ["khergit_mail_plate_c", "Khergit Mail Plate", [("pellagus_arabian_armor_p4", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3090, abundance(65)|weight(22.00)|difficulty(12)|head_armor(4)|body_armor(44)|leg_armor(3), imodbits_armor, [], [fac.kingdom_3]],
    ["khergit_lancer_cuirass", "Khergit Lancer Cuirass", [("njunja_lamellar_armor_f", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3210, abundance(70)|weight(29.00)|difficulty(14)|head_armor(4)|body_armor(42)|leg_armor(10), imodbits_armor, [], [fac.kingdom_3]],
    ["khergit_kharash_armor", "Khergit Kharash Armor", [("wei_xiadi_lamellar_armor01", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 5080, abundance(100)|weight(30.00)|difficulty(15)|head_armor(14)|body_armor(52)|leg_armor(8), imodbits_armor, [], [fac.kingdom_3]],
    ["lamellar_armor", "Khergit Lamellar Armor", [("lamellar_armor_b", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 4590, abundance(45)|weight(27.00)|difficulty(14)|head_armor(8)|body_armor(48)|leg_armor(8), imodbits_armor, [], [fac.kingdom_3]],
    ["khergit_lancer_armor", "Khergit Lancer Armor", [("njunja_heavy_lamellar_armor", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 5640, abundance(40)|weight(37.00)|difficulty(17)|head_armor(10)|body_armor(50)|leg_armor(14), imodbits_armor, [], [fac.kingdom_3]],
    ["khergit_mangudai_cuirass_a", "Mangudai Cuirass", [("sonyer_mailsarazin", 0)], itp_type_body_armor|itp_covers_legs, 0, 4290, abundance(25)|weight(19.00)|difficulty(13)|head_armor(8)|body_armor(45)|leg_armor(6), imodbits_armor, [], [fac.kingdom_3]],
    ["khergit_mangudai_cuirass_b", "Mangudai Full Cuirass", [("sonyer_lamelarghulam", 0)], itp_type_body_armor|itp_covers_legs, 0, 4690, abundance(15)|weight(20.00)|difficulty(13)|head_armor(10)|body_armor(45)|leg_armor(6), imodbits_armor, [], [fac.kingdom_3]],
    ["tarkhan_lamellar", "Tarkhan Armor", [("lamellar_armor_a", 0)], itp_type_body_armor|itp_covers_legs, 0, 6350, abundance(15)|weight(32.00)|difficulty(17)|head_armor(12)|body_armor(50)|leg_armor(14), imodbits_armor, [], [fac.kingdom_3]],
    ["khergit_mangudai_armor", "Mangudai Lamellar Armor", [("sonyer_saracenghulam", 0)], itp_type_body_armor|itp_covers_legs, 0, 6690, abundance(5)|weight(25.00)|difficulty(16)|head_armor(14)|body_armor(50)|leg_armor(12), imodbits_armor, [], [fac.kingdom_3]],
    ["khergit_jurtchi_armor", "Jurtchi Lamellar Armor", [("wei_xiadi_sarranid_mamluk_armor", 0)], itp_type_body_armor|itp_covers_legs, 0, 7550, abundance(5)|weight(38.00)|difficulty(18)|head_armor(10)|body_armor(57)|leg_armor(16), imodbits_armor, [], [fac.kingdom_3]],
    ["khergit_armor_royal", "Sanjar's Trophy Armor", [("ssh_yoroi", 0)], itp_type_body_armor|itp_unique|itp_covers_legs, 0, 8000, abundance(0)|weight(28.00)|difficulty(18)|head_armor(14)|body_armor(56)|leg_armor(14), imodbits_none, [], [fac.kingdom_3]],

    # Nordic armors
    ["nordic_archer_armor_a", "Broigne Shirt", [("pino_broigne3", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1330, abundance(90)|weight(17.00)|difficulty(10)|head_armor(4)|body_armor(26)|leg_armor(4), imodbits_armor, [], [fac.kingdom_4]],
    ["nordic_archer_armor_b", "Broigne Armor", [("pino_broigne_shirt", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1770, abundance(80)|weight(19.00)|difficulty(11)|head_armor(4)|body_armor(30)|leg_armor(6), imodbits_armor, [], [fac.kingdom_4]],
    ["nordic_archer_armor_c1", "Nordic Ring Mail", [("pino_leather_ring", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2140, abundance(70)|weight(20.00)|difficulty(12)|head_armor(6)|body_armor(32)|leg_armor(5), imodbits_armor, [], [fac.kingdom_4]],
    ["nordic_archer_armor_c2", "Nordic Ring Mail", [("pino_leather_ringfur", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2140, abundance(70)|weight(20.00)|difficulty(12)|head_armor(6)|body_armor(32)|leg_armor(5), imodbits_armor, [], [fac.kingdom_4]],
    ["nordic_archer_armor_d", "Nordic Scale Mail", [("pino_rough_macle_fured", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3520, abundance(50)|weight(24.00)|difficulty(14)|head_armor(8)|body_armor(40)|leg_armor(8), imodbits_armor, [], [fac.kingdom_4]],
    ["byrnie", "Byrnie", [("byrnie_a_new", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2340, abundance(100)|weight(17.00)|difficulty(11)|head_armor(6)|body_armor(38)|leg_armor(2), imodbits_armor, [], [fac.kingdom_4]],
    ["nordic_byrnie_1", "Nordic Byrnie", [("bwl_byrnie1", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2860, abundance(100)|weight(17.00)|difficulty(11)|head_armor(8)|body_armor(41)|leg_armor(3), imodbits_armor, [], [fac.kingdom_4]],
    ["nordic_byrnie_6", "Nordic Byrnie", [("bwl_byrnie6", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2860, abundance(100)|weight(17.00)|difficulty(11)|head_armor(8)|body_armor(41)|leg_armor(3), imodbits_armor, [], [fac.kingdom_4]],
    ["nordic_hauberk_1", "Nordic Hauberk", [("bwl_hauberk1", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2530, abundance(100)|weight(21.50)|difficulty(14)|head_armor(6)|body_armor(38)|leg_armor(6), imodbits_armor, [], [fac.kingdom_4]],
    ["nordic_hauberk_4", "Nordic Hauberk", [("bwl_hauberk4", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2530, abundance(100)|weight(21.50)|difficulty(14)|head_armor(6)|body_armor(38)|leg_armor(6), imodbits_armor, [], [fac.kingdom_4]],
    ["nordic_leather_1", "Nordic Leather Cuirass", [("bwl_lamellar_armor_dragon1", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1290, abundance(100)|weight(13.00)|difficulty(10)|head_armor(4)|body_armor(27)|leg_armor(2), imodbits_armor, [], [fac.kingdom_4]],
    ["nordic_leather_2", "Nordic Leather Cuirass", [("bwl_lamellar_armor_raven1", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1290, abundance(100)|weight(13.00)|difficulty(10)|head_armor(4)|body_armor(27)|leg_armor(2), imodbits_armor, [], [fac.kingdom_4]],
    ["scale_armor", "Scale Armor", [("lamellar_armor_e", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2910, abundance(90)|weight(25.00)|difficulty(13)|head_armor(6)|body_armor(42)|leg_armor(4), imodbits_armor, [], [fac.kingdom_4]],
    ["nordic_decor_scale_1", "Nordic Scale Armor", [("bwl_lamellar_armor_horses2", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3780, abundance(70)|weight(24.00)|difficulty(14)|head_armor(8)|body_armor(46)|leg_armor(4), imodbits_armor, [], [fac.kingdom_4]],
    ["nordic_decor_scale_2", "Nordic Scale Armor", [("bwl_lamellar_armor_unicorn2", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3780, abundance(70)|weight(24.00)|difficulty(14)|head_armor(8)|body_armor(46)|leg_armor(4), imodbits_armor, [], [fac.kingdom_4]],
    ["nordic_noble_armor_1", "Housecarl Armor", [("bwl_gambeson_and_leather2", 0)], itp_type_body_armor|itp_covers_legs, 0, 2390, abundance(40)|weight(22.00)|difficulty(13)|head_armor(6)|body_armor(32)|leg_armor(6), imodbits_armor, [], [fac.kingdom_4]],
    ["nordic_noble_armor_2", "Hoursecarl Elite Armor", [("bwl_gambeson_and_leather", 0)], itp_type_body_armor|itp_covers_legs, 0, 3320, abundance(20)|weight(23.00)|difficulty(14)|head_armor(8)|body_armor(37)|leg_armor(6), imodbits_armor, [], [fac.kingdom_4]],
    ["nordic_noble_armor_3", "Thane Armor", [("bwl_einherjar1", 0)], itp_type_body_armor|itp_covers_legs, 0, 4540, abundance(10)|weight(25.00)|difficulty(15)|head_armor(10)|body_armor(43)|leg_armor(7), imodbits_armor, [], [fac.kingdom_4]],
    ["elite_plate_nordic", "Nord War Trophy Plate", [("pellagus_full_plate_nord", 0)], itp_type_body_armor|itp_covers_legs, 0, 7550, abundance(5)|weight(44.00)|difficulty(19)|head_armor(12)|body_armor(56)|leg_armor(14), imodbits_armor, [], [fac.kingdom_4]],
    ["nordic_armor_lord_a", "Jarl Battle Armor", [("dejawolf_vikingbyrnie", 0)], itp_type_body_armor|itp_covers_legs, 0, 5100, abundance(5)|weight(24.00)|difficulty(14)|head_armor(8)|body_armor(48)|leg_armor(8), imodbits_armor, [], [fac.kingdom_4]],
    ["nordic_armor_lord_b", "Favored Jarl Armor", [("ssh_nord_coat_of_plates", 0)], itp_type_body_armor|itp_covers_legs, 0, 6940, abundance(0)|weight(25.00)|difficulty(14)|head_armor(12)|body_armor(54)|leg_armor(10), imodbits_armor, [], [fac.kingdom_4]],
    ["nordic_armor_royal", "Ragnar's Coat of Plates", [("ssh_nord_coat_of_plates_pelt", 0)], itp_type_body_armor|itp_unique|itp_covers_legs, 0, 8550, abundance(0)|weight(26.50)|difficulty(14)|head_armor(15)|body_armor(58)|leg_armor(14), imodbits_none, [], [fac.kingdom_4]],

    # Rhodok armors
    ["rhodok_archer_armor_a1", "Rhodok Leather", [("pino_banded_leather_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1290, abundance(100)|weight(17.50)|difficulty(11)|head_armor(2)|body_armor(28)|leg_armor(4), imodbits_armor, [], [fac.kingdom_5]],
    ["rhodok_archer_armor_a2", "Rhodok Leather", [("pino_banded_leather_c", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1290, abundance(100)|weight(17.50)|difficulty(11)|head_armor(2)|body_armor(28)|leg_armor(4), imodbits_armor, [], [fac.kingdom_5]],
    ["rhodok_brigandine_vest", "Rhodok Brigandine Vest", [("wei_xiadi_rod_brigandine", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1400, abundance(90)|weight(14.50)|difficulty(11)|head_armor(2)|body_armor(30)|leg_armor(2), imodbits_armor, [], [fac.kingdom_5]],
    ["rhodok_archer_armor_b1", "Rhodok Studded Leather", [("pino_banded_leather_b_spiked", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1690, abundance(95)|weight(17.50)|difficulty(12)|head_armor(2)|body_armor(32)|leg_armor(6), imodbits_armor, [], [fac.kingdom_5]],
    ["rhodok_archer_armor_b2", "Rhodok Studded Leather", [("pino_banded_leather_c_spiked", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1690, abundance(95)|weight(17.50)|difficulty(12)|head_armor(2)|body_armor(32)|leg_armor(6), imodbits_armor, [], [fac.kingdom_5]],
    ["brigandine_red", "Rhodok Brigandine (Red)", [("brigandine_b", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2210, abundance(80)|weight(19.00)|difficulty(13)|head_armor(2)|body_armor(38)|leg_armor(4), imodbits_armor, [], [fac.kingdom_5]],
    ["brigandine_blue", "Rhodok Brigandine (Blue)", [("bar_brigandine_blue", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2210, abundance(80)|weight(19.00)|difficulty(13)|head_armor(2)|body_armor(38)|leg_armor(4), imodbits_armor, [], [fac.kingdom_5]],
    ["brigandine_green", "Rhodok Brigandine (Green)", [("bar_brigandine_green", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2210, abundance(80)|weight(19.00)|difficulty(13)|head_armor(2)|body_armor(38)|leg_armor(4), imodbits_armor, [], [fac.kingdom_5]],
    ["rhodok_archer_armor_c1", "Rhodok Mail Leather", [("pino_banded_leather_a_mailed", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2580, abundance(70)|weight(17.50)|difficulty(14)|head_armor(4)|body_armor(39)|leg_armor(4), imodbits_armor, [], [fac.kingdom_5]],
    ["rhodok_archer_armor_c2", "Rhodok Mail Leather", [("pino_banded_leather_c_mailed", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2580, abundance(70)|weight(17.50)|difficulty(14)|head_armor(4)|body_armor(39)|leg_armor(4), imodbits_armor, [], [fac.kingdom_5]],
    ["rhodok_cuirass_a1", "Rhodok Cuirass", [("bar_cuirass_on_black", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3440, abundance(90)|weight(29.00)|difficulty(13)|head_armor(6)|body_armor(47)|leg_armor(4), imodbits_armor, [], [fac.kingdom_5]],
    ["rhodok_cuirass_a2", "Rhodok Cuirass", [("bar_cuirass_on_red", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3440, abundance(90)|weight(29.00)|difficulty(13)|head_armor(6)|body_armor(47)|leg_armor(4), imodbits_armor, [], [fac.kingdom_5]],
    ["rhodok_cuirass_b", "Rhodok Plated Cuirass", [("narf_churburg_13", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 5110, abundance(65)|weight(33.00)|difficulty(15)|head_armor(10)|body_armor(51)|leg_armor(10), imodbits_armor, [], [fac.kingdom_5]],
    ["rhodok_plated_brig_1", "Elite Brigandine", [("hg_new_plate_brig", 0)], itp_type_body_armor|itp_covers_legs, 0, 3150, abundance(40)|weight(19.00)|difficulty(13)|head_armor(2)|body_armor(41)|leg_armor(10), imodbits_armor, [], [fac.kingdom_5]],
    ["rhodok_plated_brig_2", "Elite Brigandine", [("hg_new_plate_halfbrig", 0)], itp_type_body_armor|itp_covers_legs, 0, 3150, abundance(40)|weight(19.00)|difficulty(13)|head_armor(2)|body_armor(41)|leg_armor(10), imodbits_armor, [], [fac.kingdom_5]],
    ["rhodok_corrazine_a", "Corrazine", [("narf_corrazina_green", 0)], itp_type_body_armor|itp_covers_legs, 0, 4970, abundance(15)|weight(23.00)|difficulty(14)|head_armor(8)|body_armor(48)|leg_armor(8), imodbits_armor, [], [fac.kingdom_5]],
    ["rhodok_corrazine_b", "Corrazine", [("narf_corrazina_grey", 0)], itp_type_body_armor|itp_covers_legs, 0, 4970, abundance(15)|weight(23.00)|difficulty(14)|head_armor(8)|body_armor(48)|leg_armor(8), imodbits_armor, [], [fac.kingdom_5]],
    ["rhodok_corrazine_c", "Corrazine", [("narf_corrazina_red", 0)], itp_type_body_armor|itp_covers_legs, 0, 4970, abundance(15)|weight(23.00)|difficulty(14)|head_armor(8)|body_armor(48)|leg_armor(8), imodbits_armor, [], [fac.kingdom_5]],
    ["rhodok_cuirass_c", "Decorated Cuirass", [("narf_churburg_13_brass", 0)], itp_type_body_armor|itp_covers_legs, 0, 5800, abundance(30)|weight(34.00)|difficulty(16)|head_armor(10)|body_armor(52)|leg_armor(10), imodbits_armor, [], [fac.kingdom_5]],
    ["rhodok_cuirass_d", "Elite Cuirass", [("narf_churburg_13_mail", 0)], itp_type_body_armor|itp_covers_legs, 0, 7620, abundance(10)|weight(42.00)|difficulty(18)|head_armor(12)|body_armor(58)|leg_armor(12), imodbits_armor, [], [fac.kingdom_5]],
    ["rhodok_armor_royal", "Graveth's Full Armor", [("cow7488_maximilian_armour", 0)], itp_type_body_armor|itp_unique|itp_covers_legs, 0, 8930, abundance(0)|weight(45.00)|difficulty(20)|head_armor(14)|body_armor(62)|leg_armor(12), imodbits_none, [], [fac.kingdom_5]],

    # Sarranid armors
    ["skirmisher_armor", "Sarranid Skirmisher Armor", [("skirmisher_armor", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 490, abundance(100)|weight(8.50)|difficulty(0)|head_armor(3)|body_armor(15)|leg_armor(1), imodbits_armor, [], [fac.kingdom_6]],
    ["archers_vest", "Sarranid Archer Vest", [("archers_vest", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 690, abundance(100)|weight(8.00)|difficulty(0)|head_armor(3)|body_armor(19)|leg_armor(1), imodbits_armor, [], [fac.kingdom_6]],
    ["archers_vest_b", "Sarranid Archer Vest", [("pellagus_archers_vest_p1", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 690, abundance(100)|weight(8.00)|difficulty(0)|head_armor(3)|body_armor(19)|leg_armor(1), imodbits_armor, [], [fac.kingdom_6]],
    ["archers_vest_c", "Sarranid Archer Vest", [("pellagus_archers_vest_p2", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 690, abundance(100)|weight(8.00)|difficulty(0)|head_armor(3)|body_armor(19)|leg_armor(1), imodbits_armor, [], [fac.kingdom_6]],
    ["archers_vest_d", "Sarranid Archer Vest", [("pellagus_archers_vest_p3", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 690, abundance(100)|weight(8.00)|difficulty(0)|head_armor(3)|body_armor(19)|leg_armor(1), imodbits_armor, [], [fac.kingdom_6]],
    ["sarranid_leather_vest", "Sarranid Leather Vest", [("pino_arab_padded_leather_3", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1290, abundance(100)|weight(13.00)|difficulty(9)|head_armor(6)|body_armor(24)|leg_armor(4), imodbits_armor, [], [fac.kingdom_6]],
    ["sarranid_leather_armor", "Sarranid Leather Armor", [("sarranid_leather_armor", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1360, abundance(100)|weight(14.00)|difficulty(0)|head_armor(4)|body_armor(26)|leg_armor(6), imodbits_armor, [], [fac.kingdom_6]],
    ["sarranid_chain", "Sarranid Army Mail", [("sonyer_saracenmailssss", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1360, abundance(100)|weight(22.00)|difficulty(11)|head_armor(2)|body_armor(28)|leg_armor(6), imodbits_armor, [], [fac.kingdom_6]],
    ["sarranid_cavalry_robe", "Sarranid Warrior Mail", [("arabian_armor_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2120, abundance(80)|weight(18.50)|difficulty(0)|head_armor(2)|body_armor(37)|leg_armor(4), imodbits_armor, [], [fac.kingdom_6]],
    ["sarranid_cavalry_robe_b", "Sarranid Warrior Mail", [("pellagus_arabian_armor_p1", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2120, abundance(80)|weight(18.50)|difficulty(0)|head_armor(2)|body_armor(37)|leg_armor(4), imodbits_armor, [], [fac.kingdom_6]],
    ["sarranid_cavalry_robe_c", "Sarranid Warrior Mail", [("pellagus_arabian_armor_p2", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2120, abundance(80)|weight(18.50)|difficulty(0)|head_armor(2)|body_armor(37)|leg_armor(4), imodbits_armor, [], [fac.kingdom_6]],
    ["sarranid_warrior_mail_b", "Sarranid Warrior Mail", [("wei_xiadi_sarranid_mamluk_robes", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2120, abundance(80)|weight(18.50)|difficulty(0)|head_armor(2)|body_armor(37)|leg_armor(4), imodbits_armor, [], [fac.kingdom_6]],
    ["sarranid_elite_armor", "Sarranid Elite Armor", [("tunic_armor_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 4120, abundance(40)|weight(30.00)|difficulty(14)|head_armor(10)|body_armor(42)|leg_armor(8), imodbits_armor, [], [fac.kingdom_6]],
    ["sarranid_eunuch_armor_a", "Eunuch Mail", [("pino_arab_mail_grn", 0)], itp_type_body_armor|itp_covers_legs, 0, 2880, abundance(45)|weight(21.00)|difficulty(13)|head_armor(2)|body_armor(41)|leg_armor(6), imodbits_armor, [], [fac.kingdom_6]],
    ["sarranid_eunuch_armor_b", "Eunuch Mail", [("pino_arab_mail_red", 0)], itp_type_body_armor|itp_covers_legs, 0, 2880, abundance(45)|weight(21.00)|difficulty(13)|head_armor(2)|body_armor(41)|leg_armor(6), imodbits_armor, [], [fac.kingdom_6]],
    ["sarranid_mail_shirt", "Sarranid Noble Mail", [("sarranian_mail_shirt", 0)], itp_type_body_armor|itp_covers_legs, 0, 3350, abundance(30)|weight(24.00)|difficulty(12)|head_armor(4)|body_armor(41)|leg_armor(8), imodbits_armor, [], [fac.kingdom_6]],
    ["sarranid_mail_shirt_b", "Sarranid Noble Mail", [("pellagus_sarranian_mail_shirt_p1", 0)], itp_type_body_armor|itp_covers_legs, 0, 3350, abundance(30)|weight(24.00)|difficulty(12)|head_armor(4)|body_armor(41)|leg_armor(8), imodbits_armor, [], [fac.kingdom_6]],
    ["sarranid_mail_shirt_c", "Sarranid Noble Mail", [("pellagus_sarranian_mail_shirt_p2", 0)], itp_type_body_armor|itp_covers_legs, 0, 3350, abundance(30)|weight(24.00)|difficulty(12)|head_armor(4)|body_armor(41)|leg_armor(8), imodbits_armor, [], [fac.kingdom_6]],
    ["sarranid_mamluke_a", "Mamluke Mail", [("pino_arab_mail_plate_1", 0)], itp_type_body_armor|itp_covers_legs, 0, 3890, abundance(20)|weight(24.00)|difficulty(15)|head_armor(2)|body_armor(47)|leg_armor(7), imodbits_armor, [], [fac.kingdom_6]],
    ["sarranid_mamluke_b", "Mamluke Mail", [("pino_arab_mail_plate_2", 0)], itp_type_body_armor|itp_covers_legs, 0, 3890, abundance(20)|weight(24.00)|difficulty(15)|head_armor(2)|body_armor(47)|leg_armor(7), imodbits_armor, [], [fac.kingdom_6]],
    ["khergit_elite_armor", "Ghazi Armor", [("lamellar_armor_d", 0)], itp_type_body_armor|itp_covers_legs, 0, 5050, abundance(20)|weight(25.00)|difficulty(14)|head_armor(10)|body_armor(45)|leg_armor(12), imodbits_armor, [], [fac.kingdom_6]],
    ["vaegir_elite_armor", "Spahbot Armor", [("lamellar_armor_c", 0)], itp_type_body_armor|itp_covers_legs, 0, 6600, abundance(10)|weight(31.00)|difficulty(16)|head_armor(12)|body_armor(50)|leg_armor(16), imodbits_armor, [], [fac.kingdom_6]],
    ["mamluke_mail", "Mamluke Armor", [("sarranid_elite_cavalary", 0)], itp_type_body_armor|itp_covers_legs, 0, 6940, abundance(10)|weight(34.00)|difficulty(17)|head_armor(10)|body_armor(56)|leg_armor(12), imodbits_armor, [], [fac.kingdom_6]],
    ["sarranid_armor_royal", "Hakim's Royal Armor", [("njunja_saladin", 0)], itp_type_body_armor|itp_unique|itp_covers_legs, 0, 9710, abundance(0)|weight(37.00)|difficulty(18)|head_armor(14)|body_armor(64)|leg_armor(16), imodbits_none, [], [fac.kingdom_6]],

    # Dark Knight armors
    ["dk_armor_a", "Dark Knight Mail Shirt", [("wei_xiadi_swa_mail_and_plate_black", 0)], itp_type_body_armor|itp_civilian|itp_covers_legs, 0, 3290, abundance(50)|weight(27.00)|difficulty(10)|head_armor(4)|body_armor(42)|leg_armor(8), imodbits_armor, [], [fac.dark_knights]],
    ["dk_armor_b", "Dark Knight Plate Armor", [("pellagus_dk_full_plate", 0)], itp_type_body_armor|itp_civilian|itp_covers_legs, 0, 6740, abundance(30)|weight(35.00)|difficulty(14)|head_armor(10)|body_armor(56)|leg_armor(14), imodbits_armor, [], [fac.dark_knights]],
    ["dk_armor_c", "Dark Knight Heavy Plate", [("pellagus_dk_full_plate_2", 0)], itp_type_body_armor|itp_civilian|itp_covers_legs, 0, 7910, abundance(30)|weight(38.00)|difficulty(15)|head_armor(12)|body_armor(60)|leg_armor(16), imodbits_armor, [], [fac.dark_knights]],
    ["dk_armor_lord", "Dark Knight Full Armor", [("cow7488_maximilian_armour_1", 0)], itp_type_body_armor|itp_civilian|itp_covers_legs, 0, 10720, abundance(0)|weight(45.00)|difficulty(18)|head_armor(16)|body_armor(66)|leg_armor(18), imodbits_armor, [], [fac.dark_knights]],
    ["larktin_black_armor", "Lady Larktin's Armor", [("spak_twiligh_armor", 0)], itp_type_body_armor|itp_unique|itp_civilian|itp_covers_legs, 0, 14230, abundance(0)|weight(50.00)|difficulty(20)|head_armor(20)|body_armor(75)|leg_armor(24), imodbits_armor, [], [fac.dark_knights]],

    # Non-kingdom faction armors
    ["raider_hauberk_a", "Sea Raider Hauberk", [("bwl_raider_hauberk", 0)], itp_type_body_armor|itp_covers_legs, 0, 1320, abundance(150)|weight(21.00)|difficulty(12)|head_armor(3)|body_armor(30)|leg_armor(6), imodbits_armor, [], [fac.outlaws]],
    ["raider_hauberk_b", "Sea Raider Hauberk", [("bwl_raider_hauberk2", 0)], itp_type_body_armor|itp_covers_legs, 0, 1320, abundance(150)|weight(21.00)|difficulty(12)|head_armor(3)|body_armor(30)|leg_armor(6), imodbits_armor, [], [fac.outlaws]],
    ["raider_hauberk_c", "Sea Raider Hauberk", [("bwl_raider_hauberk3", 0)], itp_type_body_armor|itp_covers_legs, 0, 1320, abundance(150)|weight(21.00)|difficulty(12)|head_armor(3)|body_armor(30)|leg_armor(6), imodbits_armor, [], [fac.outlaws]],

    ["armors_end", "{!}endmarker", [("invalid_item", 0)], itp_type_goods, 0, 0, weight(1), imodbits_none], 

########################################################################################################################
# RANGED WEAPONS AND AMMO
########################################################################################################################

    ["ranged_begin", "{!}marker", [("invalid_item", 0)], itp_type_goods, 0, 0, weight(1), imodbits_none], 

    # Thrown weapons
    ["stones", "Throwing Stones", [("throwing_stone", 0)], itp_type_thrown|itp_primary, itcf_throw_stone, 1, abundance(100)|weight(4.00)|difficulty(0)|spd_rtng(97)|accuracy(85)|shoot_speed(30)|thrust_damage(11, blunt)|max_ammo(18), imodbits_none, [], []],
    ["throwing_knives", "Throwing Knives", [("throwing_knife", 0)], itp_type_thrown|itp_primary|itp_merchandise, itcf_throw_knife|itcf_carry_dagger_front_right, 130, abundance(100)|weight(3.00)|difficulty(0)|spd_rtng(120)|accuracy(90)|shoot_speed(36)|thrust_damage(18, cut)|max_ammo(32), imodbits_ranged, [], []],
    ["throwing_daggers", "Throwing Daggers", [("throwing_dagger", 0)], itp_type_thrown|itp_primary|itp_merchandise, itcf_throw_knife|itcf_carry_dagger_front_right, 250, abundance(90)|weight(5.00)|difficulty(0)|spd_rtng(110)|accuracy(90)|shoot_speed(32)|thrust_damage(24, cut)|max_ammo(28), imodbits_ranged, [], []],
    ["darts", "Darts", [("dart_b", 0), ("dart_b_bag", ixmesh_carry)], itp_type_thrown|itp_primary|itp_merchandise|itp_next_item_as_melee, itcf_throw_javelin|itcf_carry_quiver_right_vertical|itcf_show_holster_when_drawn, 110, abundance(90)|weight(3.50)|difficulty(0)|spd_rtng(90)|accuracy(95)|shoot_speed(24)|thrust_damage(20, pierce)|max_ammo(14)|weapon_length(32), imodbits_ranged, [], []],
    ["darts_alt","Darts",[("dart_b",0),("dart_b_bag",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_wooden_parry,itc_stiletto|itcf_carry_quiver_right_vertical|itcf_show_holster_when_drawn,110,abundance(90)|weight(3.50)|difficulty(0)|spd_rtng(90)|weapon_length(30)|thrust_damage(10,pierce),imodbits_ranged,[],[]],
    ["war_darts", "War Darts", [("dart_a", 0), ("dart_a_bag", ixmesh_carry)], itp_type_thrown|itp_primary|itp_merchandise|itp_next_item_as_melee, itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 270, abundance(80)|weight(5.00)|difficulty(1)|spd_rtng(95)|accuracy(100)|shoot_speed(27)|thrust_damage(26, pierce)|max_ammo(20)|weapon_length(45), imodbits_ranged, [], []],
    ["war_darts_alt","War Darts",[("dart_a",0),("dart_a_bag",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_wooden_parry,itc_stiletto|itcf_carry_quiver_back|itcf_show_holster_when_drawn,270,abundance(80)|weight(5.00)|difficulty(0)|spd_rtng(95)|weapon_length(45)|thrust_damage(13,pierce),imodbits_ranged,[],[]],
    ["javelin", "Javelins", [("javelin", 0), ("javelins_quiver", ixmesh_carry)], itp_type_thrown|itp_primary|itp_merchandise|itp_next_item_as_melee, itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 420, abundance(70)|weight(6.00)|difficulty(2)|spd_rtng(95)|accuracy(100)|shoot_speed(27)|thrust_damage(30, pierce)|max_ammo(16)|weapon_length(75), imodbits_ranged, [], []],
    ["javelin_alt","Javelins",[("javelin",0),("javelins_quiver",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_wooden_parry,itc_stiletto|itcf_carry_quiver_back|itcf_show_holster_when_drawn,420,abundance(70)|weight(6.00)|difficulty(0)|spd_rtng(95)|weapon_length(77)|thrust_damage(15,pierce),imodbits_ranged,[],[]],
    ["javelin_khe", "Khergit Javelins", [("javelin", 0), ("akosmo_javelins_quiver", ixmesh_carry)], itp_type_thrown|itp_primary|itp_merchandise|itp_next_item_as_melee, itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 620, abundance(50)|weight(6.50)|difficulty(3)|spd_rtng(100)|accuracy(100)|shoot_speed(31)|thrust_damage(31, pierce)|max_ammo(18)|weapon_length(75), imodbits_ranged, [], [fac.kingdom_3]],
    ["javelin_khe_alt","Khergit Javelins",[("javelin",0),("akosmo_javelins_quiver",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_wooden_parry,itc_stiletto|itcf_carry_quiver_back|itcf_show_holster_when_drawn,620,abundance(50)|weight(6.50)|difficulty(0)|spd_rtng(100)|weapon_length(77)|thrust_damage(16,pierce),imodbits_ranged,[],[]],
    ["javelin_vae", "Vaegir Javelins", [("javelin", 0), ("javelins_quiver_new", ixmesh_carry)], itp_type_thrown|itp_primary|itp_merchandise|itp_next_item_as_melee, itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 580, abundance(60)|weight(6.00)|difficulty(3)|spd_rtng(90)|accuracy(100)|shoot_speed(26)|thrust_damage(34, pierce)|max_ammo(14)|weapon_length(75), imodbits_ranged, [], [fac.kingdom_2]],
    ["javelin_vae_alt","Vaegir Javelins",[("javelin",0),("javelins_quiver_new",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_wooden_parry,itc_stiletto|itcf_carry_quiver_back|itcf_show_holster_when_drawn,580,abundance(60)|weight(6.00)|difficulty(0)|spd_rtng(90)|weapon_length(77)|thrust_damage(17,pierce),imodbits_ranged,[],[]],
    ["javelin_sar", "Sarranid Javelins", [("javelin", 0), ("akosmo_javelins_quiver_new", ixmesh_carry)], itp_type_thrown|itp_primary|itp_merchandise|itp_next_item_as_melee, itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 420, abundance(80)|weight(5.50)|difficulty(3)|spd_rtng(105)|accuracy(100)|shoot_speed(30)|thrust_damage(29, pierce)|max_ammo(16)|weapon_length(75), imodbits_ranged, [], [fac.kingdom_6]],
    ["javelin_sar_alt","Sarranid Javelins",[("javelin",0),("akosmo_javelins_quiver_new",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_wooden_parry,itc_stiletto|itcf_carry_quiver_back|itcf_show_holster_when_drawn,420,abundance(80)|weight(5.50)|difficulty(0)|spd_rtng(105)|weapon_length(77)|thrust_damage(14,pierce),imodbits_ranged,[],[]],
    ["jarid", "Jarids", [("jarid_new", 0), ("jarid_quiver", ixmesh_carry)], itp_type_thrown|itp_primary|itp_merchandise|itp_next_item_as_melee|itp_extra_penetration, itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 690, abundance(50)|weight(7.50)|difficulty(3)|spd_rtng(90)|accuracy(100)|shoot_speed(25)|thrust_damage(36, pierce)|max_ammo(15)|weapon_length(65), imodbits_ranged, [], []],
    ["jarid_alt","Jarids",[("jarid_new",0),("jarid_quiver",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_wooden_parry,itc_stiletto|itcf_carry_quiver_back|itcf_show_holster_when_drawn,690,abundance(50)|weight(7.50)|difficulty(0)|spd_rtng(90)|weapon_length(80)|thrust_damage(18,pierce),imodbits_ranged,[],[]],
    ["jarid_sar", "Sarranid Jarids", [("jarid_new", 0), ("akosmo_jarid_quiver", ixmesh_carry)], itp_type_thrown|itp_primary|itp_merchandise|itp_next_item_as_melee|itp_extra_penetration, itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 760, abundance(50)|weight(8.00)|difficulty(4)|spd_rtng(100)|accuracy(100)|shoot_speed(28)|thrust_damage(35, pierce)|max_ammo(16)|weapon_length(65), imodbits_ranged, [], [fac.kingdom_6]],
    ["jarid_sar_alt","Sarranid Jarids",[("jarid_new",0),("akosmo_jarid_quiver",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_wooden_parry,itc_stiletto|itcf_carry_quiver_back|itcf_show_holster_when_drawn,760,abundance(50)|weight(8.00)|difficulty(0)|spd_rtng(100)|weapon_length(80)|thrust_damage(17,pierce),imodbits_ranged,[],[]],
    ["throwing_spears", "Battle Jarids", [("jarid_new_b", 0), ("jarid_new_b_bag", ixmesh_carry)], itp_type_thrown|itp_primary|itp_merchandise|itp_next_item_as_melee|itp_extra_penetration, itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 1110, abundance(40)|weight(8.00)|difficulty(4)|spd_rtng(90)|accuracy(100)|shoot_speed(29)|thrust_damage(40, pierce)|max_ammo(16)|weapon_length(65), imodbits_ranged, [], [fac.kingdom_3]],
    ["throwing_spears_alt","Battle Jarids",[("jarid_new_b",0),("jarid_new_b_bag",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_extra_penetration|itp_wooden_parry,itc_stiletto|itcf_carry_quiver_back|itcf_show_holster_when_drawn,1110,abundance(40)|weight(8.00)|difficulty(0)|spd_rtng(90)|weapon_length(80)|thrust_damage(20,pierce),imodbits_ranged,[],[]],
    ["throwing_spears_b", "Khergit Jarids", [("jarid_new_b", 0), ("akosmo_jarid_new_b_bag", ixmesh_carry)], itp_type_thrown|itp_primary|itp_merchandise|itp_next_item_as_melee|itp_extra_penetration, itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 1690, abundance(30)|weight(8.00)|difficulty(5)|spd_rtng(95)|accuracy(100)|shoot_speed(30)|thrust_damage(45, pierce)|max_ammo(14)|weapon_length(65), imodbits_ranged, [], [fac.kingdom_3]],
    ["throwing_spears_b_alt","Khergit Jarids",[("jarid_new_b",0),("akosmo_jarid_new_b_bag",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_extra_penetration|itp_wooden_parry,itc_stiletto|itcf_carry_quiver_back|itcf_show_holster_when_drawn,1690,abundance(30)|weight(8.00)|difficulty(0)|spd_rtng(95)|weapon_length(80)|thrust_damage(22,pierce),imodbits_ranged,[],[]],
    ["light_throwing_axes", "Franciscas", [("francisca", 0)], itp_type_thrown|itp_primary|itp_merchandise|itp_next_item_as_melee|itp_bonus_against_shield, itcf_throw_axe|itcf_carry_axe_left_hip, 440, abundance(80)|weight(6.00)|difficulty(2)|spd_rtng(100)|accuracy(90)|shoot_speed(20)|thrust_damage(36, cut)|max_ammo(16)|weapon_length(53), imodbits_ranged, [], []],
    ["light_throwing_axes_alt","Franciscas",[("francisca",0)],itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield|itp_wooden_parry,itc_sabre_1h|itcf_carry_axe_left_hip,440,abundance(80)|weight(6.00)|difficulty(0)|spd_rtng(100)|weapon_length(55)|swing_damage(24,cut),imodbits_ranged,[],[]],
    ["throwing_axes", "Throwing Axes", [("throwing_axe_a", 0)], itp_type_thrown|itp_primary|itp_merchandise|itp_next_item_as_melee|itp_bonus_against_shield, itcf_throw_axe|itcf_carry_axe_left_hip, 860, abundance(60)|weight(7.00)|difficulty(3)|spd_rtng(90)|accuracy(90)|shoot_speed(19)|thrust_damage(46, cut)|max_ammo(14)|weapon_length(53), imodbits_ranged, [], []],
    ["throwing_axes_alt","Throwing Axes",[("throwing_axe_a",0)],itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield|itp_wooden_parry,itc_sabre_1h|itcf_carry_axe_left_hip,860,abundance(60)|weight(7.00)|difficulty(0)|spd_rtng(90)|weapon_length(53)|swing_damage(29,cut),imodbits_ranged,[],[]],
    ["heavy_throwing_axes", "Nordic Throwing Axes", [("throwing_axe_b", 0)], itp_type_thrown|itp_primary|itp_merchandise|itp_next_item_as_melee|itp_bonus_against_shield, itcf_throw_axe|itcf_carry_axe_left_hip, 1500, abundance(40)|weight(6.50)|difficulty(4)|spd_rtng(80)|accuracy(95)|shoot_speed(22)|thrust_damage(52, cut)|max_ammo(12)|weapon_length(53), imodbits_ranged, [], [fac.kingdom_4]],
    ["heavy_throwing_axes_alt","Nordic Throwing Axes",[("throwing_axe_b",0)],itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield|itp_wooden_parry,itc_sabre_1h|itcf_carry_axe_left_hip,1500,abundance(40)|weight(6.50)|difficulty(0)|spd_rtng(80)|weapon_length(58)|swing_damage(34,cut),imodbits_ranged,[],[]],

    # Common bows
    ["hunting_bow", "Hunting Bow", [("lav_bow_common_hunting", 0), ("lav_bow_common_hunting_carry", ixmesh_carry)], itp_type_bow|itp_primary|itp_merchandise|itp_two_handed, itcf_shoot_bow|itcf_carry_bow_back, 130, abundance(100)|weight(1.00)|difficulty(0)|spd_rtng(90)|accuracy(95)|shoot_speed(50)|thrust_damage(14, cut), imodbits_ranged, [], []],
    ["short_bow", "Short Bow", [("lav_bow_common_short", 0), ("lav_bow_common_short_carry", ixmesh_carry)], itp_type_bow|itp_primary|itp_merchandise|itp_two_handed, itcf_shoot_bow|itcf_carry_bow_back, 220, abundance(100)|weight(1.50)|difficulty(1)|spd_rtng(85)|accuracy(95)|shoot_speed(50)|thrust_damage(17, cut), imodbits_ranged, [], []],
    ["nomad_bow", "Steppe Bow", [("lav_bow_common_steppe", 0), ("lav_bow_common_steppe_carry", ixmesh_carry)], itp_type_bow|itp_primary|itp_merchandise|itp_two_handed, itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 410, abundance(80)|weight(2.00)|difficulty(2)|spd_rtng(85)|accuracy(95)|shoot_speed(55)|thrust_damage(19, cut), imodbits_ranged, [], []],
    ["long_bow", "Long Bow", [("lav_bow_common_long", 0), ("lav_bow_common_long_carry", ixmesh_carry)], itp_type_bow|itp_primary|itp_merchandise|itp_two_handed|itp_cant_use_on_horseback, itcf_shoot_bow|itcf_carry_bow_back, 770, abundance(50)|weight(2.50)|difficulty(3)|spd_rtng(80)|accuracy(95)|shoot_speed(55)|thrust_damage(22, cut), imodbits_ranged, [], []],
    ["war_bow", "War Bow", [("lav_bow_common_war", 0), ("lav_bow_common_war_carry", ixmesh_carry)], itp_type_bow|itp_primary|itp_two_handed|itp_cant_use_on_horseback, itcf_shoot_bow|itcf_carry_bow_back, 1520, abundance(10)|weight(3.00)|difficulty(4)|spd_rtng(77)|accuracy(95)|shoot_speed(60)|thrust_damage(25, cut), imodbits_ranged, [], []],

    # Vaegir bows
    ["hunting_bow_vae", "Vaegir Hunting Bow", [("lav_bow_vae_hunting", 0), ("lav_bow_vae_hunting_carry", ixmesh_carry)], itp_type_bow|itp_primary|itp_merchandise|itp_two_handed, itcf_shoot_bow|itcf_carry_bow_back, 150, abundance(100)|weight(1.00)|difficulty(1)|spd_rtng(80)|accuracy(85)|shoot_speed(55)|thrust_damage(15, cut), imodbits_ranged, [], [fac.kingdom_2]],
    ["short_bow_vae", "Vaegir Short Bow", [("lav_bow_vae_short", 0), ("lav_bow_vae_short_carry", ixmesh_carry)], itp_type_bow|itp_primary|itp_merchandise|itp_two_handed, itcf_shoot_bow|itcf_carry_bow_back, 330, abundance(90)|weight(1.50)|difficulty(2)|spd_rtng(75)|accuracy(85)|shoot_speed(55)|thrust_damage(19, cut), imodbits_ranged, [], [fac.kingdom_2]],
    ["long_bow_vae", "Vaegir Long Bow", [("lav_bow_vae_long", 0), ("lav_bow_vae_long_carry", ixmesh_carry)], itp_type_bow|itp_primary|itp_merchandise|itp_two_handed|itp_cant_use_on_horseback, itcf_shoot_bow|itcf_carry_bow_back, 830, abundance(70)|weight(2.50)|difficulty(3)|spd_rtng(70)|accuracy(85)|shoot_speed(60)|thrust_damage(24, cut), imodbits_ranged, [], [fac.kingdom_2]],
    ["war_bow_vae", "Vaegir War Bow", [("lav_bow_vae_war", 0), ("lav_bow_vae_war_carry", ixmesh_carry)], itp_type_bow|itp_primary|itp_merchandise|itp_two_handed|itp_cant_use_on_horseback, itcf_shoot_bow|itcf_carry_bow_back, 1800, abundance(30)|weight(3.00)|difficulty(4)|spd_rtng(65)|accuracy(85)|shoot_speed(65)|thrust_damage(28, cut), imodbits_ranged, [], [fac.kingdom_2]],
    ["nomad_bow_ivory", "Ivory Horseman Bow", [("lav_bow_ivory_steppe", 0), ("lav_bow_ivory_steppe_carry", ixmesh_carry)], itp_type_bow|itp_primary|itp_two_handed, itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 1740, abundance(20)|weight(1.50)|difficulty(3)|spd_rtng(65)|accuracy(95)|shoot_speed(70)|thrust_damage(26, cut), imodbits_ranged, [], [fac.kingdom_2]],
    ["long_bow_ivory", "Ivory Long Bow", [("lav_bow_ivory_long", 0), ("lav_bow_ivory_long_carry", ixmesh_carry)], itp_type_bow|itp_primary|itp_two_handed|itp_cant_use_on_horseback, itcf_shoot_bow|itcf_carry_bow_back, 2550, abundance(10)|weight(2.00)|difficulty(4)|spd_rtng(65)|accuracy(95)|shoot_speed(70)|thrust_damage(29, cut), imodbits_ranged, [], [fac.kingdom_2]],
    ["war_bow_ivory", "Ivory War Bow", [("lav_bow_ivory_war", 0), ("lav_bow_ivory_war_carry", ixmesh_carry)], itp_type_bow|itp_primary|itp_two_handed|itp_cant_use_on_horseback, itcf_shoot_bow|itcf_carry_bow_back, 3460, abundance(5)|weight(2.50)|difficulty(5)|spd_rtng(55)|accuracy(95)|shoot_speed(75)|thrust_damage(32, cut), imodbits_ranged, [], [fac.kingdom_2]],
    ["vaegir_bow_royal", "Yaroglek's Ivory Bow", [("addonay_ivorybow", 0), ("addonay_ivorybow_carry", ixmesh_carry)], itp_type_bow|itp_primary|itp_unique|itp_two_handed, itcf_shoot_bow|itcf_carry_bow_back, 9080, abundance(0)|weight(2.00)|difficulty(6)|spd_rtng(60)|accuracy(100)|shoot_speed(85)|thrust_damage(41, cut), imodbits_none, [], [fac.kingdom_2]],

    # Khergit bows
    ["hunting_bow_khe", "Khergit Hunting Bow", [("lav_bow_khe_hunting", 0), ("lav_bow_khe_hunting_carry", ixmesh_carry)], itp_type_bow|itp_primary|itp_merchandise|itp_two_handed, itcf_shoot_bow|itcf_carry_bow_back, 130, abundance(80)|weight(1.00)|difficulty(0)|spd_rtng(95)|accuracy(90)|shoot_speed(55)|thrust_damage(13, cut), imodbits_ranged, [], [fac.kingdom_3]],
    ["short_bow_khe", "Khergit Short Bow", [("lav_bow_khe_short", 0), ("lav_bow_khe_short_carry", ixmesh_carry)], itp_type_bow|itp_primary|itp_merchandise|itp_two_handed, itcf_shoot_bow|itcf_carry_bow_back, 270, abundance(80)|weight(1.25)|difficulty(1)|spd_rtng(90)|accuracy(90)|shoot_speed(60)|thrust_damage(16, cut), imodbits_ranged, [], [fac.kingdom_3]],
    ["nomad_bow_khe", "Khergit Rider's Bow", [("lav_bow_khe_steppe", 0), ("lav_bow_khe_steppe_carry", ixmesh_carry)], itp_type_bow|itp_primary|itp_merchandise|itp_two_handed, itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 310, abundance(100)|weight(1.50)|difficulty(2)|spd_rtng(85)|accuracy(90)|shoot_speed(60)|thrust_damage(18, cut), imodbits_ranged, [], [fac.kingdom_3]],
    ["strong_bow_khe", "Khergit Strong Bow", [("lav_bow_khe_strong", 0), ("lav_bow_khe_strong_carry", ixmesh_carry)], itp_type_bow|itp_primary|itp_merchandise|itp_two_handed, itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 770, abundance(50)|weight(1.75)|difficulty(3)|spd_rtng(80)|accuracy(90)|shoot_speed(65)|thrust_damage(21, cut), imodbits_ranged, [], [fac.kingdom_3]],
    ["khergit_bow_khe", "Khergit Curved Bow", [("lav_bow_khe_curved", 0), ("lav_bow_khe_curved_carry", ixmesh_carry)], itp_type_bow|itp_primary|itp_merchandise|itp_two_handed, itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 1580, abundance(30)|weight(2.00)|difficulty(4)|spd_rtng(80)|accuracy(90)|shoot_speed(70)|thrust_damage(25, cut), imodbits_ranged, [], [fac.kingdom_3]],
    ["khergit_bow_royal", "Sanjar's Tulgan Bow", [("spak_lonely", 0), ("spak_lonely_carry", ixmesh_carry)], itp_type_bow|itp_primary|itp_unique|itp_two_handed, itcf_shoot_bow|itcf_carry_bow_back, 6770, abundance(0)|weight(1.50)|difficulty(4)|spd_rtng(110)|accuracy(85)|shoot_speed(75)|thrust_damage(36, cut), imodbits_none, [], [fac.kingdom_3]],

    # Nordic bows
    ["hunting_bow_nor", "Nordic Hunting Bow", [("lav_bow_nor_hunting", 0), ("lav_bow_nor_hunting_carry", ixmesh_carry)], itp_type_bow|itp_primary|itp_merchandise|itp_two_handed, itcf_shoot_bow|itcf_carry_bow_back, 120, abundance(100)|weight(1.00)|difficulty(0)|spd_rtng(90)|accuracy(100)|shoot_speed(45)|thrust_damage(14, cut), imodbits_ranged, [], [fac.kingdom_4]],
    ["short_bow_nor", "Nordic Short Bow", [("lav_bow_nor_short", 0), ("lav_bow_nor_short_carry", ixmesh_carry)], itp_type_bow|itp_primary|itp_merchandise|itp_two_handed, itcf_shoot_bow|itcf_carry_bow_back, 240, abundance(100)|weight(1.50)|difficulty(1)|spd_rtng(85)|accuracy(100)|shoot_speed(45)|thrust_damage(18, cut), imodbits_ranged, [], [fac.kingdom_4]],
    ["long_bow_nor", "Nordic Long Bow", [("lav_bow_nor_long", 0), ("lav_bow_nor_long_carry", ixmesh_carry)], itp_type_bow|itp_primary|itp_merchandise|itp_two_handed|itp_cant_use_on_horseback, itcf_shoot_bow|itcf_carry_bow_back, 620, abundance(70)|weight(2.25)|difficulty(2)|spd_rtng(80)|accuracy(100)|shoot_speed(50)|thrust_damage(22, cut), imodbits_ranged, [], [fac.kingdom_4]],

    # Sarranid bows
    ["hunting_bow_sar", "Sarranid Hunting Bow", [("lav_bow_sar_hunting", 0), ("lav_bow_sar_hunting_carry", ixmesh_carry)], itp_type_bow|itp_primary|itp_merchandise|itp_two_handed, itcf_shoot_bow|itcf_carry_bow_back, 130, abundance(100)|weight(1.00)|difficulty(0)|spd_rtng(105)|accuracy(80)|shoot_speed(50)|thrust_damage(14, cut), imodbits_ranged, [], [fac.kingdom_6]],
    ["short_bow_sar", "Sarranid Short Bow", [("lav_bow_sar_short", 0), ("lav_bow_sar_short_carry", ixmesh_carry)], itp_type_bow|itp_primary|itp_merchandise|itp_two_handed, itcf_shoot_bow|itcf_carry_bow_back, 240, abundance(90)|weight(1.50)|difficulty(1)|spd_rtng(100)|accuracy(80)|shoot_speed(50)|thrust_damage(17, cut), imodbits_ranged, [], [fac.kingdom_6]],
    ["nomad_bow_sar", "Sarranid Rider's Bow", [("lav_bow_sar_steppe", 0), ("lav_bow_sar_steppe_carry", ixmesh_carry)], itp_type_bow|itp_primary|itp_merchandise|itp_two_handed, itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 510, abundance(70)|weight(2.00)|difficulty(2)|spd_rtng(100)|accuracy(80)|shoot_speed(55)|thrust_damage(20, cut), imodbits_ranged, [], [fac.kingdom_6]],
    ["strong_bow_sar", "Sarranid Strong Bow", [("lav_bow_sar_strong", 0), ("lav_bow_sar_strong_carry", ixmesh_carry)], itp_type_bow|itp_primary|itp_merchandise|itp_two_handed, itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 930, abundance(40)|weight(2.50)|difficulty(3)|spd_rtng(95)|accuracy(80)|shoot_speed(55)|thrust_damage(23, cut), imodbits_ranged, [], [fac.kingdom_6]],

    # Common crossbows
    ["hunting_crossbow", "Hunting Crossbow", [("rathos_crossbow_b", 0)], itp_type_crossbow|itp_primary|itp_merchandise|itp_two_handed, itcf_shoot_crossbow|itcf_carry_crossbow_back, 160, abundance(100)|weight(3.00)|difficulty(0)|spd_rtng(50)|accuracy(90)|shoot_speed(75)|thrust_damage(40, pierce)|max_ammo(1), imodbits_ranged, [], []],
    ["light_crossbow", "Light Crossbow", [("rathos_crossbow_a", 0)], itp_type_crossbow|itp_primary|itp_merchandise|itp_two_handed, itcf_shoot_crossbow|itcf_carry_crossbow_back, 330, abundance(90)|weight(4.00)|difficulty(8)|spd_rtng(45)|accuracy(90)|shoot_speed(75)|thrust_damage(50, pierce)|max_ammo(1), imodbits_ranged, [], []],
    ["crossbow", "Infantry Crossbow", [("native_crossbow_b", 0)], itp_type_crossbow|itp_primary|itp_merchandise|itp_two_handed|itp_cant_reload_on_horseback, itcf_shoot_crossbow|itcf_carry_crossbow_back, 650, abundance(75)|weight(5.00)|difficulty(10)|spd_rtng(40)|accuracy(90)|shoot_speed(80)|thrust_damage(60, pierce)|max_ammo(1), imodbits_ranged, [], []],
    ["heavy_crossbow", "Heavy Crossbow", [("native_crossbow_a", 0)], itp_type_crossbow|itp_primary|itp_merchandise|itp_two_handed|itp_cant_reload_on_horseback, itcf_shoot_crossbow|itcf_carry_crossbow_back, 1230, abundance(50)|weight(6.00)|difficulty(12)|spd_rtng(35)|accuracy(90)|shoot_speed(85)|thrust_damage(70, pierce)|max_ammo(1), imodbits_ranged, [], []],
    ["sniper_crossbow", "Sniper Crossbow", [("native_crossbow_c", 0)], itp_type_crossbow|itp_primary|itp_two_handed|itp_cant_reload_on_horseback, itcf_shoot_crossbow|itcf_carry_crossbow_back, 2210, abundance(20)|weight(5.50)|difficulty(15)|spd_rtng(30)|accuracy(95)|shoot_speed(90)|thrust_damage(80, pierce)|max_ammo(1), imodbits_ranged, [], []],

    # Rhodok crossbows
    ["skirmisher_crossbow", "Skirmisher Crossbow", [("akosmo_crossbow_a", 0)], itp_type_crossbow|itp_primary|itp_merchandise|itp_two_handed, itcf_shoot_crossbow|itcf_carry_crossbow_back, 530, abundance(60)|weight(2.50)|difficulty(10)|spd_rtng(50)|accuracy(85)|shoot_speed(70)|thrust_damage(55, pierce)|max_ammo(1), imodbits_ranged, [], [fac.kingdom_5]],
    ["scout_crossbow", "Scout Crossbow", [("akosmo_crossbow_c", 0)], itp_type_crossbow|itp_primary|itp_merchandise|itp_two_handed, itcf_shoot_crossbow|itcf_carry_crossbow_back, 850, abundance(30)|weight(3.50)|difficulty(12)|spd_rtng(45)|accuracy(85)|shoot_speed(75)|thrust_damage(60, pierce)|max_ammo(1), imodbits_ranged, [], [fac.kingdom_5]],
    ["siege_crossbow", "Siege Crossbow", [("akosmo_crossbow_b", 0)], itp_type_crossbow|itp_primary|itp_two_handed|itp_cant_reload_on_horseback, itcf_shoot_crossbow|itcf_carry_crossbow_back, 4890, abundance(10)|weight(8.00)|difficulty(18)|spd_rtng(40)|accuracy(90)|shoot_speed(100)|thrust_damage(95, pierce)|max_ammo(1), imodbits_ranged, [], [fac.kingdom_5]],
    ["da_veidar", "Da Veidar Crossbow", [("pellagus_da_veidar", 0)], itp_type_crossbow|itp_primary|itp_unique|itp_two_handed, itcf_shoot_crossbow|itcf_carry_crossbow_back, 4770, abundance(0)|weight(6.50)|difficulty(11)|spd_rtng(50)|accuracy(95)|shoot_speed(95)|thrust_damage(90, pierce)|max_ammo(1), imodbits_none, [], [fac.kingdom_5]],

    ["ranged_end", "{!}endmarker", [("invalid_item", 0)], itp_type_goods, 0, 0, weight(1), imodbits_none], 

    ["ammo_begin", "{!}marker", [("invalid_item", 0)], itp_type_goods, 0, 0, weight(1), imodbits_none], 

    ["hunting_arrows", "Hunting Arrows", [("arrow", 0), ("quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise, 0, 120, abundance(100)|weight(4.00)|thrust_damage(1, cut)|max_ammo(40)|weapon_length(95), imodbits_ammo, [], []],
    ["arrows", "Arrows", [("akosmo_arrow", 0), ("akosmo_quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise, 0, 160, abundance(100)|weight(4.00)|thrust_damage(3, cut)|max_ammo(40)|weapon_length(95), imodbits_ammo, [], []],
    ["vaegir_arrows_a", "Vaegir War Arrows", [("spak_steel_arrow1", 0), ("spak_steel_arrow1_bag", ixmesh_carry)], itp_type_arrows|itp_merchandise, 0, 540, abundance(40)|weight(4.00)|thrust_damage(12, cut)|max_ammo(36)|weapon_length(95), imodbits_ammo, [], [fac.kingdom_2]],
    ["vaegir_arrows_b", "Vaegir Army Arrows", [("spak_steel_arrow3", 0), ("spak_steel_arrow3_bag", ixmesh_carry)], itp_type_arrows|itp_merchandise, 0, 290, abundance(90)|weight(4.00)|thrust_damage(8, cut)|max_ammo(40)|weapon_length(95), imodbits_ammo, [], [fac.kingdom_2]],
    ["piercing_arrows", "Piercing Arrows", [("arrow_b", 0), ("quiver_b", ixmesh_carry)], itp_type_arrows|itp_merchandise, 0, 260, abundance(80)|weight(4.00)|thrust_damage(6, cut)|max_ammo(40)|weapon_length(95), imodbits_ammo, [], []],
    ["sarranid_arrows", "Sarranid Piercing Arrows", [("akosmo_arrow_b", 0), ("akosmo_quiver_b", ixmesh_carry)], itp_type_arrows|itp_merchandise, 0, 290, abundance(90)|weight(4.00)|thrust_damage(8, cut)|max_ammo(40)|weapon_length(95), imodbits_ammo, [], [fac.kingdom_6]],
    ["barbed_arrows", "Ranger Arrows", [("spak_ar", 0), ("spak_ar_bag", ixmesh_carry)], itp_type_arrows|itp_merchandise, 0, 480, abundance(40)|weight(4.00)|thrust_damage(10, cut)|max_ammo(32)|weapon_length(95), imodbits_ammo, [], []],
    ["broadhead_arrows", "Broadhead Arrows", [("barbed_arrow", 0), ("quiver_d", ixmesh_carry)], itp_type_arrows|itp_merchandise, 0, 200, abundance(90)|weight(4.00)|thrust_damage(4, cut)|max_ammo(40)|weapon_length(95), imodbits_ammo, [], []],
    ["khergit_arrows_a", "Khergit Hunting Arrows", [("akosmo_barbed_arrow", 0), ("akosmo_quiver_d", ixmesh_carry)], itp_type_arrows|itp_merchandise, 0, 390, abundance(60)|weight(4.00)|thrust_damage(9, cut)|max_ammo(40)|weapon_length(95), imodbits_ammo, [], [fac.kingdom_3]],
    ["bodkin_arrows", "Bodkin Arrows", [("piercing_arrow", 0), ("quiver_c", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_can_penetrate_shield, 0, 480, abundance(50)|weight(4.00)|thrust_damage(11, cut)|max_ammo(34)|weapon_length(95), imodbits_ammo, [], []],
    ["khergit_arrows_b", "Khergit Arrows", [("akosmo_piercing_arrow", 0), ("akosmo_quiver_c", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_can_penetrate_shield, 0, 540, abundance(40)|weight(4.00)|thrust_damage(12, cut)|max_ammo(34)|weapon_length(95), imodbits_ammo, [], [fac.kingdom_3]],
    ["khergit_arrows_c", "Khergit Noble Arrows", [("spak_amazon_arrow", 0), ("spak_amazon_arrow_bag", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_can_penetrate_shield, 0, 760, abundance(10)|weight(4.00)|thrust_damage(15, cut)|max_ammo(34)|weapon_length(95), imodbits_ammo, [], [fac.kingdom_3]],
    ["ivory_arrows", "Ivory Arrows", [("spak_new1_arrow", 0), ("spak_new1_arrow_bag", ixmesh_carry)], itp_type_arrows|itp_extra_penetration, 0, 1000, abundance(1)|weight(4.00)|thrust_damage(20, cut)|max_ammo(30)|weapon_length(95), imodbits_ammo, [], [fac.kingdom_2]],
    ["vaegir_arrows_royal", "Yaroglek's Arrows", [("spak_arrow", 0), ("spak_arrow_bag", ixmesh_carry)], itp_type_arrows|itp_unique|itp_can_knock_down, 0, 920, abundance(0)|weight(4.00)|thrust_damage(18, cut)|max_ammo(40)|weapon_length(95), imodbits_ammo, [], [fac.kingdom_2]],

    ["bolts", "Wooden Bolts", [("bolt", 0), ("bolt_bag", ixmesh_carry)], itp_type_bolts|itp_merchandise|itp_can_penetrate_shield, 0, 100, abundance(100)|weight(3.00)|thrust_damage(0, pierce)|max_ammo(35)|weapon_length(55), imodbits_ammo, [], []],
    ["piercing_bolts", "Piercing Bolts", [("bolt", 0), ("bolt_bag_b", ixmesh_carry)], itp_type_bolts|itp_merchandise|itp_can_penetrate_shield, 0, 310, abundance(80)|weight(3.00)|thrust_damage(8, pierce)|max_ammo(35)|weapon_length(55), imodbits_ammo, [], []],
    ["hunting_bolts", "Hunting Bolts", [("bolt", 0), ("bolt_bag_c", ixmesh_carry)], itp_type_bolts|itp_merchandise|itp_can_penetrate_shield, 0, 180, abundance(100)|weight(3.00)|thrust_damage(4, pierce)|max_ammo(35)|weapon_length(55), imodbits_ammo, [], []],
    ["rhodok_bolts_a", "Rhodok Bolts", [("akosmo_bolt", 0), ("akosmo_bolt_bag", ixmesh_carry)], itp_type_bolts|itp_merchandise|itp_can_penetrate_shield|itp_can_knock_down, 0, 290, abundance(70)|weight(3.00)|thrust_damage(6, pierce)|max_ammo(35)|weapon_length(55), imodbits_ammo, [], [fac.kingdom_5]],
    ["rhodok_bolts_b", "Rhodok Piercing Bolts", [("akosmo_bolt", 0), ("akosmo_bolt_bag_b", ixmesh_carry)], itp_type_bolts|itp_merchandise|itp_can_penetrate_shield|itp_extra_penetration, 0, 450, abundance(50)|weight(3.00)|thrust_damage(10, pierce)|max_ammo(34)|weapon_length(55), imodbits_ammo, [], [fac.kingdom_5]],
    ["rhodok_bolts_c", "Rhodok Siege Bolts", [("akosmo_bolt", 0), ("akosmo_bolt_bag_c", ixmesh_carry)], itp_type_bolts|itp_can_penetrate_shield|itp_extra_penetration|itp_can_knock_down, 0, 720, abundance(10)|weight(3.00)|thrust_damage(14, pierce)|max_ammo(32)|weapon_length(55), imodbits_ammo, [], [fac.kingdom_5]],

    ["ammo_end", "{!}endmarker", [("invalid_item", 0)], itp_type_goods, 0, 0, weight(1), imodbits_none], 

########################################################################################################################
# MELEE WEAPONS: ONE-HANDED
########################################################################################################################

    ["weapons_begin", "{!}marker", [("invalid_item", 0)], itp_type_goods, 0, 0, weight(1), imodbits_none], 

    # POLEARMS: CAVALRY

    ["light_lance","Horseman Lance",[("spear_d_2-8m",0)],itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_couchable|itp_wooden_parry,itc_lance|itcf_carry_spear,231,abundance(120)|weight(2.30)|difficulty(8)|spd_rtng(93)|weapon_length(175)|thrust_damage(21,pierce),imodbits_weapon,[],[]],
    ["cavalry_lance","Cavalry Lance",[("bb_rus_lance",0)],itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_couchable|itp_wooden_parry,itc_lance|itcf_carry_spear,424,abundance(100)|weight(2.40)|difficulty(10)|spd_rtng(88)|weapon_length(190)|thrust_damage(25,pierce),imodbits_weapon,[],[]],
    ["great_lance","Great Lance",[("bb_serbian_lance",0)],itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_couchable|itp_crush_through|itp_wooden_parry,itc_lance|itcf_carry_spear,863,abundance(70)|weight(2.50)|difficulty(12)|spd_rtng(83)|weapon_length(200)|thrust_damage(29,pierce),imodbits_weapon,[],[]],
    ["tourney_lance","Joust of Peace",[("lav_lance_swa_tourney_f190",0)],itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_can_knock_down|itp_couchable|itp_wooden_parry,itc_lance|itcf_carry_spear,746,abundance(40)|weight(2.40)|difficulty(11)|spd_rtng(86)|weapon_length(198)|thrust_damage(24,blunt),imodbits_weapon,[],[]],
    ["khergit_lance_a","Steppe Lance",[("bb_mongol_light_lance",0)],itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_couchable|itp_crush_through|itp_wooden_parry,itc_lance|itcf_carry_spear,970,abundance(70)|weight(2.20)|difficulty(13)|spd_rtng(97)|weapon_length(171)|thrust_damage(31,pierce),imodbits_weapon,[],[fac.kingdom_3]],
    ["khergit_lance_b","Khergit Lance",[("bb_mongol_hooked_lance_1",0)],itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_couchable|itp_crush_through|itp_wooden_parry,itc_lance|itcf_carry_spear,1475,abundance(45)|weight(2.30)|difficulty(15)|spd_rtng(96)|weapon_length(182)|thrust_damage(34,pierce),imodbits_weapon,[],[fac.kingdom_3]],
    ["lance_swa_cav_a","Swadian Lance",[("lav_lance_swa_f170",0)],itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_couchable|itp_crush_through|itp_wooden_parry,itc_lance|itcf_carry_spear,435,abundance(100)|weight(2.70)|difficulty(9)|spd_rtng(90)|weapon_length(193)|thrust_damage(23,pierce),imodbits_weapon,[],[fac.kingdom_1]],
    ["lance_swa_cav_b","Swadian Cavalry Lance",[("lav_lance_swa_f190",0)],itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_couchable|itp_crush_through|itp_wooden_parry,itc_lance|itcf_carry_spear,790,abundance(85)|weight(2.90)|difficulty(11)|spd_rtng(86)|weapon_length(213)|thrust_damage(28,pierce),imodbits_weapon,[],[fac.kingdom_1]],
    ["lance_swa_cav_c","Swadian Great Lance",[("lav_lance_swa_f210",0)],itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_couchable|itp_crush_through|itp_wooden_parry,itc_lance|itcf_carry_spear,1228,abundance(70)|weight(3.10)|difficulty(13)|spd_rtng(82)|weapon_length(233)|thrust_damage(32,pierce),imodbits_weapon,[],[fac.kingdom_1]],
    ["knight_lance_1","Knight Lance",[("kovas_lance_1",0)],itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_couchable|itp_crush_through|itp_wooden_parry,itc_lance|itcf_carry_spear,1590,abundance(45)|weight(3.00)|difficulty(15)|spd_rtng(87)|weapon_length(225)|thrust_damage(33,pierce),imodbits_weapon,[],[fac.kingdom_1]],
    ["knight_lance_2","Knight Lance",[("kovas_lance_5",0)],itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_couchable|itp_crush_through|itp_wooden_parry,itc_lance|itcf_carry_spear,1590,abundance(45)|weight(3.00)|difficulty(15)|spd_rtng(87)|weapon_length(225)|thrust_damage(33,pierce),imodbits_weapon,[],[fac.kingdom_1]],
    ["cavalier_lance_1","Cavalier Lance",[("kovas_lance_3",0)],itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_couchable|itp_crush_through|itp_wooden_parry,itc_lance|itcf_carry_spear,2220,abundance(30)|weight(3.00)|difficulty(17)|spd_rtng(86)|weapon_length(230)|thrust_damage(37,pierce),imodbits_weapon,[],[fac.kingdom_1]],
    ["cavalier_lance_2","Cavalier Lance",[("kovas_lance_4",0)],itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_couchable|itp_crush_through|itp_wooden_parry,itc_lance|itcf_carry_spear,2220,abundance(30)|weight(3.00)|difficulty(17)|spd_rtng(86)|weapon_length(230)|thrust_damage(37,pierce),imodbits_weapon,[],[fac.kingdom_1]],
    ["paladin_lance_1","Paladin Lance",[("kovas_lance_2",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_can_penetrate_shield|itp_couchable|itp_crush_through|itp_wooden_parry,itc_lance|itcf_carry_spear,3354,abundance(10)|weight(3.10)|difficulty(19)|spd_rtng(85)|weapon_length(235)|thrust_damage(40,pierce),imodbits_weapon,[],[fac.kingdom_1]],
    ["paladin_lance_2","Paladin Lance",[("kovas_lance_6",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_can_penetrate_shield|itp_couchable|itp_crush_through|itp_wooden_parry,itc_lance|itcf_carry_spear,3354,abundance(10)|weight(3.10)|difficulty(19)|spd_rtng(85)|weapon_length(235)|thrust_damage(40,pierce),imodbits_weapon,[],[fac.kingdom_1]],
    ["priest_lance","Priest Lance",[("lav_lance_swa_tourney_f210",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_can_knock_down|itp_couchable|itp_wooden_parry,itc_lance|itcf_carry_spear,2338,abundance(5)|weight(3.00)|difficulty(17)|spd_rtng(88)|weapon_length(219)|thrust_damage(36,blunt),imodbits_weapon,[],[fac.kingdom_1]],
    ["swadian_lance_royal","Queen Katilus' Lance",[("kovas_lance_6",0)],itp_type_polearm|itp_offset_lance|itp_unique|itp_primary|itp_can_penetrate_shield|itp_couchable|itp_crush_through|itp_extra_penetration|itp_wooden_parry,itc_lance|itcf_carry_spear,5619,abundance(0)|weight(3.00)|difficulty(21)|spd_rtng(95)|weapon_length(235)|thrust_damage(45,pierce),imodbits_weapon,[],[fac.kingdom_1]],
    ["sarranid_lance_a","Sarranid Lance",[("lav_lance_sar_f160",0)],itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_couchable|itp_crush_through|itp_wooden_parry,itc_lance|itcf_carry_spear,990,abundance(80)|weight(2.40)|difficulty(14)|spd_rtng(94)|weapon_length(182)|thrust_damage(32,pierce),imodbits_weapon,[],[fac.kingdom_6]],
    ["sarranid_lance_b","Sarranid Long Lance",[("lav_lance_sar_f180",0)],itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_couchable|itp_crush_through|itp_wooden_parry,itc_lance|itcf_carry_spear,1608,abundance(50)|weight(2.60)|difficulty(16)|spd_rtng(91)|weapon_length(202)|thrust_damage(35,pierce),imodbits_weapon,[],[fac.kingdom_6]],
    ["sarranid_lance_c","Sarranid Heavy Lance",[("lav_lance_sar_f200",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_couchable|itp_crush_through|itp_wooden_parry,itc_lance|itcf_carry_spear,2279,abundance(30)|weight(2.80)|difficulty(18)|spd_rtng(87)|weapon_length(222)|thrust_damage(38,pierce),imodbits_weapon,[],[fac.kingdom_6]],

    ["hafted_blade_b","Hafted Blade",[("khergit_pike_b",0)],itp_type_polearm|itp_two_handed|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_wooden_parry,itc_poleaxe|itcf_carry_spear,442,abundance(70)|weight(2.60)|difficulty(11)|spd_rtng(99)|weapon_length(130)|swing_damage(26,cut),imodbits_weapon,[],[]],
    ["hafted_blade_c","Khergit Hafted Blade",[("luc3_glaive_no1",0)],itp_type_polearm|itp_two_handed|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_wooden_parry,itc_hafted|itcf_carry_spear,721,abundance(55)|weight(2.80)|difficulty(13)|spd_rtng(93)|weapon_length(150)|swing_damage(30,cut)|thrust_damage(25,cut),imodbits_weapon,[],[fac.kingdom_3]],
    ["hafted_blade_a","Jurtchi Hafted Blade",[("khergit_pike_a",0)],itp_type_polearm|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry,itc_hafted|itcf_carry_spear,1241,abundance(25)|weight(2.80)|difficulty(15)|spd_rtng(96)|weapon_length(152)|swing_damage(35,cut)|thrust_damage(22,cut),imodbits_weapon,[],[fac.kingdom_3]],
    ["khergit_hafted_blade_royal","Sanjar's Hafted Blade",[("luc3_glaive_kn_no1",0)],itp_type_polearm|itp_two_handed|itp_unique|itp_primary|itp_bonus_against_shield|itp_wooden_parry,itc_hafted|itcf_carry_spear,2216,abundance(0)|weight(2.90)|difficulty(18)|spd_rtng(107)|weapon_length(155)|swing_damage(41,cut)|thrust_damage(28,pierce),imodbits_weapon,[],[fac.kingdom_3]],

    # POLEARMS: INFANTRY ANTI-CAV

    ["military_fork","Military Fork",[("luc1_fork_military",0)],itp_type_polearm|itp_merchandise|itp_primary|itp_is_pike|itp_wooden_parry,itc_pike|itcf_carry_spear,214,abundance(90)|weight(2.50)|difficulty(9)|spd_rtng(96)|weapon_length(130)|thrust_damage(20,pierce),imodbits_weapon,[],[]],
    ["battle_fork","Battle Fork",[("luc1_fork_battle",0)],itp_type_polearm|itp_merchandise|itp_primary|itp_is_pike|itp_wooden_parry,itc_pike|itcf_carry_spear,301,abundance(80)|weight(2.60)|difficulty(10)|spd_rtng(94)|weapon_length(140)|thrust_damage(22,pierce),imodbits_weapon,[],[]],
    ["partisan","Partisan",[("luc1_partisan",0)],itp_type_polearm|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_is_pike|itp_wooden_parry,itc_rhodok|itcf_carry_spear,607,abundance(80)|weight(3.50)|difficulty(11)|spd_rtng(88)|weapon_length(148)|swing_damage(29,cut)|thrust_damage(24,pierce),imodbits_weapon,[],[]],
    ["trident","Trident",[("luc3_arabian_spear_trident",0)],itp_type_polearm|itp_merchandise|itp_primary|itp_is_pike|itp_wooden_parry,itc_pike|itcf_carry_spear,513,abundance(70)|weight(3.10)|difficulty(12)|spd_rtng(87)|weapon_length(180)|thrust_damage(25,pierce),imodbits_weapon,[],[]],
    ["corseque","Corseque",[("luc3_corseque_no2",0)],itp_type_polearm|itp_merchandise|itp_primary|itp_is_pike|itp_wooden_parry,itc_pike|itcf_carry_spear,601,abundance(60)|weight(3.20)|difficulty(13)|spd_rtng(83)|weapon_length(165)|thrust_damage(28,pierce),imodbits_weapon,[],[fac.kingdom_5]],
    ["battle_fork_b","Rhodok Battle Fork",[("luc3_battle_fork_no2",0)],itp_type_polearm|itp_merchandise|itp_primary|itp_is_pike|itp_wooden_parry,itc_pike|itcf_carry_spear,610,abundance(70)|weight(3.10)|difficulty(14)|spd_rtng(86)|weapon_length(185)|thrust_damage(27,pierce),imodbits_weapon,[],[fac.kingdom_5]],
    ["bill_guisarme","Bill Guisarme",[("luc1_bill_guisarme_n",0)],itp_type_polearm|itp_merchandise|itp_primary|itp_can_knock_down|itp_is_pike|itp_wooden_parry,itc_rhodok|itcf_carry_spear,706,abundance(50)|weight(2.90)|difficulty(12)|spd_rtng(92)|weapon_length(142)|swing_damage(28,cut)|thrust_damage(28,pierce),imodbits_weapon,[],[fac.kingdom_5]],
    ["guisarme","Guisarme",[("luc3_guisarme_no2",0)],itp_type_polearm|itp_merchandise|itp_primary|itp_can_knock_down|itp_is_pike|itp_wooden_parry,itc_rhodok|itcf_carry_spear,1221,abundance(40)|weight(3.30)|difficulty(14)|spd_rtng(88)|weapon_length(180)|swing_damage(32,cut)|thrust_damage(29,pierce),imodbits_weapon,[],[fac.kingdom_5]],
    ["scorpion_guisarme","Scorpion",[("luc3_guisarme_no3",0)],itp_type_polearm|itp_merchandise|itp_primary|itp_can_knock_down|itp_is_pike|itp_wooden_parry,itc_rhodok|itcf_carry_spear,1337,abundance(30)|weight(3.50)|difficulty(15)|spd_rtng(83)|weapon_length(195)|swing_damage(30,cut)|thrust_damage(32,pierce),imodbits_weapon,[],[fac.kingdom_5]],
    ["fauchard_fork","Fauchard Fork",[("luc3_fauchard_fork_no2",0)],itp_type_polearm|itp_merchandise|itp_primary|itp_can_knock_down|itp_is_pike|itp_wooden_parry,itc_rhodok|itcf_carry_spear,1571,abundance(20)|weight(3.40)|difficulty(15)|spd_rtng(84)|weapon_length(190)|swing_damage(33,cut)|thrust_damage(34,pierce),imodbits_weapon,[],[fac.kingdom_5]],

    ["awlpike","Awlpike",[("awl_pike_b",0)],itp_type_polearm|itp_two_handed|itp_merchandise|itp_primary|itp_can_penetrate_shield|itp_extra_penetration|itp_is_pike|itp_wooden_parry,itc_pike|itcf_carry_spear,689,abundance(90)|weight(2.00)|difficulty(10)|spd_rtng(109)|weapon_length(160)|thrust_damage(26,pierce),imodbits_weapon,[],[fac.kingdom_1]],
    ["awlpike_long","Long Awlpike",[("awl_pike_a",0)],itp_type_polearm|itp_two_handed|itp_merchandise|itp_primary|itp_can_penetrate_shield|itp_extra_penetration|itp_is_pike|itp_wooden_parry,itc_pike|itcf_carry_spear,1932,abundance(40)|weight(2.30)|difficulty(14)|spd_rtng(100)|weapon_length(183)|thrust_damage(35,pierce),imodbits_weapon,[],[fac.kingdom_1]],

    ["shortened_spear","Shortened Spear",[("spear_g_1-9m",0)],itp_type_polearm|itp_merchandise|itp_primary|itp_wooden_parry,itc_pike|itcf_carry_spear,137,abundance(100)|weight(1.90)|difficulty(0)|spd_rtng(98)|weapon_length(120)|thrust_damage(19,pierce),imodbits_weapon,[],[]],
    ["boar_spear","Boar Spear",[("spear_h_2-15m",0)],itp_type_polearm|itp_merchandise|itp_primary|itp_wooden_parry,itc_pike|itcf_carry_spear,182,abundance(100)|weight(2.00)|difficulty(8)|spd_rtng(95)|weapon_length(133)|thrust_damage(21,pierce),imodbits_weapon,[],[]],
    ["spear","Spear",[("bb_serbian_spear_1",0)],itp_type_polearm|itp_merchandise|itp_primary|itp_wooden_parry,itc_pike|itcf_carry_spear,226,abundance(100)|weight(2.10)|difficulty(9)|spd_rtng(93)|weapon_length(140)|thrust_damage(23,pierce),imodbits_weapon,[],[]],
    ["war_spear","War Spear",[("spear_i_2-3m",0)],itp_type_polearm|itp_merchandise|itp_primary|itp_wooden_parry,itc_pike|itcf_carry_spear,308,abundance(80)|weight(2.20)|difficulty(10)|spd_rtng(90)|weapon_length(150)|thrust_damage(24,pierce),imodbits_weapon,[],[]],
    ["ashwood_pike","Ashwood Pike",[("bb_ashwood_pike",0)],itp_type_polearm|itp_two_handed|itp_merchandise|itp_primary|itp_is_pike|itp_wooden_parry,itc_pike|itcf_carry_spear,528,abundance(70)|weight(2.70)|difficulty(11)|spd_rtng(91)|weapon_length(165)|thrust_damage(26,pierce),imodbits_weapon,[],[]],
    ["pike","Pike",[("spear_b_2-75m",0)],itp_type_polearm|itp_two_handed|itp_merchandise|itp_primary|itp_is_pike|itp_wooden_parry,itc_pike|itcf_carry_spear,710,abundance(65)|weight(2.70)|difficulty(12)|spd_rtng(90)|weapon_length(173)|thrust_damage(29,pierce),imodbits_weapon,[],[]],
    ["infantry_pike","Infantry Pike",[("spear_f_2-9m",0)],itp_type_polearm|itp_two_handed|itp_merchandise|itp_primary|itp_is_pike|itp_wooden_parry,itc_pike|itcf_carry_spear,845,abundance(60)|weight(2.90)|difficulty(13)|spd_rtng(87)|weapon_length(190)|thrust_damage(30,pierce),imodbits_weapon,[],[]],
    ["bamboo_spear","Bamboo Pike",[("arabian_spear_a_3m",0)],itp_type_polearm|itp_two_handed|itp_merchandise|itp_primary|itp_is_pike|itp_cant_use_on_horseback|itp_wooden_parry,itc_pike|itcf_carry_spear,966,abundance(70)|weight(3.00)|difficulty(13)|spd_rtng(89)|weapon_length(200)|thrust_damage(32,pierce),imodbits_weapon,[],[fac.kingdom_6]],
    ["sarranid_pike","Sarranid Pike",[("spear_a_3m",0)],itp_type_polearm|itp_two_handed|itp_merchandise|itp_primary|itp_is_pike|itp_cant_use_on_horseback|itp_wooden_parry,itc_pike|itcf_carry_spear,1351,abundance(50)|weight(3.40)|difficulty(14)|spd_rtng(83)|weapon_length(240)|thrust_damage(33,pierce),imodbits_weapon,[],[fac.kingdom_6]],
    ["sarranid_long_pike","Sarranid Long Pike",[("bb_rus_pike",0)],itp_type_polearm|itp_two_handed|itp_merchandise|itp_primary|itp_cant_use_on_horseback|itp_wooden_parry,itc_pike|itcf_carry_spear,1465,abundance(30)|weight(3.50)|difficulty(15)|spd_rtng(81)|weapon_length(250)|thrust_damage(35,pierce),imodbits_weapon,[],[fac.kingdom_6]],

    # POLEARMS: INFANTRY ANTI-INF

    ["shortened_military_scythe","Shortened Military Scythe",[("two_handed_battle_scythe_a",0)],itp_type_polearm|itp_two_handed|itp_merchandise|itp_primary|itp_wooden_parry,itc_sword_2h|itcf_carry_spear,186,abundance(80)|weight(2.10)|difficulty(8)|spd_rtng(97)|weapon_length(113)|swing_damage(21,cut)|thrust_damage(20,pierce),imodbits_weapon,[],[]],
    ["military_scythe_a","Mercenary Scythe",[("spear_c_2-5m",0)],itp_type_polearm|itp_two_handed|itp_merchandise|itp_primary|itp_wooden_parry,itc_poleaxe|itcf_carry_spear,385,abundance(60)|weight(2.50)|difficulty(10)|spd_rtng(87)|weapon_length(153)|swing_damage(25,cut),imodbits_weapon,[],[]],
    ["military_scythe_b","Military Scythe",[("spear_e_2-5m",0)],itp_type_polearm|itp_two_handed|itp_merchandise|itp_primary|itp_wooden_parry,itc_halberd|itcf_carry_spear,470,abundance(50)|weight(2.40)|difficulty(11)|spd_rtng(85)|weapon_length(153)|swing_damage(27,cut)|thrust_damage(22,pierce),imodbits_weapon,[],[]],
    ["military_scythe_c","Long Military Scythe",[("spear_e_3-25m",0)],itp_type_polearm|itp_two_handed|itp_merchandise|itp_primary|itp_is_pike|itp_cant_use_on_horseback|itp_wooden_parry,itc_halberd|itcf_carry_spear,1142,abundance(40)|weight(3.30)|difficulty(13)|spd_rtng(80)|weapon_length(225)|swing_damage(31,cut)|thrust_damage(23,pierce),imodbits_weapon,[],[]],

    ["polehammer_a","Lucerne Hammer",[("luc1_lucerne_hammer",0)],itp_type_polearm|itp_two_handed|itp_merchandise|itp_primary|itp_can_knock_down|itp_is_pike|itp_wooden_parry,itc_halberd|itcf_carry_spear,522,abundance(70)|weight(3.10)|difficulty(11)|spd_rtng(88)|weapon_length(120)|swing_damage(29,blunt)|thrust_damage(23,pierce),imodbits_weapon,[],[fac.kingdom_6]],
    ["polehammer_b","Sarranid Polehammer",[("luc1_pole_hammer_z",0)],itp_type_polearm|itp_two_handed|itp_primary|itp_can_knock_down|itp_is_pike|itp_wooden_parry,itc_halberd|itcf_carry_spear,1191,abundance(50)|weight(3.30)|difficulty(14)|spd_rtng(83)|weapon_length(144)|swing_damage(38,blunt)|thrust_damage(27,pierce),imodbits_weapon,[],[fac.kingdom_6]],

    ["poleaxe","Poleaxe",[("luc3_poleaxe_no2",0)],itp_type_polearm|itp_two_handed|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_cant_use_on_horseback|itp_wooden_parry,itc_poleaxe|itcf_carry_spear,696,abundance(80)|weight(3.70)|difficulty(13)|spd_rtng(84)|weapon_length(155)|swing_damage(31,cut),imodbits_weapon,[],[]],
    ["halberd_a","Halberd",[("luc3_poleaxe_no3",0)],itp_type_polearm|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_cant_use_on_horseback|itp_wooden_parry,itc_halberd|itcf_carry_spear,1079,abundance(60)|weight(3.50)|difficulty(13)|spd_rtng(89)|weapon_length(138)|swing_damage(37,cut)|thrust_damage(19,pierce),imodbits_weapon,[],[fac.kingdom_5]],
    ["halberd_b","Rhodok Halberd",[("luc1_flemish_halberd",0)],itp_type_polearm|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_is_pike|itp_cant_use_on_horseback|itp_wooden_parry,itc_halberd|itcf_carry_spear,1992,abundance(40)|weight(3.80)|difficulty(15)|spd_rtng(83)|weapon_length(160)|swing_damage(42,cut)|thrust_damage(21,pierce),imodbits_weapon,[],[fac.kingdom_5]],
    ["rhodok_halberd_royal","Graveth's Halberd",[("luc3_halberd_no1",0)],itp_type_polearm|itp_two_handed|itp_unique|itp_primary|itp_bonus_against_shield|itp_can_penetrate_shield|itp_crush_through|itp_is_pike|itp_cant_use_on_horseback|itp_wooden_parry,itc_halberd|itcf_carry_spear,4023,abundance(0)|weight(3.90)|difficulty(16)|spd_rtng(94)|weapon_length(150)|swing_damage(49,cut)|thrust_damage(29,pierce),imodbits_weapon,[],[fac.kingdom_5]],

    ["glaive","Glaive",[("glaive_b",0)],itp_type_polearm|itp_two_handed|itp_merchandise|itp_primary|itp_is_pike|itp_cant_use_on_horseback|itp_wooden_parry,itc_halberd|itcf_carry_spear,559,abundance(90)|weight(3.60)|difficulty(14)|spd_rtng(84)|weapon_length(158)|swing_damage(31,cut)|thrust_damage(22,cut),imodbits_weapon,[],[]],

    ["voulge_a","Shortened Voulge",[("two_handed_battle_axe_c",0)],itp_type_polearm|itp_two_handed|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_wooden_parry,itc_poleaxe|itcf_carry_spear,510,abundance(90)|weight(2.90)|difficulty(10)|spd_rtng(94)|weapon_length(100)|swing_damage(36,cut),imodbits_weapon,[],[]],
    ["voulge_b","Voulge",[("two_handed_battle_long_axe_a",0)],itp_type_polearm|itp_two_handed|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_cant_use_on_horseback|itp_wooden_parry,itc_poleaxe|itcf_carry_spear,1462,abundance(60)|weight(3.90)|difficulty(15)|spd_rtng(81)|weapon_length(172)|swing_damage(40,cut),imodbits_weapon,[],[]],

    # INFANTRY WEAPONS: TWO-HANDED

    ["bardiche_a","Shortened Bardiche",[("two_handed_battle_axe_d",0)],itp_type_polearm|itp_two_handed|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_wooden_parry,itc_poleaxe|itcf_carry_spear,404,abundance(95)|weight(3.00)|difficulty(10)|spd_rtng(107)|weapon_length(100)|swing_damage(29,cut),imodbits_weapon,[],[fac.kingdom_2]],
    ["bardiche_b","Bardiche",[("two_handed_battle_axe_f",0)],itp_type_polearm|itp_two_handed|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_wooden_parry,itc_poleaxe|itcf_carry_spear,637,abundance(85)|weight(3.20)|difficulty(11)|spd_rtng(102)|weapon_length(115)|swing_damage(33,cut),imodbits_weapon,[],[fac.kingdom_2]],
    ["bardiche_c","Infantry Bardiche",[("two_handed_battle_long_axe_b",0)],itp_type_polearm|itp_two_handed|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_wooden_parry,itc_poleaxe|itcf_carry_spear,1088,abundance(70)|weight(3.40)|difficulty(13)|spd_rtng(95)|weapon_length(138)|swing_damage(38,cut),imodbits_weapon,[],[fac.kingdom_2]],
    ["bardiche_d","Lineman Bardiche",[("two_handed_battle_long_axe_c",0)],itp_type_polearm|itp_two_handed|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_wooden_parry,itc_poleaxe|itcf_carry_spear,1426,abundance(55)|weight(3.50)|difficulty(15)|spd_rtng(90)|weapon_length(153)|swing_damage(40,cut),imodbits_weapon,[],[fac.kingdom_2]],
    ["vaegir_bardiche_royal","Yaroglek's Bardiche",[("akosmo_two_handed_battle_long_axe_b",0)],itp_type_polearm|itp_two_handed|itp_unique|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_extra_penetration|itp_wooden_parry,itc_poleaxe|itcf_carry_spear,3491,abundance(0)|weight(3.30)|difficulty(14)|spd_rtng(106)|weapon_length(138)|swing_damage(45,cut),imodbits_weapon,[],[fac.kingdom_2]],

    #
    ["bec_de_corbin_a","Bec de Corbin",[("bec_de_corbin_a",0)],itp_type_two_handed_wpn|itp_two_handed|itp_merchandise|itp_primary|itp_secondary|itp_can_penetrate_shield|itp_extra_penetration|itp_cant_use_on_horseback|itp_wooden_parry,itc_sword_2h|itcf_carry_spear,523,abundance(50)|weight(2.70)|difficulty(11)|spd_rtng(93)|weapon_length(100)|swing_damage(26,pierce)|thrust_damage(17,pierce),imodbits_weapon,[],[]],

    ["two_handed_battle_axe_a","Two-Handed Axe",[("two_handed_battle_axe_a",0)],itp_type_two_handed_wpn|itp_two_handed|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_wooden_parry,itc_sabre_2h|itcf_carry_axe_back,517,abundance(70)|weight(2.90)|difficulty(10)|spd_rtng(94)|weapon_length(87)|swing_damage(36,cut),imodbits_weapon,[],[]],
    ["two_handed_battle_axe_b","War Axe",[("two_handed_battle_axe_b",0)],itp_type_two_handed_wpn|itp_two_handed|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_wooden_parry,itc_sabre_2h|itcf_carry_axe_back,680,abundance(65)|weight(3.00)|difficulty(11)|spd_rtng(93)|weapon_length(90)|swing_damage(40,cut),imodbits_weapon,[],[]],
    ["two_handed_battle_axe_e","Bearded War Axe",[("two_handed_battle_axe_e",0)],itp_type_two_handed_wpn|itp_two_handed|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_wooden_parry,itc_sabre_2h|itcf_carry_axe_back,685,abundance(60)|weight(3.10)|difficulty(11)|spd_rtng(95)|weapon_length(90)|swing_damage(39,cut),imodbits_weapon,[],[fac.kingdom_4]],
    ["voulge","Skald War Axe",[("luc3_wagoners_axe_no2",0)],itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_secondary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_wooden_parry,itc_sabre_2h|itcf_carry_axe_back,1312,abundance(50)|weight(3.80)|difficulty(14)|spd_rtng(89)|weapon_length(130)|swing_damage(44,cut),imodbits_weapon,[],[fac.kingdom_4]],
    ["long_axe_a","Long Axe",[("long_axe_a",0)],itp_type_two_handed_wpn|itp_two_handed|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_wooden_parry,itc_sabre_2h|itcf_carry_axe_back,1135,abundance(60)|weight(3.30)|difficulty(12)|spd_rtng(92)|weapon_length(113)|swing_damage(45,cut),imodbits_weapon,[],[fac.kingdom_4]],
    ["long_axe_b","Nordic Long Axe",[("long_axe_b",0)],itp_type_two_handed_wpn|itp_two_handed|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_wooden_parry,itc_sabre_2h|itcf_carry_axe_back,1632,abundance(50)|weight(3.40)|difficulty(14)|spd_rtng(90)|weapon_length(120)|swing_damage(51,cut),imodbits_weapon,[],[fac.kingdom_4]],
    ["long_axe_c","Berserker Axe",[("long_axe_c",0)],itp_type_two_handed_wpn|itp_two_handed|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_wooden_parry,itc_sabre_2h|itcf_carry_axe_back,1803,abundance(30)|weight(3.50)|difficulty(15)|spd_rtng(87)|weapon_length(130)|swing_damage(49,cut),imodbits_weapon,[],[fac.kingdom_4]],

    ["mace_long_c","Long Spiked Club",[("mace_long_c",0)],itp_type_two_handed_wpn|itp_two_handed|itp_merchandise|itp_primary|itp_secondary|itp_can_knock_down|itp_cant_use_on_horseback|itp_wooden_parry,itc_sabre_2h|itcf_carry_axe_back,472,abundance(90)|weight(2.00)|difficulty(9)|spd_rtng(90)|weapon_length(125)|swing_damage(28,blunt),imodbits_weapon,[],[]],
    ["mace_long_a","Two-Handed Mace",[("mace_long_a",0)],itp_type_two_handed_wpn|itp_two_handed|itp_merchandise|itp_primary|itp_secondary|itp_can_knock_down|itp_cant_use_on_horseback|itp_wooden_parry,itc_sabre_2h|itcf_carry_axe_back,990,abundance(50)|weight(2.20)|difficulty(11)|spd_rtng(90)|weapon_length(130)|swing_damage(34,blunt),imodbits_weapon,[],[]],
    ["mace_long_b","Long Knobbed Mace",[("mace_long_b",0)],itp_type_two_handed_wpn|itp_two_handed|itp_merchandise|itp_primary|itp_secondary|itp_can_knock_down|itp_cant_use_on_horseback|itp_wooden_parry,itc_sabre_2h|itcf_carry_axe_back,1289,abundance(50)|weight(2.50)|difficulty(12)|spd_rtng(90)|weapon_length(135)|swing_damage(38,blunt),imodbits_weapon,[],[]],

    ["sledgehammer_b","Sledgehammer",[("maul_b",0)],itp_type_two_handed_wpn|itp_two_handed|itp_merchandise|itp_primary|itp_secondary|itp_can_knock_down|itp_crush_through|itp_cant_use_on_horseback|itp_unbalanced|itp_wooden_parry|itp_wooden_attack,itc_sabre_2h|itcf_carry_axe_back,287,abundance(100)|weight(2.50)|difficulty(12)|spd_rtng(85)|weapon_length(70)|swing_damage(30,blunt),imodbits_weapon,[],[]],
    ["sledgehammer","Wooden Hammer",[("maul_c",0)],itp_type_two_handed_wpn|itp_two_handed|itp_merchandise|itp_primary|itp_secondary|itp_can_knock_down|itp_crush_through|itp_cant_use_on_horseback|itp_unbalanced|itp_wooden_parry|itp_wooden_attack,itc_sabre_2h|itcf_carry_axe_back,243,abundance(100)|weight(2.30)|difficulty(11)|spd_rtng(89)|weapon_length(70)|swing_damage(27,blunt),imodbits_weapon,[],[]],
    ["maul","Maul",[("maul_d",0)],itp_type_two_handed_wpn|itp_two_handed|itp_merchandise|itp_primary|itp_secondary|itp_can_knock_down|itp_crush_through|itp_cant_use_on_horseback|itp_unbalanced|itp_wooden_parry,itc_sabre_2h|itcf_carry_axe_back,520,abundance(70)|weight(3.40)|difficulty(16)|spd_rtng(74)|weapon_length(70)|swing_damage(38,blunt),imodbits_weapon,[],[]],
    ["maul_b","Steel Sledgehammer",[("luc1_horsemans_hammer",0)],itp_type_two_handed_wpn|itp_two_handed|itp_merchandise|itp_primary|itp_secondary|itp_can_knock_down|itp_crush_through|itp_cant_use_on_horseback|itp_unbalanced|itp_wooden_parry,itc_sabre_2h|itcf_carry_axe_back,660,abundance(60)|weight(2.60)|difficulty(15)|spd_rtng(79)|weapon_length(73)|swing_damage(39,blunt),imodbits_weapon,[],[]],
    ["maul_c","Great Hammer",[("luc3_greathammer_no1",0)],itp_type_two_handed_wpn|itp_two_handed|itp_merchandise|itp_primary|itp_secondary|itp_can_knock_down|itp_crush_through|itp_cant_use_on_horseback|itp_unbalanced|itp_wooden_parry,itc_sabre_2h|itcf_carry_axe_back,833,abundance(50)|weight(3.20)|difficulty(17)|spd_rtng(72)|weapon_length(74)|swing_damage(44,blunt),imodbits_weapon,[],[]],
    #
    #
    #
    ["maul_d","Long Sledgehammer",[("luc1_long_hammer",0)],itp_type_two_handed_wpn|itp_two_handed|itp_merchandise|itp_primary|itp_secondary|itp_can_knock_down|itp_crush_through|itp_cant_use_on_horseback|itp_unbalanced|itp_wooden_parry,itc_sabre_2h|itcf_carry_axe_back,1378,abundance(40)|weight(3.00)|difficulty(18)|spd_rtng(70)|weapon_length(118)|swing_damage(43,blunt),imodbits_weapon,[],[]],

    ["bastard_sword_a","Short Bastard Sword",[("bastard_sword_a",0),("bastard_sword_a_scabbard",ixmesh_carry)],itp_type_two_handed_wpn|itp_two_handed|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,683,abundance(90)|weight(1.50)|difficulty(10)|spd_rtng(117)|weapon_length(98)|swing_damage(34,cut)|thrust_damage(28,pierce),imodbits_weapon,[],[]],
    ["bastard_sword_b","Bastard Sword",[("bastard_sword_b",0),("bastard_sword_b_scabbard",ixmesh_carry)],itp_type_two_handed_wpn|itp_two_handed|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,931,abundance(90)|weight(1.60)|difficulty(11)|spd_rtng(113)|weapon_length(105)|swing_damage(38,cut)|thrust_damage(30,pierce),imodbits_weapon,[],[]],
    ["sword_two_handed_b","Mercenary Bastard Sword",[("sword_two_handed_b",0)],itp_type_two_handed_wpn|itp_two_handed|itp_merchandise|itp_primary|itp_secondary,itc_sword_2h|itcf_carry_sword_back,1286,abundance(80)|weight(1.60)|difficulty(12)|spd_rtng(109)|weapon_length(108)|swing_damage(42,cut)|thrust_damage(31,pierce),imodbits_weapon,[],[]],
    ["sword_two_handed_a","Two-Handed Sword",[("sword_two_handed_a",0)],itp_type_two_handed_wpn|itp_two_handed|itp_merchandise|itp_primary|itp_secondary,itc_sword_2h|itcf_carry_sword_back,2011,abundance(50)|weight(1.80)|difficulty(14)|spd_rtng(104)|weapon_length(117)|swing_damage(45,cut)|thrust_damage(32,pierce),imodbits_weapon,[],[]],
    ["military_cleaver_a","War Cleaver",[("military_cleaver_a",0)],itp_type_two_handed_wpn|itp_two_handed|itp_merchandise|itp_primary|itp_secondary,itc_sabre_2h|itcf_carry_sword_back,2028,abundance(60)|weight(1.80)|difficulty(14)|spd_rtng(108)|weapon_length(118)|swing_damage(46,cut),imodbits_weapon,[],[fac.kingdom_5]],

    # CAVALRY WEAPONS: ONE-HANDED

    ["sword_medieval_c_small","Short Sword",[("sword_medieval_c_small",0),("sword_medieval_c_small_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,134,abundance(110)|weight(1.00)|difficulty(0)|spd_rtng(114)|weapon_length(80)|swing_damage(20,cut)|thrust_damage(19,pierce),imodbits_weapon,[],[]],
    ["sword_norman","Arming Sword",[("sword_norman",0),("sword_norman_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,209,abundance(110)|weight(1.10)|difficulty(0)|spd_rtng(106)|weapon_length(92)|swing_damage(23,cut)|thrust_damage(22,pierce),imodbits_weapon,[],[]],
    ["sword_medieval_d","Sword",[("sword_medieval_d",0),("sword_medieval_d_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,191,abundance(100)|weight(1.30)|difficulty(8)|spd_rtng(100)|weapon_length(95)|swing_damage(21,cut)|thrust_damage(20,pierce),imodbits_weapon,[],[]],
    ["sword_medieval_c","Mercenary Sword",[("sword_medieval_c",0),("sword_medieval_c_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,263,abundance(90)|weight(1.40)|difficulty(9)|spd_rtng(102)|weapon_length(96)|swing_damage(23,cut)|thrust_damage(22,pierce),imodbits_weapon,[],[]],
    ["sword_medieval_c_long","Long Sword",[("sword_medieval_c_long",0),("sword_medieval_c_long_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,357,abundance(90)|weight(1.50)|difficulty(11)|spd_rtng(97)|weapon_length(101)|swing_damage(26,cut)|thrust_damage(21,pierce),imodbits_weapon,[],[]],
    ["sword_medieval_d_long","Equite Sword",[("sword_medieval_d_long",0),("sword_medieval_d_long_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,579,abundance(70)|weight(1.50)|difficulty(12)|spd_rtng(95)|weapon_length(102)|swing_damage(30,cut)|thrust_damage(23,pierce),imodbits_weapon,[],[]],
    #
    ["sword_norman_rusty","Rusty Sword",[("sword_norman_rusty",0),("sword_norman_rusty_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,132,abundance(110)|weight(1.20)|difficulty(0)|spd_rtng(99)|weapon_length(92)|swing_damage(19,cut)|thrust_damage(18,pierce),imodbits_weapon,[],[]],

    ["swadian_short_sword_a","Swadian Short Sword",[("bb_oackeshott_type_14",0),("bb_oackeshott_type_14_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,151,abundance(120)|weight(1.00)|difficulty(0)|spd_rtng(112)|weapon_length(82)|swing_damage(22,cut)|thrust_damage(22,pierce),imodbits_weapon,[],[fac.kingdom_1]],
    ["swadian_short_sword_b","Swadian Infantry Sword",[("bb_oakeshott_type_10_V2",0),("bb_oakeshott_type_10_V2_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,239,abundance(110)|weight(1.10)|difficulty(9)|spd_rtng(117)|weapon_length(85)|swing_damage(25,cut)|thrust_damage(25,pierce),imodbits_weapon,[],[fac.kingdom_1]],
    ["swadian_short_sword_c","Swadian Sergeant Sword",[("bb_medieval_sword_3_short",0),("bb_medieval_sword_3_short_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,338,abundance(100)|weight(1.10)|difficulty(11)|spd_rtng(115)|weapon_length(85)|swing_damage(28,cut)|thrust_damage(28,pierce),imodbits_weapon,[],[fac.kingdom_1]],
    ["sword_medieval_a","Swadian Sword",[("sword_medieval_a",0),("sword_medieval_a_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,240,abundance(110)|weight(1.30)|difficulty(8)|spd_rtng(105)|weapon_length(96)|swing_damage(24,cut)|thrust_damage(24,pierce),imodbits_weapon,[],[fac.kingdom_1]],
    ["sword_swadian_a","Swadian Officer Sword",[("bb_hospitaler_sword_1",0),("bb_hospitaler_sword_1_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,405,abundance(100)|weight(1.30)|difficulty(10)|spd_rtng(103)|weapon_length(97)|swing_damage(29,cut)|thrust_damage(29,pierce),imodbits_weapon,[],[fac.kingdom_1]],
    ["sword_swadian_b","Page Sword",[("bb_serbian_sword_2",0),("bb_serbian_sword_2_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,413,abundance(80)|weight(1.50)|difficulty(12)|spd_rtng(97)|weapon_length(99)|swing_damage(27,cut)|thrust_damage(23,pierce),imodbits_weapon,[],[fac.kingdom_1]],
    ["sword_swadian_c","Squire Sword",[("bb_serbian_sword_1",0),("bb_serbian_sword_1_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,538,abundance(70)|weight(1.60)|difficulty(13)|spd_rtng(95)|weapon_length(102)|swing_damage(29,cut)|thrust_damage(24,pierce),imodbits_weapon,[],[fac.kingdom_1]],
    ["sword_swadian_d","Swadian Long Sword",[("bb_medieval_sword_2_long",0),("bb_medieval_sword_2_long_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,698,abundance(65)|weight(1.60)|difficulty(14)|spd_rtng(92)|weapon_length(104)|swing_damage(32,cut)|thrust_damage(26,pierce),imodbits_weapon,[],[fac.kingdom_1]],
    ["sword_swadian_e","Swadian Cavalry Sword",[("bb_serbian_sword_4",0),("bb_serbian_sword_4_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,809,abundance(60)|weight(1.50)|difficulty(15)|spd_rtng(99)|weapon_length(99)|swing_damage(34,cut)|thrust_damage(25,pierce),imodbits_weapon,[],[fac.kingdom_1]],
    ["sword_medieval_a_long","Knightly Blade",[("sword_medieval_a_long",0),("sword_medieval_a_long_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,861,abundance(50)|weight(1.60)|difficulty(16)|spd_rtng(93)|weapon_length(101)|swing_damage(34,cut)|thrust_damage(27,pierce),imodbits_weapon,[],[fac.kingdom_1]],
    ["sword_swadian_f","Cavalier Sword",[("bb_serbian_sword_3",0),("bb_serbian_sword_3_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,1120,abundance(40)|weight(1.60)|difficulty(17)|spd_rtng(91)|weapon_length(103)|swing_damage(37,cut)|thrust_damage(28,pierce),imodbits_weapon,[],[fac.kingdom_1]],
    ["sword_swadian_g","Paladin Sword",[("luc1_italian_longsword",0),("luc1_italian_longsword_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,1539,abundance(20)|weight(1.70)|difficulty(18)|spd_rtng(90)|weapon_length(106)|swing_damage(40,cut)|thrust_damage(29,pierce),imodbits_weapon,[],[fac.kingdom_1]],

    ["skirmisher_pick","Skirmisher Pick",[("bb_fight_pick_new_a",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_extra_penetration|itp_wooden_parry,itc_sabre_1h|itcf_carry_axe_left_hip,84,abundance(90)|weight(1.00)|difficulty(0)|spd_rtng(104)|weapon_length(60)|swing_damage(15,pierce),imodbits_weapon,[],[]],
    ["military_pick","Military Pick",[("steel_pick_new",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_extra_penetration,itc_sabre_1h|itcf_carry_axe_left_hip,144,abundance(80)|weight(1.00)|difficulty(8)|spd_rtng(99)|weapon_length(68)|swing_damage(18,pierce),imodbits_weapon,[],[]],
    ["crossbowman_pick","Crossbowman Pick",[("fighting_pick_new",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_extra_penetration|itp_wooden_parry,itc_sabre_1h|itcf_carry_axe_left_hip,209,abundance(60)|weight(1.10)|difficulty(9)|spd_rtng(97)|weapon_length(70)|swing_damage(20,pierce),imodbits_weapon,[],[fac.kingdom_1]],
    ["fighting_pick","Fighting Pick",[("luc1_warhammer_s",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_extra_penetration|itp_wooden_parry,itc_sabre_1h|itcf_carry_axe_left_hip,292,abundance(50)|weight(1.10)|difficulty(9)|spd_rtng(97)|weapon_length(69)|swing_damage(23,pierce),imodbits_weapon,[],[fac.kingdom_1]],
    ["vaegir_pick","Vaegir Pick",[("luc1_horseman_pick",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_extra_penetration,itc_sabre_1h|itcf_carry_axe_left_hip,354,abundance(50)|weight(1.20)|difficulty(11)|spd_rtng(98)|weapon_length(70)|swing_damage(25,pierce),imodbits_weapon,[],[fac.kingdom_2]],

    ["one_handed_battle_axe_g","Swadian Fighting Axe",[("one_handed_battle_axe_g",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield,itc_sabre_1h|itcf_carry_axe_left_hip,351,abundance(50)|weight(1.90)|difficulty(10)|spd_rtng(93)|weapon_length(70)|swing_damage(28,cut),imodbits_weapon,[],[fac.kingdom_1]],
    ["one_handed_battle_axe_h","Swadian Battle Axe",[("one_handed_battle_axe_h",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield,itc_sabre_1h|itcf_carry_axe_left_hip,474,abundance(40)|weight(1.70)|difficulty(9)|spd_rtng(96)|weapon_length(70)|swing_damage(31,cut),imodbits_weapon,[],[fac.kingdom_1]],
    ["two_handed_battle_axe_h","Swadian Knight Axe",[("two_handed_battle_axe_h",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield,itc_sabre_1h|itcf_carry_axe_left_hip,879,abundance(20)|weight(2.20)|difficulty(14)|spd_rtng(89)|weapon_length(90)|swing_damage(36,cut),imodbits_weapon,[],[fac.kingdom_1]],
    ["two_handed_battle_axe_g","Swadian Noble Axe",[("two_handed_battle_axe_g",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield,itc_sabre_1h|itcf_carry_axe_left_hip,1163,abundance(15)|weight(2.00)|difficulty(13)|spd_rtng(92)|weapon_length(95)|swing_damage(39,cut),imodbits_weapon,[],[fac.kingdom_1]],

    ["sentinel_morningstar","Sentinel's Morningstar",[("luc3_morningstar_no1",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_crush_through|itp_unbalanced|itp_wooden_parry,itc_sabre_1h|itcf_carry_axe_left_hip,825,abundance(5)|weight(1.50)|difficulty(9)|spd_rtng(94)|weapon_length(65)|swing_damage(39,pierce),imodbits_weapon,[],[fac.kingdom_2]],
    ["iron_morningstar","Iron Morningstar",[("luc1_iron_morningstar",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_crush_through|itp_unbalanced,itc_sabre_1h|itcf_carry_axe_left_hip,262,abundance(80)|weight(1.90)|difficulty(10)|spd_rtng(89)|weapon_length(73)|swing_damage(27,pierce),imodbits_weapon,[],[fac.kingdom_2]],
    ["morningstar","Horseman's Morningstar",[("mace_morningstar_new",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_crush_through|itp_unbalanced,itc_sabre_1h|itcf_carry_axe_left_hip,411,abundance(70)|weight(2.00)|difficulty(11)|spd_rtng(85)|weapon_length(83)|swing_damage(31,pierce),imodbits_weapon,[],[fac.kingdom_2]],
    ["elite_morningstar","Elite Morningstar",[("luc1_morningstar_new",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_crush_through|itp_unbalanced,itc_sabre_1h|itcf_carry_axe_left_hip,606,abundance(60)|weight(2.00)|difficulty(12)|spd_rtng(84)|weapon_length(85)|swing_damage(36,pierce),imodbits_weapon,[],[fac.kingdom_2]],
    ["weighted_morningstar","Weighted Morningstar",[("luc2_morningstar_2",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_crush_through|itp_unbalanced,itc_sabre_1h|itcf_carry_axe_left_hip,884,abundance(50)|weight(2.20)|difficulty(13)|spd_rtng(82)|weapon_length(95)|swing_damage(40,pierce),imodbits_weapon,[],[fac.kingdom_2]],
    ["vaegir_morningstar_royal","Yaroglek's Morningstar",[("luc3_morgenstern_no2",0)],itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_bonus_against_shield|itp_can_knock_down|itp_crush_through|itp_wooden_parry,itc_sabre_1h|itcf_carry_axe_left_hip,2310,abundance(0)|weight(2.00)|difficulty(15)|spd_rtng(93)|weapon_length(110)|swing_damage(42,pierce),imodbits_weapon,[],[fac.kingdom_2]],

    ["kharash_blade","Kharash Blade",[("luc3_swiss_falchion_v3",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sabre_1h|itcf_carry_sword_left_hip,454,abundance(80)|weight(1.30)|difficulty(9)|spd_rtng(100)|weapon_length(82)|swing_damage(31,cut),imodbits_weapon,[],[fac.kingdom_3]],
    ["khergit_sword_b","Sabre",[("khergit_sword_b",0),("khergit_sword_b_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sabre_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,271,abundance(100)|weight(1.00)|difficulty(8)|spd_rtng(102)|weapon_length(85)|swing_damage(26,cut),imodbits_weapon,[],[]],
    ["khergit_sword_a","Steppe Sabre",[("khergit_sword_a",0),("khergit_sword_a_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sabre_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,326,abundance(110)|weight(1.10)|difficulty(9)|spd_rtng(104)|weapon_length(88)|swing_damage(29,cut),imodbits_weapon,[],[]],
    ["khergit_sword_c","Khergit Sabre",[("khergit_sword_c",0),("khergit_sword_c_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sabre_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,452,abundance(100)|weight(1.10)|difficulty(10)|spd_rtng(105)|weapon_length(88)|swing_damage(32,cut),imodbits_weapon,[],[fac.kingdom_3]],
    ["khergit_sword_d","Kharash Sabre",[("khergit_sword_d",0),("khergit_sword_d_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sabre_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,756,abundance(60)|weight(1.20)|difficulty(10)|spd_rtng(101)|weapon_length(88)|swing_damage(35,cut),imodbits_weapon,[],[fac.kingdom_3]],
    ["sword_medieval_e","Khergit Light Sabre",[("sword_medieval_e",0),("sword_medieval_e_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sabre_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,562,abundance(50)|weight(1.00)|difficulty(0)|spd_rtng(108)|weapon_length(95)|swing_damage(28,cut),imodbits_weapon,[],[fac.kingdom_3]],
    ["khergit_sword","Khergit Noble Blade",[("khergit_sword",0),("khergit_sword_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sabre_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,1161,abundance(30)|weight(1.20)|difficulty(9)|spd_rtng(105)|weapon_length(100)|swing_damage(36,cut),imodbits_weapon,[],[fac.kingdom_3]],
    ["khergit_sword_two_handed_a","Tarkhan Sword",[("khergit_sword_two_handed_a",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary,itc_sabre_1h|itcf_carry_sword_left_hip,1272,abundance(20)|weight(1.30)|difficulty(12)|spd_rtng(99)|weapon_length(111)|swing_damage(35,cut),imodbits_weapon,[],[fac.kingdom_3]],
    ["khergit_sword_two_handed_b","Guanren Sabre",[("khergit_sword_two_handed_b",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary,itc_sabre_1h|itcf_carry_sword_left_hip,1749,abundance(10)|weight(1.40)|difficulty(14)|spd_rtng(100)|weapon_length(113)|swing_damage(39,cut),imodbits_weapon,[],[fac.kingdom_3]],
    ["khergit_sabre_royal","Sanjar's Blade",[("romanoir_sword",0)],itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary,itc_sabre_1h|itcf_carry_sword_left_hip,2574,abundance(0)|weight(1.10)|difficulty(11)|spd_rtng(110)|weapon_length(102)|swing_damage(47,cut),imodbits_weapon,[],[fac.kingdom_3]],

    ["sword_medieval_b_small","Nordic Militia Sword",[("sword_medieval_b_small",0),("sword_medieval_b_small_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,163,abundance(100)|weight(1.10)|difficulty(0)|spd_rtng(110)|weapon_length(80)|swing_damage(21,cut)|thrust_damage(17,pierce),imodbits_weapon,[],[]],
    ["sword_viking_a_small","Nordic Short Sword",[("sword_viking_a_small",0),("sword_viking_a_small_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,201,abundance(100)|weight(1.10)|difficulty(8)|spd_rtng(112)|weapon_length(80)|swing_damage(23,cut)|thrust_damage(20,pierce),imodbits_weapon,[],[]],
    ["sword_viking_b_small","Nordic Warrior Sword",[("sword_viking_b_small",0),("sword_viking_b_small_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,245,abundance(100)|weight(1.20)|difficulty(8)|spd_rtng(115)|weapon_length(80)|swing_damage(25,cut)|thrust_damage(22,pierce),imodbits_weapon,[],[fac.kingdom_4]],
    ["sword_medieval_b","Raider Sword",[("sword_medieval_b",0),("sword_medieval_b_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,336,abundance(100)|weight(1.40)|difficulty(8)|spd_rtng(102)|weapon_length(95)|swing_damage(27,cut)|thrust_damage(22,pierce),imodbits_weapon,[],[fac.outlaws]],
    ["sword_viking_c","Nordic Sword",[("sword_viking_c",0),("sword_viking_c_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,390,abundance(100)|weight(1.30)|difficulty(9)|spd_rtng(100)|weapon_length(95)|swing_damage(29,cut)|thrust_damage(24,pierce),imodbits_weapon,[],[fac.kingdom_4]],
    ["sword_viking_a","Butsecarl Sword",[("sword_viking_a",0),("sword_viking_a_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,491,abundance(80)|weight(1.50)|difficulty(10)|spd_rtng(95)|weapon_length(95)|swing_damage(30,cut)|thrust_damage(23,pierce),imodbits_weapon,[],[fac.kingdom_4]],
    ["sword_viking_b","Lithman Sword",[("sword_viking_b",0),("sword_viking_b_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,657,abundance(60)|weight(1.60)|difficulty(11)|spd_rtng(94)|weapon_length(95)|swing_damage(32,cut)|thrust_damage(24,pierce),imodbits_weapon,[],[fac.kingdom_4]],
    ["sword_viking_c_long","Viking Sword",[("sword_viking_c_long",0),("sword_viking_c_long_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,857,abundance(50)|weight(1.70)|difficulty(13)|spd_rtng(90)|weapon_length(102)|swing_damage(34,cut)|thrust_damage(25,pierce),imodbits_weapon,[],[fac.kingdom_4]],
    ["sword_viking_a_long","Valkyrie Sword",[("sword_viking_a_long",0),("sword_viking_a_long_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,1176,abundance(30)|weight(1.80)|difficulty(14)|spd_rtng(91)|weapon_length(102)|swing_damage(37,cut)|thrust_damage(26,pierce),imodbits_weapon,[],[fac.kingdom_4]],
    #

    ["one_handed_battle_axe_a","Fighting Axe",[("one_handed_battle_axe_a",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry,itc_sabre_1h|itcf_carry_axe_left_hip,200,abundance(100)|weight(1.60)|difficulty(9)|spd_rtng(92)|weapon_length(70)|swing_damage(26,cut),imodbits_weapon,[],[]],
    ["one_handed_battle_axe_c","Spiked Crescent Axe",[("one_handed_battle_axe_c",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry,itc_sabre_1h|itcf_carry_axe_left_hip,248,abundance(80)|weight(1.60)|difficulty(8)|spd_rtng(95)|weapon_length(70)|swing_damage(26,cut),imodbits_weapon,[],[]],
    ["one_handed_war_axe_a","Nordic Axe",[("one_handed_war_axe_a",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry,itc_sabre_1h|itcf_carry_axe_left_hip,286,abundance(90)|weight(1.70)|difficulty(10)|spd_rtng(90)|weapon_length(70)|swing_damage(30,cut),imodbits_weapon,[],[]],
    ["one_handed_war_axe_b","Nordic Bearded Axe",[("one_handed_war_axe_b",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry,itc_sabre_1h|itcf_carry_axe_left_hip,430,abundance(70)|weight(1.80)|difficulty(11)|spd_rtng(89)|weapon_length(70)|swing_damage(34,cut),imodbits_weapon,[],[]],
    ["one_handed_battle_axe_b","Crescent Axe",[("one_handed_battle_axe_b",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry,itc_sabre_1h|itcf_carry_axe_left_hip,429,abundance(60)|weight(1.70)|difficulty(10)|spd_rtng(92)|weapon_length(75)|swing_damage(31,cut),imodbits_weapon,[],[]],
    ["nordic_axe_a","Housecarl Small Axe",[("bb_slavic_axe_1",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_wooden_parry,itc_sabre_1h|itcf_carry_axe_left_hip,333,abundance(50)|weight(1.70)|difficulty(12)|spd_rtng(100)|weapon_length(65)|swing_damage(30,cut),imodbits_weapon,[],[fac.kingdom_4]],
    ["nordic_axe_b","Housecarl Axe",[("bb_bulgarian_light_foot_axe",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_wooden_parry,itc_sabre_1h|itcf_carry_axe_left_hip,517,abundance(40)|weight(1.80)|difficulty(14)|spd_rtng(97)|weapon_length(71)|swing_damage(35,cut),imodbits_weapon,[],[fac.kingdom_4]],
    ["nordic_axe_c","Thane Axe",[("bb_slavic_cavalry_axe_1",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_wooden_parry,itc_sabre_1h|itcf_carry_axe_left_hip,782,abundance(30)|weight(1.90)|difficulty(15)|spd_rtng(94)|weapon_length(79)|swing_damage(40,cut),imodbits_weapon,[],[fac.kingdom_4]],
    ["nord_axe_royal","Ragnar's Light Edge",[("bb_light_edge_final",0)],itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary,itc_sabre_1h|itcf_carry_axe_left_hip,1296,abundance(0)|weight(2.00)|difficulty(19)|spd_rtng(101)|weapon_length(85)|swing_damage(44,cut),imodbits_weapon,[],[fac.kingdom_4]],

    ["falchion_new","Falchion",[("falchion_new",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip,108,abundance(110)|weight(1.10)|difficulty(0)|spd_rtng(119)|weapon_length(72)|swing_damage(19,cut)|thrust_damage(16,pierce),imodbits_weapon,[],[]],
    #
    #
    ["heavy_falchion","Heavy Falchion",[("luc1_falchion",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip,182,abundance(100)|weight(1.40)|difficulty(8)|spd_rtng(111)|weapon_length(80)|swing_damage(22,cut)|thrust_damage(17,pierce),imodbits_weapon,[],[fac.kingdom_5]],
    ["short_bill","Shortened Bill",[("luc1_shortened_bill",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip,335,abundance(70)|weight(1.30)|difficulty(9)|spd_rtng(104)|weapon_length(81)|swing_damage(26,cut)|thrust_damage(14,pierce),imodbits_weapon,[],[fac.kingdom_5]],
    ["short_voulge","Short Voulge",[("mackie_short_voulge",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield,itc_sword_1h|itcf_carry_sword_left_hip,448,abundance(50)|weight(1.80)|difficulty(10)|spd_rtng(99)|weapon_length(70)|swing_damage(28,cut)|thrust_damage(19,cut),imodbits_weapon,[],[fac.kingdom_5]],

    ["military_cleaver_b","Military Cleaver",[("military_cleaver_b",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sabre_1h|itcf_carry_sword_left_hip,222,abundance(100)|weight(1.30)|difficulty(8)|spd_rtng(103)|weapon_length(90)|swing_damage(23,cut),imodbits_weapon,[],[fac.kingdom_5]],
    ["military_cleaver_c","Rhodok Cleaver",[("military_cleaver_c",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sabre_1h|itcf_carry_sword_left_hip,386,abundance(80)|weight(1.40)|difficulty(9)|spd_rtng(101)|weapon_length(92)|swing_damage(27,cut),imodbits_weapon,[],[fac.kingdom_5]],
    ["short_cleaver","Short Cleaver",[("bb_fight_cleaver_a",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sabre_1h|itcf_carry_sword_left_hip,75,abundance(120)|weight(1.00)|difficulty(0)|spd_rtng(112)|weapon_length(66)|swing_damage(18,cut),imodbits_weapon,[],[fac.kingdom_5]],
    ["spearman_cleaver","Spearman Cleaver",[("bb_fight_cleaver_b",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sabre_1h|itcf_carry_sword_left_hip,120,abundance(110)|weight(1.20)|difficulty(0)|spd_rtng(109)|weapon_length(74)|swing_damage(20,cut),imodbits_weapon,[],[fac.kingdom_5]],
    ["battle_cleaver","Battle Cleaver",[("bb_war_cleaver",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary,itc_sabre_1h|itcf_carry_sword_left_hip,595,abundance(60)|weight(1.60)|difficulty(10)|spd_rtng(100)|weapon_length(96)|swing_damage(30,cut),imodbits_weapon,[],[fac.kingdom_5]],
    ["arbalestier_blade","Praying Mantis",[("luc1_praying_mantis_sword_b",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip,886,abundance(15)|weight(1.70)|difficulty(14)|spd_rtng(113)|weapon_length(76)|swing_damage(35,cut)|thrust_damage(21,cut),imodbits_weapon,[],[fac.kingdom_5]],

    ["arabian_sword_d","Desert Sword",[("arabian_sword_d",0),("scab_arabian_sword_d",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,262,abundance(70)|weight(1.40)|difficulty(8)|spd_rtng(98)|weapon_length(100)|swing_damage(21,cut)|thrust_damage(16,pierce),imodbits_weapon,[],[]],
    ["arabian_sword_a","Sarranid Sword",[("arabian_sword_a",0),("scab_arabian_sword_a",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,382,abundance(60)|weight(1.50)|difficulty(9)|spd_rtng(100)|weapon_length(100)|swing_damage(24,cut)|thrust_damage(18,pierce),imodbits_weapon,[],[fac.kingdom_6]],
    ["arabian_sword_b","Sarranid Noble Sword",[("arabian_sword_b",0),("scab_arabian_sword_b",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,578,abundance(50)|weight(1.60)|difficulty(11)|spd_rtng(101)|weapon_length(100)|swing_damage(28,cut)|thrust_damage(19,pierce),imodbits_weapon,[],[fac.kingdom_6]],
    ["arabian_sword_c","Sarranid Elite Sword",[("arabian_sword_c",0),("scab_arabian_sword_c",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_secondary,itc_sword_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,868,abundance(40)|weight(1.40)|difficulty(12)|spd_rtng(99)|weapon_length(105)|swing_damage(32,cut)|thrust_damage(22,pierce),imodbits_weapon,[],[fac.kingdom_6]],

    ["scimitar","Scimitar",[("scimitar_a",0),("scab_scimeter_a",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sabre_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,280,abundance(90)|weight(1.50)|difficulty(9)|spd_rtng(110)|weapon_length(98)|swing_damage(23,cut),imodbits_weapon,[],[]],
    ["scimitar_b","Sarranid Scimitar",[("scimitar_b",0),("scab_scimeter_b",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sabre_1h|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,420,abundance(90)|weight(1.60)|difficulty(10)|spd_rtng(111)|weapon_length(102)|swing_damage(27,cut),imodbits_weapon,[],[fac.kingdom_6]],
    ["sarranid_scimitar_royal","Sultan Hakim's Warblade",[("luc1_sarranid_falchion",0)],itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary,itc_sabre_1h|itcf_carry_sword_left_hip,1851,abundance(0)|weight(1.50)|difficulty(15)|spd_rtng(120)|weapon_length(96)|swing_damage(41,cut),imodbits_weapon,[],[fac.kingdom_6]],
    ["scimitar_c","Sarranid Blade",[("luc1_sarranid_falchion_m2",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sabre_1h|itcf_carry_sword_left_hip,678,abundance(70)|weight(1.50)|difficulty(12)|spd_rtng(108)|weapon_length(98)|swing_damage(32,cut),imodbits_weapon,[],[fac.kingdom_6]],
    ["sarranid_warblade","Sarranid Warblade",[("luc2_great_scimitar",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary,itc_sabre_1h|itcf_carry_sword_back,1088,abundance(50)|weight(1.70)|difficulty(13)|spd_rtng(103)|weapon_length(106)|swing_damage(36,cut),imodbits_weapon,[],[fac.kingdom_6]],

    # INFANTRY WEAPONS: ONE-HANDED

    ["slavers_club","Slavers' Club",[("mackie_great_lakes_mace",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_can_knock_down|itp_wooden_parry,itc_sabre_1h|itcf_carry_sword_left_hip,237,abundance(60)|weight(1.00)|difficulty(0)|spd_rtng(106)|weapon_length(55)|swing_damage(18,blunt),imodbits_weapon,[],[fac.outlaws]],
    ["winged_mace","Iron Flanged Mace",[("flanged_mace",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sabre_1h|itcf_carry_mace_left_hip,274,abundance(90)|weight(1.30)|difficulty(8)|spd_rtng(96)|weapon_length(70)|swing_damage(22,blunt),imodbits_weapon,[],[]],
    ["knobbed_mace","Knobbed Mace",[("mace_a",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_wooden_parry,itc_sabre_1h|itcf_carry_mace_left_hip,296,abundance(90)|weight(1.30)|difficulty(8)|spd_rtng(95)|weapon_length(70)|swing_damage(23,blunt),imodbits_weapon,[],[]],
    ["flanged_mace","Flanged Mace",[("mace_b",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_wooden_parry,itc_sabre_1h|itcf_carry_mace_left_hip,319,abundance(90)|weight(1.30)|difficulty(8)|spd_rtng(94)|weapon_length(70)|swing_damage(24,blunt),imodbits_weapon,[],[]],
    ["spiked_mace","Spiked Mace",[("mace_c",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_wooden_parry,itc_sabre_1h|itcf_carry_mace_left_hip,290,abundance(90)|weight(1.30)|difficulty(8)|spd_rtng(93)|weapon_length(70)|swing_damage(23,blunt),imodbits_weapon,[],[]],
    ["spiked_club","Spiked Club",[("mace_d",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_wooden_parry,itc_sabre_1h|itcf_carry_mace_left_hip,215,abundance(90)|weight(1.10)|difficulty(0)|spd_rtng(101)|weapon_length(70)|swing_damage(19,blunt),imodbits_weapon,[],[]],
    ["lineman_mace","Iron Spiked Mace",[("spiked_mace_new",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sabre_1h|itcf_carry_mace_left_hip,395,abundance(90)|weight(1.40)|difficulty(9)|spd_rtng(92)|weapon_length(70)|swing_damage(27,blunt),imodbits_weapon,[],[]],
    ["mace_small_d","Steel Mace",[("mace_small_d",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary,itc_sabre_1h|itcf_carry_mace_left_hip,513,abundance(70)|weight(1.50)|difficulty(10)|spd_rtng(94)|weapon_length(70)|swing_damage(28,blunt),imodbits_weapon,[],[]],
    ["winged_mace_b","Winged Mace",[("luc1_winged_mace_2h",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_wooden_parry,itc_sabre_1h|itcf_carry_mace_left_hip,487,abundance(80)|weight(1.30)|difficulty(8)|spd_rtng(93)|weapon_length(83)|swing_damage(26,blunt),imodbits_weapon,[],[]],
    ["slavers_mace","Slaver's Bronze Mace",[("luc2_saracen_mace",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_can_knock_down|itp_crush_through|itp_wooden_parry,itc_sabre_1h|itcf_carry_mace_left_hip,983,abundance(40)|weight(1.20)|difficulty(10)|spd_rtng(98)|weapon_length(85)|swing_damage(26,blunt),imodbits_weapon,[],[fac.outlaws]],
    ["sarranid_mace","Sarranid Mace",[("luc1_flanged_two_handed",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_wooden_parry,itc_sabre_1h|itcf_carry_mace_left_hip,748,abundance(60)|weight(1.40)|difficulty(11)|spd_rtng(90)|weapon_length(90)|swing_damage(29,blunt),imodbits_weapon,[],[fac.kingdom_6]],
    ["priest_mace","Priest Mace",[("mace_long_d",0)],itp_type_one_handed_wpn|itp_primary|itp_can_knock_down,itc_sabre_1h|itcf_carry_mace_left_hip,1559,abundance(20)|weight(1.70)|difficulty(15)|spd_rtng(92)|weapon_length(97)|swing_damage(32,blunt),imodbits_weapon,[],[fac.kingdom_1]],
    ["club_with_spike_head","Mace with a Spike",[("mace_e",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_wooden_parry,itc_sword_1h|itcf_carry_sword_left_hip,397,abundance(80)|weight(1.30)|difficulty(9)|spd_rtng(100)|weapon_length(104)|swing_damage(20,blunt)|thrust_damage(17,pierce),imodbits_weapon,[],[]],
    #
    #
    #
    #
    #

    ["hammer","Iron Hammer",[("iron_hammer_new",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_can_knock_down|itp_crush_through|itp_wooden_parry,itc_sabre_1h|itcf_carry_axe_left_hip,178,abundance(80)|weight(1.20)|difficulty(0)|spd_rtng(105)|weapon_length(53)|swing_damage(16,blunt),imodbits_weapon,[],[]],
    #
    #
    #
    #
    #

    # IMPROVISED AND CIVILIAN WEAPONS

    ["dagger","Dagger",[("dagger_b",0),("dagger_b_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_extra_penetration|itp_no_parry,itc_dagger|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,60,abundance(70)|weight(0.50)|difficulty(0)|spd_rtng(126)|weapon_length(35)|swing_damage(14,cut)|thrust_damage(15,pierce),imodbits_weapon,[],[]],
    ["military_sickle","Military Sickle",[("military_sickle_a",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_crush_through|itp_penalty_with_shield|itp_wooden_parry,itc_sabre_1h|itcf_carry_axe_back,120,abundance(40)|weight(1.80)|difficulty(9)|spd_rtng(92)|weapon_length(73)|swing_damage(21,cut),imodbits_weapon,[],[]],
    ["scythe","Scythe",[("luc3_peasant_scythe_no1",0)],itp_type_polearm|itp_two_handed|itp_merchandise|itp_primary|itp_crush_through|itp_cant_use_on_horseback|itp_unbalanced|itp_wooden_parry,itc_poleaxe|itcf_carry_spear,190,abundance(40)|weight(2.00)|difficulty(0)|spd_rtng(83)|weapon_length(130)|swing_damage(23,cut),imodbits_weapon,[],[]],
    ["pitch_fork","Pitchfork",[("luc1_fork_pitch",0)],itp_type_polearm|itp_two_handed|itp_merchandise|itp_primary|itp_wooden_parry,itc_pike|itcf_carry_spear,110,abundance(40)|weight(1.90)|difficulty(0)|spd_rtng(96)|weapon_length(150)|thrust_damage(17,pierce),imodbits_weapon,[],[]],
    ["pickaxe","Pickaxe",[("bb_pickaxe_1_bigger",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_extra_penetration|itp_penalty_with_shield|itp_unbalanced|itp_wooden_parry,itc_sabre_1h|itcf_carry_axe_left_hip,50,abundance(50)|weight(1.60)|difficulty(10)|spd_rtng(92)|weapon_length(65)|swing_damage(13,pierce),imodbits_weapon,[],[]],
    ["iron_staff","Iron Staff",[("luc2_iron_staff",0)],itp_type_polearm|itp_two_handed|itp_merchandise|itp_primary|itp_can_knock_down,itc_staff|itcf_carry_spear,350,abundance(20)|weight(2.20)|difficulty(11)|spd_rtng(108)|weapon_length(127)|swing_damage(25,blunt)|thrust_damage(16,blunt),imodbits_weapon,[],[]],
    ["staff","Quarterstaff",[("luc2_wooden_staff",0)],itp_type_polearm|itp_two_handed|itp_merchandise|itp_primary|itp_can_knock_down|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_spear,200,abundance(100)|weight(1.40)|difficulty(0)|spd_rtng(124)|weapon_length(127)|swing_damage(18,blunt)|thrust_damage(15,blunt),imodbits_weapon,[],[]],

    ["peasant_knife","Peasant Knife",[("peasant_knife_new",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry,itc_cleaver|itcf_carry_dagger_front_right,25,abundance(100)|weight(0.40)|difficulty(0)|spd_rtng(125)|weapon_length(40)|swing_damage(13,cut),imodbits_weapon,[],[]],
    ["butchering_knife","Butchering Knife",[("khyber_knife_new",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_unbalanced,itc_dagger|itcf_carry_dagger_front_right,45,abundance(100)|weight(0.50)|difficulty(0)|spd_rtng(119)|weapon_length(60)|swing_damage(15,cut)|thrust_damage(10,pierce),imodbits_weapon,[],[]],
    ["cleaver","Cleaver",[("cleaver_new",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry,itc_cleaver|itcf_carry_sword_left_hip,45,abundance(100)|weight(0.90)|difficulty(0)|spd_rtng(100)|weapon_length(35)|swing_damage(20,cut),imodbits_weapon,[],[]],
    ["wooden_stick","Wooden Stick",[("wooden_stick",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack,itc_sabre_1h|itcf_carry_mace_left_hip,20,abundance(100)|weight(0.60)|difficulty(0)|spd_rtng(109)|weapon_length(62)|swing_damage(12,blunt),imodbits_none,[],[]],
    ["club","Club",[("lav_club",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack,itc_sabre_1h|itcf_carry_sword_left_hip,40,abundance(100)|weight(0.90)|difficulty(0)|spd_rtng(105)|weapon_length(66)|swing_damage(15,blunt),imodbits_none,[],[]],
    ["cudgel","Cudgel",[("lav_cudgel",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack,itc_sabre_1h|itcf_carry_sword_left_hip,85,abundance(100)|weight(1.00)|difficulty(0)|spd_rtng(108)|weapon_length(66)|swing_damage(19,blunt),imodbits_none,[],[]],
    ["smith_hammer","Blacksmith Hammer",[("bb_smith_hammer",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_wooden_parry,itc_sabre_1h|itcf_carry_axe_left_hip,35,abundance(100)|weight(0.70)|difficulty(0)|spd_rtng(102)|weapon_length(48)|swing_damage(14,blunt),imodbits_weapon,[],[]],
    ["hatchet","Hatchet",[("bb_serbian_hatchet",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry,itc_sabre_1h|itcf_carry_axe_left_hip,65,abundance(100)|weight(1.20)|difficulty(0)|spd_rtng(106)|weapon_length(49)|swing_damage(19,cut),imodbits_weapon,[],[]],
    ["beef_splitter","Beef Splitter",[("mackie_beefsplitter01",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield|itp_penalty_with_shield|itp_unbalanced,itc_sabre_1h|itcf_carry_sword_left_hip,130,abundance(100)|weight(2.00)|difficulty(10)|spd_rtng(89)|weapon_length(79)|swing_damage(24,cut),imodbits_weapon,[],[]],
    ["broken_bottle","Broken Bottle",[("pellagus_broken_bottle",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry,itc_dagger|itcf_carry_dagger_front_right,15,abundance(100)|weight(0.10)|difficulty(0)|spd_rtng(114)|weapon_length(30)|swing_damage(12,cut)|thrust_damage(10,cut),imodbits_none,[],[]],
    ["sickle","Sickle",[("lav_sickle",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary,itc_sabre_1h|itcf_carry_sword_left_hip,45,abundance(100)|weight(0.40)|difficulty(0)|spd_rtng(112)|weapon_length(52)|swing_damage(18,cut),imodbits_none,[],[]],

    # EXOTIC AND WEIRD WEAPONRY

    #
    ["warbrand","Warbrand",[("luc3_warbrand_no1",0)],itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_secondary,itc_sword_2h|itcf_carry_sword_back,3045,abundance(5)|weight(1.80)|difficulty(18)|spd_rtng(110)|weapon_length(111)|swing_damage(49,cut)|thrust_damage(21,pierce),imodbits_weapon,[],[]],
    #

    ["weapons_end", "{!}endmarker", [("invalid_item", 0)], itp_type_goods, 0, 0, weight(1), imodbits_none], 

    ["items_end", "{!}endmarker", [("invalid_item",0)], itp_type_goods, 0, 0, weight(1), imodbits_none],

]

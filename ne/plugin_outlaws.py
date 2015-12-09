from compiler import *
register_plugin()

from random import random

def wpex(*argl):
	argl = map(lambda x: int((random() * 0.2 + 0.9) * x), argl)
	n = 0
	n |= wp_one_handed(argl[0])
	n |= wp_two_handed(argl[1])
	n |= wp_polearm(argl[2])
	n |= wp_archery(argl[3])
	n |= wp_crossbow(argl[4])
	n |= wp_throwing(argl[5])
	return n

swadian_face_younger_1 = 0x0000000000002001355335371861249200000000001c96520000000000000000
swadian_face_young_1   = 0x00000004400023c1355335371861249200000000001c96520000000000000000
swadian_face_middle_1  = 0x00000008000023c1355335371861249200000000001c96520000000000000000
swadian_face_old_1     = 0x0000000e000023c0355335371861249200000000001c96520000000000000000
swadian_face_older_1   = 0x0000000fc00023c0355335371861249200000000001c96520000000000000000

swadian_face_younger_2 = 0x000000003a0045c549fddefdffffffff00000000001e6db60000000000000000
swadian_face_young_2   = 0x000000033a0045c549fddefdffffffff00000000001e6db60000000000000000
swadian_face_middle_2  = 0x00000007ba0045c549fddefdffffffff00000000001e6db60000000000000000
swadian_face_old_2     = 0x0000000e3b0045c549fddefdffffffff00000000001e6db60000000000000000
swadian_face_older_2   = 0x0000000ffa0045c549fddefdffffffff00000000001e6db60000000000000000

vaegir_face_younger_1 = 0x000000001d001141044c21928821245200000000001d22190000000000000000
vaegir_face_young_1   = 0x000000029b001181044c21928821245200000000001d22190000000000000000
vaegir_face_middle_1  = 0x000000075f001181044c21928821245200000000001d22190000000000000000
vaegir_face_old_1     = 0x0000000e1f001181044c21928821245200000000001d22190000000000000000
vaegir_face_older_1   = 0x0000000fdf001180044c21928821245200000000001d22190000000000000000

vaegir_face_younger_2 = 0x0000000037002189497e97cb5fb27fff00000000001ff8370000000000000000
vaegir_face_young_2   = 0x0000000477002249497e97cb5fb27fff00000000001ff8370000000000000000
vaegir_face_middle_2  = 0x0000000877002349497e97cb5fb27fff00000000001ff8370000000000000000
vaegir_face_old_2     = 0x0000000e37002349497e97cb5fb27fff00000000001ff8370000000000000000
vaegir_face_older_2   = 0x0000000ff7002349497e97cb5fb27fff00000000001ff8370000000000000000

khergit_face_younger_1 = 0x00000000190830ca209d69b4100906da00000000001e10e30000000000000000
khergit_face_young_1   = 0x00000003590830ca209d69b4100906da00000000001e10e30000000000000000
khergit_face_middle_1  = 0x00000007d90830ca209d69b4100906da00000000001e10e30000000000000000
khergit_face_old_1     = 0x0000000e190830ca209d69b4100906da00000000001e10e30000000000000000
khergit_face_older_1   = 0x0000000fd90830ca209d69b4100906da00000000001e10e30000000000000000

khergit_face_younger_2 = 0x000000003f08514d49fff7d86cffffff00000000001ff97f0000000000000000
khergit_face_young_2   = 0x000000047f08514d49fff7d86cffffff00000000001ff97f0000000000000000
khergit_face_middle_2  = 0x00000007bf08514d49fff7d86cffffff00000000001ff97f0000000000000000
khergit_face_old_2     = 0x0000000e3f08518d49fff7d86cffffff00000000001ff97f0000000000000000
khergit_face_older_2   = 0x0000000fff0851cd49fff7d86cffffff00000000001ff97f0000000000000000

nord_face_younger_1 = 0x000000000000014104c200928801249200000000001d24100000000000000000
nord_face_young_1   = 0x000000044000014104c200928801249200000000001d24100000000000000000
nord_face_middle_1  = 0x000000084000014104c200928801249200000000001d24100000000000000000
nord_face_old_1     = 0x0000000e0000014104c200928801249200000000001d24100000000000000000
nord_face_older_1   = 0x0000000e0000014004c200928801249200000000001d24100000000000000000

nord_face_younger_2 = 0x000000002b00218a5bfcbdbb67b7ff7f00000000001eeb6f0000000000000000
nord_face_young_2   = 0x000000036b00234a5bfcbdbb67b7ff7f00000000001eeb6f0000000000000000
nord_face_middle_2  = 0x00000007eb00234a5bfcbdbb67b7ff7f00000000001eeb6f0000000000000000
nord_face_old_2     = 0x0000000deb00234a5bfcbdbb67b7ff7f00000000001eeb6f0000000000000000
nord_face_older_2   = 0x0000000feb0023465bfcbdbb67b7ff7f00000000001eeb6f0000000000000000

rhodok_face_younger_1 = 0x0000000000003144355355370861008200000000001c96520000000000000000
rhodok_face_young_1   = 0x0000000500003141355355370861008200000000001c96520000000000000000
rhodok_face_middle_1  = 0x0000000840003141355355370861008200000000001c96520000000000000000
rhodok_face_old_1     = 0x0000000dc0003192355355370861008200000000001c96520000000000000000
rhodok_face_older_1   = 0x0000000fc0003192355355370861008200000000001c96520000000000000000

rhodok_face_younger_2 = 0x000000003e0040c649fc9e6f54b6dbbf00000000001d7b270000000000000000
rhodok_face_young_2   = 0x000000037e0040c649fc9e6f54b6dbbf00000000001d7b270000000000000000
rhodok_face_middle_2  = 0x000000083e0040c649fc9e6f54b6dbbf00000000001d7b270000000000000000
rhodok_face_old_2     = 0x0000000dfe0040c649fc9e6f54b6dbbf00000000001d7b270000000000000000
rhodok_face_older_2   = 0x0000000ffe0040c649fc9e6f54b6dbbf00000000001d7b270000000000000000

sarranid_face_younger_1 = 0x000000000000710004820c24204c000200000000001d16100000000000000000
sarranid_face_young_1   = 0x000000040000710004820c24204c000200000000001d16100000000000000000
sarranid_face_middle_1  = 0x000000088000710004820c24204c000200000000001d16100000000000000000
sarranid_face_old_1     = 0x0000000e0000718004820c24204c000200000000001d16100000000000000000
sarranid_face_older_1   = 0x0000000fc000718004820c24204c000200000000001d16100000000000000000

sarranid_face_younger_2 = 0x000000003f00714049fefe393fffc7ff00000000001ef96f0000000000000000
sarranid_face_young_2   = 0x000000043f00724049fefe393fffc7ff00000000001ef96f0000000000000000
sarranid_face_middle_2  = 0x00000007bf00728049fefe393fffc7ff00000000001ef96f0000000000000000
sarranid_face_old_2     = 0x0000000e3f00728049fefe393fffc7ff00000000001ef96f0000000000000000
sarranid_face_older_2   = 0x0000000fff00728049fefe393fffc7ff00000000001ef96f0000000000000000

outlaws_hate_factions = [(fac.player_faction, -0.15), (fac.commoners, -0.60), (fac.manhunters, -0.20)]
outlaws_hate_kingdoms = [(fac.player_supporters_faction, -0.05), (fac.kingdom_1, -0.05), (fac.kingdom_2, -0.05), (fac.kingdom_3, -0.05), (fac.kingdom_4, -0.05), (fac.kingdom_5, -0.05), (fac.kingdom_6, -0.05), (fac.dark_knights, -0.02)]
outlaws_hate_outlaws  = [(fac.outlaws_forest, -0.10), (fac.outlaws_tundra, -0.10), (fac.outlaws_mountain, -0.10), (fac.outlaws_steppe, -0.10), (fac.outlaws_highway, -0.10), (fac.outlaws_river, -0.10), ]

factions = [
	("outlaws_forest",   "Forest Bandits",   max_player_rating(-30), 0.5, outlaws_hate_factions + outlaws_hate_kingdoms, [], 0xff0000),
	("outlaws_tundra",   "Tundra Bandits",   max_player_rating(-30), 0.6, outlaws_hate_factions + outlaws_hate_kingdoms, [], 0xff0000),
	("outlaws_mountain", "Mountain Clans",   max_player_rating(-30), 0.4, outlaws_hate_factions + outlaws_hate_kingdoms, [], 0xff0000),
	("outlaws_steppe",   "Steppe Raiders",   max_player_rating(-30), 0.4, outlaws_hate_factions + outlaws_hate_kingdoms, [], 0xff0000),
	("outlaws_highway",  "Highway Robbers",  max_player_rating(-30), 0.5, outlaws_hate_factions + outlaws_hate_kingdoms, [], 0xff0000),
	("outlaws_river",    "River Pirates",    max_player_rating(-30), 0.4, outlaws_hate_factions + outlaws_hate_kingdoms, [], 0xff0000),
	("outlaws_raider",   "Sea Raiders",      max_player_rating(-30), 0.6, outlaws_hate_factions + outlaws_hate_kingdoms + outlaws_hate_outlaws, [], 0xff0000),
	("outlaws_pirate",   "Southern Pirates", max_player_rating(-30), 0.7, outlaws_hate_factions + outlaws_hate_kingdoms + outlaws_hate_outlaws, [], 0xff0000),
	("outlaws_slaver",   "Slavers",          max_player_rating(-30), 0.8, outlaws_hate_factions + outlaws_hate_kingdoms + outlaws_hate_outlaws, [], 0xff0000),
]

troops = [

	["outlaw_forest_a", "Poacher", "Poacher", tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.outlaws_forest, [
		itm.pilgrim_hood,itm.common_hood,itm.common_hood_b,itm.black_hood,itm.wrapping_boots,itm.ankle_boots,itm.linen_tunic,itm.green_tunic,
		itm.hunting_bow,itm.hunting_arrows,itm.arrows,
		itm.butchering_knife,itm.cleaver,itm.club,itm.cudgel,itm.hatchet,itm.skirmisher_pick,itm.shortened_spear,
	], ATTR(10,13,9,5,10), wpex(70,70,70,70,70,70), SKILLS(power_throw=1, power_draw=1, weapon_master=1, athletics=3, tracking=2, spotting=2, ), vaegir_face_younger_1, vaegir_face_older_2],
	["outlaw_forest_b", "Seasoned Poacher", "Seasoned Poacher", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, 0, 0, fac.outlaws_forest, [
		itm.pilgrim_hood,itm.common_hood,itm.common_hood_b,itm.black_hood,itm.padded_coif,itm.fur_hat,itm.wrapping_boots,itm.ankle_boots,itm.hunter_boots,itm.hide_boots,itm.linen_tunic,itm.green_tunic,itm.tunic_with_green_cape,itm.ragged_outfit,itm.pelt_coat,itm.rawhide_coat,
		itm.hunting_bow,itm.short_bow,itm.arrows,itm.broadhead_arrows,
		itm.cudgel,itm.hatchet,itm.sword_medieval_c_small,itm.skirmisher_pick,itm.military_pick,itm.fighting_pick,itm.sword_medieval_b_small,itm.mace_long_c,itm.shortened_spear,itm.boar_spear,itm.spear,
	], ATTR(11,16,10,5,15), wpex(90,90,90,100,100,100), SKILLS(power_throw=2, power_draw=2, weapon_master=2, athletics=4, tracking=3, spotting=3, ), vaegir_face_younger_1, vaegir_face_older_2],
	["outlaw_forest_c", "Forest Bandit", "Forest Bandit", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet, 0, 0, fac.outlaws_forest, [
		itm.padded_coif,itm.fur_hat,itm.skullcap,itm.leather_warrior_cap,itm.wrapping_boots,itm.ankle_boots,itm.hunter_boots,itm.hide_boots,itm.light_leather_boots,itm.leather_boots,itm.green_tunic,itm.tunic_with_green_cape,itm.ragged_outfit,itm.leather_jacket,itm.pelt_coat,itm.rawhide_coat,itm.leather_jerkin,itm.light_leather,
		itm.short_bow,itm.long_bow,itm.broadhead_arrows,itm.piercing_arrows,
		itm.sword_medieval_c_small,itm.sword_norman,itm.crossbowman_pick,itm.fighting_pick,itm.sword_medieval_b_small,itm.sword_viking_a_small,itm.sword_medieval_b,itm.mace_long_c,itm.two_handed_battle_axe_a,itm.voulge_a,itm.shortened_military_scythe,itm.boar_spear,itm.spear,itm.war_spear,
	], ATTR(13,17,12,5,20), wpex(100,100,100,130,130,130), SKILLS(ironflesh=1, power_strike=1, power_throw=2, power_draw=3, weapon_master=3, athletics=5, tracking=4, spotting=3, leadership=1, ), vaegir_face_younger_1, vaegir_face_older_2],
	["outlaw_forest_d", "Forest Bandit Lord", "Forest Bandit Lord", tf_guarantee_all, 0, 0, fac.outlaws_forest, [
		itm.skullcap,itm.leather_warrior_cap,itm.footman_helmet,itm.hide_boots,itm.light_leather_boots,itm.leather_boots,itm.leather_jacket,itm.leather_vest,itm.padded_cloth,itm.aketon_green,itm.leather_jerkin,itm.light_leather,itm.leather_armor,itm.padded_leather,itm.leather_armor_shirt,
		itm.shield_common_round_d,
		itm.long_bow,itm.piercing_arrows,itm.barbed_arrows,
		itm.sword_medieval_c,itm.sword_viking_a_small,itm.sword_viking_b_small,itm.sword_medieval_b,itm.one_handed_battle_axe_a,itm.voulge_a,
	], ATTR(15,19,14,8,26), wpex(120,120,120,160,160,160), SKILLS(ironflesh=3, power_strike=3, power_throw=2, power_draw=4, weapon_master=4, athletics=6, tracking=5, spotting=4, trainer=1, leadership=2, ), vaegir_face_younger_1, vaegir_face_older_2],

	["outlaw_tundra_a", "Smuggler", "Smuggler", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves, 0, 0, fac.outlaws_tundra, [
		itm.pilgrim_hood,itm.black_hood,itm.padded_coif,itm.fur_hat,itm.woolen_cap,itm.woolen_cap_b,itm.hunter_boots,itm.hide_boots,itm.archer_gloves,itm.linen_tunic,itm.red_tunic,itm.green_tunic,itm.blue_tunic,itm.white_tunic,itm.yellow_tunic,itm.nordic_shirt_01,itm.nordic_shirt_02,itm.nordic_shirt_03,itm.nordic_shirt_04,itm.nordic_shirt_05,itm.nordic_shirt_06,
		itm.shield_common_round_c,itm.shield_common_round_d,
		itm.stones,itm.throwing_knives,itm.hunting_bow,itm.hunting_arrows,itm.arrows,itm.hunting_crossbow,itm.hunting_bolts,
		itm.dagger,itm.butchering_knife,itm.cleaver,itm.club,itm.cudgel,itm.hatchet,itm.hammer,
	], ATTR(12,11,6,8,9), wpex(60,60,60,60,60,60), SKILLS(ironflesh=2, weapon_master=1, athletics=3, engineer=1, ), nord_face_younger_1, nord_face_older_2],
	["outlaw_tundra_b", "Plunderer", "Plunderer", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet, 0, 0, fac.outlaws_tundra, [
		itm.pilgrim_hood,itm.black_hood,itm.padded_coif,itm.fur_hat,itm.woolen_cap,itm.woolen_cap_b,itm.hunter_boots,itm.hide_boots,itm.archer_gloves,itm.archer_gloves,itm.archer_vambraces,itm.coarse_tunic,itm.tunic_with_green_cape,itm.ragged_outfit,itm.leather_vest,
		itm.shield_common_round_c,itm.shield_common_kite_e,itm.shield_common_round_a,
		itm.throwing_knives,itm.throwing_daggers,itm.darts,itm.hunting_bow,itm.short_bow,itm.arrows,itm.hunting_crossbow,itm.light_crossbow,itm.bolts,itm.hunting_bolts,
		itm.military_sickle,itm.cudgel,itm.beef_splitter,itm.hammer,itm.spiked_club,itm.sword_medieval_b_small,itm.sword_viking_a_small,itm.sword_medieval_c_small,itm.skirmisher_pick,itm.military_pick,itm.shortened_spear,
	], ATTR(14,13,7,8,14), wpex(80,80,80,80,80,80), SKILLS(ironflesh=2, power_throw=1, power_draw=1, weapon_master=2, shield=1, athletics=4, engineer=1, ), nord_face_younger_1, nord_face_older_2],
	["outlaw_tundra_c", "Taiga Bandit", "Taiga Bandit", tf_guarantee_all_wo_ranged, 0, 0, fac.outlaws_tundra, [
		itm.padded_coif,itm.fur_hat,itm.leather_cap,itm.leather_warrior_cap,itm.skullcap,itm.hunter_boots,itm.hide_boots,itm.light_leather_boots,itm.leather_boots,itm.archer_gloves,itm.archer_vambraces,itm.archer_vambraces,itm.leather_vest,itm.fur_coat,itm.ragged_outfit,itm.leather_jacket,itm.pelt_coat,itm.rawhide_coat,itm.leather_jerkin,
		itm.shield_common_round_c,itm.shield_common_kite_e,itm.shield_common_round_a,
		itm.throwing_daggers,itm.war_darts,itm.javelin,itm.short_bow,itm.long_bow,itm.arrows,itm.broadhead_arrows,itm.light_crossbow,itm.crossbow,itm.bolts,
		itm.military_sickle,itm.beef_splitter,itm.spiked_club,itm.winged_mace,itm.knobbed_mace,itm.flanged_mace,itm.spiked_mace,itm.sword_viking_a_small,itm.sword_viking_b_small,itm.sword_medieval_c_small,itm.sword_norman,itm.skirmisher_pick,itm.military_pick,itm.vaegir_pick,itm.mace_long_c,itm.shortened_military_scythe,itm.shortened_spear,
	], ATTR(15,15,8,9,19), wpex(100,100,100,100,100,100), SKILLS(ironflesh=3, power_throw=2, power_draw=2, weapon_master=3, shield=2, athletics=4, engineer=2, ), nord_face_younger_1, nord_face_older_2],
	["outlaw_tundra_d", "Taiga Ranger", "Taiga Ranger", tf_guarantee_all, 0, 0, fac.outlaws_tundra, [
		itm.leather_warrior_cap,itm.skullcap,itm.vaegir_fur_cap,itm.light_leather_boots,itm.leather_boots,itm.archer_vambraces,itm.leather_jerkin,itm.tribal_warrior_outfit,itm.light_leather,itm.leather_armor,itm.padded_leather,itm.leather_armor_shirt,
		itm.shield_common_kite_e,itm.shield_common_round_a,
		itm.war_darts,itm.javelin,itm.javelin_vae,itm.light_throwing_axes,itm.long_bow,itm.broadhead_arrows,itm.piercing_arrows,itm.crossbow,itm.bolts,itm.piercing_bolts,
		itm.winged_mace,itm.knobbed_mace,itm.flanged_mace,itm.spiked_mace,itm.one_handed_battle_axe_a,itm.sword_viking_b_small,itm.sword_norman,itm.sword_medieval_d,itm.vaegir_pick,itm.mace_long_c,itm.voulge_a,itm.shortened_military_scythe,itm.military_scythe_a,itm.military_scythe_b,
	], ATTR(19,16,9,9,25), wpex(130,130,130,130,130,130), SKILLS(ironflesh=3, power_strike=1, power_throw=3, power_draw=3, weapon_master=4, shield=3, athletics=5, engineer=2, ), nord_face_younger_1, nord_face_older_2],

	["outlaw_mountain_a", "Clansman", "Clansman", tf_guarantee_armor|tf_guarantee_helmet, 0, 0, fac.outlaws_mountain, [
		itm.headcloth,itm.woolen_cap,itm.woolen_cap_b,itm.leather_steppe_cap_a,itm.ankle_boots,itm.nomad_boots,itm.hide_boots,itm.ragged_outfit,itm.tunic_with_green_cape,itm.linen_tunic,itm.nomad_vest,itm.nomad_robe,
		itm.mountain_horse,itm.farm_horse,itm.riding_horse,
		itm.shield_common_heater_a,
		itm.throwing_knives,itm.darts,
		itm.pickaxe,itm.military_sickle,itm.hammer,itm.sword_medieval_c_small,itm.spiked_club,itm.skirmisher_pick,itm.mace_long_c,itm.shortened_military_scythe,itm.shortened_spear,itm.boar_spear,
	], ATTR(12,13,6,6,10), wpex(80,80,80,60,60,60), SKILLS(ironflesh=1, power_strike=2, power_throw=2, weapon_master=1, shield=1, riding=1, spotting=2, ), khergit_face_younger_1, khergit_face_older_2],
	["outlaw_mountain_b", "Clansman Raider", "Clansman Raider", tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_boots, 0, 0, fac.outlaws_mountain, [
		itm.woolen_cap,itm.woolen_cap_b,itm.fur_hat,itm.nomad_cap_b,itm.leather_steppe_cap_a,itm.nomad_boots,itm.hide_boots,itm.light_leather_boots,itm.leather_gloves,itm.nomad_armor,itm.khergit_armor,itm.steppe_armor,itm.leather_vest,itm.nomad_vest,itm.nomad_robe,
		itm.mountain_horse,itm.farm_horse,itm.riding_horse,
		itm.shield_common_heater_a,
		itm.throwing_knives,itm.throwing_daggers,itm.darts,itm.war_darts,
		itm.sword_medieval_c_small,itm.military_sickle,itm.hammer,itm.sword_norman,itm.spiked_club,itm.winged_mace,itm.knobbed_mace,itm.flanged_mace,itm.spiked_mace,itm.skirmisher_pick,itm.military_pick,itm.fighting_pick,itm.bastard_sword_a,itm.mace_long_c,itm.shortened_military_scythe,itm.military_scythe_a,itm.military_scythe_b,itm.shortened_spear,itm.boar_spear,itm.spear,itm.military_fork,itm.battle_fork,
	], ATTR(14,15,7,6,15), wpex(110,110,110,70,70,70), SKILLS(ironflesh=1, power_strike=3, power_throw=2, weapon_master=2, shield=2, riding=2, horse_archery=1, spotting=2, ), khergit_face_younger_1, khergit_face_older_2],
	["outlaw_mountain_c", "Mountain Bandit", "Mountain Bandit", tf_mounted|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_horse, 0, 0, fac.outlaws_mountain, [
		itm.fur_hat,itm.nomad_cap_b,itm.leather_steppe_cap_a,itm.leather_warrior_cap,itm.steppe_cap,itm.khergit_leather_helmet,itm.light_leather_boots,itm.leather_boots,itm.leather_gloves,itm.mail_gauntlets,itm.tribal_warrior_outfit,itm.leather_jerkin,itm.leather_jacket,itm.steppe_armor,
		itm.mountain_horse,itm.courser_horse,itm.hunter_horse,
		itm.shield_common_heater_a,
		itm.throwing_daggers,itm.war_darts,itm.javelin,itm.javelin_khe,itm.javelin_vae,
		itm.sword_norman,itm.sword_medieval_d,itm.khergit_sword_b,itm.winged_mace,itm.knobbed_mace,itm.flanged_mace,itm.spiked_mace,itm.lineman_mace,itm.winged_mace_b,itm.bastard_sword_a,itm.bastard_sword_b,itm.boar_spear,itm.spear,itm.war_spear,itm.military_fork,itm.battle_fork,
	], ATTR(15,16,9,7,20), wpex(150,150,150,80,80,80), SKILLS(ironflesh=1, power_strike=4, power_throw=2, weapon_master=3, shield=2, riding=3, horse_archery=2, spotting=3, ), khergit_face_younger_1, khergit_face_older_2],
	["outlaw_mountain_d", "Mountain Brigand", "Mountain Brigand", tf_guarantee_all_wo_ranged, 0, 0, fac.outlaws_mountain, [
		itm.leather_warrior_cap,itm.steppe_cap,itm.khergit_leather_helmet,itm.vaegir_fur_cap,itm.leather_steppe_cap_b,itm.nomad_cap,itm.leather_boots,itm.khergit_leather_boots,itm.leather_gloves,itm.mail_gauntlets,itm.tribal_warrior_outfit,itm.khergit_leather_a,itm.khergit_leather_b,itm.vaegir_inf_armor_a,itm.lamellar_vest,itm.lamellar_vest_khergit,
		itm.mountain_horse,itm.courser_horse,itm.hunter_horse,
		itm.shield_common_heater_a,
		itm.javelin_khe,itm.javelin_vae,
		itm.sword_medieval_d,itm.sword_medieval_c,itm.sword_medieval_c_long,itm.khergit_sword_b,itm.khergit_sword_a,itm.winged_mace_b,itm.bastard_sword_b,itm.sword_two_handed_b,itm.spear,itm.war_spear,itm.light_lance,
	], ATTR(18,18,11,7,25), wpex(190,190,190,80,80,80), SKILLS(ironflesh=2, power_strike=5, power_throw=2, weapon_master=4, shield=3, riding=4, horse_archery=2, spotting=3, leadership=1, ), khergit_face_younger_1, khergit_face_older_2],

	["outlaw_steppe_a", "Steppe Outcast", "Steppe Outcast", tf_guarantee_armor|tf_guarantee_horse, 0, 0, fac.outlaws_steppe, [
		itm.head_wrappings,itm.head_wrappings,itm.head_wrappings,itm.leather_steppe_cap_a,itm.ankle_boots,itm.nomad_boots,itm.nomad_vest,itm.nomad_robe,itm.ragged_outfit,
		itm.farm_horse,itm.riding_horse,
		itm.darts,itm.hunting_bow_khe,itm.short_bow_khe,itm.hunting_bow_sar,itm.short_bow_sar,itm.arrows,itm.broadhead_arrows,
		itm.club,itm.cudgel,itm.sword_norman,itm.winged_mace,itm.knobbed_mace,itm.flanged_mace,itm.spiked_mace,itm.shortened_spear,
	], ATTR(11,13,5,6,8), wpex(60,60,60,70,70,70), SKILLS(power_throw=2, power_draw=2, weapon_master=1, riding=2, horse_archery=3, spotting=1, ), khergit_face_younger_1, khergit_face_older_2],
	["outlaw_steppe_b", "Steppe Bandit", "Steppe Bandit", tf_mounted|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_ranged, 0, 0, fac.outlaws_steppe, [
		itm.head_wrappings,itm.leather_steppe_cap_a,itm.nomad_cap_b,itm.steppe_cap,itm.nomad_boots,itm.hide_boots,itm.light_leather_boots,itm.nomad_armor,itm.nomad_vest,itm.khergit_armor,itm.light_leather,itm.leather_vest,itm.padded_cloth,itm.aketon_green,
		itm.riding_horse,itm.khergit_horse,
		itm.khergit_shield_a1,itm.khergit_shield_a2,itm.khergit_shield_a3,itm.hera_sarranid_small_shield_a,
		itm.darts,itm.war_darts,itm.short_bow_khe,itm.nomad_bow_khe,itm.short_bow_sar,itm.nomad_bow_sar,itm.arrows,itm.broadhead_arrows,itm.piercing_arrows,itm.barbed_arrows,
		itm.arabian_sword_d,itm.sword_norman,itm.sword_medieval_d,itm.khergit_sword_b,itm.winged_mace,itm.knobbed_mace,itm.flanged_mace,itm.spiked_mace,itm.shortened_spear,itm.boar_spear,itm.spear,
	], ATTR(13,14,7,6,13), wpex(80,80,80,100,100,100), SKILLS(power_throw=3, power_draw=3, weapon_master=2, shield=1, riding=3, horse_archery=4, spotting=1, ), khergit_face_younger_1, khergit_face_older_2],
	["outlaw_steppe_c", "Steppe Raider", "Steppe Raider", tf_mounted|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_ranged, 0, 0, fac.outlaws_steppe, [
		itm.nomad_cap_b,itm.steppe_cap,itm.khergit_leather_helmet,itm.leather_steppe_cap_b,itm.light_leather_boots,itm.leather_boots,itm.khergit_leather_boots,itm.tribal_warrior_outfit,itm.steppe_armor,itm.light_leather,itm.leather_armor,
		itm.khergit_horse,itm.courser_horse,itm.hunter_horse,
		itm.khergit_shield_a1,itm.khergit_shield_a2,itm.khergit_shield_a3,itm.hera_sarranid_small_shield_a,
		itm.war_darts,itm.javelin,itm.javelin_khe,itm.javelin_sar,itm.nomad_bow_khe,itm.strong_bow_khe,itm.nomad_bow_sar,itm.strong_bow_sar,itm.broadhead_arrows,itm.piercing_arrows,itm.barbed_arrows,
		itm.arabian_sword_d,itm.arabian_sword_a,itm.scimitar,itm.sword_medieval_d,itm.sword_medieval_c,itm.khergit_sword_b,itm.khergit_sword_a,itm.spear,itm.war_spear,itm.light_lance,
	], ATTR(14,17,8,6,18), wpex(100,100,100,130,130,130), SKILLS(power_strike=1, power_throw=3, power_draw=4, weapon_master=3, shield=1, riding=4, horse_archery=5, spotting=2, ), khergit_face_younger_1, khergit_face_older_2],
	["outlaw_steppe_d", "Steppe Raider Khan", "Steppe Raider Khan", tf_guarantee_all, 0, 0, fac.outlaws_steppe, [
		itm.khergit_leather_helmet,itm.leather_steppe_cap_b,itm.nomad_cap,itm.khergit_cavalry_helmet,itm.khergit_leather_boots,itm.steppe_armor,itm.tribal_warrior_outfit,itm.lamellar_vest,itm.lamellar_vest_khergit,itm.khergit_leather_a,itm.khergit_leather_b,
		itm.courser_horse,itm.hunter_horse,itm.armored_courser,itm.armored_hunter,itm.khergit_warhorse_a,
		itm.khergit_shield_a1,itm.khergit_shield_a2,itm.khergit_shield_a3,itm.hera_sarranid_small_shield_b,itm.hera_sarranid_small_shield_c,
		itm.javelin_khe,itm.javelin_sar,itm.strong_bow_khe,itm.strong_bow_sar,itm.khergit_arrows_a,itm.bodkin_arrows,itm.khergit_arrows_b,
		itm.arabian_sword_a,itm.scimitar,itm.khergit_sword_a,itm.khergit_sword_c,itm.sword_medieval_c,itm.scimitar_b,itm.light_lance,itm.khergit_lance_a,
	], ATTR(17,19,9,9,24), wpex(140,140,140,140,140,140), SKILLS(ironflesh=3, power_strike=1, power_throw=4, power_draw=5, weapon_master=4, shield=2, riding=5, horse_archery=6, spotting=2, ), khergit_face_younger_1, khergit_face_older_2],

	["outlaw_highway_a", "Outlaw", "Outlaw", tf_guarantee_armor, 0, 0, fac.outlaws_highway, [
		itm.head_wrappings,itm.headcloth,itm.straw_hat,itm.felt_hat,itm.felt_hat_b,itm.turban,itm.desert_turban,itm.arming_cap,itm.woolen_cap,itm.woolen_cap_b,itm.wrapping_boots,itm.woolen_hose,itm.blue_hose,itm.ankle_boots,itm.sarranid_boots_a,itm.linen_tunic,itm.red_tunic,itm.green_tunic,itm.blue_tunic,itm.white_tunic,itm.yellow_tunic,itm.tunic_with_green_cape,itm.ragged_outfit,itm.sarranid_vest_a,itm.sarranid_vest_b,itm.sarranid_vest_a,itm.sarranid_vest_b,itm.tabard,
		itm.shield_common_round_d,
		itm.hunting_crossbow,itm.bolts,itm.hunting_bolts,
		itm.dagger,itm.cleaver,itm.hatchet,itm.cudgel,itm.hammer,itm.skirmisher_pick,
	], ATTR(14,10,6,6,9), wpex(70,70,70,50,50,50), SKILLS(power_strike=2, weapon_master=1, shield=1, athletics=2, spotting=2, ), rhodok_face_younger_1, rhodok_face_older_2],
	["outlaw_highway_b", "Robber", "Robber", tf_guarantee_armor|tf_guarantee_boots, 0, 0, fac.outlaws_highway, [
		itm.felt_hat,itm.padded_coif,itm.leather_cap,itm.felt_hat_b,itm.wrapping_boots,itm.woolen_hose,itm.blue_hose,itm.ankle_boots,itm.sarranid_boots_a,itm.nomad_boots,itm.leather_gloves,itm.ragged_outfit,itm.coarse_tunic,itm.nomad_vest,itm.gambeson,itm.blue_gambeson,itm.red_gambeson,itm.leather_vest,itm.padded_cloth,itm.aketon_green,itm.skirmisher_armor,
		itm.mercenary_shield_a,itm.shield_common_round_d,itm.shield_common_round_a,
		itm.hunting_crossbow,itm.light_crossbow,itm.rhodok_bolts_a,itm.hunting_bolts,itm.rhodok_bolts_a,
		itm.military_sickle,itm.hatchet,itm.hammer,itm.falchion_new,itm.short_cleaver,itm.winged_mace,itm.knobbed_mace,itm.flanged_mace,itm.spiked_mace,itm.spiked_club,itm.skirmisher_pick,itm.military_pick,itm.mace_long_c,itm.voulge_a,itm.shortened_military_scythe,itm.shortened_spear,
	], ATTR(17,11,6,7,14), wpex(90,90,90,60,60,60), SKILLS(power_strike=2, weapon_master=2, shield=2, athletics=3, spotting=3, ), rhodok_face_younger_1, rhodok_face_older_2],
	["outlaw_highway_c", "Highway Robber", "Highway Robber", tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_shield, 0, 0, fac.outlaws_highway, [
		itm.felt_hat_b,itm.leather_cap,itm.padded_coif,itm.sarranid_felt_hat,itm.ankle_boots,itm.sarranid_boots_a,itm.nomad_boots,itm.light_leather_boots,itm.leather_boots,itm.leather_gloves,itm.nomad_vest,itm.leather_jacket,itm.leather_vest,itm.padded_cloth,itm.skirmisher_armor,itm.archers_vest,itm.archers_vest_b,itm.archers_vest_c,itm.archers_vest_d,
		itm.mule,itm.farm_horse,itm.riding_horse,
		itm.shield_common_round_a,itm.mercenary_shield_a,itm.mercenary_shield_a,itm.mercenary_shield_b,
		itm.light_crossbow,itm.rhodok_bolts_a,itm.piercing_bolts,
		itm.military_sickle,itm.falchion_new,itm.heavy_falchion,itm.short_cleaver,itm.arabian_sword_d,itm.arabian_sword_a,itm.winged_mace,itm.knobbed_mace,itm.flanged_mace,itm.spiked_mace,itm.lineman_mace,itm.military_pick,itm.fighting_pick,itm.bastard_sword_a,itm.mace_long_c,itm.mace_long_a,itm.mace_long_b,itm.voulge_a,itm.glaive,itm.voulge_b,itm.shortened_military_scythe,itm.military_scythe_a,itm.military_scythe_b,itm.shortened_spear,itm.boar_spear,
	], ATTR(18,13,7,8,19), wpex(120,120,120,70,70,70), SKILLS(power_strike=3, power_throw=1, weapon_master=3, shield=3, athletics=4, riding=1, spotting=3, ), rhodok_face_younger_1, rhodok_face_older_2],
	["outlaw_highway_d", "Highwayman", "Highwayman", tf_mounted|tf_guarantee_all_wo_ranged, 0, 0, fac.outlaws_highway, [
		itm.sarranid_felt_hat,itm.rhodok_infantry_cap,itm.rhodok_kettle_hat,itm.sarranid_helmet1,itm.sarranid_spiked_helmet,itm.leather_boots,itm.khergit_leather_boots,itm.sarranid_boots_b,itm.leather_gloves,itm.mail_gauntlets,itm.light_leather,itm.leather_armor,itm.padded_leather,itm.leather_jerkin,itm.leather_vest,itm.padded_cloth,itm.leather_jacket,itm.archers_vest,itm.archers_vest_b,itm.archers_vest_c,itm.archers_vest_d,itm.sarranid_leather_vest,itm.sarranid_leather_armor,
		itm.riding_horse,itm.khergit_horse,itm.sarranid_horse_a,itm.sarranid_horse_b,
		itm.mercenary_shield_b,itm.mercenary_shield_c,
		itm.light_crossbow,itm.crossbow,itm.piercing_bolts,itm.rhodok_bolts_b,
		itm.military_cleaver_b,itm.winged_mace_b,itm.lineman_mace,itm.arabian_sword_a,itm.bastard_sword_a,itm.bastard_sword_b,itm.sword_two_handed_b,itm.mace_long_a,itm.mace_long_b,itm.two_handed_battle_axe_a,itm.voulge_a,itm.military_scythe_b,
	], ATTR(22,14,8,9,24), wpex(160,160,160,70,70,70), SKILLS(power_strike=3, power_throw=1, weapon_master=4, shield=4, athletics=4, riding=2, spotting=4, trainer=1, ), rhodok_face_younger_1, rhodok_face_older_2],

	["outlaw_river_a", "River Pirate Young", "River Pirate Young", tf_guarantee_boots|tf_guarantee_ranged, 0, 0, fac.outlaws_river, [
		itm.wrapping_boots,itm.red_tunic,itm.green_tunic,itm.blue_tunic,itm.blue_gambeson,itm.red_gambeson,itm.leather_jacket,
		itm.stones,
		itm.dagger,itm.staff,itm.butchering_knife,itm.cleaver,itm.club,itm.cudgel,itm.hatchet,
	], ATTR(9,10,7,7,6), wpex(50,50,50,60,60,60), SKILLS(power_strike=1, power_throw=2, weapon_master=1, ), swadian_face_younger_1, swadian_face_older_2],
	["outlaw_river_b", "River Pirate", "River Pirate", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves, 0, 0, fac.outlaws_river, [
		itm.leather_cap,itm.wrapping_boots,itm.woolen_hose,itm.blue_hose,itm.ankle_boots,itm.leather_gloves,itm.ragged_outfit,itm.gambeson,itm.blue_gambeson,itm.red_gambeson,itm.padded_cloth,itm.aketon_green,
		itm.shield_common_round_d,
		itm.stones,itm.throwing_knives,
		itm.hatchet,itm.hammer,itm.sword_medieval_c_small,itm.falchion_new,itm.skirmisher_pick,
	], ATTR(11,12,7,8,11), wpex(80,80,80,70,70,70), SKILLS(power_strike=2, power_throw=2, weapon_master=2, shield=1, athletics=1, ), swadian_face_younger_1, swadian_face_older_2],
	["outlaw_river_c", "River Pirate Boatswain", "River Pirate Boatswain", tf_guarantee_all_wo_ranged, 0, 0, fac.outlaws_river, [
		itm.leather_cap,itm.skullcap,itm.ankle_boots,itm.leather_gloves,itm.padded_cloth,itm.aketon_green,itm.leather_vest,
		itm.shield_common_round_d,itm.shield_common_round_a,
		itm.throwing_knives,itm.throwing_daggers,
		itm.sword_medieval_c_small,itm.falchion_new,itm.sword_norman,itm.heavy_falchion,itm.military_pick,itm.mace_long_c,itm.shortened_spear,
	], ATTR(13,13,8,9,16), wpex(110,110,110,80,80,80), SKILLS(power_strike=3, power_throw=3, weapon_master=3, shield=2, athletics=2, trainer=1, leadership=1, ), swadian_face_younger_1, swadian_face_older_2],
	["outlaw_river_d", "River Pirate Captain", "River Pirate Captain", tf_guarantee_all_wo_ranged, 0, 0, fac.outlaws_river, [
		itm.rhodok_kettle_hat,itm.rhodok_army_cap,itm.segmented_helmet,itm.light_leather_boots,itm.leather_boots,itm.mail_gauntlets,itm.padded_cloth,itm.aketon_green,itm.leather_vest,itm.light_leather,itm.leather_armor,
		itm.mercenary_shield_a,
		itm.throwing_daggers,
		itm.sword_medieval_d,itm.sword_medieval_c,itm.sword_medieval_c_long,itm.fighting_pick,itm.bastard_sword_a,
	], ATTR(14,16,9,10,22), wpex(140,140,140,100,100,100), SKILLS(ironflesh=2, power_strike=4, power_throw=4, weapon_master=4, shield=3, athletics=2, trainer=1, leadership=3, ), swadian_face_younger_1, swadian_face_older_2],

	["outlaw_raider_a", "Sea Raider Rookie", "Sea Raider Rookie", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, 0, 0, fac.outlaws_raider, [
		itm.woolen_cap,itm.woolen_cap_b,itm.fur_hat,itm.hunter_boots,itm.hide_boots,itm.light_leather,itm.leather_armor,itm.padded_leather,itm.leather_armor_shirt,itm.studded_leather_coat,
		itm.norman_shield_2,itm.norman_shield_4,itm.norman_shield_8,
		itm.light_throwing_axes,itm.hunting_bow_nor,itm.short_bow_nor,itm.arrows,itm.broadhead_arrows,
		itm.hammer,itm.hatchet,itm.one_handed_battle_axe_a,itm.two_handed_battle_axe_a,itm.voulge_a,
	], ATTR(16,10,8,6,12), wpex(70,70,70,90,90,90), SKILLS(power_strike=2, power_throw=2, power_draw=2, weapon_master=1, shield=2, athletics=2, spotting=1, engineer=1, ), nord_face_younger_1, nord_face_older_2],
	["outlaw_raider_b", "Sea Raider", "Sea Raider", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, 0, 0, fac.outlaws_raider, [
		itm.woolen_cap,itm.woolen_cap_b,itm.fur_hat,itm.skullcap,itm.nordic_archer_helmet,itm.hunter_boots,itm.hide_boots,itm.light_leather_boots,itm.leather_boots,itm.leather_gloves,itm.mail_gauntlets,itm.leather_armor_shirt,itm.studded_leather_coat,itm.nordic_archer_armor_a,itm.nordic_archer_armor_b,itm.nordic_archer_armor_c1,itm.nordic_archer_armor_c2,itm.raider_hauberk_a,itm.raider_hauberk_b,itm.raider_hauberk_c,
		itm.norman_shield_2,itm.norman_shield_4,itm.norman_shield_8,
		itm.light_throwing_axes,itm.throwing_axes,itm.short_bow_nor,itm.long_bow_nor,itm.broadhead_arrows,itm.piercing_arrows,
		itm.sword_medieval_b,itm.one_handed_battle_axe_a,itm.one_handed_battle_axe_c,itm.one_handed_war_axe_a,itm.two_handed_battle_axe_a,itm.two_handed_battle_axe_b,itm.two_handed_battle_axe_e,itm.voulge_a,
	], ATTR(19,11,9,6,17), wpex(100,100,100,100,100,100), SKILLS(ironflesh=1, power_strike=3, power_throw=2, power_draw=2, weapon_master=2, shield=3, athletics=3, spotting=1, engineer=1, ), nord_face_younger_1, nord_face_older_2],
	["outlaw_raider_c", "Veteran Sea Raider", "Veteran Sea Raider", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield, 0, 0, fac.outlaws_raider, [
		itm.skullcap,itm.nordic_archer_helmet,itm.nordic_veteran_archer_helmet,itm.nordic_skullcap,itm.light_leather_boots,itm.leather_boots,itm.splinted_greaves,itm.leather_gloves,itm.mail_gauntlets,itm.mail_mittens,itm.nordic_archer_armor_a,itm.nordic_archer_armor_b,itm.nordic_archer_armor_c1,itm.nordic_archer_armor_c2,itm.raider_hauberk_a,itm.raider_hauberk_b,itm.raider_hauberk_c,itm.nordic_archer_armor_d,itm.byrnie,
		itm.norman_shield_2,itm.norman_shield_4,itm.norman_shield_8,itm.norman_shield_1,itm.norman_shield_3,itm.norman_shield_5,itm.norman_shield_6,itm.norman_shield_7,
		itm.light_throwing_axes,itm.throwing_axes,itm.heavy_throwing_axes,itm.long_bow_nor,itm.broadhead_arrows,itm.piercing_arrows,itm.barbed_arrows,itm.bodkin_arrows,
		itm.sword_medieval_b,itm.sword_viking_c,itm.one_handed_war_axe_a,itm.one_handed_war_axe_b,itm.one_handed_battle_axe_b,itm.two_handed_battle_axe_b,itm.two_handed_battle_axe_e,
	], ATTR(19,13,10,8,22), wpex(140,140,140,110,110,110), SKILLS(ironflesh=2, power_strike=4, power_throw=3, power_draw=3, weapon_master=3, shield=4, athletics=4, spotting=1, engineer=1, leadership=1, ), nord_face_younger_1, nord_face_older_2],
	["outlaw_raider_d", "Sea Raider Chief", "Sea Raider Chief", tf_guarantee_all_wo_ranged, 0, 0, fac.outlaws_raider, [
		itm.norman_helmet,itm.nasal_helmet,itm.spiked_helmet,itm.splinted_greaves,itm.mail_chausses,itm.mail_gauntlets,itm.mail_mittens,itm.scale_gauntlets,itm.nordic_byrnie_1,itm.nordic_byrnie_6,itm.nordic_hauberk_1,itm.nordic_hauberk_4,itm.scale_armor,
		itm.norman_shield_1,itm.norman_shield_3,itm.norman_shield_5,itm.norman_shield_6,itm.norman_shield_7,
		itm.throwing_axes,itm.heavy_throwing_axes,itm.long_bow_nor,itm.barbed_arrows,itm.bodkin_arrows,
		itm.sword_medieval_b,itm.sword_viking_c,itm.sword_viking_c_long,itm.one_handed_battle_axe_b,itm.voulge,
	], ATTR(24,14,11,10,30), wpex(180,180,180,120,120,120), SKILLS(ironflesh=3, power_strike=6, power_throw=3, power_draw=3, weapon_master=4, shield=5, athletics=5, spotting=1, engineer=1, trainer=1, leadership=1, ), nord_face_younger_1, nord_face_older_2],

	["outlaw_pirate_a", "Pirate Young", "Pirate Young", tf_guarantee_boots|tf_guarantee_ranged, 0, 0, fac.outlaws_pirate, [
		itm.head_wrappings,itm.headcloth,itm.woolen_cap,itm.woolen_cap_b,itm.felt_hat_b,itm.wrapping_boots,itm.woolen_hose,itm.blue_hose,itm.ankle_boots,itm.leather_jacket,itm.leather_jerkin,itm.leather_vest,itm.padded_cloth,itm.aketon_green,itm.leather_jerkin,itm.light_leather,
		itm.darts,itm.war_darts,
		itm.dagger,itm.hammer,itm.falchion_new,itm.skirmisher_pick,itm.military_pick,
	], ATTR(9,15,6,7,10), wpex(60,60,60,70,70,70), SKILLS(ironflesh=2, power_throw=2, weapon_master=1, athletics=1, engineer=1, ), rhodok_face_younger_1, rhodok_face_older_2],
	["outlaw_pirate_b", "Pirate", "Pirate", tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.outlaws_pirate, [
		itm.head_wrappings,itm.headcloth,itm.woolen_cap,itm.woolen_cap_b,itm.felt_hat_b,itm.wrapping_boots,itm.ankle_boots,itm.hide_boots,itm.leather_gloves,itm.light_leather,itm.leather_armor,itm.padded_leather,itm.leather_jerkin,itm.leather_armor_shirt,
		itm.mercenary_shield_a,
		itm.javelin,itm.hunting_crossbow,itm.bolts,
		itm.falchion_new,itm.heavy_falchion,itm.short_cleaver,itm.one_handed_battle_axe_a,itm.military_pick,itm.fighting_pick,
	], ATTR(10,19,6,7,15), wpex(100,100,100,70,70,70), SKILLS(ironflesh=3, power_strike=1, power_throw=2, weapon_master=2, shield=1, athletics=1, spotting=1, engineer=2, ), rhodok_face_younger_1, rhodok_face_older_2],
	["outlaw_pirate_c", "Pirate Boarder", "Pirate Boarder", tf_guarantee_all_wo_ranged, 0, 0, fac.outlaws_pirate, [
		itm.padded_coif,itm.leather_cap,itm.skullcap,itm.hide_boots,itm.light_leather_boots,itm.leather_gloves,itm.mail_gauntlets,itm.light_leather,itm.leather_armor,itm.padded_leather,itm.leather_armor_shirt,itm.rhodok_brigandine_vest,
		itm.riding_horse,
		itm.mercenary_shield_a,itm.mercenary_shield_b,
		itm.javelin,itm.hunting_crossbow,itm.light_crossbow,itm.bolts,itm.hunting_bolts,
		itm.short_cleaver,itm.heavy_falchion,itm.military_cleaver_b,itm.one_handed_battle_axe_a,itm.fighting_pick,
	], ATTR(12,21,6,8,20), wpex(130,130,130,80,80,80), SKILLS(ironflesh=4, power_strike=1, power_throw=2, weapon_master=3, shield=2, athletics=2, riding=1, spotting=2, engineer=3, ), rhodok_face_younger_1, rhodok_face_older_2],
	["outlaw_pirate_d", "Pirate Sea Wolf", "Pirate Sea Wolf", tf_mounted|tf_guarantee_all_wo_ranged, 0, 0, fac.outlaws_pirate, [
		itm.skullcap,itm.footman_helmet,itm.segmented_helmet,itm.light_leather_boots,itm.leather_boots,itm.mail_gauntlets,itm.leather_armor_shirt,itm.studded_leather_coat,itm.light_mail_and_plate,itm.haubergeon,itm.rhodok_brigandine_vest,itm.rhodok_archer_armor_b1,itm.rhodok_archer_armor_b2,
		itm.courser_horse,itm.sarranid_horse_a,itm.sarranid_horse_b,
		itm.mercenary_shield_b,itm.mercenary_shield_c,
		itm.javelin,itm.light_crossbow,itm.hunting_bolts,itm.rhodok_bolts_a,
		itm.military_cleaver_b,itm.military_cleaver_c,
	], ATTR(14,26,6,9,27), wpex(160,160,160,80,80,80), SKILLS(ironflesh=5, power_strike=2, power_throw=2, weapon_master=4, shield=3, athletics=2, riding=2, spotting=3, engineer=4, leadership=1, ), rhodok_face_younger_1, rhodok_face_older_2],

	["outlaw_slaver_a", "Slaver", "Slaver", tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.outlaws_slaver, [
		itm.turban,itm.desert_turban,itm.sarranid_boots_a,itm.leather_gloves,itm.sarranid_vest_a,itm.sarranid_vest_b,itm.skirmisher_armor,
		itm.farm_horse,itm.riding_horse,
		itm.shield_common_kite_d,
		itm.stones,
		itm.club,itm.cudgel,itm.smith_hammer,itm.staff,itm.iron_staff,itm.hammer,itm.slavers_club,itm.mace_long_c,itm.mace_long_a,itm.mace_long_b,
	], ATTR(13,14,6,6,11), wpex(60,60,60,60,60,60), SKILLS(power_strike=1, weapon_master=1, shield=2, athletics=3, riding=1, tracking=3, spotting=2, ), sarranid_face_young_1, sarranid_face_middle_2],
	["outlaw_slaver_b", "Slave Hunter", "Slave Hunter", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse, 0, 0, fac.outlaws_slaver, [
		itm.turban,itm.desert_turban,itm.sarranid_felt_hat,itm.sarranid_felt_hat,itm.sarranid_boots_a,itm.sarranid_boots_a,itm.sarranid_boots_b,itm.leather_gloves,itm.skirmisher_armor,itm.archers_vest,itm.archers_vest_b,itm.archers_vest_c,itm.archers_vest_d,
		itm.sarranid_horse_a,itm.sarranid_horse_b,itm.sarranid_camel_a,itm.sarranid_camel_b,
		itm.shield_common_kite_d,
		itm.cudgel,itm.winged_mace,itm.knobbed_mace,itm.flanged_mace,itm.spiked_mace,itm.slavers_club,itm.mace_long_a,itm.mace_long_b,
	], ATTR(16,15,6,7,16), wpex(90,90,90,90,90,90), SKILLS(power_strike=1, weapon_master=2, shield=3, athletics=3, riding=2, tracking=4, spotting=2, ), sarranid_face_young_1, sarranid_face_old_2],
	["outlaw_slaver_c", "Slave Crusher", "Slave Crusher", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet, 0, 0, fac.outlaws_slaver, [
		itm.sarranid_felt_hat,itm.sarranid_helmet1,itm.sarranid_spiked_helmet,itm.sarranid_boots_a,itm.sarranid_boots_b,itm.sarranid_boots_b,itm.leather_gloves,itm.mail_gauntlets,itm.archers_vest,itm.archers_vest_b,itm.archers_vest_c,itm.archers_vest_d,itm.sarranid_leather_vest,itm.sarranid_leather_armor,
		itm.sarranid_camel_a,itm.sarranid_camel_b,itm.heavy_camel_a,itm.heavy_camel_b,
		itm.shield_common_kite_d,
		itm.winged_mace,itm.knobbed_mace,itm.flanged_mace,itm.spiked_mace,itm.slavers_mace,itm.winged_mace_b,itm.mace_long_a,itm.mace_long_b,
	], ATTR(18,16,7,7,21), wpex(120,120,120,120,120,120), SKILLS(power_strike=2, weapon_master=3, shield=4, athletics=3, riding=3, tracking=5, spotting=3, ), sarranid_face_middle_1, sarranid_face_old_2],
	["outlaw_slaver_d", "Slavemaster", "Slavemaster", tf_mounted|tf_guarantee_all_wo_ranged, 0, 0, fac.outlaws_slaver, [
		itm.sarranid_helmet1,itm.sarranid_spiked_helmet,itm.sarranid_warrior_cap,itm.sarranid_mail_helmet,itm.sarranid_horseman_helmet,itm.sarranid_boots_b,itm.sarranid_boots_c,itm.mail_gauntlets,itm.mail_mittens,itm.sarranid_leather_vest,itm.sarranid_leather_armor,itm.sarranid_chain,
		itm.heavy_camel_a,itm.heavy_camel_b,
		itm.shield_common_kite_d,
		itm.slavers_mace,itm.winged_mace_b,itm.sarranid_mace,
	], ATTR(20,19,8,9,28), wpex(150,150,150,150,150,150), SKILLS(power_strike=2, weapon_master=4, shield=5, athletics=3, riding=4, tracking=6, spotting=4, trainer=1, ), sarranid_face_middle_1, sarranid_face_older_2],

]

define_troop_upgrade(trp.outlaw_forest_a, trp.outlaw_forest_b)
define_troop_upgrade(trp.outlaw_forest_b, trp.outlaw_forest_c)
define_troop_upgrade(trp.outlaw_forest_c, trp.outlaw_forest_d)
define_troop_upgrade(trp.outlaw_tundra_a, trp.outlaw_tundra_b)
define_troop_upgrade(trp.outlaw_tundra_b, trp.outlaw_tundra_c)
define_troop_upgrade(trp.outlaw_tundra_c, trp.outlaw_tundra_d)
define_troop_upgrade(trp.outlaw_mountain_a, trp.outlaw_mountain_b)
define_troop_upgrade(trp.outlaw_mountain_b, trp.outlaw_mountain_c)
define_troop_upgrade(trp.outlaw_mountain_c, trp.outlaw_mountain_d)
define_troop_upgrade(trp.outlaw_steppe_a, trp.outlaw_steppe_b)
define_troop_upgrade(trp.outlaw_steppe_b, trp.outlaw_steppe_c)
define_troop_upgrade(trp.outlaw_steppe_c, trp.outlaw_steppe_d)
define_troop_upgrade(trp.outlaw_highway_a, trp.outlaw_highway_b)
define_troop_upgrade(trp.outlaw_highway_b, trp.outlaw_highway_c)
define_troop_upgrade(trp.outlaw_highway_c, trp.outlaw_highway_d)
define_troop_upgrade(trp.outlaw_river_a, trp.outlaw_river_b)
define_troop_upgrade(trp.outlaw_river_b, trp.outlaw_river_c)
define_troop_upgrade(trp.outlaw_river_c, trp.outlaw_river_d)
define_troop_upgrade(trp.outlaw_raider_a, trp.outlaw_raider_b)
define_troop_upgrade(trp.outlaw_raider_b, trp.outlaw_raider_c)
define_troop_upgrade(trp.outlaw_raider_c, trp.outlaw_raider_d)
define_troop_upgrade(trp.outlaw_pirate_a, trp.outlaw_pirate_b)
define_troop_upgrade(trp.outlaw_pirate_b, trp.outlaw_pirate_c)
define_troop_upgrade(trp.outlaw_pirate_c, trp.outlaw_pirate_d)
define_troop_upgrade(trp.outlaw_slaver_a, trp.outlaw_slaver_b)
define_troop_upgrade(trp.outlaw_slaver_b, trp.outlaw_slaver_c)
define_troop_upgrade(trp.outlaw_slaver_c, trp.outlaw_slaver_d)


def invert_list(l):
	return [item for item in reversed(l)]

party_templates = [

	("outlaws_forest_a", "Poachers",       icon.outlaw_archer_bandits|carries_goods(1), 0, fac.outlaws_forest, bandit_personality, invert_list([(trp.outlaw_forest_a,6,12),(trp.outlaw_forest_b,2,4)])),
	("outlaws_forest_b", "Forest Bandits", icon.outlaw_archer_bandits|carries_goods(2), 0, fac.outlaws_forest, bandit_personality, invert_list([(trp.outlaw_forest_a,2,6),(trp.outlaw_forest_b,6,16),(trp.outlaw_forest_c,4,8)])),
	("outlaws_forest_c", "Forest Gang",    icon.outlaw_archer_bandits|carries_goods(3), 0, fac.outlaws_forest, bandit_personality, invert_list([(trp.outlaw_forest_b,4,10),(trp.outlaw_forest_c,16,30),(trp.outlaw_forest_d,1,2)])),

	("outlaws_tundra_a", "Smugglers",      icon.axeman|carries_goods(1), 0, fac.outlaws_tundra, bandit_personality, invert_list([(trp.outlaw_tundra_a,4,10),(trp.outlaw_tundra_b,1,6)])),
	("outlaws_tundra_b", "Tundra Bandits", icon.axeman|carries_goods(2), 0, fac.outlaws_tundra, bandit_personality, invert_list([(trp.outlaw_tundra_a,2,4),(trp.outlaw_tundra_b,8,16),(trp.outlaw_tundra_c,4,8)])),
	("outlaws_tundra_c", "Tundra Rangers", icon.axeman|carries_goods(3), 0, fac.outlaws_tundra, bandit_personality, invert_list([(trp.outlaw_tundra_b,6,12),(trp.outlaw_tundra_c,12,32),(trp.outlaw_tundra_d,1,3)])),

	("outlaws_mountain_a", "Mountain Clansmen", icon.outlaw_mountain_bandits|carries_goods(1), 0, fac.outlaws_mountain, bandit_personality, invert_list([(trp.outlaw_mountain_a,8,14),(trp.outlaw_mountain_b,1,2)])),
	("outlaws_mountain_b", "Mountain Bandits",  icon.outlaw_mountain_bandits|carries_goods(2), 0, fac.outlaws_mountain, bandit_personality, invert_list([(trp.outlaw_mountain_a,2,4),(trp.outlaw_mountain_b,6,20),(trp.outlaw_mountain_c,4,6)])),
	("outlaws_mountain_c", "Mountain Brigands", icon.outlaw_mountain_bandits|carries_goods(3), 0, fac.outlaws_mountain, bandit_personality, invert_list([(trp.outlaw_mountain_b,2,6),(trp.outlaw_mountain_c,14,34),(trp.outlaw_mountain_d,4,6)])),

	("outlaws_steppe_a", "Steppe Scum",    icon.khergit|carries_goods(1), 0, fac.outlaws_steppe, bandit_personality, invert_list([(trp.outlaw_steppe_a,8,16),(trp.outlaw_steppe_b,1,2)])),
	("outlaws_steppe_b", "Steppe Bandits", icon.khergit|carries_goods(2), 0, fac.outlaws_steppe, bandit_personality, invert_list([(trp.outlaw_steppe_a,1,5),(trp.outlaw_steppe_b,8,20),(trp.outlaw_steppe_c,4,10)])),
	("outlaws_steppe_c", "Steppe Raiders", icon.khergit|carries_goods(3), 0, fac.outlaws_steppe, bandit_personality, invert_list([(trp.outlaw_steppe_b,8,14),(trp.outlaw_steppe_c,22,42),(trp.outlaw_steppe_d,1,1)])),

	("outlaws_highway_a", "Outlaws",    icon.axeman|carries_goods(1), 0, fac.outlaws_highway, bandit_personality, invert_list([(trp.outlaw_highway_a,6,16),(trp.outlaw_highway_b,1,4)])),
	("outlaws_highway_b", "Robbers",    icon.axeman|carries_goods(2), 0, fac.outlaws_highway, bandit_personality, invert_list([(trp.outlaw_highway_a,1,8),(trp.outlaw_highway_b,6,16),(trp.outlaw_highway_c,4,12)])),
	("outlaws_highway_c", "Highwaymen", icon.axeman|carries_goods(3), 0, fac.outlaws_highway, bandit_personality, invert_list([(trp.outlaw_highway_b,2,6),(trp.outlaw_highway_c,10,22),(trp.outlaw_highway_d,6,16)])),

	("outlaws_river_a", "River Pirate Patrol", icon.axeman|carries_goods(1), 0, fac.outlaws_river, bandit_personality, invert_list([(trp.outlaw_river_a,2,8),(trp.outlaw_river_b,6,10)])),
	("outlaws_river_b", "River Pirates",       icon.axeman|carries_goods(2), 0, fac.outlaws_river, bandit_personality, invert_list([(trp.outlaw_river_a,6,12),(trp.outlaw_river_b,12,30),(trp.outlaw_river_c,1,4)])),
	("outlaws_river_c", "River Pirate Army",   icon.axeman|carries_goods(4), 0, fac.outlaws_river, bandit_personality, invert_list([(trp.outlaw_river_a,14,20),(trp.outlaw_river_b,24,40),(trp.outlaw_river_c,2,6),(trp.outlaw_river_d,1,1)])),

	("outlaws_raider_a", "Sea Raider Patrol", icon.outlaw_sea_raiders|carries_goods(1), 0, fac.outlaws_raider, bandit_personality, invert_list([(trp.outlaw_raider_a,4,8),(trp.outlaw_raider_b,4,8)])),
	("outlaws_raider_b", "Sea Raiders",       icon.outlaw_sea_raiders|carries_goods(2), 0, fac.outlaws_raider, bandit_personality, invert_list([(trp.outlaw_raider_a,8,12),(trp.outlaw_raider_b,6,16),(trp.outlaw_raider_c,2,4)])),
	("outlaws_raider_c", "Sea Raider Gang",   icon.outlaw_sea_raiders|carries_goods(3), 0, fac.outlaws_raider, bandit_personality, invert_list([(trp.outlaw_raider_a,10,18),(trp.outlaw_raider_b,2,8),(trp.outlaw_raider_c,18,32),(trp.outlaw_raider_d,1,1)])),

	("outlaws_pirate_a", "Pirate Harassers",      icon.axeman|carries_goods(1), 0, fac.outlaws_pirate, bandit_personality, invert_list([(trp.outlaw_pirate_a,8,14),(trp.outlaw_pirate_b,2,4)])),
	("outlaws_pirate_b", "Pirate Boarding Party", icon.axeman|carries_goods(2), 0, fac.outlaws_pirate, bandit_personality, invert_list([(trp.outlaw_pirate_a,2,6),(trp.outlaw_pirate_b,4,12),(trp.outlaw_pirate_c,4,10)])),
	("outlaws_pirate_c", "Pirate Landing Party",  icon.axeman|carries_goods(3), 0, fac.outlaws_pirate, bandit_personality, invert_list([(trp.outlaw_pirate_a,2,8),(trp.outlaw_pirate_b,4,14),(trp.outlaw_pirate_c,12,26),(trp.outlaw_pirate_d,6,10)])),

	("outlaws_slaver_a", "Slavers",       icon.outlaw_desert_bandits|carries_goods(1), 0, fac.outlaws_slaver, bandit_personality, invert_list([(trp.outlaw_slaver_a,6,14),(trp.outlaw_slaver_b,1,1)])),
	("outlaws_slaver_b", "Slave Hunters", icon.outlaw_desert_bandits|carries_goods(2), 0, fac.outlaws_slaver, bandit_personality, invert_list([(trp.outlaw_slaver_a,1,8),(trp.outlaw_slaver_b,10,22),(trp.outlaw_slaver_c,1,3)])),
	("outlaws_slaver_c", "Slavemasters",  icon.outlaw_desert_bandits|carries_goods(3), 0, fac.outlaws_slaver, bandit_personality, invert_list([(trp.outlaw_slaver_b,8,18),(trp.outlaw_slaver_c,12,26),(trp.outlaw_slaver_d,1,4)])),

]



parties = [

	# Spawn areas for Forest Bandits (points with radius):

	("spawn_forest_1", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_forest, 0, ai_bhvr_hold, 0, (-72.0, 34.2), [(trp.cattle,11,0)]),
	("spawn_forest_2", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_forest, 0, ai_bhvr_hold, 0, (-62.0, 25.0), [(trp.cattle,11,0)]),
	("spawn_forest_3", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_forest, 0, ai_bhvr_hold, 0, (-34.5, 20.0), [(trp.cattle,13,0)]),
	("spawn_forest_4", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_forest, 0, ai_bhvr_hold, 0, (-26.0, 64.5), [(trp.cattle,17,0)]),
	("spawn_forest_5", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_forest, 0, ai_bhvr_hold, 0, (  3.5, 48.0), [(trp.cattle,18,0)]),
	("spawn_forest_6", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_forest, 0, ai_bhvr_hold, 0, ( 10.0, 32.5), [(trp.cattle,18,0)]),
	("spawn_forest_7", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_forest, 0, ai_bhvr_hold, 0, ( 26.0, 29.5), [(trp.cattle,14,0)]),
	("spawn_forest_8", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_forest, 0, ai_bhvr_hold, 0, (  3.0, 11.5), [(trp.cattle, 9,0)]),

	# Spawn areas for Tundra Bandits (points with radius):

	("spawn_tundra_1", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_tundra, 0, ai_bhvr_hold, 0, (24.0, 50.0), [(trp.cattle, 4,0)]),
	("spawn_tundra_2", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_tundra, 0, ai_bhvr_hold, 0, (35.0, 73.5), [(trp.cattle,16,0)]),
	("spawn_tundra_3", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_tundra, 0, ai_bhvr_hold, 0, (13.0, 86.0), [(trp.cattle, 6,0)]),
	("spawn_tundra_4", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_tundra, 0, ai_bhvr_hold, 0, (36.0, 95.5), [(trp.cattle, 9,0)]),
	("spawn_tundra_5", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_tundra, 0, ai_bhvr_hold, 0, (49.0, 93.5), [(trp.cattle, 4,0)]),

	# Spawn range for Mountain Bandits (base points form a jagged line, get random point, get land within 6 units):

	("spawn_mountain_1", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_mountain, 0, ai_bhvr_hold, 0, (102.719,  1.140), []),
	("spawn_mountain_2", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_mountain, 0, ai_bhvr_hold, 0, (101.897, 33.029), []),
	("spawn_mountain_3", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_mountain, 0, ai_bhvr_hold, 0, (138.065, 53.736), []),
	("spawn_mountain_4", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_mountain, 0, ai_bhvr_hold, 0, (154.798, 45.014), []),
	("spawn_mountain_5", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_mountain, 0, ai_bhvr_hold, 0, (169.346, 53.798), []),

	# Spawn areas for Steppe Raiders (points with radius):

	("spawn_steppe_1", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_steppe, 0, ai_bhvr_hold, 0, (66.5, -56.0), [(trp.cattle,12,0)]),
	("spawn_steppe_2", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_steppe, 0, ai_bhvr_hold, 0, (85.5, -70.0), [(trp.cattle, 8,0)]),

	# Spawn areas for Highway Robbers (points with radius):

	("spawn_highway_1", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_highway, 0, ai_bhvr_hold, 0, (-20.127, -76.120), [(trp.cattle,9,0)]),
	("spawn_highway_2", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_highway, 0, ai_bhvr_hold, 0, (  5.780, -72.159), [(trp.cattle,11,0)]),
	("spawn_highway_3", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_highway, 0, ai_bhvr_hold, 0, (  6.187, -97.177), [(trp.cattle,7,0)]),

	# Landing zones for River Pirates (base point, max radius => get water in radius=max, get land in radius=1):

	("spawn_river_1", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_river, 0, ai_bhvr_hold, 0, (-107.5,  0.0), [(trp.cattle,25,0)]),
	("spawn_river_2", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_river, 0, ai_bhvr_hold, 0, ( -79.0, -3.5), [(trp.cattle,15,0)]),

#	# Landing triangles for Sea Raiders (1st land point, 2nd land point, sea point):
#
#	# Vaegir east
#	("spawn_raider_1_lz1", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_raider, 0, ai_bhvr_hold, 0, ( 101.610, 130.386), []),
#	("spawn_raider_1_lz2", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_raider, 0, ai_bhvr_hold, 0, (  86.460, 122.496), []),
#	("spawn_raider_1_sea", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_raider, 0, ai_bhvr_hold, 0, (  85.898, 134.087), []),
#	# Vaegir near Rivacheg
#	("spawn_raider_2_lz1", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_raider, 0, ai_bhvr_hold, 0, (  70.061, 116.443), []),
#	("spawn_raider_2_lz2", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_raider, 0, ai_bhvr_hold, 0, (  46.974, 116.678), []),
#	("spawn_raider_2_sea", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_raider, 0, ai_bhvr_hold, 0, (  55.587, 133.745), []),
#	# Nord near Odasan
#	("spawn_raider_3_lz1", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_raider, 0, ai_bhvr_hold, 0, ( -17.100, 126.114), []),
#	("spawn_raider_3_lz2", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_raider, 0, ai_bhvr_hold, 0, ( -19.100, 126.410), []),
#	("spawn_raider_3_sea", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_raider, 0, ai_bhvr_hold, 0, ( -18.100, 128.514), []),
#	# Nord far west of Wercheg
#	("spawn_raider_4_lz1", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_raider, 0, ai_bhvr_hold, 0, ( -39.100, 118.486), []),
#	("spawn_raider_4_lz2", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_raider, 0, ai_bhvr_hold, 0, ( -40.100, 114.197), []),
#	("spawn_raider_4_sea", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_raider, 0, ai_bhvr_hold, 0, ( -44.100, 117.537), []),
#	# Shore strip between Tihr and Buillin
#	("spawn_raider_5_lz1", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_raider, 0, ai_bhvr_hold, 0, ( -56.100,  77.461), []),
#	("spawn_raider_5_lz2", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_raider, 0, ai_bhvr_hold, 0, ( -91.100, 110.545), []),
#	("spawn_raider_5_sea", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_raider, 0, ai_bhvr_hold, 0, ( -51.100, 112.184), []),
#	# Shore strip between Buillin and Kulum
#	("spawn_raider_6_lz1", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_raider, 0, ai_bhvr_hold, 0, ( -78.100, 109.262), []),
#	("spawn_raider_6_lz2", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_raider, 0, ai_bhvr_hold, 0, (-128.100, 107.860), []),
#	("spawn_raider_6_sea", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_raider, 0, ai_bhvr_hold, 0, (-105.100, 149.859), []),
#
#	# Landing triangles for Pirates (1st land point, 2nd land point, sea point):
#
#	# Swadia near Balanli
#	("spawn_pirate_1_lz1", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_pirate, 0, ai_bhvr_hold, 0, (-130.1000, 44.156), []),
#	("spawn_pirate_1_lz2", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_pirate, 0, ai_bhvr_hold, 0, (-131.1000, 42.853), []),
#	("spawn_pirate_1_sea", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_pirate, 0, ai_bhvr_hold, 0, (-133.1000, 44.152), []),
#	# Swadian south-western shore near Elberl
#	("spawn_pirate_2_lz1", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_pirate, 0, ai_bhvr_hold, 0, (-141.1000, 30.335), []),
#	("spawn_pirate_2_lz2", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_pirate, 0, ai_bhvr_hold, 0, (-132.1000, 3.387), []),
#	("spawn_pirate_2_sea", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_pirate, 0, ai_bhvr_hold, 0, (-166.1000, 18.044), []),
#	# Rhodok western shore from Istiniar and to the south
#	("spawn_pirate_3_lz1", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_pirate, 0, ai_bhvr_hold, 0, (-134.1000, 0.172), []),
#	("spawn_pirate_3_lz2", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_pirate, 0, ai_bhvr_hold, 0, (-161.1000, -31.1000), []),
#	("spawn_pirate_3_sea", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_pirate, 0, ai_bhvr_hold, 0, (-173.1000, 13.088), []),
#	# Small shore strip south of Epeshe
#	("spawn_pirate_4_lz1", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_pirate, 0, ai_bhvr_hold, 0, (-107.1000, -64.1000), []),
#	("spawn_pirate_4_lz2", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_pirate, 0, ai_bhvr_hold, 0, (-102.1000, -65.1000), []),
#	("spawn_pirate_4_sea", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_pirate, 0, ai_bhvr_hold, 0, (-107.1000, -71.1000), []),
#	# Shoreline south of Jelkala
#	("spawn_pirate_5_lz1", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_pirate, 0, ai_bhvr_hold, 0, (-96.1000, -98.1000), []),
#	("spawn_pirate_5_lz2", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_pirate, 0, ai_bhvr_hold, 0, (-56.1000, -99.1000), []),
#	("spawn_pirate_5_sea", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_pirate, 0, ai_bhvr_hold, 0, (-80.1000, -123.1000), []),
#
#	# Spawn points for Slavers (points with minimal radius):
#
#	("spawn_slaver_1", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_slaver, 0, ai_bhvr_hold, 0, (169.316,    9.1), []),
#	("spawn_slaver_2", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_slaver, 0, ai_bhvr_hold, 0, (181.625,  -32.1), []),
#	("spawn_slaver_3", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_slaver, 0, ai_bhvr_hold, 0, (178.952,  -71.1), []),
#	("spawn_slaver_4", "{!}spawn", pf_disabled|pf_is_static, 0, pt.none, fac.outlaws_slaver, 0, ai_bhvr_hold, 0, (178.823, -130.1), []),

]

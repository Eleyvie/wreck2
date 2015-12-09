from compiler import *

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [

    ("none","none",icon.gray_knight,0,fac.commoners,merchant_personality,[]),
    ("disabled_01", "{!}disabled 01", icon.ship|pf_is_static, 0, fac.commoners, merchant_personality, []),
    ("disabled_02", "{!}disabled 02", icon.ship|pf_is_static, 0, fac.outlaws,   merchant_personality, []),
    ("disabled_03", "{!}disabled 03", icon.ship|pf_is_static, 0, fac.commoners, merchant_personality, []),

    ####################################################################################################################
    # Party templates before this point are hard-wired into the game and should not be changed.
    ####################################################################################################################

    ("village_defenders","Village Defenders",icon.peasant,0,fac.commoners,merchant_personality,[(trp.farmer,10,20),(trp.peasant_woman,0,4)]), # Reinforcement party for villages
    ("cattle_herd","Cattle Herd",icon.cattle|carries_goods(10),0,fac.neutral,merchant_personality,[(trp.cattle,80,120)]), # Cattle party

    ##  ("vaegir_nobleman","Vaegir Nobleman",icon.vaegir_knight|carries_goods(10)|pf_quest_party,0,fac.commoners,merchant_personality,[(trp.nobleman,1,1),(trp.vaegir_knight,2,6),(trp.vaegir_horseman,4,12)]),
    ##  ("swadian_nobleman","Swadian Nobleman",icon.gray_knight|carries_goods(10)|pf_quest_party,0,fac.commoners,merchant_personality,[(trp.nobleman,1,1),(trp.swadian_knight,2,6),(trp.swadian_man_at_arms,4,12)]),
    # Ryan BEGIN
    # ("looters","Looters",icon.axeman|carries_goods(8),0,fac.outlaws,bandit_personality,[(trp.looter,3,45)]),
    # Ryan END
    # ("manhunters","Manhunters",icon.gray_knight,0,fac.manhunters,soldier_personality,[(trp.manhunter,9,40)]),
    ##  ("peasant","Peasant",icon.peasant,0,fac.commoners,merchant_personality,[(trp.farmer,1,6),(trp.peasant_woman,0,7)]),

    # NE
    ("looters", "Mercenary War Band", icon.outlaw_mercenaries|carries_goods(8), 0, fac.outlaws, bandit_personality, [(trp.female_pike_sister,3,12),(trp.female_shield_sister,3,6),(trp.mercenary_swordsman,6,12),(trp.mercenary_crossbowman,3,8),(trp.mercenary_equite,3,6),(trp.female_archer,3,12)] ),
    ("manhunters","Manhunters",icon.manhunters,0,fac.manhunters,soldier_personality,[(trp.manhunter_t4,1,1),(trp.manhunter_t3,0,10),(trp.manhunter_t2,6,18),(trp.manhunter,4,12),(trp.looter,0,6,pmf_is_prisoner),(trp.brigand,0,4,pmf_is_prisoner),(trp.bandit,0,3,pmf_is_prisoner)]),
    ("cheese_rustlers","Cheese Rustlers",icon.axeman|carries_goods(2)|pf_quest_party,0,fac.outlaws,bandit_personality,[(trp.cheese_rustler,15,25)]),
    ("cheese_paladins","Cheese Rustlers",icon.gray_knight|carries_goods(20)|pf_quest_party,0,fac.outlaws,merchant_personality,[(trp.cheese_rustler2,8,12)]),
    ("scholars","Scholars",icon.lone_man|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party,0,fac.commoners,escorted_merchant_personality,[(trp.scholar,10,10)]),
    ("nemesis", "Hired Blades", icon.gray_knight|carries_goods(2)|pf_quest_party, 0, fac.neutral, merchant_personality, [(trp.female_shield_maiden,6,18),(trp.female_line_maiden,9,27),(trp.female_stalker,9,18),(trp.mercenary_sniper,9,18),(trp.mercenary_zweihander,6,18),(trp.mercenary_cavalry,3,12)] ),
    ("nemesis2", "Hired Blades", icon.gray_knight|carries_goods(0)|pf_quest_party, 0, fac.robber_knights, escorted_merchant_personality, [(trp.mercenary_cavalry,100,150),(trp.female_shield_maiden,50,75)] ),
    # v585 Josef elites
    ("elites_fac1", "Usurpers", icon.swadia_rebels|carries_goods(2)|pf_quest_party, 0, fac.neutral, merchant_personality, [(trp.swadian_paladin,9,27),(trp.swadian_priest,9,27),(trp.swadian_cavalier,27,36)] ),
    ("elites_fac2", "Usurpers", icon.vaegir_rebels|carries_goods(2)|pf_quest_party, 0, fac.neutral, merchant_personality, [(trp.vaegir_ivory_sentinel,27,36),(trp.vaegir_knyaz,27,36),(trp.vaegir_druzhina,36,45)] ),
    ("elites_fac3", "Usurpers", icon.khergit_rebels|carries_goods(2)|pf_quest_party, 0, fac.neutral, merchant_personality, [(trp.khergit_guanren, 27, 42), (trp.khergit_keshik,42,90), (trp.khergit_jurtchi,42,72)]),
    ("elites_fac4", "Usurpers", icon.nordic_rebels|carries_goods(2)|pf_quest_party, 0, fac.neutral, merchant_personality, [(trp.nord_einherjar,27,42),(trp.nord_valkyrie,27,42),(trp.nord_thane,18,36)] ),
    ("elites_fac5", "Usurpers", icon.rhodok_rebels|carries_goods(2)|pf_quest_party, 0, fac.neutral, merchant_personality, [(trp.rhodok_arbalest,42,60),(trp.rhodok_spear_knight,18,27),(trp.rhodok_councilman,27,36)] ),
    ("elites_fac6", "Usurpers", icon.sarranid_rebels|carries_goods(2)|pf_quest_party, 0, fac.neutral, merchant_personality, [(trp.sarranid_zhayedan,20,20),(trp.sarranid_spahbod_serden,15,45),(trp.sarranid_spahbod,15,45),(trp.sarranid_dailamite,35,65)] ),

    # v585 Josef Kidnapped wife quest
    ("bandits_awaiting_ransom2","Bandits Awaiting Ransom",icon.axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac.neutral,bandit_personality,[(trp.brigand,24,58),(trp.kidnapped_wife,1,1,pmf_is_prisoner)]),
    ("kidnapped_wife","Miller's Wife",icon.woman|pf_quest_party,0,fac.neutral,merchant_personality,[(trp.kidnapped_wife,1,1)]),
    # v585 Josef strange portrait quest
    ("spymaster","Spymaster",icon.lone_man|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac.neutral,bandit_personality,[(trp.spymaster,1,1)]),
    # end NE

    # NE bandit numbers - rem change these

    ("steppe_bandits","Steppe Bandits",icon.khergit|carries_goods(2),0,fac.outlaws,bandit_personality,[(trp.steppe_bandit,15,58),(trp.steppe_raider,9,12)]),
    ("taiga_bandits","Tundra Bandits",icon.axeman|carries_goods(2),0,fac.outlaws,bandit_personality,[(trp.taiga_bandit,22,58)]),
    ("desert_bandits","Desert Bandits",icon.outlaw_desert_bandits|carries_goods(2),0,fac.outlaws,bandit_personality,[(trp.desert_bandit,22,58)]),
    ("forest_bandits","Forest Bandits",icon.outlaw_archer_bandits|carries_goods(2),0,fac.forest_bandits,bandit_personality,[(trp.forest_bandit,19,52),(trp.peasant_woman,0,4,pmf_is_prisoner)]),
    ("mountain_bandits","Mountain Bandits",icon.outlaw_mountain_bandits|carries_goods(2),0,fac.mountain_bandits,bandit_personality,[(trp.mountain_bandit,22,60),(trp.peasant_woman,0,2,pmf_is_prisoner)]),
    ("sea_raiders","Sea Raiders",icon.outlaw_sea_raiders|carries_goods(2),0,fac.outlaws,bandit_personality,[(trp.sea_raider,20,50)]),

    ("deserters","Deserters",icon.outlaw_deserters|carries_goods(3),0,fac.deserters,bandit_personality,[]),

    ("merchant_caravan","Merchant Caravan",icon.quest_caravan|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party,0,fac.commoners,escorted_merchant_personality,[(trp.caravan_master,1,1),(trp.caravan_guard,5,25)]),
    ("troublesome_bandits","Troublesome Bandits",icon.axeman|carries_goods(9)|pf_quest_party,0,fac.outlaws,bandit_personality,[(trp.brigand,14,55)]),
    ("bandits_awaiting_ransom","Bandits Awaiting Ransom",icon.axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac.neutral,bandit_personality,[(trp.bandit,24,58),(trp.kidnapped_girl,1,1,pmf_is_prisoner)]),
    ("kidnapped_girl","Kidnapped Girl",icon.woman|pf_quest_party,0,fac.neutral,merchant_personality,[(trp.kidnapped_girl,1,1)]),


    ("smugglers","Smugglers",icon.peasant|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac.neutral,merchant_personality,[(trp.brigand,3,3), (trp.forest_bandit,3,3), (trp.mountain_bandit,3,3)]),	
    # end v585 Josef

    # NE quests end
    ("village_farmers","Village Farmers",icon.peasant|pf_civilian,0,fac.neutral,merchant_personality,[(trp.farmer,5,10),(trp.peasant_woman,3,8)]),

    ("spy_partners", "Unremarkable Travellers", icon.outlaw_deserters|carries_goods(10)|pf_default_behavior|pf_quest_party,0,fac.neutral,merchant_personality,[(trp.spy_partner,1,1),(trp.caravan_guard,5,11)]),
    ("runaway_serfs","Runaway Serfs",icon.peasant|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac.neutral,merchant_personality,[(trp.farmer,6,7), (trp.peasant_woman,3,3)]),
    ("spy", "Ordinary Townsman", icon.lone_man|carries_goods(4)|pf_default_behavior|pf_quest_party,0,fac.neutral,merchant_personality,[(trp.spy,1,1)]),
    ("sacrificed_messenger", "Sacrificed Messenger", icon.gray_knight|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac.neutral,merchant_personality,[]),

    ("forager_party","Foraging Party",icon.gray_knight|carries_goods(5)|pf_show_faction,0,fac.commoners,merchant_personality,[]),
    ("swadian_scouts", "Scouts", icon.swadia_scouts|carries_goods(1)|pf_show_faction, 0, fac.kingdom_1, bandit_personality, [(trp.swadian_veteran_crossbowman,4,8),(trp.swadian_crossbowman,2,4),(trp.swadian_sergeant,1,3)] ),
    ("vaegir_scouts", "Scouts", icon.vaegir_scouts|carries_goods(1)|pf_show_faction, 0, fac.kingdom_2, bandit_personality, [(trp.vaegir_marksman,6,14),(trp.vaegir_scout,1,3),(trp.vaegir_varangian,1,4)] ),
    ("khergit_scouts","Scouts",icon.khergit_scouts|carries_goods(1)|pf_show_faction,0,fac.kingdom_3,bandit_personality,[(trp.khergit_horse_archer,2,4),(trp.khergit_master_horse_archer,4,8),(trp.khergit_lancer,3,9)]),
    ("nord_scouts", "Scouts", icon.nordic_scouts|carries_goods(1)|pf_show_faction, 0, fac.kingdom_4, bandit_personality, [(trp.nord_skald,1,2),(trp.nord_raiding_archer,3,9),(trp.nord_warrior,1,3)] ),
    ("rhodok_scouts", "Scouts", icon.rhodok_scouts|carries_goods(1)|pf_show_faction, 0, fac.kingdom_5, bandit_personality, [(trp.rhodok_sharpshooter,4,8),(trp.rhodok_master_spearman,2,4),(trp.rhodok_scout,1,1)] ),
    ("swadian_patrol", "Patrol", icon.swadia_patrol|carries_goods(2)|pf_show_faction, 0, fac.kingdom_1, soldier_personality, [(trp.swadian_man_at_arms,2,4),(trp.swadian_sergeant,6,12),(trp.swadian_infantry,12,18),(trp.swadian_squire,3,9),(trp.swadian_crossbowman,6,18),(trp.swadian_paladin,1,1)] ),
    ("vaegir_patrol", "Patrol", icon.vaegir_patrol|carries_goods(2)|pf_show_faction, 0, fac.kingdom_2, soldier_personality, [(trp.vaegir_horseman,3,9),(trp.vaegir_varangian_guard,5,9),(trp.vaegir_pikeman,3,12),(trp.vaegir_marksman,3,12),(trp.vaegir_archer,9,27),(trp.vaegir_knyaz,1,1)] ),
    ("khergit_patrol","Patrol",icon.khergit_patrol|carries_goods(2)|pf_show_faction,0,fac.kingdom_3,soldier_personality,[(trp.khergit_horse_archer,6,18),(trp.khergit_lancer,6,18),(trp.khergit_keshik,1,1),(trp.khergit_tarkhan,2,7),(trp.khergit_kharash,12,27)]),
    ("nord_patrol", "Patrol", icon.nordic_patrol|carries_goods(2)|pf_show_faction, 0, fac.kingdom_4, soldier_personality, [(trp.nord_merkismathr,3,9),(trp.nord_berserker,3,9),(trp.nord_butsecarl,1,1),(trp.nord_skald,6,12),(trp.nord_warrior,9,18)] ),
    ("rhodok_patrol", "Patrol", icon.rhodok_patrol|carries_goods(2)|pf_show_faction, 0, fac.kingdom_5, soldier_personality, [(trp.rhodok_spear_knight,1,1),(trp.rhodok_arbalest,5,9),(trp.rhodok_veteran_spearman,9,10),(trp.rhodok_sharpshooter,9,10),(trp.rhodok_swordsman,9,10)] ),
    ("crusaders", "Holy Crusaders", icon.swadia_elites|carries_goods(2)|pf_show_faction, 0, fac.kingdom_1, soldier_personality, [(trp.swadian_paladin,3,6),(trp.swadian_priest,5,11)] ),
    ("ivory_guards", "Ivory Guards", icon.vaegir_elites|carries_goods(2)|pf_show_faction, 0, fac.kingdom_2, soldier_personality, [(trp.vaegir_ivory_sentinel,6,12),(trp.vaegir_knyaz,2,7),(trp.vaegir_druzhina,1,1)] ),
    ("red_horde","Red Horde",icon.khergit_elites1|carries_goods(2)|pf_show_faction,0,fac.kingdom_3,soldier_personality,[(trp.khergit_veteran_horse_archer,27,48),(trp.khergit_lancer,27,48),(trp.khergit_savage_kharash,27,48),(trp.khergit_mangudai,18,36),(trp.khergit_guanren,2,2),(trp.khergit_keshik,2,2)]),
    ("blue_horde","Blue Horde",icon.khergit_elites2|carries_goods(2)|pf_show_faction,0,fac.kingdom_3,soldier_personality,[(trp.khergit_veteran_horse_archer,27,48),(trp.khergit_lancer,27,48),(trp.khergit_kharash_clansman,27,48),(trp.khergit_jurtchi,9,18),(trp.khergit_guanren,1,4),(trp.khergit_keshik,0,4)]),
    ("raiders", "Berserkers", icon.nordic_elites|carries_goods(2)|pf_show_faction, 0, fac.kingdom_4, soldier_personality, [(trp.nord_berserker,3,9),(trp.nord_einherjar,2,7),(trp.nord_valkyrie,1,3),(trp.nord_merkismathr,1,3)] ),
    ("councilmen", "Councilmen", icon.rhodok_elites|carries_goods(2)|pf_show_faction, 0, fac.kingdom_5, soldier_personality, [(trp.rhodok_armsman,3,9),(trp.rhodok_spear_knight,1,3),(trp.rhodok_arbalest,6,18),(trp.rhodok_veteran_scout,3,9),(trp.rhodok_master_swordsman,3,9)] ),
    #  ("war_party", "War Party",icon.gray_knight|carries_goods(3),0,fac.commoners,soldier_personality,[]),
    ("messenger_party","Messenger",icon.gray_knight|pf_show_faction,0,fac.commoners,merchant_personality,[]),
    ("raider_party","Raiders",icon.gray_knight|carries_goods(16)|pf_quest_party,0,fac.commoners,bandit_personality,[]),
    ("raider_captives","Raider Captives",0,0,fac.commoners,0,[(trp.peasant_woman,6,30,pmf_is_prisoner)]),
    ("kingdom_caravan_party","Caravan",icon.mule|carries_goods(25)|pf_show_faction,0,fac.commoners,merchant_personality,[(trp.caravan_master,1,1),(trp.caravan_guard,12,40)]),
    ("swadian_prisoner_train", "Prisoner Train", icon.gray_knight|carries_goods(5)|pf_show_faction, 0, fac.kingdom_1, merchant_personality, [(trp.swadian_infantry,5,10),(trp.swadian_senior_squire,6,8),(trp.swadian_crossbowman,7,12),(trp.bandit,10,24,pmf_is_prisoner)] ),
    ("vaegir_prisoner_train", "Prisoner Train", icon.gray_knight|carries_goods(5)|pf_show_faction, 0, fac.kingdom_2, merchant_personality, [(trp.vaegir_sergeant,5,10),(trp.vaegir_horseman,3,5),(trp.vaegir_archer,9,15),(trp.bandit,10,24,pmf_is_prisoner)] ),
    ("khergit_prisoner_train","Prisoner Train",icon.gray_knight|carries_goods(5)|pf_show_faction,0,fac.kingdom_3,merchant_personality,[(trp.khergit_horse_archer,18,36),(trp.khergit_lancer,18,36),(trp.steppe_bandit,17,95,pmf_is_prisoner),(trp.steppe_raider,3,36,pmf_is_prisoner)] ),
    ("nord_prisoner_train", "Prisoner Train", icon.gray_knight|carries_goods(5)|pf_show_faction, 0, fac.kingdom_4, merchant_personality, [(trp.nord_warrior,14,36),(trp.sea_raider,5,18,pmf_is_prisoner),(trp.nord_raiding_archer,2,8),(trp.nord_butsecarl,1,1)] ),
    ("rhodok_prisoner_train", "Prisoner Train", icon.gray_knight|carries_goods(5)|pf_show_faction, 0, fac.kingdom_5, merchant_personality, [(trp.rhodok_veteran_spearman,10,20),(trp.rhodok_crossbowman,10,20),(trp.bandit,10,24,pmf_is_prisoner)] ),
    # NE TODO - enter Sarranid prisoner train
    ("sarranid_scouts", "Sarranid Scouts", icon.sarranid_scouts|carries_goods(1)|pf_show_faction, 0, fac.kingdom_6, bandit_personality, [(trp.sarranid_kamandaran_serden,3,9),(trp.sarranid_kamandaran,6,12),(trp.sarranid_timariot,1,1)] ),
    ("sarranid_patrol", "Sarranid Patrol", icon.sarranid_patrol|carries_goods(2)|pf_show_faction, 0, fac.kingdom_6, soldier_personality, [(trp.sarranid_dervish,4,8),(trp.sarranid_janissary,5,9),(trp.sarranid_dailamite,9,10),(trp.sarranid_timariot,9,10),(trp.sarranid_kamandaran_serden,9,10),(trp.sarranid_mamluke,1,1)] ),
    ("sarranid_crusaders", "Jihadists", icon.sarranid_elites|carries_goods(2)|pf_show_faction, 0, fac.kingdom_6, soldier_personality, [(trp.sarranid_bey,2,3),(trp.sarranid_ghazi,4,8),(trp.sarranid_spahbod,4,8)] ),
    ("sarranid_prisoner_train", "Prisoner Train", icon.gray_knight|carries_goods(5)|pf_show_faction, 0, fac.kingdom_6, merchant_personality, [(trp.sarranid_janissary,5,10),(trp.sarranid_dervish,6,8),(trp.sarranid_akinci,7,12),(trp.bandit,10,24,pmf_is_prisoner)] ),
    ("mamlukes","Jihadists",icon.sarranid_elites|carries_goods(2)|pf_show_faction,0,fac.kingdom_6,soldier_personality,[(trp.sarranid_mamluke,3,3),(trp.sarranid_siphai,7,10),(trp.sarranid_dervish,10,12)]),





    ("default_prisoners","Default Prisoners",0,0,fac.commoners,0,[(trp.brigand,5,10,pmf_is_prisoner)]),
    # end NE

    # ("scout_party","Scouts",icon.gray_knight|carries_goods(1)|pf_show_faction,0,fac.commoners,bandit_personality,[]),
    # ("patrol_party","Patrol",icon.gray_knight|carries_goods(2)|pf_show_faction,0,fac.commoners,soldier_personality,[]),
    #####("war_party", "War Party",icon.gray_knight|carries_goods(3),0,fac.commoners,soldier_personality,[]),
    # ("messenger_party","Messenger",icon.gray_knight|pf_show_faction,0,fac.commoners,merchant_personality,[]),
    # ("raider_party","Raiders",icon.gray_knight|carries_goods(16)|pf_quest_party,0,fac.commoners,bandit_personality,[]),
    # ("raider_captives","Raider Captives",0,0,fac.commoners,0,[(trp.peasant_woman,6,30,pmf_is_prisoner)]),
    # ("kingdom_caravan_party","Caravan",icon.mule|carries_goods(25)|pf_show_faction,0,fac.commoners,merchant_personality,[(trp.caravan_master,1,1),(trp.caravan_guard,12,40)]),
    ("prisoner_train_party","Prisoner Train",icon.gray_knight|carries_goods(5)|pf_show_faction,0,fac.commoners,merchant_personality,[]),
    # ("default_prisoners","Default Prisoners",0,0,fac.commoners,0,[(trp.bandit,5,10,pmf_is_prisoner)]),

    ("routed_warriors","Routed Enemies",icon.vaegir_knight,0,fac.commoners,soldier_personality,[]),


    # Caravans
    #("center_reinforcements","Reinforcements",icon.axeman|carries_goods(16),0,fac.commoners,soldier_personality,[(trp.townsman,5,30),(trp.watchman,4,20)]),

    ("kingdom_hero_party","War Party",icon.flagbearer_a|pf_show_faction|pf_default_behavior,0,fac.commoners,soldier_personality,[]),

    # Reinforcements
    # each faction includes three party templates. One is less-modernised, one is med-modernised and one is high-modernised
    # less-modernised templates are generally includes 7-14 troops in total,
    # med-modernised templates are generally includes 5-10 troops in total,
    # high-modernised templates are generally includes 3-5 troops in total

    # ("kingdom_1_reinforcements_a", "{!}kingdom_1_reinforcements_a", 0, 0, fac.commoners, 0, [(trp.swadian_recruit,5,10),(trp.swadian_militia,2,4)]),
    # ("kingdom_1_reinforcements_b", "{!}kingdom_1_reinforcements_b", 0, 0, fac.commoners, 0, [(trp.swadian_footman,3,6),(trp.swadian_skirmisher,2,4)]),
    # ("kingdom_1_reinforcements_c", "{!}kingdom_1_reinforcements_c", 0, 0, fac.commoners, 0, [(trp.swadian_man_at_arms,2,4),(trp.swadian_crossbowman,1,2)]), #Swadians are a bit less-powered thats why they have a bit more troops in their modernised party template (3-6, others 3-5)

    # ("kingdom_2_reinforcements_a", "{!}kingdom_2_reinforcements_a", 0, 0, fac.commoners, 0, [(trp.vaegir_recruit,5,10),(trp.vaegir_footman,2,4)]),
    # ("kingdom_2_reinforcements_b", "{!}kingdom_2_reinforcements_b", 0, 0, fac.commoners, 0, [(trp.vaegir_veteran,2,4),(trp.vaegir_skirmisher,2,4),(trp.vaegir_footman,1,2)]),
    # ("kingdom_2_reinforcements_c", "{!}kingdom_2_reinforcements_c", 0, 0, fac.commoners, 0, [(trp.vaegir_horseman,2,3),(trp.vaegir_infantry,1,2)]),

    # ("kingdom_3_reinforcements_a", "{!}kingdom_3_reinforcements_a", 0, 0, fac.commoners, 0, [(trp.khergit_tribesman,3,5),(trp.khergit_skirmisher,4,9)]), #Khergits are a bit less-powered thats why they have a bit more 2nd upgraded(trp.khergit_skirmisher) than non-upgraded one(trp.khergit_tribesman).
    # ("kingdom_3_reinforcements_b", "{!}kingdom_3_reinforcements_b", 0, 0, fac.commoners, 0, [(trp.khergit_horseman,2,4),(trp.khergit_horse_archer,2,4),(trp.khergit_skirmisher,1,2)]),
    # ("kingdom_3_reinforcements_c", "{!}kingdom_3_reinforcements_c", 0, 0, fac.commoners, 0, [(trp.khergit_horseman,2,4),(trp.khergit_veteran_horse_archer,2,3)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

    # ("kingdom_4_reinforcements_a", "{!}kingdom_4_reinforcements_a", 0, 0, fac.commoners, 0, [(trp.nord_footman,5,10),(trp.nord_recruit,2,4)]),
    # ("kingdom_4_reinforcements_b", "{!}kingdom_4_reinforcements_b", 0, 0, fac.commoners, 0, [(trp.nord_huntsman,2,5),(trp.nord_archer,2,3),(trp.nord_footman,1,2)]),
    # ("kingdom_4_reinforcements_c", "{!}kingdom_4_reinforcements_c", 0, 0, fac.commoners, 0, [(trp.nord_warrior,3,5)]),

    # ("kingdom_5_reinforcements_a", "{!}kingdom_5_reinforcements_a", 0, 0, fac.commoners, 0, [(trp.rhodok_tribesman,5,10),(trp.rhodok_spearman,2,4)]),
    # ("kingdom_5_reinforcements_b", "{!}kingdom_5_reinforcements_b", 0, 0, fac.commoners, 0, [(trp.rhodok_crossbowman,3,6),(trp.rhodok_trained_crossbowman,2,4)]),
    # ("kingdom_5_reinforcements_c", "{!}kingdom_5_reinforcements_c", 0, 0, fac.commoners, 0, [(trp.rhodok_veteran_spearman,2,3),(trp.rhodok_veteran_crossbowman,1,2)]),

    ######NE
    # Begin NE 600 series standardized reinforcement packs
    ("kingdom_1_reinforcements_a", "{!}kingdom_1_reinforcements_a", 0, 0, fac.commoners, 0, [(trp.swadian_recruit,4,9),(trp.swadian_proselyte,3,8),(trp.swadian_page,2,7),(trp.swadian_skirmisher,1,6)] ),
    ("kingdom_1_reinforcements_b", "{!}kingdom_1_reinforcements_b", 0, 0, fac.commoners, 0, [(trp.swadian_infantry,3,8),(trp.swadian_veteran_crossbowman,2,7), (trp.swadian_pikeman,1,6)] ),
    ("kingdom_1_reinforcements_c", "{!}kingdom_1_reinforcements_c", 0, 0, fac.commoners, 0, [(trp.swadian_knight,2,7), (trp.swadian_captain,1,6)] ),

    ("kingdom_2_reinforcements_a", "{!}kingdom_2_reinforcements_a", 0, 0, fac.commoners, 0, [(trp.vaegir_recruit,4,9),(trp.vaegir_footman,3,8),(trp.vaegir_scout,2,7),(trp.vaegir_bowman,1,6)] ),
    ("kingdom_2_reinforcements_b", "{!}kingdom_2_reinforcements_b", 0, 0, fac.commoners, 0, [(trp.vaegir_sergeant,3,8),(trp.vaegir_pikeman,2,7),(trp.vaegir_archer,1,6)] ),
    ("kingdom_2_reinforcements_c", "{!}kingdom_2_reinforcements_c", 0, 0, fac.commoners, 0, [(trp.vaegir_master_bowyer,2,7), (trp.vaegir_druzhina,1,6)] ),

    ("kingdom_3_reinforcements_a", "{!}kingdom_3_reinforcements_a", 0, 0, fac.commoners, 0, [(trp.khergit_tribesman,4,9),(trp.khergit_kharash,3,8),(trp.khergit_rider,2,7), (trp.khergit_kharash_scout,1,6)]),
    ("kingdom_3_reinforcements_b", "{!}kingdom_3_reinforcements_b", 0, 0, fac.commoners, 0, [(trp.khergit_scarred_kharash,3,8),(trp.khergit_horse_archer,2,7),(trp.khergit_lancer,1,6)]),
    ("kingdom_3_reinforcements_c", "{!}kingdom_3_reinforcements_c", 0, 0, fac.commoners, 0, [(trp.khergit_tribal_chieftain,2,7), (trp.khergit_mangudai,1,6)]),

    ("kingdom_4_reinforcements_a", "{!}kingdom_4_reinforcements_a", 0, 0, fac.commoners, 0, [(trp.nord_recruit,4,9),(trp.nord_drengr,3,8),(trp.nord_warrior,2,7),(trp.nord_raiding_hunter,1,6)] ),
    ("kingdom_4_reinforcements_b", "{!}kingdom_4_reinforcements_b", 0, 0, fac.commoners, 0, [(trp.nord_raiding_marksman,3,8),(trp.nord_shieldmaster,2,7),(trp.nord_veteran_warrior,1,6)] ),
    ("kingdom_4_reinforcements_c", "{!}kingdom_4_reinforcements_c", 0, 0, fac.commoners, 0, [(trp.nord_housecarl,2,7),(trp.nord_berserker,1,6)] ),

    ("kingdom_5_reinforcements_a", "{!}kingdom_5_reinforcements_a", 0, 0, fac.commoners, 0, [(trp.rhodok_tribesman,4,9),(trp.rhodok_spearman,3,8),(trp.rhodok_reservist,2,7),(trp.rhodok_skirmisher,1,6)] ),
    ("kingdom_5_reinforcements_b", "{!}kingdom_5_reinforcements_b", 0, 0, fac.commoners, 0, [(trp.rhodok_crossbowman,3,8),(trp.rhodok_scout,2,7),(trp.rhodok_veteran_spearman,1,6)] ),
    ("kingdom_5_reinforcements_c", "{!}kingdom_5_reinforcements_c", 0, 0, fac.commoners, 0, [(trp.rhodok_armsman,2,7),(trp.rhodok_councilman,1,6)] ),

    ("dark_knights_reinforcements_a", "{!}dark_knights_reinforcements_a", 0, 0, fac.commoners, 0, [(trp.dark_page,14,16),(trp.dark_skirmisher,8,10),(trp.dark_squire,8,10)]),
    ("dark_knights_reinforcements_b", "{!}dark_knights_reinforcements_b", 0, 0, fac.commoners, 0, [(trp.dark_marksman,7,9),(trp.dark_champion,7,9),(trp.dark_knight_master,8,10)]),
    ("dark_knights_reinforcements_c", "{!}dark_knights_reinforcements_c", 0, 0, fac.commoners, 0, [(trp.blackguard,3,5),(trp.dark_ranger,3,5),(trp.unholy_crusader,5,7)]),

    ("kingdom_6_reinforcements_a", "{!}kingdom_6_reinforcements_a", 0, 0, fac.commoners, 0, [(trp.sarranid_recruit,4,9),(trp.sarranid_azap,3,8),(trp.sarranid_seyman,2,7),(trp.sarranid_janissary,1,6)]),
    ("kingdom_6_reinforcements_b", "{!}kingdom_6_reinforcements_b", 0, 0, fac.commoners, 0, [(trp.sarranid_akinci,3,8),(trp.sarranid_kamandaran,2,7),(trp.sarranid_timariot,1,6)]),
    ("kingdom_6_reinforcements_c", "{!}kingdom_6_reinforcements_c", 0, 0, fac.commoners, 0, [(trp.sarranid_eunuch,2,7),(trp.sarranid_siphai,1,6)]),
    # End NE 600 series stanardized reinforcement packs

    # NE 2
    # ("kingdom_1_reinforcements_a", "{!}kingdom_1_reinforcements_a", 0, 0, fac.commoners, 0, [(trp.swadian_infantry,4,7),(trp.swadian_page,2,4),(trp.swadian_militia,2,6)]),
    # ("kingdom_1_reinforcements_b", "{!}kingdom_1_reinforcements_b", 0, 0, fac.commoners, 0, [(trp.swadian_sharpshooter,4,7),(trp.swadian_crossbowman,2,6),(trp.watchman,0,3)]),
    # ("kingdom_1_reinforcements_c", "{!}kingdom_1_reinforcements_c", 0, 0, fac.commoners, 0, [(trp.swadian_knight,3,6)]),

    # ("kingdom_2_reinforcements_a", "{!}kingdom_2_reinforcements_a", 0, 0, fac.commoners, 0, [(trp.vaegir_footman,2,6),(trp.vaegir_infantry,4,7),(trp.vaegir_clanelder,2,4)]),
    # ("kingdom_2_reinforcements_b", "{!}kingdom_2_reinforcements_b", 0, 0, fac.commoners, 0, [(trp.vaegir_archer,2,6),(trp.vaegir_marksman,1,3),(trp.watchman,0,3)]),
    # ("kingdom_2_reinforcements_c", "{!}kingdom_2_reinforcements_c", 0, 0, fac.commoners, 0, [(trp.vaegir_knight,3,6)]),

    # ("kingdom_3_reinforcements_a", "{!}kingdom_3_reinforcements_a", 0, 0, fac.commoners, 0, [(trp.khergit_skirmisher,2,6),(trp.khergit_lancer,4,7),(trp.khergit_tribe,2,4)]),
    # ("kingdom_3_reinforcements_b", "{!}kngdom_3_reinforcements_b", 0, 0, fac.commoners, 0, [(trp.khergit_veteran_horse_archer,2,6),(trp.khergit_keshik,4,7),(trp.watchman,0,3)]),
    # ("kingdom_3_reinforcements_c", "{!}kingdom_3_reinforcements_c", 0, 0, fac.commoners, 0, [(trp.khergit_tarkan,3,6)]),

    # ("kingdom_4_reinforcements_a", "{!}kingdom_4_reinforcements_a", 0, 0, fac.commoners, 0, [(trp.nord_recruit,4,8),(trp.nord_trained_footman,2,4),(trp.nord_cavalry,2,4)]),
    # ("kingdom_4_reinforcements_b", "{!}kingdom_4_reinforcements_b", 0, 0, fac.commoners, 0, [(trp.nord_huntsman,3,5),(trp.nord_raider_archer,2,5),(trp.watchman,0,3)]),
    # ("kingdom_4_reinforcements_c", "{!}kingdom_4_reinforcements_c", 0, 0, fac.commoners, 0, [(trp.nord_cavalry,3,6)]),

    # ("kingdom_5_reinforcements_a", "{!}kingdom_5_reinforcements_a", 0, 0, fac.commoners, 0, [(trp.rhodok_spearman,3,7),(trp.rhodok_tribesman,3,6),(trp.rhodok_elder,2,4)]),
    # ("kingdom_5_reinforcements_b", "{!}kingdom_5_reinforcements_b", 0, 0, fac.commoners, 0, [(trp.rhodok_trained_crossbowman,2,6),(trp.rhodok_sergeant,4,7),(trp.watchman,0,3)]),
    # ("kingdom_5_reinforcements_c", "{!}kingdom_5_reinforcements_c", 0, 0, fac.commoners, 0, [(trp.rhodok_crossbowman,3,6)]),

    # ("dark_knights_reinforcements_a", "{!}dark_knights_reinforcements_a", 0, 0, fac.commoners, 0, [(trp.dark_page,14,16),(trp.dark_skirmisher,8,10),(trp.dark_squire,8,10)]),
    # ("dark_knights_reinforcements_b", "{!}dark_knights_reinforcements_b", 0, 0, fac.commoners, 0, [(trp.dark_marksman,7,9),(trp.dark_champion,7,9),(trp.dark_knight_master,8,10)]),
    # ("dark_knights_reinforcements_c", "{!}dark_knights_reinforcements_c", 0, 0, fac.commoners, 0, [(trp.blackguard,3,5),(trp.dark_ranger,3,5),(trp.unholy_crusader,5,7)]),



    # ("kingdom_6_reinforcements_a", "{!}kingdom_6_reinforcements_a", 0, 0, fac.commoners, 0, [(trp.sarranid_recruit,5,10),(trp.sarranid_footman,2,4)]),
    # ("kingdom_6_reinforcements_b", "{!}kingdom_6_reinforcements_b", 0, 0, fac.commoners, 0, [(trp.sarranid_skirmisher,2,4),(trp.sarranid_veteran_footman,2,3),(trp.sarranid_footman,1,3)]),
    # ("kingdom_6_reinforcements_c", "{!}kingdom_6_reinforcements_c", 0, 0, fac.commoners, 0, [(trp.sarranid_horseman,3,5)]),

    # end NE 2






    ##  ("kingdom_1_reinforcements_a", "kingdom_1_reinforcements_a", 0, 0, fac.commoners, 0, [(trp.swadian_footman,3,7),(trp.swadian_skirmisher,5,10),(trp.swadian_militia,11,26)]),
    ##  ("kingdom_1_reinforcements_b", "kingdom_1_reinforcements_b", 0, 0, fac.commoners, 0, [(trp.swadian_man_at_arms,5,10),(trp.swadian_infantry,5,10),(trp.swadian_crossbowman,3,8)]),
    ##  ("kingdom_1_reinforcements_c", "kingdom_1_reinforcements_c", 0, 0, fac.commoners, 0, [(trp.swadian_knight,2,6),(trp.swadian_sergeant,2,5),(trp.swadian_sharpshooter,2,5)]),
    ##
    ##  ("kingdom_2_reinforcements_a", "kingdom_2_reinforcements_a", 0, 0, fac.commoners, 0, [(trp.vaegir_veteran,3,7),(trp.vaegir_skirmisher,5,10),(trp.vaegir_footman,11,26)]),
    ##  ("kingdom_2_reinforcements_b", "kingdom_2_reinforcements_b", 0, 0, fac.commoners, 0, [(trp.vaegir_horseman,4,9),(trp.vaegir_infantry,5,10),(trp.vaegir_archer,3,8)]),
    ##  ("kingdom_2_reinforcements_c", "kingdom_2_reinforcements_c", 0, 0, fac.commoners, 0, [(trp.vaegir_knight,3,7),(trp.vaegir_guard,2,5),(trp.vaegir_marksman,2,5)]),
    ##
    ##  ("kingdom_3_reinforcements_a", "kingdom_3_reinforcements_a", 0, 0, fac.commoners, 0, [(trp.khergit_horseman,3,7),(trp.khergit_skirmisher,5,10),(trp.khergit_tribesman,11,26)]),
    ##  ("kingdom_3_reinforcements_b", "kingdom_3_reinforcements_b", 0, 0, fac.commoners, 0, [(trp.khergit_veteran_horse_archer,4,9),(trp.khergit_horse_archer,5,10),(trp.khergit_horseman,3,8)]),
    ##  ("kingdom_3_reinforcements_c", "kingdom_3_reinforcements_c", 0, 0, fac.commoners, 0, [(trp.khergit_lancer,3,7),(trp.khergit_veteran_horse_archer,2,5),(trp.khergit_horse_archer,2,5)]),
    ##
    ##  ("kingdom_4_reinforcements_a", "kingdom_4_reinforcements_a", 0, 0, fac.commoners, 0, [(trp.nord_trained_footman,3,7),(trp.nord_footman,5,10),(trp.nord_recruit,11,26)]),
    ##  ("kingdom_4_reinforcements_b", "kingdom_4_reinforcements_b", 0, 0, fac.commoners, 0, [(trp.nord_veteran,4,9),(trp.nord_warrior,5,10),(trp.nord_footman,3,8)]),
    ##  ("kingdom_4_reinforcements_c", "kingdom_4_reinforcements_c", 0, 0, fac.commoners, 0, [(trp.nord_champion,1,3),(trp.nord_veteran,2,5),(trp.nord_warrior,2,5)]),
    ##
    ##  ("kingdom_5_reinforcements_a", "kingdom_5_reinforcements_a", 0, 0, fac.commoners, 0, [(trp.rhodok_spearman,3,7),(trp.rhodok_crossbowman,5,10),(trp.rhodok_tribesman,11,26)]),
    ##  ("kingdom_5_reinforcements_b", "kingdom_5_reinforcements_b", 0, 0, fac.commoners, 0, [(trp.rhodok_trained_spearman,4,9),(trp.rhodok_spearman,5,10),(trp.rhodok_crossbowman,3,8)]),
    ##  ("kingdom_5_reinforcements_c", "kingdom_5_reinforcements_c", 0, 0, fac.commoners, 0, [(trp.rhodok_sergeant,3,7),(trp.rhodok_veteran_spearman,2,5),(trp.rhodok_veteran_crossbowman,2,5)]),



    ("steppe_bandit_lair" ,"Steppe Bandit Lair",icon.bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac.neutral,bandit_personality,[(trp.steppe_bandit,15,58)]),
    ("taiga_bandit_lair","Tundra Bandit Lair",icon.bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac.neutral,bandit_personality,[(trp.taiga_bandit,15,58)]),
    ("desert_bandit_lair" ,"Desert Bandit Lair",icon.bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac.neutral,bandit_personality,[(trp.desert_bandit,15,58)]),
    ("forest_bandit_lair" ,"Forest Bandit Camp",icon.bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac.neutral,bandit_personality,[(trp.forest_bandit,15,58)]),
    ("mountain_bandit_lair" ,"Mountain Bandit Hideout",icon.bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac.neutral,bandit_personality,[(trp.mountain_bandit,15,58)]),
    ("sea_raider_lair","Sea Raider Landing",icon.bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac.neutral,bandit_personality,[(trp.sea_raider,15,50)]),
    ("looter_lair","Kidnappers' Hideout",icon.bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac.neutral,bandit_personality,[(trp.looter,15,25)]),

    ("bandit_lair_templates_end","{!}bandit_lair_templates_end",icon.axeman|carries_goods(2)|pf_is_static,0,fac.outlaws,bandit_personality,[(trp.sea_raider,15,50)]),

    ("leaded_looters","Band of robbers",icon.axeman|carries_goods(8)|pf_quest_party,0,fac.neutral,bandit_personality,[(trp.looter_leader,1,1),(trp.looter,3,3)]),

    ("town",    "Town",    icon.town|pf_label_large|     pf_is_static|pf_always_visible|pf_show_faction,   0, fac.no_faction, 0, []),
    ("castle",  "Castle",  icon.castle_a|pf_label_medium|pf_is_static|pf_always_visible|pf_show_faction,   0, fac.no_faction, 0, []),
    ("village", "Village", icon.village_a|pf_label_small|pf_is_static|pf_always_visible|pf_hide_defenders, 0, fac.no_faction, 0, []),
    ("bridge",  "Bridge",  icon.bridge_a|pf_no_label|    pf_is_static|pf_always_visible,                   0, fac.no_faction, 0, []),
    ("grounds", "Grounds", icon.training_ground|pf_label_medium|pf_hide_defenders|pf_is_static|pf_always_visible, 0, fac.no_faction, 0, []),

]

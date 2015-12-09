from compiler import *

####################################################################################################################
#  Each troop contains the following fields:
#  1) Troop id (string): used for referencing troops in other files. The prefix trp_ is automatically added before each troop-id .
#  2) Toop name (string).
#  3) Plural troop name (string).
#  4) Troop flags (int). See header_troops.py for a list of available flags
#  5) Scene (int) (only applicable to heroes) For example: scn.reyvadin_castle|entry(1) puts troop in reyvadin castle's first entry point
#  6) Reserved (int). Put constant "reserved" or 0.
#  7) Faction (int)
#  8) Inventory (list): Must be a list of items
#  9) Attributes (int): Example usage:
#           str_6|agi_6|int_4|cha_5|level(5)
# 10) Weapon proficiencies (int): Example usage:
#           wp_one_handed(55)|wp_two_handed(90)|wp_polearm(36)|wp_archery(80)|wp_crossbow(24)|wp_throwing(45)
#     The function wp(x) will create random weapon proficiencies close to value x.
#     To make an expert archer with other weapon proficiencies close to 60 you can use something like:
#           wp_archery(160) | wp(60)
# 11) Skills (int): See header_skills.py to see a list of skills. Example:
#           knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2
# 12) Face code (int): You can obtain the face code by pressing ctrl+E in face generator screen
# 13) Face code (int)(2) (only applicable to regular troops, can be omitted for heroes):
#     The game will create random faces between Face code 1 and face code 2 for generated troops
# 14) Troop image (string): If this variable is set, the troop will use an image rather than its 3D visual during the conversations
#  town_1   Sargoth
#  town_2   Tihr
#  town_3   Veluca
#  town_4   Suno
#  town_5   Jelkala
#  town_6   Praven
#  town_7   Uxkhal
#  town_8   Reyvadin
#  town_9   Khudan
#  town_10  Tulga
#  town_11  Curaw
#  town_12  Wercheg
#  town_13  Rivacheg
#  town_14  Halmar
####################################################################################################################

# Some constant and function declarations to be used below...
# wp_one_handed () | wp_two_handed () | wp_polearm () | wp_archery () | wp_crossbow () | wp_throwing ()
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

#Skills
knows_common = knows_riding_1|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1
def_attrib = str_7 | agi_5 | int_4 | cha_4


# NE kings
#knows_lord_1 = knows_riding_3|knows_trade_2|knows_inventory_management_2|knows_tactics_4|knows_prisoner_management_4|knows_leadership_7
knows_lord_1 = knows_trade_2|knows_inventory_management_2|knows_tactics_4|knows_prisoner_management_4|knows_leadership_7
knows_king = knows_ironflesh_10|knows_power_strike_10|knows_riding_10
# NE end kings

knows_warrior_npc = knows_weapon_master_2|knows_ironflesh_1|knows_athletics_1|knows_power_strike_2|knows_riding_2|knows_shield_1|knows_inventory_management_2
knows_merchant_npc = knows_riding_2|knows_trade_3|knows_inventory_management_3 #knows persuasion
knows_tracker_npc = knows_weapon_master_1|knows_athletics_2|knows_spotting_2|knows_pathfinding_2|knows_tracking_2|knows_ironflesh_1|knows_inventory_management_2

lord_attrib = str_20|agi_20|int_20|cha_20|level(38)
# NE lord attribs
new_lord_attrib = str_30|agi_24|int_16|cha_18|level(26)
jarl_attrib = str_30|agi_24|int_16|cha_18|level(26)
# NE end lord attrib

knight_attrib_1 = str_15|agi_14|int_8|cha_16|level(22)
knight_attrib_2 = str_16|agi_16|int_10|cha_18|level(26)
knight_attrib_3 = str_18|agi_17|int_12|cha_20|level(30)
knight_attrib_4 = str_19|agi_19|int_13|cha_22|level(35)
knight_attrib_5 = str_20|agi_20|int_15|cha_25|level(41)
knight_skills_1 = knows_riding_3|knows_ironflesh_2|knows_power_strike_3|knows_athletics_1|knows_tactics_2|knows_prisoner_management_1|knows_leadership_3
knight_skills_2 = knows_riding_4|knows_ironflesh_3|knows_power_strike_4|knows_athletics_2|knows_tactics_3|knows_prisoner_management_2|knows_leadership_5
knight_skills_3 = knows_riding_5|knows_ironflesh_4|knows_power_strike_5|knows_athletics_3|knows_tactics_4|knows_prisoner_management_2|knows_leadership_6
knight_skills_4 = knows_riding_6|knows_ironflesh_5|knows_power_strike_6|knows_athletics_4|knows_tactics_5|knows_prisoner_management_3|knows_leadership_7
knight_skills_5 = knows_riding_7|knows_ironflesh_6|knows_power_strike_7|knows_athletics_5|knows_tactics_6|knows_prisoner_management_3|knows_leadership_9

#These face codes are generated by the in-game face generator.
#Enable edit mode and press ctrl+E in face generator screen to obtain face codes.


reserved = 0

no_scene = 0

man_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
man_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
man_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
man_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
man_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

man_face_younger_2 = 0x000000003f0052064deeffffffffffff00000000001efff90000000000000000
man_face_young_2   = 0x00000003bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_middle_2  = 0x00000007bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_old_2     = 0x0000000bff0052064deeffffffffffff00000000001efff90000000000000000
man_face_older_2   = 0x0000000fff0052064deeffffffffffff00000000001efff90000000000000000

# Previous face definitions

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

# Nemchenk's face definitions

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



merchant_face_1    = man_face_young_1
merchant_face_2    = man_face_older_2

woman_face_1    = 0x0000000000000001000000000000000000000000001c00000000000000000000
woman_face_2    = 0x00000003bf0030067ff7fbffefff6dff00000000001f6dbf0000000000000000

swadian_woman_face_1 = 0x0000000180102006124925124928924900000000001c92890000000000000000
swadian_woman_face_2 = 0x00000001bf1000061db6d75db6b6dbad00000000001c92890000000000000000

khergit_woman_face_1 = 0x0000000180103006124925124928924900000000001c92890000000000000000
khergit_woman_face_2 = 0x00000001af1030025b6eb6dd6db6dd6d00000000001eedae0000000000000000

refugee_face1 = woman_face_1
refugee_face2 = woman_face_2
girl_face1    = woman_face_1
girl_face2    = woman_face_2

mercenary_face_1 = 0x0000000000000000000000000000000000000000001c00000000000000000000
mercenary_face_2 = 0x0000000cff00730b6db6db6db7fbffff00000000001efffe0000000000000000

vaegir_face1  = vaegir_face_young_1
vaegir_face2  = vaegir_face_older_2

bandit_face1  = man_face_young_1
bandit_face2  = man_face_older_2

#v585 Josefgirl
bride_face1 = 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000
bride_face2 = 0x00000001ba104002321c68da9675c88c00000000001f37990000000000000000
bride_face3 = 0x000000003a0c000723cd68c263af473400000000001c00920000000000000000

scholar_face_1 = 0x0000000fc0000001124000000020000000000000001c00800000000000000000
scholar_face_2 = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
scholar_face_3 = 0x0000000fc0000001124000000020000000000000001c00800000000000000000
scholar_face_4 = 0x0000000ff100230c4deeffffffffffff00000000001efff90000000000000000
scholar_face_5 = 0x0000000fc0000001124000000020000000000000001c00800000000000000000
scholar_face_6 = 0x0000000fc0000001124000000020000000000000001c00800000000000000000
scholar_face_7 = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
scholar_face_8 = 0x0000000fc0000001124000000020000000000000001c00800000000000000000
scholar_face_9 = 0x0000000fff0052064deeffffffffffff00000000001efff90000000000000000
scholar_face_10 = 0x0000000fff0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
scholar_face_11 = 0x0000000ff10023084deeffffffffffff00000000001efff90000000000000000
# v585 Josef

undead_face1  = 0x00000000002000000000000000000000
undead_face2  = 0x000000000020010000001fffffffffff

#NAMES:
#

troops = [

  ["player","Player","Player",tf_hero|tf_unmoveable_in_party_window,no_scene,reserved,fac.player_faction,[itm.hunting_crossbow,itm.bolts],level(1)|str_6|agi_6|int_6|cha_6,wp(30),0,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_male","multiplayer_profile_troop_male","multiplayer_profile_troop_male", tf_hero|tf_guarantee_all, 0, 0,fac.commoners,[itm.leather_jerkin,itm.leather_boots],0,0,0,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_female","multiplayer_profile_troop_female","multiplayer_profile_troop_female", tf_hero|tf_female|tf_guarantee_all, 0, 0,fac.commoners,[itm.tribal_warrior_outfit,itm.leather_boots],0,0,0,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["temp_troop","Temp Troop","Temp Troop",tf_hero,no_scene,reserved,fac.commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],

  ####################################################################################################################
  # Troops before this point are hardwired into the game and their order should not be changed!
  ####################################################################################################################

  # NE kingdom - DEPRECATED
  ["player_kingdom_name","Change this to your kingdom name","name",0,0,reserved,fac.commoners,[],1,0,0,0],
  # NE end kingdom
  ["find_item_cheat","find_item_cheat","find_item_cheat",tf_hero|tf_is_merchant,no_scene,reserved,fac.commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["random_town_sequence","Random Town Sequence","Random Town Sequence",tf_hero,no_scene,reserved,fac.commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["tournament_participants","Tournament Participants","Tournament Participants",tf_hero,no_scene,reserved,fac.commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],



  ["novice_fighter","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,[itm.hide_boots],level(5)|str_6|agi_6,wp(60),knows_common,mercenary_face_1,mercenary_face_2],
  ["regular_fighter","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,[itm.hide_boots],level(11)|str_8|agi_8,wp(90),knows_common|knows_ironflesh_1|knows_power_strike_1|knows_athletics_1|knows_riding_1|knows_shield_2,mercenary_face_1,mercenary_face_2],
  ["veteran_fighter","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,0,fac.commoners,[itm.hide_boots],level(17)|str_10|agi_10,wp(110),knows_common|knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2|knows_shield_3,mercenary_face_1,mercenary_face_2],
  ["champion_fighter","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,[itm.hide_boots],level(22)|str_12|agi_11,wp(140),knows_common|knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_riding_3|knows_shield_4,mercenary_face_1,mercenary_face_2],

  ["arena_training_fighter_1","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,[itm.hide_boots],level(5)|str_6|agi_6,wp(60),knows_common,mercenary_face_1,mercenary_face_2],
  ["arena_training_fighter_2","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,[itm.hide_boots],level(7)|str_7|agi_6,wp(70),knows_common,mercenary_face_1,mercenary_face_2],
  ["arena_training_fighter_3","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,[itm.hide_boots],level(9)|str_8|agi_7,wp(80),knows_common,mercenary_face_1,mercenary_face_2],
  ["arena_training_fighter_4","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,[itm.hide_boots],level(11)|str_8|agi_8,wp(90),knows_common,mercenary_face_1,mercenary_face_2],
  ["arena_training_fighter_5","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,[itm.hide_boots],level(13)|str_9|agi_8,wp(100),knows_common,mercenary_face_1,mercenary_face_2],
  ["arena_training_fighter_6","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,[itm.hide_boots],level(15)|str_10|agi_9,wp(110),knows_common,mercenary_face_1,mercenary_face_2],
  ["arena_training_fighter_7","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,[itm.hide_boots],level(17)|str_10|agi_10,wp(120),knows_common,mercenary_face_1,mercenary_face_2],
  ["arena_training_fighter_8","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,[itm.hide_boots],level(19)|str_11|agi_10,wp(130),knows_common,mercenary_face_1,mercenary_face_2],
  ["arena_training_fighter_9","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,[itm.hide_boots],level(21)|str_12|agi_11,wp(140),knows_common,mercenary_face_1,mercenary_face_2],
  ["arena_training_fighter_10","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,[itm.hide_boots],level(23)|str_12|agi_12,wp(150),knows_common,mercenary_face_1,mercenary_face_2],

  ["cattle","Cattle","Cattle",0,no_scene,reserved,fac.neutral, [], level(1)|def_attrib,wp(60),0,mercenary_face_1, mercenary_face_2],



  #soldiers:
  ["soldiers_begin", "{!}", "{!}marker", tf_hero|tf_inactive, 0, 0, fac.no_faction, [], 0, 0, knows_inventory_management_10, 0],

  ["farmer", "Farmer", "Farmers", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac.commoners, [
    itm.linen_tunic,itm.coarse_tunic,itm.wrapping_boots,itm.ankle_boots,itm.nomad_boots,itm.common_hood,itm.straw_hat,itm.woolen_cap,itm.felt_hat,
    itm.donkey_a,itm.donkey_b,itm.mule,itm.farm_horse,
    itm.stones,
    itm.scythe,itm.pitch_fork,itm.pickaxe,itm.staff,itm.peasant_knife,itm.butchering_knife,itm.cleaver,itm.wooden_stick,itm.club,itm.cudgel,itm.smith_hammer,itm.hatchet,itm.beef_splitter,itm.sickle,
  ], level(6)|str_12|agi_9|int_6|cha_6, wpex(30,30,30,30,30,30), 0, man_face_young_1, man_face_old_2 ],

  ["caravan_guard","Caravan Guard","Caravan Guards",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield,no_scene,0,fac.commoners,[
    itm.leather_armor,itm.padded_leather,itm.studded_leather_coat,itm.vaegir_inf_armor_a,itm.steppe_armor,itm.nordic_archer_armor_a,itm.nomad_boots,itm.hunter_boots,itm.hide_boots,itm.light_leather_boots,itm.leather_boots,itm.leather_gloves,itm.leather_gloves,itm.leather_gloves,itm.mail_gauntlets,itm.leather_cap,itm.skullcap,itm.footman_helmet,itm.segmented_helmet,itm.mail_coif,
    itm.shield_common_round_d,
    itm.sword_norman,itm.sword_medieval_d,itm.boar_spear,itm.spear,itm.war_spear,itm.shortened_military_scythe,
    itm.riding_horse,
  ], level(14)|str_15|agi_14|int_6|cha_6,wp(85),knows_common|knows_riding_2|knows_ironflesh_1|knows_shield_3,mercenary_face_1,mercenary_face_2],

  ["mercenary_rabble", "Mercenary Rabble", "Mercenary Rabble", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, no_scene, reserved, fac.commoners, [
    itm.ragged_outfit,itm.leather_jacket,itm.pelt_coat,itm.rawhide_coat,itm.leather_vest,itm.padded_cloth,itm.aketon_green,itm.leather_jerkin,itm.nomad_vest,itm.tribal_warrior_outfit,itm.nomad_robe,itm.light_leather,itm.hide_boots,itm.light_leather_boots,itm.leather_gloves,itm.padded_coif,itm.leather_steppe_cap_a,itm.fur_hat,
    itm.mercenary_shield_a,
    itm.hammer,itm.spiked_club,itm.club_with_spike_head,itm.falchion_new,itm.sword_medieval_b_small,itm.sword_viking_a_small,itm.skirmisher_pick,itm.sword_medieval_c_small,
  ], level(10)|str_13|agi_12|int_6|cha_6, wpex(75,30,30,75,30,30), knows_weapon_master_3|knows_ironflesh_3|knows_power_strike_2, mercenary_face_1, mercenary_face_2 ],

  ["mercenary_watchman", "Mercenary Watchman", "Mercenary Watchmen", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.commoners, [
    itm.light_leather,itm.leather_armor,itm.padded_leather,itm.light_leather_boots,itm.leather_boots,itm.splinted_greaves,itm.leather_gloves,itm.leather_cap,itm.nomad_cap_b,itm.leather_warrior_cap,
    itm.mercenary_shield_a,
    itm.winged_mace,itm.knobbed_mace,itm.flanged_mace,itm.spiked_mace,itm.one_handed_battle_axe_a,itm.one_handed_battle_axe_c,itm.khergit_sword_b,itm.military_pick,itm.sword_norman,itm.sword_medieval_d,itm.sword_medieval_c,
  ], level(14)|str_15|agi_14|int_6|cha_6, wpex(100,140,30,30,30,30), knows_shield_1|knows_athletics_4|knows_power_strike_5|knows_ironflesh_5|knows_weapon_master_3, mercenary_face_1, mercenary_face_2 ],

  ["mercenary_guard", "Mercenary Guard", "Mercenary Guard", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.commoners, [
    itm.padded_leather,itm.studded_leather_coat,itm.haubergeon,itm.mail_hauberk,itm.light_leather_boots,itm.leather_boots,itm.splinted_greaves,itm.leather_gloves,itm.skullcap,itm.footman_helmet,
    itm.mercenary_shield_b,
    itm.lineman_mace,itm.mace_small_d,itm.winged_mace_b,itm.one_handed_war_axe_a,itm.one_handed_war_axe_b,itm.one_handed_battle_axe_b,itm.sword_medieval_c_long,itm.sword_medieval_d_long,
  ], level(16)|str_16|agi_15|int_6|cha_6, wpex(140,180,30,30,30,30), knows_shield_2|knows_athletics_4|knows_power_strike_5|knows_ironflesh_5|knows_weapon_master_5, mercenary_face_1, mercenary_face_2 ],

  ["mercenary_swordsman", "Mercenary Swordsman", "Mercenary Swordsmen", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.commoners, [
    itm.haubergeon,itm.mail_hauberk,itm.mail_shirt,itm.mail_with_surcoat,itm.surcoat_over_mail,itm.splinted_greaves,itm.mail_chausses,itm.mail_boots,itm.mail_mittens,itm.norman_helmet,itm.rhodok_kettle_hat,
    itm.mercenary_shield_b,
    itm.sword_medieval_c_long,itm.sword_medieval_d_long,
  ], level(18)|str_18|agi_15|int_6|cha_6, wpex(200,180,30,30,30,30), knows_shield_3|knows_ironflesh_6|knows_power_strike_6|knows_weapon_master_5|knows_athletics_4, mercenary_face_1, mercenary_face_2 ],

  ["mercenary_zweihander", "Mercenary Zweihander", "Mercenary Zweihander", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.commoners, [
    itm.mail_shirt,itm.mail_with_surcoat,itm.surcoat_over_mail,itm.coat_of_plates,itm.coat_of_plates_red,itm.splinted_greaves,itm.mail_chausses,itm.mail_boots,itm.mail_mittens,itm.segmented_helmet,itm.mail_coif,itm.nasal_helmet,
    itm.bastard_sword_b,itm.sword_two_handed_b,itm.sword_two_handed_a,
    itm.goods_gold,
  ], level(24)|str_24|agi_15|int_6|cha_6, wpex(180,220,30,30,30,30), knows_athletics_5|knows_ironflesh_8|knows_power_strike_8|knows_weapon_master_5, mercenary_face_1, mercenary_face_2 ],

  ["mercenary_stablehand", "Mercenary Stablehand", "Mercenary Stablehands", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.commoners, [
    itm.light_leather,itm.leather_armor,itm.padded_leather,itm.light_leather_boots,itm.leather_boots,itm.splinted_greaves,itm.leather_gloves,itm.leather_cap,itm.nomad_cap_b,itm.leather_warrior_cap,
    itm.mercenary_shield_a,
    itm.boar_spear,itm.spear,itm.war_spear,itm.sword_norman,itm.sword_medieval_d,itm.sword_medieval_c,
    itm.farm_horse,itm.riding_horse,itm.khergit_horse,itm.sarranid_horse_a,itm.sarranid_horse_b,
  ], level(12)|str_13|agi_14|int_6|cha_6, wpex(120,90,100,30,30,30), knows_riding_3|knows_ironflesh_3|knows_shield_3|knows_power_strike_2|knows_weapon_master_4, mercenary_face_1, mercenary_face_2 ],

  ["mercenary_scout", "Mercenary Scout", "Mercenary Scouts", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.commoners, [
    itm.padded_leather,itm.studded_leather_coat,itm.haubergeon,itm.mail_hauberk,itm.light_leather_boots,itm.leather_boots,itm.splinted_greaves,itm.leather_gloves,itm.skullcap,itm.footman_helmet,
    itm.mercenary_shield_a,
    itm.war_spear,itm.light_lance,itm.khergit_sword_b,itm.sword_medieval_d,itm.sword_medieval_c,
    itm.riding_horse,itm.courser_horse,itm.hunter_horse,itm.khergit_horse,itm.sarranid_horse_a,itm.sarranid_horse_b,
  ], level(14)|str_14|agi_15|int_6|cha_6, wpex(145,90,120,30,30,30), knows_riding_3|knows_ironflesh_3|knows_shield_3|knows_power_strike_4|knows_weapon_master_4, mercenary_face_1, mercenary_face_2 ],

  ["mercenary_equite", "Mercenary Equite", "Mercenary Equite", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.commoners, [
    itm.haubergeon,itm.mail_hauberk,itm.mail_shirt,itm.mail_with_surcoat,itm.surcoat_over_mail,itm.splinted_greaves,itm.mail_chausses,itm.mail_boots,itm.mail_mittens,itm.norman_helmet,itm.rhodok_kettle_hat,
    itm.mercenary_shield_b,
    itm.light_lance,itm.cavalry_lance,itm.sword_medieval_c_long,itm.sword_medieval_d_long,
    itm.courser_horse,itm.hunter_horse,itm.armored_courser,itm.armored_hunter,
  ], level(18)|str_18|agi_15|int_6|cha_6, wpex(185,90,140,30,30,30), knows_riding_4|knows_ironflesh_3|knows_shield_4|knows_power_strike_5|knows_weapon_master_5, mercenary_face_1, mercenary_face_2 ],

  ["mercenary_cavalry", "Mercenary Cavalry", "Mercenary Cavalry", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.commoners, [
    itm.mail_shirt,itm.mail_with_surcoat,itm.surcoat_over_mail,itm.coat_of_plates,itm.coat_of_plates_red,itm.splinted_greaves,itm.mail_chausses,itm.mail_boots,itm.mail_mittens,itm.segmented_helmet,itm.mail_coif,itm.nasal_helmet,
    itm.mercenary_shield_c,
    itm.cavalry_lance,itm.great_lance,itm.sword_medieval_c_long,itm.sword_medieval_d_long,
    itm.armored_courser,itm.armored_hunter,itm.swadian_warhorse_a,itm.vaegir_warhorse_a,itm.khergit_warhorse_a,itm.nordic_warhorse_a,itm.rhodok_warhorse_a,itm.sarranid_warhorse_a,
    itm.goods_gold,
  ], level(22)|str_22|agi_15|int_6|cha_6, wpex(205,90,160,30,30,30), knows_riding_5|knows_ironflesh_4|knows_shield_4|knows_power_strike_7|knows_weapon_master_5, mercenary_face_1, mercenary_face_2 ],

  ["mercenary_skirmisher", "Mercenary Skirmisher", "Mercenary Skirmisher", tf_guarantee_all, no_scene, reserved, fac.commoners, [
    itm.ragged_outfit,itm.leather_jacket,itm.pelt_coat,itm.rawhide_coat,itm.leather_vest,itm.padded_cloth,itm.aketon_green,itm.leather_jerkin,itm.nomad_vest,itm.tribal_warrior_outfit,itm.nomad_robe,itm.light_leather,itm.hide_boots,itm.light_leather_boots,itm.padded_coif,itm.leather_steppe_cap_a,itm.fur_hat,
    itm.mercenary_shield_a,
    itm.hunting_crossbow,itm.bolts,itm.hammer,itm.spiked_club,itm.club_with_spike_head,itm.falchion_new,itm.sword_medieval_b_small,itm.sword_viking_a_small,itm.skirmisher_pick,itm.sword_medieval_c_small,
  ], level(10)|str_12|agi_13|int_6|cha_6, wpex(85,30,30,30,100,30), knows_athletics_4|knows_power_strike_2|knows_ironflesh_3|knows_weapon_master_3, mercenary_face_1, mercenary_face_2 ],

  ["mercenary_crossbowman", "Mercenary Crossbowman", "Mercenary Crossbowmen", tf_guarantee_all, no_scene, reserved, fac.commoners, [
    itm.light_leather,itm.leather_armor,itm.padded_leather,itm.hide_boots,itm.light_leather_boots,itm.leather_cap,itm.nomad_cap_b,itm.leather_warrior_cap,
    itm.mercenary_shield_a,
    itm.hunting_crossbow,itm.light_crossbow,itm.bolts,itm.hunting_bolts,itm.hammer,itm.spiked_club,itm.club_with_spike_head,itm.falchion_new,itm.sword_medieval_b_small,itm.sword_viking_a_small,itm.skirmisher_pick,itm.sword_medieval_c_small,
  ], level(12)|str_12|agi_15|int_6|cha_6, wpex(125,30,30,30,120,30), knows_athletics_4|knows_shield_3|knows_ironflesh_3|knows_power_strike_2|knows_weapon_master_3, mercenary_face_1, mercenary_face_2 ],

  ["mercenary_trained_crossbowman", "Mercenary Trained Crossbowman", "Mercenary Trained Crossbowmen", tf_guarantee_all, no_scene, reserved, fac.commoners, [
    itm.padded_leather,itm.studded_leather_coat,itm.haubergeon,itm.mail_hauberk,itm.light_leather_boots,itm.leather_boots,itm.splinted_greaves,itm.skullcap,itm.footman_helmet,
    itm.mercenary_shield_a,
    itm.light_crossbow,itm.crossbow,itm.bolts,itm.hunting_bolts,itm.hammer,itm.spiked_club,itm.club_with_spike_head,itm.falchion_new,itm.sword_medieval_b_small,itm.sword_viking_a_small,itm.skirmisher_pick,itm.sword_medieval_c_small,
  ], level(14)|str_12|agi_17|int_6|cha_6, wpex(105,30,30,30,140,30), knows_shield_4|knows_ironflesh_3|knows_power_strike_2|knows_weapon_master_4|knows_athletics_4, mercenary_face_1, mercenary_face_2 ],

  ["mercenary_veteran_crossbowman", "Mercenary Veteran Crossbowman", "Mercenary Veteran Crossbowmen", tf_guarantee_all, no_scene, reserved, fac.commoners, [
    itm.haubergeon,itm.mail_hauberk,itm.mail_shirt,itm.mail_with_surcoat,itm.surcoat_over_mail,itm.light_leather_boots,itm.leather_boots,itm.splinted_greaves,itm.norman_helmet,itm.rhodok_kettle_hat,
    itm.mercenary_shield_b,
    itm.crossbow,itm.heavy_crossbow,itm.bolts,itm.hunting_bolts,itm.piercing_bolts,itm.hammer,itm.spiked_club,itm.club_with_spike_head,itm.falchion_new,itm.sword_medieval_b_small,itm.sword_viking_a_small,itm.skirmisher_pick,itm.sword_medieval_c_small,
  ], level(18)|str_15|agi_18|int_6|cha_6, wpex(110,30,30,30,180,30), knows_shield_5|knows_ironflesh_4|knows_power_strike_2|knows_weapon_master_5|knows_athletics_5, mercenary_face_1, mercenary_face_2 ],

  ["mercenary_sniper", "Mercenary Sniper", "Mercenary Snipers", tf_guarantee_all, no_scene, reserved, fac.commoners, [
    itm.mail_shirt,itm.mail_with_surcoat,itm.surcoat_over_mail,itm.coat_of_plates,itm.coat_of_plates_red,itm.splinted_greaves,itm.mail_chausses,itm.mail_boots,itm.segmented_helmet,itm.mail_coif,itm.nasal_helmet,
    itm.mercenary_shield_b,
    itm.heavy_crossbow,itm.hunting_bolts,itm.piercing_bolts,itm.hammer,itm.spiked_club,itm.club_with_spike_head,itm.falchion_new,itm.sword_medieval_b_small,itm.sword_viking_a_small,itm.skirmisher_pick,itm.sword_medieval_c_small,
    itm.goods_gold,
  ], level(20)|str_15|agi_18|int_8|cha_6, wpex(110,30,30,30,200,30), knows_athletics_6|knows_shield_6|knows_ironflesh_5|knows_power_strike_2|knows_weapon_master_6, mercenary_face_1, mercenary_face_2 ],

  # Begin Female Mercenary Tree - Leave Peasant Woman as is or the game will break (SEEMS NO LONGER TRUE)
  # The first 5 units here are called specifically in scripts - do not change their identifiers

  ["peasant_woman", "Peasant Woman", "Peasant Women", tf_female|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet, no_scene, reserved, fac.commoners, [
    itm.dress,itm.woolen_dress,itm.wrapping_boots,itm.wimple_a,itm.wimple_with_veil,itm.head_wrappings,itm.headcloth,
    itm.pitch_fork,itm.sickle,itm.club,itm.cudgel,itm.peasant_knife,itm.butchering_knife,
  ], level(6)|str_9|agi_12|int_6|cha_6, wpex(30,30,30,30,30,30), 0, refugee_face1, refugee_face2 ],

  ["female_camp_defender", "Mercenary Camp Defender", "Mercenary Camp Defenders", tf_female|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.commoners, [
    itm.ragged_outfit,itm.pelt_coat,itm.rawhide_coat,itm.padded_cloth,itm.aketon_green,itm.nomad_vest,itm.nomad_robe,itm.hunter_boots,itm.hide_boots,itm.leather_gloves,itm.padded_coif,itm.leather_steppe_cap_a,itm.fur_hat,
    itm.mercenary_shield_a,
    itm.cudgel,itm.spiked_club,itm.sword_medieval_b_small,itm.sword_viking_a_small,itm.skirmisher_pick,itm.sword_medieval_c_small,itm.sword_norman,
  ], level(10)|str_13|agi_12|int_6|cha_6, wpex(80,30,30,30,30,30), knows_power_strike_2|knows_power_throw_2|knows_weapon_master_2|knows_shield_1, refugee_face1, refugee_face2 ],

  ["female_stable_maiden", "Mercenary Stable Maiden", "Mercenary Stable Maidens", tf_female|tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.commoners, [
    itm.leather_jacket,itm.leather_vest,itm.leather_jerkin,itm.tribal_warrior_outfit,itm.light_leather,itm.hide_boots,itm.light_leather_boots,itm.leather_gloves,itm.leather_cap,itm.nomad_cap_b,itm.leather_warrior_cap,
    itm.mercenary_shield_a,
    itm.boar_spear,itm.spear,itm.war_spear,itm.sword_norman,
    itm.farm_horse,itm.riding_horse,itm.sarranid_horse_a,itm.sarranid_horse_b,itm.khergit_horse,
  ], level(12)|str_13|agi_14|int_6|cha_6, wpex(100,30,100,30,30,30), knows_riding_3|knows_shield_2|knows_power_strike_2|knows_ironflesh_3|knows_weapon_master_3|knows_horse_archery_2, refugee_face1, refugee_face2 ],

  ["female_sister_in_arms", "Mercenary Sister-in-arms", "Mercenary Sisters-in-arms", tf_female|tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.commoners, [
    itm.light_leather,itm.leather_armor,itm.padded_leather,itm.light_leather_boots,itm.leather_boots,itm.splinted_greaves,itm.mail_mittens,itm.skullcap,itm.footman_helmet,
    itm.mercenary_shield_b,
    itm.war_spear,itm.light_lance,itm.sword_medieval_d,
    itm.khergit_horse,itm.hunter_horse,itm.courser_horse,
  ], level(14)|str_15|agi_14|int_6|cha_6, wpex(110,30,120,30,30,30), knows_horse_archery_2|knows_shield_2|knows_power_strike_2|knows_ironflesh_4|knows_weapon_master_4|knows_horse_archery_3|knows_riding_3, refugee_face1, refugee_face2 ],

  ["female_shield_sister", "Mercenary Shield Sister", "Mercenary Shield Sisters", tf_female|tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.commoners, [
    itm.padded_leather,itm.studded_leather_coat,itm.haubergeon,itm.mail_hauberk,itm.light_leather_boots,itm.leather_boots,itm.splinted_greaves,itm.mail_mittens,itm.norman_helmet,itm.rhodok_kettle_hat,
    itm.mercenary_shield_b,
    itm.light_lance,itm.cavalry_lance,itm.sword_medieval_c,
    itm.hunter_horse,itm.armored_courser,itm.armored_hunter,
  ], level(18)|str_16|agi_17|int_6|cha_6, wpex(135,30,150,30,30,30), knows_riding_4|knows_power_strike_3|knows_ironflesh_5|knows_weapon_master_4|knows_shield_2|knows_horse_archery_3, refugee_face1, refugee_face2 ],

  ["female_shield_mistress", "Mercenary Shield Mistress", "Mercenary Shield Mistresses", tf_female|tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.commoners, [
    itm.haubergeon,itm.mail_hauberk,itm.mail_shirt,itm.mail_with_surcoat,itm.surcoat_over_mail,itm.splinted_greaves,itm.mail_chausses,itm.mail_boots,itm.scale_gauntlets,itm.segmented_helmet,itm.mail_coif,itm.nasal_helmet,
    itm.mercenary_shield_c,
    itm.cavalry_lance,itm.great_lance,itm.sword_medieval_c_long,
    itm.armored_courser,itm.armored_hunter,itm.swadian_warhorse_a,itm.vaegir_warhorse_a,itm.khergit_warhorse_a,itm.nordic_warhorse_a,itm.rhodok_warhorse_a,itm.sarranid_warhorse_a,
    itm.goods_gold,
  ], level(20)|str_18|agi_17|int_6|cha_6, wpex(145,30,160,30,30,30), knows_riding_4|knows_athletics_2|knows_shield_3|knows_power_strike_3|knows_ironflesh_5|knows_weapon_master_4|knows_horse_archery_4, refugee_face1, refugee_face2 ],

  ["female_shield_maiden", "Mercenary Shield Maiden", "Mercenary Shield Maidens", tf_female|tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.commoners, [
    itm.mail_shirt,itm.mail_with_surcoat,itm.surcoat_over_mail,itm.coat_of_plates,itm.coat_of_plates_red,itm.splinted_greaves,itm.mail_chausses,itm.mail_boots,itm.scale_gauntlets,itm.helmet_with_neckguard,itm.spiked_helmet,
    itm.mercenary_shield_c,
    itm.great_lance,itm.sword_medieval_d_long,
    itm.swadian_warhorse_a,itm.vaegir_warhorse_a,itm.khergit_warhorse_a,itm.nordic_warhorse_a,itm.rhodok_warhorse_a,itm.sarranid_warhorse_a,
    itm.goods_gold,
  ], level(24)|str_21|agi_18|int_6|cha_6, wpex(170,30,180,30,30,30), knows_athletics_4|knows_shield_3|knows_power_strike_4|knows_ironflesh_6|knows_weapon_master_4|knows_riding_5|knows_horse_archery_5, refugee_face1, refugee_face2 ],

  ["female_pike_sister", "Mercenary Pike Sister", "Mercenary Pike Sisters", tf_female|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.commoners, [
    itm.leather_jacket,itm.leather_vest,itm.leather_jerkin,itm.tribal_warrior_outfit,itm.light_leather,itm.hide_boots,itm.light_leather_boots,itm.mail_mittens,itm.leather_cap,itm.nomad_cap_b,itm.leather_warrior_cap,
    itm.mercenary_shield_a,
    itm.military_fork,itm.battle_fork,itm.partisan,itm.boar_spear,itm.spear,itm.war_spear,itm.hammer,itm.winged_mace,itm.spiked_club,itm.falchion_new,itm.sword_medieval_b_small,itm.sword_medieval_c_small,itm.sword_medieval_d,
  ], level(12)|str_13|agi_14|int_6|cha_6, wpex(80,30,100,30,30,30), knows_athletics_4|knows_shield_4|knows_ironflesh_3|knows_power_strike_4|knows_power_throw_2|knows_weapon_master_2, refugee_face1, refugee_face2 ],

  ["female_pike_maiden", "Mercenary Pike Maiden", "Mercenary Pike Maidens", tf_female|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.commoners, [
    itm.light_leather,itm.leather_armor,itm.padded_leather,itm.light_leather_boots,itm.leather_boots,itm.splinted_greaves,itm.mail_mittens,itm.skullcap,itm.footman_helmet,
    itm.mercenary_shield_b,
    itm.battle_fork,itm.partisan,itm.war_spear,itm.ashwood_pike,itm.military_scythe_a,itm.military_scythe_b,itm.poleaxe,itm.glaive,itm.knobbed_mace,itm.flanged_mace,itm.spiked_mace,itm.one_handed_battle_axe_a,itm.one_handed_battle_axe_c,itm.sword_viking_a_small,itm.military_pick,itm.sword_norman,itm.sword_medieval_c,
  ], level(14)|str_14|agi_15|int_6|cha_6, wpex(90,30,140,30,30,30), knows_athletics_5|knows_shield_4|knows_ironflesh_3|knows_power_strike_4|knows_power_throw_2|knows_weapon_master_3, refugee_face1, refugee_face2 ],

  ["female_line_sister", "Mercenary Line Sister", "Mercenary Line Sisters", tf_female|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.commoners, [
    itm.padded_leather,itm.studded_leather_coat,itm.haubergeon,itm.mail_hauberk,itm.light_leather_boots,itm.leather_boots,itm.splinted_greaves,itm.scale_gauntlets,itm.norman_helmet,itm.rhodok_kettle_hat,
    itm.mercenary_shield_b,
    itm.trident,itm.ashwood_pike,itm.pike,itm.military_scythe_a,itm.military_scythe_b,itm.glaive,itm.voulge_b,itm.lineman_mace,itm.mace_small_d,itm.winged_mace_b,itm.one_handed_war_axe_a,itm.one_handed_battle_axe_b,itm.khergit_sword_b,itm.fighting_pick,itm.sword_medieval_c_long,
  ], level(18)|str_17|agi_16|int_6|cha_6, wpex(100,30,180,30,30,30), knows_shield_4|knows_athletics_6|knows_ironflesh_5|knows_power_strike_4|knows_power_throw_2|knows_weapon_master_4, refugee_face1, refugee_face2 ],

  ["female_line_maiden", "Mercenary Line Maiden", "Mercenary Line Maidens", tf_female|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.commoners, [
    itm.haubergeon,itm.mail_hauberk,itm.mail_shirt,itm.mail_with_surcoat,itm.surcoat_over_mail,itm.splinted_greaves,itm.mail_chausses,itm.mail_boots,itm.scale_gauntlets,itm.segmented_helmet,itm.mail_coif,itm.nasal_helmet,
    itm.mercenary_shield_c,
    itm.trident,itm.pike,itm.infantry_pike,itm.military_scythe_c,itm.voulge_b,itm.one_handed_war_axe_b,itm.sword_medieval_d_long,
    itm.goods_gold,
  ], level(20)|str_17|agi_18|int_6|cha_6, wpex(120,30,220,30,30,30), knows_shield_5|knows_riding_9|knows_athletics_6|knows_ironflesh_5|knows_power_strike_5|knows_power_throw_2|knows_weapon_master_5, refugee_face1, refugee_face2 ],

  ["female_tracker", "Mercenary Tracker", "Mercenary Trackers", tf_female|tf_guarantee_all, no_scene, reserved, fac.commoners, [
    itm.ragged_outfit,itm.pelt_coat,itm.rawhide_coat,itm.padded_cloth,itm.aketon_green,itm.nomad_vest,itm.nomad_robe,itm.hunter_boots,itm.hide_boots,itm.padded_coif,itm.leather_steppe_cap_a,itm.fur_hat,
    itm.mercenary_shield_a,
    itm.hunting_bow,itm.hunting_arrows,itm.falchion_new,itm.spiked_club,itm.hammer,
  ], level(10)|str_13|agi_12|int_6|cha_6, wpex(70,30,30,90,30,30), knows_athletics_4|knows_ironflesh_1|knows_power_strike_1|knows_shield_3|knows_weapon_master_2, refugee_face1, refugee_face2 ],

  ["female_archer", "Mercenary Archer", "Mercenary Archers", tf_female|tf_guarantee_all, no_scene, reserved, fac.commoners, [
    itm.leather_jacket,itm.leather_vest,itm.leather_jerkin,itm.tribal_warrior_outfit,itm.light_leather,itm.hide_boots,itm.light_leather_boots,itm.leather_cap,itm.nomad_cap_b,itm.leather_warrior_cap,
    itm.mercenary_shield_a,
    itm.hunting_bow,itm.short_bow,itm.hunting_arrows,itm.arrows,itm.winged_mace,itm.knobbed_mace,itm.flanged_mace,itm.spiked_mace,itm.lineman_mace,
  ], level(14)|str_13|agi_16|int_6|cha_6, wpex(90,30,30,100,30,30), knows_ironflesh_1|knows_power_strike_2|knows_power_draw_4|knows_athletics_5|knows_shield_3|knows_weapon_master_2, refugee_face1, refugee_face2 ],

  ["female_huntress", "Mercenary Huntress", "Mercenary Huntresses", tf_female|tf_guarantee_all, no_scene, reserved, fac.commoners, [
    itm.light_leather,itm.leather_armor,itm.padded_leather,itm.hide_boots,itm.light_leather_boots,itm.skullcap,itm.footman_helmet,
    itm.mercenary_shield_a,
    itm.short_bow,itm.arrows,itm.khergit_sword_b,itm.military_pick,itm.spiked_mace,
  ], level(18)|str_17|agi_16|int_6|cha_6, wpex(110,30,30,140,30,30), knows_ironflesh_1|knows_power_strike_4|knows_power_draw_5|knows_athletics_5|knows_shield_3|knows_weapon_master_3, refugee_face1, refugee_face2 ],

  ["female_master_huntress", "Mercenary Master Huntress", "Mercenary Master Huntresses", tf_female|tf_guarantee_all, no_scene, reserved, fac.commoners, [
    itm.padded_leather,itm.studded_leather_coat,itm.haubergeon,itm.mail_hauberk,itm.light_leather_boots,itm.leather_boots,itm.splinted_greaves,itm.norman_helmet,itm.rhodok_kettle_hat,
    itm.mercenary_shield_b,
    itm.nomad_bow,itm.arrows,itm.broadhead_arrows,itm.khergit_sword_a,itm.khergit_sword_b,
  ], level(20)|str_18|agi_17|int_6|cha_6, wpex(130,30,30,180,30,30), knows_athletics_5|knows_shield_3|knows_ironflesh_1|knows_power_strike_4|knows_power_draw_6, refugee_face1, refugee_face2 ],

  ["female_stalker", "Mercenary Stalker", "Mercenary Stalkers", tf_female|tf_guarantee_all, no_scene, reserved, fac.commoners, [
    itm.haubergeon,itm.mail_hauberk,itm.mail_shirt,itm.mail_with_surcoat,itm.surcoat_over_mail,itm.splinted_greaves,itm.mail_chausses,itm.mail_boots,itm.segmented_helmet,itm.mail_coif,itm.nasal_helmet,
    itm.mercenary_shield_b,
    itm.long_bow,itm.broadhead_arrows,itm.piercing_arrows,itm.barbed_arrows,itm.scimitar,itm.khergit_sword_a,
    itm.goods_gold,
  ], level(24)|str_21|agi_18|int_6|cha_6, wpex(150,30,30,200,30,30), knows_athletics_6|knows_shield_3|knows_ironflesh_1|knows_power_strike_5|knows_power_draw_7|knows_weapon_master_5, refugee_face1, refugee_face2 ],

  ["mercenaries_end", "{!}", "{!}endmarker", tf_hero|tf_inactive, 0, 0, fac.no_faction, [], 0, 0, knows_inventory_management_10, 0],

  #Do not change the hired_blade identifier.  It and mercenary_swordsman are specifically called out in scripts.
  # NE 600 series - moving hired_blade outside of the merc tree so it can't show up in merc polling

  ["hired_blade","Mercenary","Mercenaries",tf_guarantee_all,no_scene,reserved,fac.commoners,[
    itm.haubergeon,itm.mail_hauberk,itm.mail_shirt,itm.haubergeon,itm.mail_chausses,itm.mail_boots,itm.mail_mittens,itm.splinted_leather_greaves,itm.guard_helmet,itm.kettle_hat,itm.bascinet,itm.flat_topped_helmet,
    itm.mercenary_shield_c,
    itm.poleaxe,itm.sword_medieval_c_long,itm.sword_medieval_d_long,
  ],level(25)|str_16|agi_8|int_4|cha_4,wp(130),knows_common|knows_riding_3|knows_athletics_5|knows_shield_4|knows_power_strike_5|knows_ironflesh_4,mercenary_face_1,mercenary_face_2],


  ["regular_soldiers_begin", "{!}", "{!}marker", tf_hero|tf_inactive, 0, 0, fac.no_faction, [], 0, 0, knows_inventory_management_10, 0],


  #Begin Swadian Units
  ["swadian_recruit", "Swadian Recruit", "Swadian Recruits", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac.kingdom_1, [
    itm.linen_tunic,itm.red_tunic,itm.green_tunic,itm.blue_tunic,itm.white_tunic,itm.yellow_tunic,itm.coarse_tunic,itm.tunic_with_green_cape,
    itm.wrapping_boots,itm.ankle_boots,
    itm.common_hood,itm.felt_hat,
    itm.scythe,itm.pitch_fork,itm.peasant_knife,itm.butchering_knife,itm.cleaver,itm.club,itm.hatchet,itm.sickle,
  ], level(6)|str_11|agi_10|int_6|cha_6, wpex(90,30,30,30,30,30), knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_2|knows_shield_2|knows_athletics_2, swadian_face_younger_1, swadian_face_middle_2 ],

  ["swadian_proselyte", "Swadian Proselyte", "Swadian Proselytes", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, no_scene, reserved, fac.kingdom_1, [
    itm.hera_padded_cloth_a,itm.hera_padded_cloth_b,
    itm.hunter_boots,itm.hide_boots,
    itm.padded_coif,itm.leather_cap,
    itm.hera_swadian_inf_shield_a,
    itm.hunting_crossbow,itm.bolts,
    itm.sword_medieval_c_small,itm.cudgel,itm.spiked_club,
  ], level(8)|str_12|agi_11|int_6|cha_6, wpex(100,30,30,30,60,30), knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_3|knows_shield_3|knows_athletics_2, swadian_face_younger_1, swadian_face_middle_2 ],

  ["swadian_infantry", "Swadian Infantry", "Swadian Infantry", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_1, [
    itm.padded_leather,
    itm.light_leather_boots,itm.leather_boots,
    itm.leather_gloves,
    itm.skullcap,
    itm.hera_swadian_inf_shield_a,
    itm.one_handed_battle_axe_g,
    itm.swadian_short_sword_a,
  ], level(10)|str_13|agi_12|int_6|cha_6, wpex(100,30,30,30,30,30), knows_ironflesh_3|knows_shield_3|knows_power_strike_2|knows_weapon_master_3|knows_athletics_2, swadian_face_young_1, swadian_face_old_2 ],

  ["swadian_sergeant", "Swadian Sergeant", "Swadian Sergeants", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_1, [
    itm.hera_light_mail_and_plate,
    itm.splinted_greaves,
    itm.mail_gauntlets,
    itm.footman_helmet,itm.segmented_helmet,
    itm.hera_swadian_inf_shield_b,
    itm.one_handed_battle_axe_g,itm.one_handed_battle_axe_h,
    itm.swadian_short_sword_b,
  ], level(12)|str_15|agi_12|cha_6|int_6, wpex(140,30,30,30,30,30), knows_shield_3|knows_ironflesh_3|knows_power_strike_3|knows_athletics_3|knows_weapon_master_3, swadian_face_young_1, swadian_face_old_2 ],

  ["swadian_pikeman", "Swadian Pikeman", "Swadian Pikemen", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_1, [
    itm.hera_arena_armor,
    itm.mail_chausses,itm.mail_boots,
    itm.mail_mittens,
    itm.mail_coif,
    itm.hera_swadian_inf_shield_b,
    itm.awlpike,itm.one_handed_battle_axe_h,
    itm.swadian_short_sword_b,
  ], level(14)|str_17|agi_12|int_6|cha_6, wpex(100,30,120,30,30,30), knows_shield_3|knows_ironflesh_3|knows_power_strike_3|knows_weapon_master_3|knows_shield_3|knows_athletics_3, swadian_face_middle_1, swadian_face_older_2 ],

  ["swadian_halberdier", "Swadian Pikemaster", "Swadian Pikemasters", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_1, [
    itm.hera_cuir_bouilli_a,
    itm.splinted_leather_greaves,itm.iron_greaves,
    itm.scale_gauntlets,
    itm.helmet_with_neckguard,itm.guard_helmet,
    itm.hera_swadian_inf_shield_c,
    itm.awlpike_long,itm.one_handed_battle_axe_h,
    itm.swadian_short_sword_c,
  ], level(18)|str_18|agi_15|int_6|cha_6, wpex(100,30,175,30,30,30), knows_athletics_3|knows_shield_3|knows_ironflesh_5|knows_power_strike_6|knows_weapon_master_4, swadian_face_old_1, swadian_face_older_2 ],

  ["swadian_swordsman", "Swadian Swordsman", "Swadian Swordsmen", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_1, [
    itm.hera_mail_and_plate,
    itm.mail_chausses,itm.mail_boots,
    itm.mail_mittens,
    itm.mail_coif,
    itm.hera_swadian_inf_shield_b,
    itm.sword_medieval_a,
  ], level(14)|str_17|agi_12|int_6|cha_6, wp_melee(160), knows_ironflesh_3|knows_power_strike_4|knows_weapon_master_4|knows_athletics_3|knows_shield_3, swadian_face_middle_1, swadian_face_older_2 ],

  ["swadian_captain", "Swadian Captain", "Swadian Captains", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_1, [
    itm.hera_cuir_bouilli_a,
    itm.splinted_leather_greaves,itm.iron_greaves,
    itm.scale_gauntlets,
    itm.helmet_with_neckguard,itm.guard_helmet,
    itm.hera_swadian_inf_shield_c,
    itm.sword_swadian_a,
  ], agi_12|int_6|cha_6|level(18)|str_21, wp_melee(180), knows_ironflesh_3|knows_power_strike_4|knows_weapon_master_4|knows_athletics_5|knows_shield_4, swadian_face_old_1, swadian_face_older_2 ],

  ["swadian_skirmisher", "Swadian Skirmisher", "Swadian Skirmishers", tf_guarantee_all, no_scene, reserved, fac.kingdom_1, [
    itm.hera_padded_cloth_a,itm.hera_padded_cloth_b,itm.light_leather,itm.leather_armor,
    itm.hunter_boots,itm.hide_boots,
    itm.padded_coif,itm.leather_cap,
    itm.hera_swadian_inf_shield_a,
    itm.light_crossbow,itm.bolts,
    itm.skirmisher_pick,
  ], level(10)|str_13|agi_12|int_6|cha_6, wpex(100,30,30,30,80,30), knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_3|knows_shield_4|knows_athletics_3, swadian_face_younger_1, swadian_face_middle_2 ],

  ["swadian_untrained_crossbowman", "Swadian Untrained Crossbowman", "Swadian Untrained Crossbowmen", tf_guarantee_all, no_scene, reserved, fac.kingdom_1, [
    itm.padded_leather,
    itm.hunter_boots,itm.hide_boots,
    itm.leather_cap,itm.skullcap,
    itm.hera_swadian_inf_shield_a,
    itm.crossbow,itm.bolts,itm.hunting_bolts,
    itm.military_pick,
  ], level(12)|str_15|agi_12|int_6|cha_6, wpex(100,30,30,30,100,30), knows_shield_4|knows_ironflesh_3|knows_power_strike_1|knows_weapon_master_3|knows_athletics_4, swadian_face_young_1, swadian_face_old_2 ],

  ["swadian_crossbowman", "Swadian Crossbowman", "Swadian Crossbowmen", tf_guarantee_all, no_scene, reserved, fac.kingdom_1, [
    itm.padded_leather,
    itm.light_leather_boots,itm.leather_boots,
    itm.skullcap,itm.footman_helmet,
    itm.hera_swadian_inf_shield_a,
    itm.heavy_crossbow,itm.hunting_bolts,itm.piercing_bolts,
    itm.crossbowman_pick,
  ], level(14)|str_15|agi_14|int_6|cha_6, wpex(100,30,30,30,130,30), knows_ironflesh_4|knows_power_strike_2|knows_weapon_master_3|knows_shield_4|knows_athletics_4, swadian_face_young_1, swadian_face_old_2 ],

  ["swadian_veteran_crossbowman", "Swadian Veteran Crossbowman", "Swadian Veteran Crossbowmen", tf_guarantee_all, no_scene, reserved, fac.kingdom_1, [
    itm.heraldic_mail_with_tunic_b,
    itm.splinted_greaves,
    itm.segmented_helmet,itm.mail_coif,
    itm.hera_swadian_inf_shield_b,
    itm.sniper_crossbow,itm.piercing_bolts,
    itm.fighting_pick,
  ], str_16|level(16)|agi_15|int_6|cha_6, wpex(100,30,30,30,155,30), knows_ironflesh_4|knows_power_strike_2|knows_weapon_master_4|knows_shield_5|knows_athletics_4, swadian_face_middle_1, swadian_face_older_2 ],

  ["swadian_page", "Swadian Page", "Swadian Pages", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_1, [
    itm.padded_leather,
    itm.light_leather_boots,itm.leather_boots,
    itm.skullcap,itm.footman_helmet,
    itm.mail_mittens,
    itm.hera_swadian_cav_shield_a,
    itm.lance_swa_cav_a,itm.sword_swadian_b,
    itm.riding_horse,itm.hunter_horse,
  ], level(14)|str_14|agi_15|cha_6|int_6, wpex(120,30,115,30,30,30), knows_riding_4|knows_ironflesh_3|knows_shield_2|knows_power_strike_3|knows_weapon_master_3|knows_athletics_2, swadian_face_younger_1, swadian_face_middle_2 ],

  ["swadian_squire", "Swadian Squire", "Swadian Squires", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_1, [
    itm.hera_arena_armor,
    itm.splinted_greaves,
    itm.scale_gauntlets,
    itm.segmented_helmet,itm.mail_coif,
    itm.hera_swadian_cav_shield_a,
    itm.lance_swa_cav_b,itm.sword_swadian_c,
    itm.hunter_horse,itm.armored_hunter,
  ], level(18)|str_15|agi_18|int_6|cha_6, wpex(140,30,150,30,30,30), knows_riding_5|knows_shield_3|knows_ironflesh_4|knows_power_strike_3|knows_weapon_master_4|knows_athletics_2, swadian_face_young_1, swadian_face_old_2 ],

  ["swadian_senior_squire", "Swadian Senior Squire", "Swadian Senior Squires", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_1, [
    itm.hera_cuir_bouilli_a,
    itm.mail_chausses,itm.mail_boots,
    itm.lamellar_gauntlets,
    itm.helmet_with_neckguard,itm.guard_helmet,
    itm.hera_swadian_cav_shield_b,
    itm.lance_swa_cav_c,itm.sword_swadian_d,
    itm.armored_hunter,itm.swadian_warhorse_a,
  ], level(22)|str_19|agi_18|int_6|cha_6, wpex(140,30,180,30,30,30), knows_riding_6|knows_shield_5|knows_ironflesh_4|knows_power_strike_4|knows_weapon_master_4|knows_athletics_2, swadian_face_young_1, swadian_face_older_2 ],

  ["swadian_man_at_arms", "Swadian Man-at-arms", "Swadian Men-at-arms", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_1, [
    itm.hera_mail_long_surcoat,
    itm.mail_chausses,itm.mail_boots,
    itm.scale_gauntlets,
    itm.helmet_with_neckguard,itm.guard_helmet,
    itm.hera_swadian_cav_shield_b,
    itm.lance_swa_cav_b,itm.lance_swa_cav_c,itm.two_handed_battle_axe_h,itm.sword_swadian_e,itm.sword_swadian_e,
    itm.swadian_warhorse_b,
  ], level(24)|str_21|agi_18|int_6|cha_6, wpex(160,30,190,30,30,30), knows_riding_7|knows_ironflesh_4|knows_athletics_2|knows_power_strike_4|knows_weapon_master_5|knows_shield_5, swadian_face_young_1, swadian_face_old_2 ],

  ["swadian_knight", "Swadian Knight", "Swadian Knights", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_1, [
    itm.hera_cuir_bouilli_a,
    itm.splinted_leather_greaves,itm.iron_greaves,
    itm.lamellar_gauntlets,
    itm.guard_helmet,itm.bascinet,itm.bascinet_2,
    itm.hera_swadian_cav_shield_c,
    itm.knight_lance_1,itm.knight_lance_2,itm.two_handed_battle_axe_h,itm.two_handed_battle_axe_g,itm.sword_medieval_a_long,itm.sword_medieval_a_long,itm.sword_medieval_a_long,
    itm.swadian_warhorse_c,
  ], level(26)|str_23|agi_18|int_6|cha_6, wpex(170,30,200,30,30,30), knows_riding_6|knows_shield_6|knows_ironflesh_5|knows_power_strike_5|knows_weapon_master_5|knows_athletics_2, swadian_face_middle_1, swadian_face_older_2 ],

  ["swadian_cavalier", "Swadian Cavalier", "Swadian Cavaliers", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_1, [
    itm.hera_plate_armor,
    itm.plate_boots,
    itm.gauntlets,
    itm.bascinet_2,itm.bascinet_3,
    itm.hera_swadian_cav_shield_c,
    itm.cavalier_lance_1,itm.cavalier_lance_2,itm.two_handed_battle_axe_g,itm.sword_swadian_f,itm.sword_swadian_f,
    itm.swadian_charger_a,
  ], level(28)|str_24|agi_19|int_6|cha_6, wpex(170,30,220,30,30,30), knows_riding_6|knows_shield_6|knows_ironflesh_6|knows_power_strike_5|knows_weapon_master_6|knows_athletics_2, swadian_face_middle_1, swadian_face_older_2 ],

  ["swadian_paladin", "Swadian Paladin", "Swadian Paladins", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_1, [
    itm.hera_plate_armor,
    itm.plate_boots,
    itm.plated_gauntlets,
    itm.winged_great_helmet,
    itm.hera_swadian_inf_shield_c,
    itm.paladin_lance_1,itm.paladin_lance_2,itm.two_handed_battle_axe_g,itm.sword_swadian_g,
    itm.swadian_charger_b,
  ], level(36)|str_24|agi_27|int_6|cha_6, wpex(175,30,300,30,30,30), knows_riding_9|knows_shield_5|knows_ironflesh_8|knows_power_strike_8|knows_weapon_master_7|knows_athletics_2, swadian_face_middle_1, swadian_face_old_2 ],

  ["swadian_priest", "Swadian Priest", "Swadian Priest", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_1, [
    itm.hera_plate_armor,
    itm.plate_boots,
    itm.plated_gauntlets,
    itm.great_helmet,
    itm.hera_swadian_inf_shield_c,
    itm.priest_lance,itm.priest_mace,
    itm.swadian_warhorse_d,itm.swadian_warhorse_e,
  ], level(36)|str_27|agi_24|int_6|cha_6, wpex(250,30,250,30,30,30), knows_riding_8|knows_shield_8|knows_ironflesh_8|knows_power_strike_7|knows_weapon_master_6, swadian_face_old_1, swadian_face_older_2 ],

  ["swadian_prison_guard","Swadian Prison Guard","Swadian Prison Guards",tf_guarantee_all_wo_ranged,0,reserved, fac.kingdom_1,[
    itm.mail_with_surcoat,
    itm.mail_chausses,itm.mail_boots,
    itm.mail_mittens,
    itm.mail_coif,
    itm.hera_swadian_inf_shield_c,
    itm.sword_medieval_a_long,
  ],level(25)|def_attrib,wp(130),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],

  ["swadian_castle_guard","Swadian Castle Guard","Swadian Castle Guards",tf_guarantee_all_wo_ranged,0,reserved, fac.kingdom_1,[
    itm.plate_armor,
    itm.plate_boots,
    itm.plated_gauntlets,
    itm.bascinet_3,
    itm.hera_swadian_inf_shield_c,
    itm.two_handed_battle_axe_h,
  ],level(25)|def_attrib,wp(130),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],

  ["swadian_messenger","Swadian Messenger","Swadian Messengers",0,0,reserved, fac.kingdom_1,[],level(25)|def_attrib|agi_21,wp(130),knows_common|knows_riding_7|knows_horse_archery_5,swadian_face_young_1,swadian_face_old_2],
  ["swadian_deserter","Swadian Deserter","Swadian Deserters",0,0,reserved, fac.kingdom_1,[],level(14)|def_attrib,wp(80),knows_common|knows_riding_2|knows_ironflesh_1,swadian_face_young_1,swadian_face_old_2],

  #Begin Vaegir Units
  ["vaegir_recruit", "Vaegir Conscript", "Vaegir Conscripts", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac.kingdom_2, [
    itm.linen_tunic,itm.white_tunic,itm.coarse_tunic,itm.leather_apron,
    itm.wrapping_boots,itm.ankle_boots,itm.nomad_boots,
    itm.head_wrappings,itm.headcloth,itm.straw_hat,
    itm.scythe,itm.pitch_fork,itm.staff,itm.butchering_knife,itm.cleaver,itm.wooden_stick,itm.smith_hammer,itm.hatchet,itm.beef_splitter,itm.sickle,
    # improvised weapons
  ], level(6)|str_11|agi_10|int_6|cha_6, wpex(60,30,30,30,30,30), knows_ironflesh_3|knows_power_strike_1|knows_weapon_master_2|knows_athletics_3, vaegir_face_younger_1, vaegir_face_middle_2 ],

  ["vaegir_footman", "Vaegir Footman", "Vaegir Footmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, no_scene, reserved, fac.kingdom_2, [
    itm.leather_jacket,itm.pelt_coat,itm.rawhide_coat,itm.fur_coat,
    itm.nomad_boots,itm.hunter_boots,itm.hide_boots,
    itm.leather_gloves,
    itm.fur_hat,itm.leather_warrior_cap,
    itm.hera_vaegir_inf_shield_a,
    itm.darts,
    itm.sword_medieval_c_small,itm.sword_medieval_b_small,itm.sword_viking_a_small,itm.spiked_club,
  ], level(8)|str_12|agi_11|cha_6|int_6, wpex(80,30,30,30,30,60), knows_ironflesh_3|knows_power_strike_1|knows_weapon_master_2|knows_athletics_4, vaegir_face_young_1, vaegir_face_middle_2 ],

  ["vaegir_sergeant", "Vaegir Sergeant", "Vaegir Sergeants", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_2, [
    itm.light_leather,itm.leather_armor,itm.padded_leather,
    itm.leather_boots,itm.khergit_leather_boots,
    itm.mail_gauntlets,
    itm.leather_warrior_cap,itm.vaegir_fur_cap,
    itm.hera_vaegir_inf_shield_b,
    itm.war_darts,
    itm.sword_norman,itm.skirmisher_pick,itm.one_handed_battle_axe_a,
  ], level(10)|str_13|agi_12|cha_6|int_6, wpex(100,30,30,30,30,80), knows_power_throw_1|knows_shield_1|knows_ironflesh_4|knows_power_strike_3|knows_weapon_master_2|knows_athletics_4, vaegir_face_young_1, vaegir_face_old_2 ],

  ["vaegir_varangian", "Vaegir Varangian", "Vaegir Varangians", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_2, [
    itm.vaegir_inf_armor_a,
    itm.splinted_greaves,
    itm.mail_mittens,
    itm.vaegir_fur_cap,itm.vaegir_fur_helmet,itm.vaegir_lamellar_helmet,
    itm.hera_vaegir_inf_shield_b,
    itm.javelin,
    itm.sword_medieval_d,itm.khergit_sword_b,itm.one_handed_battle_axe_c,
  ], level(12)|str_15|agi_12|int_6|cha_6, wpex(140,140,30,30,30,100), knows_power_throw_2|knows_shield_2|knows_ironflesh_4|knows_power_strike_4|knows_weapon_master_3|knows_athletics_4, vaegir_face_young_1, vaegir_face_middle_2 ],

  ["vaegir_pikeman", "Vaegir Pikeman", "Vaegir Pikemen", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_2, [
    itm.coat_of_plates,itm.coat_of_plates_red,
    itm.mail_chausses,itm.mail_boots,
    itm.scale_gauntlets,
    itm.vaegir_army_helm,
    itm.hera_vaegir_inf_shield_c,
    itm.bardiche_b,itm.bardiche_c,itm.vaegir_pick,itm.winged_mace,itm.lineman_mace,
    itm.military_pick,itm.one_handed_war_axe_a,
  ], level(14)|str_16|agi_12|int_6|cha_6, wpex(100,30,160,30,30,30), knows_shield_2|knows_ironflesh_5|knows_power_strike_5|knows_weapon_master_4|knows_athletics_4, vaegir_face_young_1, vaegir_face_older_2 ],

  ["vaegir_lineman", "Vaegir Lineman", "Vaegir Linemen", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_2, [
    itm.banded_armor,
    itm.splinted_leather_greaves,itm.iron_greaves,
    itm.lamellar_gauntlets,
    itm.vaegir_noble_helmet,
    itm.hera_vaegir_inf_shield_c,
    itm.bardiche_c,itm.bardiche_d,itm.vaegir_pick,itm.winged_mace,itm.lineman_mace,
    itm.one_handed_war_axe_b,itm.one_handed_battle_axe_b,
  ], level(16)|str_18|agi_12|int_6|cha_6, wpex(140,30,180,30,30,30), knows_shield_4|knows_athletics_4|knows_ironflesh_6|knows_power_strike_6|knows_weapon_master_4, vaegir_face_middle_1, vaegir_face_older_2 ],

  ["vaegir_veteran_varangian", "Vaegir Veteran Varangian", "Vaegir Veteran Varangians", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_2, [
    itm.vaegir_inf_armor_b,
    itm.mail_chausses,itm.mail_boots,
    itm.scale_gauntlets,
    itm.vaegir_spiked_helmet,
    itm.hera_vaegir_inf_shield_c,
    itm.javelin_vae,
    itm.khergit_sword_a,itm.military_pick,itm.one_handed_war_axe_a,
  ], level(14)|str_16|agi_12|int_6|cha_6, wpex(160,160,30,30,30,120), knows_power_throw_3|knows_shield_3|knows_ironflesh_5|knows_power_strike_5|knows_weapon_master_4|knows_athletics_4, vaegir_face_young_1, vaegir_face_older_2 ],

  ["vaegir_varangian_guard", "Vaegir Varangian Guard", "Vaegir Varangian Guards", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_2, [
    itm.vaegir_inf_armor_c,
    itm.splinted_leather_greaves,itm.iron_greaves,
    itm.lamellar_gauntlets,
    itm.vaegir_war_mask,
    itm.hera_vaegir_inf_shield_c,
    itm.javelin_vae,
    itm.sword_medieval_c_long,itm.one_handed_war_axe_b,itm.one_handed_battle_axe_b,
  ], level(16)|str_18|agi_12|int_6|cha_6, wpex(180,180,30,30,30,150), knows_power_throw_4|knows_shield_4|knows_ironflesh_6|knows_power_strike_6|knows_weapon_master_4|knows_athletics_4, vaegir_face_middle_1, vaegir_face_older_2 ],

  ["vaegir_bowman", "Vaegir Bowman", "Vaegir Bowmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac.kingdom_2, [
    itm.light_leather,
    itm.nomad_boots,itm.hunter_boots,itm.hide_boots,
    itm.hera_vaegir_inf_shield_a,
    itm.hunting_bow_vae,itm.broadhead_arrows,itm.arrows,
    itm.falchion_new,
  ], str_12|level(12)|agi_15|int_6|cha_6, wpex(90,30,30,125,30,30), knows_ironflesh_3|knows_power_strike_2|knows_weapon_master_3|knows_athletics_4|knows_power_draw_3, vaegir_face_young_1, vaegir_face_old_2 ],

  ["vaegir_archer", "Vaegir Archer", "Vaegir Archers", tf_guarantee_all, no_scene, reserved, fac.kingdom_2, [
    itm.vaegir_inf_armor_a,
    itm.nomad_boots,itm.hunter_boots,itm.hide_boots,
    itm.archer_gloves,
    itm.leather_warrior_cap,
    itm.hera_vaegir_inf_shield_a,
    itm.short_bow_vae,itm.vaegir_arrows_b,itm.piercing_arrows,itm.broadhead_arrows,
    itm.sword_medieval_b_small,
  ], str_13|level(14)|agi_16|int_6|cha_6, wpex(90,30,30,140,30,30), knows_ironflesh_3|knows_power_strike_2|knows_power_draw_4|knows_weapon_master_3|knows_athletics_5, vaegir_face_young_1, vaegir_face_older_2 ],

  ["vaegir_marksman", "Vaegir Marksman", "Vaegir Marksmen", tf_guarantee_all, no_scene, reserved, fac.kingdom_2, [
    itm.light_mail_and_plate,
    itm.leather_boots,itm.khergit_leather_boots,
    itm.archer_gloves,
    itm.vaegir_fur_cap,
    itm.hera_vaegir_inf_shield_b,
    itm.long_bow_vae,itm.vaegir_arrows_a,itm.vaegir_arrows_b,itm.vaegir_arrows_b,
    itm.sword_medieval_b_small,itm.sword_viking_a_small,
  ], str_15|level(18)|agi_18|int_6|cha_6, wpex(100,30,30,180,30,30), knows_shield_1|knows_ironflesh_3|knows_power_strike_3|knows_power_draw_5|knows_weapon_master_4|knows_athletics_6, vaegir_face_young_1, vaegir_face_older_2 ],

  ["vaegir_master_bowyer", "Vaegir Master Bowyer", "Vaegir Master Bowyers", tf_guarantee_all, no_scene, reserved, fac.kingdom_2, [
    itm.mail_and_plate,
    itm.leather_boots,itm.khergit_leather_boots,
    itm.archer_vambraces,
    itm.vaegir_fur_helmet,
    itm.hera_vaegir_inf_shield_b,
    itm.war_bow_vae,itm.vaegir_arrows_a,itm.vaegir_arrows_b,
    itm.sword_viking_a_small,
  ], str_16|level(22)|agi_21|int_6|cha_6, wpex(100,30,30,220,30,30), knows_shield_1|knows_ironflesh_4|knows_power_strike_3|knows_power_draw_5|knows_weapon_master_5|knows_athletics_7, vaegir_face_young_1, vaegir_face_older_2 ],

  ["vaegir_scout", "Vaegir Scout", "Vaegir Scouts", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_2, [
    itm.vaegir_chain,
    itm.splinted_greaves,
    itm.vaegir_fur_cap,itm.vaegir_fur_helmet,
    itm.leather_gloves,
    itm.hera_vaegir_cav_shield_a,
    itm.iron_morningstar,
    itm.armored_courser,itm.armored_hunter,
  ], level(12)|str_13|agi_14|int_6|cha_6, wpex(110,30,100,30,30,30), knows_shield_1|knows_athletics_4|knows_ironflesh_4|knows_power_strike_3|knows_weapon_master_2|knows_riding_2, vaegir_face_middle_1, vaegir_face_older_2 ],

  ["vaegir_horseman", "Vaegir Horseman", "Vaegir Horsemen", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_2, [
    itm.vaegir_lamellar_a,itm.vaegir_lamellar_b,
    itm.mail_chausses,itm.mail_boots,
    itm.mail_mittens,
    itm.vaegir_lamellar_helmet,itm.vaegir_army_helm,
    itm.hera_vaegir_cav_shield_b,
    itm.morningstar,
    itm.vaegir_warhorse_a,
  ], level(14)|str_14|agi_15|int_6|cha_6, wpex(150,30,100,30,30,30), knows_shield_2|knows_riding_3|knows_ironflesh_4|knows_power_strike_4|knows_weapon_master_2|knows_athletics_4, vaegir_face_young_1, vaegir_face_older_2 ],

  ["vaegir_druzhina", "Vaegir Druzhina", "Vaegir Druzhinniks", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_2, [
    itm.vaegir_scaled_cuirass,
    itm.splinted_leather_greaves,itm.iron_greaves,
    itm.scale_gauntlets,
    itm.vaegir_noble_helmet,itm.vaegir_war_helmet,
    itm.hera_vaegir_cav_shield_c,
    itm.elite_morningstar,
    itm.vaegir_warhorse_b,
  ], level(18)|str_15|agi_18|int_6|cha_6, wpex(180,30,140,30,30,30), knows_shield_3|knows_riding_5|knows_ironflesh_4|knows_power_strike_5|knows_weapon_master_3|knows_athletics_4, vaegir_face_middle_1, vaegir_face_older_2 ],

  ["vaegir_ivory_bowman", "Vaegir Ivory Bowman", "Vaegir Ivory Bowmen", tf_guarantee_all, no_scene, reserved, fac.kingdom_2, [
    itm.vaegir_kuyak_c,
    itm.leather_boots,itm.khergit_leather_boots,
    itm.archer_vambraces,
    itm.vaegir_fur_helmet,
    itm.long_bow_ivory,itm.vaegir_arrows_b,itm.vaegir_arrows_a,
    itm.bardiche_a,
  ], level(24)|str_15|agi_24|int_6|cha_6, wpex(100,30,100,230,30,30), knows_ironflesh_4|knows_power_strike_4|knows_power_draw_5|knows_weapon_master_6|knows_athletics_7, vaegir_face_young_1, vaegir_face_middle_2 ],

  ["vaegir_ivory_archer", "Vaegir Ivory Archer", "Vaegir Ivory Archers", tf_guarantee_all, no_scene, reserved, fac.kingdom_2, [
    itm.vaegir_kuyak_d,
    itm.splinted_greaves,
    itm.archer_vambraces,
    itm.vaegir_army_helm,
    itm.war_bow_ivory,itm.vaegir_arrows_a,
    itm.bardiche_a,itm.bardiche_b,
  ], agi_26|int_6|cha_6|level(26)|str_15, wpex(100,30,120,250,30,30), knows_ironflesh_4|knows_power_strike_4|knows_power_draw_5|knows_athletics_8|knows_weapon_master_6, vaegir_face_young_1, vaegir_face_older_2 ],

  ["vaegir_ivory_marksman", "Vaegir Ivory Marksman", "Vaegir Ivory Marksmen", tf_guarantee_all, no_scene, reserved, fac.kingdom_2, [
    itm.vaegir_kuyak_a,itm.vaegir_kuyak_b,
    itm.mail_chausses,itm.mail_boots,
    itm.archer_vambraces,
    itm.vaegir_noble_helmet,itm.vaegir_war_helmet,
    itm.war_bow_ivory,itm.vaegir_arrows_a,itm.ivory_arrows,
    itm.bardiche_b,itm.bardiche_c,
  ], level(28)|str_15|agi_28|int_6|cha_6, wpex(100,30,140,270,30,30), knows_athletics_9|knows_ironflesh_4|knows_power_strike_4|knows_power_draw_5|knows_weapon_master_6, vaegir_face_middle_1, vaegir_face_older_2 ],

  ["vaegir_ivory_sentinel", "Vaegir Ivory Sentinel", "Vaegir Ivory Sentinels", tf_guarantee_all, no_scene, reserved, fac.kingdom_2, [
    itm.vaegir_kuyak_b,
    itm.iron_greaves,
    itm.archer_vambraces,
    itm.vaegir_lichina_helm,
    itm.hera_vaegir_inf_shield_c,
    itm.war_bow_ivory,itm.ivory_arrows,
    itm.sentinel_morningstar,
  ], level(36)|str_21|agi_30|int_6|cha_6, wpex(230,30,30,420,30,30), knows_shield_5|knows_ironflesh_7|knows_power_strike_5|knows_power_draw_7|knows_weapon_master_10|knows_athletics_10, vaegir_face_young_1, vaegir_face_middle_2 ],

  ["vaegir_knyaz", "Vaegir Knyaz", "Vaegir Knyaz", tf_guarantee_all, no_scene, reserved, fac.kingdom_2, [
    itm.vaegir_kuyak_b,
    itm.iron_greaves,
    itm.archer_vambraces,
    itm.vaegir_noble_fullhelm,
    itm.hera_vaegir_inf_shield_c,
    itm.nomad_bow_ivory,itm.ivory_arrows,
    itm.weighted_morningstar,
  ], level(36)|str_21|agi_30|int_6|cha_6, wpex(260,30,30,260,30,30), knows_ironflesh_7|knows_power_strike_6|knows_power_draw_7|knows_shield_4|knows_weapon_master_6|knows_horse_archery_6, vaegir_face_young_1, vaegir_face_middle_2 ],

  ["vaegir_prison_guard","Prison Guard","Prison Guards", tf_guarantee_all_wo_ranged,0,reserved, fac.kingdom_2,[
    itm.vaegir_chain,
    itm.splinted_greaves,
    itm.mail_gauntlets,
    itm.vaegir_fur_cap,
    #itm.hera_vaegir_inf_shield_c,
    itm.jarid,
    itm.bardiche_b,
  ],level(24)|def_attrib,wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,vaegir_face_middle_1,vaegir_face_older_2],

  ["vaegir_castle_guard","Castle Guard","Castle Guards", tf_guarantee_all_wo_ranged,0,reserved, fac.kingdom_2,[
    itm.vaegir_lamellar_a,itm.vaegir_lamellar_b,
    itm.splinted_leather_greaves,itm.iron_greaves,
    itm.lamellar_gauntlets,
    itm.vaegir_noble_helm,
    itm.hera_vaegir_inf_shield_c,
    itm.weighted_morningstar,
  ],level(24)|def_attrib,wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,vaegir_face_middle_1,vaegir_face_older_2],

  ["vaegir_messenger","Vaegir Messenger","Vaegir Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,reserved, fac.kingdom_2,[],level(25)|def_attrib|agi_21,wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,vaegir_face_young_1,vaegir_face_older_2],
  ["vaegir_deserter","Vaegir Deserter","Vaegir Deserters",tf_guarantee_boots|tf_guarantee_armor,0,reserved, fac.kingdom_2,[],level(14)|def_attrib|str_10,wp(80),knows_ironflesh_1|knows_power_draw_1,vaegir_face_young_1,vaegir_face_older_2],


  #Begin Khergit
  ["khergit_tribesman", "Khergit Tribesman", "Khergit Tribesmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse, no_scene, reserved, fac.kingdom_3, [
    itm.nomad_vest,itm.nomad_robe,itm.nomad_armor,itm.khergit_armor,
    itm.nomad_boots,itm.hunter_boots,
    itm.leather_gloves,
    itm.throwing_knives,itm.throwing_daggers,itm.darts,
    itm.staff,itm.wooden_stick,itm.club,itm.cudgel,
    itm.farm_horse,itm.riding_horse,
  ], level(8)|str_12|agi_11|cha_6|int_6, wpex(50,30,30,30,30,40), knows_riding_3|knows_ironflesh_1|knows_weapon_master_1, khergit_face_younger_1, khergit_face_old_2 ],

  ["khergit_rider", "Khergit Rider", "Khergit Riders", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse, no_scene, reserved, fac.kingdom_3, [
    itm.steppe_armor,
    itm.hide_boots,itm.light_leather_boots,
    itm.leather_gloves,
    itm.fur_hat,itm.nomad_cap_b,itm.leather_steppe_cap_a,
    itm.khergit_shield_a1,itm.khergit_shield_a2,itm.khergit_shield_a3,
    itm.darts,itm.war_darts,itm.hunting_bow_khe,itm.hunting_arrows,itm.arrows,
    itm.khergit_sword_b,
    itm.khergit_horse,
  ], level(10)|str_12|agi_13|cha_6|int_6, wpex(90,30,30,70,30,90), knows_riding_4|knows_ironflesh_1|knows_weapon_master_2|knows_power_draw_1|knows_power_throw_1|knows_shield_1, khergit_face_young_1, khergit_face_older_2 ],

  ["khergit_lancer", "Khergit Lancer", "Khergit Lancers", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_3, [
    itm.khergit_chain,
    itm.leather_boots,itm.khergit_leather_boots,
    itm.mail_mittens,
    itm.leather_steppe_cap_b,
    itm.khergit_shield_a1,itm.khergit_shield_a2,itm.khergit_shield_a3,
    itm.light_lance,itm.khergit_sword_a,
    itm.khergit_warhorse_a,
  ], level(12)|str_12|agi_15|int_6|cha_6, wpex(90,30,125,30,30,90), knows_shield_2|knows_riding_5|knows_power_strike_2|knows_power_throw_2|knows_ironflesh_1|knows_weapon_master_3, khergit_face_middle_1, khergit_face_older_2 ],

  ["khergit_scarred_lancer", "Khergit Scarred Lancer", "Khergit Scarred Lancers", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_3, [
    itm.khergit_lancer_cuirass,
    itm.splinted_greaves,
    itm.scale_gauntlets,
    itm.khergit_cavalry_helmet,
    itm.khergit_shield_b1,itm.khergit_shield_b2,
    itm.khergit_lance_a,itm.khergit_sword_a,itm.khergit_sword_c,
    itm.khergit_charger_a,
  ], level(16)|str_14|agi_17|int_6|cha_6, wpex(105,30,160,30,30,105), knows_shield_3|knows_riding_5|knows_power_strike_3|knows_ironflesh_2|knows_power_throw_3|knows_weapon_master_4, khergit_face_middle_1, khergit_face_older_2 ],

  ["khergit_savage_lancer", "Khergit Savage Lancer", "Khergit Savage Lancers", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_3, [
    itm.khergit_lancer_armor,
    itm.splinted_leather_greaves,itm.iron_greaves,
    itm.lamellar_gauntlets,
    itm.khergit_war_helmet,
    itm.khergit_shield_b1,itm.khergit_shield_b2,
    itm.khergit_lance_b,itm.khergit_sword_c,
    itm.khergit_charger_b,
  ], level(20)|str_14|agi_21|int_6|cha_6, wpex(130,30,180,30,30,130), knows_shield_4|knows_riding_6|knows_power_strike_3|knows_ironflesh_3|knows_power_throw_3|knows_weapon_master_5, khergit_face_middle_1, khergit_face_older_2 ],

  ["khergit_horse_archer", "Khergit Horse Archer", "Khergit Horse Archers", tf_mounted|tf_guarantee_all, no_scene, reserved, fac.kingdom_3, [
    itm.lamellar_vest,itm.lamellar_vest_khergit,
    itm.hide_boots,itm.light_leather_boots,
    itm.steppe_cap,itm.khergit_leather_helmet,
    itm.khergit_shield_a1,itm.khergit_shield_a2,itm.khergit_shield_a3,
    itm.short_bow_khe,itm.arrows,itm.broadhead_arrows,itm.khergit_arrows_a,
    itm.sword_medieval_e,
    itm.courser_horse,itm.hunter_horse,
  ], level(12)|str_12|agi_15|int_6|cha_6, wpex(75,30,30,140,30,30), knows_shield_1|knows_riding_5|knows_horse_archery_5|knows_power_draw_2|knows_weapon_master_3, khergit_face_middle_1, khergit_face_older_2 ],
  
  ["khergit_veteran_horse_archer", "Khergit Veteran Horse Archer", "Khergit Veteran Horse Archers", tf_mounted|tf_guarantee_all, no_scene, reserved, fac.kingdom_3, [
    itm.khergit_kharash_vest,
    itm.leather_boots,itm.khergit_leather_boots,
    itm.nomad_cap,
    itm.khergit_shield_a1,itm.khergit_shield_a2,itm.khergit_shield_a3,
    itm.nomad_bow_khe,itm.bodkin_arrows,itm.piercing_arrows,itm.barbed_arrows,itm.khergit_arrows_a,
    (itm.sword_medieval_e,imod.fine),(itm.sword_medieval_e,imod.heavy),
    itm.armored_courser,itm.armored_hunter,
  ], level(16)|str_12|agi_19|int_6|cha_6, wpex(95,30,30,180,30,30), knows_shield_2|knows_riding_6|knows_horse_archery_6|knows_power_draw_3|knows_weapon_master_4, khergit_face_middle_1, khergit_face_older_2 ],

  ["khergit_master_horse_archer", "Khergit Master Horse Archer", "Khergit Master Horse Archers", tf_mounted|tf_guarantee_all, no_scene, reserved, fac.kingdom_3, [
    itm.khergit_mail_plate_a,itm.khergit_mail_plate_b,itm.khergit_mail_plate_c,
    itm.leather_boots,itm.khergit_leather_boots,
    itm.khergit_cavalry_helmet,
    itm.khergit_shield_b1,itm.bodkin_arrows,itm.khergit_shield_b2,
    itm.strong_bow_khe,itm.khergit_arrows_b,
    (itm.sword_medieval_e,imod.heavy),(itm.sword_medieval_e,imod.deadly),(itm.sword_medieval_e,imod.powerful),(itm.sword_medieval_e,imod.tempered),
    itm.armored_courser,itm.armored_hunter,
  ], level(20)|str_18|agi_23|int_6|cha_6, wpex(115,30,30,220,30,30), knows_shield_3|knows_riding_7|knows_horse_archery_7|knows_power_draw_4|knows_weapon_master_5, khergit_face_middle_1, khergit_face_older_2 ],

  ["khergit_kharash", "Khergit Kharash", "Khergit Kharash", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_3, [
    itm.khergit_leather_a,itm.khergit_leather_b,
    itm.hide_boots,itm.light_leather_boots,
    itm.khergit_leather_helmet,
    itm.mail_gauntlets,
    itm.khergit_shield_a1,itm.khergit_shield_a2,itm.khergit_shield_a3,
    itm.war_darts,itm.javelin,
    itm.kharash_blade,
    itm.hunter_horse,itm.armored_hunter,
  ], level(10)|str_12|agi_13|cha_6|int_6, wpex(90,30,30,30,30,100), knows_riding_4|knows_ironflesh_1|knows_weapon_master_2|knows_athletics_2|knows_shield_2|knows_power_throw_2, khergit_face_younger_1, khergit_face_old_2 ],

  ["khergit_kharash_scout", "Khergit Kharash Scout", "Khergit Kharash Scouts", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_3, [
    itm.khergit_kharash_vest,
    itm.leather_boots,itm.khergit_leather_boots,
    itm.scale_gauntlets,
    itm.leather_steppe_cap_b,itm.nomad_cap,
    itm.khergit_shield_a1,itm.khergit_shield_a2,itm.khergit_shield_a3,
    itm.kharash_blade,itm.kharash_blade,itm.khergit_sword_d,
    itm.khergit_warhorse_a,
  ], level(12)|str_12|agi_15|int_6|cha_6, wpex(140,30,75,30,30,30), SKILLS(riding=3,weapon_master=3,ironflesh=2,power_strike=3,shield=2,athletics=2), khergit_face_young_1, khergit_face_older_2 ],

  ["khergit_kharash_rider", "Khergit Kharash Rider", "Khergit Kharash Riders", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_3, [
    itm.lamellar_armor,
    itm.splinted_greaves,
    itm.scale_gauntlets,
    itm.nomad_cap,itm.khergit_cavalry_helmet,itm.khergit_war_helmet,
    itm.khergit_shield_b1,itm.khergit_shield_b2,
    itm.kharash_blade,itm.khergit_sword_d,itm.khergit_sword_d,
    itm.khergit_warhorse_b,
  ], level(16)|str_12|agi_18|int_6|cha_6, wpex(180,30,90,30,30,30), SKILLS(riding=4,weapon_master=4,ironflesh=3,power_strike=4,shield=3,athletics=4), khergit_face_young_1, khergit_face_older_2 ],

  ["khergit_kharash_clansman", "Khergit Kharash Clansman", "Khergit Kharash Clansmen", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_3, [
    itm.khergit_kharash_armor,
    itm.mail_chausses,itm.mail_boots,
    itm.lamellar_gauntlets,
    itm.khergit_war_helmet,itm.khergit_covered_helm,
    itm.khergit_shield_c1,itm.khergit_shield_c2,itm.khergit_shield_c3,
    itm.khergit_sword_d,
    itm.khergit_warhorse_c,
  ], level(20)|str_12|agi_21|int_6|cha_6, wpex(220,30,105,30,30,30), SKILLS(riding=4,weapon_master=5,ironflesh=4,power_strike=6,shield=4,athletics=5), khergit_face_younger_1, khergit_face_old_2 ],

  ["khergit_scarred_kharash", "Khergit Scarred Kharash", "Khergit Scarred Kharash", tf_mounted|tf_guarantee_all, no_scene, reserved, fac.kingdom_3, [
    itm.khergit_clansman_vest,
    itm.leather_boots,itm.khergit_leather_boots,
    itm.scale_gauntlets,
    itm.khergit_covered_helm,
    itm.khergit_shield_b1,itm.khergit_shield_b2,
    itm.javelin_khe,itm.jarid,
    itm.kharash_blade,
    itm.armored_courser,itm.armored_hunter,
  ], level(14)|str_14|agi_15|int_6|cha_6, wpex(115,30,30,30,30,120), SKILLS(riding=5,power_throw=4,weapon_master=3,horse_archery=3,power_strike=1), khergit_face_middle_1, khergit_face_older_2 ],

  ["khergit_savage_kharash", "Khergit Savage Kharash", "Khergit Savage Kharash", tf_mounted|tf_guarantee_all, no_scene, reserved, fac.kingdom_3, [
    itm.khergit_clansman_armor,
    itm.splinted_greaves,
    itm.lamellar_gauntlets,
    itm.khergit_covered_helm,
    itm.khergit_shield_c1,itm.khergit_shield_c2,itm.khergit_shield_c3,
    itm.jarid,itm.throwing_spears,itm.throwing_spears_b,
    itm.khergit_sword_d,
    itm.armored_courser,itm.armored_hunter,
  ], level(18)|str_18|agi_15|int_6|cha_6, wpex(135,30,30,30,30,140), SKILLS(riding=6,power_throw=6,weapon_master=4,horse_archery=5,power_strike=1,ironflesh=1), khergit_face_middle_1, khergit_face_older_2 ],

  ["khergit_tribal_chieftain", "Khergit Tribal Chieftain", "Khergit Tribal Chieftains", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_3, [
    itm.khergit_mail_plate_a,itm.khergit_mail_plate_b,itm.khergit_mail_plate_c,
    itm.splinted_leather_greaves,itm.iron_greaves,
    itm.lamellar_gauntlets,
    itm.khergit_war_helmet,
    itm.khergit_shield_b1,itm.khergit_shield_b2,
    itm.throwing_spears,itm.throwing_spears_b,
    itm.hafted_blade_b,itm.khergit_sword,
    itm.khergit_warhorse_a,
  ], level(22)|str_15|agi_22|int_6|cha_6, wpex(140,30,180,30,30,130), knows_shield_3|knows_riding_7|knows_ironflesh_3|knows_power_throw_5|knows_power_strike_3|knows_weapon_master_5, khergit_face_middle_1, khergit_face_older_2 ],

  ["khergit_tarkhan", "Khergit Tarkhan", "Khergit Tarkhans", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_3, [
    itm.tarkhan_lamellar,
    itm.tarkhan_boots,
    itm.lamellar_gauntlets,
    itm.tarkhan_helm,
    itm.khergit_shield_c1,itm.khergit_shield_c2,itm.khergit_shield_c3,
    itm.hafted_blade_c,itm.khergit_sword_two_handed_a,
    itm.khergit_charger_a,
  ], level(24)|str_18|agi_21|int_6|cha_6, wpex(150,30,225,30,30,150), knows_shield_4|knows_ironflesh_3|knows_power_strike_3|knows_power_throw_6|knows_weapon_master_6|knows_riding_7, khergit_face_younger_1, khergit_face_old_2 ],

  ["khergit_jurtchi", "Khergit Jurtchi", "Khergit Jurtchi", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_3, [
    itm.khergit_jurtchi_armor,
    itm.tarkhan_boots,
    itm.lamellar_gauntlets,
    itm.tarkhan_helm,
    itm.khergit_shield_c1,itm.khergit_shield_c2,itm.khergit_shield_c3,
    itm.hafted_blade_a,itm.khergit_sword_two_handed_a,
    itm.khergit_charger_b,
  ], level(26)|str_18|agi_21|int_6|cha_6, wpex(160,30,245,30,30,170), knows_shield_5|knows_riding_7|knows_power_strike_5|knows_ironflesh_5|knows_power_throw_6|knows_weapon_master_6, khergit_face_middle_1, khergit_face_older_2 ],

  ["khergit_elite_horse_archer", "Khergit Elite Horse Archer", "Khergit Elite Horse Archer", tf_mounted|tf_guarantee_all, no_scene, reserved, fac.kingdom_3, [
    itm.khergit_mangudai_cuirass_a,itm.khergit_mangudai_cuirass_b,
    itm.mail_chausses,itm.mail_boots,
    itm.khergit_covered_helm,
    #itm.khergit_shield_b1,itm.khergit_shield_b2,
    itm.strong_bow_khe,itm.khergit_arrows_b,
    itm.hafted_blade_b,
    itm.khergit_warhorse_b,
  ], level(24)|str_14|agi_25|int_6|cha_6, wpex(30,30,155,230,30,30), knows_riding_8|knows_horse_archery_8|knows_ironflesh_1|knows_power_draw_5|knows_weapon_master_6, khergit_face_middle_1, khergit_face_older_2 ],

  ["khergit_mangudai", "Khergit Mangudai", "Khergit Mangudai", tf_mounted|tf_guarantee_all, no_scene, reserved, fac.kingdom_3, [
    itm.khergit_mangudai_armor,
    itm.mail_chausses,itm.mail_boots,
    itm.khergit_covered_helm,
    #itm.khergit_shield_c1,itm.khergit_shield_c2,itm.khergit_shield_c3,
    itm.khergit_bow_khe,itm.khergit_arrows_b,itm.khergit_arrows_c,
    itm.hafted_blade_c,
    itm.khergit_warhorse_b,
  ], level(26)|str_14|agi_27|int_6|cha_6, wpex(30,30,170,260,30,30), knows_riding_9|knows_horse_archery_9|knows_power_draw_4|knows_ironflesh_1|knows_weapon_master_6, khergit_face_middle_1, khergit_face_older_2 ],

  ["khergit_keshik", "Khergit Keshik", "Khergit Keshik", tf_mounted|tf_guarantee_all, no_scene, reserved, fac.kingdom_3, [
    itm.khergit_jurtchi_armor,
    itm.iron_greaves,
    itm.tarkhan_helm,
    itm.khergit_shield_c1,itm.khergit_shield_c2,itm.khergit_shield_c3,
    itm.khergit_bow_khe,itm.khergit_arrows_c,
    (itm.sword_medieval_e,imod.masterwork),
    itm.khergit_warhorse_c,
  ], level(33)|str_18|agi_30|int_6|cha_6, wpex(200,30,180,300,30,30), knows_shield_6|knows_riding_10|knows_ironflesh_3|knows_weapon_master_7|knows_power_draw_6|knows_horse_archery_10, khergit_face_middle_1, khergit_face_older_2 ],

  ["khergit_guanren", "Khergit Guanren", "Khergit Guanren", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_3, [
    itm.khergit_jurtchi_armor,
    itm.iron_greaves,
    itm.lamellar_gauntlets,
    itm.khergit_noble_helm,
    itm.khergit_shield_c1,itm.khergit_shield_c2,itm.khergit_shield_c3,
    itm.throwing_spears,itm.throwing_spears_b,
    itm.khergit_lance_b,itm.khergit_sword_two_handed_b,
    itm.khergit_charger_c,
  ], level(33)|str_18|agi_30|int_6|cha_6, wpex(180,30,210,30,30,320), knows_power_strike_5|knows_ironflesh_5|knows_power_throw_6|knows_weapon_master_10|knows_riding_5|knows_horse_archery_6, khergit_face_middle_1, khergit_face_older_2 ],

  ["khergit_prison_guard","Prison Guard","Prison Guards", tf_guarantee_all,0,reserved, fac.kingdom_3,[
    itm.lamellar_vest,itm.lamellar_vest_khergit,
    itm.splinted_greaves,
    itm.mail_gauntlets,
    itm.khergit_cavalry_helmet,
    itm.khergit_shield_b1,itm.khergit_shield_b2,
    itm.throwing_spears,
    itm.khergit_sword,
  ],level(24)|def_attrib,wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,khergit_face_middle_1,khergit_face_older_2],

  ["khergit_castle_guard","Castle Guard","Castle Guards", tf_guarantee_all_wo_ranged,0,reserved, fac.kingdom_3,[
    itm.khergit_kharash_armor,
    itm.iron_greaves,
    itm.lamellar_gauntlets,
    itm.khergit_noble_helm,
    itm.khergit_shield_c1,itm.khergit_shield_c2,itm.khergit_shield_c3,
    itm.khergit_sword_two_handed_b,
  ],level(24)|def_attrib,wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,khergit_face_middle_1,khergit_face_older_2],

  ["khergit_messenger","Khergit Messenger","Khergit Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,reserved, fac.kingdom_3,[],level(25)|def_attrib|agi_21,wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,khergit_face_young_1,khergit_face_older_2],
  ["khergit_deserter","Khergit Deserter","Khergit Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,reserved, fac.kingdom_3,[],level(14)|def_attrib|str_10,wp(80),knows_ironflesh_1|knows_power_draw_1,khergit_face_young_1,khergit_face_older_2],

  # TODO: RANGED WEAPONS STARTING FROM THIS POINT

  #Begin Nord
  ["nord_recruit", "Nord Volunteer", "Nord Volunteers", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac.kingdom_4, [
    itm.nordic_shirt_01,itm.nordic_shirt_02,itm.nordic_shirt_03,itm.nordic_shirt_04,itm.nordic_shirt_05,itm.nordic_shirt_06,
    itm.wrapping_boots,itm.ankle_boots,
    itm.common_hood,itm.woolen_cap,itm.felt_hat,
    itm.pitch_fork,itm.pickaxe,itm.staff,itm.cleaver,itm.club,itm.smith_hammer,itm.hatchet,itm.beef_splitter,
  ], level(6)|str_12|agi_9|int_6|cha_6, wpex(50,30,50,30,30,30), knows_ironflesh_2|knows_weapon_master_1|knows_athletics_2, nord_face_younger_1, nord_face_old_2 ],

  ["nord_thrall", "Nord Thrall", "Nord Thralls", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, no_scene, reserved, fac.kingdom_4, [
    itm.leather_jacket,itm.leather_vest,itm.leather_jerkin,
    itm.wrapping_boots,itm.ankle_boots,
    itm.leather_gloves,
    itm.nordic_archer_helmet,
    itm.nord_round_shield_a1,itm.nord_round_shield_a2,itm.nord_round_shield_a3,
    itm.light_throwing_axes,
    itm.sword_medieval_b_small,
  ], level(8)|str_12|agi_11|int_6|cha_6, wpex(70,30,30,30,30,65), knows_shield_1|knows_ironflesh_3|knows_power_throw_1|knows_athletics_3|knows_weapon_master_2, nord_face_young_1, nord_face_old_2 ],

  ["nord_drengr", "Nord Drengr", "Nord Drengir", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_4, [
    itm.nordic_leather_1,itm.nordic_leather_2,
    itm.hunter_boots,itm.hide_boots,
    itm.mail_gauntlets,
    itm.nordic_skullcap,
    itm.nord_round_shield_b1,itm.nord_round_shield_b2,itm.nord_round_shield_b3,
    itm.light_throwing_axes,itm.throwing_axes,
    itm.sword_viking_a_small,itm.one_handed_battle_axe_a,
  ], level(10)|str_13|agi_12|int_6|cha_6, wpex(80,30,30,30,30,100), knows_shield_3|knows_ironflesh_3|knows_power_throw_2|knows_athletics_3|knows_weapon_master_2, nord_face_young_1, nord_face_old_2 ],

  ["nord_warrior", "Nord Warrior", "Nord Warriors", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_4, [
    itm.nordic_hauberk_1,itm.nordic_hauberk_4,
    itm.light_leather_boots,itm.leather_boots,
    itm.scale_gauntlets,
    itm.nordic_raider_helmet,
    itm.nord_round_shield_b1,itm.nord_round_shield_b2,itm.nord_round_shield_b3,
    itm.throwing_axes,
    itm.sword_viking_b_small,itm.one_handed_battle_axe_c,
  ], level(14)|str_17|agi_12|int_6|cha_6, wpex(100,30,30,30,30,120), knows_shield_4|knows_ironflesh_5|knows_power_strike_2|knows_power_throw_2|knows_athletics_4|knows_weapon_master_4, nord_face_young_1, nord_face_older_2 ],

  ["nord_shieldmaster", "Nord Shieldmaster", "Nord Shieldmasters", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_4, [
    itm.nordic_byrnie_1,itm.nordic_byrnie_6,
    itm.light_leather_boots,itm.leather_boots,
    itm.lamellar_gauntlets,
    itm.nordic_helmet,
    itm.nord_round_shield_c1,itm.nord_round_shield_c2,itm.nord_round_shield_c3,
    itm.throwing_axes,itm.heavy_throwing_axes,
    itm.one_handed_war_axe_a,
  ], level(18)|str_21|agi_12|int_6|cha_6, wpex(140,30,30,30,30,140), knows_ironflesh_6|knows_power_strike_3|knows_power_throw_2|knows_athletics_5|knows_shield_6|knows_weapon_master_4, nord_face_young_1, nord_face_older_2 ],

  ["nord_merkismathr", "Nord Merkismathr", "Nord Merkismathir", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_4, [
    itm.nordic_decor_scale_1,itm.nordic_decor_scale_2,
    itm.splinted_greaves,
    itm.gauntlets,
    itm.nordic_huscarl_helmet,
    itm.nord_round_shield_c1,itm.nord_round_shield_c2,itm.nord_round_shield_c3,
    itm.heavy_throwing_axes,
    itm.one_handed_war_axe_b,
  ], level(22)|str_21|agi_16|int_6|cha_6, wpex(180,30,30,30,30,150), knows_ironflesh_6|knows_power_strike_4|knows_power_throw_2|knows_athletics_4|knows_shield_7|knows_weapon_master_5, nord_face_middle_1, nord_face_older_2 ],

  ["nord_veteran_warrior", "Nord Veteran Warrior", "Nord Veteran Warriors", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_4, [
    itm.nordic_byrnie_1,itm.nordic_byrnie_6,
    itm.light_leather_boots,itm.leather_boots,
    itm.scale_gauntlets,
    itm.nordic_helmet,
    itm.nord_round_shield_b1,itm.nord_round_shield_b2,itm.nord_round_shield_b3,
    itm.throwing_axes,itm.heavy_throwing_axes,
    itm.one_handed_battle_axe_b,
  ], level(18)|str_21|agi_12|int_6|cha_6, wpex(120,100,30,30,30,160), knows_shield_5|knows_ironflesh_6|knows_power_strike_3|knows_power_throw_4|knows_athletics_4|knows_weapon_master_4, nord_face_young_1, nord_face_old_2 ],

  ["nord_berserker", "Nord Berserker", "Nord Berserkers", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_4, [
    itm.nordic_decor_scale_1,itm.nordic_decor_scale_2,
    itm.splinted_greaves,
    itm.gauntlets,
    itm.nordic_huscarl_helmet,
    itm.heavy_throwing_axes,itm.heavy_throwing_axes,
    itm.long_axe_a,itm.long_axe_b,itm.long_axe_c,
  ], level(22)|str_22|agi_15|int_6|cha_6, wpex(30,135,30,30,30,180), knows_ironflesh_6|knows_power_strike_4|knows_weapon_master_5|knows_athletics_5|knows_power_throw_5, nord_face_young_1, nord_face_old_2 ],

  ["nord_raiding_hunter", "Nord Raiding Hunter", "Nord Raiding Hunters", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac.kingdom_4, [
    itm.nordic_archer_armor_a,
    itm.wrapping_boots,itm.ankle_boots,
    itm.padded_coif,itm.leather_cap,
    itm.hunting_bow_nor,itm.arrows,
    itm.two_handed_battle_axe_a,
  ], str_15|level(12)|agi_12|int_6|cha_6, wpex(30,90,30,140,30,65), knows_ironflesh_3|knows_athletics_4|knows_power_throw_1|knows_power_draw_3|knows_weapon_master_4, nord_face_young_1, nord_face_old_2 ],

  ["nord_raiding_archer", "Nord Raiding Archer", "Nord Raiding Archers", tf_guarantee_all, no_scene, reserved, fac.kingdom_4, [
    itm.nordic_archer_armor_b,
    itm.wrapping_boots,itm.ankle_boots,
    itm.nordic_archer_helmet,
    itm.nord_round_shield_a1,itm.nord_round_shield_a2,itm.nord_round_shield_a3,
    itm.short_bow_nor,itm.piercing_arrows,itm.broadhead_arrows,itm.piercing_arrows,
    itm.two_handed_battle_axe_b,
  ], str_17|level(14)|agi_12|int_6|cha_6, wpex(30,110,30,160,30,85), knows_ironflesh_4|knows_power_draw_4|knows_athletics_4|knows_power_throw_1|knows_weapon_master_4, nord_face_young_1, nord_face_old_2 ],

  ["nord_raiding_marksman", "Nord Raiding Marksman", "Nord Raiding Marksmen", tf_guarantee_all, no_scene, reserved, fac.kingdom_4, [
    itm.nordic_archer_armor_c1,itm.nordic_archer_armor_c2,
    itm.hunter_boots,itm.hide_boots,
    itm.nordic_veteran_archer_helmet,
    itm.nord_round_shield_a1,itm.nord_round_shield_a2,itm.nord_round_shield_a3,
    itm.long_bow_nor,itm.broadhead_arrows,itm.piercing_arrows,
    itm.two_handed_battle_axe_e,
  ], str_19|level(16)|agi_12|int_6|cha_6, wpex(30,130,30,180,30,95), knows_ironflesh_4|knows_power_draw_5|knows_athletics_4|knows_power_throw_2|knows_weapon_master_4, nord_face_middle_1, nord_face_older_2 ],

  ["nord_skald", "Nord Skald", "Nord Skalds", tf_guarantee_all, no_scene, reserved, fac.kingdom_4, [
    itm.nordic_archer_armor_d,
    itm.light_leather_boots,itm.leather_boots,
    itm.spiked_helmet,
    itm.nord_round_shield_b1,itm.nord_round_shield_b2,itm.nord_round_shield_b3,
    itm.long_bow_nor,itm.bodkin_arrows,
    itm.voulge,
  ], level(18)|str_21|agi_12|int_6|cha_6, wpex(30,140,30,200,30,105), knows_ironflesh_4|knows_power_draw_6|knows_athletics_4|knows_power_throw_2|knows_weapon_master_5, nord_face_middle_1, nord_face_older_2 ],

  ["nord_butsecarl", "Nord Butsecarl", "Nord Butsecarls", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_4, [
    itm.mail_hauberk,itm.mail_hauberk_b,itm.haubergeon,
    itm.light_leather_boots,itm.leather_boots,
    itm.mail_mittens,
    itm.norman_helmet,
    itm.nord_round_shield_a1,itm.nord_round_shield_a2,itm.nord_round_shield_a3,
    itm.sword_viking_a,
    itm.hunter_horse,itm.armored_hunter,
  ], level(12)|str_14|agi_13|int_6|cha_6, wpex(90,30,30,30,30,140), knows_ironflesh_3|knows_shield_1|knows_athletics_3|knows_weapon_master_3|knows_power_throw_4|knows_riding_3, rhodok_face_young_1, rhodok_face_old_2 ],

  ["nord_lithman", "Nord Lithman", "Nord Lithmen", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_4, [
    itm.byrnie,
    itm.mail_chausses,itm.mail_boots,
    itm.scale_gauntlets,
    itm.nordic_footman_helmet,
    itm.nord_round_shield_b1,itm.nord_round_shield_b2,itm.nord_round_shield_b3,
    itm.sword_viking_b,
    itm.nordic_warhorse_a,
  ], level(14)|str_14|agi_15|int_6|cha_6, wpex(120,30,30,30,30,160), knows_ironflesh_3|knows_weapon_master_4|knows_shield_2|knows_athletics_3|knows_power_throw_4|knows_riding_3, nord_face_young_1, nord_face_old_2 ],

  ["nord_viking", "Nord Viking", "Nord Vikings", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_4, [
    itm.scale_armor,
    itm.splinted_leather_greaves,itm.iron_greaves,
    itm.lamellar_gauntlets,
    itm.nordic_fighter_helmet,
    itm.nord_round_shield_d1,itm.nord_round_shield_d2,itm.nord_round_shield_d3,
    itm.sword_viking_c_long,
    itm.nordic_warhorse_b,
  ], level(16)|str_16|agi_15|int_6|cha_6, wpex(150,30,30,30,30,180), knows_ironflesh_3|knows_power_throw_4|knows_weapon_master_4|knows_shield_3|knows_athletics_3|knows_riding_4, nord_face_young_1, nord_face_old_2 ],

  ["nord_housecarl", "Nord Housecarl", "Nord Housecarls", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_4, [
    itm.nordic_noble_armor_1,
    itm.mail_chausses,itm.mail_boots,
    itm.mail_mittens,
    itm.nordic_helmet,
    itm.nord_round_shield_b1,itm.nord_round_shield_b2,itm.nord_round_shield_b3,
    itm.throwing_axes,itm.heavy_throwing_axes,
    itm.nordic_axe_a,
  ], level(24)|str_24|agi_15|int_6|cha_6, wpex(160,30,30,30,30,140), knows_shield_5|knows_ironflesh_7|knows_power_strike_6|knows_weapon_master_5|knows_athletics_4|knows_power_throw_5, nord_face_young_1, nord_face_old_2 ],

  ["nord_champion_housecarl", "Nord Champion Housecarl", "Nord Champion Housecarls", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_4, [
    itm.nordic_noble_armor_2,
    itm.mail_chausses,itm.mail_boots,
    itm.scale_gauntlets,
    itm.nordic_huscarl_helmet,
    itm.nord_round_shield_c1,itm.nord_round_shield_c2,itm.nord_round_shield_c3,
    itm.heavy_throwing_axes,
    itm.nordic_axe_b,
  ], level(26)|str_26|agi_15|int_6|cha_6, wpex(180,30,30,30,30,160), knows_shield_6|knows_ironflesh_8|knows_power_strike_6|knows_weapon_master_5|knows_athletics_4|knows_power_throw_6, nord_face_young_1, nord_face_old_2 ],

  ["nord_thane", "Nord Thane", "Nord Thanes", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_4, [
    itm.nordic_noble_armor_3,
    itm.splinted_leather_greaves,itm.iron_greaves,
    itm.lamellar_gauntlets,
    itm.nordic_warlord_helmet,
    itm.nord_round_shield_c1,itm.nord_round_shield_c2,itm.nord_round_shield_c3,
    itm.heavy_throwing_axes,
    itm.nordic_axe_c,
  ], level(28)|str_28|agi_15|int_6|cha_6, wpex(200,30,30,30,30,180), knows_shield_7|knows_ironflesh_9|knows_power_strike_6|knows_power_throw_7|knows_weapon_master_5|knows_athletics_4, nord_face_young_1, nord_face_old_2 ],

  ["nord_einherjar", "Nord Einherjar", "Nord Einherjar", tf_guarantee_all, no_scene, reserved, fac.kingdom_4, [
    itm.nordic_decor_scale_2,
    itm.splinted_leather_greaves,
    itm.gauntlets,
    itm.nordic_warlord_helmet,
    itm.nord_round_shield_c1,itm.nord_round_shield_c2,itm.nord_round_shield_c3,
    itm.heavy_throwing_axes,
    itm.nordic_axe_c,
  ], level(35)|str_30|agi_18|int_6|cha_6, wpex(30,220,30,30,30,220), knows_shield_8|knows_ironflesh_10|knows_power_strike_10|knows_weapon_master_5|knows_athletics_6|knows_power_throw_9, nord_face_young_1, nord_face_old_2 ],

  ["nord_valkyrie", "Nord Valkyrie", "Nord Valkyries", tf_female|tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_4, [
    itm.nordic_decor_scale_2,
    itm.iron_greaves,
    itm.gauntlets,
    itm.nordic_noble_helm,
    itm.nord_round_shield_d1,itm.nord_round_shield_d2,itm.nord_round_shield_d3,
    itm.light_lance,itm.cavalry_lance,itm.great_lance,itm.sword_viking_a_long,
    itm.nordic_warhorse_b,
  ], level(36)|str_24|agi_27|int_6|cha_6, wpex(150,30,30,30,30,340), knows_ironflesh_6|knows_power_strike_7|knows_shield_7|knows_athletics_4|knows_riding_7|knows_weapon_master_8, woman_face_1, woman_face_2 ],

  ["nord_prison_guard","Prison Guard","Prison Guards", tf_guarantee_all_wo_ranged,0,reserved, fac.kingdom_4,[
    itm.nordic_byrnie_1,itm.nordic_byrnie_6,
    itm.scale_gauntlets,
    itm.light_leather_boots,itm.leather_boots,
    itm.nordic_footman_helmet,
    itm.nord_round_shield_b1,itm.nord_round_shield_b2,itm.nord_round_shield_b3,
    itm.one_handed_war_axe_b,
  ],level(24)|def_attrib,wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,nord_face_middle_1,nord_face_older_2],

  ["nord_castle_guard","Castle Guard","Castle Guards", tf_guarantee_all_wo_ranged,0,reserved, fac.kingdom_4,[
    itm.nordic_decor_scale_1,itm.nordic_decor_scale_2,
    itm.splinted_leather_greaves,itm.iron_greaves,
    itm.lamellar_gauntlets,
    itm.nordic_warlord_helmet,
    itm.nord_round_shield_c1,itm.nord_round_shield_c2,itm.nord_round_shield_c3,
    itm.nordic_axe_c,
  ],level(24)|def_attrib,wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,nord_face_middle_1,nord_face_older_2],

  ["nord_messenger","Nord Messenger","Nord Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,reserved, fac.kingdom_4,[],level(25)|def_attrib|agi_21,wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,nord_face_young_1,nord_face_older_2],
  ["nord_deserter","Nord Deserter","Nord Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,reserved, fac.kingdom_4,[],level(14)|def_attrib|str_10,wp(80),knows_ironflesh_1|knows_power_draw_1,nord_face_young_1,nord_face_older_2],

  #Begin Rhodok
  ["rhodok_tribesman", "Rhodok Militia", "Rhodok Militiamen", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac.kingdom_5, [
    itm.coarse_tunic,itm.tunic_with_green_cape,itm.ragged_outfit,
    itm.woolen_hose,itm.blue_hose,
    itm.headcloth,itm.arming_cap,itm.woolen_cap,itm.felt_hat_b,
    itm.scythe,itm.pitch_fork,itm.pickaxe,itm.peasant_knife,itm.butchering_knife,itm.cleaver,itm.club,itm.cudgel,itm.smith_hammer,itm.hatchet,
  ], level(8)|str_12|str_11|agi_6|cha_6, wp_melee(50), knows_shield_1|knows_weapon_master_1, rhodok_face_younger_1, rhodok_face_old_2 ],

  ["rhodok_spearman", "Rhodok Spearman", "Rhodok Spearman", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, no_scene, reserved, fac.kingdom_5, [
    itm.padded_leather,itm.leather_armor,
    itm.hunter_boots,itm.hide_boots,
    itm.mail_gauntlets,
    itm.padded_coif,itm.leather_cap,
    itm.hera_rhodok_pavise_a,
    itm.military_fork,itm.battle_fork,itm.falchion_new,itm.short_cleaver,
  ], level(10)|str_12|agi_12|cha_6|int_6, wp_melee(90), knows_shield_2|knows_ironflesh_2|knows_power_strike_2|knows_weapon_master_2|knows_athletics_3, rhodok_face_young_1, rhodok_face_old_2 ],

  ["rhodok_veteran_spearman", "Rhodok Veteran Spearman", "Rhodok Veteran Spearmen", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_5, [
    itm.mail_shirt,
    itm.splinted_greaves,
    itm.mail_mittens,
    itm.rhodok_infantry_cap,
    itm.hera_rhodok_pavise_a,
    itm.partisan,itm.corseque,itm.bill_guisarme,itm.heavy_falchion,itm.spearman_cleaver,
  ], level(12)|str_15|agi_12|cha_6|int_6, wpex(90,30,140,30,30,30), knows_shield_3|knows_ironflesh_5|knows_power_strike_3|knows_athletics_4|knows_weapon_master_3, rhodok_face_young_1, rhodok_face_older_2 ],

  ["rhodok_adept_spearman", "Rhodok Adept Spearman", "Rhodok Adept Spearmen", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_5, [
    itm.rhodok_cuirass_a1,itm.rhodok_cuirass_a2,
    itm.mail_chausses,itm.mail_boots,
    itm.scale_gauntlets,
    itm.rhodok_army_cap,
    itm.hera_rhodok_pavise_b,
    itm.trident,itm.battle_fork_b,itm.guisarme,itm.spearman_cleaver,itm.short_bill,
  ], level(14)|str_15|agi_14|int_6|cha_6, wpex(100,30,180,30,30,30), knows_shield_4|knows_ironflesh_5|knows_power_strike_4|knows_athletics_4|knows_weapon_master_4, rhodok_face_middle_1, rhodok_face_older_2 ],

  ["rhodok_master_spearman", "Rhodok Master Spearman", "Rhodok Master spearmen", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_5, [
    itm.rhodok_cuirass_b,
    itm.splinted_leather_greaves,itm.iron_greaves,
    itm.lamellar_gauntlets,
    itm.kettle_hat,
    itm.hera_rhodok_pavise_c,
    itm.scorpion_guisarme,itm.fauchard_fork,itm.short_bill,itm.short_voulge,
  ], level(18)|str_18|agi_15|int_6|cha_6, wpex(110,30,220,30,30,30), knows_shield_5|knows_ironflesh_6|knows_power_strike_5|knows_athletics_5|knows_weapon_master_5, rhodok_face_young_1, rhodok_face_old_2 ],

  ["rhodok_swordsman", "Rhodok Swordsman", "Rhodok Swordsmen", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_5, [
    itm.rhodok_brigandine_vest,
    itm.splinted_greaves,
    itm.mail_mittens,
    itm.rhodok_kettle_hat,
    itm.hera_rhodok_pavise_a,
    itm.military_cleaver_b,
  ], level(14)|str_17|agi_12|int_6|cha_6, wpex(150,30,30,30,30,30), knows_ironflesh_3|knows_shield_3|knows_power_strike_3|knows_athletics_4|knows_weapon_master_4, rhodok_face_young_1, rhodok_face_old_2 ],

  ["rhodok_master_swordsman", "Rhodok Master Swordsman", "Rhodok Master Swordsmen", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_5, [
    itm.brigandine_red,itm.brigandine_green,itm.brigandine_blue,
    itm.mail_chausses,itm.mail_boots,
    itm.scale_gauntlets,
    itm.kettle_hat,
    itm.hera_rhodok_pavise_b,
    itm.military_cleaver_c,
  ], level(18)|str_21|agi_12|int_6|cha_6, wpex(180,30,30,30,30,30), knows_ironflesh_4|knows_shield_4|knows_power_strike_4|knows_athletics_4|knows_weapon_master_5, rhodok_face_young_1, rhodok_face_old_2 ],

  ["rhodok_reservist", "Rhodok Reservist", "Rhodok Reservists", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_5, [
    itm.light_leather,itm.leather_armor,
    itm.hunter_boots,itm.hide_boots,
    itm.leather_gloves,
    itm.padded_coif,itm.leather_cap,
    itm.hera_rhodok_pavise_a,
    itm.light_crossbow,itm.rhodok_bolts_a,
    itm.falchion_new,
  ], level(10)|str_12|agi_12|cha_6|int_6, wpex(70,30,30,30,100,30), knows_shield_2|knows_ironflesh_3|knows_power_strike_1|knows_athletics_3, rhodok_face_young_1, rhodok_face_older_2 ],

  ["rhodok_crossbowman", "Rhodok Crossbowman", "Rhodok Crossbowmen", tf_guarantee_all, no_scene, reserved, fac.kingdom_5, [
    itm.rhodok_archer_armor_a1,itm.rhodok_archer_armor_a2,
    itm.light_leather_boots,itm.leather_boots,
    itm.rhodok_infantry_cap,
    itm.hera_rhodok_pavise_a,
    itm.crossbow,itm.rhodok_bolts_a,itm.rhodok_bolts_b,
    itm.falchion_new,itm.short_cleaver,
  ], level(14)|str_14|agi_15|cha_6|int_6, wpex(80,30,30,30,170,30), knows_ironflesh_3|knows_shield_4|knows_power_strike_1|knows_athletics_4|knows_weapon_master_4, rhodok_face_young_1, rhodok_face_older_2 ],

  ["rhodok_veteran_crossbowman", "Rhodok Veteran Crossbowman", "Rhodok Veteran Crossbowmen", tf_guarantee_all, no_scene, reserved, fac.kingdom_5, [
    itm.rhodok_archer_armor_b1,itm.rhodok_archer_armor_b2,
    itm.splinted_greaves,
    itm.rhodok_kettle_hat,
    itm.hera_rhodok_pavise_b,
    itm.heavy_crossbow,itm.rhodok_bolts_a,itm.rhodok_bolts_b,
    itm.short_cleaver,itm.heavy_falchion,
  ], level(16)|str_16|agi_15|int_6|cha_6, wpex(85,30,30,30,220,30), knows_ironflesh_4|knows_shield_5|knows_power_strike_1|knows_athletics_4|knows_weapon_master_5, rhodok_face_middle_1, rhodok_face_older_2 ],

  ["rhodok_sharpshooter", "Rhodok Sharpshooter", "Rhodok Sharpshooters", tf_guarantee_all, no_scene, reserved, fac.kingdom_5, [
    itm.rhodok_archer_armor_c1,itm.rhodok_archer_armor_c2,
    itm.mail_chausses,itm.mail_boots,
    itm.kettle_hat,
    itm.hera_rhodok_pavise_c,
    itm.sniper_crossbow,itm.rhodok_bolts_b,
    itm.heavy_falchion,
  ], level(20)|str_17|agi_18|int_6|cha_6, wpex(90,30,30,30,260,30), knows_ironflesh_5|knows_shield_6|knows_power_strike_2|knows_athletics_4|knows_weapon_master_6, rhodok_face_middle_1, rhodok_face_older_2 ],

  ["rhodok_skirmisher", "Rhodok Skirmisher", "Rhodok Skirmishers", tf_mounted|tf_guarantee_all, no_scene, reserved, fac.kingdom_5, [
    itm.padded_leather,
    itm.mail_mittens,
    itm.hunter_boots,itm.hide_boots,
    itm.rhodok_kettle_hat,
    itm.shield_common_round_d,
    itm.light_crossbow,itm.rhodok_bolts_a,
    itm.military_cleaver_b,
    itm.farm_horse,itm.riding_horse,
  ], level(14)|str_14|agi_15|int_6|cha_6, wpex(95,30,95,30,140,30), knows_shield_1|knows_ironflesh_4|knows_power_strike_3|knows_riding_4|knows_horse_archery_3|knows_weapon_master_4, rhodok_face_younger_1, rhodok_face_old_2 ],

  ["rhodok_scout", "Rhodok Scout", "Rhodok Scouts", tf_mounted|tf_guarantee_all, no_scene, reserved, fac.kingdom_5, [
    itm.studded_leather_coat,
    itm.scale_gauntlets,
    itm.light_leather_boots,itm.leather_boots,
    itm.rhodok_flattop,
    itm.shield_common_round_d,
    itm.skirmisher_crossbow,itm.rhodok_bolts_a,itm.rhodok_bolts_b,
    itm.military_cleaver_b,itm.military_cleaver_c,
    itm.riding_horse,itm.courser_horse,
  ], level(16)|str_16|agi_15|int_6|cha_6, wpex(115,30,115,30,160,30), knows_shield_1|knows_ironflesh_4|knows_power_strike_3|knows_riding_4|knows_horse_archery_4|knows_weapon_master_4, rhodok_face_younger_1, rhodok_face_old_2 ],

  ["rhodok_veteran_scout", "Rhodok Veteran Scout", "Rhodok Veteran Scouts", tf_mounted|tf_guarantee_all, no_scene, reserved, fac.kingdom_5, [
    itm.mail_with_surcoat,itm.surcoat_over_mail,
    itm.splinted_greaves,
    itm.lamellar_gauntlets,
    itm.flat_topped_helmet,
    itm.shield_common_round_a,
    itm.scout_crossbow,itm.rhodok_bolts_b,
    itm.military_cleaver_c,
    itm.courser_horse,itm.armored_courser,
  ], level(20)|str_17|agi_18|int_6|cha_6, wpex(130,30,130,30,180,30), knows_shield_1|knows_ironflesh_5|knows_power_strike_3|knows_riding_5|knows_weapon_master_5|knows_horse_archery_5, rhodok_face_younger_1, rhodok_face_old_2 ],

  ["rhodok_armsman", "Rhodok Armsman", "Rhodok Armsmen", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_5, [
    itm.brigandine_red,itm.brigandine_green,itm.brigandine_blue,
    itm.mail_chausses,itm.mail_boots,
    itm.lamellar_gauntlets,
    itm.rhodok_flattop,
    itm.hera_rhodok_pavise_c,
    itm.poleaxe,itm.battle_cleaver,
  ], level(22)|str_25|agi_12|int_6|cha_6, wpex(90,30,220,30,30,30), knows_power_strike_5|knows_ironflesh_5|knows_shield_5|knows_weapon_master_5|knows_athletics_5, rhodok_face_younger_1, rhodok_face_old_2 ],

  ["rhodok_councilman", "Rhodok Halberdier", "Rhodok Halberdiers", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_5, [
    itm.rhodok_cuirass_c,
    itm.splinted_leather_greaves,itm.iron_greaves,
    itm.lamellar_gauntlets,
    itm.rhodok_open_sallet,
    itm.hera_rhodok_pavise_c,
    itm.halberd_a,itm.battle_cleaver,
  ], level(24)|str_25|agi_12|int_6|cha_6, wpex(100,30,240,30,30,30), knows_ironflesh_6|knows_power_strike_5|knows_weapon_master_6|knows_shield_6|knows_athletics_6, rhodok_face_younger_1, rhodok_face_old_2 ],

  ["rhodok_champion", "Rhodok Champion", "Rhodok Champions", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_5, [
    itm.rhodok_cuirass_d,
    itm.plate_boots,
    itm.lamellar_gauntlets,
    itm.rhodok_open_sallet,
    itm.hera_rhodok_pavise_c,
    itm.halberd_b,itm.battle_cleaver,
  ], level(26)|str_27|agi_12|int_6|cha_6, wpex(120,30,260,30,30,30), knows_ironflesh_7|knows_power_strike_6|knows_shield_6|knows_weapon_master_6|knows_athletics_6, rhodok_face_younger_1, rhodok_face_old_2 ],

  ["rhodok_horseman", "Rhodok Horseman", "Rhodok Horsemen", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_5, [
    itm.rhodok_plated_brig_1,itm.rhodok_plated_brig_2,
    itm.mail_chausses,itm.mail_boots,
    itm.lamellar_gauntlets,
    itm.flat_topped_helmet,
    itm.light_lance,itm.cavalry_lance,itm.military_cleaver_a,
    itm.rhodok_warhorse_a,
  ], level(24)|str_18|agi_21|int_6|cha_6, wpex(30,190,175,30,30,30), knows_ironflesh_5|knows_power_strike_5|knows_riding_5|knows_weapon_master_5|knows_riding_6, rhodok_face_younger_1, rhodok_face_old_2 ],

  ["rhodok_spear_horseman", "Rhodok Spear Horseman", "Rhodok Spear Horsemen", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_5, [
    itm.rhodok_corrazine_a,itm.rhodok_corrazine_b,itm.rhodok_corrazine_c,
    itm.splinted_leather_greaves,itm.iron_greaves,
    itm.lamellar_gauntlets,
    itm.full_helm,
    itm.cavalry_lance,itm.great_lance,itm.military_cleaver_a,
    itm.rhodok_warhorse_b,
  ], level(26)|str_18|agi_21|int_6|cha_6, wpex(30,200,195,30,30,30), knows_ironflesh_6|knows_power_strike_6|knows_riding_7|knows_weapon_master_6|knows_horse_archery_6, rhodok_face_younger_1, rhodok_face_old_2 ],

  ["rhodok_arbalest", "Rhodok Arbalestier", "Rhodok Arbalestiers", tf_guarantee_all, no_scene, reserved, fac.kingdom_5, [
    itm.rhodok_cuirass_d,
    itm.plate_boots,
    itm.plated_gauntlets,
    itm.rhodok_open_sallet,
    itm.hera_rhodok_pavise_c,
    itm.siege_crossbow,itm.rhodok_bolts_c,
    itm.arbalestier_blade,
  ], level(33)|str_21|agi_27|int_6|cha_6, wpex(165,30,30,30,340,30), knows_ironflesh_7|knows_power_strike_3|knows_shield_9|knows_athletics_9|knows_weapon_master_8, rhodok_face_middle_1, rhodok_face_older_2 ],

  ["rhodok_spear_knight", "Rhodok Spear Knight", "Rhodok Spear Knights", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_5, [
    itm.rhodok_cuirass_d,
    itm.plate_boots,
    itm.plated_gauntlets,
    itm.rhodok_visored_sallet,
    itm.shield_common_round_b,
    itm.great_lance,itm.battle_cleaver,
    itm.rhodok_warhorse_c,
  ], level(33)|str_27|agi_21|int_6|cha_6, wpex(225,30,225,30,30,30), knows_shield_4|knows_ironflesh_9|knows_power_strike_9|knows_riding_7|knows_weapon_master_7, rhodok_face_younger_1, rhodok_face_old_2 ],

  ["rhodok_prison_guard","Prison Guard","Prison Guards", tf_guarantee_all_wo_ranged,0,reserved, fac.kingdom_5,[
    itm.brigandine_red,itm.brigandine_green,itm.brigandine_blue,
    itm.splinted_greaves,
    itm.scale_gauntlets,
    itm.kettle_hat,
    itm.hera_rhodok_pavise_b,
    itm.military_cleaver_c,
  ],level(24)|def_attrib,wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,rhodok_face_middle_1,rhodok_face_older_2],

  ["rhodok_castle_guard","Castle Guard","Castle Guards", tf_guarantee_all_wo_ranged,0,reserved, fac.kingdom_5,[
    itm.rhodok_corrazine_a,itm.rhodok_corrazine_b,itm.rhodok_corrazine_c,
    itm.plate_boots,
    itm.gauntlets,
    itm.rhodok_open_sallet,
    itm.hera_rhodok_pavise_c,
    itm.battle_cleaver,
  ],level(24)|def_attrib,wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,rhodok_face_middle_1,rhodok_face_older_2],

  ["rhodok_messenger","Rhodok Messenger","Rhodok Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,reserved, fac.kingdom_5,[],level(25)|def_attrib|agi_21,wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,rhodok_face_middle_1,rhodok_face_older_2],
  ["rhodok_deserter","Rhodok Deserter","Rhodok Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,reserved, fac.kingdom_5,[],level(14)|def_attrib|str_10,wp(80),knows_ironflesh_1|knows_power_draw_1,rhodok_face_middle_1,rhodok_face_older_2],

  #Start Dark Knights

  ["dark_initiate","Dark Initiate","Dark Initiates",tf_guarantee_all_wo_ranged,0,reserved, fac.kingdom_6,[
    itm.dk_armor_a,itm.hera_dk_inf_shield_c,itm.dk_helm_a,itm.wb_dk_plate_boots,itm.dark_gauntlet,
    itm.sword_swadian_f,
  ],level(6)|def_attrib,wp(120),knows_common,swadian_face_younger_1,swadian_face_middle_2],

  ["dark_acolyte","Dark Acolyte","Dark Acolytes",tf_guarantee_all_wo_ranged,0,reserved, fac.kingdom_6,[
    itm.dk_armor_a,itm.hera_dk_inf_shield_c,itm.dk_helm_a,itm.wb_dk_plate_boots,itm.dark_gauntlet,
    itm.sword_swadian_f,
  ],level(12)|def_attrib,wp(150),knows_common,swadian_face_younger_1,swadian_face_middle_2],

  ["dark_page","Dark Page","Dark Pages",tf_mounted|tf_guarantee_all_wo_ranged,0,reserved, fac.kingdom_6,[
    itm.dk_armor_a,itm.hera_dk_cav_shield_c,itm.dk_helm_b,itm.wb_dk_plate_boots,itm.dark_gauntlet,
    itm.cavalry_lance,
    itm.sword_swadian_f,
    itm.dk_warhorse,
  ],level(18)|str_14|agi_12|int_7|cha_7,wp(180),knows_common|knows_ironflesh_4|knows_shield_3|knows_power_strike_4|knows_athletics_4,swadian_face_younger_1,swadian_face_middle_2],

  ["dark_squire","Dark Squire","Dark Squires",tf_mounted|tf_guarantee_all_wo_ranged,0,reserved, fac.kingdom_6,[
    itm.dk_armor_b,itm.hera_dk_cav_shield_c,itm.dk_helm_b,itm.wb_dk_plate_boots,itm.dark_gauntlet,
    itm.cavalry_lance,
    itm.sword_swadian_f,
    itm.dk_warhorse,
  ],level(25)|str_18|agi_15|int_7|cha_8,wp(220),knows_common|knows_ironflesh_6|knows_shield_5|knows_power_strike_5|knows_athletics_5|knows_riding_4|knows_leadership_1,swadian_face_younger_1,swadian_face_middle_2],

  ["dark_knight","Dark Knight","Dark Knights",tf_mounted|tf_guarantee_all_wo_ranged,0,reserved, fac.kingdom_6,[
    itm.dk_armor_b,itm.hera_dk_cav_shield_c,itm.dk_helm_b,itm.wb_dk_plate_boots,itm.dk_gauntlet,
    itm.great_lance,
    itm.sword_swadian_f,
    itm.dk_warhorse,
  ],level(31)|str_23|agi_18|int_10|cha_14,wp(250),knows_common|knows_ironflesh_8|knows_shield_7|knows_power_strike_7|knows_athletics_7|knows_riding_6|knows_leadership_4,swadian_face_younger_1,swadian_face_middle_2],

  ["dark_knight_master","Dark Knight-Master","Dark Knight-Masters",tf_mounted|tf_guarantee_all_wo_ranged,0,reserved, fac.kingdom_6,[
    itm.dk_armor_b,itm.hera_dk_cav_shield_c,itm.dk_helm_b,itm.wb_dk_plate_boots,itm.dk_gauntlet,
    itm.great_lance,
    itm.sword_swadian_f,
    itm.dk_warhorse,
  ],level(36)|str_27|agi_21|int_15|cha_18,wp(300),knows_common|knows_ironflesh_10|knows_shield_9|knows_power_strike_9|knows_athletics_8|knows_riding_8|knows_leadership_7,swadian_face_younger_1,swadian_face_middle_2],

  ["dark_champion","Dark Champion","Dark Champions",tf_mounted|tf_guarantee_all_wo_ranged,0,reserved, fac.kingdom_6,[
    itm.dk_armor_b,itm.hera_dk_cav_shield_c,itm.dk_helm_c,itm.dk_helm_d,itm.wb_dk_plate_boots,itm.dk_gauntlet,
    itm.great_lance,
    itm.sword_swadian_f,
    itm.dk_warhorse,
  ],level(38)|str_30|agi_24|int_18|cha_20,wp(300),knows_common|knows_ironflesh_10|knows_shield_10|knows_power_strike_10|knows_athletics_10|knows_riding_10|knows_leadership_10,swadian_face_younger_1,swadian_face_middle_2],

  ["shadow_knight","Shadow Knight","Shadow Knights",tf_mounted|tf_guarantee_all_wo_ranged,0,reserved, fac.kingdom_6,[
    itm.dk_armor_c,itm.hera_dk_cav_shield_c,itm.dk_helm_c,itm.dk_helm_d,itm.wb_dk_plate_boots,itm.dk_gauntlet,
    itm.great_lance,
    itm.sword_swadian_f,
    itm.dk_warhorse,
  ],level(40)|str_30|agi_28|int_21|cha_24,wp(350),knows_common|knows_ironflesh_10|knows_shield_10|knows_power_strike_10|knows_athletics_10|knows_riding_10|knows_leadership_10,swadian_face_younger_1,swadian_face_middle_2],

  ["unholy_crusader","Unholy Crusader","Unholy Crusaders",tf_mounted|tf_guarantee_all_wo_ranged,0,reserved, fac.kingdom_6,[
    itm.dk_armor_c,itm.hera_dk_cav_shield_c,itm.dk_helm_c,itm.dk_helm_d,itm.wb_dk_plate_boots,itm.dk_gauntlet,
    itm.great_lance,
    itm.sword_swadian_f,
    itm.dk_warhorse,
  ],level(42)|str_30|agi_30|int_26|cha_28,wp(380),knows_common|knows_ironflesh_10|knows_shield_10|knows_power_strike_10|knows_athletics_10|knows_riding_10|knows_leadership_10,swadian_face_younger_1,swadian_face_middle_2],

  ["blackguard","Blackguard","Blackguards",tf_mounted|tf_guarantee_all_wo_ranged,0,reserved, fac.kingdom_6,[
    itm.dk_armor_c,itm.hera_dk_cav_shield_c,itm.dk_helm_c,itm.dk_helm_d,itm.wb_dk_plate_boots,itm.dk_gauntlet,
    itm.great_lance,
    itm.sword_swadian_f,
    itm.dk_charger,
  ],level(45)|str_30|agi_30|int_30|cha_30,wp(410),knows_common|knows_ironflesh_10|knows_shield_10|knows_power_strike_10|knows_athletics_10|knows_riding_10|knows_leadership_10,swadian_face_younger_1,swadian_face_middle_2],

  ["champion_blackguard","Champion Blackguard","Champion Blackguards",tf_mounted|tf_guarantee_all_wo_ranged,0,reserved, fac.kingdom_6,[
    itm.dk_armor_c,itm.hera_dk_cav_shield_c,itm.dk_helm_c,itm.dk_helm_d,itm.wb_dk_plate_boots,itm.dk_gauntlet,
    itm.great_lance,
    itm.sword_swadian_f,
    itm.dk_charger,
  ],level(48)|str_30|agi_30|int_30|cha_30,wp(440),knows_common|knows_ironflesh_10|knows_shield_10|knows_power_strike_10|knows_athletics_10|knows_riding_10|knows_leadership_10,swadian_face_younger_1,swadian_face_middle_2],

  ["blackguard_lord","Lord Blackguard","Lord Blackguards",tf_mounted|tf_guarantee_all_wo_ranged,0,reserved, fac.kingdom_6,[
    itm.dk_armor_lord,itm.hera_dk_cav_shield_c,itm.dk_helm_lord_a,itm.dk_helm_lord_b,itm.wb_dk_plate_boots,itm.dk_gauntlet,
    itm.great_lance,
    itm.sword_swadian_f,
    itm.dk_charger,
  ],level(51)|str_30|agi_30|int_30|cha_30,wp(480),knows_common|knows_ironflesh_10|knows_shield_10|knows_power_strike_10|knows_athletics_10|knows_riding_10,swadian_face_younger_1,swadian_face_middle_2],

  ["dark_skirmisher","Dark Skirmisher","Dark Skirmishers",tf_guarantee_all,0,reserved, fac.kingdom_6,[
    itm.dk_armor_a,itm.hera_dk_inf_shield_c,itm.dk_helm_a,itm.wb_dk_plate_boots,itm.dark_gauntlet,
    itm.long_bow,itm.piercing_arrows,itm.barbed_arrows,
    itm.sword_swadian_f,
  ],level(14)|str_16|agi_9|int_5|cha_7,wp(160),knows_common|knows_power_draw_5,swadian_face_younger_1,swadian_face_middle_2],

  ["dark_archer","Dark Archer","Dark Archers",tf_guarantee_all,0,reserved, fac.kingdom_6,[
    itm.dk_armor_a,itm.hera_dk_inf_shield_c,itm.dk_helm_a,itm.wb_dk_plate_boots,itm.dark_gauntlet,
    itm.long_bow,itm.piercing_arrows,itm.barbed_arrows,itm.bodkin_arrows,
    itm.sword_swadian_f,
  ],level(21)|str_21|agi_12|int_8|cha_12,wp(190),knows_common|knows_power_draw_7|knows_ironflesh_6|knows_power_strike_4,swadian_face_younger_1,swadian_face_middle_2],

  ["dark_marksman","Dark Marksman","Dark Marksmen",tf_guarantee_all,0,reserved, fac.kingdom_6,[
    itm.dk_armor_a,itm.hera_dk_inf_shield_c,itm.dk_helm_a,itm.wb_dk_plate_boots,itm.dark_gauntlet,
    itm.long_bow,itm.barbed_arrows,itm.bodkin_arrows,
    itm.sword_swadian_f,
  ],level(29)|str_27|agi_16|int_12|cha_16,wp(210),knows_common|knows_power_draw_9|knows_ironflesh_8|knows_power_strike_6,swadian_face_younger_1,swadian_face_middle_2],

  ["dark_sharpshooter","Dark Sharpshooter","Dark Sharpshooters",tf_guarantee_all,0,reserved, fac.kingdom_6,[
    itm.dk_armor_a,itm.hera_dk_inf_shield_c,itm.dk_helm_b,itm.wb_dk_plate_boots,itm.dark_gauntlet,
    itm.war_bow,itm.barbed_arrows,itm.bodkin_arrows,
    itm.sword_swadian_f,
  ],level(34)|str_30|agi_24|int_18|cha_21,wp(240),knows_common|knows_power_draw_10|knows_ironflesh_10|knows_power_strike_9,swadian_face_younger_1,swadian_face_middle_2],

  ["dark_ranger","Dark Ranger","Dark Rangers",tf_guarantee_all,0,reserved, fac.kingdom_6,[
    itm.dk_armor_b,itm.hera_dk_inf_shield_c,itm.dk_helm_b,itm.wb_dk_plate_boots,itm.dark_gauntlet,
    itm.war_bow,itm.barbed_arrows,itm.bodkin_arrows,
    itm.sword_swadian_f,
  ],level(40)|str_30|agi_16|int_12|cha_16,wp(210),knows_common|knows_power_draw_10|knows_ironflesh_10|knows_power_strike_10,swadian_face_younger_1,swadian_face_middle_2],


  #Begin Sarranid
  ["sarranid_recruit", "Sarranid Paighan", "Sarranid Paighani", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac.kingdom_6, [
    itm.sarranid_cloth_robe,itm.sarranid_cloth_robe_b,itm.sarranid_cloth_robe_c,itm.sarranid_cloth_robe_d,itm.sarranid_cloth_robe_e,
    itm.sarranid_boots_a,
    itm.turban,itm.desert_turban,
    itm.staff,itm.peasant_knife,itm.cleaver,itm.wooden_stick,itm.club,itm.cudgel,itm.hatchet,itm.sickle,
  ], level(6)|str_12|agi_11|cha_6|int_6, wpex(60,30,60,30,30,30), knows_ironflesh_2|knows_power_strike_2|knows_athletics_2|knows_weapon_master_2, sarranid_face_younger_1, sarranid_face_middle_2 ],

  ["sarranid_seyman", "Sarranid Seyman", "Sarranid Seymen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac.kingdom_6, [
    itm.skirmisher_armor,
    itm.sarranid_boots_a,
    itm.sarranid_felt_hat,
    itm.hera_sarranid_large_shield_a,
    itm.boar_spear,itm.spear,itm.war_spear,itm.spiked_club,
  ], level(10)|str_13|agi_12|cha_6|int_6, wpex(90,30,90,30,30,30), knows_ironflesh_2|knows_shield_2|knows_power_strike_1|knows_weapon_master_2, sarranid_face_young_1, sarranid_face_old_2 ],

  ["sarranid_janissary", "Sarranid Janissary", "Sarranid Janissaries", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_6, [
    itm.sarranid_leather_armor,
    itm.sarranid_boots_b,
    itm.leather_gloves,
    itm.sarranid_spiked_helmet,
    itm.hera_sarranid_large_shield_b,
    itm.ashwood_pike,itm.pike,itm.scimitar,
  ], level(14)|str_16|agi_13|cha_6|int_6, wpex(120,30,105,30,30,30), knows_shield_3|knows_ironflesh_3|knows_power_strike_4|knows_athletics_3|knows_weapon_master_4, sarranid_face_middle_1, sarranid_face_older_2 ],

  ["sarranid_dervish", "Sarranid Dervish", "Sarranid Dervishes", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_6, [
    itm.sarranid_chain,
    itm.sarranid_boots_d,
    itm.mail_mittens,
    itm.sarranid_mail_helmet,
    itm.hera_sarranid_large_shield_c,
    itm.infantry_pike,itm.bamboo_spear,itm.scimitar_b,
  ], level(16)|str_18|agi_13|int_6|cha_6, wpex(140,30,125,30,30,30), knows_shield_3|knows_ironflesh_4|knows_power_strike_5|knows_athletics_3|knows_weapon_master_4, sarranid_face_middle_1, sarranid_face_older_2 ],

  ["sarranid_dailamite", "Sarranid Dailamite", "Sarranid Dailamites", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_6, [
    itm.sarranid_cavalry_robe,itm.sarranid_cavalry_robe_b,itm.sarranid_cavalry_robe_c,itm.sarranid_warrior_mail_b,
    itm.sarranid_boots_c,
    itm.scale_gauntlets,
    itm.sarranid_warrior_helm,
    itm.hera_sarranid_large_shield_d,
    itm.sarranid_pike,itm.sarranid_long_pike,itm.scimitar_c,
  ], level(20)|str_21|agi_14|int_6|cha_6, wpex(160,30,165,30,30,30), knows_shield_4|knows_ironflesh_5|knows_power_strike_7|knows_athletics_3|knows_weapon_master_5, sarranid_face_middle_1, sarranid_face_older_2 ],

  ["sarranid_timariot", "Sarranid Timariot", "Sarranid Timariot", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_6, [
    itm.sarranid_chain,
    itm.sarranid_boots_b,
    itm.mail_gauntlets,
    itm.sarranid_mail_helmet,
    itm.hera_sarranid_small_shield_a,
    itm.light_lance,itm.scimitar,
    itm.sarranid_horse_a,itm.sarranid_horse_b,
  ], level(14)|str_15|agi_14|int_6|cha_6, wpex(100,30,120,30,30,30), knows_riding_3|knows_ironflesh_3|knows_athletics_2|knows_power_strike_3|knows_weapon_master_3|knows_shield_3, sarranid_face_young_1, sarranid_face_middle_2 ],

  ["sarranid_mamluke", "Sarranid Mamluke", "Sarranid Mamlukes", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_6, [
    itm.sarranid_cavalry_robe,itm.sarranid_cavalry_robe_b,itm.sarranid_cavalry_robe_c,
    itm.sarranid_boots_d,
    itm.scale_gauntlets,
    itm.sarranid_warrior_helm,
    itm.hera_sarranid_small_shield_b,
    itm.light_lance,itm.sarranid_lance_a,itm.scimitar_b,
    itm.sarranid_warhorse_a,
  ], level(16)|str_16|agi_15|int_6|cha_6, wpex(110,30,140,30,30,30), knows_riding_4|knows_shield_4|knows_ironflesh_3|knows_power_strike_3|knows_weapon_master_3|knows_athletics_2, sarranid_face_middle_1, sarranid_face_older_2 ],

  ["sarranid_cataphract", "Sarranid Cataphract", "Sarranid Cataphracti", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_6, [
    itm.sarranid_elite_armor,
    itm.sarranid_boots_c,
    itm.lamellar_gauntlets,
    itm.sarranid_full_keffiyeh,
    itm.hera_sarranid_small_shield_c,
    itm.sarranid_lance_a,itm.sarranid_lance_b,itm.scimitar_c,
    itm.sarranid_warhorse_b,
  ], level(20)|str_18|agi_17|int_6|cha_6, wpex(130,30,160,30,30,30), knows_riding_5|knows_ironflesh_5|knows_shield_4|knows_power_strike_3|knows_weapon_master_4|knows_athletics_2, sarranid_face_young_1, sarranid_face_old_2 ],

  ["sarranid_azap", "Sarranid Azap", "Sarranid Azapi", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_6, [
    itm.sarranid_vest_a,itm.sarranid_vest_b,
    itm.sarranid_boots_a,
    itm.sarranid_felt_hat,
    itm.hera_sarranid_large_shield_a,
    itm.throwing_knives,itm.throwing_daggers,itm.darts,itm.war_darts,itm.hunting_bow_sar,itm.arrows,itm.broadhead_arrows,
    itm.knobbed_mace,itm.flanged_mace,itm.spiked_mace,
  ], level(10)|str_12|agi_13|int_6|cha_6, wpex(80,30,30,60,30,60), knows_athletics_2|knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_2, sarranid_face_young_1, sarranid_face_old_2 ],

  ["sarranid_kamandaran", "Sarranid Kamandaran", "Sarranid Kamandarai", tf_guarantee_all, no_scene, reserved, fac.kingdom_6, [
    itm.archers_vest,itm.archers_vest_b,itm.archers_vest_c,itm.archers_vest_d,
    itm.sarranid_boots_b,
    itm.sarranid_helmet1,
    itm.hera_sarranid_large_shield_b,
    itm.short_bow_sar,itm.arrows,itm.broadhead_arrows,itm.piercing_arrows,
    itm.winged_mace_b,
  ], level(14)|str_12|agi_17|cha_6|int_6, wpex(105,30,30,140,30,30), knows_shield_1|knows_power_draw_4|knows_ironflesh_2|knows_athletics_4|knows_power_strike_1|knows_weapon_master_3, sarranid_face_young_1, sarranid_face_old_2 ],

  ["sarranid_kamandaran_serden", "Sarranid Kamandaran Serden", "Sarranid Kamandaran Serden", tf_guarantee_all, no_scene, reserved, fac.kingdom_6, [
    itm.sarranid_leather_vest,
    itm.sarranid_boots_b,
    itm.sarranid_warrior_cap,
    itm.hera_sarranid_large_shield_c,
    itm.nomad_bow_sar,itm.broadhead_arrows,itm.piercing_arrows,itm.sarranid_arrows,
    itm.sarranid_mace,
  ], level(18)|str_15|agi_18|int_6|cha_6, wpex(125,30,30,180,30,30), knows_shield_2|knows_power_draw_5|knows_ironflesh_4|knows_athletics_6|knows_power_strike_2|knows_weapon_master_4, sarranid_face_middle_1, sarranid_face_older_2 ],

  ["sarranid_akinci", "Sarranid Akinci", "Sarranid Akinci", tf_mounted|tf_guarantee_all, no_scene, reserved, fac.kingdom_6, [
    itm.sarranid_leather_armor,
    itm.sarranid_boots_a,
    itm.leather_gloves,
    itm.sarranid_helmet1,
    itm.hera_sarranid_small_shield_a,
    itm.darts,itm.war_darts,
    itm.scimitar,
    itm.sarranid_horse_a,itm.sarranid_horse_b,
  ], level(12)|str_12|agi_15|int_6|cha_6, wpex(70,30,30,30,30,120), knows_shield_2|knows_horse_archery_3|knows_ironflesh_2|knows_power_strike_1|knows_power_throw_3|knows_weapon_master_3|knows_athletics_2|knows_riding_2, sarranid_face_young_1, sarranid_face_old_2 ],

  ["sarranid_akinci_deliler", "Sarranid Akinci Deliler", "Sarranid Akinci Deliler", tf_mounted|tf_guarantee_all, no_scene, reserved, fac.kingdom_6, [
    itm.sarranid_chain,
    itm.sarranid_boots_b,
    itm.mail_gauntlets,
    itm.sarranid_warrior_cap,
    itm.hera_sarranid_small_shield_b,
    itm.javelin_sar,
    itm.scimitar_b,
    itm.sarranid_horse_a,itm.sarranid_horse_b,itm.sarranid_camel_a,itm.sarranid_camel_b,
  ], level(14)|str_14|agi_15|int_6|cha_6, wpex(90,30,30,30,30,140), knows_horse_archery_4|knows_riding_3|knows_ironflesh_2|knows_shield_3|knows_power_strike_2|knows_power_throw_4|knows_weapon_master_3, sarranid_face_young_1, sarranid_face_old_2 ],

  ["sarranid_akinci_serden", "Sarranid Akinci Serden", "Sarranid Akinci Serden", tf_mounted|tf_guarantee_all, no_scene, reserved, fac.kingdom_6, [
    itm.sarranid_cavalry_robe,itm.sarranid_cavalry_robe_b,itm.sarranid_cavalry_robe_c,itm.sarranid_warrior_mail_b,
    itm.sarranid_boots_d,
    itm.mail_mittens,
    itm.sarranid_mail_coif,
    itm.hera_sarranid_small_shield_c,
    itm.jarid_sar,
    itm.scimitar_c,
    itm.sarranid_camel_a,itm.sarranid_camel_b,
  ], level(18)|str_15|agi_18|int_6|cha_6, wpex(110,30,30,30,30,180), knows_horse_archery_5|knows_riding_5|knows_shield_4|knows_ironflesh_2|knows_power_strike_1|knows_power_throw_5|knows_weapon_master_4|knows_athletics_2, sarranid_face_middle_1, sarranid_face_older_2 ],

  ["sarranid_eunuch", "Sarranid Eunuch", "Sarranid Eunuchs", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_6, [
    itm.sarranid_eunuch_armor_a,itm.sarranid_eunuch_armor_b,
    itm.sarranid_boots_d,
    itm.scale_gauntlets,
    itm.sarranid_horseman_helmet,
    itm.hera_sarranid_large_shield_d,
    itm.bec_de_corbin_a,itm.arabian_sword_d,
  ], level(22)|str_22|agi_15|int_6|cha_6, wpex(140,30,180,30,30,30), knows_ironflesh_6|knows_power_strike_8|knows_weapon_master_5|knows_athletics_3|knows_shield_4, sarranid_face_young_1, sarranid_face_old_2 ],

  ["sarranid_ghazi", "Sarranid Ghazi", "Sarranid Ghazi", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_6, [
    itm.khergit_elite_armor,
    itm.sarranid_boots_c,
    itm.lamellar_gauntlets,
    itm.sarranid_warrior_helm,
    itm.hera_sarranid_large_shield_e,
    itm.polehammer_a,itm.arabian_sword_a,
  ], level(24)|str_24|agi_15|int_6|cha_6, wpex(150,30,200,30,30,30), knows_shield_5|knows_ironflesh_7|knows_power_strike_8|knows_athletics_4|knows_weapon_master_5, sarranid_face_middle_1, sarranid_face_older_2 ],

  ["sarranid_spahbod", "Sarranid Spahbod", "Sarranid Spahbod", tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_6, [
    itm.vaegir_elite_armor,
    itm.sarranid_boots_c,
    itm.gauntlets,
    itm.sarranid_full_keffiyeh,
    itm.hera_sarranid_large_shield_e,
    itm.polehammer_b,itm.arabian_sword_b,
  ], level(26)|str_24|agi_15|cha_6|int_8, wpex(165,30,220,30,30,30), knows_ironflesh_8|knows_shield_6|knows_athletics_5|knows_power_strike_8|knows_weapon_master_5, sarranid_face_middle_1, sarranid_face_old_2 ],

  ["sarranid_siphai", "Sarranid Siphai", "Sarranid Siphai", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_6, [
    itm.sarranid_mamluke_a,itm.sarranid_mamluke_b,
    itm.sarranid_boots_c,
    itm.lamellar_gauntlets,
    itm.sarranid_warrior_helm,
    itm.hera_sarranid_small_shield_c,
    itm.sarranid_lance_b,itm.arabian_sword_a,
    itm.sarranid_warhorse_a,
  ], level(24)|str_21|agi_18|int_6|cha_6, wpex(140,30,180,30,30,30), knows_riding_6|knows_shield_4|knows_ironflesh_6|knows_power_strike_4|knows_weapon_master_5|knows_athletics_2, sarranid_face_middle_1, sarranid_face_older_2 ],

  ["sarranid_bey", "Sarranid Bey", "Sarranid Bey", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_6, [
    itm.mamluke_mail,
    itm.sarranid_boots_c,
    itm.gauntlets,
    itm.sarranid_full_keffiyeh,
    itm.hera_sarranid_small_shield_c,
    itm.sarranid_lance_c,itm.arabian_sword_b,
    itm.sarranid_warhorse_b,
  ], level(26)|str_21|agi_20|cha_6|int_6, wpex(170,30,230,30,30,30), knows_riding_6|knows_ironflesh_6|knows_shield_5|knows_athletics_2|knows_power_strike_5|knows_weapon_master_5, sarranid_face_middle_1, sarranid_face_old_2 ],

  ["sarranid_spahbod_serden", "Sarranid Spahbod Serden", "Sarranid Spahbod Serden", tf_guarantee_all, no_scene, reserved, fac.kingdom_6, [
    itm.mamluke_mail,
    itm.sarranid_boots_c,
    itm.gauntlets,
    itm.sarranid_veiled_helmet,
    itm.hera_sarranid_large_shield_d,
    itm.strong_bow_sar,itm.sarranid_arrows,itm.barbed_arrows,itm.bodkin_arrows,
    itm.arabian_sword_c,
  ], level(33)|str_30|agi_18|cha_6|int_8, wpex(180,30,30,260,30,30), knows_power_draw_7|knows_ironflesh_10|knows_shield_6|knows_athletics_6|knows_power_strike_10|knows_weapon_master_6, sarranid_face_middle_1, sarranid_face_old_2 ],

  ["sarranid_zhayedan", "Sarranid Zhayedan", "Sarranid Zhayedan", tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac.kingdom_6, [
    itm.mamluke_mail,
    itm.sarranid_boots_c,
    itm.gauntlets,
    itm.sarranid_veiled_helmet,
    itm.hera_sarranid_small_shield_c,
    itm.sarranid_lance_c,itm.sarranid_warblade,
    itm.sarranid_warhorse_c,
  ], level(33)|str_27|agi_21|int_6|cha_6, wpex(195,30,260,30,30,30), knows_riding_7|knows_ironflesh_9|knows_shield_6|knows_power_strike_6|knows_weapon_master_6|knows_athletics_2, sarranid_face_young_1, sarranid_face_old_2 ],

  ["sarranid_prison_guard","Prison Guard","Prison Guards",tf_guarantee_all_wo_ranged,0,reserved, fac.kingdom_6,[
    itm.sarranid_cavalry_robe,itm.sarranid_cavalry_robe_b,itm.sarranid_cavalry_robe_c,
    itm.sarranid_boots_d,
    itm.mail_gauntlets,
    itm.sarranid_mail_helmet,
    itm.hera_sarranid_large_shield_d,
    itm.scimitar_c,
  ],level(25)|def_attrib,wp_melee(135)|wp_throwing(100),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,sarranid_face_middle_1,sarranid_face_older_2],

  ["sarranid_castle_guard","Kapikulu","Kapikullari",tf_guarantee_all_wo_ranged,0,reserved, fac.kingdom_6,[
    itm.khergit_elite_armor,
    itm.sarranid_boots_c,
    itm.lamellar_gauntlets,
    itm.sarranid_veiled_helmet,
    itm.hera_sarranid_large_shield_e,
    itm.sarranid_warblade,
  ],level(25)|def_attrib,wp_melee(135)|wp_throwing(100),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,sarranid_face_middle_1,sarranid_face_older_2],

  ["sarranid_messenger","Sarranid Messenger","Sarranid Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,reserved, fac.kingdom_6,[],level(20)|def_attrib,wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,sarranid_face_young_1,sarranid_face_old_2],
  ["sarranid_deserter","Sarranid Deserter","Sarranid Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,reserved, fac.kingdom_6,[],level(20)|def_attrib,wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,sarranid_face_young_1,sarranid_face_old_2],

  ["regular_soldiers_end", "{!}", "{!}endmarker", tf_hero|tf_inactive, 0, 0, fac.no_faction, [], 0, 0, knows_inventory_management_10, 0],

  # OUTLAWS

  # Quest and miscellaneous outlaws
  ["looter","Looter","Looters",0,0,0,fac.outlaws,[
    itm.rawhide_coat,itm.nomad_armor,itm.nomad_armor,itm.nomad_boots,itm.wrapping_boots,itm.woolen_cap,
    itm.shield_common_round_d,
    itm.falchion_new,itm.hammer,itm.dagger,itm.butchering_knife,itm.cleaver,itm.club,itm.hatchet,
  ],level(4)|def_attrib,wp(20),knows_common,bandit_face1,bandit_face2],

  ["brigand", "Brigand", "Brigands", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac.outlaws, [
    itm.rawhide_coat,itm.leather_jerkin,itm.nomad_armor,itm.nomad_boots,itm.wrapping_boots,itm.leather_cap,
    itm.shield_common_round_d,
    itm.spear,itm.cudgel,itm.knobbed_mace,itm.flanged_mace,itm.spiked_mace,itm.spiked_club,itm.falchion_new,itm.sword_medieval_c_small,itm.sword_norman,itm.sword_medieval_d,
    itm.farm_horse,
  ], level(10)|def_attrib, wp(65), knows_common|knows_power_draw_1, bandit_face1, bandit_face2 ],

  ["tough","Town Tough","Town Toughs",0,0,0,fac.outlaws,[
    itm.rawhide_coat,itm.nomad_armor,itm.nomad_armor,itm.nomad_boots,itm.wrapping_boots,itm.woolen_cap,
    itm.club,itm.spiked_club,
  ],level(2)|def_attrib,wp(20),knows_common,bandit_face1,bandit_face2],

  ["tough2","Town Tough","Town Toughs",tf_guarantee_armor|tf_guarantee_boots,0,0,fac.outlaws,[
    itm.broken_bottle,itm.maul,
  ],level(7)|str_14|agi_8|int_4|cha_4,wp(50),knows_common|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2,bandit_face1,bandit_face2],

  ["scholar","Scholar","Scholars",tf_guarantee_armor,0,0,fac.neutral,[
    itm.pilgrim_disguise,itm.nomad_boots,
    itm.staff,itm.cudgel,
    itm.donkey_a,itm.donkey_b,itm.mule,
  ],level(10)|def_attrib,wp(65),knows_common|knows_power_draw_3|knows_pathfinding_4|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2,scholar_face_1,scholar_face_11],

  ["wedding_guest","Wedding Guest","Wedding Guests",tf_guarantee_armor|tf_guarantee_boots,0,0,fac.commoners,[
    itm.tabard,itm.rich_outfit,itm.gambeson,itm.blue_gambeson,itm.red_gambeson,itm.blue_hose,itm.woolen_hose,itm.ankle_boots,itm.leather_boots,
    itm.winged_mace,itm.knobbed_mace,itm.flanged_mace,itm.spiked_mace,itm.spiked_club,
  ],level(10)|str_14|agi_6|int_4|cha_4,wp(140),knows_common|knows_ironflesh_5|knows_power_strike_6|knows_power_draw_4|knows_shield_2|knows_athletics_3,man_face_younger_1,man_face_older_2],

  ["cheese_rustler","Cheese Rustler","Cheese Rustlers",tf_guarantee_armor,0,0,fac.outlaws,[
    itm.gambeson,itm.blue_gambeson,itm.red_gambeson,itm.blue_hose,itm.woolen_hose,itm.ankle_boots,
    itm.shield_common_round_d,
    itm.spear,itm.war_spear,itm.sword_norman,itm.sword_medieval_d,itm.sword_medieval_c,
    itm.farm_horse,itm.riding_horse,
  ],level(10)|def_attrib,wp(65),knows_common|knows_power_draw_3|knows_pathfinding_4|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2,bandit_face1,bandit_face2],

  ["cheese_rustler2","Cheese Rustler","Cheese Rustlers",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac.kingdom_1,[
    itm.plate_armor,
    itm.plate_boots,
    itm.plated_gauntlets,
    itm.winged_great_helmet,
    itm.hera_swadian_inf_shield_c,
    itm.paladin_lance_1,itm.paladin_lance_2,itm.two_handed_battle_axe_g,itm.sword_swadian_g,
    itm.swadian_charger_b,
  ],level(29)|str_30|agi_12|int_18|cha_10,wp_melee(300),knows_common|knows_riding_6|knows_shield_7|knows_ironflesh_7|knows_power_strike_10|knows_weapon_master_10,swadian_face_middle_1,swadian_face_older_2],

  # Assassin attacks
  ["assassin",       "Murderer",         "Murderers",         0,0,0,fac.outlaws,[
    itm.rawhide_coat,itm.nomad_armor,itm.nomad_armor,itm.nomad_boots,itm.wrapping_boots,itm.woolen_cap,
    itm.throwing_knives,
    itm.khergit_sword_b,
  ],level(4)|def_attrib,wp(20),knows_common,bandit_face1,bandit_face2],

  ["assassin1",      "Novice Assassin",  "Novice Assassins",  tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac.outlaws,[
    itm.ssin_low_armour,itm.assassin_boots,itm.leather_gloves,itm.assassin_hood,
    itm.throwing_knives,
    itm.khergit_sword_b,
  ],level(12)|def_attrib,wp_melee(160)|wp_throwing(180),knows_ironflesh_6|knows_power_strike_4|knows_power_throw_4|knows_athletics_6|knows_weapon_master_4,bandit_face1,bandit_face2],

  ["assassin2",      "Prefect Assassin", "Prefect Assassins", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac.outlaws,[
    itm.ssin_med_armour,itm.assassin_boots,itm.leather_gloves,itm.assassin_hood,
    itm.throwing_knives,itm.throwing_daggers,
    itm.khergit_sword_b,
  ],level(16)|def_attrib,wp_melee(200)|wp_throwing(240),knows_ironflesh_6|knows_power_strike_6|knows_power_throw_6|knows_athletics_8|knows_weapon_master_6,bandit_face1,bandit_face2],

  ["assassin_royal", "Royal Assassin",   "Royal Assassins",   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac.outlaws,[
    itm.ssin_high_armour,itm.assassin_boots,itm.leather_gloves,itm.assassin_hood,
    itm.throwing_daggers,
    itm.khergit_sword_b,
  ],level(20)|def_attrib,wp_melee(240)|wp_throwing(260),knows_ironflesh_8|knows_power_strike_8|knows_power_throw_8|knows_athletics_10|knows_weapon_master_8,bandit_face1,bandit_face2],

  # Regular bandits
  ["robber",     "Robber",         "Robbers",         0, no_scene, reserved, fac.outlaws, [], level(1)|def_attrib, wp(20), knows_common, rhodok_face_young_1, rhodok_face_old_2],
  ["highwayman", "Highwayman",     "Highwaymen",      0, no_scene, reserved, fac.outlaws, [], level(1)|def_attrib, wp(20), knows_common, rhodok_face_young_1, rhodok_face_old_2],
  ["bandit",     "Highway Robber", "Highway Robbers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse, no_scene, reserved, fac.outlaws, [
    itm.leather_jerkin,itm.nomad_boots,itm.leather_cap,
    itm.shield_common_round_d,
    itm.shortened_spear,itm.boar_spear,itm.spear,itm.war_spear,itm.falchion_new,itm.heavy_falchion,itm.scimitar,itm.spiked_club,
    itm.riding_horse,itm.khergit_horse,itm.sarranid_horse_a,itm.sarranid_horse_b,
  ],level(16)|def_attrib,wp(90),knows_common|knows_power_draw_3, rhodok_face_young_1, rhodok_face_old_2],

  ["berber",         "Berber Tribesman", "Berber Tribesmen", 0, no_scene, reserved, fac.outlaws, [], level(1)|def_attrib, wp(20), knows_common, sarranid_face_young_1,sarranid_face_old_2],
  ["berber_warrior", "Berber Warrior",   "Berber Warriors",  0, no_scene, reserved, fac.outlaws, [], level(1)|def_attrib, wp(20), knows_common, sarranid_face_young_1,sarranid_face_old_2],
  ["desert_bandit",  "Desert Bandit",    "Desert Bandits",   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted,0,0,fac.outlaws,[
    itm.sarranid_cloth_robe,itm.sarranid_cloth_robe,itm.skirmisher_armor,itm.khergit_leather_boots,itm.sarranid_boots_b,itm.desert_turban,itm.turban,itm.leather_steppe_cap_b,
    itm.shield_common_heater_b,
    itm.war_spear,itm.ashwood_pike,itm.pike,itm.scimitar,itm.scimitar_b,
    itm.heavy_camel_a,itm.heavy_camel_b,
  ],level(12)|def_attrib,wp(100),knows_riding_4|knows_horse_archery_3|knows_power_draw_3,sarranid_face_young_1,sarranid_face_old_2],

  ["nomad_marauder", "Nomad Marauder", "Nomad Marauders", 0, no_scene, reserved, fac.outlaws, [], level(1)|def_attrib, wp(20), knows_common, khergit_face_young_1,khergit_face_old_2],
  ["steppe_bandit",  "Steppe Bandit",  "Steppe Bandits",  tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_mounted,0,0,fac.outlaws,[
    itm.khergit_armor,itm.nomad_armor,itm.steppe_armor,itm.leather_vest,itm.hide_boots,itm.nomad_boots,itm.leather_steppe_cap_a,itm.leather_steppe_cap_b,itm.steppe_cap,
    itm.shield_common_round_a,
    itm.light_lance,itm.khergit_lance_a,itm.hafted_blade_b,itm.khergit_sword_b,itm.khergit_sword_a,
    itm.tribal_horse_a,itm.tribal_horse_b,
  ],level(22)|str_16|agi_10|int_4|cha_4,wp(100),knows_ironflesh_3|knows_power_strike_3|knows_power_draw_4|knows_riding_4|knows_horse_archery_3,khergit_face_young_1,khergit_face_old_2],
  ["steppe_raider",  "Steppe Raider",  "Steppe Raiders",  tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_mounted,0,0,fac.outlaws,[
    itm.khergit_armor,itm.steppe_armor,itm.nomad_vest,itm.nomad_robe,itm.leather_boots,itm.nomad_boots,itm.hide_boots,itm.hunter_boots,itm.leather_steppe_cap_a,itm.leather_steppe_cap_b,itm.steppe_cap,
    itm.shield_common_round_a,
    itm.light_lance,itm.khergit_lance_a,itm.hafted_blade_b,itm.khergit_sword_b,itm.khergit_sword_a,
    itm.tribal_horse_a,itm.tribal_horse_b,
  ],level(24)|str_20|agi_15|int_4|cha_4,wp(140),knows_ironflesh_5|knows_power_strike_5|knows_power_draw_5|knows_power_throw_3|knows_shield_2|knows_athletics_1|knows_riding_5|knows_horse_archery_3,khergit_face_young_1,khergit_face_old_2],

  ["highlander",       "Highlander",       "Highlanders",       0, no_scene, reserved, fac.outlaws, [], level(1)|def_attrib, wp(20), knows_common, vaegir_face_young_1, vaegir_face_old_2],
  ["highlander_rebel", "Highlander Rebel", "Highlander Rebels", 0, no_scene, reserved, fac.outlaws, [], level(1)|def_attrib, wp(20), knows_common, vaegir_face_young_1, vaegir_face_old_2],
  ["mountain_bandit",  "Mountain Bandit",  "Mountain Bandits",  tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac.outlaws, [
    itm.khergit_armor,itm.nomad_armor,itm.rawhide_coat,itm.nomad_vest,itm.hide_boots,itm.nomad_boots,itm.skullcap,itm.felt_hat,itm.head_wrappings,
    itm.shield_common_round_a,itm.shield_common_round_d,
    itm.spear,itm.ashwood_pike,itm.light_lance,itm.military_fork,itm.battle_fork,itm.sword_norman,itm.sword_medieval_d,itm.sword_medieval_c,itm.sword_medieval_c_long,itm.falchion_new,itm.heavy_falchion,itm.military_cleaver_b,
    itm.mountain_horse,
  ], level(22)|str_18|agi_10|int_4|cha_4, wp(150), knows_common|knows_power_draw_3|knows_power_strike_5|knows_ironflesh_5|knows_shield_4|knows_riding_4|knows_power_draw_2|knows_horse_archery_2, vaegir_face_young_1, vaegir_face_old_2 ],

  ["poacher",          "Poacher",          "Poachers",          0, no_scene, reserved, fac.outlaws, [], level(1)|def_attrib, wp(20), knows_common, bandit_face1, bandit_face2],
  ["seasoned_poacher", "Seasoned Poacher", "Seasoned Poachers", 0, no_scene, reserved, fac.outlaws, [], level(1)|def_attrib, wp(20), knows_common, bandit_face1, bandit_face2],
  ["forest_bandit",    "Forest Bandit",    "Forest Bandits",    tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac.outlaws, [
    itm.padded_leather,itm.leather_jerkin,itm.ragged_outfit,itm.hide_boots,itm.leather_boots,itm.common_hood,itm.black_hood,
    #itm.hunting_bow,itm.short_bow,itm.long_bow,itm.arrows,itm.broadhead_arrows,itm.piercing_arrows,
    itm.shortened_military_scythe,itm.voulge_a,itm.military_sickle,
  ], level(22)|str_18|agi_10|int_4|cha_4, wp(140), knows_common|knows_ironflesh_5|knows_power_strike_6|knows_power_draw_4|knows_shield_2|knows_athletics_3|knows_power_draw_2, nord_face_young_1, nord_face_old_2 ],

  ["smuggler",     "Smuggler",     "Smugglers",     0, no_scene, reserved, fac.outlaws, [], level(1)|def_attrib, wp(20), knows_common, bandit_face1, bandit_face2],
  ["convict",      "Convict",      "Convicts",      0, no_scene, reserved, fac.outlaws, [], level(1)|def_attrib, wp(20), knows_common, bandit_face1, bandit_face2],
  ["taiga_bandit", "Taiga Bandit", "Taiga Bandits", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac.outlaws,[
    itm.nomad_armor,itm.leather_jerkin,itm.hide_boots,itm.nomad_boots,itm.vaegir_fur_cap,itm.steppe_cap,
    itm.shield_common_round_c,itm.shield_common_kite_e,
    itm.darts,itm.war_darts,itm.javelin,
    itm.bardiche_a,itm.khergit_sword_b,itm.sword_medieval_b_small,itm.sword_viking_a_small,itm.sword_viking_b_small,
  ],level(15)|def_attrib,wp(110),knows_common|knows_power_draw_4|knows_power_throw_3,vaegir_face_young_1,vaegir_face_old_2],

  # Outside threats
  ["sea_raider_young", "Sea Raider Young",   "Sea Raider Youngs",   0, no_scene, reserved, fac.outlaws, [], level(1)|def_attrib, wp(20), knows_common, bandit_face1, bandit_face2],
  ["sea_raider",       "Sea Raider",         "Sea Raiders",         tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac.outlaws,[
    itm.raider_hauberk_a,itm.raider_hauberk_b,itm.raider_hauberk_c,itm.nordic_archer_armor_b,itm.nordic_archer_armor_c1,itm.nordic_archer_armor_c2,itm.nordic_archer_armor_d,itm.byrnie,itm.leather_jacket,itm.pelt_coat,itm.rawhide_coat,itm.leather_vest,itm.leather_jerkin,
    itm.leather_boots,itm.nomad_boots,itm.nordic_helmet_b,itm.nordic_helmet,itm.nordic_helmet_b,itm.nasal_helmet,
    itm.norman_shield_2,itm.norman_shield_4,itm.norman_shield_8,
    itm.light_throwing_axes,itm.throwing_axes,
    itm.sword_medieval_b,
  ],level(18)|def_attrib,wp(120),knows_ironflesh_5|knows_power_strike_2|knows_power_draw_3|knows_power_throw_2|knows_riding_1|knows_athletics_2,nord_face_young_1,nord_face_old_2],
  ["sea_raider_vet",   "Veteran Sea Raider", "Veteran Sea Raiders", 0, no_scene, reserved, fac.outlaws, [
    itm.norman_shield_1,itm.norman_shield_3,itm.norman_shield_5,itm.norman_shield_6,itm.norman_shield_7,
  ], level(1)|def_attrib, wp(20), knows_common, bandit_face1, bandit_face2],

  # bandits_end marker
  ["black_khergit_horseman","{!}","{!}",0,0,0,fac.outlaws,[],level(1)|def_attrib,wp(20),knows_common,khergit_face_young_1,khergit_face_old_2],


  # MANHUNTERS

  #Begin Manhunter Troops
  ["manhunter", "Manhunter Wannabe", "Manhunter Wannabe", tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.manhunters, [
    itm.woolen_cap,itm.rawhide_coat,itm.coarse_tunic,itm.nomad_boots,itm.wrapping_boots,
    itm.club,itm.cudgel,itm.staff,
    itm.mule,itm.farm_horse,
  ], ATTR(14,12,7,7,10), wpex(50,50,50,50,50,50), SKILLS(power_strike=1, weapon_master=1, shield=1, athletics=3, riding=1, tracking=1, spotting=2, leadership=2, ), man_face_younger_1, man_face_older_2],
  ["manhunter_t2", "Manhunter", "Manhunter", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, 0, 0, fac.manhunters, [
    itm.padded_coif,itm.fur_hat,itm.nomad_cap_b,itm.leather_steppe_cap_a,itm.leather_cap,itm.sarranid_boots_a,itm.nomad_boots,itm.hunter_boots,itm.leather_gloves,itm.leather_jacket,itm.pelt_coat,itm.rawhide_coat,
    itm.shield_common_kite_c,
    itm.cudgel,itm.hammer,itm.winged_mace,itm.knobbed_mace,itm.flanged_mace,itm.spiked_mace,
    itm.riding_horse,itm.khergit_horse,
  ], ATTR(15,13,7,8,13), wpex(80,80,80,80,80,80), SKILLS(ironflesh=1, power_strike=2, weapon_master=2, shield=1, athletics=5, riding=2, tracking=2, spotting=2, ), man_face_younger_1, man_face_older_2],
  ["manhunter_t3", "Veteran Manhunter", "Veteran Manhunter", tf_mounted|tf_guarantee_all_wo_ranged, 0, 0, fac.manhunters, [
    itm.nomad_cap_b,itm.leather_cap,itm.skullcap,itm.hunter_boots,itm.hide_boots,itm.light_leather_boots,itm.hide_boots,itm.light_leather_boots,itm.leather_boots,itm.leather_gloves,itm.leather_jacket,itm.leather_vest,itm.padded_cloth,itm.aketon_green,itm.leather_jerkin,
    itm.shield_common_kite_c,
    itm.winged_mace,itm.knobbed_mace,itm.flanged_mace,itm.spiked_mace,
    itm.khergit_horse,itm.courser_horse,
  ], ATTR(16,14,8,8,16), wpex(110,110,110,110,110,110), SKILLS(ironflesh=1, power_strike=3, weapon_master=3, shield=2, athletics=4, riding=3, tracking=3, spotting=3, leadership=1, ), man_face_younger_1, man_face_older_2],
  ["manhunter_t4", "Manhunter Captain", "Manhunter Captain", tf_mounted|tf_guarantee_all_wo_ranged, 0, 0, fac.manhunters, [
    itm.manhunter_helmet,itm.light_leather_boots,itm.leather_boots,itm.leather_gloves,itm.mail_gauntlets,itm.padded_cloth,itm.aketon_green,
    itm.shield_common_kite_c,
    itm.tourney_lance,
    itm.winged_mace,itm.knobbed_mace,itm.flanged_mace,itm.spiked_mace,
    itm.courser_horse,itm.hunter_horse,itm.armored_courser,itm.armored_hunter,
  ], ATTR(17,15,8,9,19), wpex(135,135,135,135,135,135), SKILLS(ironflesh=2, power_strike=4, weapon_master=4, shield=2, athletics=3, riding=4, tracking=4, spotting=3, leadership=3, ), man_face_younger_1, man_face_older_2],
  ["manhunter_t5", "Bounty Hunter", "Bounty Hunter", tf_mounted|tf_guarantee_all_wo_ranged, 0, 0, fac.manhunters, [
    itm.manhunter_helmet,itm.splinted_greaves,itm.leather_gloves,itm.mail_gauntlets,itm.mail_mittens,itm.scale_gauntlets,itm.light_leather,itm.leather_armor,itm.padded_leather,
    itm.shield_common_kite_c,
    itm.tourney_lance,
    itm.winged_mace,itm.knobbed_mace,itm.flanged_mace,itm.spiked_mace,
    itm.armored_courser,itm.armored_hunter,
  ], ATTR(18,15,8,12,23), wpex(160,160,160,160,160,160), SKILLS(ironflesh=2, power_strike=5, weapon_master=5, shield=3, athletics=2, riding=5, tracking=5, spotting=4, leadership=4, ), man_face_younger_1, man_face_older_2],

  #["refugee","Refugee","Refugees",tf_female|tf_guarantee_armor,0,0,fac.commoners,[itm.knife,itm.pitch_fork,itm.sickle,itm.hatchet,itm.club,itm.dress,itm.robe,itm.woolen_dress,itm.headcloth,itm.common_hood,itm.wrapping_boots],level(1)|def_attrib,wp(45),knows_common,refugee_face1,refugee_face2],
  ["caravan_master","Caravan Master","Caravan Masters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac.commoners,[
    itm.lamellar_vest,itm.leather_boots,itm.leather_gloves,itm.rhodok_kettle_hat,
    itm.shield_common_round_a,itm.shield_common_round_d,itm.shield_common_kite_a,itm.shield_common_kite_b,itm.mercenary_shield_a,
    itm.spear,itm.sword_medieval_c,
    itm.courser_horse,itm.riding_horse,itm.riding_horse,
  ],level(15)|def_attrib,wp(150),knows_common|knows_riding_4|knows_ironflesh_6,mercenary_face_1,mercenary_face_2],

  ["kidnapped_girl","Kidnapped Girl","Kidnapped Girls",tf_hero|tf_female|tf_randomize_face|tf_unmoveable_in_party_window,0,reserved,fac.commoners,[
    itm.dress,itm.leather_boots,itm.peasant_knife,
  ],level(2)|def_attrib,wp(50),knows_common|knows_riding_2,woman_face_1,woman_face_2],


  ["soldiers_end", "{!}", "{!}endmarker", tf_hero|tf_inactive, 0, 0, fac.no_faction, [], 0, 0, knows_inventory_management_10, 0],



  #This troop is the troop marked as soldiers_end and town_walkers_begin
  #["town_walker_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac.commoners,[itm.red_shirt,itm.linen_tunic,itm.fur_coat,itm.coarse_tunic,itm.tabard,itm.leather_vest,itm.arena_tunic_white,itm.leather_apron,itm.arena_tunic_green,itm.arena_tunic_blue,itm.woolen_hose,itm.nomad_boots,itm.blue_hose,itm.hide_boots,itm.ankle_boots,itm.leather_boots,itm.fur_hat,itm.leather_cap,itm.straw_hat,itm.felt_hat],level(4)|def_attrib,wp(60),knows_common,man_face_young_1,man_face_old_2],
  #["town_walker_2","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac.commoners,[itm.blue_dress,itm.dress,itm.woolen_dress,itm.peasant_dress,itm.woolen_hose,itm.blue_hose,itm.wimple_a,itm.wimple_with_veil,itm.female_hood],level(2)|def_attrib,wp(40),knows_common,woman_face_1,woman_face_2],
  #["khergit_townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac.commoners,[itm.sarranid_felt_hat,itm.turban,itm.wrapping_boots,itm.khergit_leather_boots,itm.sarranid_cloth_robe,itm.sarranid_cloth_robe_b,itm.sarranid_cloth_robe_c,itm.sarranid_cloth_robe_d,itm.sarranid_cloth_robe_e],level(4)|def_attrib,wp(60),knows_common,swadian_face_younger_1,swadian_face_middle_2],
  #["khergit_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac.commoners,[itm.blue_dress,itm.dress,itm.woolen_dress,itm.peasant_dress,itm.woolen_hose,itm.blue_hose,itm.wimple_a,itm.wimple_with_veil,itm.female_hood],level(2)|def_attrib,wp(40),knows_common,woman_face_1,woman_face_2],
  #["sarranid_townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac.commoners,[itm.sarranid_felt_hat,itm.turban,itm.wrapping_boots,itm.sarranid_boots_a,itm.sarranid_cloth_robe,itm.sarranid_cloth_robe_b,itm.sarranid_cloth_robe_c,itm.sarranid_cloth_robe_d,itm.sarranid_cloth_robe_e],level(4)|def_attrib,wp(60),knows_common,swadian_face_younger_1,swadian_face_middle_2],
  #["sarranid_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac.commoners,[itm.sarranid_common_dress,itm.sarranid_common_dress_b,itm.woolen_hose,itm.sarranid_boots_a,itm.sarranid_felt_head_cloth,itm.sarranid_felt_head_cloth_b],level(2)|def_attrib,wp(40),knows_common,woman_face_1,woman_face_2],
  ##This troop is the troop marked as town_walkers_end and village_walkers_begin
  #["village_walker_1","Villager","Villagers",tf_guarantee_boots|tf_guarantee_armor,0,0,fac.commoners,[itm.red_shirt,itm.linen_tunic,itm.coarse_tunic,itm.leather_vest,itm.leather_apron,itm.woolen_hose,itm.nomad_boots,itm.blue_hose,itm.hide_boots,itm.ankle_boots,itm.leather_boots,itm.fur_hat,itm.leather_cap,itm.straw_hat,itm.felt_hat],level(4)|def_attrib,wp(60),knows_common,man_face_younger_1,man_face_older_2],
  #["village_walker_2","Villager","Villagers",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac.commoners,[itm.blue_dress,itm.dress,itm.woolen_dress,itm.peasant_dress,itm.woolen_hose,itm.blue_hose,itm.wimple_a,itm.wimple_with_veil,itm.female_hood],level(2)|def_attrib,wp(40),knows_common,woman_face_1,woman_face_2],
  #This troop is the troop marked as village_walkers_end and spy_walkers_begin
  # Ryan END

  ["town_walker_swa_m", "Townsman", "Townsmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, 0, 0, fac.kingdom_1, [
    itm.common_hood,itm.common_hood_b,itm.woolen_cap,itm.woolen_cap_b,itm.headcloth,itm.leather_cap,itm.padded_coif,
    itm.wrapping_boots,itm.ankle_boots,
    itm.linen_tunic,itm.red_tunic,itm.green_tunic,itm.blue_tunic,itm.white_tunic,itm.yellow_tunic,itm.coarse_tunic,itm.leather_apron,itm.tabard,itm.tunic_with_green_cape,itm.ragged_outfit,itm.gambeson,itm.blue_gambeson,itm.red_gambeson,
  ], level(1)|def_attrib, wp(60), knows_common, swadian_face_younger_1, swadian_face_old_2],
  ["town_walker_swa_f", "Townswoman", "Townswomen", tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, 0, 0, fac.kingdom_2, [
    itm.wimple_a,itm.wimple_with_veil,
    itm.woolen_hose,itm.blue_hose,
    itm.dress,itm.peasant_dress,itm.woolen_dress,
  ], level(1)|def_attrib, wp(40), knows_common, woman_face_1, woman_face_2],

  ["town_walker_vae_m", "Townsman", "Townsmen", tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.kingdom_1, [
    itm.fur_hat,
    itm.nomad_boots,itm.hunter_boots,itm.hide_boots,
    itm.fur_coat,itm.linen_tunic,itm.coarse_tunic,itm.leather_apron,itm.tunic_with_green_cape,itm.ragged_outfit,itm.leather_jacket,itm.pelt_coat,itm.rawhide_coat,itm.leather_vest,itm.leather_jerkin,
  ], level(1)|def_attrib, wp(60), knows_common, vaegir_face_younger_1, vaegir_face_old_2],
  ["town_walker_vae_f", "Townswoman", "Townswomen", tf_female|tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.kingdom_2, [
    itm.headcloth,
    itm.woolen_hose,itm.blue_hose,
    itm.dress,itm.peasant_dress,itm.woolen_dress,
  ], level(1)|def_attrib, wp(40), knows_common, woman_face_1, woman_face_2],

  ["town_walker_khe_m", "Townsman", "Townsmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, 0, 0, fac.kingdom_1, [
    itm.fur_hat,itm.nomad_cap_b,itm.leather_steppe_cap_a,
    itm.nomad_boots,itm.hunter_boots,itm.hide_boots,
    itm.pelt_coat,itm.rawhide_coat,itm.nomad_vest,itm.nomad_robe,itm.leather_vest,itm.leather_jerkin,itm.tribal_warrior_outfit,itm.khergit_leather_a,itm.khergit_leather_b,
  ], level(1)|def_attrib, wp(60), knows_common, khergit_face_younger_1, khergit_face_old_2],
  ["town_walker_khe_f", "Townswoman", "Townswomen", tf_female|tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.kingdom_2, [
    itm.nomad_boots,itm.hunter_boots,itm.hide_boots,
    itm.nomad_vest,itm.nomad_robe,itm.tribal_warrior_outfit,itm.khergit_leather_a,itm.khergit_leather_b,
  ], level(1)|def_attrib, wp(40), knows_common, woman_face_1, woman_face_2],

  ["town_walker_nor_m", "Townsman", "Townsmen",             tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.kingdom_1, [
    itm.leather_cap,itm.felt_hat,itm.headcloth,itm.fur_hat,
    itm.nomad_boots,itm.hunter_boots,itm.hide_boots,
    itm.nordic_shirt_01,itm.nordic_shirt_02,itm.nordic_shirt_03,itm.nordic_shirt_04,itm.nordic_shirt_05,itm.nordic_shirt_06,
  ], level(1)|def_attrib, wp(60), knows_common, nord_face_younger_1, nord_face_old_2],
  ["town_walker_nor_f", "Townswoman", "Townswomen", tf_female|tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.kingdom_2, [
    itm.wimple_a,itm.wimple_with_veil,itm.headcloth,
    itm.nomad_boots,itm.hunter_boots,itm.hide_boots,
    itm.dress,itm.peasant_dress,itm.woolen_dress,
  ], level(1)|def_attrib, wp(40), knows_common, woman_face_1, woman_face_2],

  ["town_walker_rho_m", "Townsman", "Townsmen", tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.kingdom_1, [
    itm.common_hood,itm.common_hood_b,itm.felt_hat,itm.felt_hat_b,itm.headcloth,
    itm.woolen_hose,itm.blue_hose,
    itm.linen_tunic,itm.red_shirt,itm.coarse_tunic,itm.ragged_outfit,
  ], level(1)|def_attrib, wp(60), knows_common, rhodok_face_younger_1, rhodok_face_old_2],
  ["town_walker_rho_f", "Townswoman", "Townswomen", tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, 0, 0, fac.kingdom_2, [
    itm.wimple_a,itm.wimple_with_veil,itm.headcloth,
    itm.woolen_hose,itm.blue_hose,
    itm.dress,itm.peasant_dress,itm.woolen_dress,itm.blue_dress,
  ], level(1)|def_attrib, wp(40), knows_common, woman_face_1, woman_face_2],

  ["town_walker_sar_m", "Townsman", "Townsmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, 0, 0, fac.kingdom_1, [
    itm.turban,itm.desert_turban,
    itm.sarranid_boots_a,
    itm.sarranid_cloth_robe,itm.sarranid_cloth_robe_b,itm.sarranid_cloth_robe_c,itm.sarranid_cloth_robe_d,itm.sarranid_cloth_robe_e,itm.sarranid_vest_a,itm.sarranid_vest_b,
  ], level(1)|def_attrib, wp(60), knows_common, sarranid_face_younger_1, sarranid_face_old_2],
  ["town_walker_sar_f", "Townswoman", "Townswomen", tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, 0, 0, fac.kingdom_2, [
    itm.sarranid_felt_head_cloth,itm.sarranid_felt_head_cloth_b,
    itm.sarranid_boots_a,
    itm.sarranid_common_dress,itm.sarranid_common_dress_b,
  ], level(1)|def_attrib, wp(40), knows_common, woman_face_1, woman_face_2],


  ["village_walker_swa_m", "Serf", "Serfs", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, 0, 0, fac.kingdom_1, [
    itm.straw_hat,itm.common_hood,itm.common_hood_b,itm.head_wrappings,itm.headcloth,itm.woolen_cap,itm.woolen_cap_b,
    itm.wrapping_boots,itm.ankle_boots,
    itm.linen_tunic,itm.leather_apron,itm.tunic_with_green_cape,itm.ragged_outfit,
  ], level(1)|def_attrib, wp(60), knows_common, swadian_face_young_1, swadian_face_older_2],
  ["village_walker_swa_f", "Serf's Wife", "Serf's Wife", tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, 0, 0, fac.kingdom_1, [
    itm.head_wrappings,itm.headcloth,itm.arming_cap,
    itm.wrapping_boots,itm.ankle_boots,
    itm.dress,itm.peasant_dress,itm.woolen_dress,
  ], level(1)|def_attrib, wp(40), knows_common, woman_face_1, woman_face_2],

  ["village_walker_vae_m", "Kholop", "Kholopi", tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.kingdom_2, [
    itm.straw_hat,
    itm.nomad_boots,itm.hunter_boots,itm.hide_boots,
    itm.linen_tunic,itm.red_tunic,itm.green_tunic,itm.blue_tunic,itm.white_tunic,itm.yellow_tunic,itm.leather_apron,itm.ragged_outfit,itm.leather_jacket,itm.pelt_coat,itm.rawhide_coat,
  ], level(1)|def_attrib, wp(60), knows_common, vaegir_face_young_1, vaegir_face_older_2],
  ["village_walker_vae_f", "Kholopka", "Kholopki", tf_female|tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.kingdom_2, [
    itm.head_wrappings,itm.headcloth,
    itm.wrapping_boots,itm.ankle_boots,
    itm.dress,itm.peasant_dress,itm.woolen_dress,
  ], level(1)|def_attrib, wp(40), knows_common, woman_face_1, woman_face_2],

  ["village_walker_khe_m", "Tribesman", "Tribesmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, 0, 0, fac.kingdom_3, [
    itm.fur_hat,itm.nomad_cap_b,itm.leather_steppe_cap_a,
    itm.nomad_boots,itm.hunter_boots,itm.hide_boots,
    itm.nomad_vest,itm.leather_jerkin,itm.tribal_warrior_outfit,
  ], level(1)|def_attrib, wp(60), knows_common, khergit_face_young_1, khergit_face_older_2],
  ["village_walker_khe_f", "Tribeswoman", "Tribeswomen", tf_female|tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.kingdom_3, [
    itm.wrapping_boots,itm.ankle_boots,
    itm.nomad_vest,itm.nomad_robe,itm.khergit_leather_a,itm.khergit_leather_b,
  ], level(1)|def_attrib, wp(40), knows_common, woman_face_1, woman_face_2],

  ["village_walker_nor_m", "Freeman", "Freemen", tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.kingdom_4, [
    itm.leather_cap,itm.felt_hat,itm.headcloth,itm.fur_hat,
    itm.nomad_boots,itm.hunter_boots,itm.hide_boots,
    itm.nordic_shirt_01,itm.nordic_shirt_02,itm.nordic_shirt_03,itm.nordic_shirt_04,itm.nordic_shirt_05,itm.nordic_shirt_06,
  ], level(1)|def_attrib, wp(60), knows_common, nord_face_young_1, nord_face_older_2],
  ["village_walker_nor_f", "Freewoman", "Freewomen", tf_female|tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.kingdom_4, [
    itm.head_wrappings,itm.headcloth,
    itm.wrapping_boots,itm.ankle_boots,
    itm.dress,itm.peasant_dress,itm.woolen_dress,
  ], level(1)|def_attrib, wp(40), knows_common, woman_face_1, woman_face_2],

  ["village_walker_rho_m", "Farmer", "Farmers", tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.kingdom_5, [
    itm.woolen_cap,itm.woolen_cap_b,itm.straw_hat,
    itm.wrapping_boots,itm.ankle_boots,
    itm.linen_tunic,itm.red_tunic,itm.green_tunic,itm.blue_tunic,itm.white_tunic,itm.yellow_tunic,itm.leather_apron,itm.tunic_with_green_cape,itm.ragged_outfit,
  ], level(1)|def_attrib, wp(60), knows_common, rhodok_face_young_1, rhodok_face_older_2],
  ["village_walker_rho_f", "Farmer's Wife", "Farmer's Wife", tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, 0, 0, fac.kingdom_5, [
    itm.head_wrappings,itm.headcloth,itm.arming_cap,
    itm.wrapping_boots,itm.ankle_boots,
    itm.dress,itm.peasant_dress,itm.woolen_dress,
  ], level(1)|def_attrib, wp(40), knows_common, woman_face_1, woman_face_2],

  ["village_walker_sar_m", "Peasant", "Peasants", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, 0, 0, fac.kingdom_6, [
    itm.turban,itm.desert_turban,
    itm.sarranid_boots_a,
    itm.sarranid_cloth_robe,itm.sarranid_cloth_robe_b,itm.sarranid_cloth_robe_c,itm.sarranid_cloth_robe_d,itm.sarranid_cloth_robe_e,
  ], level(1)|def_attrib, wp(60), knows_common, sarranid_face_young_1, sarranid_face_older_2],
  ["village_walker_sar_f", "Peasant Woman", "Peasant Women", tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, 0, 0, fac.kingdom_6, [
    itm.sarranid_felt_head_cloth,itm.sarranid_felt_head_cloth_b,
    itm.sarranid_boots_a,
    itm.sarranid_common_dress,itm.sarranid_common_dress_b,
  ], level(1)|def_attrib, wp(40), knows_common, woman_face_1, woman_face_2],


  ["spy_walker_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac.commoners,[
    itm.red_shirt,itm.linen_tunic,itm.coarse_tunic,itm.tabard,itm.leather_vest,itm.leather_apron,itm.woolen_hose,itm.nomad_boots,itm.blue_hose,itm.hide_boots,itm.ankle_boots,itm.leather_boots,itm.fur_hat,itm.leather_cap,itm.straw_hat,itm.felt_hat
  ],level(4)|def_attrib,wp(60),knows_common,man_face_middle_1,man_face_old_2],
  ["spy_walker_2","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac.commoners,[
    itm.blue_dress,itm.dress,itm.woolen_dress,itm.peasant_dress,itm.woolen_hose,itm.blue_hose,itm.wimple_a,itm.wimple_with_veil,itm.female_hood
  ],level(2)|def_attrib,wp(40),knows_common,woman_face_1,woman_face_2],



  #This troop is the troop marked as spy_walkers_end
  # Zendar
  #["tournament_master","Tournament Master","Tournament Master",tf_hero, scn.zendar_center|entry(1),reserved,  fac.commoners,[itm.nomad_armor,itm.nomad_boots],level(2)|def_attrib,wp(20),knows_common,0x000000000008414401e28f534c8a2d09],
  #["trainer","Trainer","Trainer",tf_hero, scn.zendar_center|entry(2),reserved,  fac.commoners,[itm.leather_jerkin,itm.hide_boots],level(2)|def_attrib,wp(20),knows_common,0x00000000000430c701ea98836781647f],
  #["Constable_Hareck","Constable Hareck","Constable Hareck",tf_hero, scn.zendar_center|entry(5),reserved,  fac.commoners,[itm.leather_jacket,itm.hide_boots],level(5)|def_attrib,wp(20),knows_common,0x00000000000c41c001fb15234eb6dd3f],

  # Ryan BEGIN
  ["Ramun_the_slave_trader","Ramun, the slave trader","Ramun, the slave trader",tf_hero, no_scene,reserved, fac.slavers,[itm.leather_jacket,itm.hide_boots],level(5)|def_attrib,wp(20),knows_common,0x0000000fd5105592385281c55b8e44eb00000000001d9b220000000000000000],

  ["guide","Quick Jimmy","Quick Jimmy",tf_hero, no_scene,0,  fac.commoners,[itm.coarse_tunic,itm.hide_boots],level(2)|def_attrib,wp(20),knows_inventory_management_10, 0x00000000000c318301f24e38a36e38e3],
  # Ryan END

  ["Xerina",  "Ymira",   "Ymira",   tf_hero|tf_female, no_scene, reserved, fac.commoners, [itm.leather_jerkin,itm.hide_boots], level(39)|def_attrib|str_15|agi_15, wp(312), knows_power_strike_5|knows_ironflesh_5|knows_riding_6|knows_power_draw_4|knows_athletics_8|knows_shield_3, 0x00000001ac0820074920561d0b51e6ed00000000001d40ed0000000000000000],
  ["Dranton", "Dranton", "Dranton", tf_hero,           no_scene, reserved, fac.commoners, [itm.leather_vest,itm.hide_boots],   level(42)|def_attrib|str_15|agi_14, wp(324), knows_power_strike_5|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4|knows_shield_3, 0x0000000a460c3002470c50f3502879f800000000001ce0a00000000000000000],
  ["Kradus",  "Kradus",  "Kradus",  tf_hero,           no_scene, reserved, fac.commoners, [itm.padded_leather,itm.hide_boots], level(43)|def_attrib|str_15|agi_14, wp(270), knows_power_strike_5|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4|knows_shield_3, 0x0000000f5b1052c61ce1a9521db1375200000000001ed31b0000000000000000],


  #Sargoth
  #halkard, hardawk. lord_taucard lord_caupard. lord_paugard

  #Salt mine
  ["Galeas","Galeas","Galeas",tf_hero, 0, reserved, fac.commoners,[itm.leather_jacket,itm.hide_boots],level(5)|def_attrib,wp(20),knows_common,0x000000000004718201c073191a9bb10c],

  #Dhorak keep

  ["farmer_from_bandit_village", "Farmer", "Farmers", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac.commoners, [itm.linen_tunic,itm.coarse_tunic,itm.nomad_boots,itm.wrapping_boots,itm.farm_horse], level(6)|def_attrib, wp(60), knows_common, man_face_middle_1, man_face_older_2 ],

  ["trainer_1","Trainer","Trainer",tf_hero, scn.training_ground_ranged_melee_1|entry(6),reserved,  fac.commoners,[itm.leather_jerkin,itm.hide_boots],level(2)|def_attrib,wp(20),knows_common,0x0000000d0d1030c74ae8d661b651c6840000000000000e220000000000000000],
  ["trainer_2","Trainer","Trainer",tf_hero, scn.training_ground_ranged_melee_2|entry(6),reserved,  fac.commoners,[itm.nomad_vest,itm.hide_boots],level(2)|def_attrib,wp(20),knows_common,0x0000000e5a04360428ec253846640b5d0000000000000ee80000000000000000],
  ["trainer_3","Trainer","Trainer",tf_hero, scn.training_ground_ranged_melee_3|entry(6),reserved,  fac.commoners,[itm.padded_leather,itm.hide_boots],level(2)|def_attrib,wp(20),knows_common,0x0000000e4a0445822ca1a11ab1e9eaea0000000000000f510000000000000000],
  ["trainer_4","Trainer","Trainer",tf_hero, scn.training_ground_ranged_melee_4|entry(6),reserved,  fac.commoners,[itm.leather_jerkin,itm.hide_boots],level(2)|def_attrib,wp(20),knows_common,0x0000000e600452c32ef8e5bb92cf1c970000000000000fc20000000000000000],
  ["trainer_5","Trainer","Trainer",tf_hero, scn.training_ground_ranged_melee_5|entry(6),reserved,  fac.commoners,[itm.leather_vest,itm.hide_boots],level(2)|def_attrib,wp(20),knows_common,0x0000000e77082000150049a34c42ec960000000000000e080000000000000000],

  # Ransom brokers.
  ["ransom_broker_1","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.leather_vest,itm.hide_boots],level(5)|def_attrib,wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_2","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.tabard,itm.hide_boots],level(5)|def_attrib,wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_3","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.leather_vest,itm.hide_boots],level(5)|def_attrib,wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_4","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.red_shirt,itm.hide_boots],level(5)|def_attrib,wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_5","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.gambeson,itm.hide_boots],level(5)|def_attrib,wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_6","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.blue_gambeson,itm.hide_boots],level(5)|def_attrib,wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_7","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.red_gambeson,itm.hide_boots],level(5)|def_attrib,wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_8","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.fur_coat,itm.hide_boots],level(5)|def_attrib,wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_9","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.leather_vest,itm.hide_boots],level(5)|def_attrib,wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_10","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.leather_jacket,itm.hide_boots],level(5)|def_attrib,wp(20),knows_common,merchant_face_1,merchant_face_2],

  # Tavern traveler.
  ["tavern_traveler_1","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.fur_coat,itm.hide_boots],level(5)|def_attrib,wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_2","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.tabard,itm.hide_boots],level(5)|def_attrib,wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_3","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.leather_vest,itm.hide_boots],level(5)|def_attrib,wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_4","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.blue_gambeson,itm.hide_boots],level(5)|def_attrib,wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_5","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.red_shirt,itm.hide_boots],level(5)|def_attrib,wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_6","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.fur_coat,itm.hide_boots],level(5)|def_attrib,wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_7","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.leather_jacket,itm.hide_boots],level(5)|def_attrib,wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_8","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.tabard,itm.hide_boots],level(5)|def_attrib,wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_9","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.fur_coat,itm.hide_boots],level(5)|def_attrib,wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_10","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.leather_jacket,itm.hide_boots],level(5)|def_attrib,wp(20),knows_common,merchant_face_1,merchant_face_2],

  # Tavern traveler.
  ["tavern_bookseller_1","Book_Merchant","Book_Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac.commoners,[itm.fur_coat,itm.hide_boots,itm.book_tactics,itm.book_persuasion,itm.book_wound_treatment_reference,itm.book_leadership,itm.book_intelligence,itm.book_training_reference,itm.book_surgery_reference],level(5)|def_attrib,wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_bookseller_2","Book_Merchant","Book_Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac.commoners,[itm.fur_coat,itm.hide_boots,itm.book_wound_treatment_reference,itm.book_leadership,itm.book_intelligence,itm.book_trade,itm.book_engineering,itm.book_weapon_mastery],level(5)|def_attrib,wp(20),knows_common,merchant_face_1,merchant_face_2],



  # Tavern minstrel.
  ["tavern_minstrel_1","Wandering Minstrel","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac.commoners,[itm.leather_jacket,itm.hide_boots,itm.lute],level(5)|def_attrib,wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_minstrel_2","Wandering Bard","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac.commoners,[itm.tunic_with_green_cape,itm.hide_boots,itm.lyre],level(5)|def_attrib,wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_minstrel_3","Wandering Ashik","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac.commoners,[itm.nomad_robe,itm.hide_boots,itm.lute],level(5)|def_attrib,wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_minstrel_4","Wandering Skald","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac.commoners,[itm.fur_coat,itm.hide_boots,itm.lyre],level(5)|def_attrib,wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_minstrel_5","Wandering Troubadour","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac.commoners,[itm.red_shirt,itm.hide_boots,itm.lute],level(5)|def_attrib,wp(20),knows_common,merchant_face_1,merchant_face_2],

  # Tavern minstrel.
  ["tavern_minstrel_0","Minstrel","Minstrel",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac.commoners,[itm.leather_jacket,itm.hide_boots,itm.mandolin],level(5)|str_9|agi_9|int_12|cha_7,wp(90),knows_warrior_npc|knows_riding_2|knows_horse_archery_3|knows_power_draw_3|knows_leadership_2|knows_weapon_master_1,merchant_face_2],

  #NPC system changes begin
  #Companions
  ["kingdom_heroes_including_player_begin", "kingdom_heroes_including_player_begin", "kingdom_heroes_including_player_begin", tf_hero, 0, reserved, fac.kingdom_1, [], lord_attrib, wp(220), knows_lord_1, 0x000000000010918a01f248377289467d],

  # NPC MODIFICATIONS BY LAV:

  # Horse thief
  ["npc1","Kana","Kana",                    tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac.commoners,[
    itm.nomad_boots,itm.leather_gloves,itm.nomad_vest,
    itm.throwing_knives,itm.club,
    (itm.riding_horse, imod.spirited),
  ], ATTR(9,13,15,7,3),wpex(60,40,30,40,40,60),SKILLS(power_strike=1,weapon_master=1,athletics=1,riding=4,horse_archery=1,looting=1,tracking=2,pathfinding=4,spotting=1,inventory_management=2,first_aid=2,trade=2),0x00000004bf086143259d061a9046e23500000000001db52c0000000000000000],

  # Unlucky merchant
  ["npc2","Tismanu","Tismanu",              tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac.commoners,[
    itm.straw_hat,itm.ankle_boots,itm.blue_tunic,
    itm.falchion,
  ], level(1)|str_8|agi_9|int_11|cha_14,wpex(40,30,30,30,40,30),knows_ironflesh_2|knows_weapon_master_1|knows_athletics_1|knows_riding_3|knows_trainer_1|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_3|knows_wound_treatment_1|knows_engineer_1|knows_trade_4,0x000000019d004001570b893712c8d28d00000000001dc8990000000000000000],

  # Megamerc doctor
  ["npc3","Xerina","Xerina",      tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac.commoners,[
     itm.mail_coif,itm.splinted_greaves,itm.mail_mittens,itm.mail_with_surcoat,
     itm.mercenary_shield_b,
     itm.sword_medieval_c,
  ], level(17)|str_17|agi_13|int_21|cha_7,wpe(220,90,140,100),knows_ironflesh_5|knows_power_strike_2|knows_weapon_master_3|knows_shield_3|knows_athletics_3|knows_riding_4|knows_looting_2|knows_trainer_1|knows_inventory_management_1|knows_wound_treatment_6|knows_surgery_5|knows_first_aid_3|knows_prisoner_management_1|knows_leadership_1,0x0000000083040001583b6db8dec5925b00000000001d80980000000000000000],

  # Foreign noble
  ["npc4","Thorgrim","Thorgrim",            tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac.commoners,[
    itm.footman_helmet,itm.mail_chausses,itm.mail_gauntlets,itm.mail_hauberk,
    itm.shield_common_round_d,
    itm.sword_medieval_c_long,
    itm.hunter_horse,
  ], level(10)|str_16|agi_11|int_13|cha_11,wpex(120,120,100,70,80,120),knows_ironflesh_3|knows_power_strike_4|knows_power_throw_3|knows_weapon_master_2|knows_shield_3|knows_athletics_2|knows_riding_3|knows_trainer_2|knows_tactics_2|knows_inventory_management_1|knows_first_aid_2|knows_prisoner_management_1|knows_leadership_3,0x000000057f1074002c75c6a8a58ad72e00000000001e1a890000000000000000],

  # Noble khergit
  ["npc5","Baheshtur","Baheshtur",          tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac.commoners,[
    itm.khergit_leather_boots,itm.steppe_armor,
    itm.khergit_shield_a2,
    itm.nomad_bow_khe,itm.broadhead_arrows,itm.khergit_sword_b,
    itm.khergit_horse,
  ], level(5)|str_11|agi_16|int_12|cha_7,wpex(90,60,90,110,60,80),knows_ironflesh_2|knows_power_strike_1|knows_power_draw_3|knows_weapon_master_2|knows_shield_2|knows_riding_5|knows_horse_archery_4|knows_looting_1|knows_pathfinding_1|knows_inventory_management_1|knows_prisoner_management_2,0x000000088910318b5c6f972328324a6200000000001cd3310000000000000000],

  # Military captain
  ["npc6","Erevan Ilesere","Erevan Ilesere",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac.commoners,[
    itm.skullcap,itm.light_leather_boots,itm.leather_gloves,itm.studded_leather_coat,
    itm.sword_medieval_c,
    itm.shield_common_round_d,
  ], level(6)|str_17|agi_14|int_11|cha_5,wpe(105,90,90,90),knows_ironflesh_4|knows_power_strike_5|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_3|knows_shield_4|knows_athletics_3|knows_riding_1|knows_looting_2|knows_inventory_management_1|knows_prisoner_management_1,0x00000002050052036a1895d0748f3ca30000000000000f0b0000000000000000],

  # Runaway bandit, archer
  ["npc7","Deshavi","Deshavi",    tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac.commoners,[
    itm.black_hood,itm.hunter_boots,itm.archer_gloves,itm.padded_cloth,
    itm.long_bow,itm.hunting_arrows,itm.shortened_spear,
  ], level(2)|str_12|agi_14|int_10|cha_7,wpex(50,60,70,90,60,70),knows_ironflesh_3|knows_power_strike_1|knows_power_draw_3|knows_weapon_master_1|knows_shield_1|knows_athletics_4|knows_riding_1|knows_looting_2|knows_inventory_management_2|knows_prisoner_management_2|knows_trade_1,0x00000001fc08400533a15297634d44f400000000001e02db0000000000000000],

  # Engineer
  ["npc8","Jinnai","Jinnai",                tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac.commoners,[
    itm.donkey_b,itm.woolen_hose,itm.red_shirt,
    itm.hammer,
  ], level(7)|str_9|agi_10|int_16|cha_13,wpex(90,70,70,70,80,80),knows_ironflesh_3|knows_power_strike_3|knows_weapon_master_1|knows_shield_3|knows_riding_3|knows_looting_1|knows_trainer_1|knows_tactics_1|knows_inventory_management_2|knows_engineer_5|knows_leadership_1|knows_trade_3,0x000000003f00224524ed6d001a82da0300000000001cc0b70000000000000000],

  # Megamerc noble
  ["npc9","Achilles","Achilles",            tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac.commoners,[
    itm.helmet_with_neckguard,itm.mail_chausses,itm.scale_gauntlets,
    itm.mercenary_shield_b,
    itm.bastard_sword_a,itm.sword_medieval_d,
    itm.armored_hunter,itm.hera_arena_armor,
  ], level(25)|str_28|agi_17|int_10|cha_11,wpe(250,220,190,200),knows_ironflesh_7|knows_power_strike_9|knows_power_draw_6|knows_weapon_master_4|knows_shield_5|knows_athletics_3|knows_riding_5|knows_horse_archery_2|knows_looting_3|knows_trainer_2|knows_inventory_management_1|knows_first_aid_1|knows_prisoner_management_2|knows_leadership_1,0x000000030100300f499d5b391b6db8d300000000001dc2e10000000000000000],

  # Captain of civil guard in Veluca
  ["npc10","Vorian","Vorian",               tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac.commoners,[
    itm.helmet_with_neckguard,itm.mail_chausses,itm.mail_mittens,itm.rhodok_brigandine_vest,
    itm.crossbow,itm.bolts,itm.heavy_falchion,
    itm.hera_rhodok_pavise_b,
  ], level(9)|str_17|agi_11|int_9|cha_13,wpex(100,80,110,70,130,80),knows_ironflesh_4|knows_power_strike_3|knows_weapon_master_3|knows_shield_3|knows_athletics_3|knows_riding_1|knows_trainer_3|knows_tactics_2|knows_spotting_1|knows_inventory_management_1|knows_first_aid_1|knows_prisoner_management_2|knows_leadership_3,0x0000000a3f081006572c91c71c8d46cb00000000001e468a0000000000000000],

  # Army merchant
  ["npc11","Katrin","Katrin",     tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac.commoners,[
    itm.wimple_a,itm.blue_hose,itm.woolen_dress,
    itm.stones,itm.cleaver,
    itm.mule,
  ], level(8)|str_8|agi_11|int_13|cha_17,wpex(60,40,30,60,60,60),knows_ironflesh_1|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_1|knows_athletics_3|knows_riding_2|knows_looting_3|knows_tracking_1|knows_pathfinding_3|knows_inventory_management_3|knows_first_aid_3|knows_prisoner_management_1|knows_trade_5,0x0000000d7f0400035915aa226b4d975200000000001ea49e0000000000000000],

  # Doctor
  ["npc12","Aragorn","Aragorn",             tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac.commoners,[
    itm.wrapping_boots,itm.pilgrim_disguise,
    itm.dagger,
  ], level(4)|str_8|agi_10|int_19|cha_8,wpex(30,30,50,30,30,40),knows_ironflesh_1|knows_athletics_3|knows_trainer_1|knows_inventory_management_2|knows_wound_treatment_4|knows_surgery_6|knows_first_aid_5|knows_engineer_1,0x000000078000500e4f8ba62a9cd5d36d00000000001e36250000000000000000],

  # Warrior, poet
  ["npc13","Nizar","Nizar",                 tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac.commoners,[
    itm.sarranid_helmet1,itm.sarranid_boots_b,itm.leather_gloves,itm.sarranid_leather_vest,
    itm.scimitar,
    itm.arabian_horse_b,
  ], level(3)|str_9|agi_13|int_12|cha_10,wpex(90,60,80,50,40,60),knows_power_strike_3|knows_weapon_master_2|knows_shield_4|knows_riding_4|knows_trainer_1|knows_tracking_1|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_prisoner_management_1|knows_leadership_3,0x00000004bf0475c85f4e9592de4e574c00000000001e369c0000000000000000],

  # Megamerc noble, trainer
  ["npc14","Kelemvor","Kelemvor",           tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac.commoners,[
    itm.norman_helmet,itm.splinted_greaves,itm.mail_gauntlets,itm.byrnie,
    itm.light_crossbow,itm.bolts,itm.sword_viking_c,
    itm.mercenary_shield_b,
  ], level(22)|str_16|agi_13|int_23|cha_11,wp(200),knows_ironflesh_4|knows_power_strike_2|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_4|knows_shield_3|knows_athletics_2|knows_riding_4|knows_horse_archery_2|knows_looting_1|knows_trainer_7|knows_tactics_4|knows_inventory_management_1|knows_first_aid_4|knows_leadership_3,0x00000001a410259144d5d1d6eb55e96a00000000001db0db0000000000000000],

  # Lady, captain of golden company
  ["npc15","Alyssa","Alyssa",     tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac.commoners,[
    itm.guard_helmet,itm.mail_boots,itm.mail_mittens,itm.cuir_bouilli,
    itm.mercenary_shield_a,itm.sword_swadian_a,
    itm.armored_courser,
  ], level(24)|str_17|agi_15|int_17|cha_16,wpe(210,100,120,120),knows_ironflesh_5|knows_power_strike_5|knows_weapon_master_4|knows_shield_5|knows_athletics_2|knows_riding_5|knows_looting_4|knows_trainer_3|knows_tactics_5|knows_inventory_management_2|knows_first_aid_1|knows_prisoner_management_2|knows_leadership_5|knows_trade_1,0x00000000330c00020480401600a0000000000000001c00c70000000000000000],

  # Former castle servant, on the thievy side
  ["npc16","Klethi","Klethi",     tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac.commoners,[
    itm.headcloth,itm.ankle_boots,itm.peasant_dress,
    itm.darts,itm.club,
  ], level(2)|str_9|agi_15|int_8|cha_11,wpex(60,30,30,50,40,70),knows_ironflesh_1|knows_power_throw_3|knows_weapon_master_1|knows_athletics_3|knows_riding_1|knows_looting_3|knows_pathfinding_1|knows_spotting_2|knows_inventory_management_2|knows_first_aid_1|knows_trade_3,0x00000000000c100739ce9c805d2f381300000000001cc7ad0000000000000000],

  # KINGS

  ["kingdom_1_lord",  "Queen Katilus",     "Katilus",  tf_hero|tf_female, 0,reserved, fac.kingdom_1,    [
    itm.rich_outfit,itm.blue_hose,
    itm.swadian_armor_royal,itm.swadian_boots_royal,itm.ornate_gauntlets,itm.swadian_helm_royal,
    itm.swadian_shield_royal,
    itm.swadian_lance_royal,itm.sword_swadian_g,
    itm.swadian_horse_royal,
  ], level(41)|str_30|agi_30|int_25|cha_30, wp(440), knows_king|knows_athletics_7|knows_trainer_5|knows_tactics_8|knows_leadership_10|knows_prisoner_management_3, 0x00000000ef00000237dc71b90c31631200000000001e371b0000000000000000],
  ["kingdom_2_lord",  "Czar Yaroglek",     "Yaroglek", tf_hero,           0,reserved, fac.kingdom_2,    [
    itm.courtly_outfit,itm.leather_boots,
    itm.vaegir_armor_royal,itm.vaegir_boots_royal,itm.vaegir_gauntlets_royal,itm.vaegir_lichina_helm,
    itm.vaegir_shield_royal,
    itm.vaegir_bardiche_royal,itm.vaegir_morningstar_royal,itm.vaegir_bow_royal,itm.vaegir_arrows_royal,
    itm.vaegir_horse_royal,
  ], level(41)|str_30|agi_30|int_30|cha_30, wp(440), knows_king|knows_athletics_8|knows_trainer_4|knows_tactics_10|knows_leadership_10|knows_prisoner_management_3, 0x0000000ec50001400a2269f919dee11700000000001cc57d0000000000000000, vaegir_face_old_2],
  ["kingdom_3_lord",  "Sanjar-Khagan",     "Sanjar",   tf_hero,           0,reserved, fac.kingdom_3,    [
    itm.nomad_robe,itm.leather_boots,
    itm.khergit_armor_royal,itm.khergit_boots_royal,itm.khergit_gauntlets_royal,itm.tarkhan_helm,
    itm.khergit_shield_royal,
    itm.khergit_hafted_blade_royal,itm.khergit_sabre_royal,itm.khergit_bow_royal,itm.khergit_arrows_c,
    itm.khergit_horse_royal,
  ], level(41)|str_30|agi_30|int_25|cha_30, wp_melee(440)|wp_archery(520), knows_king|knows_power_draw_10|knows_athletics_4|knows_horse_archery_10|knows_trainer_6|knows_tactics_7|knows_leadership_10|knows_prisoner_management_3, 0x0000000cee0051cc44be2d14d370c65c00000000001ed6df0000000000000000, khergit_face_old_2],
  ["kingdom_4_lord",  "Jarl Ragnar",       "Ragnar",   tf_hero,           0,reserved, fac.kingdom_4,    [
    itm.nobleman_outfit,itm.leather_boots,
    itm.nordic_armor_royal,itm.nord_boots_royal,itm.scale_gauntlets_gilded,itm.nordic_helm_royal,
    itm.nord_shield_royal,
    itm.nord_axe_royal,itm.heavy_throwing_axes,itm.heavy_throwing_axes,
    itm.nordic_horse_royal,
  ], level(41)|str_30|agi_30|int_20|cha_30, wp(440), knows_king|knows_athletics_10|knows_trainer_4|knows_tactics_10|knows_leadership_10|knows_prisoner_management_3, 0x0000000e2c0c028a068e8c18557b12a500000000001c0fe80000000000000000, nord_face_older_2],
  ["kingdom_5_lord",  "Dictator Graveth",  "Graveth",  tf_hero,           0,reserved, fac.kingdom_5,    [
    itm.tabard,itm.leather_boots,
    itm.rhodok_armor_royal,itm.elite_plate_boots,itm.ornate_gauntlets,itm.rhodok_visored_sallet,
    itm.rhodok_shield_royal,
    itm.rhodok_halberd_royal,itm.battle_cleaver,itm.da_veidar,itm.rhodok_bolts_c,
    itm.rhodok_horse_royal,
  ], level(37)|str_30|agi_27|int_20|cha_30, wp(440), knows_king|knows_athletics_10|knows_trainer_5|knows_tactics_6|knows_leadership_9|knows_prisoner_management_3, 0x0000000efc04119225848dac5d50d62400000000001d48b80000000000000000, rhodok_face_old_2],
  ["kingdom_6_lord",  "Sultan Hakim",      "Hakim",    tf_hero,           0,reserved, fac.kingdom_6,    [
    itm.nobleman_outfit,itm.sarranid_boots_c,
    itm.sarranid_armor_royal,itm.sarranid_boots_c,itm.sarranid_gauntlets_royal,itm.sarranid_helm_royal,
    itm.sarranid_shield_royal,
    itm.sarranid_lance_c,itm.sarranid_scimitar_royal,
    itm.sarranid_horse_royal,
  ], level(41)|str_30|agi_30|int_20|cha_30, wp(440), knows_king|knows_athletics_10|knows_trainer_5|knows_tactics_10|knows_leadership_10|knows_prisoner_management_3, 0x0000000a4b103354189c71d6d386e8ac00000000001e24eb0000000000000000, rhodok_face_old_2],
  ["dark_knight_lord","Kaiserine Larktin", "Larktin",  tf_hero|tf_female, 0,reserved, fac.dark_knights, [
    itm.larktin_black_armor,itm.larktin_black_greaves,itm.larktin_gauntlets,itm.dk_helm_royal,
    itm.dk_shield_royal,
    itm.great_lance,itm.sword_medieval_d_long,
    itm.dk_horse_royal,
  ], level(63)|str_30|agi_30|int_30|cha_30, wp(560), knows_ironflesh_10|knows_shield_10|knows_power_strike_10|knows_athletics_10|knows_riding_10|knows_tactics_10|knows_leadership_10, 0x00000000000000050e50a3d741a6824800000000001c00200000000000000000],

  # LORDS

  #Swadian civilian clothes: itm.courtly_outfit itm.gambeson itm.blue_gambeson itm.red_gambeson itm.nobleman_outfit itm.rich_outfit itm.red_shirt itm.tabard,
  #Older knights with higher skills moved to top

  ["knight_1_1", "Count Klargus", "Klargus", tf_hero, 0, reserved, fac.kingdom_1, [
    itm.hera_tabard_b,itm.nomad_boots,
    itm.hera_plate_armor,itm.plate_boots,itm.ornate_gauntlets,itm.winged_great_helmet,
    itm.hera_swadian_cav_shield_c,
    itm.paladin_lance_1,itm.sword_swadian_f,
    itm.swadian_charger_b,
  ], new_lord_attrib, wp(230), knight_skills_5|knows_trainer_1|knows_trainer_3, 0x0000000c3e08601414ab4dc6e39296b200000000001e231b0000000000000000, swadian_face_older_2],
  ["knight_1_2", "Count Delinard", "Delinard", tf_hero, 0, reserved, fac.kingdom_1, [
    itm.hera_padded_cloth_a,itm.nomad_boots,
    itm.hera_plate_armor,itm.plate_boots,itm.ornate_gauntlets,itm.winged_great_helmet,
    itm.hera_swadian_cav_shield_c,
    itm.paladin_lance_2,itm.sword_swadian_f,
    itm.swadian_charger_b,
  ], new_lord_attrib, wp(240), knight_skills_5, 0x0000000c0f0c320627627238dcd6599400000000001c573d0000000000000000, swadian_face_young_2],
  ["knight_1_3", "Count Haringoth", "Haringoth", tf_hero, 0, reserved, fac.kingdom_1, [
    itm.hera_tabard_b,itm.leather_boots,
    itm.hera_plate_armor,itm.plate_boots,itm.ornate_gauntlets,itm.winged_great_helmet,
    itm.hera_swadian_cav_shield_c,
    itm.paladin_lance_1,itm.sword_swadian_g,
    itm.swadian_charger_b,
  ], new_lord_attrib, wp(260), knight_skills_5|knows_trainer_3, 0x0000000cb700210214ce89db276aa2f400000000001d36730000000000000000, swadian_face_young_2],
  ["knight_1_4", "Count Clais", "Clais", tf_hero, 0, reserved, fac.kingdom_1, [
    itm.hera_rich_tunic_a,itm.leather_boots,
    itm.hera_plate_armor,itm.plate_boots,itm.ornate_gauntlets,itm.winged_great_helmet,
    itm.hera_swadian_cav_shield_c,
    itm.paladin_lance_2,itm.sword_swadian_f,
    itm.swadian_charger_b,
  ], new_lord_attrib, wp(180), knight_skills_5|knows_trainer_4, 0x0000000c370c1194546469ca6c4e450e00000000001ebac40000000000000000, swadian_face_older_2],
  ["knight_1_5", "Count Deglan", "Deglan", tf_hero, 0, reserved, fac.kingdom_1, [
    itm.hera_tabard_b,itm.woolen_hose,
    itm.hera_plate_armor,itm.plate_boots,itm.ornate_gauntlets,itm.winged_great_helmet,
    itm.hera_swadian_cav_shield_c,
    itm.paladin_lance_1,itm.sword_swadian_g,
    itm.swadian_charger_b,
  ], new_lord_attrib, wp(200), knight_skills_4|knows_trainer_6, 0x0000000c0c1064864ba34e2ae291992b00000000001da8720000000000000000, swadian_face_older_2],
  ["knight_1_6", "Count Tredian", "Tredian", tf_hero, 0, reserved, fac.kingdom_1, [
    itm.hera_tabard_b,itm.leather_boots,
    itm.hera_plate_armor,itm.plate_boots,itm.ornate_gauntlets,itm.winged_great_helmet,
    itm.hera_swadian_cav_shield_c,
    itm.paladin_lance_2,itm.sword_swadian_g,
    itm.swadian_charger_b,
  ], new_lord_attrib, wp(240), knight_skills_4|knows_trainer_4, 0x0000000c0a08038736db74c6a396a8e500000000001db8eb0000000000000000, swadian_face_older_2],
  ["knight_1_7", "Count Grainwad", "Grainwad", tf_hero, 0, reserved, fac.kingdom_1, [
    itm.hera_tabard_b,itm.leather_boots,
    itm.hera_plate_armor,itm.plate_boots,itm.ornate_gauntlets,itm.winged_great_helmet,
    itm.hera_swadian_cav_shield_c,
    itm.paladin_lance_1,itm.sword_swadian_f,
    itm.swadian_charger_b,
  ], new_lord_attrib, wp(290), knight_skills_4|knows_trainer_4, 0x0000000c1e001500589dae4094aa291c00000000001e37a80000000000000000, swadian_face_young_2],
  ["knight_1_8", "Count Ryis", "Ryis", tf_hero, 0, reserved, fac.kingdom_1, [
    itm.hera_tabard_b,itm.leather_boots,
    itm.hera_plate_armor,itm.plate_boots,itm.ornate_gauntlets,itm.winged_great_helmet,
    itm.hera_swadian_cav_shield_c,
    itm.paladin_lance_2,itm.sword_swadian_f,
    itm.swadian_charger_b,
  ], new_lord_attrib, wp(250), knight_skills_4, 0x0000000c330855054aa9aa431a48d74600000000001ed5240000000000000000, swadian_face_older_2],
  ["knight_1_9", "Count Plais", "Plais", tf_hero, 0, reserved, fac.kingdom_1, [
    itm.hera_padded_cloth_b,itm.blue_hose,
    itm.hera_plate_armor,itm.plate_boots,itm.ornate_gauntlets,itm.winged_great_helmet,
    itm.hera_swadian_cav_shield_c,
    itm.cavalier_lance_1,itm.sword_swadian_f,
    itm.swadian_warhorse_d,
  ], new_lord_attrib, wp(160), knight_skills_3, 0x0000000c0f08000458739a9a1476199800000000001fb6f10000000000000000, swadian_face_old_2],
  ["knight_1_10", "Count Mirchaud", "Mirchaud", tf_hero, 0, reserved, fac.kingdom_1, [
    itm.hera_padded_cloth_a,itm.woolen_hose,
    itm.hera_plate_armor,itm.plate_boots,itm.ornate_gauntlets,itm.winged_great_helmet,
    itm.hera_swadian_cav_shield_c,
    itm.cavalier_lance_2,itm.sword_swadian_g,
    itm.swadian_warhorse_e,
  ], new_lord_attrib, wp(190), knight_skills_3, 0x0000000c0610351048e325361d7236cd00000000001d532a0000000000000000, swadian_face_older_2],
  ["knight_1_11", "Count Stamar", "Stamar", tf_hero, 0, reserved, fac.kingdom_1, [
    itm.hera_tabard_b,itm.nomad_boots,
    itm.hera_plate_armor,itm.plate_boots,itm.ornate_gauntlets,itm.winged_great_helmet,
    itm.hera_swadian_cav_shield_c,
    itm.cavalier_lance_1,itm.sword_swadian_f,
    itm.swadian_warhorse_e,
  ], new_lord_attrib, wp(220), knight_skills_3, 0x0000000c03104490280a8cb2a24196ab00000000001eb4dc0000000000000000, swadian_face_older_2],
  ["knight_1_12", "Count Meltor", "Meltor", tf_hero, 0, reserved, fac.kingdom_1, [
    itm.hera_tabard_b,itm.nomad_boots,
    itm.hera_plate_armor,itm.plate_boots,itm.ornate_gauntlets,itm.winged_great_helmet,
    itm.hera_swadian_cav_shield_c,
    itm.cavalier_lance_2,itm.sword_swadian_f,
    itm.swadian_warhorse_d,
  ], new_lord_attrib, wp(130), knight_skills_3, 0x0000000c2a0805442b2c6cc98c8dbaac00000000001d389b0000000000000000, swadian_face_older_2],
  ["knight_1_13", "Count Beranz", "Beranz", tf_hero, 0, reserved, fac.kingdom_1, [
    itm.hera_leather_vest,itm.nomad_boots,
    itm.hera_plate_armor,itm.plate_boots,itm.ornate_gauntlets,itm.winged_great_helmet,
    itm.hera_swadian_cav_shield_c,
    itm.cavalier_lance_1,itm.sword_swadian_f,
    itm.swadian_warhorse_d,
  ], new_lord_attrib, wp(160), knight_skills_2, 0x0000000c380c30c2392a8e5322a5392c00000000001e5c620000000000000000, swadian_face_older_2],
  ["knight_1_14", "Count Rafard", "Rafard", tf_hero, 0, reserved, fac.kingdom_1, [
    itm.hera_rich_tunic_a,itm.leather_boots,
    itm.hera_plate_armor,itm.plate_boots,itm.ornate_gauntlets,itm.winged_great_helmet,
    itm.hera_swadian_cav_shield_c,
    itm.cavalier_lance_1,itm.sword_swadian_g,
    itm.swadian_warhorse_d,
  ], new_lord_attrib, wp(190), knight_skills_3|knows_trainer_6, 0x0000000c3f10000532d45203954e192200000000001e47630000000000000000, swadian_face_older_2],
  ["knight_1_15", "Count Regas", "Regas", tf_hero, 0, reserved, fac.kingdom_1, [
    itm.hera_tabard_b,itm.woolen_hose,
    itm.hera_plate_armor,itm.plate_boots,itm.ornate_gauntlets,itm.winged_great_helmet,
    itm.hera_swadian_cav_shield_c,
    itm.cavalier_lance_2,itm.sword_swadian_g,
    itm.swadian_warhorse_e,
  ], new_lord_attrib, wp(140), knight_skills_2, 0x0000000c5c0840034895654c9b660c5d00000000001e34530000000000000000, swadian_face_young_2],
  ["knight_1_16", "Count Devlian", "Devlian", tf_hero, 0, reserved, fac.kingdom_1, [
    itm.hera_tabard_b,itm.nomad_boots,
    itm.hera_plate_armor,itm.plate_boots,itm.ornate_gauntlets,itm.winged_great_helmet,
    itm.hera_swadian_cav_shield_c,
    itm.cavalier_lance_2,itm.sword_swadian_f,
    itm.swadian_warhorse_e,
  ], new_lord_attrib, wp(130), knight_skills_2, 0x000000095108144657a1ba3ad456e8cb00000000001e325a0000000000000000, swadian_face_young_2],
  ["knight_1_17", "Count Rafarch", "Rafarch", tf_hero, 0, reserved, fac.kingdom_1, [
    itm.hera_padded_cloth_b,itm.blue_hose,
    itm.hera_plate_armor,itm.plate_boots,itm.ornate_gauntlets,itm.winged_great_helmet,
    itm.hera_swadian_cav_shield_c,
    itm.cavalier_lance_1,itm.sword_swadian_f,
    itm.swadian_warhorse_e,
  ], new_lord_attrib, wp(190), knight_skills_1|knows_trainer_4, 0x0000000c010c42c14d9d6918bdb336e200000000001dd6a30000000000000000, swadian_face_young_2],
  ["knight_1_18", "Count Rochabarth", "Rochabarth", tf_hero, 0, reserved, fac.kingdom_1, [
    itm.hera_tabard_b,itm.woolen_hose,
    itm.hera_plate_armor,itm.plate_boots,itm.ornate_gauntlets,itm.winged_great_helmet,
    itm.hera_swadian_cav_shield_c,
    itm.cavalier_lance_2,itm.sword_swadian_g,
    itm.swadian_warhorse_d,
  ], new_lord_attrib, wp(210), knight_skills_1, 0x0000000c150045c6365d8565932a8d6400000000001ec6940000000000000000, swadian_face_young_2],
  ["knight_1_19", "Count Despin", "Despin", tf_hero, 0, reserved, fac.kingdom_1, [
    itm.hera_tabard_b,itm.nomad_boots,
    itm.hera_plate_armor,itm.plate_boots,itm.ornate_gauntlets,itm.winged_great_helmet,
    itm.hera_swadian_cav_shield_c,
    itm.cavalier_lance_2,itm.sword_swadian_f,
    itm.swadian_warhorse_e,
  ], new_lord_attrib, wp(120), knight_skills_1, 0x00000008200012033d9b6d4a92ada53500000000001cc1180000000000000000, swadian_face_young_2],
  ["knight_1_20", "Count Montewar", "Montewar", tf_hero, 0, reserved, fac.kingdom_1, [
    itm.hera_leather_vest,itm.nomad_boots,
    itm.hera_plate_armor,itm.plate_boots,itm.ornate_gauntlets,itm.winged_great_helmet,
    itm.hera_swadian_cav_shield_c,
    itm.cavalier_lance_1,itm.sword_swadian_f,
    itm.swadian_warhorse_d,
  ], new_lord_attrib, wp(150), knight_skills_1, 0x0000000c4d0840d24a9b2ab4ac2a332400000000001d34db0000000000000000, swadian_face_young_2],


  ["knight_2_1", "Boyar Vuldrat", "Vuldrat", tf_hero, 0, reserved, fac.kingdom_2, [
    itm.hera_padded_cloth_a,itm.nomad_boots,
    itm.vaegir_scaled_cuirass,itm.splinted_leather_greaves,itm.scale_gauntlets_gilded,itm.vaegir_noble_fullhelm,
    itm.hera_vaegir_inf_shield_c,
    itm.great_lance,itm.weighted_morningstar,
    itm.vaegir_warhorse_c,
  ], new_lord_attrib, wp(130), knight_skills_1|knows_trainer_3, 0x00000005590011c33d9b6d4a92ada53500000000001cc1180000000000000000, vaegir_face_middle_2],
  ["knight_2_2", "Boyar Naldera", "Naldera", tf_hero, 0, reserved, fac.kingdom_2, [
    itm.hera_padded_cloth_a,itm.woolen_hose,
    itm.vaegir_scaled_cuirass,itm.splinted_leather_greaves,itm.scale_gauntlets_gilded,itm.vaegir_noble_fullhelm,
    itm.hera_vaegir_inf_shield_c,
    itm.great_lance,itm.weighted_morningstar,
    itm.vaegir_warhorse_c,
  ], new_lord_attrib, wp(160), knight_skills_2, 0x0000000c2a0015d249b68b46a98e176400000000001d95a40000000000000000, vaegir_face_old_2],
  ["knight_2_3", "Boyar Meriga", "Meriga", tf_hero, 0, reserved, fac.kingdom_2, [
    itm.hera_rich_tunic_a,itm.woolen_hose,
    itm.vaegir_scaled_cuirass,itm.splinted_leather_greaves,itm.scale_gauntlets_gilded,itm.vaegir_noble_fullhelm,
    itm.hera_vaegir_inf_shield_c,
    itm.great_lance,itm.weighted_morningstar,
    itm.vaegir_warhorse_c,
  ], new_lord_attrib, wp(190), knight_skills_3, 0x0000000c131031c546a38a2765b4c86000000000001e58d30000000000000000, vaegir_face_older_2],
  ["knight_2_4", "Boyar Khavel", "Khavel", tf_hero, 0, reserved, fac.kingdom_2, [
    itm.hera_padded_cloth_b,itm.leather_boots,
    itm.vaegir_scaled_cuirass,itm.splinted_leather_greaves,itm.scale_gauntlets_gilded,itm.vaegir_noble_fullhelm,
    itm.hera_vaegir_inf_shield_c,
    itm.great_lance,itm.weighted_morningstar,
    itm.vaegir_warhorse_c,
  ], new_lord_attrib, wp(220), knight_skills_4, 0x0000000c2f0832c748f272540d8ab65900000000001d34e60000000000000000, vaegir_face_older_2],
  ["knight_2_5", "Boyar Doru", "Doru", tf_hero, 0, reserved, fac.kingdom_2, [
    itm.hera_tabard_b,itm.leather_boots,
    itm.vaegir_scaled_cuirass,itm.splinted_leather_greaves,itm.scale_gauntlets_gilded,itm.vaegir_noble_fullhelm,
    itm.hera_vaegir_inf_shield_c,
    itm.great_lance,itm.weighted_morningstar,
    itm.vaegir_warhorse_c,
  ], new_lord_attrib, wp(250), knight_skills_5, 0x0000000e310061435d76bb5f55bad9ad00000000001ed8ec0000000000000000, vaegir_face_older_2],
  ["knight_2_6", "Boyar Belgaru", "Belgaru", tf_hero, 0, reserved, fac.kingdom_2, [
    itm.hera_padded_cloth_b,itm.woolen_hose,
    itm.vaegir_scaled_cuirass,itm.splinted_leather_greaves,itm.scale_gauntlets_gilded,itm.vaegir_noble_fullhelm,
    itm.hera_vaegir_inf_shield_c,
    itm.great_lance,itm.weighted_morningstar,
    itm.vaegir_warhorse_c,
  ], new_lord_attrib, wp(130), knight_skills_1|knows_trainer_3, 0x0000000a0100421038da7157aa4e430a00000000001da8bc0000000000000000, vaegir_face_middle_2],
  ["knight_2_7", "Boyar Ralcha", "Ralcha", tf_hero, 0, reserved, fac.kingdom_2, [
    itm.hera_leather_vest,itm.leather_boots,
    itm.vaegir_scaled_cuirass,itm.splinted_leather_greaves,itm.scale_gauntlets_gilded,itm.vaegir_noble_fullhelm,
    itm.hera_vaegir_inf_shield_c,
    itm.great_lance,itm.weighted_morningstar,
    itm.vaegir_warhorse_c,
  ], new_lord_attrib, wp(160), knight_skills_2|knows_trainer_4, 0x0000000c04100153335ba9390b2d277500000000001d89120000000000000000, vaegir_face_old_2],
  ["knight_2_8", "Boyar Vlan", "Vlan", tf_hero, 0, reserved, fac.kingdom_2, [
    itm.hera_padded_cloth_b,itm.woolen_hose,
    itm.vaegir_scaled_cuirass,itm.splinted_leather_greaves,itm.scale_gauntlets_gilded,itm.vaegir_noble_fullhelm,
    itm.hera_vaegir_inf_shield_c,
    itm.great_lance,itm.weighted_morningstar,
    itm.vaegir_warhorse_c,
  ], new_lord_attrib, wp(200), knight_skills_3|knows_trainer_5, 0x0000000c00046581234e8da2cdd248db00000000001f569c0000000000000000, vaegir_face_older_2],
  ["knight_2_9", "Boyar Mleza", "Mleza", tf_hero, 0, reserved, fac.kingdom_2, [
    itm.hera_padded_cloth_a,itm.leather_boots,
    itm.vaegir_scaled_cuirass,itm.splinted_leather_greaves,itm.scale_gauntlets_gilded,itm.vaegir_noble_fullhelm,
    itm.hera_vaegir_inf_shield_c,
    itm.great_lance,itm.weighted_morningstar,
    itm.vaegir_warhorse_c,
  ], new_lord_attrib, wp(230), knight_skills_4, 0x0000000c160451d2136469c4d9b159ad00000000001e28f10000000000000000, vaegir_face_older_2],
  ["knight_2_10", "Boyar Nelag", "Nelag", tf_hero, 0, reserved, fac.kingdom_2, [
    itm.hera_padded_cloth_a,itm.woolen_hose,
    itm.vaegir_scaled_cuirass,itm.splinted_leather_greaves,itm.scale_gauntlets_gilded,itm.vaegir_noble_fullhelm,
    itm.hera_vaegir_inf_shield_c,
    itm.great_lance,itm.weighted_morningstar,
    itm.vaegir_warhorse_c,
  ], new_lord_attrib, wp(260), knight_skills_5|knows_trainer_6, 0x0000000f7c00520e66b76edd5cd5eb6e00000000001f691e0000000000000000, vaegir_face_older_2],
  ["knight_2_11", "Boyar Crahask", "Crahask", tf_hero, 0, reserved, fac.kingdom_2, [
    itm.hera_leather_vest,itm.nomad_boots,
    itm.vaegir_scaled_cuirass,itm.splinted_leather_greaves,itm.scale_gauntlets_gilded,itm.vaegir_noble_fullhelm,
    itm.hera_vaegir_inf_shield_c,
    itm.great_lance,itm.weighted_morningstar,
    itm.vaegir_warhorse_c,
  ], new_lord_attrib, wp(130), knight_skills_1, 0x0000000c1d0821d236acd6991b74d69d00000000001e476c0000000000000000, vaegir_face_middle_2],
  ["knight_2_12", "Boyar Bracha", "Bracha", tf_hero, 0, reserved, fac.kingdom_2, [
    itm.hera_padded_cloth_b,itm.woolen_hose,
    itm.vaegir_scaled_cuirass,itm.splinted_leather_greaves,itm.scale_gauntlets_gilded,itm.vaegir_noble_fullhelm,
    itm.hera_vaegir_inf_shield_c,
    itm.great_lance,itm.weighted_morningstar,
    itm.vaegir_warhorse_c,
  ], new_lord_attrib, wp(170), knight_skills_2, 0x0000000c0f04024b2509d5d53944c6a300000000001d5b320000000000000000, vaegir_face_old_2],
  ["knight_2_13", "Boyar Druli", "Druli", tf_hero, 0, reserved, fac.kingdom_2, [
    itm.hera_rich_tunic_a,itm.woolen_hose,
    itm.vaegir_scaled_cuirass,itm.splinted_leather_greaves,itm.scale_gauntlets_gilded,itm.vaegir_noble_fullhelm,
    itm.hera_vaegir_inf_shield_c,
    itm.great_lance,itm.weighted_morningstar,
    itm.vaegir_warhorse_c,
  ], new_lord_attrib, wp(190), knight_skills_3, 0x0000000c680432d3392230cb926d56ca00000000001da69b0000000000000000, vaegir_face_older_2],
  ["knight_2_14", "Boyar Marmun", "Marmun", tf_hero, 0, reserved, fac.kingdom_2, [
    itm.hera_padded_cloth_a,itm.leather_boots,
    itm.vaegir_scaled_cuirass,itm.splinted_leather_greaves,itm.scale_gauntlets_gilded,itm.vaegir_noble_fullhelm,
    itm.hera_vaegir_inf_shield_c,
    itm.great_lance,itm.weighted_morningstar,
    itm.vaegir_warhorse_c,
  ], new_lord_attrib, wp(220), knight_skills_4|knows_trainer_6, 0x0000000c27046000471bd2e93375b52c00000000001dd5220000000000000000, vaegir_face_older_2],
  ["knight_2_15", "Boyar Gastya", "Gastya", tf_hero, 0, reserved, fac.kingdom_2, [
    itm.hera_padded_cloth_b,itm.leather_boots,
    itm.vaegir_scaled_cuirass,itm.splinted_leather_greaves,itm.scale_gauntlets_gilded,itm.vaegir_noble_fullhelm,
    itm.hera_vaegir_inf_shield_c,
    itm.great_lance,itm.weighted_morningstar,
    itm.vaegir_warhorse_c,
  ], new_lord_attrib, wp(250), knight_skills_5, 0x0000000de50052123b6bb36de5d6eb7400000000001dd72c0000000000000000, vaegir_face_older_2],
  ["knight_2_16", "Boyar Harish", "Harish", tf_hero, 0, reserved, fac.kingdom_2, [
    itm.hera_padded_cloth_b,itm.woolen_hose,
    itm.vaegir_scaled_cuirass,itm.splinted_leather_greaves,itm.scale_gauntlets_gilded,itm.vaegir_noble_fullhelm,
    itm.hera_vaegir_inf_shield_c,
    itm.great_lance,itm.weighted_morningstar,
    itm.vaegir_warhorse_c,
  ], new_lord_attrib, wp(120), knight_skills_1, 0x000000085f00000539233512e287391d00000000001db7200000000000000000, vaegir_face_middle_2],
  ["knight_2_17", "Boyar Taisa", "Taisa", tf_hero, 0, reserved, fac.kingdom_2, [
    itm.hera_leather_vest,itm.leather_boots,
    itm.vaegir_scaled_cuirass,itm.splinted_leather_greaves,itm.scale_gauntlets_gilded,itm.vaegir_noble_fullhelm,
    itm.hera_vaegir_inf_shield_c,
    itm.great_lance,itm.weighted_morningstar,
    itm.vaegir_warhorse_c,
  ], new_lord_attrib, wp(150), knight_skills_2, 0x0000000a070c4387374bd19addd2a4ab00000000001e32cc0000000000000000, vaegir_face_old_2],
  ["knight_2_18", "Boyar Valishin", "Valishin", tf_hero, 0, reserved, fac.kingdom_2, [
    itm.hera_padded_cloth_b,itm.woolen_hose,
    itm.vaegir_scaled_cuirass,itm.splinted_leather_greaves,itm.scale_gauntlets_gilded,itm.vaegir_noble_fullhelm,
    itm.hera_vaegir_inf_shield_c,
    itm.great_lance,itm.weighted_morningstar,
    itm.vaegir_warhorse_c,
  ], new_lord_attrib, wp(180), knight_skills_3, 0x0000000b670012c23d9b6d4a92ada53500000000001cc1180000000000000000, vaegir_face_older_2],
  ["knight_2_19", "Boyar Rudin", "Rudin", tf_hero, 0, reserved, fac.kingdom_2, [
    itm.hera_tabard_b,itm.leather_boots,
    itm.vaegir_scaled_cuirass,itm.splinted_leather_greaves,itm.scale_gauntlets_gilded,itm.vaegir_noble_fullhelm,
    itm.hera_vaegir_inf_shield_c,
    itm.great_lance,itm.weighted_morningstar,
    itm.vaegir_warhorse_c,
  ], new_lord_attrib, wp(210), knight_skills_4|knows_trainer_4, 0x0000000e070050853b0a6e4994ae272a00000000001db4e10000000000000000, vaegir_face_older_2],
  ["knight_2_20", "Boyar Kumipa", "Kumipa", tf_hero, 0, reserved, fac.kingdom_2, [
    itm.hera_padded_cloth_a,itm.woolen_hose,
    itm.vaegir_scaled_cuirass,itm.splinted_leather_greaves,itm.scale_gauntlets_gilded,itm.vaegir_noble_fullhelm,
    itm.hera_vaegir_inf_shield_c,
    itm.great_lance,itm.weighted_morningstar,
    itm.vaegir_warhorse_c,
  ], new_lord_attrib, wp(240), knight_skills_5|knows_trainer_5, 0x0000000f800021c63b0a6e4994ae272a00000000001db4e10000000000000000, vaegir_face_older_2],

  #khergit civilian clothes: itm.leather_vest,itm.nomad_vest,itm.nomad_robe,itm.lamellar_vest,itm.tribal_warrior_outfit,
  ["knight_3_1", "Alagur Noyan", "Alagur", tf_hero, 0, reserved, fac.kingdom_3, [
    itm.hera_leather_vest,itm.nomad_boots,
    itm.tarkhan_lamellar,itm.tarkhan_boots,itm.khergit_noble_helm,
    itm.khergit_noble_shield,
    itm.hafted_blade_a,itm.khergit_sword_two_handed_b,
    itm.khergit_charger_c,
  ], new_lord_attrib, wp(130), knight_skills_1|knows_trainer_3|knows_power_draw_4, 0x000000043000318b54b246b7094dc39c00000000001d31270000000000000000, khergit_face_middle_2],
  ["knight_3_2", "Tonju Noyan", "Tonju", tf_hero, 0, reserved, fac.kingdom_3, [
    itm.hera_tribal_warrior_outfit_a_new,itm.hide_boots,
    itm.tarkhan_lamellar,itm.tarkhan_boots,itm.khergit_noble_helm,
    itm.khergit_noble_shield,
    itm.khergit_bow_khe,itm.khergit_arrows_c,itm.khergit_sword_two_handed_b,
    itm.khergit_warhorse_c,
  ], new_lord_attrib, wp(160), knight_skills_2|knows_power_draw_4, 0x0000000c280461004929b334ad632aa200000000001e05120000000000000000, khergit_face_old_2],
  ["knight_3_3", "Belir Noyan", "Belir", tf_hero, 0, reserved, fac.kingdom_3, [
    itm.hera_tribal_warrior_outfit_a_new,itm.nomad_boots,
    itm.tarkhan_lamellar,itm.tarkhan_boots,itm.khergit_noble_helm,
    itm.khergit_noble_shield,
    itm.khergit_lance_b,itm.khergit_sword_two_handed_b,
    itm.khergit_warhorse_c,
  ], new_lord_attrib, wp(190), knight_skills_3|knows_trainer_5|knows_power_draw_4, 0x0000000e880062c53b0a6e4994ae272a00000000001db4e10000000000000000, khergit_face_older_2],
  ["knight_3_4", "Asugan Noyan", "Asugan", tf_hero, 0, reserved, fac.kingdom_3, [
    itm.hera_tribal_warrior_outfit_a_new,itm.hide_boots,
    itm.tarkhan_lamellar,itm.tarkhan_boots,itm.scale_gauntlets_gilded,itm.khergit_noble_helm,
    itm.khergit_noble_shield,
    itm.hafted_blade_a,itm.khergit_sword_two_handed_b,
    itm.khergit_charger_c,
  ], new_lord_attrib, wp(220), knight_skills_4|knows_power_draw_4, 0x0000000c23085386391b5ac72a96d95c00000000001e37230000000000000000, khergit_face_older_2],
  ["knight_3_5", "Brula Noyan", "Brula", tf_hero, 0, reserved, fac.kingdom_3, [
    itm.hera_tribal_warrior_outfit_a_new,itm.hide_boots,
    itm.tarkhan_lamellar,itm.tarkhan_boots,itm.scale_gauntlets_gilded,itm.khergit_noble_helm,
    itm.khergit_noble_shield,
    itm.khergit_bow_khe,itm.khergit_arrows_c,itm.khergit_sword_two_handed_b,
    itm.khergit_charger_c,
  ], new_lord_attrib, wp(250), knight_skills_5|knows_power_draw_4, 0x0000000efe0051ca4b377b4964b6eb6500000000001f696c0000000000000000, khergit_face_older_2],
  ["knight_3_6", "Imirza Noyan", "Imirza", tf_hero, 0, reserved, fac.kingdom_3, [
    itm.hera_tribal_warrior_outfit_a_new,itm.hide_boots,
    itm.tarkhan_lamellar,itm.tarkhan_boots,itm.scale_gauntlets_gilded,itm.khergit_noble_helm,
    itm.khergit_noble_shield,
    itm.hafted_blade_a,itm.khergit_sword_two_handed_b,
    itm.khergit_charger_c,
  ], new_lord_attrib, wp(130), knight_skills_1|knows_power_draw_4, 0x00000006f600418b54b246b7094dc31a00000000001d37270000000000000000, khergit_face_middle_2],
  ["knight_3_7", "Urumuda Noyan", "Urumuda", tf_hero, 0, reserved, fac.kingdom_3, [
    itm.hera_leather_vest,itm.leather_boots,
    itm.tarkhan_lamellar,itm.tarkhan_boots,itm.scale_gauntlets_gilded,itm.khergit_noble_helm,
    itm.khergit_noble_shield,
    itm.khergit_lance_b,itm.khergit_sword_two_handed_b,
    itm.khergit_warhorse_c,
  ], new_lord_attrib, wp(160), knight_skills_2|knows_power_draw_4, 0x0000000bdd00510a44be2d14d370c65c00000000001ed6df0000000000000000, khergit_face_old_2],
  ["knight_3_8", "Kramuk Noyan", "Kramuk", tf_hero, 0, reserved, fac.kingdom_3, [
    itm.hera_tribal_warrior_outfit_a_new,itm.woolen_hose,
    itm.tarkhan_lamellar,itm.tarkhan_boots,itm.scale_gauntlets_gilded,itm.khergit_noble_helm,
    itm.khergit_noble_shield,
    itm.khergit_lance_b,itm.khergit_sword_two_handed_b,
    itm.khergit_warhorse_c,
  ], new_lord_attrib, wp(190), knight_skills_3|knows_power_draw_4, 0x0000000abc00518b5af4ab4b9c8e596400000000001dc76d0000000000000000, khergit_face_older_2],
  ["knight_3_9", "Chaurka Noyan", "Chaurka", tf_hero, 0, reserved, fac.kingdom_3, [
    itm.hera_tribal_warrior_outfit_a_new,itm.leather_boots,
    itm.tarkhan_lamellar,itm.tarkhan_boots,itm.scale_gauntlets_gilded,itm.khergit_noble_helm,
    itm.khergit_noble_shield,
    itm.khergit_bow_khe,itm.khergit_arrows_c,itm.khergit_sword_two_handed_b,
    itm.khergit_warhorse_c,
  ], new_lord_attrib, wp(220), knight_skills_4|knows_power_draw_4, 0x0000000a180441c921a30ea68b54971500000000001e54db0000000000000000, khergit_face_older_2],
  ["knight_3_10", "Sebula Noyan", "Sebula", tf_hero, 0, reserved, fac.kingdom_3, [
    itm.hera_tribal_warrior_outfit_a_new,itm.lamellar_armor,
    itm.tarkhan_lamellar,itm.tarkhan_boots,itm.scale_gauntlets_gilded,itm.khergit_noble_helm,
    itm.khergit_noble_shield,
    itm.khergit_bow_khe,itm.khergit_arrows_c,itm.khergit_sword_two_handed_b,
    itm.khergit_warhorse_c,
  ], new_lord_attrib, wp(250), knight_skills_5|knows_trainer_6|knows_power_draw_4, 0x0000000a3b00418c5b36c686d920a76100000000001c436f0000000000000000, khergit_face_older_2],
  ["knight_3_11", "Tulug Noyan", "Tulug", tf_hero, 0, reserved, fac.kingdom_3, [
    itm.hera_leather_vest,itm.nomad_boots,
    itm.tarkhan_lamellar,itm.tarkhan_boots,itm.khergit_noble_helm,
    itm.khergit_noble_shield,
    itm.hafted_blade_a,itm.khergit_sword_two_handed_b,
    itm.khergit_charger_c,
  ], new_lord_attrib, wp(150), knight_skills_1|knows_power_draw_4, 0x00000007d100534b44962d14d370c65c00000000001ed6df0000000000000000, khergit_face_middle_2],
  ["knight_3_12", "Nasugei Noyan", "Nasugei", tf_hero, 0, reserved, fac.kingdom_3, [
    itm.hera_tribal_warrior_outfit_a_new,itm.hide_boots,
    itm.tarkhan_lamellar,itm.tarkhan_boots,itm.scale_gauntlets_gilded,itm.khergit_noble_helm,
    itm.khergit_noble_shield,
    itm.khergit_lance_b,itm.khergit_sword_two_handed_b,
    itm.khergit_warhorse_c,
  ], new_lord_attrib, wp(190), knight_skills_2|knows_power_draw_4, 0x0000000bf400610c5b33d3c9258edb6c00000000001eb96d0000000000000000, khergit_face_old_2],
  ["knight_3_13", "Urubay Noyan", "Urubay", tf_hero, 0, reserved, fac.kingdom_3, [
    itm.hera_tribal_warrior_outfit_a_new,itm.nomad_boots,
    itm.tarkhan_lamellar,itm.tarkhan_boots,itm.khergit_noble_helm,
    itm.khergit_noble_shield,
    itm.khergit_lance_b,itm.khergit_sword_two_handed_b,
    itm.khergit_warhorse_c,
  ], new_lord_attrib, wp(200), knight_skills_3|knows_trainer_3|knows_power_draw_4, 0x0000000bfd0061c65b6eb33b25d2591d00000000001f58eb0000000000000000, khergit_face_older_2],
  ["knight_3_14", "Hugu Noyan", "Hugu", tf_hero, 0, reserved, fac.kingdom_3, [
    itm.hera_tribal_warrior_outfit_a_new,itm.hide_boots,
    itm.tarkhan_lamellar,itm.tarkhan_boots,itm.khergit_noble_helm,
    itm.khergit_noble_shield,
    itm.khergit_bow_khe,itm.khergit_arrows_c,itm.khergit_sword_two_handed_b,
    itm.khergit_warhorse_c,
  ], new_lord_attrib, wp(300), knight_skills_4|knows_trainer_6|knows_power_draw_4, 0x0000000b6900514144be2d14d370c65c00000000001ed6df0000000000000000, khergit_face_older_2],
  ["knight_3_15", "Tansugai Noyan", "Tansugai", tf_hero, 0, reserved, fac.kingdom_3, [
    itm.hera_tribal_warrior_outfit_a_new,itm.hide_boots,
    itm.tarkhan_lamellar,itm.tarkhan_boots,itm.scale_gauntlets_gilded,itm.khergit_noble_helm,
    itm.khergit_noble_shield,
    itm.hafted_blade_a,itm.khergit_sword_two_handed_b,
    itm.khergit_charger_c,
  ], new_lord_attrib, wp(240), knight_skills_5|knows_trainer_4|knows_power_draw_4, 0x0000000c360c524b6454465b59b9d93500000000001ea4860000000000000000, khergit_face_older_2],
  ["knight_3_16", "Tirida Noyan", "Tirida", tf_hero, 0, reserved, fac.kingdom_3, [
    itm.hera_tribal_warrior_outfit_a_new,itm.hide_boots,
    itm.tarkhan_lamellar,itm.tarkhan_boots,itm.khergit_noble_helm,
    itm.khergit_noble_shield,
    itm.khergit_lance_b,itm.khergit_sword_two_handed_b,
    itm.khergit_charger_c,
  ], new_lord_attrib, wp(120), knight_skills_1|knows_power_draw_4, 0x0000000c350c418438ab85b75c61b8d300000000001d21530000000000000000, khergit_face_middle_2],
  ["knight_3_17", "Ulusamai Noyan", "Ulusamai", tf_hero, 0, reserved, fac.kingdom_3, [
    itm.hera_leather_vest,itm.leather_boots,
    itm.tarkhan_lamellar,itm.tarkhan_boots,itm.khergit_noble_helm,
    itm.khergit_noble_shield,
    itm.khergit_bow_khe,itm.khergit_arrows_c,itm.khergit_sword_two_handed_b,
    itm.khergit_warhorse_c,
  ], new_lord_attrib, wp(150), knight_skills_2|knows_power_draw_4, 0x0000000c3c0821c647264ab6e68dc4d500000000001e42590000000000000000, khergit_face_old_2],
  ["knight_3_18", "Karaban Noyan", "Karaban", tf_hero, 0, reserved, fac.kingdom_3, [
    itm.hera_tribal_warrior_outfit_a_new,itm.hide_boots,
    itm.tarkhan_lamellar,itm.tarkhan_boots,itm.khergit_noble_helm,
    itm.khergit_noble_shield,
    itm.hafted_blade_a,itm.khergit_sword_two_handed_b,
    itm.khergit_charger_c,
  ], new_lord_attrib, wp(180), knight_skills_3|knows_trainer_4|knows_power_draw_4, 0x0000000c0810500347ae7acd0d3ad74a00000000001e289a0000000000000000, khergit_face_older_2],
  ["knight_3_19", "Akadan Noyan", "Akadan", tf_hero, 0, reserved, fac.kingdom_3, [
    itm.hera_tribal_warrior_outfit_a_new,itm.leather_boots,
    itm.tarkhan_lamellar,itm.tarkhan_boots,itm.scale_gauntlets_gilded,itm.khergit_noble_helm,
    itm.khergit_noble_shield,
    itm.khergit_lance_b,itm.khergit_sword_two_handed_b,
    itm.khergit_warhorse_c,
  ], new_lord_attrib, wp(210), knight_skills_4|knows_trainer_5|knows_power_draw_4, 0x0000000c1500510528f50d52d20b152300000000001d66db0000000000000000, khergit_face_older_2],
  ["knight_3_20", "Dundush Noyan", "Dundush", tf_hero, 0, reserved, fac.kingdom_3, [
    itm.hera_tribal_warrior_outfit_a_new,itm.hide_boots,
    itm.tarkhan_lamellar,itm.tarkhan_boots,itm.khergit_noble_helm,
    itm.khergit_noble_shield,
    itm.hafted_blade_a,itm.khergit_sword_two_handed_b,
    itm.khergit_warhorse_c,
  ], new_lord_attrib, wp(240), knight_skills_5|knows_power_draw_4, 0x0000000f7800620d66b76edd5cd5eb6e00000000001f691e0000000000000000, khergit_face_older_2],

  ["knight_4_1", "Jarl Aedin", "Aedin", tf_hero, 0, reserved, fac.kingdom_4, [                 
    itm.hera_leather_vest,itm.woolen_hose,
    itm.nordic_noble_armor_3,itm.splinted_leather_greaves,itm.gauntlets,itm.nordic_noble_helm,
    itm.nord_round_shield_c3,
    itm.nordic_axe_c,
  ], jarl_attrib, wp(130), knight_skills_1, 0x0000000c13002254340eb1d91159392d00000000001eb75a0000000000000000, nord_face_middle_2],
  ["knight_4_2", "Jarl Irya", "Irya", tf_hero, 0, reserved, fac.kingdom_4, [                   
    itm.hera_rich_tunic_a,itm.blue_hose,
    itm.nordic_noble_armor_3,itm.splinted_leather_greaves,itm.gauntlets,itm.nordic_noble_helm,
    itm.nord_round_shield_c1,
    itm.nordic_axe_c,
  ], jarl_attrib, wp(160), knight_skills_2|knows_trainer_3, 0x0000000c1610218368e29744e9a5985b00000000001db2a10000000000000000, nord_face_old_2],
  ["knight_4_3", "Jarl Olaf", "Olaf", tf_hero, 0, reserved, fac.kingdom_4, [
    itm.hera_leather_vest,itm.nomad_boots,
    itm.nordic_noble_armor_3,itm.splinted_leather_greaves,itm.gauntlets,itm.nordic_noble_helm,
    itm.nord_round_shield_c2,
    itm.great_lance,itm.sword_viking_c_long,
    itm.nordic_warhorse_b,
  ], jarl_attrib, wp(190), knight_skills_3, 0x0000000c03040289245a314b744b30a400000000001eb2a90000000000000000, nord_face_older_2],
  ["knight_4_4", "Jarl Reamald", "Reamald", tf_hero, 0, reserved, fac.kingdom_4, [
    itm.hera_leather_vest,itm.woolen_hose,
    itm.nordic_noble_armor_3,itm.splinted_leather_greaves,itm.gauntlets,itm.nordic_noble_helm,
    itm.nord_round_shield_c1,
    itm.great_lance,itm.sword_viking_c_long,
    itm.nordic_warhorse_b,
  ], jarl_attrib, wp(210), knight_skills_4, 0x0000000c3f1001ca3d6955b26a8939a300000000001e39b60000000000000000, nord_face_older_2],
  ["knight_4_5", "Jarl Turya", "Turya", tf_hero, 0, reserved, fac.kingdom_4, [                 
    itm.hera_leather_vest,itm.leather_boots,
    itm.nordic_noble_armor_3,itm.splinted_leather_greaves,itm.gauntlets,itm.nordic_noble_helm,
    itm.nord_round_shield_c3,
    itm.nordic_axe_c,
  ], jarl_attrib, wp(250), knight_skills_5, 0x0000000ff508330546dc4a59422d450c00000000001e51340000000000000000, nord_face_older_2],
  ["knight_4_6", "Jarl Gundur", "Gundur", tf_hero, 0, reserved, fac.kingdom_4, [               
    itm.hera_leather_vest,itm.nomad_boots,
    itm.nordic_noble_armor_3,itm.splinted_leather_greaves,itm.gauntlets,itm.nordic_noble_helm,
    itm.nord_round_shield_c3,
    itm.nordic_axe_c,
  ], jarl_attrib, wp(130), knight_skills_1, 0x00000005b00011813d9b6d4a92ada53500000000001cc1180000000000000000, nord_face_middle_2],
  ["knight_4_7", "Jarl Harald", "Harald", tf_hero, 0, reserved, fac.kingdom_4, [               
    itm.hera_leather_vest,itm.nomad_boots,
    itm.nordic_noble_armor_3,itm.splinted_leather_greaves,itm.gauntlets,itm.nordic_noble_helm,
    itm.nord_round_shield_c2,
    itm.nordic_axe_c,
  ], jarl_attrib, wp(160), knight_skills_2|knows_trainer_4, 0x00000006690002873d9b6d4a92ada53500000000001cc1180000000000000000, nord_face_old_2],
  ["knight_4_8", "Jarl Knudarr", "Knudarr", tf_hero, 0, reserved, fac.kingdom_4, [             
    itm.hera_leather_vest,itm.woolen_hose,
    itm.nordic_noble_armor_3,itm.splinted_leather_greaves,itm.gauntlets,itm.nordic_noble_helm,
    itm.nord_round_shield_c1,
    itm.nordic_axe_c,
  ], jarl_attrib, wp(190), knight_skills_3, 0x0000000f830051c53b026e4994ae272a00000000001db4e10000000000000000, nord_face_older_2],
  ["knight_4_9", "Jarl Haeda", "Haeda", tf_hero, 0, reserved, fac.kingdom_4, [
    itm.hera_leather_vest,itm.blue_hose,
    itm.nordic_noble_armor_3,itm.splinted_leather_greaves,itm.gauntlets,itm.nordic_noble_helm,
    itm.nord_round_shield_c2,
    itm.great_lance,itm.sword_viking_c_long,
    itm.nordic_warhorse_b,
  ], jarl_attrib, wp(220), knight_skills_4|knows_trainer_5|knows_power_draw_4, 0x00000000080c54c1345bd21349b1b67300000000001c90c80000000000000000, nord_face_older_2],
  ["knight_4_10", "Jarl Turegor", "Turegor", tf_hero, 0, reserved, fac.kingdom_4, [
    itm.hera_leather_vest,itm.nomad_boots,
    itm.nordic_noble_armor_3,itm.splinted_leather_greaves,itm.gauntlets,itm.nordic_noble_helm,
    itm.nord_round_shield_c3,
    itm.great_lance,itm.sword_viking_c_long,
    itm.nordic_warhorse_b,
  ], jarl_attrib, wp(250), knight_skills_5|knows_trainer_6, 0x000000084b0002063d9b6d4a92ada53500000000001cc1180000000000000000, nord_face_older_2],
  ["knight_4_11", "Jarl Logarson", "Logarson", tf_hero, 0, reserved, fac.kingdom_4, [          
    itm.hera_leather_vest,itm.woolen_hose,
    itm.nordic_noble_armor_3,itm.splinted_leather_greaves,itm.gauntlets,itm.nordic_noble_helm,
    itm.nord_round_shield_c1,
    itm.nordic_axe_c,
  ], jarl_attrib, wp(140), knight_skills_1, 0x000000002d100005471d4ae69ccacb1d00000000001dca550000000000000000, nord_face_middle_2],
  ["knight_4_12", "Jarl Aeric", "Aeric", tf_hero, 0, reserved, fac.kingdom_4, [                
    itm.hera_rich_tunic_a,itm.blue_hose,
    itm.nordic_noble_armor_3,itm.splinted_leather_greaves,itm.gauntlets,itm.nordic_noble_helm,
    itm.nord_round_shield_c1,
    itm.nordic_axe_c,
  ], jarl_attrib, wp(200), knight_skills_2, 0x0000000b9500020824936cc51cb5bb2500000000001dd4d80000000000000000, nord_face_old_2],
  ["knight_4_13", "Jarl Faarn", "Faarn", tf_hero, 0, reserved, fac.kingdom_4, [
    itm.hera_leather_vest,itm.nomad_boots,
    itm.nordic_noble_armor_3,itm.splinted_leather_greaves,itm.gauntlets,itm.nordic_noble_helm,
    itm.nord_round_shield_c3,
    itm.great_lance,itm.sword_viking_c_long,
    itm.nordic_warhorse_b,
  ], jarl_attrib, wp(250), knight_skills_3|knows_trainer_3, 0x0000000a300012c439233512e287391d00000000001db7200000000000000000, nord_face_older_2],
  ["knight_4_14", "Jarl Bulba", "Bulba", tf_hero, 0, reserved, fac.kingdom_4, [                
    itm.hera_leather_vest,itm.woolen_hose,
    itm.nordic_noble_armor_3,itm.splinted_leather_greaves,itm.gauntlets,itm.nordic_noble_helm,
    itm.nord_round_shield_c2,
    itm.nordic_axe_c,
  ], jarl_attrib, wp(200), knight_skills_4, 0x0000000c0700414f2cb6aa36ea50a69d00000000001dc55c0000000000000000, nord_face_older_2],
  ["knight_4_15", "Jarl Rayeck", "Rayeck", tf_hero, 0, reserved, fac.kingdom_4, [
    itm.hera_leather_vest,itm.leather_boots,
    itm.nordic_noble_armor_3,itm.splinted_leather_greaves,itm.gauntlets,itm.nordic_noble_helm,
    itm.nord_round_shield_c1,
    itm.great_lance,itm.sword_viking_c_long,
    itm.nordic_warhorse_b,
  ], jarl_attrib, wp(290), knight_skills_5|knows_trainer_6, 0x0000000d920801831715d1aa9221372300000000001ec6630000000000000000, nord_face_older_2],
  ["knight_4_16", "Jarl Dirigun", "Dirigun", tf_hero, 0, reserved, fac.kingdom_4, [            
    itm.hera_leather_vest,itm.nomad_boots,
    itm.nordic_noble_armor_3,itm.splinted_leather_greaves,itm.gauntlets,itm.nordic_noble_helm,
    itm.nord_round_shield_c1,
    itm.nordic_axe_c,
  ], jarl_attrib, wp(120), knight_skills_1, 0x000000099700124239233512e287391d00000000001db7200000000000000000, nord_face_middle_2],
  ["knight_4_17", "Jarl Marayirr", "Marayirr", tf_hero, 0, reserved, fac.kingdom_4, [          
    itm.hera_leather_vest,itm.nomad_boots,
    itm.nordic_noble_armor_3,itm.splinted_leather_greaves,itm.gauntlets,itm.nordic_noble_helm,
    itm.nord_round_shield_c2,
    itm.nordic_axe_c,
  ], jarl_attrib, wp(150), knight_skills_2|knows_trainer_4, 0x0000000c2f0442036d232a2324b5b81400000000001e55630000000000000000, nord_face_old_2],
  ["knight_4_18", "Jarl Gearth", "Gearth", tf_hero, 0, reserved, fac.kingdom_4, [              
    itm.hera_leather_vest,itm.woolen_hose,
    itm.nordic_noble_armor_3,itm.splinted_leather_greaves,itm.gauntlets,itm.nordic_noble_helm,
    itm.nord_round_shield_c1,
    itm.nordic_axe_c,
  ], jarl_attrib, wp(180), knight_skills_3, 0x0000000c0d00118866e22e3d9735a72600000000001eacad0000000000000000, nord_face_older_2],
  ["knight_4_19", "Jarl Surdun", "Surdun", tf_hero, 0, reserved, fac.kingdom_4, [
    itm.hera_leather_vest,itm.blue_hose,
    itm.nordic_noble_armor_3,itm.splinted_leather_greaves,itm.gauntlets,itm.nordic_noble_helm,
    itm.nord_round_shield_c3,
    itm.great_lance,itm.sword_viking_c_long,
    itm.nordic_warhorse_b,
  ], jarl_attrib, wp(210), knight_skills_4|knows_trainer_5, 0x0000000c0308225124e26d4a6295965a00000000001d23e40000000000000000, nord_face_older_2],
  ["knight_4_20", "Jarl Gerlad", "Gerlad", tf_hero, 0, reserved, fac.kingdom_4, [
    itm.hera_leather_vest,itm.nomad_boots,
    itm.nordic_noble_armor_3,itm.splinted_leather_greaves,itm.gauntlets,itm.nordic_noble_helm,
    itm.nord_round_shield_c3,
    itm.great_lance,itm.sword_viking_c_long,
    itm.nordic_warhorse_b,
  ], jarl_attrib, wp(240), knight_skills_5, 0x0000000f630052813b6bb36de5d6eb7400000000001dd72c0000000000000000, nord_face_older_2],

  ["knight_5_1", "Count Matheas", "Matheas", tf_hero, 0, reserved, fac.kingdom_5, [
    itm.hera_tabard_b,itm.leather_boots,
    itm.rhodok_corrazine_a,itm.plate_boots,itm.ornate_gauntlets,itm.rhodok_visored_sallet,
    itm.hera_rhodok_pavise_c,
    itm.great_lance,itm.battle_cleaver,
    itm.rhodok_warhorse_c,
  ], new_lord_attrib, wp(130), knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_5_2", "Count Gutlans", "Gutlans", tf_hero, 0, reserved, fac.kingdom_5, [
    itm.hera_padded_cloth_a,itm.leather_boots,
    itm.rhodok_corrazine_c,itm.plate_boots,itm.ornate_gauntlets,itm.rhodok_visored_sallet,
    itm.hera_rhodok_pavise_c,
    itm.great_lance,itm.battle_cleaver,
    itm.rhodok_warhorse_c,
  ], new_lord_attrib, wp(160), knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_5_3", "Count Laruqen", "Laruqen", tf_hero, 0, reserved, fac.kingdom_5, [
    itm.hera_rich_tunic_a,itm.nomad_boots,
    itm.rhodok_corrazine_b,itm.plate_boots,itm.ornate_gauntlets,itm.rhodok_visored_sallet,
    itm.hera_rhodok_pavise_c,
    itm.great_lance,itm.battle_cleaver,
    itm.rhodok_warhorse_c,
  ], new_lord_attrib, wp(190), knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_5_4", "Count Raichs", "Raichs", tf_hero, 0, reserved, fac.kingdom_5, [
    itm.hera_leather_vest,itm.woolen_hose,
    itm.rhodok_corrazine_a,itm.plate_boots,itm.ornate_gauntlets,itm.rhodok_visored_sallet,
    itm.hera_rhodok_pavise_c,
    itm.great_lance,itm.battle_cleaver,
    itm.rhodok_warhorse_c,
  ], new_lord_attrib, wp(220), knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_5_5", "Count Reland", "Reland", tf_hero, 0, reserved, fac.kingdom_5, [
    itm.hera_rich_tunic_a,itm.leather_boots,
    itm.rhodok_corrazine_c,itm.plate_boots,itm.ornate_gauntlets,itm.rhodok_visored_sallet,
    itm.hera_rhodok_pavise_c,
    itm.great_lance,itm.battle_cleaver,
    itm.rhodok_warhorse_c,
  ], new_lord_attrib, wp(250), knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_5_6", "Count Tarchias", "Tarchias", tf_hero, 0, reserved, fac.kingdom_5, [
    itm.hera_rich_tunic_a,itm.woolen_hose,
    itm.rhodok_corrazine_a,itm.plate_boots,itm.ornate_gauntlets,itm.rhodok_visored_sallet,
    itm.hera_rhodok_pavise_c,
    itm.great_lance,itm.battle_cleaver,
    itm.rhodok_warhorse_c,
  ], new_lord_attrib, wp(130), knight_skills_1, 0x000000001100000648d24d36cd964b1d00000000001e2dac0000000000000000, rhodok_face_middle_2],
  ["knight_5_7", "Count Gharmall", "Gharmall", tf_hero, 0, reserved, fac.kingdom_5, [
    itm.hera_rich_tunic_a,itm.leather_boots,
    itm.rhodok_corrazine_b,itm.plate_boots,itm.ornate_gauntlets,itm.rhodok_visored_sallet,
    itm.hera_rhodok_pavise_c,
    itm.great_lance,itm.battle_cleaver,
    itm.rhodok_warhorse_c,
  ], new_lord_attrib, wp(160), knight_skills_2, 0x0000000c3a0455c443d46e4c8b91291a00000000001ca51b0000000000000000, rhodok_face_old_2],
  ["knight_5_8", "Count Talbar", "Talbar", tf_hero, 0, reserved, fac.kingdom_5, [
    itm.hera_rich_tunic_a,itm.woolen_hose,
    itm.rhodok_corrazine_b,itm.plate_boots,itm.ornate_gauntlets,itm.rhodok_visored_sallet,
    itm.hera_rhodok_pavise_c,
    itm.great_lance,itm.battle_cleaver,
    itm.rhodok_warhorse_c,
  ], new_lord_attrib, wp(190), knight_skills_3|knows_trainer_3, 0x0000000c2c0844d42914d19b2369b4ea00000000001e331b0000000000000000, rhodok_face_older_2],
  ["knight_5_9", "Count Rimusk", "Rimusk", tf_hero, 0, reserved, fac.kingdom_5, [
    itm.hera_leather_vest,itm.leather_boots,
    itm.rhodok_corrazine_a,itm.plate_boots,itm.ornate_gauntlets,itm.rhodok_visored_sallet,
    itm.hera_rhodok_pavise_c,
    itm.great_lance,itm.battle_cleaver,
    itm.rhodok_warhorse_c,
  ], new_lord_attrib, wp(220), knight_skills_4|knows_trainer_6, 0x00000000420430c32331b5551c4724a100000000001e39a40000000000000000, rhodok_face_older_2],
  ["knight_5_10", "Count Falsevor", "Falsevor", tf_hero, 0, reserved, fac.kingdom_5, [
    itm.hera_rich_tunic_a,itm.blue_hose,
    itm.rhodok_corrazine_c,itm.plate_boots,itm.ornate_gauntlets,itm.rhodok_visored_sallet,
    itm.hera_rhodok_pavise_c,
    itm.great_lance,itm.battle_cleaver,
    itm.rhodok_warhorse_c,
  ], new_lord_attrib, wp(250), knight_skills_5|knows_trainer_4, 0x00000008e20011063d9b6d4a92ada53500000000001cc1180000000000000000, rhodok_face_older_2],
  ["knight_5_11", "Count Etrosq", "Etrosq", tf_hero, 0, reserved, fac.kingdom_5, [
    itm.hera_tabard_b,itm.leather_boots,
    itm.rhodok_corrazine_c,itm.plate_boots,itm.ornate_gauntlets,itm.rhodok_visored_sallet,
    itm.hera_rhodok_pavise_c,
    itm.great_lance,itm.battle_cleaver,
    itm.rhodok_warhorse_c,
  ], new_lord_attrib, wp(130), knight_skills_1, 0x0000000c170c14874752adb6eb3228d500000000001c955c0000000000000000, rhodok_face_middle_2],
  ["knight_5_12", "Count Kurnias", "Kurnias", tf_hero, 0, reserved, fac.kingdom_5, [
    itm.hera_padded_cloth_b,itm.leather_boots,
    itm.rhodok_corrazine_c,itm.plate_boots,itm.ornate_gauntlets,itm.rhodok_visored_sallet,
    itm.hera_rhodok_pavise_c,
    itm.great_lance,itm.battle_cleaver,
    itm.rhodok_warhorse_c,
  ], new_lord_attrib, wp(160), knight_skills_2|knows_trainer_5, 0x0000000c080c13d056ec8da85e3126ed00000000001d4ce60000000000000000, rhodok_face_old_2],
  ["knight_5_13", "Count Tellrog", "Tellrog", tf_hero, 0, reserved, fac.kingdom_5, [
    itm.hera_rich_tunic_a,itm.nomad_boots,
    itm.rhodok_corrazine_a,itm.plate_boots,itm.ornate_gauntlets,itm.rhodok_visored_sallet,
    itm.hera_rhodok_pavise_c,
    itm.great_lance,itm.battle_cleaver,
    itm.rhodok_warhorse_c,
  ], new_lord_attrib, wp(190), knight_skills_3, 0x0000000cbf10100562a4954ae731588a00000000001d6b530000000000000000, rhodok_face_older_2],
  ["knight_5_14", "Count Tribidan", "Tribidan", tf_hero, 0, reserved, fac.kingdom_5, [
    itm.hera_leather_vest,itm.woolen_hose,
    itm.rhodok_corrazine_b,itm.plate_boots,itm.ornate_gauntlets,itm.rhodok_visored_sallet,
    itm.hera_rhodok_pavise_c,
    itm.great_lance,itm.battle_cleaver,
    itm.rhodok_warhorse_c,
  ], new_lord_attrib, wp(220), knight_skills_4, 0x0000000c330805823baa77556c4e331a00000000001cb9110000000000000000, rhodok_face_older_2],
  ["knight_5_15", "Count Gerluchs", "Gerluchs", tf_hero, 0, reserved, fac.kingdom_5, [
    itm.hera_rich_tunic_a,itm.leather_boots,
    itm.rhodok_corrazine_a,itm.plate_boots,itm.ornate_gauntlets,itm.rhodok_visored_sallet,
    itm.hera_rhodok_pavise_c,
    itm.great_lance,itm.battle_cleaver,
    itm.rhodok_warhorse_c,
  ], new_lord_attrib, wp(250), knight_skills_5, 0x0000000d51000106370c4d4732b536de00000000001db9280000000000000000, rhodok_face_older_2],
  ["knight_5_16", "Count Fudreim", "Fudreim", tf_hero, 0, reserved, fac.kingdom_5, [
    itm.hera_rich_tunic_a,itm.woolen_hose,
    itm.rhodok_corrazine_b,itm.plate_boots,itm.ornate_gauntlets,itm.rhodok_visored_sallet,
    itm.hera_rhodok_pavise_c,
    itm.great_lance,itm.battle_cleaver,
    itm.rhodok_warhorse_c,
  ], new_lord_attrib, wp(120), knight_skills_1, 0x0000000c06046151435b5122a37756a400000000001c46e50000000000000000, rhodok_face_middle_2],
  ["knight_5_17", "Count Nealcha", "Nealcha", tf_hero, 0, reserved, fac.kingdom_5, [
    itm.hera_rich_tunic_a,itm.leather_boots,
    itm.rhodok_corrazine_c,itm.plate_boots,itm.ornate_gauntlets,itm.rhodok_visored_sallet,
    itm.hera_rhodok_pavise_c,
    itm.great_lance,itm.battle_cleaver,
    itm.rhodok_warhorse_c,
  ], new_lord_attrib, wp(150), knight_skills_2, 0x0000000c081001d3465c89a6a452356300000000001cda550000000000000000, rhodok_face_old_2],
  ["knight_5_18", "Count Fraichin", "Fraichin", tf_hero, 0, reserved, fac.kingdom_5, [
    itm.hera_rich_tunic_a,itm.woolen_hose,
    itm.rhodok_corrazine_a,itm.plate_boots,itm.ornate_gauntlets,itm.rhodok_visored_sallet,
    itm.hera_rhodok_pavise_c,
    itm.great_lance,itm.battle_cleaver,
    itm.rhodok_warhorse_c,
  ], new_lord_attrib, wp(180), knight_skills_3, 0x0000000a3d0c13c3452aa967276dc95c00000000001dad350000000000000000, rhodok_face_older_2],
  ["knight_5_19", "Count Trimbau", "Trimbau", tf_hero, 0, reserved, fac.kingdom_5, [
    itm.hera_leather_vest,itm.leather_boots,
    itm.rhodok_corrazine_a,itm.plate_boots,itm.ornate_gauntlets,itm.rhodok_visored_sallet,
    itm.hera_rhodok_pavise_c,
    itm.great_lance,itm.battle_cleaver,
    itm.rhodok_warhorse_c,
  ], new_lord_attrib, wp(210), knight_skills_4|knows_trainer_5, 0x0000000038043194092ab4b2d9adb44c00000000001e072c0000000000000000, rhodok_face_older_2],
  ["knight_5_20", "Count Reichsin", "Reichsin", tf_hero, 0, reserved, fac.kingdom_5, [
    itm.hera_rich_tunic_a,itm.blue_hose,
    itm.rhodok_corrazine_c,itm.plate_boots,itm.ornate_gauntlets,itm.rhodok_visored_sallet,
    itm.hera_rhodok_pavise_c,
    itm.great_lance,itm.battle_cleaver,
    itm.rhodok_warhorse_c,
  ], new_lord_attrib, wp(240), knight_skills_5|knows_trainer_6, 0x000000003600420515a865b45c64d64c00000000001d544b0000000000000000, rhodok_face_older_2],

  ["knight_6_1", "Emir Uqais", "Uqais", tf_hero, 0, reserved, fac.kingdom_6, [
    itm.hera_archers_vest,itm.sarranid_boots_c,
    itm.vaegir_elite_armor,itm.sarranid_boots_c,itm.scale_gauntlets_gilded,itm.sarranid_veiled_helmet,
    itm.hera_sarranid_small_shield_c,
    itm.sarranid_lance_c,itm.sarranid_warblade,
    itm.sarranid_warhorse_c,
  ], new_lord_attrib, wp(130), knight_skills_1|knows_trainer_3, 0x00000000600c2084486195383349eae500000000001d16a30000000000000000, rhodok_face_middle_2],
  ["knight_6_2", "Emir Hamezan", "Hamezan", tf_hero, 0, reserved, fac.kingdom_6, [
    itm.hera_archers_vest,itm.sarranid_boots_c,
    itm.vaegir_elite_armor,itm.sarranid_boots_c,itm.scale_gauntlets_gilded,itm.sarranid_veiled_helmet,
    itm.hera_sarranid_small_shield_c,
    itm.sarranid_lance_c,itm.sarranid_warblade,
    itm.sarranid_warhorse_c,
  ], new_lord_attrib, wp(160), knight_skills_2|knows_trainer_4, 0x00000001380825d444cb68b92b8d3b1d00000000001dd71e0000000000000000, rhodok_face_old_2],
  ["knight_6_3", "Emir Atis", "Atis", tf_hero, 0, reserved, fac.kingdom_6, [
    itm.hera_sarranid_leather_armor,itm.nomad_boots,
    itm.vaegir_elite_armor,itm.sarranid_boots_c,itm.scale_gauntlets_gilded,itm.sarranid_veiled_helmet,
    itm.hera_sarranid_small_shield_c,
    itm.sarranid_lance_c,itm.sarranid_warblade,
    itm.sarranid_warhorse_c,
  ], new_lord_attrib, wp(190), knight_skills_3, 0x000000002208428579723147247ad4e500000000001f14d40000000000000000, rhodok_face_older_2],
  ["knight_6_4", "Emir Nuwas", "Nuwas", tf_hero, 0, reserved, fac.kingdom_6, [
    itm.hera_sarranid_leather_armor,itm.sarranid_boots_c,
    itm.vaegir_elite_armor,itm.sarranid_boots_c,itm.scale_gauntlets_gilded,itm.sarranid_veiled_helmet,
    itm.hera_sarranid_small_shield_c,
    itm.sarranid_lance_c,itm.sarranid_warblade,
    itm.sarranid_warhorse_c,
  ], new_lord_attrib, wp(220), knight_skills_4, 0x00000009bf084285050caa7d285be51a00000000001d11010000000000000000, rhodok_face_older_2],
  ["knight_6_5", "Emir Mundhalir", "Mundhalir", tf_hero, 0, reserved, fac.kingdom_6, [
    itm.hera_archers_vest,itm.sarranid_boots_c,
    itm.vaegir_elite_armor,itm.sarranid_boots_c,itm.scale_gauntlets_gilded,itm.sarranid_veiled_helmet,
    itm.hera_sarranid_small_shield_c,
    itm.sarranid_lance_c,itm.sarranid_warblade,
    itm.sarranid_warhorse_c,
  ], new_lord_attrib, wp(250), knight_skills_5, 0x000000002a084003330175aae175da9c00000000001e02150000000000000000, rhodok_face_older_2],
  ["knight_6_6", "Emir Ghanawa", "Ghanawa", tf_hero, 0, reserved, fac.kingdom_6, [
    itm.hera_archers_vest,itm.sarranid_boots_c,
    itm.vaegir_elite_armor,itm.sarranid_boots_c,itm.scale_gauntlets_gilded,itm.sarranid_veiled_helmet,
    itm.hera_sarranid_small_shield_c,
    itm.sarranid_lance_c,itm.sarranid_warblade,
    itm.sarranid_warhorse_c,
  ], new_lord_attrib, wp(130), knight_skills_1, 0x00000001830043834733294c89b128e200000000001259510000000000000000, rhodok_face_middle_2],
  ["knight_6_7", "Emir Nuam", "Nuam", tf_hero, 0, reserved, fac.kingdom_6, [
    itm.hera_archers_vest,itm.sarranid_boots_c,
    itm.vaegir_elite_armor,itm.sarranid_boots_c,itm.scale_gauntlets_gilded,itm.sarranid_veiled_helmet,
    itm.hera_sarranid_small_shield_c,
    itm.sarranid_lance_c,itm.sarranid_warblade,
    itm.sarranid_warhorse_c,
  ], new_lord_attrib, wp(160), knight_skills_2, 0x0000000cbf10434020504bbbda9135d500000000001f62380000000000000000, rhodok_face_old_2],
  ["knight_6_8", "Emir Dhiyul", "Dhiyul", tf_hero, 0, reserved, fac.kingdom_6, [
    itm.hera_archers_vest,itm.sarranid_boots_c,
    itm.vaegir_elite_armor,itm.sarranid_boots_c,itm.scale_gauntlets_gilded,itm.sarranid_veiled_helmet,
    itm.hera_sarranid_small_shield_c,
    itm.sarranid_lance_c,itm.sarranid_warblade,
    itm.sarranid_warhorse_c,
  ], new_lord_attrib, wp(190), knight_skills_3|knows_trainer_3, 0x0000000190044003336dcd3ca2cacae300000000001f47640000000000000000, rhodok_face_older_2],
  ["knight_6_9", "Emir Lakhem", "Lakhem", tf_hero, 0, reserved, fac.kingdom_6, [
    itm.hera_sarranid_leather_armor,
    itm.vaegir_elite_armor,itm.sarranid_boots_c,itm.scale_gauntlets_gilded,itm.sarranid_veiled_helmet,
    itm.hera_sarranid_small_shield_c,
    itm.sarranid_lance_c,itm.sarranid_warblade,
    itm.sarranid_warhorse_c,
  ], new_lord_attrib, wp(220), knight_skills_4|knows_trainer_6, 0x0000000dde0040c4549dd5ca6f4dd56500000000001e291b0000000000000000, rhodok_face_older_2],
  ["knight_6_10", "Emir Ghulassen", "Ghulassen", tf_hero, 0, reserved, fac.kingdom_6, [
    itm.hera_archers_vest,itm.sarranid_boots_c,
    itm.vaegir_elite_armor,itm.sarranid_boots_c,itm.scale_gauntlets_gilded,itm.sarranid_veiled_helmet,
    itm.hera_sarranid_small_shield_c,
    itm.sarranid_lance_c,itm.sarranid_warblade,
    itm.sarranid_warhorse_c,
  ], new_lord_attrib, wp(250), knight_skills_5|knows_trainer_4, 0x00000001a60441c66ce99256b4ad4b3300000000001d392c0000000000000000, rhodok_face_older_2],
  ["knight_6_11", "Emir Azadun", "Azadun", tf_hero, 0, reserved, fac.kingdom_6, [
    itm.hera_sarranid_leather_armor,itm.sarranid_boots_c,
    itm.vaegir_elite_armor,itm.sarranid_boots_c,itm.scale_gauntlets_gilded,itm.sarranid_veiled_helmet,
    itm.hera_sarranid_small_shield_c,
    itm.sarranid_lance_c,itm.sarranid_warblade,
    itm.sarranid_warhorse_c,
  ], new_lord_attrib, wp(130), knight_skills_1, 0x0000000fff08134726c28af8dc96e4da00000000001e541d0000000000000000, rhodok_face_middle_2],
  ["knight_6_12", "Emir Quryas", "Quryas", tf_hero, 0, reserved, fac.kingdom_6, [
    itm.hera_archers_vest,itm.sarranid_boots_c,
    itm.vaegir_elite_armor,itm.sarranid_boots_c,itm.scale_gauntlets_gilded,itm.sarranid_veiled_helmet,
    itm.hera_sarranid_small_shield_c,
    itm.sarranid_lance_c,itm.sarranid_warblade,
    itm.sarranid_warhorse_c,
  ], new_lord_attrib, wp(160), knight_skills_2|knows_trainer_5, 0x0000000035104084635b74ba5491a7a400000000001e46d60000000000000000, rhodok_face_old_2],
  ["knight_6_13", "Emir Amdar", "Amdar", tf_hero, 0, reserved, fac.kingdom_6, [
    itm.hera_sarranid_leather_armor,itm.sarranid_boots_c,
    itm.vaegir_elite_armor,itm.sarranid_boots_c,itm.scale_gauntlets_gilded,itm.sarranid_veiled_helmet,
    itm.hera_sarranid_small_shield_c,
    itm.sarranid_lance_c,itm.sarranid_warblade,
    itm.sarranid_warhorse_c,
  ], new_lord_attrib, wp(190), knight_skills_3, 0x00000000001021435b734d4ad94eba9400000000001eb8eb0000000000000000, rhodok_face_older_2],
  ["knight_6_14", "Emir Hiwan", "Hiwan", tf_hero, 0, reserved, fac.kingdom_6, [
    itm.hera_archers_vest,itm.sarranid_boots_c,
    itm.vaegir_elite_armor,itm.sarranid_boots_c,itm.scale_gauntlets_gilded,itm.sarranid_veiled_helmet,
    itm.hera_sarranid_small_shield_c,
    itm.sarranid_lance_c,itm.sarranid_warblade,
    itm.sarranid_warhorse_c,
  ], new_lord_attrib, wp(220), knight_skills_4, 0x000000000c0c45c63a5b921ac22db8e200000000001cca530000000000000000, rhodok_face_older_2],
  ["knight_6_15", "Emir Muhnir", "Muhnir", tf_hero, 0, reserved, fac.kingdom_6, [
    itm.hera_sarranid_leather_armor,itm.sarranid_boots_c,
    itm.vaegir_elite_armor,itm.sarranid_boots_c,itm.scale_gauntlets_gilded,itm.sarranid_veiled_helmet,
    itm.hera_sarranid_small_shield_c,
    itm.sarranid_lance_c,itm.sarranid_warblade,
    itm.sarranid_warhorse_c,
  ], new_lord_attrib, wp(250), knight_skills_5, 0x000000001b0c4185369a6938cecde95600000000001f25210000000000000000, rhodok_face_older_2],
  ["knight_6_16", "Emir Ayyam", "Ayyam", tf_hero, 0, reserved, fac.kingdom_6, [
    itm.hera_sarranid_leather_armor,itm.sarranid_boots_c,
    itm.vaegir_elite_armor,itm.sarranid_boots_c,itm.scale_gauntlets_gilded,itm.sarranid_veiled_helmet,
    itm.hera_sarranid_small_shield_c,
    itm.sarranid_lance_c,itm.sarranid_warblade,
    itm.sarranid_warhorse_c,
  ], new_lord_attrib, wp(120), knight_skills_1, 0x00000007770841c80a01e1c5eb51ffff00000000001f12d80000000000000000, rhodok_face_middle_2],
  ["knight_6_17", "Emir Raddoun", "Raddoun", tf_hero, 0, reserved, fac.kingdom_6, [
    itm.hera_archers_vest,itm.sarranid_boots_c,
    itm.vaegir_elite_armor,itm.sarranid_boots_c,itm.scale_gauntlets_gilded,itm.sarranid_veiled_helmet,
    itm.hera_sarranid_small_shield_c,
    itm.sarranid_lance_c,itm.sarranid_warblade,
    itm.sarranid_warhorse_c,
  ], new_lord_attrib, wp(150), knight_skills_2, 0x000000007f0462c32419f47a1aba8bcf00000000001e7e090000000000000000, rhodok_face_old_2],
  ["knight_6_18", "Emir Tilimsan", "Tilimsan", tf_hero, 0, reserved, fac.kingdom_6, [
    itm.hera_sarranid_leather_armor,itm.sarranid_boots_c,
    itm.vaegir_elite_armor,itm.sarranid_boots_c,itm.scale_gauntlets_gilded,itm.sarranid_veiled_helmet,
    itm.hera_sarranid_small_shield_c,
    itm.sarranid_lance_c,itm.sarranid_warblade,
    itm.sarranid_warhorse_c,
  ], new_lord_attrib, wp(180), knight_skills_3, 0x000000003410410070d975caac91aca500000000001c27530000000000000000, rhodok_face_older_2],
  ["knight_6_19", "Emir Dhashwal", "Dhashwal", tf_hero, 0, reserved, fac.kingdom_6, [
    itm.hera_archers_vest,itm.sarranid_boots_c,
    itm.vaegir_elite_armor,itm.sarranid_boots_c,itm.scale_gauntlets_gilded,itm.sarranid_veiled_helmet,
    itm.hera_sarranid_small_shield_c,
    itm.sarranid_lance_c,itm.sarranid_warblade,
    itm.sarranid_warhorse_c,
  ], new_lord_attrib, wp(210), knight_skills_4|knows_trainer_5, 0x000000018a08618016ac36bc8b6e4a9900000000001dd45d0000000000000000, rhodok_face_older_2],
  ["knight_6_20", "Emir Biliya", "Biliya", tf_hero, 0, reserved, fac.kingdom_6, [
    itm.hera_archers_vest,itm.sarranid_boots_c,
    itm.vaegir_elite_armor,itm.sarranid_boots_c,itm.scale_gauntlets_gilded,itm.sarranid_veiled_helmet,
    itm.hera_sarranid_small_shield_c,
    itm.sarranid_lance_c,itm.sarranid_warblade,
    itm.sarranid_warhorse_c,
  ], new_lord_attrib, wp(240), knight_skills_5|knows_trainer_6, 0x00000001bd0040c0281a899ac956b94b00000000001ec8910000000000000000, rhodok_face_older_2],

  ["dark_knight_lord1", "Lord Purin", "Purin", tf_hero, 0, 0, fac.dark_knights, [
    itm.dk_helm_lord_a,itm.wb_dk_plate_boots,itm.dk_gauntlet,itm.dk_armor_lord,
    itm.hera_dk_cav_shield_c,
    itm.great_lance,itm.sword_medieval_d_long,
    itm.dk_charger,
  ], level(56)|str_30|agi_30|int_30|cha_30, wp(500), knows_lord_1|knows_ironflesh_10|knows_shield_10|knows_power_strike_10|knows_athletics_10|knows_riding_10|knows_tactics_7|knows_leadership_7, 0x00000001a410259144d5d1d6eb55e96a00000000001db0db0000000000000000],
  ["dark_knight_lord2", "Lord Grife", "Grife", tf_hero, 0, 0, fac.dark_knights, [
    itm.dk_helm_lord_b,itm.wb_dk_plate_boots,itm.dk_gauntlet,itm.dk_armor_lord,
    itm.hera_dk_cav_shield_c,
    itm.great_lance,itm.sword_medieval_d_long,
    itm.dk_charger,
  ], level(56)|str_30|agi_30|int_30|cha_30, wp(500), knows_lord_1|knows_ironflesh_10|knows_shield_10|knows_power_strike_10|knows_athletics_10|knows_riding_10|knows_tactics_7|knows_leadership_7, 0x0000000c13002254340eb1d91159392d00000000001eb75a0000000000000000],
  ["dark_knight_lord3", "Lord Tantius", "Tantius", tf_hero, 0, 0, fac.dark_knights, [
    itm.dk_helm_lord_a,itm.wb_dk_plate_boots,itm.dark_gauntlet,itm.dk_armor_lord,
    itm.hera_dk_cav_shield_c,
    itm.great_lance,itm.sword_medieval_d_long,
    itm.dk_charger,
  ], level(56)|str_30|agi_30|int_30|cha_30, wp(500), knows_lord_1|knows_ironflesh_10|knows_shield_10|knows_power_strike_10|knows_athletics_10|knows_riding_10|knows_tactics_7|knows_leadership_7, 0x0000000c370c1194546469ca6c4e450e00000000001ebac40000000000000000],
  ["dark_knight_lord4", "Lord Gracius", "Gracius", tf_hero, 0, 0, fac.dark_knights, [
    itm.dk_helm_lord_b,itm.wb_dk_plate_boots,itm.dark_gauntlet,itm.dk_armor_lord,
    itm.hera_dk_cav_shield_c,
    itm.great_lance,itm.sword_medieval_d_long,
    itm.dk_charger,
  ], level(56)|str_30|agi_30|int_30|cha_30, wp(500), knows_lord_1|knows_ironflesh_10|knows_shield_10|knows_power_strike_10|knows_athletics_10|knows_riding_10|knows_tactics_7|knows_leadership_7, 0x0000000d51000106370c4d4732b536de00000000001db9280000000000000000],


  ["kingdom_1_pretender", "Lady Isolla of Suno", "Isolla", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_1, [
    itm.rich_outfit,itm.blue_hose,
    itm.surcoat_over_mail,itm.iron_greaves,itm.bascinet,
    itm.hera_swadian_cav_shield_c,
    itm.paladin_lance_2,itm.sword_swadian_g,
    itm.swadian_charger_b,
  ], lord_attrib, wp(220), knight_skills_5, 0x00000000ef00000237dc71b90c31631200000000001e371b0000000000000000],
  #claims pre-salic descent

  ["kingdom_2_pretender", "Prince Valdym the Bastard", "Valdym", tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_2, [
    itm.courtly_outfit,itm.leather_boots,
    itm.vaegir_scaled_cuirass,itm.mail_chausses,itm.vaegir_noble_helm,
    itm.hera_vaegir_inf_shield_c,
    itm.great_lance,itm.elite_morningstar,
    itm.vaegir_warhorse_c,
  ], lord_attrib, wp(220), knight_skills_5, 0x00000000200412142452ed631b30365c00000000001c94e80000000000000000, vaegir_face_middle_2],
  #had his patrimony falsified

  ["kingdom_3_pretender", "Dustum Khan", "Dustum", tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_3, [
    itm.nomad_robe,itm.leather_boots,
    itm.tarkhan_lamellar,itm.splinted_greaves,itm.khergit_cavalry_helmet,
    itm.khergit_shield_c2,
    itm.khergit_lance_b,itm.khergit_sword_two_handed_a,
    itm.khergit_warhorse_c,
  ], lord_attrib, wp(220), knight_skills_5, 0x000000065504310b30d556b51238f66100000000001c256d0000000000000000, khergit_face_middle_2],
  #of the family

  ["kingdom_4_pretender", "Lethwin Far-Seeker", "Lethwin Far-Seeker", tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_4, [
    itm.tabard,itm.leather_boots,
    itm.nordic_hauberk_4,itm.splinted_leather_greaves,itm.nordic_huscarl_helmet,
    itm.nord_round_shield_d3,
    itm.great_lance,itm.nordic_axe_c,
    itm.nordic_warhorse_b,
  ], lord_attrib, wp(220), knight_skills_5, 0x00000004340c01841d89949529a6776a00000000001c910a0000000000000000, nord_face_young_2],
  #dispossessed and wronged

  ["kingdom_5_pretender", "Lord Kastor of Veluca", "Kastor", tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_5, [
    itm.nobleman_outfit,itm.leather_boots,
    itm.brigandine_red,itm.mail_boots,itm.kettle_hat,
    itm.hera_rhodok_pavise_c,
    itm.great_lance,itm.arbalestier_blade,
    itm.rhodok_warhorse_c,
  ], lord_attrib, wp(220), knight_skills_5, 0x0000000bed1031051da9abc49ecce25e00000000001e98680000000000000000, rhodok_face_old_2],
  #republican

  ["kingdom_6_pretender", "Arwa the Pearled One", "Arwa the Pearled One", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_6, [
    itm.sarranid_lady_dress,itm.sarranid_boots_a,
    itm.sarranid_mail_shirt_b,itm.sarranid_boots_c,itm.sarranid_mail_coif,
    itm.hera_sarranid_large_shield_e,
    itm.sarranid_lance_c,itm.arabian_sword_c,
    itm.sarranid_warhorse_c,
  ], lord_attrib, wp(220), knight_skills_5, 0x000000050b003004072d51c293a9a70b00000000001dd6a90000000000000000],


  #Royal family members

  ["knight_1_1_wife", "Error - knight_1_1_wife should not appear in game", "knight_1_1_wife", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.commoners, [itm.lady_dress_ruby ,itm.turret_hat_ruby,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],

  #Swadian ladies - eight mothers, eight daughters, four sisters
  ["kingdom_1_lady_1", "Lady Anna", "Anna", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_1, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_1_lady_2", "Lady Nelda", "Nelda", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_1, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["knight_1_lady_3", "Lady Bela", "Bela", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_1, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["knight_1_lady_4", "Lady Elina", "Elina", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_1, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_l_lady_5", "Lady Constanis", "Constanis", tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_1, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_6", "Lady Vera", "Vera", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_1, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_1_lady_7", "Lady Auberina", "Auberina", tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_1, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_8", "Lady Tibal", "Tibal", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_1, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_1_lady_9", "Lady Magar", "Magar", tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_1, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_10", "Lady Thedosa", "Thedosa", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_1, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_1_lady_11", "Lady Melisar", "Melisar", tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_1, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_12", "Lady Irena", "Irena", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_1, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_l_lady_13", "Lady Philenna", "Philenna", tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_1, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_14", "Lady Sonadel", "Sonadel", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_1, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_1_lady_15", "Lady Boadila", "Boadila", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_1, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_16", "Lady Elys", "Elys", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_1, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_1_lady_17", "Lady Johana", "Johana", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_1, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_1_lady_18", "Lady Bernatys", "Bernatys", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_1, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_1_lady_19", "Lady Enricata", "Enricata", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_1, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_1_lady_20", "Lady Gaeta", "Gaeta", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_1, [itm.lady_dress_green,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, swadian_woman_face_2],

  #Vaegir ladies
  ["kingdom_2_lady_1", "Lady Junitha", "Junitha", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_2, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_2", "Lady Katia", "Katia", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_2, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_3", "Lady Seomis", "Seomis", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_2, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_4", "Lady Drina", "Drina", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_2, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_5", "Lady Nesha", "Nesha", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_2, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_6", "Lady Tabath", "Tabath", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_2, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_7", "Lady Pelaeka", "Pelaeka", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_2, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_8", "Lady Haris", "Haris", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_2, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_9", "Lady Vayen", "Vayen", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_2, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_10", "Lady Joaka", "Joaka", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_2, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_11", "Lady Tejina", "Tejina", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_2, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_12", "Lady Olekseia", "Olekseia", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_2, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_13", "Lady Myntha", "Myntha", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_2, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_14", "Lady Akilina", "Akilina", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_2, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_15", "Lady Sepana", "Sepana", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_2, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_16", "Lady Iarina", "Iarina", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_2, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_17", "Lady Sihavan", "Sihavan", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_2, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_18", "Lady Erenchina", "Erenchina", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_2, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_19", "Lady Tamar", "Tamar", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_2, [itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_20", "Lady Valka", "Valka", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_2, [itm.green_dress,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],


  ["kingdom_3_lady_1", "Lady Borge", "Borge", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_3, [itm.brown_dress,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, khergit_woman_face_1],
  ["kingdom_3_lady_2", "Lady Tuan", "Tuan", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_3, [itm.green_dress,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_3_lady_3", "Lady Mahraz", "Mahraz", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_3, [itm.red_dress ,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, khergit_woman_face_2],
  ["kingdom_3_lady_4", "Lady Ayasu", "Ayasu", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_3, [itm.red_dress ,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  ["kingdom_3_lady_5", "Lady Ravin", "Ravin", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_3, [itm.green_dress,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_3_lady_6", "Lady Ruha", "Ruha", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_3, [itm.green_dress,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_3_lady_7", "Lady Chedina", "Chedina", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_3, [itm.brown_dress,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_3_lady_8", "Lady Kefra", "Kefra", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_3, [itm.brown_dress ,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_3_lady_9", "Lady Nirvaz", "Nirvaz", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_3, [itm.brown_dress,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000001940c3006019c925165d1129b00000000001d13240000000000000000],
  ["kingdom_3_lady_10", "Lady Dulua", "Dulua", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_3, [itm.brown_dress,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_3_lady_11", "Lady Selik", "Selik", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_3, [itm.brown_dress ,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000019b083005389591941379b8d100000000001e63150000000000000000],
  ["kingdom_3_lady_12", "Lady Thalatha", "Thalatha", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_3, [itm.brown_dress ,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  ["kingdom_3_lady_13", "Lady Yasreen", "Yasreen", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_3, [itm.brown_dress,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_3_lady_14", "Lady Nadha", "Nadha", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_3, [itm.brown_dress,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, khergit_woman_face_1],
  ["kingdom_3_lady_15", "Lady Zenur", "Zenur", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_3, [itm.brown_dress ,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, khergit_woman_face_2],
  ["kingdom_3_lady_16", "Lady Arjis", "Zenur", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_3, [itm.brown_dress ,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000001ad003001628c54b05d2e48b200000000001d56e60000000000000000],
  ["kingdom_3_lady_17", "Lady Atjahan", "Atjahan", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_3, [itm.brown_dress,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000001a700300265cb6db15d6db6da00000000001f82180000000000000000],
  ["kingdom_3_lady_18", "Lady Qutala", "Qutala", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_3, [itm.brown_dress,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_3_lady_19", "Lady Hindal", "Hindal", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_3, [itm.brown_dress ,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_3_lady_20", "Lady Mechet", "Mechet", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_3, [itm.brown_dress ,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],



  ["kingdom_4_lady_1", "Lady Jadeth", "Jadeth", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_4, [itm.court_dress ,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_lady_2", "Lady Miar", "Miar", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_4, [itm.court_dress ,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_lady_3", "Lady Dria", "Dria", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_4, [itm.peasant_dress,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_4_lady_4", "Lady Glunde", "Glunde", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_4, [itm.peasant_dress,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_lady_5", "Lady Loeka", "Loeka", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_4, [itm.court_dress ,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_lady_6", "Lady Bryn", "Bryn", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_4, [itm.court_dress ,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_lady_7", "Lady Eir", "Eir", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_4, [itm.peasant_dress,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["knight_4_2b_daughter_1", "Lady Thera", "Thera", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_4, [itm.peasant_dress,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_lady_9", "Lady Hild", "Hild", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_4, [itm.court_dress ,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["knight_4_2c_wife_1", "Lady Endegrid", "Endegrid", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_4, [itm.court_dress ,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_lady_11", "Lady Herjasa", "Herjasa", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_4, [itm.peasant_dress,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["knight_4_2c_daughter", "Lady Svipul", "Svipul", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_4, [itm.peasant_dress,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["knight_4_1b_wife", "Lady Ingunn", "Ingunn", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_4, [itm.court_dress ,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_lady_14", "Lady Kaeteli", "Kaeteli", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_4, [itm.court_dress ,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["knight_4_1b_daughter", "Lady Eilif", "Eilif", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_4, [itm.peasant_dress,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["knight_4_2b_daughter_2", "Lady Gudrun", "Gudrun", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_4, [itm.peasant_dress,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_lady_17", "Lady Bergit", "Bergit", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_4, [itm.court_dress ,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["knight_4_2c_wife_2", "Lady Aesa", "Aesa", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_4, [itm.court_dress ,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["knight_4_1c_daughter", "Lady Alfrun", "Alfrun", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_4, [itm.peasant_dress,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_4_lady_20", "Lady Afrid", "Afrid", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_4, [itm.peasant_dress,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],


  ["kingdom_5_lady_1", "Lady Brina", "Brina", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_5, [itm.lady_dress_green,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_lady_2", "Lady Aliena", "Aliena", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_5, [itm.lady_dress_green,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_lady_3", "Lady Aneth", "Aneth", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_5, [itm.lady_dress_ruby ,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_lady_4", "Lady Reada", "Reada", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_5, [itm.lady_dress_ruby ,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_5_wife", "Lady Saraten", "Saraten", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_5, [itm.lady_dress_green,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_5_2b_wife_1", "Lady Baotheia", "Baotheia", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_5, [itm.lady_dress_green,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000000bf0400035913aa236b4d975a00000000001eb69c0000000000000000],
  ["kingdom_5_1c_daughter_1", "Lady Eleandra", "Eleandra", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_5, [itm.lady_dress_ruby ,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_2c_daughter_1", "Lady Meraced", "Meraced", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_5, [itm.lady_dress_ruby ,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_1c_wife_1", "Lady Adelisa", "Adelisa", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_5, [itm.lady_dress_green,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_2c_wife_1", "Lady Calantina", "Calantina", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_5, [itm.lady_dress_green,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_1c_daughter_2", "Lady Forbesa", "Forbesa", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_5, [itm.lady_dress_ruby ,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_2c_daughter_2", "Lady Claudora", "Claudora", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_5, [itm.lady_dress_ruby ,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_1b_wife", "Lady Anais", "Anais", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_5, [itm.lady_dress_green,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_2b_wife_2", "Lady Miraeia", "Miraeia", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_5, [itm.lady_dress_green,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_1c_daughter_3", "Lady Agasia", "Agasia", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_5, [itm.lady_dress_ruby ,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_lady_16", "Lady Geneiava", "Geneiava", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_5, [itm.lady_dress_ruby ,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_1c_wife_2", "Lady Gwenael", "Gwenael", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_5, [itm.lady_dress_green,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_2c_wife_2", "Lady Ysueth", "Ysueth", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_5, [itm.lady_dress_green,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_1c_daughter_4", "Lady Ellian", "Ellian", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_5, [itm.lady_dress_ruby ,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_lady_20", "Lady Timethi", "Timethi", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_5, [itm.lady_dress_ruby ,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],

  #Sarranid ladies
  ["kingdom_6_lady_1", "Lady Rayma", "Rayma", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_6, [itm.sarranid_lady_dress,itm.sarranid_head_cloth,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_6_lady_2", "Lady Thanaikha", "Thanaikha", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_6, [itm.sarranid_lady_dress_b,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["kingdom_6_lady_3", "Lady Sulaha", "Sulaha", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_6, [itm.sarranid_lady_dress,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["kingdom_6_lady_4", "Lady Shatha", "Shatha", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_6, [itm.sarranid_lady_dress,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_6_lady_5", "Lady Bawthan", "Bawthan", tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_6, [itm.sarranid_lady_dress,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_6", "Lady Mahayl", "Mahayl", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_6, [itm.sarranid_lady_dress_b,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_6_lady_7", "Lady Isna", "Isna", tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_6, [itm.sarranid_lady_dress,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_8", "Lady Siyafan", "Siyafan", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_6, [itm.sarranid_lady_dress_b,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_6_lady_9", "Lady Ifar", "Ifar", tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_6, [itm.sarranid_lady_dress_b,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_10", "Lady Yasmin", "Yasmin", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_6, [itm.sarranid_lady_dress,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_6_lady_11", "Lady Dula", "Dula", tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_6, [itm.sarranid_lady_dress,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_12", "Lady Ruwa", "Ruwa", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_6, [itm.sarranid_lady_dress_b,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_6_lady_13", "Lady Luqa", "Luqa", tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_6, [itm.sarranid_lady_dress_b,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_14", "Lady Zandina", "Zandina", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_6, [itm.sarranid_lady_dress,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_6_lady_15", "Lady Lulya", "Lulya", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_6, [itm.sarranid_lady_dress_b,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_16", "Lady Zahara", "Zahara", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_6, [itm.sarranid_lady_dress,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_6_lady_17", "Lady Safiya", "Safiya", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_6, [itm.sarranid_lady_dress_b,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_6_lady_18", "Lady Khalisa", "Khalisa", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_6, [itm.sarranid_lady_dress,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_6_lady_19", "Lady Janab", "Janab", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_6, [itm.sarranid_lady_dress_b,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_6_lady_20", "Lady Sur", "Sur", tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac.kingdom_6, [itm.sarranid_lady_dress,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, swadian_woman_face_2],

  ["heroes_end", "{!}heroes end", "{!}heroes end", tf_hero, 0, reserved, fac.neutral, [itm.riding_horse,itm.leather_jacket,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_common, 0x000000000008318101f390c515555594],

  #Seneschals
  ["town_1_seneschal", "{!}Town 1 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.coarse_tunic,itm.leather_boots], level(2)|def_attrib, wp(20), knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["town_2_seneschal", "{!}Town 2 Seneschal", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.padded_leather,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["town_3_seneschal", "{!}Town 3 Seneschal", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.coarse_tunic,itm.leather_boots], level(2)|def_attrib, wp(20), knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["town_4_seneschal", "{!}Town 4 Seneschal", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.blue_gambeson,itm.blue_hose], level(2)|def_attrib, wp(20), knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["town_5_seneschal", "{!}Town 5 Seneschal", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.leather_jerkin,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, 0x000000000000249101e7898999ac54c6],
  ["town_6_seneschal", "{!}Town 6 Seneschal", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.red_gambeson,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_common, 0x000000000010360b01cef8b57553d34e],
  ["town_7_seneschal", "{!}Town 7 Seneschal", "{!}Town7 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.leather_jerkin,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, 0x000000000000018101f9487aa831dce4],
  ["town_8_seneschal", "{!}Town 8 Seneschal", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.red_gambeson,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_common, 0x000000000004715201ea236c60a2bcae],
  ["town_9_seneschal", "{!}Town 9 Seneschal", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.coarse_tunic,itm.leather_boots], level(2)|def_attrib, wp(20), knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["town_10_seneschal", "{!}Town 10 Seneschal", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.leather_jerkin,itm.blue_hose], level(2)|def_attrib, wp(20), knows_common, 0x000000000010230c01ef41badb50465e],
  ["town_11_seneschal", "{!}Town 11 Seneschal", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.leather_jacket,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_common, 0x000000000008061301fb89acfb95332f],
  ["town_12_seneschal", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.coarse_tunic,itm.leather_boots], level(2)|def_attrib, wp(20), knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["town_13_seneschal", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.leather_jerkin,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["town_14_seneschal", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.blue_gambeson,itm.blue_hose], level(2)|def_attrib, wp(20), knows_common, 0x000000000004728b01c293c694944b05],
  ["town_15_seneschal", "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.blue_gambeson,itm.blue_hose], level(2)|def_attrib, wp(20), knows_common, 0x000000000004728b01c293c694944b05],
  ["town_16_seneschal", "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.blue_gambeson,itm.blue_hose], level(2)|def_attrib, wp(20), knows_common, 0x000000000004728b01c293c694944b05],
  ["town_17_seneschal", "{!}Town17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.blue_gambeson,itm.blue_hose], level(2)|def_attrib, wp(20), knows_common, 0x000000000004728b01c293c694944b05],
  ["town_18_seneschal", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.blue_gambeson,itm.blue_hose], level(2)|def_attrib, wp(20), knows_common, 0x000000000004728b01c293c694944b05],
  ["town_19_seneschal", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.blue_gambeson,itm.blue_hose], level(2)|def_attrib, wp(20), knows_common, 0x000000000004728b01c293c694944b05],
  ["town_20_seneschal", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.blue_gambeson,itm.blue_hose], level(2)|def_attrib, wp(20), knows_common, 0x000000000004728b01c293c694944b05],
  ["town_21_seneschal", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.blue_gambeson,itm.blue_hose], level(2)|def_attrib, wp(20), knows_common, 0x000000000004728b01c293c694944b05],
  ["town_22_seneschal", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.blue_gambeson,itm.blue_hose], level(2)|def_attrib, wp(20), knows_common, 0x000000000004728b01c293c694944b05],
  # NE city
  #  ["town_23_seneschal", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.blue_gambeson,itm.blue_hose], level(2)|def_attrib, wp(20), knows_common, 0x000000000004728b01c293c694944b05],

  ["castle_1_seneschal", "{!}Castle 1 Seneschal", "{!}Castle 1 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.coarse_tunic,itm.hide_boots], level(2)|def_attrib, wp(20), knows_common, 0x000000000010360b01cef8b57553d34e],
  ["castle_2_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.nomad_armor,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_3_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.padded_leather,itm.leather_boots], level(2)|def_attrib, wp(20), knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_4_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.linen_tunic,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_5_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.leather_jerkin,itm.hide_boots], level(2)|def_attrib, wp(20), knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_6_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.coarse_tunic,itm.leather_boots], level(2)|def_attrib, wp(20), knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_7_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.blue_gambeson,itm.blue_hose], level(2)|def_attrib, wp(20), knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_8_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.padded_leather,itm.hide_boots], level(2)|def_attrib, wp(20), knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_9_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.leather_jacket,itm.leather_boots], level(2)|def_attrib, wp(20), knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_10_seneschal", "{!}Castle 10 Seneschal", "{!}Castle 10 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.padded_leather,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_11_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.padded_leather,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_12_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.nomad_armor,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_13_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.padded_leather,itm.leather_boots], level(2)|def_attrib, wp(20), knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_14_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.linen_tunic,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_15_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.leather_jerkin,itm.hide_boots], level(2)|def_attrib, wp(20), knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_16_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.coarse_tunic,itm.leather_boots], level(2)|def_attrib, wp(20), knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_17_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.blue_gambeson,itm.blue_hose], level(2)|def_attrib, wp(20), knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_18_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.padded_leather,itm.hide_boots], level(2)|def_attrib, wp(20), knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_19_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.leather_jacket,itm.leather_boots], level(2)|def_attrib, wp(20), knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_20_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.padded_leather,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_21_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.padded_leather,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_22_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.nomad_armor,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_23_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.padded_leather,itm.leather_boots], level(2)|def_attrib, wp(20), knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_24_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.linen_tunic,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_25_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.leather_jerkin,itm.hide_boots], level(2)|def_attrib, wp(20), knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_26_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.coarse_tunic,itm.leather_boots], level(2)|def_attrib, wp(20), knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_27_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.blue_gambeson,itm.blue_hose], level(2)|def_attrib, wp(20), knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_28_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.padded_leather,itm.hide_boots], level(2)|def_attrib, wp(20), knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_29_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.leather_jacket,itm.leather_boots], level(2)|def_attrib, wp(20), knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_30_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.padded_leather,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_31_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.padded_leather,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_32_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.nomad_armor,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_33_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.padded_leather,itm.leather_boots], level(2)|def_attrib, wp(20), knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_34_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.linen_tunic,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_35_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.leather_jerkin,itm.hide_boots], level(2)|def_attrib, wp(20), knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_36_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.coarse_tunic,itm.leather_boots], level(2)|def_attrib, wp(20), knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_37_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.blue_gambeson,itm.blue_hose], level(2)|def_attrib, wp(20), knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_38_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.padded_leather,itm.hide_boots], level(2)|def_attrib, wp(20), knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_39_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.leather_jacket,itm.leather_boots], level(2)|def_attrib, wp(20), knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_40_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.padded_leather,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_41_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.padded_leather,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_42_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.padded_leather,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_43_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.padded_leather,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_44_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.padded_leather,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_45_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.padded_leather,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_46_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.padded_leather,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_47_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.padded_leather,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_48_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.padded_leather,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, 0x00000000000440c601e1cd45cfb38550],

  #Arena Masters
  ["town_1_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn.town_1_arena|entry(52), reserved, fac.commoners, [itm.coarse_tunic,itm.hide_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, man_face_older_2],
  ["town_2_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn.town_2_arena|entry(52), reserved, fac.commoners, [itm.linen_tunic,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, man_face_older_2],
  ["town_3_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn.town_3_arena|entry(52), reserved, fac.commoners, [itm.nomad_armor,itm.hide_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, man_face_older_2],
  ["town_4_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn.town_4_arena|entry(52), reserved, fac.commoners, [itm.coarse_tunic,itm.hide_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, man_face_older_2],
  ["town_5_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn.town_5_arena|entry(52), reserved, fac.commoners, [itm.linen_tunic,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, man_face_older_2],
  ["town_6_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn.town_6_arena|entry(52), reserved, fac.commoners, [itm.leather_jerkin,itm.leather_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, man_face_older_2],
  ["town_7_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn.town_7_arena|entry(52), reserved, fac.commoners, [itm.padded_leather,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, man_face_older_2],
  ["town_8_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn.town_8_arena|entry(52), reserved, fac.commoners, [itm.linen_tunic,itm.hide_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, man_face_older_2],
  ["town_9_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn.town_9_arena|entry(52), reserved, fac.commoners, [itm.padded_leather,itm.leather_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, man_face_older_2],
  ["town_10_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn.town_10_arena|entry(52), reserved, fac.commoners, [itm.nomad_armor,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, man_face_older_2],
  ["town_11_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn.town_11_arena|entry(52), reserved, fac.commoners, [itm.coarse_tunic,itm.hide_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, man_face_older_2],
  ["town_12_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn.town_12_arena|entry(52), reserved, fac.commoners, [itm.leather_jerkin,itm.hide_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, man_face_older_2],
  ["town_13_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn.town_13_arena|entry(52), reserved, fac.commoners, [itm.coarse_tunic,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, man_face_older_2],
  ["town_14_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn.town_14_arena|entry(52), reserved, fac.commoners, [itm.padded_leather,itm.hide_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, man_face_older_2],
  ["town_15_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn.town_15_arena|entry(52), reserved, fac.commoners, [itm.padded_leather,itm.hide_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, man_face_older_2],
  ["town_16_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn.town_16_arena|entry(52), reserved, fac.commoners, [itm.fur_coat,itm.hide_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, man_face_older_2],
  ["town_17_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn.town_17_arena|entry(52), reserved, fac.commoners, [itm.padded_leather,itm.hide_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, man_face_older_2],
  ["town_18_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn.town_18_arena|entry(52), reserved, fac.commoners, [itm.padded_leather,itm.hide_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, man_face_older_2],
  ["town_19_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn.town_19_arena|entry(52), reserved, fac.commoners, [itm.padded_leather,itm.hide_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, man_face_older_2],
  ["town_20_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn.town_20_arena|entry(52), reserved, fac.commoners, [itm.fur_coat,itm.hide_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, man_face_older_2],
  ["town_21_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn.town_21_arena|entry(52), reserved, fac.commoners, [itm.padded_leather,itm.hide_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, man_face_older_2],
  ["town_22_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn.town_22_arena|entry(52), reserved, fac.commoners, [itm.padded_leather,itm.hide_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, man_face_older_2],

  # Armor Merchants

  ["town_1_armorer", "Armorer", "{!}Armorer", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.linen_tunic,itm.leather_boots   ], level(2)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_2_armorer", "Armorer", "{!}Armorer", tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac.commoners, [itm.woolen_dress,itm.straw_hat       ], level(2)|def_attrib, wp(20), knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_3_armorer", "Armorer", "{!}Armorer", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.arena_tunic_red,itm.hide_boots      ], level(2)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_4_armorer", "Armorer", "{!}Armorer", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.red_gambeson,itm.leather_boots   ], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_5_armorer", "Armorer", "{!}Armorer", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.linen_tunic,itm.nomad_boots     ], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_6_armorer", "Armorer", "{!}Armorer", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.fur_coat,itm.nomad_boots     ], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_7_armorer", "Armorer", "{!}Armorer", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.leather_jerkin,itm.blue_hose       ], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_8_armorer", "Armorer", "{!}Armorer", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.padded_leather,itm.leather_boots   ], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_9_armorer", "Armorer", "{!}Armorer", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.blue_gambeson,itm.nomad_boots     ], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_10_armorer", "Armorer", "{!}Armorer", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.leather_jerkin,itm.hide_boots      ], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_11_armorer", "Armorer", "{!}Armorer", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.fur_coat,itm.leather_boots   ], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_12_armorer", "Armorer", "{!}Armorer", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.red_gambeson,itm.nomad_boots     ], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_13_armorer", "Armorer", "{!}Armorer", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.leather_jacket,itm.hide_boots      ], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_14_armorer", "Armorer", "{!}Armorer", tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac.commoners, [itm.woolen_dress,itm.headcloth       ], level(5)|def_attrib, wp(20), knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_15_armorer", "Armorer", "{!}Armorer", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.blue_gambeson,itm.leather_boots   ], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_16_armorer", "Armorer", "{!}Armorer", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.fur_coat,itm.nomad_boots     ], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_17_armorer", "Armorer", "{!}Armorer", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.fur_coat,itm.hide_boots      ], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_18_armorer", "Armorer", "{!}Armorer", tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac.commoners, [itm.woolen_dress,itm.headcloth       ], level(5)|def_attrib, wp(20), knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_19_armorer", "Armorer", "{!}Armorer", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.blue_gambeson,itm.leather_boots   ], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_20_armorer", "Armorer", "{!}Armorer", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.fur_coat,itm.nomad_boots     ], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_21_armorer", "Armorer", "{!}Armorer", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.fur_coat,itm.hide_boots      ], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_22_armorer", "Armorer", "{!}Armorer", tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_common_dress,itm.sarranid_head_cloth       ], level(5)|def_attrib, wp(20), knows_inventory_management_10, woman_face_1, woman_face_2],

  # Weapon merchants

  ["town_1_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac.commoners, [itm.linen_tunic,itm.hide_boots,itm.straw_hat], level(2)|def_attrib, wp(20), knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_2_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.leather_apron,itm.nomad_boots], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_3_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.fur_coat,itm.hide_boots], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_4_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.leather_apron,itm.hide_boots], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_5_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.leather_jerkin,itm.wrapping_boots], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_6_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.linen_tunic,itm.hide_boots], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_7_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.leather_apron,itm.hide_boots], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_8_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac.commoners, [itm.woolen_dress,itm.wrapping_boots,itm.straw_hat], level(5)|def_attrib, wp(20), knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_9_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.leather_jerkin,itm.leather_boots], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_10_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.linen_tunic,itm.hide_boots], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_11_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.leather_jacket,itm.woolen_hose], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_12_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.leather_apron,itm.hide_boots], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_13_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.arena_tunic_red,itm.wrapping_boots], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_14_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.arena_tunic_blue,itm.wrapping_boots], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_15_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.leather_jacket,itm.woolen_hose], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_16_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.leather_apron,itm.hide_boots], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_17_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.arena_tunic_green,itm.wrapping_boots], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_18_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.linen_tunic,itm.wrapping_boots], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_19_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.leather_jacket,itm.sarranid_boots_a], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_20_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.leather_apron,itm.sarranid_boots_a], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_21_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.arena_tunic_green,itm.sarranid_boots_a], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_22_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners, [itm.linen_tunic,itm.sarranid_boots_a], level(5)|def_attrib, wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2],

  #Tavern keepers

  ["town_1_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_randomize_face, scn.town_1_tavern|entry(9), 0, fac.commoners, [itm.leather_apron,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_common, mercenary_face_1, mercenary_face_2],
  ["town_2_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_randomize_face, scn.town_2_tavern|entry(9), 0, fac.commoners, [itm.leather_apron,itm.leather_boots], level(2)|def_attrib, wp(20), knows_common, mercenary_face_1, mercenary_face_2],
  ["town_3_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_randomize_face|tf_female, scn.town_3_tavern|entry(9), 0, fac.commoners, [itm.woolen_dress,itm.hide_boots], level(2)|def_attrib, wp(20), knows_common, woman_face_1, woman_face_2],
  ["town_4_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_randomize_face, scn.town_4_tavern|entry(9), 0, fac.commoners, [itm.leather_apron,itm.leather_boots], level(2)|def_attrib, wp(20), knows_common, mercenary_face_1, mercenary_face_2],
  ["town_5_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_randomize_face, scn.town_5_tavern|entry(9), 0, fac.commoners, [itm.leather_apron,itm.hide_boots], level(2)|def_attrib, wp(20), knows_common, mercenary_face_1, mercenary_face_2],
  ["town_6_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_randomize_face|tf_female, scn.town_6_tavern|entry(9), 0, fac.commoners, [itm.woolen_dress,itm.hide_boots], level(2)|def_attrib, wp(20), knows_common, woman_face_1, woman_face_2],
  ["town_7_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_randomize_face|tf_female, scn.town_7_tavern|entry(9), 0, fac.commoners, [itm.woolen_dress,itm.leather_boots,itm.headcloth], level(2)|def_attrib, wp(20), knows_common, woman_face_1, woman_face_2],
  ["town_8_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_randomize_face, scn.town_8_tavern|entry(9), 0, fac.commoners, [itm.leather_apron,itm.leather_boots], level(2)|def_attrib, wp(20), knows_common, mercenary_face_1, mercenary_face_2],
  ["town_9_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_randomize_face|tf_female, scn.town_9_tavern|entry(9), 0, fac.commoners, [itm.woolen_dress,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_common, woman_face_1, woman_face_2],
  ["town_10_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_randomize_face|tf_female, scn.town_10_tavern|entry(9), 0, fac.commoners, [itm.woolen_dress,itm.hide_boots], level(2)|def_attrib, wp(20), knows_common, woman_face_1, woman_face_2],
  ["town_11_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_randomize_face|tf_female, scn.town_11_tavern|entry(9), 0, fac.commoners, [itm.woolen_dress,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_common, woman_face_1, woman_face_2],
  ["town_12_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_randomize_face, scn.town_12_tavern|entry(9), 0, fac.commoners, [itm.leather_apron,itm.hide_boots], level(2)|def_attrib, wp(20), knows_common, mercenary_face_1, mercenary_face_2],
  ["town_13_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_randomize_face|tf_female, scn.town_13_tavern|entry(9), 0, fac.commoners, [itm.woolen_dress,itm.hide_boots,itm.headcloth], level(2)|def_attrib, wp(20), knows_common, woman_face_1, woman_face_2],
  ["town_14_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_randomize_face, scn.town_14_tavern|entry(9), 0, fac.commoners, [itm.linen_tunic,itm.leather_boots], level(2)|def_attrib, wp(20), knows_common, mercenary_face_1, mercenary_face_2],
  ["town_15_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_randomize_face|tf_female, scn.town_15_tavern|entry(9), 0, fac.commoners, [itm.woolen_dress,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_common, woman_face_1, woman_face_2],
  ["town_16_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_randomize_face, scn.town_16_tavern|entry(9), 0, fac.commoners, [itm.leather_apron,itm.hide_boots], level(2)|def_attrib, wp(20), knows_common, mercenary_face_1, mercenary_face_2],
  ["town_17_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_randomize_face|tf_female, scn.town_17_tavern|entry(9), 0, fac.commoners, [itm.woolen_dress,itm.hide_boots,itm.headcloth], level(2)|def_attrib, wp(20), knows_common, woman_face_1, woman_face_2],
  ["town_18_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_randomize_face, scn.town_18_tavern|entry(9), 0, fac.commoners, [itm.linen_tunic,itm.leather_boots], level(2)|def_attrib, wp(20), knows_common, mercenary_face_1, mercenary_face_2],
  ["town_19_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_randomize_face|tf_female, scn.town_19_tavern|entry(9), 0, fac.commoners, [itm.sarranid_common_dress_b,itm.sarranid_boots_a], level(2)|def_attrib, wp(20), knows_common, woman_face_1, woman_face_2],
  ["town_20_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_randomize_face, scn.town_20_tavern|entry(9), 0, fac.commoners, [itm.sarranid_cloth_robe,itm.sarranid_boots_a], level(2)|def_attrib, wp(20), knows_common, mercenary_face_1, mercenary_face_2],
  ["town_21_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_randomize_face|tf_female, scn.town_21_tavern|entry(9), 0, fac.commoners, [itm.sarranid_common_dress,itm.sarranid_boots_a,itm.headcloth], level(2)|def_attrib, wp(20), knows_common, woman_face_1, woman_face_2],
  ["town_22_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_randomize_face, scn.town_22_tavern|entry(9), 0, fac.commoners, [itm.sarranid_cloth_robe_b,itm.sarranid_boots_a], level(2)|def_attrib, wp(20), knows_common, mercenary_face_1, mercenary_face_2],

  #Goods Merchants

  ["town_1_merchant", "Merchant", "{!}Merchant", tf_hero|tf_randomize_face|tf_is_merchant, scn.town_1_store|entry(9), 0, fac.commoners, [itm.coarse_tunic,itm.leather_boots                   ], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_2_merchant", "Merchant", "{!}Merchant", tf_hero|tf_randomize_face|tf_is_merchant, scn.town_2_store|entry(9), 0, fac.commoners, [itm.leather_apron,itm.leather_boots                   ], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_3_merchant", "Merchant", "{!}Merchant", tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn.town_3_store|entry(9), 0, fac.commoners, [itm.dress,itm.leather_boots,itm.straw_hat   ], level(2)|def_attrib, wp(20), knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_4_merchant", "Merchant", "{!}Merchant", tf_hero|tf_randomize_face|tf_is_merchant, scn.town_4_store|entry(9), 0, fac.commoners, [itm.leather_apron,itm.leather_boots                   ], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_5_merchant", "Merchant", "{!}Merchant", tf_hero|tf_randomize_face|tf_is_merchant, scn.town_5_store|entry(9), 0, fac.commoners, [itm.nomad_armor,itm.leather_boots                   ], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_6_merchant", "Merchant", "{!}Merchant", tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn.town_6_store|entry(9), 0, fac.commoners, [itm.woolen_dress,itm.leather_boots                   ], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_7_merchant", "Merchant", "{!}Merchant", tf_hero|tf_randomize_face|tf_is_merchant, scn.town_7_store|entry(9), 0, fac.commoners, [itm.leather_jerkin,itm.leather_boots                   ], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_8_merchant", "Merchant", "{!}Merchant", tf_hero|tf_randomize_face|tf_is_merchant, scn.town_8_store|entry(9), 0, fac.commoners, [itm.leather_apron,itm.leather_boots                   ], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_9_merchant", "Merchant", "{!}Merchant", tf_hero|tf_randomize_face|tf_is_merchant, scn.town_9_store|entry(9), 0, fac.commoners, [itm.leather_apron,itm.leather_boots                   ], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_10_merchant", "Merchant", "{!}Merchant", tf_hero|tf_randomize_face|tf_is_merchant, scn.town_10_store|entry(9), 0, fac.commoners, [itm.leather_jerkin,itm.leather_boots                   ], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_11_merchant", "Merchant", "{!}Merchant", tf_hero|tf_randomize_face|tf_is_merchant, scn.town_11_store|entry(9), 0, fac.commoners, [itm.leather_apron,itm.leather_boots                   ], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_12_merchant", "Merchant", "{!}Merchant", tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn.town_12_store|entry(9), 0, fac.commoners, [itm.woolen_dress,itm.leather_boots,itm.female_hood ], level(2)|def_attrib, wp(20), knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_13_merchant", "Merchant", "{!}Merchant", tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn.town_13_store|entry(9), 0, fac.commoners, [itm.dress,itm.leather_boots,itm.straw_hat   ], level(2)|def_attrib, wp(20), knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_14_merchant", "Merchant", "{!}Merchant", tf_hero|tf_randomize_face|tf_is_merchant, scn.town_14_store|entry(9), 0, fac.commoners, [itm.leather_apron,itm.leather_boots                   ], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_15_merchant", "Merchant", "{!}Merchant", tf_hero|tf_randomize_face|tf_is_merchant, scn.town_15_store|entry(9), 0, fac.commoners, [itm.leather_apron,itm.leather_boots                   ], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_16_merchant", "Merchant", "{!}Merchant", tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn.town_16_store|entry(9), 0, fac.commoners, [itm.woolen_dress,itm.leather_boots,itm.female_hood ], level(2)|def_attrib, wp(20), knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_17_merchant", "Merchant", "{!}Merchant", tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn.town_17_store|entry(9), 0, fac.commoners, [itm.dress,itm.leather_boots,itm.straw_hat   ], level(2)|def_attrib, wp(20), knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_18_merchant", "Merchant", "{!}Merchant", tf_hero|tf_randomize_face|tf_is_merchant, scn.town_18_store|entry(9), 0, fac.commoners, [itm.leather_apron,itm.leather_boots                   ], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_19_merchant", "Merchant", "{!}Merchant", tf_hero|tf_randomize_face|tf_is_merchant, scn.town_19_store|entry(9), 0, fac.commoners, [itm.leather_apron,itm.leather_boots                   ], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_20_merchant", "Merchant", "{!}Merchant", tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn.town_20_store|entry(9), 0, fac.commoners, [itm.sarranid_common_dress_b,itm.sarranid_boots_a,itm.sarranid_felt_head_cloth_b  ], level(2)|def_attrib, wp(20), knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_21_merchant", "Merchant", "{!}Merchant", tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn.town_21_store|entry(9), 0, fac.commoners, [itm.sarranid_common_dress,itm.sarranid_boots_a,itm.sarranid_felt_head_cloth  ], level(2)|def_attrib, wp(20), knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_22_merchant", "Merchant", "{!}Merchant", tf_hero|tf_randomize_face|tf_is_merchant, scn.town_22_store|entry(9), 0, fac.commoners, [itm.leather_apron,itm.leather_boots                   ], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2],

  # Horse Merchants

  ["town_1_horse_merchant", "Horse Merchant", "{!}Town 1 Horse Merchant", tf_hero|tf_randomize_face|tf_is_merchant|tf_female, 0, 0, fac.commoners, [itm.blue_dress,itm.blue_hose,itm.female_hood], level(2)|def_attrib, wp(20), knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_2_horse_merchant", "Horse Merchant", "{!}Town 2 Horse Merchant", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.linen_tunic,itm.nomad_boots, ], level(5)|def_attrib, wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_3_horse_merchant", "Horse Merchant", "{!}Town 3 Horse Merchant", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.nomad_armor,itm.hide_boots], level(5)|def_attrib, wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_4_horse_merchant", "Horse Merchant", "{!}Town 4 Horse Merchant", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.leather_jerkin,itm.nomad_boots], level(5)|def_attrib, wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_5_horse_merchant", "Horse Merchant", "{!}Town 5 Horse Merchant", tf_hero|tf_randomize_face|tf_is_merchant|tf_female, 0, 0, fac.commoners, [itm.dress,itm.woolen_hose,itm.common_hood], level(5)|def_attrib, wp(20), knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_6_horse_merchant", "Horse Merchant", "{!}Town 6 Horse Merchant", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.hide_boots], level(5)|def_attrib, wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_7_horse_merchant", "Horse Merchant", "{!}Town 7 Horse Merchant", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.leather_boots], level(5)|def_attrib, wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_8_horse_merchant", "Horse Merchant", "{!}Town 8 Horse Merchant", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.hide_boots], level(5)|def_attrib, wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_9_horse_merchant", "Horse Merchant", "{!}Town 9 Horse Merchant", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.leather_jerkin,itm.woolen_hose], level(5)|def_attrib, wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_10_horse_merchant", "Horse Merchant", "{!}Town 10 Horse Merchant", tf_hero|tf_randomize_face|tf_is_merchant|tf_female, 0, 0, fac.commoners, [itm.blue_dress,itm.blue_hose,itm.straw_hat], level(5)|def_attrib, wp(20), knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_11_horse_merchant", "Horse Merchant", "{!}Town 11 Horse Merchant", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.nomad_armor,itm.leather_boots], level(5)|def_attrib, wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_12_horse_merchant", "Horse Merchant", "{!}Town 12 Horse Merchant", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.leather_jacket,itm.hide_boots], level(5)|def_attrib, wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_13_horse_merchant", "Horse Merchant", "{!}Town 13 Horse Merchant", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.nomad_boots], level(5)|def_attrib, wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_14_horse_merchant", "Horse Merchant", "{!}Town 14 Horse Merchant", tf_hero|tf_randomize_face|tf_is_merchant|tf_female, 0, 0, fac.commoners, [itm.peasant_dress,itm.blue_hose,itm.headcloth], level(5)|def_attrib, wp(20), knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_15_horse_merchant", "Horse Merchant", "{!}Town 15 Horse Merchant", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.nomad_armor,itm.leather_boots], level(5)|def_attrib, wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_16_horse_merchant", "Horse Merchant", "{!}Town 16 Horse Merchant", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.leather_jacket,itm.hide_boots], level(5)|def_attrib, wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_17_horse_merchant", "Horse Merchant", "{!}Town 17 Horse Merchant", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.nomad_boots], level(5)|def_attrib, wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_18_horse_merchant", "Horse Merchant", "{!}Town 18 Horse Merchant", tf_hero|tf_randomize_face|tf_is_merchant|tf_female, 0, 0, fac.commoners, [itm.peasant_dress,itm.blue_hose,itm.headcloth], level(5)|def_attrib, wp(20), knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_19_horse_merchant", "Horse Merchant", "{!}Town 15 Horse Merchant", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.nomad_armor,itm.sarranid_boots_a], level(5)|def_attrib, wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_20_horse_merchant", "Horse Merchant", "{!}Town 16 Horse Merchant", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe,itm.sarranid_boots_a], level(5)|def_attrib, wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_21_horse_merchant", "Horse Merchant", "{!}Town 17 Horse Merchant", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe_b,itm.sarranid_boots_a], level(5)|def_attrib, wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_22_horse_merchant", "Horse Merchant", "{!}Town 18 Horse Merchant", tf_hero|tf_randomize_face|tf_is_merchant|tf_female, 0, 0, fac.commoners, [itm.sarranid_common_dress_b,itm.blue_hose,itm.sarranid_felt_head_cloth_b], level(5)|def_attrib, wp(20), knows_inventory_management_10, woman_face_1, woman_face_2],

  #Town Mayors

  ["town_1_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0, reserved, fac.neutral, [itm.courtly_outfit,itm.leather_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, mercenary_face_2],
  ["town_2_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0, reserved, fac.neutral, [itm.gambeson,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, mercenary_face_2],
  ["town_3_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0, reserved, fac.neutral, [itm.blue_gambeson,itm.leather_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, mercenary_face_2],
  ["town_4_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0, reserved, fac.neutral, [itm.fur_coat,itm.blue_hose], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, mercenary_face_2],
  ["town_5_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0, reserved, fac.neutral, [itm.nobleman_outfit,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, mercenary_face_2],
  ["town_6_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0, reserved, fac.neutral, [itm.red_gambeson,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, mercenary_face_2],
  ["town_7_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0, reserved, fac.neutral, [itm.rich_outfit,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, mercenary_face_2],
  ["town_8_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0, reserved, fac.neutral, [itm.red_gambeson,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, mercenary_face_2],
  ["town_9_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0, reserved, fac.neutral, [itm.courtly_outfit,itm.leather_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, mercenary_face_2],
  ["town_10_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0, reserved, fac.neutral, [itm.leather_jerkin,itm.blue_hose], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, mercenary_face_2],
  ["town_11_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0, reserved, fac.neutral, [itm.leather_jacket,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, mercenary_face_2],
  ["town_12_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0, reserved, fac.neutral, [itm.red_gambeson,itm.leather_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, mercenary_face_2],
  ["town_13_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0, reserved, fac.neutral, [itm.nobleman_outfit,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, mercenary_face_2],
  ["town_14_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0, reserved, fac.neutral, [itm.blue_gambeson,itm.blue_hose], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, mercenary_face_2],
  ["town_15_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0, reserved, fac.neutral, [itm.leather_jacket,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, mercenary_face_2],
  ["town_16_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0, reserved, fac.neutral, [itm.fur_coat,itm.leather_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, mercenary_face_2],
  ["town_17_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0, reserved, fac.neutral, [itm.nobleman_outfit,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, mercenary_face_2],
  ["town_18_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0, reserved, fac.neutral, [itm.blue_gambeson,itm.blue_hose], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, mercenary_face_2],
  ["town_19_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0, reserved, fac.neutral, [itm.sarranid_cloth_robe,itm.sarranid_boots_a], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, mercenary_face_2],
  ["town_20_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0, reserved, fac.neutral, [itm.sarranid_cloth_robe,itm.sarranid_boots_a], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, mercenary_face_2],
  ["town_21_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0, reserved, fac.neutral, [itm.sarranid_cloth_robe,itm.sarranid_boots_a], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, mercenary_face_2],
  ["town_22_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0, reserved, fac.neutral, [itm.sarranid_cloth_robe,itm.sarranid_boots_a], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, mercenary_face_2],

  #Village Elders

  ["village_1_elder", "Elder Wilfred", "Wilfred", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.hide_boots,itm.felt_hat], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_2_elder", "Elder Michael", "Michael", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.tabard,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_3_elder", "Elder Gerchard", "Gerchard", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_4_elder", "Elder Harmin", "Harmin", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.nomad_boots,itm.leather_cap], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_5_elder", "Elder Bjoern", "Bjoern", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_6_elder", "Elder Feyn", "Feyn", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.hide_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_7_elder", "Elder Charlin", "Charlin", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.fur_coat,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_8_elder", "Elder Arvid", "Arvid", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.wrapping_boots,itm.felt_hat], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_9_elder", "Elder Rostachio", "Rostachio", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.hide_boots,itm.leather_cap], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_10_elder", "Elder Bjarte", "Bjarte", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.fur_coat,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_11_elder", "Elder Agalay", "Agalay", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_12_elder", "Elder Visin", "Visin", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe_b,itm.wrapping_boots,itm.leather_cap], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_13_elder", "Elder Garth", "Garth", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_14_elder", "Elder Rostophey", "Rostophey", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_15_elder", "Elder Alfred", "Alfred", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.hide_boots,itm.felt_hat], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_16_elder", "Elder Kolomir", "Kolomir", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.hide_boots,itm.leather_warrior_cap], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_17_elder", "Elder Pechar", "Pechar", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.fur_coat,itm.nomad_boots,itm.fur_hat], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_18_elder", "Elder Otrozh", "Otrozh", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.hide_boots,itm.leather_warrior_cap], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_19_elder", "Elder Velezh", "Velezh", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.nomad_boots,itm.fur_hat], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_20_elder", "Elder Lopar", "Lopar", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.hide_boots,itm.leather_warrior_cap], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_21_elder", "Elder Chemyaka", "Chemyaka", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.fur_coat,itm.wrapping_boots,itm.leather_cap], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_22_elder", "Elder Oleg", "Oleg", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.fur_coat,itm.nomad_boots,itm.fur_hat], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_23_elder", "Elder Estor", "Estor", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.hide_boots,itm.felt_hat], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_24_elder", "Elder Tocchi", "Tocchi", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.red_shirt,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_25_elder", "Elder Boghan", "Boghan", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.fur_coat,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_26_elder", "Elder Verandi", "Verandi", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.blue_tunic,itm.wrapping_boots,itm.leather_cap], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_27_elder", "Elder Basquar", "Basquar", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.wrapping_boots,itm.felt_hat], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_28_elder", "Elder Batyr", "Batyr", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.nomad_vest,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_29_elder", "Elder Asmund", "Asmund", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.hide_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_30_elder", "Elder Ulf", "Ulf", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.ragged_outfit,itm.wrapping_boots,itm.leather_cap], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_31_elder", "Elder Fridtjof", "Fridtjof", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_32_elder", "Elder Rolf", "Rolf", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.tunic_with_green_cape,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_33_elder", "Elder Heinrich", "Heinrich", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.wrapping_boots,itm.leather_cap], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_34_elder", "Elder Bran", "Bran", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.nomad_boots,itm.fur_hat], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_35_elder", "Elder Severin", "Severin", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.blue_tunic,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_36_elder", "Elder Oddmund", "Oddmund", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.hide_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_37_elder", "Elder Khomyr", "Khomyr", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe_b,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_38_elder", "Elder Meinzer", "Meinzer", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.hide_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_39_elder", "Elder Jacob", "Jacob", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_40_elder", "Elder Arterius", "Arterius", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.gambeson,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_41_elder", "Elder Habar", "Habar", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_42_elder", "Elder Ohhomyr", "Ohhomyr", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.linen_tunic,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_43_elder", "Elder Tamysh", "Tamysh", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.pilgrim_disguise,itm.wrapping_boots,itm.leather_cap], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_44_elder", "Elder Varraha", "Varraha", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.nomad_boots,itm.fur_hat], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_45_elder", "Elder Babay", "Babay", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.rawhide_coat,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_46_elder", "Elder Notti", "Notti", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.hide_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_47_elder", "Elder Palkon", "Palkon", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe_b,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_48_elder", "Elder Darth", "Darth", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.hide_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_49_elder", "Elder Borey", "Borey", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.fur_coat,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_50_elder", "Elder Kotophey", "Kotophey", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe_b,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_51_elder", "Elder Aksel", "Aksel", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe_b,itm.wrapping_boots,itm.leather_cap], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_52_elder", "Elder Sodraghan", "Sodraghan", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.nomad_boots,itm.fur_hat], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_53_elder", "Elder Toizer", "Toizer", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.hide_boots,itm.felt_hat], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_54_elder", "Elder Cranz", "Cranz", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe_b,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_55_elder", "Elder Hodron", "Hodron", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_56_elder", "Elder Eirik", "Eirik", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe_b,itm.wrapping_boots,itm.leather_cap], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_57_elder", "Elder Malenz", "Malenz", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.wrapping_boots,itm.felt_hat], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_58_elder", "Elder Khomol", "Khomol", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.fur_coat,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_59_elder", "Elder Marquen", "Marquen", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.hide_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_60_elder", "Elder Otto", "Otto", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe_b,itm.wrapping_boots,itm.leather_cap], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_61_elder", "Elder Esben", "Esben", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe_b,itm.wrapping_boots,itm.leather_cap], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_62_elder", "Elder Volodar", "Volodar", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.nomad_boots,itm.fur_hat], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_63_elder", "Elder Keirh", "Keirh", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.hide_boots,itm.felt_hat], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_64_elder", "Elder Emroq", "Emroq", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe_b,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_65_elder", "Elder Rindarr", "Rindarr", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.fur_coat,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_66_elder", "Elder Umety", "Umety", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe_b,itm.wrapping_boots,itm.leather_cap], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_67_elder", "Elder Vezhev", "Vezhev", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.wrapping_boots,itm.felt_hat], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_68_elder", "Elder Koltir", "Koltir", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe_b,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_69_elder", "Elder Edvard", "Edvard", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.hide_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_70_elder", "Elder Waltios", "Waltios", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe_b,itm.wrapping_boots,itm.leather_cap], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_71_elder", "Elder Drem", "Drem", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe_b,itm.wrapping_boots,itm.leather_cap], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_72_elder", "Elder Teffin", "Teffin", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.nomad_boots,itm.fur_hat], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_73_elder", "Elder Chokki", "Chokki", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.hide_boots,itm.felt_hat], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_74_elder", "Elder Kuzmar", "Kuzmar", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe_b,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_75_elder", "Elder Chomysh", "Chomysh", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_76_elder", "Elder Storra", "Storra", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.fur_coat,itm.wrapping_boots,itm.leather_cap], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_77_elder", "Elder Torleif", "Torleif", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.wrapping_boots,itm.felt_hat], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_78_elder", "Elder Knestir", "Knestir", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe_b,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_79_elder", "Elder Ars_Totti", "Ars_Totti", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.hide_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_80_elder", "Elder Erling", "Erling", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe_b,itm.wrapping_boots,itm.leather_cap], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_81_elder", "Elder Torgils", "Torgils", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_82_elder", "Elder Cort", "Cort", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe_b,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_83_elder", "Elder Eric", "Eric", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.fur_coat,itm.wrapping_boots,itm.leather_cap], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_84_elder", "Elder Astorro", "Astorro", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.nomad_boots,itm.fur_hat], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_85_elder", "Elder Opashny", "Opashny", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe_b,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_86_elder", "Elder Lesno", "Lesno", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.hide_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_87_elder", "Elder Koropach", "Koropach", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe_b,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_88_elder", "Elder Dastarkh", "Dastarkh", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.fur_coat,itm.hide_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_89_elder", "Elder Kelchyk", "Kelchyk", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_90_elder", "Elder Brin", "Brin", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_91_elder", "Elder Ahmad", "Ahmad", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_92_elder", "Elder Mohammar", "Mohammar", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe_b,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_93_elder", "Elder Mottalib", "Mottalib", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe,itm.wrapping_boots,itm.leather_cap], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_94_elder", "Elder Al-Alem", "Al-Alem", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe,itm.nomad_boots,itm.fur_hat], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_95_elder", "Elder Quasim", "Quasim", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe_b,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_96_elder", "Elder Nabil", "Nabil", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.hide_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_97_elder", "Elder Rayam", "Rayam", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_98_elder", "Elder Saif", "Saif", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe,itm.hide_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_99_elder", "Elder Omar", "Omar", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_100_elder", "Elder Quadir", "Quadir", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_101_elder", "Elder Rodha", "Rodha", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe_b,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_102_elder", "Elder Jabir", "Jabir", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe_b,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_103_elder", "Elder Il-Makah", "Il-Makah", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe,itm.wrapping_boots,itm.leather_cap], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_104_elder", "Elder Kaffir", "Kaffir", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.nomad_boots,itm.fur_hat], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_105_elder", "Elder Ismat", "Ismat", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe_b,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_106_elder", "Elder Faraj", "Faraj", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.coarse_tunic,itm.hide_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_107_elder", "Elder Hadi", "Hadi", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe_b,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_108_elder", "Elder Firdous", "Firdous", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe_b,itm.hide_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_109_elder", "Elder Hisein", "Hisein", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe_b,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_110_elder", "Elder Ghaza-Hadj", "Ghaza-Hadj", tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac.commoners, [itm.sarranid_cloth_robe_b,itm.wrapping_boots], level(2)|def_attrib, wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2],

  # Place extra merchants before this point

  ["merchants_end", "merchants_end", "merchants_end", tf_hero|tf_is_merchant, 0, 0, fac.commoners, [], level(2)|def_attrib, wp(20), knows_inventory_management_10, 0],

  #Used for player enterprises

  ["town_1_master_craftsman", "{!}Town 1 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.leather_apron,itm.leather_boots], level(2)|def_attrib, wp(20), knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_2_master_craftsman", "{!}Town 2 Craftsman", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.padded_leather,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, 0x0000000f010811c92d3295e46a96c72300000000001f5a980000000000000000],
  ["town_3_master_craftsman", "{!}Town 3 Craftsman", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.coarse_tunic,itm.leather_boots], level(2)|def_attrib, wp(20), knows_common, 0x000000001b083203151d2ad5648e52b400000000001b172e0000000000000000],
  ["town_4_master_craftsman", "{!}Town 4 Craftsman", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.leather_apron,itm.blue_hose], level(2)|def_attrib, wp(20), knows_common, 0x000000001a10114f091b2c259cd4c92300000000000228dd0000000000000000],
  ["town_5_master_craftsman", "{!}Town 5 Craftsman", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.leather_jerkin,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, 0x000000000d1044c578598cd92b5256db00000000001f23340000000000000000],
  ["town_6_master_craftsman", "{!}Town 6 Craftsman", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.leather_apron,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_common, 0x000000001f046285493eaf1b048abcdb00000000001a8aad0000000000000000],
  ["town_7_master_craftsman", "{!}Town 7 Craftsman", "{!}Town 7 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.leather_jerkin,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, 0x000000002b0052c34c549225619356d400000000001cc6e60000000000000000],
  ["town_8_master_craftsman", "{!}Town 8 Craftsman", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.leather_apron,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_common, 0x0000000fdb0c20465b6e51e8a12c82d400000000001e148c0000000000000000],
  ["town_9_master_craftsman", "{!}Town 9 Craftsman", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.coarse_tunic,itm.leather_boots], level(2)|def_attrib, wp(20), knows_common, 0x00000009f7005246071db236e296a45300000000001a8b0a0000000000000000],
  ["town_10_master_craftsman", "{!}Town 10 Craftsman", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.leather_jerkin,itm.blue_hose], level(2)|def_attrib, wp(20), knows_common, 0x00000009f71012c2456a921aa379321a000000000012c6d90000000000000000],
  ["town_11_master_craftsman", "{!}Town 11 Craftsman", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.leather_apron,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_common, 0x00000009f308514428db71b9ad70b72400000000001dc9140000000000000000],
  ["town_12_master_craftsman", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.coarse_tunic,itm.leather_boots], level(2)|def_attrib, wp(20), knows_common, 0x00000009e90825863853a5b91cd71a5b00000000000598db0000000000000000],
  ["town_13_master_craftsman", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.leather_jerkin,itm.woolen_hose], level(2)|def_attrib, wp(20), knows_common, 0x00000009fa0c708f274c8eb4c64e271300000000001eb69a0000000000000000],
  ["town_14_master_craftsman", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.leather_apron,itm.blue_hose], level(2)|def_attrib, wp(20), knows_common, 0x00000007590c3206155c8b475a4e439a00000000001f489a0000000000000000],
  ["town_15_master_craftsman", "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.leather_apron,itm.blue_hose], level(2)|def_attrib, wp(20), knows_common, 0x00000007440022d04b2c6cb7d3723d5a00000000001dc90a0000000000000000],
  ["town_16_master_craftsman", "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.leather_apron,itm.blue_hose], level(2)|def_attrib, wp(20), knows_common, 0x00000007680c3586054b8e372e4db65c00000000001db7230000000000000000],
  ["town_17_master_craftsman", "{!}Town 17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.leather_apron,itm.blue_hose], level(2)|def_attrib, wp(20), knows_common, 0x0000000766046186591b564cec85d2e200000000001e4cea0000000000000000],
  ["town_18_master_craftsman", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.leather_apron,itm.blue_hose], level(2)|def_attrib, wp(20), knows_common, 0x0000000e7e0075523a6aa9b6da61e8dd00000000001d96d30000000000000000],
  ["town_19_master_craftsman", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.sarranid_cloth_robe,itm.blue_hose], level(2)|def_attrib, wp(20), knows_common, 0x000000002408314852a432e88aaa42e100000000001e284e0000000000000000],
  ["town_20_master_craftsman", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.sarranid_cloth_robe_b,itm.blue_hose], level(2)|def_attrib, wp(20), knows_common, 0x000000001104449136e44cbd1c9352bc000000000005e8d10000000000000000],
  ["town_21_master_craftsman", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.sarranid_cloth_robe,itm.blue_hose], level(2)|def_attrib, wp(20), knows_common, 0x00000000131032d3351c6e43226ec96c000000000005b5240000000000000000],
  ["town_22_master_craftsman", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0, reserved, fac.neutral, [itm.sarranid_cloth_robe_b,itm.blue_hose], level(2)|def_attrib, wp(20), knows_common, 0x00000000200c658a5723b1a3148dc455000000000015ab920000000000000000],

  # Chests

  ["tutorial_chest_1", "{!}Melee Weapons Chest", "{!}Melee Weapons Chest", tf_hero|tf_inactive, 0, reserved, fac.neutral, [itm.tutorial_sword,itm.tutorial_axe,itm.tutorial_spear,itm.tutorial_club,itm.tutorial_battle_axe], level(18)|def_attrib, wp(60), knows_common, 0],
  ["tutorial_chest_2", "{!}Ranged Weapons Chest", "{!}Ranged Weapons Chest", tf_hero|tf_inactive, 0, reserved, fac.neutral, [itm.tutorial_throwing_daggers], level(18)|def_attrib, wp(60), knows_common, 0],
  ["bonus_chest_1", "{!}Bonus Chest", "{!}Bonus Chest", tf_hero|tf_inactive, 0, reserved, fac.neutral, [], level(18)|def_attrib, wp(60), knows_common, 0],
  ["bonus_chest_2", "{!}Bonus Chest", "{!}Bonus Chest", tf_hero|tf_inactive, 0, reserved, fac.neutral, [], level(18)|def_attrib, wp(60), knows_common, 0],
  ["bonus_chest_3", "{!}Bonus Chest", "{!}Bonus Chest", tf_hero|tf_inactive, 0, reserved, fac.neutral, [], level(18)|def_attrib, wp(60), knows_common, 0],

  ["household_possessions", "{!}household_possessions", "{!}household_possessions", tf_hero|tf_inactive|tf_is_merchant, 0, reserved, fac.neutral, [], level(18)|def_attrib, wp(60), knows_inventory_management_10, 0],

  # These are used as arrays in the scripts.
  ["temp_array_a", "{!}temp_array_a", "{!}temp_array_a", tf_hero|tf_inactive, 0, reserved, fac.neutral, [], level(18)|def_attrib, wp(60), knows_common, 0],
  ["temp_array_b", "{!}temp_array_b", "{!}temp_array_b", tf_hero|tf_inactive, 0, reserved, fac.neutral, [], level(18)|def_attrib, wp(60), knows_common, 0],
  ["temp_array_c", "{!}temp_array_c", "{!}temp_array_c", tf_hero|tf_inactive, 0, reserved, fac.neutral, [], level(18)|def_attrib, wp(60), knows_common, 0],

  ["stack_selection_amounts", "{!}stack_selection_amounts", "{!}stack_selection_amounts", tf_hero|tf_inactive, 0, reserved, fac.neutral, [], def_attrib, 0, knows_common, 0],
  ["stack_selection_ids", "{!}stack_selection_ids", "{!}stack_selection_ids", tf_hero|tf_inactive, 0, reserved, fac.neutral, [], def_attrib, 0, knows_common, 0],

  ["notification_menu_types", "{!}notification_menu_types", "{!}notification_menu_types", tf_hero|tf_inactive, 0, reserved, fac.neutral, [], def_attrib, 0, knows_common, 0],
  ["notification_menu_var1", "{!}notification_menu_var1", "{!}notification_menu_var1", tf_hero|tf_inactive, 0, reserved, fac.neutral, [], def_attrib, 0, knows_common, 0],
  ["notification_menu_var2", "{!}notification_menu_var2", "{!}notification_menu_var2", tf_hero|tf_inactive, 0, reserved, fac.neutral, [], def_attrib, 0, knows_common, 0],

  ["banner_background_color_array", "{!}banner_background_color_array", "{!}banner_background_color_array", tf_hero|tf_inactive, 0, reserved, fac.neutral, [], def_attrib, 0, knows_common, 0],

  # Add Extra Quest NPCs below this point

  ["local_merchant", "Local Merchant", "Local Merchants", tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.commoners, [
    itm.leather_apron,itm.leather_boots,itm.spiked_club
  ], level(5)|def_attrib, wp(40), knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["tax_rebel", "Peasant Rebel", "Peasant Rebels", tf_guarantee_armor, 0, reserved, fac.commoners, [
    itm.leather_cap,itm.felt_hat,itm.felt_hat,itm.linen_tunic,itm.coarse_tunic,itm.nomad_boots,itm.wrapping_boots,itm.club,itm.spiked_club,itm.hammer,itm.cleaver,itm.hatchet,itm.beef_splitter,
  ], level(4)|def_attrib, wp(60), knows_common, vaegir_face1, vaegir_face2],
  ["trainee_peasant", "Peasant", "Peasants", tf_guarantee_armor, 0, reserved, fac.commoners, [
    itm.leather_cap,itm.felt_hat,itm.felt_hat,itm.linen_tunic,itm.coarse_tunic,itm.nomad_boots,itm.wrapping_boots,itm.staff,
  ], level(4)|def_attrib, wp(60), knows_common, vaegir_face1, vaegir_face2],
  ["fugitive", "Nervous Man", "Nervous Men", tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.commoners, [
    itm.red_shirt,itm.linen_tunic,itm.coarse_tunic,itm.tabard,itm.leather_vest,itm.woolen_hose,itm.nomad_boots,itm.blue_hose,itm.wrapping_boots,itm.fur_hat,itm.leather_cap,itm.one_handed_battle_axe_a,
  ], level(26)|def_attrib|str_24|agi_25, wp(180), knows_common|knows_power_throw_6|knows_power_strike_6|knows_ironflesh_9, man_face_middle_1, man_face_old_2],
  ["belligerent_drunk", "Belligerent Drunk", "Belligerent Drunks", tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.commoners, [
    itm.red_shirt,itm.linen_tunic,itm.coarse_tunic,itm.tabard,itm.leather_vest,itm.woolen_hose,itm.nomad_boots,itm.blue_hose,itm.wrapping_boots,itm.fur_hat,itm.leather_cap,itm.sword_norman_rusty
  ], level(15)|def_attrib|str_20|agi_8, wp(120), knows_common|knows_power_strike_2|knows_ironflesh_9, bandit_face1, bandit_face2],

  # ???

  ["hired_assassin", "Hired Assassin", "Hired Assassin", tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.commoners, [
    itm.red_shirt,itm.linen_tunic,itm.coarse_tunic,itm.tabard,itm.leather_vest,itm.woolen_hose,itm.nomad_boots,itm.blue_hose,itm.wrapping_boots,itm.fur_hat,itm.leather_cap,itm.scimitar,
  ], level(20)|def_attrib|str_20|agi_16, wp(180), knows_common|knows_power_strike_5|knows_ironflesh_3, bandit_face1, bandit_face2],
  ["fight_promoter", "Rough-Looking Character", "Rough-Looking Character", tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.commoners, [
    itm.red_shirt,itm.linen_tunic,itm.coarse_tunic,itm.tabard,itm.leather_vest,itm.woolen_hose,itm.nomad_boots,itm.blue_hose,itm.wrapping_boots,itm.fur_hat,itm.leather_cap,itm.sword_medieval_c,
  ], level(20)|def_attrib|str_20|agi_16, wp(180), knows_common|knows_power_strike_5|knows_ironflesh_3, bandit_face1, bandit_face2],
  ["spy", "Ordinary Townsman", "Ordinary Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse, 0, 0, fac.neutral, [
    itm.leather_jerkin,itm.leather_boots,itm.courser_horse,itm.leather_gloves,itm.sword_norman,
  ], level(20)|def_attrib|agi_11, wp(130), knows_common, man_face_middle_1, man_face_older_2],
  ["spy_partner", "Unremarkable Townsman", "Unremarkable Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse, 0, 0, fac.neutral, [
    itm.leather_jerkin,itm.leather_boots,itm.courser_horse,itm.leather_gloves,itm.sword_medieval_c_long,
  ], level(10)|def_attrib|agi_11, wp(130), knows_common, vaegir_face1, vaegir_face2],

  ["nurse_for_lady", "Nurse", "Nurse", tf_female|tf_guarantee_armor, 0, reserved, fac.commoners, [itm.pilgrim_disguise,itm.black_hood,itm.wrapping_boots], level(4)|def_attrib, wp(60), knows_common, woman_face_1, woman_face_2],
  ["temporary_minister", "Minister", "Minister", tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac.commoners, [itm.rich_outfit,itm.wrapping_boots], level(4)|def_attrib, wp(60), knows_common, man_face_middle_1, man_face_older_2],
  ["runaway_girl", "Bride-To-Be", "Brides-To-Be", tf_hero|tf_female|tf_randomize_face, 0, reserved, fac.commoners, [itm.wedding_dress,itm.wimple_with_veil,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, bride_face1, scholar_face_1],
  ["spymaster", "Spymaster", "Spymaster", tf_hero|tf_randomize_face, 0, reserved, fac.neutral, [itm.pilgrim_disguise,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, mercenary_face_2],
  ["kidnapped_wife", "Miller's Wife", "Miller's Wives", tf_hero|tf_female|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved, fac.commoners, [itm.dress,itm.leather_boots], level(2)|def_attrib, wp(50), knows_common|knows_riding_2, woman_face_1, woman_face_2],

  # Kingdom Advisors here

  ["finances_array_this", "finances_array_this", "finances_array_this", tf_hero|tf_inactive, 0, reserved, fac.neutral, [], level(18)|def_attrib, wp(60), knows_common, 0],
  ["finances_array_last", "finances_array_last", "finances_array_last", tf_hero|tf_inactive, 0, reserved, fac.neutral, [], level(18)|def_attrib, wp(60), knows_common, 0],
  ["array_to_be_named", "array_to_be_named", "array_to_be_named", tf_hero|tf_inactive, 0, reserved, fac.neutral, [], level(18)|def_attrib, wp(60), knows_common, 0],
  ["civil_adviser", "Civics_Adviser", "Civics_Adviser", tf_hero|tf_randomize_face, 0, reserved, fac.neutral, [itm.courtly_outfit,itm.leather_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_2, mercenary_face_2],
  ["financial_adviser", "Chamberlain", "Chamberlain", tf_hero|tf_randomize_face, 0, reserved, fac.neutral, [itm.blue_gambeson,itm.blue_hose], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, mercenary_face_2],
  ["logistics_adviser", "Logistician", "Logistician", tf_hero|tf_randomize_face, 0, reserved, fac.neutral, [itm.rich_outfit,itm.blue_hose], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, mercenary_face_2],
  ["intel_adviser", "Spymaster", "Spymaster", tf_hero|tf_randomize_face, 0, reserved, fac.neutral, [itm.pilgrim_disguise,itm.nomad_boots], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, mercenary_face_2],

  #Player history array

  ["log_array_entry_type", "{!}Local Merchant", "{!}Local Merchant", tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.commoners, [], level(5)|def_attrib, wp(40), knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_entry_time", "{!}Local Merchant", "{!}Local Merchant", tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.commoners, [], level(5)|def_attrib, wp(40), knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_actor", "{!}Local Merchant", "{!}Local Merchant", tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.commoners, [], level(5)|def_attrib, wp(40), knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object", "{!}Local Merchant", "{!}Local Merchant", tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.commoners, [], level(5)|def_attrib, wp(40), knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object_lord", "{!}Local Merchant", "{!}Local Merchant", tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.commoners, [], level(5)|def_attrib, wp(40), knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object_faction", "{!}Local Merchant", "{!}Local Merchant", tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.commoners, [], level(5)|def_attrib, wp(40), knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_troop_object", "{!}Local Merchant", "{!}Local Merchant", tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.commoners, [], level(5)|def_attrib, wp(40), knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_troop_object_faction", "{!}Local Merchant", "{!}Local Merchant", tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.commoners, [], level(5)|def_attrib, wp(40), knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_faction_object", "{!}Local Merchant", "{!}Local Merchant", tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.commoners, [], level(5)|def_attrib, wp(40), knows_power_strike_1, merchant_face_1, merchant_face_2],

  ["swadian_merchant", "Merchant of Praven", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac.kingdom_4, [itm.courtly_outfit,itm.leather_boots,itm.bastard_sword_b,], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, mercenary_face_2],
  ["vaegir_merchant", "Merchant of Reyvadin", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac.kingdom_5, [itm.nobleman_outfit,itm.woolen_hose,itm.maul_b,], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, mercenary_face_2],
  ["khergit_merchant", "Merchant of Tulga", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac.kingdom_1, [itm.red_gambeson,itm.nomad_boots,itm.mace_long_b,], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, mercenary_face_2],
  ["nord_merchant", "Merchant of Sargoth", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac.kingdom_2, [itm.red_gambeson,itm.nomad_boots,itm.long_axe_b,], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, mercenary_face_2],
  ["rhodok_merchant", "Merchant of Jelkala", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac.kingdom_3, [itm.leather_jerkin,itm.blue_hose,itm.military_cleaver_a,], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, mercenary_face_2],
  ["sarranid_merchant", "Merchant of Shariz", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac.kingdom_6, [itm.sarranid_cloth_robe,itm.sarranid_boots_a,itm.bec_de_corbin_a,], level(2)|def_attrib, wp(20), knows_common, man_face_middle_1, mercenary_face_2],

  ["startup_merchants_end", "startup_merchants_end", "startup_merchants_end", tf_hero, 0, 0, fac.commoners, [], level(2)|def_attrib, wp(20), knows_inventory_management_10, 0],

  # Bandit leaders (???)

  ["sea_raider_leader", "Sea Raider Captain", "Sea Raiders", tf_hero|tf_guarantee_all_wo_ranged, 0, 0, fac.outlaws, [
    itm.nordic_helmet,itm.nordic_helmet,itm.nasal_helmet,itm.mail_shirt,itm.byrnie,itm.mail_hauberk,itm.leather_boots,itm.nomad_boots,
    itm.boar_spear,itm.sword_medieval_b,itm.sword_medieval_b,itm.sword_viking_c,itm.one_handed_war_axe_b,itm.javelin,itm.light_throwing_axes,itm.long_bow_nor,itm.broadhead_arrows,
  ], level(24)|def_attrib, wp(110), knows_ironflesh_2|knows_power_strike_2|knows_power_draw_3|knows_power_throw_2|knows_riding_1|knows_athletics_2, nord_face_young_1, nord_face_old_2],
  ["looter_leader", "Robber", "Looters", tf_hero, 0, 0, fac.outlaws, [
    itm.rawhide_coat,itm.nomad_armor,itm.nomad_armor,itm.woolen_cap,itm.woolen_cap,itm.nomad_boots,itm.wrapping_boots,
    itm.hatchet,itm.club,itm.butchering_knife,itm.falchion,itm.stones,
  ], level(4)|def_attrib, wp(20), knows_common, 0x00000001b80032473ac49738206626b200000000001da7660000000000000000, bandit_face2],

  ["bandit_leaders_end", "bandit_leaders_end", "bandit_leaders_end", tf_hero, 0, 0, fac.commoners, [], level(2)|def_attrib, wp(20), knows_inventory_management_10, 0],

  ["relative_of_merchant", "Merchant's Brother", "{!}Prominent", tf_hero, 0, 0, fac.kingdom_2, [itm.linen_tunic,itm.nomad_boots], level(1)|def_attrib, wp_melee(10), knows_athletics_1|knows_ironflesh_2|knows_shield_2, 0x00000000320410022d2595495491afa400000000001d9ae30000000000000000, mercenary_face_2],

  ["relative_of_merchants_end", "relative_of_merchants_end", "relative_of_merchants_end", tf_hero, 0, 0, fac.commoners, [], level(2)|def_attrib, wp(20), knows_inventory_management_10, 0],

# PLUGIN_MULTIPLAYER

]

####Troop upgrade declarations
# NE 600 Series Troop Upgrade Paths - all others pruned
# Mercenary Upgrade Paths NE 600 Series
# Female
define_troop_upgrade(trp.peasant_woman, trp.female_camp_defender, trp.female_tracker)
define_troop_upgrade(trp.female_camp_defender, trp.female_pike_sister, trp.female_stable_maiden)

# Merc Female Archer Branch
define_troop_upgrade(trp.female_tracker, trp.female_archer)
define_troop_upgrade(trp.female_archer, trp.female_huntress)
define_troop_upgrade(trp.female_huntress, trp.female_master_huntress)
define_troop_upgrade(trp.female_master_huntress, trp.female_stalker)

# Merc Female Infantry
define_troop_upgrade(trp.female_pike_sister, trp.female_pike_maiden)
define_troop_upgrade(trp.female_pike_maiden, trp.female_line_sister)
define_troop_upgrade(trp.female_line_sister, trp.female_line_maiden)

# Merc Female Skirmishers
define_troop_upgrade(trp.female_stable_maiden, trp.female_sister_in_arms)
define_troop_upgrade(trp.female_sister_in_arms, trp.female_shield_sister)
define_troop_upgrade(trp.female_shield_sister, trp.female_shield_mistress)
define_troop_upgrade(trp.female_shield_mistress, trp.female_shield_maiden)

# Male
define_troop_upgrade(trp.farmer, trp.mercenary_rabble, trp.mercenary_skirmisher)
define_troop_upgrade(trp.mercenary_rabble, trp.mercenary_watchman, trp.mercenary_stablehand)

# Merc Male Crossbow Branch
define_troop_upgrade(trp.mercenary_skirmisher, trp.mercenary_crossbowman)
define_troop_upgrade(trp.mercenary_crossbowman, trp.mercenary_trained_crossbowman)
define_troop_upgrade(trp.mercenary_trained_crossbowman, trp.mercenary_veteran_crossbowman)
define_troop_upgrade(trp.mercenary_veteran_crossbowman, trp.mercenary_sniper)

# Merc Male Infantry
define_troop_upgrade(trp.mercenary_watchman, trp.mercenary_guard)
define_troop_upgrade(trp.mercenary_guard, trp.mercenary_swordsman)
define_troop_upgrade(trp.mercenary_swordsman, trp.mercenary_zweihander)

# Merc Male Cavalary
define_troop_upgrade(trp.mercenary_stablehand, trp.mercenary_scout)
define_troop_upgrade(trp.mercenary_scout, trp.mercenary_equite)
define_troop_upgrade(trp.mercenary_equite, trp.mercenary_cavalry)

# End Mercenary Upgrade Paths NE 600 Series

#Swadian Upgrade Paths NE 600 Series
#Swadian Recruits
define_troop_upgrade(trp.swadian_recruit, trp.swadian_proselyte)
define_troop_upgrade(trp.swadian_proselyte, trp.swadian_infantry, trp.swadian_skirmisher)
#Swadian Skirmisher Branch
define_troop_upgrade(trp.swadian_skirmisher, trp.swadian_untrained_crossbowman)
define_troop_upgrade(trp.swadian_untrained_crossbowman, trp.swadian_crossbowman)
define_troop_upgrade(trp.swadian_crossbowman, trp.swadian_veteran_crossbowman)

#Swadian Infantry Branch
define_troop_upgrade(trp.swadian_infantry, trp.swadian_sergeant, trp.swadian_page)
define_troop_upgrade(trp.swadian_sergeant, trp.swadian_pikeman, trp.swadian_swordsman)
define_troop_upgrade(trp.swadian_pikeman, trp.swadian_halberdier)
define_troop_upgrade(trp.swadian_swordsman, trp.swadian_captain)

#Swadian Cavalary Branch
define_troop_upgrade(trp.swadian_page, trp.swadian_squire)
define_troop_upgrade(trp.swadian_squire, trp.swadian_senior_squire)

#Swadian Noble Branch
define_troop_upgrade(trp.swadian_man_at_arms, trp.swadian_knight)
define_troop_upgrade(trp.swadian_knight, trp.swadian_cavalier)

# End Swadian Upgrade paths NE 600 Series

#NE Vaegir Upgrade paths NE 600 series
define_troop_upgrade(trp.vaegir_recruit, trp.vaegir_footman)
define_troop_upgrade(trp.vaegir_footman, trp.vaegir_sergeant, trp.vaegir_bowman)

#Vaegir Archer Branch
define_troop_upgrade(trp.vaegir_bowman, trp.vaegir_archer)
define_troop_upgrade(trp.vaegir_archer, trp.vaegir_marksman)
define_troop_upgrade(trp.vaegir_marksman, trp.vaegir_master_bowyer)

#Vaegir Infantry branch
define_troop_upgrade(trp.vaegir_sergeant, trp.vaegir_scout, trp.vaegir_varangian)
define_troop_upgrade(trp.vaegir_varangian, trp.vaegir_pikeman, trp.vaegir_veteran_varangian)
define_troop_upgrade(trp.vaegir_veteran_varangian, trp.vaegir_varangian_guard)
define_troop_upgrade(trp.vaegir_pikeman, trp.vaegir_lineman)

#Vaegir Cavalry Branch
define_troop_upgrade(trp.vaegir_scout, trp.vaegir_horseman)
define_troop_upgrade(trp.vaegir_horseman, trp.vaegir_druzhina)

#Vaegir Noble Branch
define_troop_upgrade(trp.vaegir_ivory_bowman, trp.vaegir_ivory_archer)
define_troop_upgrade(trp.vaegir_ivory_archer, trp.vaegir_ivory_marksman)
# End Vaegir upgrade paths NE 600 series

# Khergit Upgrade Paths NE 600 Series
define_troop_upgrade(trp.khergit_tribesman, trp.khergit_rider, trp.khergit_kharash)
define_troop_upgrade(trp.khergit_kharash, trp.khergit_kharash_scout, trp.khergit_scarred_kharash)
define_troop_upgrade(trp.khergit_rider, trp.khergit_horse_archer, trp.khergit_lancer)

# Khergit Infantry Branch
define_troop_upgrade(trp.khergit_scarred_kharash, trp.khergit_savage_kharash)

# Khergit Scout Branch
define_troop_upgrade(trp.khergit_kharash_scout, trp.khergit_kharash_rider)
define_troop_upgrade(trp.khergit_kharash_rider, trp.khergit_kharash_clansman)

# Khergit Lancer Branch
define_troop_upgrade(trp.khergit_lancer, trp.khergit_scarred_lancer)
define_troop_upgrade(trp.khergit_scarred_lancer, trp.khergit_savage_lancer)

# Khergit Horse Archer Branch
define_troop_upgrade(trp.khergit_horse_archer, trp.khergit_veteran_horse_archer)
define_troop_upgrade(trp.khergit_veteran_horse_archer, trp.khergit_master_horse_archer)

# Khergit Noble Branch
define_troop_upgrade(trp.khergit_tribal_chieftain, trp.khergit_elite_horse_archer, trp.khergit_tarkhan)
define_troop_upgrade(trp.khergit_elite_horse_archer, trp.khergit_mangudai)
define_troop_upgrade(trp.khergit_tarkhan, trp.khergit_jurtchi)

# End Khergit Upgrade Paths NE 600 Series

# Nord Upgrade Paths NE 600 Series
define_troop_upgrade(trp.nord_recruit, trp.nord_thrall)
define_troop_upgrade(trp.nord_thrall, trp.nord_drengr, trp.nord_raiding_hunter)

# Nord Raider Branch
define_troop_upgrade(trp.nord_raiding_hunter, trp.nord_raiding_archer)
define_troop_upgrade(trp.nord_raiding_archer, trp.nord_raiding_marksman)
define_troop_upgrade(trp.nord_raiding_marksman, trp.nord_skald)

# Nord Infantry Branch
define_troop_upgrade(trp.nord_drengr, trp.nord_warrior, trp.nord_butsecarl)
define_troop_upgrade(trp.nord_warrior, trp.nord_shieldmaster, trp.nord_veteran_warrior)
define_troop_upgrade(trp.nord_shieldmaster, trp.nord_merkismathr)
define_troop_upgrade(trp.nord_veteran_warrior, trp.nord_berserker)

# Nord Cavalry Branch
define_troop_upgrade(trp.nord_butsecarl, trp.nord_lithman)
define_troop_upgrade(trp.nord_lithman, trp.nord_viking)

# Nord Noble Branch
define_troop_upgrade(trp.nord_housecarl, trp.nord_champion_housecarl)
define_troop_upgrade(trp.nord_champion_housecarl, trp.nord_thane)

# End Nord Upgrade Paths 600 series

#Nord Upgrade Paths

# Rhodok Upgrade Paths NE 600 series
define_troop_upgrade(trp.rhodok_tribesman, trp.rhodok_reservist, trp.rhodok_spearman)
define_troop_upgrade(trp.rhodok_reservist, trp.rhodok_crossbowman, trp.rhodok_skirmisher)
define_troop_upgrade(trp.rhodok_spearman, trp.rhodok_veteran_spearman, trp.rhodok_swordsman)

#Rhodok Infantry
define_troop_upgrade(trp.rhodok_veteran_spearman, trp.rhodok_adept_spearman)
define_troop_upgrade(trp.rhodok_adept_spearman, trp.rhodok_master_spearman)
define_troop_upgrade(trp.rhodok_swordsman, trp.rhodok_master_swordsman)

#Rhodok Crossbow
define_troop_upgrade(trp.rhodok_crossbowman, trp.rhodok_veteran_crossbowman)
define_troop_upgrade(trp.rhodok_veteran_crossbowman, trp.rhodok_sharpshooter)

#Rhodok Skirmishers
define_troop_upgrade(trp.rhodok_skirmisher, trp.rhodok_scout)
define_troop_upgrade(trp.rhodok_scout, trp.rhodok_veteran_scout)

#Rhodok Nobles
define_troop_upgrade(trp.rhodok_armsman, trp.rhodok_horseman, trp.rhodok_councilman)
define_troop_upgrade(trp.rhodok_councilman, trp.rhodok_champion)
define_troop_upgrade(trp.rhodok_horseman, trp.rhodok_spear_horseman)

# End Rhodok Upgrade Paths NE 600 series

#Manhunter Upgrade Paths
define_troop_upgrade(trp.manhunter, trp.manhunter_t2)
define_troop_upgrade(trp.manhunter_t2, trp.manhunter_t3)
define_troop_upgrade(trp.manhunter_t3, trp.manhunter_t4)
define_troop_upgrade(trp.manhunter_t4, trp.manhunter_t5)

#Dark Knight Upgrade Paths
define_troop_upgrade(trp.dark_initiate, trp.dark_acolyte)
define_troop_upgrade(trp.dark_acolyte, trp.dark_page, trp.dark_skirmisher)
define_troop_upgrade(trp.dark_page, trp.dark_squire)
define_troop_upgrade(trp.dark_squire, trp.dark_knight)
define_troop_upgrade(trp.dark_knight, trp.dark_knight_master)
define_troop_upgrade(trp.dark_knight_master, trp.dark_champion)
define_troop_upgrade(trp.dark_champion, trp.shadow_knight)
define_troop_upgrade(trp.shadow_knight, trp.unholy_crusader)
define_troop_upgrade(trp.unholy_crusader, trp.blackguard)
define_troop_upgrade(trp.blackguard, trp.champion_blackguard)
define_troop_upgrade(trp.champion_blackguard, trp.blackguard_lord)
define_troop_upgrade(trp.dark_skirmisher, trp.dark_archer)
define_troop_upgrade(trp.dark_archer, trp.dark_marksman)
define_troop_upgrade(trp.dark_marksman, trp.dark_sharpshooter)
define_troop_upgrade(trp.dark_sharpshooter, trp.dark_ranger)

# Sarranid Upgrade Paths NE 600 Series
define_troop_upgrade(trp.sarranid_recruit, trp.sarranid_seyman, trp.sarranid_azap)
define_troop_upgrade(trp.sarranid_azap, trp.sarranid_akinci, trp.sarranid_kamandaran)
define_troop_upgrade(trp.sarranid_seyman, trp.sarranid_janissary, trp.sarranid_timariot)

#Sarranid Archer Branch
define_troop_upgrade(trp.sarranid_kamandaran, trp.sarranid_kamandaran_serden)

#Sarranid Skirmisher Branch
define_troop_upgrade(trp.sarranid_akinci, trp.sarranid_akinci_deliler)
define_troop_upgrade(trp.sarranid_akinci_deliler, trp.sarranid_akinci_serden)

#Sarranid Infantry Branch
define_troop_upgrade(trp.sarranid_janissary, trp.sarranid_dervish)
define_troop_upgrade(trp.sarranid_dervish, trp.sarranid_dailamite)

#Sarranid Cavalry Branch
define_troop_upgrade(trp.sarranid_timariot, trp.sarranid_mamluke)
define_troop_upgrade(trp.sarranid_mamluke, trp.sarranid_cataphract)

#Sarranid Noble Branch
define_troop_upgrade(trp.sarranid_eunuch, trp.sarranid_ghazi, trp.sarranid_siphai)
define_troop_upgrade(trp.sarranid_ghazi, trp.sarranid_spahbod)
define_troop_upgrade(trp.sarranid_siphai, trp.sarranid_bey)

# End Sarranid Upgrade Paths NE 600 Series
# End NE 600 Series Troop Update Paths

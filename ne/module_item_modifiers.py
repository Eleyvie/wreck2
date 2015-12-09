####################################################################################################################
#  Each item modifier record contains the following fields:
#  1) Modifier id: used for referencing modifiers in other files.
#  2) Modifier name: how this modifier will change item name, with %s being substituted by item's base name.
#  3) Price modifier: coefficient for item price when modifier is in effect.
#  4) Rarity modifier: how common are items with this modifier.
####################################################################################################################

item_modifiers = [

    ("plain", "%s",                     1.000000, 1.000000), # DEFAULT
    ("battered", "Battered %s",         0.450000, 0.800000), # -5 damage, -4 armor, -46 hp
    ("cracked", "Cracked %s",           0.600000, 0.900000), # -3 damage, -3 armor
    ("bent", "Bent %s",                 0.500000, 0.850000), # -3 damage,                   -3 speed
    ("chipped", "Chipped %s",           0.900000, 0.950000), # -1 damage
    ("old", "Old %s",                   0.750000, 0.900000), #            -2 armor, -26 hp
    ("decent", "Decent %s",             1.400000, 0.900000), # (used for clothing, goods, food)
    ("tarnished", "Tarnished %s",       0.850000, 0.850000), # -2 damage, -1 armor
    ("appetizing", "Appetizing %s",     2.250000, 0.800000), # (used for food)
    ("refined", "Refined %s",           2.900000, 0.550000), # (used for clothing, goods, food)
    ("fine", "Fine %s",                 1.800000, 0.650000), # +1 damage
    ("flavored", "Flavored %s",         3.300000, 0.500000), # (used for food)
    ("elegant", "Elegant %s",           4.900000, 0.200000), # (used for clothing, goods)
    ("deadly", "Deadly %s",             8.200000, 0.250000), # +3 damage,                   +3 speed
    ("tempered", "Tempered %s",        11.700000, 0.100000), # +4 damage
    ("flawless", "Flawless %s",         6.600000, 0.100000), # (used for clothing, goods)
    ("delicious", "Delicious %s",       7.100000, 0.350000), # (used for food)
    ("masterwork", "Masterwork %s",    16.500000, 0.020000), # +5 damage,                   +1 speed, +4 prerequisite
    ("heavy", "Heavy %s",               2.150000, 0.600000), # +2 damage, +3 armor, +10 hp, -2 speed, +1 prerequisite, +4 horse charge
    ("powerful", "Powerful %s",         4.800000, 0.350000), # +3 damage,                   -3 speed, +2 preresuisite
    ("exquisite", "Exquisite %s",       9.800000, 0.150000), # (used for clothing, goods, food)
    ("makeshift", "Makeshift %s",       0.600000, 0.850000), #            -3 armor
    ("crude", "Crude %s",               0.800000, 0.950000), #            -2 armor
    ("delectable", "Delectable %s",    11.600000, 0.150000), # (used for food)
    ("sturdy", "Sturdy %s",             1.850000, 0.550000), #            +1 armor
    ("tough", "Tough %s",               3.250000, 0.500000), #            +2 armor, +47 hp
    ("hardened", "Hardened %s",         5.500000, 0.250000), #            +3 armor
    ("superior", "Superior %s",         7.400000, 0.150000), #            +4 armor, +83 hp
    ("pungent", "Pungent %s",           0.450000, 0.200000), # (used for food)
    ("lordly", "Lordly %s",            14.300000, 0.050000), #            +6 armor, +155 hp
    ("lame", "Lame %s",                 0.650000, 0.750000), # -5 horse maneuver (weapon speed), -10 horse (projectile) speed
    ("shabby", "Shabby %s",             0.700000, 0.950000), # -2 horse maneuver (weapon speed), -4 horse (projectile) speed
    ("unwieldy", "Unwieldy %s",         0.700000, 1.000000), #                       +5 hp,           +1 prerequisite
    ("balanced", "Balanced %s",         2.500000, 0.100000), #                                        -1 prerequisite
    ("exotic", "Exotic %s",            20.000000, 0.010000), # (used for goods, food)
    ("restless", "Restless %s",         2.400000, 0.200000), # +1 horse maneuver (weapon speed), +2 horse (projectile) speed, +1 horse charge, +1 prerequisite
    ("spirited", "Spirited %s",         5.750000, 0.100000), # +2 horse maneuver (weapon speed), +4 horse (projectile) speed, +2 horse charge, +2 prerequisite
    ("fresh", "Fresh %s",               1.000000, 1.000000), # (used for perishable foods)
    ("day_old", "Day-old %s",           1.000000, 1.000000), # (used for perishable foods)
    ("two_day_old", "Two Days-old %s",  0.850000, 1.000000), # (used for perishable foods)
    ("smelling", "Smelling %s",         0.350000, 1.000000), # (used for perishable foods)
    ("rotten", "Rotten %s",             0.050000, 1.000000), # (used for perishable foods)
    ("large_bag", "Large Bag of %s",    1.900000, 0.250000), # increased item amount, repeated shot for crossbows

]

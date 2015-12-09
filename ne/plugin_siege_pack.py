from compiler import *
register_plugin()

def preprocess_entities(glob):

	scene_def = glob['scenes'][int(WRECK.scn(scene_name))]
	scene_def[7] = terrain_code
	scene_def[10] = border_terrain

('town_2_center', '0x0000000030015f2b000350d4000011a4000017ee000054af', 'sea_outer_terrain_1'),
('town_13_center', '0x300416a600035cd600007ee80000012100003fbc', 'sea_outer_terrain_2'),

('town_2_walls', '0x00000001300010c800054d5c00004af000005d3f00002ca0', 'sea_outer_terrain_1'),

('village_3', '0x000000023003dc4e0006118b000029f8000034670000105f', 'sea_outer_terrain_1'),
('village_5', '0x000000003001ce100006097d0000134c000016d8000042a2', 'sea_outer_terrain_1'),
('village_29', '0x000000023007b2320004f93c000023ed000053e500002949', 'sea_outer_terrain_1'),
('village_30', '0x0000000230079cb20005394e00001ef90000753000000731', 'sea_outer_terrain_1'),
('village_35', '0x0000000230079cb20005394e00001ef90000753000000731', 'sea_outer_terrain_1'),
('village_36', '0x000000013003a1560006118d00003ce300004123000043b2', 'sea_outer_terrain_1'),
('village_53', '0x000000023002dd19000691a40000566a000012a000001037', 'sea_outer_terrain_1'),
('village_61', '0x00000001300325350006659e0000603500006b0200005676', 'sea_outer_terrain_1'),
('village_72', '0x00000006300654ac00062d910000635800007c9600005d35', 'sea_outer_terrain_1'),
('village_77', '0x000000023009629a0005615800005564000023590000579e', 'sea_outer_terrain_1'),
('village_81', '0x0000000230025e0a0004dd3700004822000032ea0000011b', 'sea_outer_terrain_1'),
('village_83', '0x000000013007b2320005956300001e640000462c00003a51', 'sea_outer_terrain_1'),
('village_90', '0x000000012002cd900005314c00001f6d00006d7700003493', 'sea_outer_terrain_1'),

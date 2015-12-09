from compiler import *
register_plugin()

def preprocess_entities(glob):

	#armor_types = ['head', 'body', 'foot', 'hand']
	#armors = []
	#for item in glob['items']:
	#	if itp_type_head_armor <= (item[3] & 0xFF) <= itp_type_hand_armor:
	#		line = [item[0], item[1], item[2][0][0], '', armor_types[(item[3] & 0xFF) - itp_type_head_armor]]
	#		if item[3] & itp_unique: line.append('unique')
	#		elif item[3] & itp_merchandise: line.append('merchandise')
	#		else: line.append('rare')
	#		if item[3] & itp_civilian: line.append('civilian')
	#		else: line.append('')
	#		line.append('yes' if (item[3] & itp_fit_to_head) else '')
	#		line.append('yes' if (item[3] & itp_attach_armature) else '')
	#		line.append('yes' if (item[3] & itp_covers_head) else '')
	#		line.append('' if (item[3] & itp_doesnt_cover_hair) else 'yes')
	#		line.append('yes' if (item[3] & itp_covers_beard) else '')
	#		line.append('yes' if (item[3] & itp_covers_legs) else '')
	#		line.append(str(item[5]))
	#		line.extend([str(item[6].get('abundance', 100)), ('%.2f' % item[6].get('weight', 0)).replace('.', ','), str(item[6].get('diff', 0)), str(item[6].get('head', 0)), str(item[6].get('body', 0)), str(item[6].get('leg', 0))])
	#		line.append('none')
	#		line.append('')
	#		armors.append(';'.join(line))
	#with open('export_armors.csv', 'w+b') as f: f.write("\r\n".join(armors))
	#raise Exception('export successful')

	#lines = []
	#for item in glob['items']:
	#	if (item[3] & 0xFF) == itp_type_horse:
	#		line = [item[0], item[1], item[2][0][0], 'normal', str(item[5]), str(item[6].get('abundance', 100)), str(item[6].get('hp', 0)), str(item[6].get('body', 0)), str(item[6].get('diff', 0)), str(item[6].get('msspd', 0)), str(item[6].get('speed', 0)), str(item[6].get('thrust', 0) & ibf_armor_mask), str(item[6].get('size', 100)), '', 'basic']
	#		lines.append(';'.join(line))
	#with open('export_horses.csv', 'w+b') as f: f.write("\r\n".join(lines))
	#raise Exception('export successful')

	lines = []
	for item in glob['items']:
		if (item[3] & 0xFF) == itp_type_shield:
			line = [item[0], item[1], item[2][0][0], '']
			if item[3] & itp_unique: line.append('unique')
			elif item[3] & itp_merchandise: line.append('merchandise')
			else: line.append('rare')
			line.append('yes' if (item[3] & itp_wooden_parry) else '')
			line.append('yes' if (item[3] & itp_cant_use_on_horseback) else '')
			if item[4] & itcf_carry_kite_shield: line.append('kite')
			elif item[4] & itcf_carry_round_shield: line.append('round')
			elif item[4] & itcf_carry_buckler_shield: line.append('buckler')
			elif item[4] & itcf_carry_board_shield: line.append('board')
			else: line.append('???')
			line.extend([str(item[5]), str(item[6].get('abundance', 100)), ('%.2f' % item[6].get('weight', 0)).replace('.', ','), str(item[6].get('diff', 0)), str(item[6].get('size', 0)), str(item[6].get('msspd', '')),
			str(item[6].get('body', 0)), str(item[6].get('hp', 0)), str(item[6].get('speed', 0)), 'shield', ''])
			lines.append(';'.join(line))
	with open('export_shields.csv', 'w+b') as f: f.write("\r\n".join(lines))
	raise Exception('export successful')


#  0                   1                       2                          3                                                    4  5
# ["hera_plate_armor", "Heraldic Plate Armor", [("full_plate_armor", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 6553,
# 6                                                                     7               8
# weight(27)|abundance(100)|body_armor(55)|leg_armor(17)|difficulty(9), imodbits_armor, [(ti_on_init_item, [(store_trigger_param_1, ":agent_id"), (store_trigger_param_2, ":troop_id"), (call_script, "script_shield_item_set_banner", "tableau_heraldic_full_plate", ":agent_id", ":troop_id")])],
# 9
# []],

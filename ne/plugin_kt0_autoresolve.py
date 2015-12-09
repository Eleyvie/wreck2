from compiler import *
register_plugin()



scripts = [

	# Lav's replacement for kt0 compile-time troop evaluation code
	("autoresolve_evaluate_troop", [
		(store_script_param, l.troop, 1),
		(try_begin),
			(this_or_next|troop_is_hero, l.troop), # Recalculate if it's a hero troop since hero inventory can change
			(troop_slot_eq, l.troop, kt_slot_troop_type, 0), # Otherwise only recalculate once
			(store_skill_level, l.ironflesh, 36, l.troop), # Use hardcoded skill id as it can be renamed in module
			(store_skill_level, l.power_strike, 35, l.troop), # Use hardcoded skill id as it can be renamed in module
			(store_skill_level, l.power_throw, 34, l.troop), # Use hardcoded skill id as it can be renamed in module
			(store_skill_level, l.power_draw, 33, l.troop), # Use hardcoded skill id as it can be renamed in module
#(debug_values, l.ironflesh, l.power_strike, l.power_throw, l.power_draw),
			(val_mul, l.ironflesh, 2),
			(val_mul, l.power_strike, 8),
			(val_add, l.power_strike, 100),
			(val_mul, l.power_throw, 10),
			(val_add, l.power_throw, 100),
#(debug_values, l.ironflesh, l.power_strike, l.power_throw),
			(store_attribute_level, l.strength, l.troop, ca_strength),
			(assign, l.max_slot_id, num_equipment_kinds),
			(try_begin),
				(neg|troop_is_hero, l.troop),
				(troop_get_inventory_capacity, l.max_slot_id, l.troop), # If it's a regular troop we need to check entire inventory
			(try_end),
			# Initialize resulting values
			(assign, l.helmet_def, 0), (assign, l.helmet_count, 0),
			(assign, l.armor_def, 0),  (assign, l.armor_count, 0),
			(assign, l.gloves_def, 0), (assign, l.gloves_count, 0),
			(assign, l.boots_def, 0),  (assign, l.boots_count, 0),
			(assign, l.shield_def, 0), (assign, l.shield_count, 0),
			(assign, l.melee_off, 0),  (assign, l.melee_count, 0),
			(assign, l.ranged_off, 0), (assign, l.ranged_count, 0),
			(assign, l.thrown_off, 0), (assign, l.thrown_count, 0),
			(assign, l.ammo_off, 0),   (assign, l.ammo_count, 0),
			(assign, l.horse_val, 0),  (assign, l.horse_count, 0),
			# Iterate through items
			(try_for_range, l.slot_id, 0, l.max_slot_id),
				(troop_get_inventory_slot, l.item, l.troop, l.slot_id),
				(ge, l.item, 0),
				(item_get_type, l.item_type, l.item),
				(troop_get_inventory_slot_modifier, l.modifier, l.troop, l.slot_id),
#(debug_values, l.slot_id, l.item, l.modifier),
				(try_begin),
					(is_between, l.item_type, itp_type_one_handed_wpn, itp_type_polearm + 1),
					# Melee weapon
					(store_sub, l.proficiency, l.item_type, itp_type_one_handed_wpn),
					(store_proficiency_level, l.coeff, l.troop, l.proficiency),
					(item_get_speed_rating, l.speed, l.item),
					(val_mul, l.coeff, l.speed),
					(val_mul, l.coeff, l.power_strike),
					# Base damage
					(item_modifier_get_damage, l.bonus_damage, l.modifier),
					(item_get_swing_damage, l.damage, l.item),
					(val_add, l.damage, l.bonus_damage),
					(item_get_swing_damage_type, l.damage_type, l.item),
					(try_begin),
						(eq, l.damage_type, pierce),
						(val_mul, l.damage, 3),
						(val_rshift, l.damage, 1),
					(else_try),
						(eq, l.damage_type, blunt),
						(val_mul, l.damage, 5),
						(val_rshift, l.damage, 2),
					(try_end),
					(item_get_thrust_damage, l.thrust, l.item),
					(val_add, l.thrust, l.bonus_damage),
					(item_get_thrust_damage_type, l.damage_type, l.item),
					(try_begin),
						(eq, l.damage_type, pierce),
						(val_mul, l.thrust, 3),
						(val_rshift, l.thrust, 1),
					(else_try),
						(eq, l.damage_type, blunt),
						(val_mul, l.thrust, 5),
						(val_rshift, l.thrust, 2),
					(try_end),
					(val_max, l.damage, l.thrust),
#(debug_values, l.damage, l.bonus_damage, l.coeff),
					# Apply coefficients and save
					(val_mul, l.damage, l.coeff),
					(val_div, l.damage, 1000000),
					(val_add, l.melee_off, l.damage),
					(val_add, l.melee_count, 1),
#(debug_values, l.melee_off, l.melee_count),
				(else_try),
					(is_between, l.item_type, itp_type_bow, itp_type_thrown + 1),
					# Bow or crossbow
					(store_sub, l.proficiency, l.item_type, itp_type_bow - 3),
					(store_proficiency_level, l.coeff, l.troop, l.proficiency),
					(item_get_speed_rating, l.value, l.item),
					(val_mul, l.coeff, l.value),
					(item_get_accuracy, l.value, l.item),
					(try_begin),
						(eq, l.value, 0),
						(assign, l.value, 100),
					(try_end),
					(val_mul, l.coeff, l.value),
					# Base damage
					(item_modifier_get_damage, l.bonus_damage, l.modifier),
					(item_get_thrust_damage, l.damage, l.item),
					(val_add, l.damage, l.bonus_damage),
					(item_get_thrust_damage_type, l.damage_type, l.item),
					(try_begin),
						(eq, l.damage_type, pierce),
						(val_mul, l.damage, 3),
						(val_rshift, l.damage, 1),
					(else_try),
						(eq, l.damage_type, blunt),
						(val_mul, l.damage, 5),
						(val_rshift, l.damage, 2),
					(try_end),
					# Apply coefficients and power draw
					(val_mul, l.damage, l.coeff),
					(try_begin),
						(eq, l.item_type, itp_type_bow),
						(item_get_difficulty, l.real_power_draw, l.item),
						(val_add, l.real_power_draw, 4),
						(val_min, l.real_power_draw, l.power_draw),
						(val_mul, l.real_power_draw, 14),
						(val_add, l.real_power_draw, 100),
						(val_mul, l.damage, l.real_power_draw),
						(val_div, l.damage, 100),
					(else_try),
						(eq, l.item_type, itp_type_thrown),
						(val_mul, l.damage, l.power_throw),
						(val_div, l.damage, 100),
					(try_end),
					(val_div, l.damage, 1000000),
#(debug_values, l.damage, l.bonus_damage, l.real_power_draw),
					# Save
					(try_begin),
						(eq, l.item_type, itp_type_thrown),
						(val_add, l.thrown_off, l.damage),
						(val_add, l.thrown_count, 1),
					(else_try),
						(val_add, l.ranged_off, l.damage),
						(val_add, l.ranged_count, 1),
					(try_end),
#(debug_values, l.ranged_off, l.ranged_count, l.thrown_off, l.thrown_count),
				(else_try),
					(is_between, l.item_type, itp_type_arrows, itp_type_bolts + 1),
					(item_modifier_get_damage, l.bonus_damage, l.modifier),
					(item_get_thrust_damage, l.damage, l.item),
					(val_add, l.damage, l.bonus_damage),
					# Save
					(val_add, l.ammo_off, l.damage),
					(val_add, l.ammo_count, 1),
#(debug_values, l.ammo_off, l.ammo_count),
				(else_try),
					(is_between, l.item_type, itp_type_head_armor, itp_type_hand_armor + 1),
					(item_get_head_armor, l.ha, l.item),
					(item_get_body_armor, l.ba, l.item),
					(item_get_leg_armor, l.la, l.item),
					(item_modifier_get_armor, l.bonus_armor, l.modifier),
					(try_begin),
						(gt, l.ha, 0), (val_add, l.ha, l.bonus_armor), (val_max, l.ha, 0),
					(try_end),
					(try_begin),
						(gt, l.ba, 0), (val_add, l.ba, l.bonus_armor), (val_max, l.ba, 0),
					(try_end),
					(try_begin),
						(gt, l.la, 0), (val_add, l.la, l.bonus_armor), (val_max, l.la, 0),
					(try_end),
					(val_add, l.ha, l.ba),
					(val_add, l.ha, l.la),
					(try_begin),
						(eq, l.item_type, itp_type_head_armor),
						(val_add, l.helmet_def, l.ha),
						(val_add, l.helmet_count, 1),
					(else_try),
						(eq, l.item_type, itp_type_body_armor),
						(val_add, l.armor_def, l.ha),
						(val_add, l.armor_count, 1),
					(else_try),
						(eq, l.item_type, itp_type_hand_armor),
						(val_add, l.gloves_def, l.ha),
						(val_add, l.gloves_count, 1),
					(else_try),
						(eq, l.item_type, itp_type_foot_armor),
						(val_add, l.boots_def, l.ha),
						(val_add, l.boots_count, 1),
					(try_end),
				(else_try),
					(eq, l.item_type, itp_type_shield),
					(item_get_weapon_length, l.shield, l.item),
					(val_add, l.shield_def, l.shield),
					(val_add, l.shield_count, 1),
				(else_try),
					(eq, l.item_type, itp_type_horse),
					(item_get_body_armor, l.horse, l.item),
					(item_get_thrust_damage, l.thrust, l.item),
					(item_modifier_get_armor, l.bonus_armor, l.modifier),
					(item_modifier_get_horse_charge, l.bonus_damage, l.modifier),
					(val_add, l.horse, l.bonus_armor),
					(val_add, l.thrust, l.bonus_damage),
					(val_add, l.horse, 5),
					(val_div, l.horse, 10),
					(val_add, l.horse, l.thrust),
					(val_add, l.horse_val, l.horse),
					(val_add, l.horse_count, 1),
				(try_end),
			(try_end),
			# We have aggregated all items, now calculating average values
			(try_begin),
				(gt, l.helmet_count, 0), (val_div, l.helmet_def, l.helmet_count),
			(try_end),
			(try_begin),
				(gt, l.armor_count, 0), (val_div, l.armor_def, l.armor_count),
			(try_end),
			(try_begin),
				(gt, l.gloves_count, 0), (val_div, l.gloves_def, l.gloves_count),
			(try_end),
			(try_begin),
				(gt, l.boots_count, 0), (val_div, l.boots_def, l.boots_count),
			(try_end),
			(try_begin),
				(gt, l.shield_count, 0), (val_div, l.shield_def, l.shield_count),
			(try_end),
			(try_begin),
				(gt, l.melee_count, 0), (val_div, l.melee_off, l.melee_count),
			(try_end),
			(try_begin),
				(this_or_next|eq, l.ammo_count, 0),
				(eq, l.ranged_count, 0),
				(assign, l.ranged_off, 0),
				(try_begin),
					(gt, l.thrown_count, 0),
					(store_div, l.ranged_off, l.thrown_off, l.thrown_count), # No ammo or ranged - default to thrown only!
				(try_end),
			(else_try),
				(val_mul, l.ammo_off, l.ranged_count),
				(val_div, l.ammo_off, l.ammo_count), # We increase ranged damage on average by this
				(val_add, l.ranged_off, l.ammo_off),
				(val_add, l.ranged_off, l.thrown_off),
				(val_add, l.ranged_count, l.thrown_count),
				(val_div, l.ranged_off, l.ranged_count), # True average for ranged and thrown while taking ammo in consideration
			(try_end),
			(try_begin),
				(gt, l.horse_count, 0), (val_div, l.horse_val, l.horse_count),
			(try_end),
#(debug_values, l.helmet_def, l.armor_def, l.gloves_def, l.boots_def, l.shield_def, l.melee_off, l.ranged_off, l.horse_val),
			# Divine troop type and apply guarantee flag effects
			(try_begin),
				(troop_is_hero, l.troop),
				(try_begin),
					(gt, l.horse_val, 0),
					(try_begin),
						(gt, l.ranged_off, 0),
						(troop_set_slot, l.troop, kt_slot_troop_type, kt_troop_type_mtdarcher),
					(else_try),
						(troop_set_slot, l.troop, kt_slot_troop_type, kt_troop_type_cavalry),
					(try_end),
				(else_try),
					(try_begin),
						(gt, l.ranged_off, 0),
						(troop_set_slot, l.troop, kt_slot_troop_type, kt_troop_type_archer),
					(else_try),
						(troop_set_slot, l.troop, kt_slot_troop_type, kt_troop_type_footsoldier),
					(try_end),
				(try_end),
			(else_try),
				(try_begin),
					(troop_is_guarantee_horse, l.troop),
					(gt, l.horse_val, 0),
					(try_begin),
						(troop_is_guarantee_ranged, l.troop),
						(gt, l.ranged_off, 0),
						(troop_set_slot, l.troop, kt_slot_troop_type, kt_troop_type_mtdarcher),
					(else_try),
						(troop_set_slot, l.troop, kt_slot_troop_type, kt_troop_type_cavalry),
					(try_end),
				(else_try),
					(val_div, l.horse_val, 2),
					(try_begin),
						(troop_is_guarantee_ranged, l.troop),
						(gt, l.ranged_off, 0),
						(troop_set_slot, l.troop, kt_slot_troop_type, kt_troop_type_archer),
					(else_try),
						(troop_set_slot, l.troop, kt_slot_troop_type, kt_troop_type_footsoldier),
					(try_end),
				(try_end),
			(try_end),
			# Convert resulting average values to troop ratings
			(store_add, l.troop_def, l.helmet_def, l.armor_def),
			(val_add, l.troop_def, l.gloves_def),
			(val_add, l.troop_def, l.boots_def),
			(val_add, l.troop_def, l.shield_def),
			(val_div, l.troop_def, 5),
			(val_add, l.troop_def, l.ironflesh),
			(val_add, l.troop_def, l.strength),
			(troop_set_slot, l.troop, kt_slot_troop_d_val, l.troop_def),
			(try_begin),
				(troop_is_guarantee_ranged, l.troop),
				(gt, l.ranged_off, 0),
				(val_div, l.melee_off, 3),
			(else_try),
				(val_div, l.ranged_off, 4),
			(try_end),
			(val_add, l.melee_off, l.ranged_off),
			(troop_set_slot, l.troop, kt_slot_troop_o_val, l.melee_off),
			(troop_set_slot, l.troop, kt_slot_troop_h_val, l.horse_val),
#(troop_get_slot, l.troop_type, l.troop, kt_slot_troop_type),
#(debug_values, l.troop_type, l.troop_def, l.melee_off, l.horse_val),
		(try_end),
	]),

	# kt0:  new strength calculation
	# this script makes use of new slots that are filled out at init time with
	# script code that was generated at compile time.  the range of the values
	# coming out of this script are much larger (about 100x) than the original
	# range.  furthermore, we add a defense calculation and troop count to the
	# returns.
	# INPUT:
	#      arg1:  party_id
	#      arg2:  exclude leader
	#      arg3:  is siege
	# OUTPUT:
	#      reg0:  offense value
	#      reg1:  defense value (damage redux in percent)
	#      reg2:  troop count
	( "kt_party_calculate_strength", [

		# remember our params
		(store_script_param_1, ":party"),   # party id
		(store_script_param_2, ":exclude_leader"), # also a party id apparently
		(store_script_param, ":is_siege", 3), # so we don't count horses for sieges

		# clear out our returns and temps
		(assign, reg0, 0),
		(assign, reg1, 0),
		(assign, reg2, 0),

		# figure out which stack to start with and how many we have
		(party_get_num_companion_stacks, ":num_stacks", ":party"),
		(assign, ":first_stack", 0),
		(try_begin),
			(neq, ":exclude_leader", 0),
			(assign, ":first_stack", 1),
		(try_end),

		# for each stack that we care about, grab the offense, defense and count
		# and stuff the values into our return registers.
		(try_for_range, ":i_stack", ":first_stack", ":num_stacks"),
			(party_stack_get_troop_id, ":stack_troop", ":party", ":i_stack"),
			(party_stack_get_size, ":stack_size",":party",":i_stack"),
			(party_stack_get_num_wounded, ":num_wounded",":party",":i_stack"),
			(val_sub, ":stack_size", ":num_wounded"),
			(gt, ":stack_size", 0),

			# Lav: new dynamic strength calculation
			(call_script, "script_autoresolve_evaluate_troop", ":stack_troop"),
			(troop_get_slot, ":o_val", ":stack_troop", kt_slot_troop_o_val),
			(troop_get_slot, ":d_val", ":stack_troop", kt_slot_troop_d_val),
			(troop_get_slot, ":h_val", ":stack_troop", kt_slot_troop_h_val),
			(troop_get_slot, ":tr_type", ":stack_troop", kt_slot_troop_type),
			# mul by stack size
			(val_mul, ":o_val", ":stack_size"),
			(val_mul, ":d_val", ":stack_size"),
			(val_mul, ":h_val", ":stack_size"),

			# siege checks
			(try_begin),
				# if not sieging, mounted guys get a bonus.
				(eq, ":is_siege", 0),
				(try_begin),
					# mounted archers only get 50% more defense
					(eq, ":tr_type", kt_troop_type_mtdarcher),
					(val_mul, ":d_val", 3),
					(try_begin),
					(neq, ":d_val", 0),
					(val_div, ":d_val", 2),
					(try_end),
				(else_try),
					# cavalry get 50% more attack and defense and add h_val to o_val
					(eq, ":tr_type", kt_troop_type_cavalry),
					(val_mul, ":o_val", 3),
					(try_begin),
					(neq, ":o_val", 0),
					(val_div, ":o_val", 2),
					(try_end),
					(val_add, ":o_val", ":h_val"),
					(val_mul, ":d_val", 3),
					(try_begin),
					(neq, ":d_val", 0),
					(val_div, ":d_val", 2),
					(try_end),

				(try_end),
				(val_add, ":o_val", ":h_val"),
			(try_end),

			# add stuff up
			(val_add, reg0, ":o_val"),
			(val_add, reg1, ":d_val"),
			(val_add, reg2, ":stack_size"),
#(display_message, "@ Total Offense {reg0}, defense {reg1}, Stack size: {reg2}", 0xFFFFFF00),
		(try_end),

		# Make player's party weaker in auto-resolve (if player managed to knock himself out, he must HURT)
		(try_begin),
			(eq, ":party", "p_main_party"),
			(val_div, reg0, 2), # player party has 50% attack
			(val_mul, reg1, 3),
			(val_div, reg1, 4), # player party has 75% defence
		(try_end),

		# calculate damage redux from defense
		(try_begin),
			(neq, reg2, 0),
			(val_div, reg1, reg2), # avg defense
		(try_end),
		(val_clamp, reg1, 0, 90), # values outside this range don't work well
		(store_sub, reg1, 100, reg1), # opponent offense should be multiplied by this %
	]),

	# kt0:  this is a helper that basically calls kt_party_calculate_strength
	# for each attachment to the given party.
	# INPUT:
	#      arg1:  party_id
	#      arg2:  exclude leader of given stack (not attachments)
	#      arg3:  is_siege
	# OUTPUT:
	#      reg0:  aggregate strength
	#      reg1:  number of attached parties
	( "kt_party_calculate_strength_with_attachments", [

		# remember our params and set some initial values
		(store_script_param_1, ":root_party"),
		(store_script_param_2, ":exclude_leader"),
		(store_script_param, ":is_siege", 3),

		# call the counting script for the given party
		(call_script, "script_kt_party_calculate_strength", ":root_party", ":exclude_leader", ":is_siege"),
		(store_sub, reg1, 100, reg1),
		(assign, ":strength_so_far", reg0),
		(assign, ":def_so_far", reg1),
		(assign, ":count_so_far", reg2),
		(val_mul, ":def_so_far", ":count_so_far"),

		# for every attached party, do the same
		(party_get_num_attached_parties, ":attached_count", ":root_party"),
		(try_for_range, ":rank", 0, ":attached_count"),
			(party_get_attached_party_with_rank, ":attached_party", ":root_party", ":rank"),
			(call_script, "script_kt_party_calculate_strength", ":attached_party", 0, ":is_siege"),
			(store_sub, reg1, 100, reg1),
			(val_add, ":strength_so_far", reg0),
			(store_mul, ":def_this_party", reg1, reg2),
			(val_add, ":def_so_far", ":def_this_party"),
			(val_add, ":count_so_far", reg2),
		(try_end),

		# fill out our returns
		(assign, reg0, ":strength_so_far"),
		(assign, reg2, ":count_so_far"),
		(try_begin),
			(gt, ":count_so_far", 0),
			(val_div, ":def_so_far", ":count_so_far"),
			(store_sub, reg1, 100, ":def_so_far"),
		(else_try),
			(assign, reg1, 0),
		(try_end),
	]),

	# kt0:  there seem to be multiple ways to calculate how many fit troops
	# there are in an encounter and they all do something slightly different
	# but seem to be used for the same things.  this is a simple consolidation
	# attempt that counts guys the same way that we calculate party strengths.
	# INPUT:
	#      arg1:  party_id
	#      arg2:  exclude leader
	# OUTPUT:
	#      reg0:  viable troop count
	( "kt_count_viable_troops", [
		# remember our params
		(store_script_param_1, ":party"),   # party id
		(store_script_param_2, ":exclude_leader"), # also a party id apparently

		# clear out our return
		(assign, reg0, 0),

		# figure out which stack to start with and how many we have
		(party_get_num_companion_stacks, ":num_stacks", ":party"),
		(assign, ":first_stack", 0),
		(try_begin),
			(neq, ":exclude_leader", 0),
			(assign, ":first_stack", 1),
		(try_end),

		(try_for_range, ":i_stack", ":first_stack", ":num_stacks"),
			(party_stack_get_troop_id, ":stack_troop", ":party", ":i_stack"),
			(party_stack_get_size, ":stack_size",":party",":i_stack"),
			(party_stack_get_num_wounded, ":num_wounded",":party",":i_stack"),
			(val_sub, ":stack_size", ":num_wounded"),
			(try_begin),
				(gt, ":stack_size", 0),
				(try_begin),
					# if this stack is a hero, check health vs. the viable thresh.
					(troop_is_hero, ":stack_troop"),
					(neg|troop_is_wounded, ":stack_troop"),
					(val_add, reg0, 1),
				(else_try),
					# otherwise just add
					(val_add, reg0, ":stack_size"),
				(try_end),
			(try_end),
		(try_end),
		# reg0 should have the battle-ready count
	]),

	# kt0:  this is a helper that basically calls kt_count_viable_troops for
	# each attachment to the given party.  if the party has no attachments,
	# it just returns the given party's count.
	# INPUT:
	#      arg1:  party_id
	#      arg2:  exclude leader of given stack (not attachments)
	# OUTPUT:
	#      reg0:  viable troop count
	#      reg1:  number of attached parties
	( "kt_count_viable_troops_with_attachments",
	[
		# remember our params and set some initial values
		(store_script_param_1, ":root_party"),
		(store_script_param_2, ":exclude_leader"),

		# call the counting script for the given party
		(call_script, "script_kt_count_viable_troops", ":root_party", ":exclude_leader"),
		(assign, ":count_so_far", reg0),

		# for every attached party, do the same
		(party_get_num_attached_parties, ":attached_count", ":root_party"),
		(try_for_range, ":rank", 0, ":attached_count"),
			(party_get_attached_party_with_rank, ":attached_party", ":root_party", ":rank"),
			(call_script, "script_kt_count_viable_troops", ":attached_party", 0),
			(val_add, ":count_so_far", reg0),
		(try_end),

		# fill out our returns
		(assign, reg0, ":count_so_far"),
		(assign, reg1, ":attached_count"),
	]),

]

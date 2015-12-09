from compiler import *
register_plugin()
require_plugin('plugin_ms_extension', 'plugin_presentations', 'plugin_window_manager')



def wp(x):
	return wp_one_handed(x)|wp_two_handed(x)|wp_polearm(x)|wp_archery(x)|wp_crossbow(x)|wp_throwing(x)


# $g_lco_target
# $g_lco_operation
# $g_lco_page 0..1 instead of 0..2
# $g_lco_presentation

troops = [
	["companions_overview", "{!}Hidden", "{!}Hidden", tf_hero, 0, 0, 0, [], ATTR(4,4,4,4,1), wp(100), SKILLS(inventory_management=10), 0],
	["companions_discard",  "{!}Hidden", "{!}Hidden", tf_hero, 0, 0, 0, [], ATTR(4,4,4,4,1), wp(100), SKILLS(inventory_management=10), 0],
]
lco_storage = "trp_companions_overview"
lco_garbage = "trp_companions_discard"
lco_run_presentation = 1
lco_view_character = 2

tc_companions_overseer = -1

injection = {
	#'game_start_globals': [
	#	(assign, "$g_lco_presentation", "prsnt_equipment_overview"),
	#],
	# Add inject('dialog_top') at the very top of dialogs list.
	'dialogs_top' : [
		[anyone, "start", [(eq, "$talk_context", tc_companions_overseer)], "Here you are.", "lco_conversation_end", [(change_screen_view_character)]],
		[anyone, "lco_conversation_end", [], "Nice to know you are not forgetting me!", "close_window",   [(assign, "$window_manager_action", WM_PRESENTATION), (assign, "$window_manager_param1", "$window_manager_param2"), (jump_to_menu, "mnu_window_manager"), (change_screen_return)]],
		[anyone, "lco_conversation_end", [], "It's a honor to serve you, {sir/my lady}!", "close_window", [(assign, "$window_manager_action", WM_PRESENTATION), (assign, "$window_manager_param1", "$window_manager_param2"), (jump_to_menu, "mnu_window_manager"), (change_screen_return)]],
	],
	# Add inject('menu_reports_items') among the Reports menu items.
	'menu_reports_items': [
		("party_overseer", [], "Overview party skills and equipment", [
			(assign, "$g_lco_return_to", "mnu_reports"),
			(start_window_manager, WM_PRESENTATION, "prsnt_companions_overview"),
		]),
	],
	# Utilize hooks for looting interface (NE-related)
	'loot_interface_check': [
		(eq, "$setting_overseer_looting", 1),
		(assign, "$g_lco_garbage_troop", "trp_temp_troop"),
		#(assign, "$g_lco_page", 2),
		#(assign, "$g_lco_auto_menu", ":loot_interface_caller"), # To ensure we return to current menu once again to process some code at menu starting block
		#(jump_to_menu, "mnu_lco_presentation"),
		(assign, "$g_lco_return_to", ":loot_interface_caller"),
		(start_window_manager, WM_PRESENTATION, "prsnt_equipment_overview"), # start equipment presentation, return to calling menu
		(else_try),
	],
	# Add inject('menu_town_trade_items') in town's trade menu
	'menu_town_trade_items': [
		("sell_loot", [
			(eq, "$setting_overseer_looting", 1),
			(troop_get_inventory_capacity, ":capacity", "trp_player"),
			(try_for_range, ":slot", num_equipment_kinds, ":capacity"),
				(call_script, "script_cf_lco_slot_is_frozen", ":slot"), # Ignore frozen slots
			(else_try),
				(troop_get_inventory_slot, ":item", "trp_player", ":slot"),
				(ge, ":item", 0), # Player has item to sell
				(assign, ":capacity", 0),
			(try_end),
			(eq, ":capacity", 0), # i.e. cycle was broken because some non-frozen item was found
		], "Sell your entire loot.", [
			(jump_to_menu, "mnu_town_sell_loot"),
		]),
	],
}

simple_triggers = [
	(0, [
		(map_free),
		(gt, "$ne_key_overseer", 0),
		(key_clicked, "$ne_key_overseer"),
		(assign, "$g_lco_return_to", 0),
		(start_window_manager, WM_PRESENTATION, "prsnt_equipment_overview"), # return normally
	]),
]

DISABLED_game_menus = [
	("lco_presentation", 0, "Hidden Text", "none", [
		(jump_to_menu, "mnu_lco_presentation"), # Self-reference
		(try_begin),
			(eq, "$g_lco_page", 2),
			(start_presentation, "prsnt_equipment_overview"),
		(else_try),
			(start_presentation, "prsnt_companions_overview"),
		(try_end),
	], [
		("lco_go_back", [], "{!}Return", []),
	]),

	("lco_view_character", 0, "Hidden Text", "none", [
		(modify_visitors_at_site, "scn_conversation_scene"),
		(reset_visitors),
		(set_visitor,0, "trp_player"),
		(set_visitor,17, "$g_lco_target"),
		(set_jump_mission, "mt_conversation_encounter"),
		(jump_to_scene, "scn_conversation_scene"),
		(change_screen_map_conversation, "$g_lco_target"),
	], [
		("lco_go_back", [], "{!}Return", []),
	]),

	("lco_auto_return", 0, "Hidden Text", "none", [
		(try_begin),
			(gt, "$g_lco_auto_menu", 0),
			(jump_to_menu, "$g_lco_auto_menu"),
			(assign, "$g_lco_auto_menu", 0),
		(else_try),
			(change_screen_return),
		(try_end),
	], [
		("lco_go_back",[],"{!}Return",[]),
	]),

]

game_menus = [

	("town_sell_loot", 0, "{s1}^^Hint: inventory slots marked as frozen in Companions Overseer (with right mouse button click) are exempt from bulk selling.", "none", [
		(call_script, "script_set_town_picture"),
		(str_store_party_name, s2, "$current_town"),

		(call_script, "script_lco_sort_player_inventory"), # Most expensive items first

		(party_get_slot, "$g_inside_obj_1", "$current_town", slot_town_weaponsmith),
		(store_troop_gold, ":gold", "$g_inside_obj_1"),
		(store_free_inventory_capacity, ":space", "$g_inside_obj_1"),
		(troop_set_slot, "$g_inside_obj_1", slot_troop_tmp1, ":gold"),  # merchant current gold
		(troop_set_slot, "$g_inside_obj_1", slot_troop_tmp2, ":space"), # merchant free inventory space
		(troop_set_slot, "$g_inside_obj_1", slot_troop_tmp3, 0),        # number of items bought by this merchant

		(party_get_slot, "$g_inside_obj_2", "$current_town", slot_town_armorer),
		(store_troop_gold, ":gold", "$g_inside_obj_2"),
		(store_free_inventory_capacity, ":space", "$g_inside_obj_2"),
		(troop_set_slot, "$g_inside_obj_2", slot_troop_tmp1, ":gold"),
		(troop_set_slot, "$g_inside_obj_2", slot_troop_tmp2, ":space"),
		(troop_set_slot, "$g_inside_obj_2", slot_troop_tmp3, 0),        # number of items bought by this merchant

		(party_get_slot, "$g_inside_obj_3", "$current_town", slot_town_horse_merchant),
		(store_troop_gold, ":gold", "$g_inside_obj_3"),
		(store_free_inventory_capacity, ":space", "$g_inside_obj_3"),
		(troop_set_slot, "$g_inside_obj_3", slot_troop_tmp1, ":gold"),
		(troop_set_slot, "$g_inside_obj_3", slot_troop_tmp2, ":space"),
		(troop_set_slot, "$g_inside_obj_3", slot_troop_tmp3, 0),        # number of items bought by this merchant

		(party_get_slot, "$g_inside_obj_4", "$current_town", slot_town_merchant),
		(store_troop_gold, ":gold", "$g_inside_obj_4"),
		(store_free_inventory_capacity, ":space", "$g_inside_obj_4"),
		(troop_set_slot, "$g_inside_obj_4", slot_troop_tmp1, ":gold"),
		(troop_set_slot, "$g_inside_obj_4", slot_troop_tmp2, ":space"),
		(troop_set_slot, "$g_inside_obj_4", slot_troop_tmp3, 0),        # number of items bought by this merchant

		(assign, ":cached_value", "$g_talk_troop"),
		(assign, "$g_talk_troop", "$g_inside_obj_4"), # Use general merchant for some internal calculations
		(assign, ":profit", 0),
		(assign, ":items_sold", 0),
		(assign, ":items_offered", 0),

		(str_clear, s11),
		(str_clear, s12),
		(str_clear, s13),
		(str_clear, s14),

		(troop_get_inventory_capacity, ":capacity", "trp_player"),
		(try_for_range, ":slot", num_equipment_kinds, ":capacity"),
			(troop_set_slot, "trp_temp_troop", ":slot", 0), # Do not sell by default
			(call_script, "script_cf_lco_slot_is_frozen", ":slot"), # Ignore frozen slots
		(else_try),
			(troop_get_inventory_slot, ":item", "trp_player", ":slot"),
			(ge, ":item", 0), # Player has item to sell
			(val_add, ":items_offered", 1),
			(troop_get_inventory_slot_modifier, ":modifier", "trp_player", ":slot"),
			(troop_inventory_slot_get_item_amount, ":quantity", "trp_player", ":slot"),
			(troop_inventory_slot_get_item_max_amount, ":max_quantity", "trp_player", ":slot"),
			# Identify item selling price
			(call_script, "script_lco_get_item_price", ":item", ":modifier", ":quantity"),
			(assign, ":sell_price", reg0),
			(call_script, "script_game_get_item_sell_price_factor", ":item"),
			(val_mul, ":sell_price", reg0),
			(val_div, ":sell_price", 100),
			# Identify buyer
			(assign, ":buyer", "$g_inside_obj_1"),
			(assign, ":string", s11),
			(item_get_type, ":type", ":item"),
			(try_begin),
				(eq, ":type", itp_type_horse),
				(assign, ":buyer", "$g_inside_obj_3"),
				(assign, ":string", s13),
			(else_try),
				(is_between, ":type", itp_type_head_armor, itp_type_hand_armor + 1),
				(assign, ":buyer", "$g_inside_obj_2"),
				(assign, ":string", s12),
			(else_try),
				(this_or_next|eq, ":type", itp_type_goods),
				(ge, ":type", itp_type_animal), # i.e. animal or book
				(assign, ":buyer", "$g_inside_obj_4"),
				(assign, ":string", s14),
			(try_end),
			# If standard buyer can purchase, fallback to goods trader
			(try_begin),
				(neq, ":buyer", "$g_inside_obj_4"), # We do not check for goods trader on this iteration, as it's the fallback trader anyway
				(this_or_next|neg|troop_slot_ge, ":buyer", slot_troop_tmp2, 1),
				(neg|troop_slot_ge, ":buyer", slot_troop_tmp1, ":sell_price"),
				(assign, ":buyer", "$g_inside_obj_4"), # Fallback
				(assign, ":string", s14),
			(try_end),
			# Check that the selected buyer can purchase
			(troop_slot_ge, ":buyer", slot_troop_tmp1, ":sell_price"),
			(troop_slot_ge, ":buyer", slot_troop_tmp2, 1),
			# Yosh! Write down what merchant will buy this item
			(troop_set_slot, "trp_temp_troop", ":slot", ":buyer"),
			# Substract gold
			(troop_get_slot, ":gold", ":buyer", slot_troop_tmp1),
			(val_sub, ":gold", ":sell_price"),
			(troop_set_slot, ":buyer", slot_troop_tmp1, ":gold"),
			# Reduce inventory space
			(troop_get_slot, ":space", ":buyer", slot_troop_tmp2),
			(val_sub, ":space", 1),
			(troop_set_slot, ":buyer", slot_troop_tmp2, ":space"),
			# Add item name to displayed string
			(call_script, "script_lco_item_name_to_s41", ":item", ":modifier", ":quantity", ":max_quantity"),
			(troop_get_slot, ":count", ":buyer", slot_troop_tmp3),
			(try_begin),
				(eq, ":count", 0),
				(str_store_string_reg, ":string", s41),
			(else_try),
				(eq, ":count", 1),
				(str_store_string_reg, s50, s41),
				(str_store_string_reg, s51, ":string"),
				(str_store_string, ":string", "str_s50_and_s51"),
			(else_try),
				(str_store_string_reg, s50, s41),
				(str_store_string_reg, s51, ":string"),
				(str_store_string, ":string", "str_s50_comma_s51"),
			(try_end),
			(val_add, ":count", 1),
			(troop_set_slot, ":buyer", slot_troop_tmp3, ":count"),
			# Modify profits and generate game event
			(val_add, ":profit", ":sell_price"),
			(call_script, "script_game_event_sell_item", ":item", 0),
			(val_add, ":items_sold", 1),
		(try_end),
		(assign, "$g_inside_obj_5", 0),
		(try_begin),
			(eq, ":items_offered", 0),
			(str_store_string, s1, "@After checking your inventory, you realise that you have nothing to offer to the local merchants. Everything you have is something you need."),
		(else_try),
			(eq, ":items_sold", 0),
			(str_store_string, s1, "@After checking with the local merchants, you realise that they won't be able to buy anything that you might offer."),
		(else_try),
			(str_clear, s10),
			(try_begin),
				(troop_slot_ge, "$g_inside_obj_1", slot_troop_tmp3, 1),
				(str_store_string, s10, "@{s10}^Weapon merchant can buy {s11}."),
			(try_end),
			(try_begin),
				(troop_slot_ge, "$g_inside_obj_2", slot_troop_tmp3, 1),
				(str_store_string, s10, "@{s10}^Armor merchant can buy {s12}."),
			(try_end),
			(try_begin),
				(troop_slot_ge, "$g_inside_obj_3", slot_troop_tmp3, 1),
				(str_store_string, s10, "@{s10}^Horse merchant can buy {s13}."),
			(try_end),
			(try_begin),
				(troop_slot_ge, "$g_inside_obj_4", slot_troop_tmp3, 1),
				(str_store_string, s10, "@{s10}^General merchant can buy {s14}."),
			(try_end),
			(call_script, "script_game_get_money_text", ":profit"),
			(assign, reg0, ":items_sold"),
			(assign, reg1, ":profit"),
			(str_store_string, s1, "@After checking with the local merchants, you estimate that you can sell {reg0} items for a total of {s1}.^{s10}"),
			(assign, "$g_inside_obj_5", ":profit"),
		(try_end),

		# Restore price modifiers
		(try_for_range, ":slot", num_equipment_kinds, ":capacity"),
			(troop_slot_ge, "trp_temp_troop", ":slot", 1), # Selling to someone
			(troop_get_slot, ":buyer", "trp_temp_troop", ":slot"),
			(troop_get_inventory_slot, ":item", "trp_player", ":slot"),
			(call_script, "script_game_event_buy_item", ":item", 1), # Reclaim mode
		(try_end),

		(assign, "$g_talk_troop", ":cached_value"), # Restore previous value
	], [

		("confirm", [

			(gt, "$g_inside_obj_5", 0)

		], "Sell loot.", [

			(assign, ":cached_value", "$g_talk_troop"),
			(party_get_slot, "$g_talk_troop", "$current_town", slot_town_merchant),

			# "Sell" items
			(troop_get_inventory_capacity, ":capacity", "trp_player"),
			(try_for_range, ":slot", num_equipment_kinds, ":capacity"),
				(troop_slot_ge, "trp_temp_troop", ":slot", 1), # Selling to someone
				(troop_get_slot, ":buyer", "trp_temp_troop", ":slot"),
				(troop_get_inventory_slot, ":item", "trp_player", ":slot"),
				(troop_get_inventory_slot_modifier, ":modifier", "trp_player", ":slot"),
				(troop_inventory_slot_get_item_amount, ":quantity", "trp_player", ":slot"),
				# Sell the item.
				(troop_set_inventory_slot, "trp_player", ":slot", -1),         # Remove item from player
				(troop_add_item, ":buyer", ":item", ":modifier", ":quantity"), # Add item to buyer
				(call_script, "script_game_event_sell_item", ":item", 0),      # Generate game event
			(try_end),
			# Remove gold from merchants
			(assign, ":profit", 0),
			(try_for_range, ":slot", slot_town_weaponsmith, slot_town_horse_merchant + 1),
				(party_get_slot, ":buyer", "$current_town", ":slot"),
				(store_troop_gold, ":old_gold", ":buyer"),
				(troop_get_slot, ":new_gold", ":buyer", slot_troop_tmp1),
				(store_sub, ":amount_paid", ":old_gold", ":new_gold"),
				(gt, ":amount_paid", 0),
				(val_add, ":profit", ":amount_paid"),
				(troop_remove_gold, ":buyer", ":amount_paid"),
			(try_end),
			# Integrity check
			(try_begin),
				(neq, ":profit", "$g_inside_obj_5"),
				(assign, reg1, ":profit"),
				(assign, reg2, "$g_inside_obj_5"),
				(display_message, "@Integrity check error: merchants lost {reg1} gold, while player received {reg2} gold!", 0xff0000),
			(try_end),
			# Add gold to player
			(troop_add_gold, "trp_player", "$g_inside_obj_5"),
			(call_script, "script_adjust_finances", slot_finance_items, "$g_inside_obj_5"),

			(assign, "$g_talk_troop", ":cached_value"), # Restore previous value
			(jump_to_menu, "mnu_town_trade"),
		]),

		("cancel", [(gt, "$g_inside_obj_5", 0)], "Cancel.", [
			(jump_to_menu, "mnu_town_trade"),
		]),

		("continue", [(eq, "$g_inside_obj_5", 0)], "Continue...", [
			(jump_to_menu, "mnu_town_trade"),
		]),

	]),

]

strings = [
	# Version string
	("lco_version", "Companions Overseer v. 1.25"),

	# Interface element strings
	("lco_i_return",           "Return"),
	("lco_i_attributes",       "View Attributes"),
	("lco_i_equipment",        "View Equipment"),
	("lco_i_ae_with",          "Auto-Equip Companions With:"),
	("lco_i_ae_with_horses",   "Horses"),
	("lco_i_ae_with_armors",   "Armors"),
	("lco_i_ae_with_shields",  "Shields"),
	("lco_i_ae_companion",     "Equip Companion"),
	("lco_i_ae_everyone",      "Equip Everyone"),
	("lco_i_title_companions", "Companions"),
	("lco_i_list_companions",  "List Companions"),
	("lco_i_list_lords",       "List Kingdom Lords"),
	("lco_i_list_regulars",    "List Regular Troops"),
	("lco_i_hero_panel_title", "Accessible Companions"),
	("lco_i_weapons",          "Weapons:"),
	("lco_i_armor",            "Armor:"),
	("lco_i_horse",            "Horse:"),
	("lco_i_books",            "Books"),
	("lco_i_inventory",        "Inventory:"),
	("lco_i_discard",          "Discard/Loot:"),
	("lco_i_retrieve",         "Retrieve All Items"),
	("lco_i_denars",           "{reg60} denar(s)"), # No longer used as of V1.20
	("lco_i_character",        "Character Screen"),
	("lco_i_ie_icon",          "I/E"),

	# Slot name strings
	("lco_slot_name_0", "(weapon slot)"),
	("lco_slot_name_1", "(weapon slot)"),
	("lco_slot_name_2", "(weapon slot)"),
	("lco_slot_name_3", "(weapon slot)"),
	("lco_slot_name_4", "(helm slot)"),
	("lco_slot_name_5", "(armor slot)"),
	("lco_slot_name_6", "(boots slot)"),
	("lco_slot_name_7", "(gauntlets slot)"),
	("lco_slot_name_8", "(horse slot)"),
	("lco_slot_name_9", "(book slot)"),
	("lco_slot_name_A", "(book slot)"),
	("lco_slot_frozen", "(frozen)"),

	# Messages and error strings
	("lco_error_drop_first", "Please deposit currently dragged item somewhere first."),
	("lco_message_hero_ae", "{s41} has equipped {reg60?her:him}self from your inventory."),
	("lco_message_all_heroes_ae", "Your companions have equipped themselves from your inventory."),
	("lco_message_hero_no_need", "{s40} has no need for {s41}."),
	("lco_error_inv_full", "Cannot give item to player, inventory is full."),
	("lco_message_hero_replaced", "{s40} replaced {reg4?her:his} {s41} with {s39}."),
	("lco_message_hero_equipped", "{s40} equipped {s41}."),
	("lco_message_nobody_needs", "Nobody wants to take {s41}."),
	("lco_drop_error_type", "You cannot drop this item here!"),
	("lco_drop_error_reqs", "Item prerequisites are not met to equip it!"),
	("lco_drop_error_control", "You cannot control this troop's equipment."),
	("lco_impossible_error", "SCRIPT ERROR #001: NO SWAP ITEM FOUND."),

	# Functional strings
	("lco_drop_here", "Drop items here to discard them.^Currently {reg0} item(s) discarded."),
	("lco_s40", "{s40}"),
	("lco_reg40", "{reg40}"),
	("lco_reg40_41", "{reg40}/{reg41}"),

	# Attribute/skill/proficiency name strings
	("lco_c_level", "Level"),
	("lco_c_xp", "XP"),
	("lco_c_xp2next_level", "XP to Next Lvl"),
	("lco_c_hp", "HP/Max HP"),
	("lco_c_morale", "Morale"),
]

scripts = [

	("lco_item_name_to_s41", [
		(assign, ":ex_reg60", reg60),
		(assign, ":ex_reg61", reg61),
		(store_script_param, ":item_id", 1),
		(store_script_param, ":modifier", 2),
		(store_script_param, reg60, 3),
		(store_script_param, reg61, 4),
		(str_store_item_name, s99, ":item_id"),
		(store_add, ":str_offset", "str_item_modifier_00", ":modifier"),
		(str_store_string, s41, ":str_offset"),
		(try_begin),
			(gt, reg61, 1),
			(try_begin),
				(item_get_type, ":item_type", ":item_id"),
				(eq, ":item_type", itp_type_goods),
				(str_store_string, s41, "@{s41} ({reg60}/{reg61})"),
			(else_try),
				(str_store_string, s41, "@{s41} ({reg60})"),
			(try_end),
		(try_end),
		(assign, reg60, ":ex_reg60"),
		(assign, reg61, ":ex_reg61"),
	]),

	("lco_fill_hero_panels", [
		(try_begin),
			(eq, "$g_lco_heroes", 0),
			(call_script, "script_lco_clear_all_items", lco_storage),
			(assign, ":troop_id", lco_storage),
			(assign, "$extra_text_preq_display_2", 0),
		(else_try),
			(store_add, ":offset", "$g_lco_heroes", "$g_lco_active_hero"), # Slot ID where hero reference is stored
			(troop_get_slot, ":troop_id", lco_storage, ":offset"), # We got hero troop ID, now checking equipment
			(assign, "$extra_text_preq_display_2", ":troop_id"),
		(try_end),
		(store_mul, ":offset", "$g_lco_heroes", 2),
		(val_add, ":offset", 11), # Offset now points to first text overlay of hero equipment
		(str_clear, s40),
		(try_for_range, ":index", 0, 9),
			(store_add, ":overlay_offset", ":offset", ":index"),
			(troop_get_slot, ":overlay_id", lco_storage, ":overlay_offset"),
			(troop_get_inventory_slot, ":item_id", ":troop_id", ":index"),
			(try_begin),
				(lt, ":item_id", 0),
				(store_add, ":string_id", "str_lco_slot_name_0", ":index"),
				(overlay_set_text, ":overlay_id", ":string_id"),
				(overlay_set_color, ":overlay_id", 0x808080),
			(else_try),
				(troop_get_inventory_slot_modifier, ":modifier", ":troop_id", ":index"),
				(troop_inventory_slot_get_item_amount, ":qty", ":troop_id", ":index"),
				(troop_inventory_slot_get_item_max_amount, ":qty_max", ":troop_id", ":index"),
				(call_script, "script_lco_item_name_to_s41", ":item_id", ":modifier", ":qty", ":qty_max"),
				(overlay_set_text, ":overlay_id", s41),
				(overlay_set_color, ":overlay_id", 0x000000),
			(try_end),
		(try_end),
		# Update V1.1. Disable book slots configuration variable
		(try_begin),
			(eq, "$g_lco_suppress_books", 0),
			# Searching for books...
			(val_add, ":overlay_offset", 1),
			(assign, ":books_found", 0),
			(troop_get_inventory_capacity, ":capacity", ":troop_id"),
			(try_for_range, ":index", num_equipment_kinds, ":capacity"),
				(troop_get_inventory_slot, ":item_id", ":troop_id", ":index"),
				(ge, ":item_id", 0),
				(item_get_type, ":item_type", ":item_id"),
				(eq, ":item_type", itp_type_book),
				(troop_get_inventory_slot_modifier, ":modifier", ":troop_id", ":index"),
				(troop_inventory_slot_get_item_amount, ":qty", ":troop_id", ":index"),
				(troop_inventory_slot_get_item_max_amount, ":qty_max", ":troop_id", ":index"),
				(call_script, "script_lco_item_name_to_s41", ":item_id", ":modifier", ":qty", ":qty_max"),
				(troop_get_slot, ":overlay_id", lco_storage, ":overlay_offset"),
				(overlay_set_text, ":overlay_id", s41),
				(overlay_set_color, ":overlay_id", 0x000000),
				(val_add, ":overlay_offset", 1),
				(val_add, ":books_found", 1),
				(try_begin),
					(gt, ":books_found", 1), # Found two books, so stopping
					(assign, ":capacity", 0),
				(try_end),
			(try_end),
			(try_for_range, ":index", ":books_found", 2),
				(troop_get_slot, ":overlay_id", lco_storage, ":overlay_offset"),
				(overlay_set_text, ":overlay_id", "str_lco_slot_name_9"),
				(overlay_set_color, ":overlay_id", 0x808080),
				(val_add, ":overlay_offset", 1),
			(try_end),
		(try_end),
	]),

	("lco_fill_player_panels", [
		(store_mul, ":offset", "$g_lco_heroes", 2),
		(val_add, ":offset", 31), # Offset now points to first text overlay of player equipment
		(str_clear, s40),
		(try_for_range, ":index", 0, 9),
			(store_add, ":overlay_offset", ":offset", ":index"),
			(troop_get_slot, ":overlay_id", lco_storage, ":overlay_offset"),
			(troop_get_inventory_slot, ":item_id", "trp_player", ":index"),
			(try_begin),
				(lt, ":item_id", 0),
				(store_add, ":string_id", "str_lco_slot_name_0", ":index"),
				(overlay_set_text, ":overlay_id", ":string_id"),
				(overlay_set_color, ":overlay_id", 0x808080),
			(else_try),
				(troop_get_inventory_slot_modifier, ":modifier", "trp_player", ":index"),
				(troop_inventory_slot_get_item_amount, ":qty", "trp_player", ":index"),
				(troop_inventory_slot_get_item_max_amount, ":qty_max", "trp_player", ":index"),
				(call_script, "script_lco_item_name_to_s41", ":item_id", ":modifier", ":qty", ":qty_max"),
				(overlay_set_text, ":overlay_id", s41),
				(overlay_set_color, ":overlay_id", 0x000000),
			(try_end),
		(try_end),
		# Displaying inventory
		(store_mul, ":offset", "$g_lco_heroes", 2),
		(val_add, ":offset", 40),
		(val_add, ":offset", "$g_lco_inv_slots"),
		(try_for_range, ":index", 0, "$g_lco_inv_slots"),
			(store_add, ":inventory_offset", ":index", num_equipment_kinds), # Actual inventory slot for player
			(store_add, ":overlay_offset", ":offset", ":index"),
			(troop_get_slot, ":overlay_id", lco_storage, ":overlay_offset"), # Text overlay for slot
			# Update V1.1. Checking slot frozen status and updating text color as necessary
			(try_begin),
				(call_script, "script_cf_lco_slot_is_frozen", ":inventory_offset"),
				(overlay_set_color, ":overlay_id", 0x000000FF),
			(else_try),
				(overlay_set_color, ":overlay_id", 0x00000000),
			(try_end),
			(troop_get_inventory_slot, ":item_id", "trp_player", ":inventory_offset"),
			(try_begin),
				(lt, ":item_id", 0),
				(try_begin),
					(call_script, "script_cf_lco_slot_is_frozen", ":inventory_offset"),
					(overlay_set_color, ":overlay_id", 0x006060FF),
					(overlay_set_text, ":overlay_id", "str_lco_slot_frozen"),
				(else_try),
					(overlay_set_text, ":overlay_id", s40),
				(try_end),
			(else_try),
				(troop_get_inventory_slot_modifier, ":modifier", "trp_player", ":inventory_offset"),
				(troop_inventory_slot_get_item_amount, ":qty", "trp_player", ":inventory_offset"),
				(troop_inventory_slot_get_item_max_amount, ":qty_max", "trp_player", ":inventory_offset"),
				(call_script, "script_lco_item_name_to_s41", ":item_id", ":modifier", ":qty", ":qty_max"),
				(overlay_set_text, ":overlay_id", s41),
			(try_end),
		(try_end),
		# Displaying garbage/loot
		(val_add, ":offset", "$g_lco_inv_slots"),
		(val_add, ":offset", "$g_lco_garb_slots"),
		(try_for_range, ":index", 0, "$g_lco_garb_slots"),
			(store_add, ":overlay_offset", ":offset", ":index"),
			(troop_get_slot, ":overlay_id", lco_storage, ":overlay_offset"),
			(store_add, ":inventory_offset", ":index", num_equipment_kinds),
			(troop_get_inventory_slot, ":item_id", "$g_lco_garbage_troop", ":inventory_offset"),
			(try_begin),
				(lt, ":item_id", 0),
				(overlay_set_text, ":overlay_id", s40),
			(else_try),
				(troop_get_inventory_slot_modifier, ":modifier", "$g_lco_garbage_troop", ":inventory_offset"),
				(troop_inventory_slot_get_item_amount, ":qty", "$g_lco_garbage_troop", ":inventory_offset"),
				(troop_inventory_slot_get_item_max_amount, ":qty_max", "$g_lco_garbage_troop", ":inventory_offset"),
				(call_script, "script_lco_item_name_to_s41", ":item_id", ":modifier", ":qty", ":qty_max"),
				(overlay_set_text, ":overlay_id", s41),
			(try_end),
		(try_end),
	]),

	("cf_lco_is_active_panel", [
		(store_script_param_1, ":overlay"),
		(assign, ":found", 0),
		(store_mul, ":range1", "$g_lco_heroes", 2),
		(store_add, ":range2", ":range1", 11),
		# Checking hero equipment panels
		(try_for_range, ":index", ":range1", ":range2"),
			(troop_slot_eq, lco_storage, ":index", ":overlay"),
			(assign, ":found", 1),
		(try_end),
		# Checking player equipment panels
		(try_begin),
			(eq, ":found", 0),
			(val_add, ":range1", 22),
			(store_add, ":range2", ":range1", 9),
			(try_for_range, ":index", ":range1", ":range2"),
				(troop_slot_eq, lco_storage, ":index", ":overlay"),
				(assign, ":found", 1),
			(try_end),
		(try_end),
		# Checking player inventory panels
		(try_begin),
			(eq, ":found", 0),
			(val_add, ":range1", 18),
			(store_add, ":range2", ":range1", "$g_lco_inv_slots"),
			(try_for_range, ":index", ":range1", ":range2"),
				(troop_slot_eq, lco_storage, ":index", ":overlay"),
				(assign, ":found", 1),
			(try_end),
		(try_end),
		# Checking garbage/loot inventory panels
		(try_begin),
			(eq, ":found", 0),
			(val_add, ":range1", "$g_lco_inv_slots"), # Skipping player inventory panels
			(val_add, ":range1", "$g_lco_inv_slots"), # Skipping player inventory text labels
			(store_add, ":range2", ":range1", "$g_lco_garb_slots"),
			(try_for_range, ":index", ":range1", ":range2"),
				(troop_slot_eq, lco_storage, ":index", ":overlay"),
				(assign, ":found", 1),
			(try_end),
		(try_end),
		(eq, ":found", 1),
	]),

	("lco_get_slot_details_for_panel", [
		(store_script_param_1, ":overlay"),
		(assign, reg0, -1),
		(assign, reg1, -1),
		(assign, reg2, -1),
		(assign, reg3, 0),
		(assign, reg4, 0),
		(assign, reg5, 0),
		(assign, ":found", 0),
		# Looking for hero equipment slots
		(store_mul, ":range1", "$g_lco_heroes", 2),
		(store_add, ":range2", ":range1", 11),
		(try_for_range, ":index", ":range1", ":range2"),
			(troop_slot_eq, lco_storage, ":index", ":overlay"),
			(store_add, ":hero_offset", "$g_lco_heroes", "$g_lco_active_hero"),
			(troop_get_slot, ":troop_id", lco_storage, ":hero_offset"),
			(store_sub, ":n_index", ":index", ":range1"),
			(try_begin),
				(lt, ":n_index", 9),
				(assign, reg0, ":troop_id"),
				(assign, reg1, ":n_index"),
			(else_try),
				(call_script, "script_lco_allocate_slots_for_books", ":troop_id"), # reg0 and reg1 now contain slot ids for first two books in inventory, or for empty slots
				(try_begin),
					(eq, ":n_index", 9),
					(assign, reg1, reg0),
				(try_end),
				(assign, reg0, ":troop_id"),
			(try_end),
			(assign, ":found", 1),
		(try_end),
		# Looking for player equipment slots
		(try_begin),
			(eq, ":found", 0),
			(val_add, ":range1", 22),
			(store_add, ":range2", ":range1", 9),
			(try_for_range, ":index", ":range1", ":range2"),
				(troop_slot_eq, lco_storage, ":index", ":overlay"),
				(assign, reg0, "trp_player"),
				(store_sub, reg1, ":index", ":range1"),
				(assign, ":found", 1),
			(try_end),
		(try_end),
		# Looking for player inventory slots
		(try_begin),
			(eq, ":found", 0),
			(val_add, ":range1", 18),
			(store_add, ":range2", ":range1", "$g_lco_inv_slots"),
			(try_for_range, ":index", ":range1", ":range2"),
				(troop_slot_eq, lco_storage, ":index", ":overlay"),
				(assign, reg0, "trp_player"),
				(store_sub, reg1, ":index", ":range1"),
				(val_add, reg1, num_equipment_kinds),
				(assign, ":found", 1),
			(try_end),
		(try_end),
		# Looking for garbage/loot inventory slots
		(try_begin),
			(eq, ":found", 0),
			(val_add, ":range1", "$g_lco_inv_slots"), # Skipping player inventory panels
			(val_add, ":range1", "$g_lco_inv_slots"), # Skipping player inventory text labels
			(store_add, ":range2", ":range1", "$g_lco_garb_slots"),
			(try_for_range, ":index", ":range1", ":range2"),
				(troop_slot_eq, lco_storage, ":index", ":overlay"),
				(assign, reg0, "$g_lco_garbage_troop"),
				(store_sub, reg1, ":index", ":range1"),
				(val_add, reg1, num_equipment_kinds),
				(assign, ":found", 1),
			(try_end),
		(try_end),
		# Finally if found, filling item details
		(try_begin),
			(eq, ":found", 1),
			(troop_get_inventory_slot, reg2, reg0, reg1),
			(try_begin),
				(ge, reg2, 0),
				(troop_get_inventory_slot_modifier, reg3, reg0, reg1),
				(troop_inventory_slot_get_item_amount, reg4, reg0, reg1),
				(troop_inventory_slot_get_item_max_amount, reg5, reg0, reg1),
			(try_end),
		(try_end),
	]),

	# INPUT: arg1 = <troop_id>, arg2 = <slot_id>
	# OUTPUT: none, script modifies some $g_lco_* variables which are tracked by ti_on_presentation_run trigger in prsnt_overview_equipment
	("lco_drag_item", [
		(store_script_param_1, ":troop_id"),
		(store_script_param_2, ":slot_id"),
		(try_begin),
			(call_script, "script_cf_lco_controllable", ":troop_id"),
			(troop_get_inventory_slot, ":item_id", ":troop_id", ":slot_id"),
			(try_begin),
				(ge, ":item_id", 0),
				(assign, "$g_lco_drag_item", ":item_id"),
				(troop_get_inventory_slot_modifier, "$g_lco_drag_modifier", ":troop_id", ":slot_id"),
				(troop_inventory_slot_get_item_amount, "$g_lco_drag_quantity", ":troop_id", ":slot_id"),
				(troop_inventory_slot_get_item_max_amount, "$g_lco_drag_quantity_max", ":troop_id", ":slot_id"),
				(assign, "$g_lco_dragging_from", ":troop_id"),
				(assign, "$g_lco_dragging_from_slot", ":slot_id"),
				# Displaying overlay
				(call_script, "script_lco_item_name_to_s41", ":item_id", "$g_lco_drag_modifier", "$g_lco_drag_quantity", "$g_lco_drag_quantity_max"),
				(overlay_set_text, "$g_lco_dragging_text", s41),
				(overlay_set_display, "$g_lco_dragging_panel", 1),
				(assign, "$g_lco_dragging", 1),
				(troop_set_inventory_slot, ":troop_id", ":slot_id", -1),
				(try_begin),
					(eq, ":troop_id", "$g_lco_garbage_troop"),
					(troop_sort_inventory, "$g_lco_garbage_troop"),
				(try_end),
			(try_end),
		(else_try),
			(display_message, "str_lco_drop_error_control", 0xFF4040),
		(try_end),
	]),

	("lco_cancel_drag_item", [
		(try_begin),
			(eq, "$g_lco_dragging", 1), # Safety check
			(try_begin),
				# Trying to deposit the item where it originally belongs
				(troop_get_inventory_slot, ":stored_id", "$g_lco_dragging_from", "$g_lco_dragging_from_slot"),
				(lt, ":stored_id", 0),
				(troop_set_inventory_slot, "$g_lco_dragging_from", "$g_lco_dragging_from_slot", "$g_lco_drag_item"),
				(troop_set_inventory_slot_modifier, "$g_lco_dragging_from", "$g_lco_dragging_from_slot", "$g_lco_drag_modifier"),
				(try_begin),
					(gt, "$g_lco_drag_quantity", 0),
					(troop_inventory_slot_set_item_amount, "$g_lco_dragging_from", "$g_lco_dragging_from_slot", "$g_lco_drag_quantity"),
				(try_end),
				(assign, "$g_lco_dragging", 0),
			(else_try),
				# Original slot is occupied, so trying to drop the dragged item to player's inventory
				(troop_get_inventory_capacity, ":capacity", "trp_player"),
				(try_for_range, ":slot_id", num_equipment_kinds, ":capacity"),
					(troop_get_inventory_slot, ":stored_id", "trp_player", ":slot_id"),
					(lt, ":stored_id", 0),
					(troop_set_inventory_slot, "trp_player", ":slot_id", "$g_lco_drag_item"),
					(troop_set_inventory_slot_modifier, "trp_player", ":slot_id", "$g_lco_drag_modifier"),
					(try_begin),
						(gt, "$g_lco_drag_quantity", 0),
						(troop_inventory_slot_set_item_amount, "trp_player", ":slot_id", "$g_lco_drag_quantity"),
					(try_end),
					(assign, "$g_lco_dragging", 0),
					(assign, ":capacity", 0), # Break cycle
				(try_end),
				(eq, "$g_lco_dragging", 0), # Check for success
			(else_try),
				# Player inventory is full, trying to deposit item to garbage
				(troop_get_inventory_capacity, ":capacity", "$g_lco_garbage_troop"),
				(try_for_range, ":slot_id", num_equipment_kinds, ":capacity"),
					(troop_get_inventory_slot, ":stored_id", "$g_lco_garbage_troop", ":slot_id"),
					(lt, ":stored_id", 0),
					(troop_set_inventory_slot, "$g_lco_garbage_troop", ":slot_id", "$g_lco_drag_item"),
					(troop_set_inventory_slot_modifier, "$g_lco_garbage_troop", ":slot_id", "$g_lco_drag_modifier"),
					(try_begin),
						(gt, "$g_lco_drag_quantity", 0),
						(troop_inventory_slot_set_item_amount, "$g_lco_garbage_troop", ":slot_id", "$g_lco_drag_quantity"),
					(try_end),
					(assign, "$g_lco_dragging", 0),
					(assign, ":capacity", 0), # Break cycle
					(troop_sort_inventory, "$g_lco_garbage_troop"),
				(try_end),
			(try_end),
			# If no longer dragging, we need to make proper modifications
			(try_begin),
				(eq, "$g_lco_dragging", 0),
				(assign, "$g_lco_dragging_from", 0),      # Troop ID of dragged item current owner
				(assign, "$g_lco_dragging_from_slot", 0), # Slot ID of dragged item current owner
				(assign, "$g_lco_drag_item", -1),         # Item type currently being dragged
				(assign, "$g_lco_drag_modifier", 0),      # Modifier of item currently being dragged
				(assign, "$g_lco_drag_quantity", 0),      # Quantity of item currently being dragged (for foods)
				(assign, "$g_lco_drag_quantity_max", 0),  # Max quantity of item currently being dragged (for foods)
				(overlay_set_display, "$g_lco_dragging_panel", 0),
			(try_end),
		(try_end),
	]),

	("lco_drop_item", [
		(store_script_param_1, ":troop_id"),
		(store_script_param_2, ":slot_id"),
		(try_begin),
			# If user is dropping item to garbage, then we override normal procedure and just drop the item, even if player is clicking on a filled panel
			(eq, ":troop_id", "$g_lco_garbage_troop"),
			(call_script, "script_lco_discard_item", "$g_lco_drag_item", "$g_lco_drag_modifier", "$g_lco_drag_quantity"),
			(assign, "$g_lco_dragging_from", 0),      # Troop ID of dragged item current owner
			(assign, "$g_lco_dragging_from_slot", 0), # Slot ID of dragged item current owner
			(assign, "$g_lco_drag_item", -1),         # Item type currently being dragged
			(assign, "$g_lco_drag_modifier", 0),      # Modifier of item currently being dragged
			(assign, "$g_lco_drag_quantity", 0),      # Quantity of item currently being dragged (for foods)
			(assign, "$g_lco_drag_quantity_max", 0),  # Max quantity of item currently being dragged (for foods)
			(assign, "$g_lco_dragging", 0),
			(overlay_set_display, "$g_lco_dragging_panel", 0),
		(else_try),
			(call_script, "script_cf_lco_controllable", ":troop_id"),
			(troop_get_inventory_slot, ":ex_item_id", ":troop_id", ":slot_id"),
			(troop_get_inventory_slot_modifier, ":ex_modifier", ":troop_id", ":slot_id"),
			(troop_inventory_slot_get_item_amount, ":ex_quantity", ":troop_id", ":slot_id"),
			(troop_inventory_slot_get_item_max_amount, ":ex_quantity_max", ":troop_id", ":slot_id"),
			(troop_set_inventory_slot, ":troop_id", ":slot_id", "$g_lco_drag_item"),
			(troop_set_inventory_slot_modifier, ":troop_id", ":slot_id", "$g_lco_drag_modifier"),
			(try_begin),
				(gt, "$g_lco_drag_quantity", 0),
				(troop_inventory_slot_set_item_amount, ":troop_id", ":slot_id", "$g_lco_drag_quantity"),
			(try_end),
			(try_begin),
				(ge, ":ex_item_id", 0),
				(assign, "$g_lco_drag_item", ":ex_item_id"),
				(assign, "$g_lco_drag_modifier", ":ex_modifier"),
				(assign, "$g_lco_drag_quantity", ":ex_quantity"),
				(assign, "$g_lco_drag_quantity_max", ":ex_quantity_max"),
				(assign, "$g_lco_dragging_from", ":troop_id"),
				(assign, "$g_lco_dragging_from_slot", ":slot_id"),
				# Displaying overlay
				(call_script, "script_lco_item_name_to_s41", "$g_lco_drag_item", "$g_lco_drag_modifier", "$g_lco_drag_quantity", "$g_lco_drag_quantity_max"),
				(overlay_set_text, "$g_lco_dragging_text", s41),
				(overlay_set_display, "$g_lco_dragging_panel", 1), # Not necessary but just in case
				(assign, "$g_lco_dragging", 1), # Not necessary but just in case
			(else_try),
				(assign, "$g_lco_dragging_from", 0),      # Troop ID of dragged item current owner
				(assign, "$g_lco_dragging_from_slot", 0), # Slot ID of dragged item current owner
				(assign, "$g_lco_drag_item", -1),         # Item type currently being dragged
				(assign, "$g_lco_drag_modifier", 0),      # Modifier of item currently being dragged
				(assign, "$g_lco_drag_quantity", 0),      # Quantity of item currently being dragged (for foods)
				(assign, "$g_lco_drag_quantity_max", 0),  # Max quantity of item currently being dragged (for foods)
				(assign, "$g_lco_dragging", 0),
				(overlay_set_display, "$g_lco_dragging_panel", 0),
			(try_end),
		(else_try),
			(display_message, "str_lco_drop_error_control", 0xFF4040),
		(try_end),

	]),

	# OUTPUT: reg0 = error string if cannot drop
	("cf_lco_can_drop_item", [
		(store_script_param, ":troop_id", 1),
		(store_script_param, ":slot_id", 2),
		(store_script_param, ":item_id", 3),
		(store_script_param, ":modifier", 4),

		(assign, reg0, "str_lco_drop_error_control"),
		(call_script, "script_cf_lco_controllable", ":troop_id"),

		(assign, ":can_drop", 0),
		(assign, ":result", "str_lco_drop_error_type"),
		(try_begin),
			(ge, ":slot_id", num_equipment_kinds),
			(try_begin),
				(this_or_next|eq, ":troop_id", "trp_player"),
				(eq, ":troop_id", "$g_lco_garbage_troop"),
				(assign, ":can_drop", 1), # We can drop anything into player's inventory slots or to the garbage
			(else_try),
				(item_get_type, ":type", ":item_id"),
				(eq, ":type", itp_type_book), # We can only drop books into other companions inventory slots
				# Update V1.1. Disable book slots configuration variable
				(eq, "$g_lco_suppress_books", 0),
				(assign, ":can_drop", 1),
			(try_end),
		(else_try),
			(item_get_type, ":type", ":item_id"),
			(try_begin),
				(lt, ":slot_id", 4), # Weapon slot
				(this_or_next|eq, ":type", itp_type_one_handed_wpn),
				(this_or_next|eq, ":type", itp_type_two_handed_wpn),
				(this_or_next|eq, ":type", itp_type_polearm),
				(this_or_next|eq, ":type", itp_type_arrows),
				(this_or_next|eq, ":type", itp_type_bolts),
				(this_or_next|eq, ":type", itp_type_shield),
				(this_or_next|eq, ":type", itp_type_bow),
				(this_or_next|eq, ":type", itp_type_crossbow),
				(this_or_next|eq, ":type", itp_type_thrown),
				(this_or_next|eq, ":type", itp_type_pistol),
				(this_or_next|eq, ":type", itp_type_musket),
				(eq, ":type", itp_type_bullets),
				(assign, ":can_drop", 1),
			(else_try),
				(eq, ":slot_id", 4), # Head armor
				(eq, ":type", itp_type_head_armor),
				(assign, ":can_drop", 1),
			(else_try),
				(eq, ":slot_id", 5), # Body armor
				(eq, ":type", itp_type_body_armor),
				(assign, ":can_drop", 1),
			(else_try),
				(eq, ":slot_id", 6), # Leg armor
				(eq, ":type", itp_type_foot_armor),
				(assign, ":can_drop", 1),
			(else_try),
				(eq, ":slot_id", 7), # Hand armor
				(eq, ":type", itp_type_hand_armor),
				(assign, ":can_drop", 1),
			(else_try),
				(eq, ":slot_id", 8), # Horse
				(eq, ":type", itp_type_horse),
				(assign, ":can_drop", 1),
			(try_end),
			(try_begin),
				(eq, ":can_drop", 1), # Item and slot match by type, but can the character actually equip this item?
				(neq, ":type", itp_type_arrows),  # Do not check for ammo
				(neq, ":type", itp_type_bolts),   # Do not check for ammo
				(neq, ":type", itp_type_bullets), # Do not check for ammo
				(assign, ":result", "str_lco_drop_error_reqs"),
				(call_script, "script_lco_replicate_attributes", ":troop_id"),
				(call_script, "script_lco_clear_all_items", lco_storage),
				(troop_set_auto_equip, lco_storage, 0),
				(troop_set_inventory_slot, lco_storage, num_equipment_kinds, ":item_id"),
				(troop_set_inventory_slot_modifier, lco_storage, num_equipment_kinds, ":modifier"),
				# BugFix V1.1. Shields require some additional care
				(try_begin),
					(eq, ":type", itp_type_shield),
					(troop_add_item, lco_storage, "itm_tutorial_club", imod.plain), # So the testing troop has both weapon and shield and auto-equip will work properly.
				(try_end),
				(troop_equip_items, lco_storage),
				(troop_get_inventory_slot, ":copy_item_id", lco_storage, num_equipment_kinds),
				(call_script, "script_lco_clear_all_items", lco_storage),
				(ge, ":copy_item_id", 0), # He did not equip it!
				(assign, ":can_drop", 0), # Hence original troop cannot equip it either!
			(try_end),
		(try_end),
		(assign, reg0, ":result"),
		(eq, ":can_drop", 1),
	]),

	("lco_set_active_hero", [
		(store_script_param_1, ":index"),
		(assign, "$g_lco_active_hero", ":index"),
		(position_set_x, pos60, 25),
		(store_mul, ":base_y", "$g_lco_heroes", 25),
		(val_sub, ":base_y", 25),
		(val_max, ":base_y", 500),
		(store_mul, ":y", "$g_lco_active_hero", 25),
		(store_sub, ":y", ":base_y", ":y"),
		(position_set_y, pos60, ":y"),
		(overlay_set_position, "$g_lco_active_panel", pos60),
		(call_script, "script_lco_fill_hero_panels"),
	]),

	# This script will scan hero inventory and will return his "book" slots.
	# Slot numbers of first two books found in character inventory are used as the book slots.
	# If less than two books are found, remaining ones are picked from free slots in character inventory.
	("lco_allocate_slots_for_books", [
		(store_script_param_1, ":troop_id"),
		(troop_sort_inventory, ":troop_id"),
		(troop_get_inventory_capacity, ":capacity", ":troop_id"),
		(assign, reg0, -1),
		(assign, reg1, -1),
		(try_for_range, ":slot_id", num_equipment_kinds, ":capacity"),
			(troop_get_inventory_slot, ":item_id", ":troop_id", ":slot_id"),
			(try_begin),
				(ge, ":item_id", 0),
				(item_get_type, ":type", ":item_id"),
				(eq, ":type", itp_type_book),
				(try_begin),
					(eq, reg0, -1),
					(assign, reg0, ":slot_id"),
				(else_try),
					(eq, reg1, -1),
					(assign, reg1, ":slot_id"),
				(try_end),
			(try_end),
		(try_end),
		(try_for_range, ":slot_id", num_equipment_kinds, ":capacity"),
			(troop_get_inventory_slot, ":item_id", ":troop_id", ":slot_id"),
			(try_begin),
				(lt, ":item_id", 0),
				(try_begin),
					(eq, reg0, -1),
					(assign, reg0, ":slot_id"),
				(else_try),
					(eq, reg1, -1),
					(assign, reg1, ":slot_id"),
				(try_end),
			(try_end),
		(try_end),
	]),

	("cf_lco_auto_offer_item", [
		(store_script_param, ":troop_id", 1),
		(store_script_param, ":item_id", 2),
		(store_script_param, ":modifier", 3),
		(store_script_param, ":quantity", 4),
		(item_get_type, ":type", ":item_id"),
		(assign, ":out_item_id", -1),
		(assign, ":out_modifier", 0),
		(assign, ":out_quantity", 0),
		(assign, ":out_quantity_max", 0),
		(assign, ":is_equipped", 0),

		(call_script, "script_cf_lco_controllable", ":troop_id"), # Automatic failure

		# First option: if item is a weapon, troop has a free slot and can equip the item, we equip it by default
		(try_begin),
			(this_or_next|is_between, ":type", itp_type_one_handed_wpn, itp_type_goods),
			(is_between, ":type", itp_type_pistol, itp_type_animal),
			(try_for_range, ":slot_id", 0, 4),
				(eq, ":is_equipped", 0),
				(troop_get_inventory_slot, ":eq_item_id", ":troop_id", ":slot_id"),
				(lt, ":eq_item_id", 0),
				(call_script, "script_cf_lco_can_drop_item", ":troop_id", ":slot_id", ":item_id", ":modifier"),
				(troop_set_inventory_slot, ":troop_id", ":slot_id", ":item_id"),
				(troop_set_inventory_slot_modifier, ":troop_id", ":slot_id", ":modifier"),
				(try_begin),
					(gt, ":quantity", 0),
					(troop_inventory_slot_set_item_amount, ":troop_id", ":slot_id", ":quantity"),
				(try_end),
				(assign, ":is_equipped", 1),
			(try_end),
		(try_end),

		# Second option: if item is a book, we automatically give it to troop, sort the inventory and look for books.
		# If we find more than two, we'll return the third.
		# TODO: When companion book reading is implemented, need to make proper checks here.
		# Companion should not automatically give away a book he's currently reading.
		(try_begin),
			(eq, ":is_equipped", 0),
			(eq, ":type", itp_type_book),
			# Update V1.1. Disable book slots configuration variable
			(eq, "$g_lco_suppress_books", 0),
			(troop_add_item, ":troop_id", ":item_id", ":modifier"),
			(assign, ":is_equipped", 1),
			(troop_sort_inventory, ":troop_id"),
			(troop_get_inventory_capacity, ":capacity", ":troop_id"),
			(assign, ":books_found", 0),
			(try_for_range, ":slot_id", num_equipment_kinds, ":capacity"),
				(troop_get_inventory_slot, ":cur_item_id", ":troop_id", ":slot_id"),
				(ge, ":cur_item_id", 0),
				(item_get_type, ":cur_type", ":cur_item_id"),
				(eq, ":cur_type", itp_type_book),
				(try_begin),
					(lt, ":books_found", 2),
					(val_add, ":books_found", 1),
				(else_try),
					(assign, ":out_item_id", ":cur_item_id"),
					(troop_set_inventory_slot, ":troop_id", ":slot_id", -1), # Delete book from inventory
					(assign, ":capacity", 0), # Break cycle
				(try_end),
			(try_end),
		(try_end),

		# Third option: we create a duplicate, give him an item and check if he will equip it.
		# If he will not equip it, it's a failure
		# If he will equip it, there may be zero, one or more items lying in inventory.
		# If it's zero, fine.
		# If it's one, also fine, we return it as a compensation item
		# If it's more than one, then we sort inventory and add ammo/shield items to free slots while there are free slots
		# Then we sort again and retrieve the first item in inventory as compensation
		(try_begin),
			(eq, ":is_equipped", 0),
			(neq, ":type", itp_type_goods),
			(neq, ":type", itp_type_animal),
			(neq, ":type", itp_type_book),
			(call_script, "script_lco_clear_all_items", lco_storage),
			(call_script, "script_lco_replicate_attributes", ":troop_id"),
			(call_script, "script_lco_replicate_equipment", ":troop_id"),
			(troop_add_item, lco_storage, ":item_id", ":modifier"),
			(troop_equip_items, lco_storage),
			(troop_sort_inventory, lco_storage),
			# Checking if our item is lying in inventory
			(assign, ":is_equipped", 1),
			(troop_get_inventory_capacity, ":capacity", ":troop_id"),
			(try_for_range, ":slot_id", num_equipment_kinds, ":capacity"),
				(troop_get_inventory_slot, ":inv_item_id", lco_storage, ":slot_id"),
				(troop_get_inventory_slot_modifier, ":inv_modifier", lco_storage, ":slot_id"),
				(eq, ":item_id", ":inv_item_id"),
				(eq, ":modifier", ":inv_modifier"),
				(assign, ":is_equipped", 0), # Troop refused to equip our item, so no sense checking further
				(assign, ":capacity", 0), # Break cycle
			(try_end),
			# Since it's not, we are now looking for a slot to put the item in.
			(try_begin),
				(eq, ":is_equipped", 1),
				(assign, ":swap_slot", -1),
				(try_begin),
					(eq, ":type", itp_type_horse),
					(assign, ":swap_slot", 8),
				(else_try),
					(is_between, ":type", itp_type_head_armor, itp_type_pistol),
					(store_sub, ":swap_slot", ":type", 8),
				(else_try),
					# Our item is a weapon or ammo.
					# This means we have at least one item in inventory (if there was an empty weapon slot it would be filled on first option).
					# Now we look for the first item that is not ammo. If we find it, this is the swapped item.
					(assign, ":swap_item_id", -1),
					(assign, ":swap_item_mod", 0),
					(try_for_range, ":slot_id", num_equipment_kinds, num_equipment_kinds+5), # Because there cannot be more items by code design
						(eq, ":swap_item_id", -1), # Not yet found
						(troop_get_inventory_slot, ":cur_item_id", lco_storage, ":slot_id"),
						(ge, ":cur_item_id", 0), # Slot is not empty
						(item_get_type, ":cur_type", ":cur_item_id"),
						(this_or_next|is_between, ":cur_type", itp_type_one_handed_wpn, itp_type_arrows),
						(this_or_next|is_between, ":cur_type", itp_type_bow, itp_type_goods),
						(is_between, ":cur_type", itp_type_pistol, itp_type_bullets),
						(assign, ":swap_item_id", ":cur_item_id"),
						(troop_get_inventory_slot_modifier, ":swap_item_mod", lco_storage, ":slot_id"),
					(try_end),
					# If we didn't find a weapon, then we look for ammo and choose the last in the list (least expensive)
					(try_for_range_backwards, ":slot_id", num_equipment_kinds, num_equipment_kinds+5), # Because there cannot be more items by code design
						(eq, ":swap_item_id", -1), # Not yet found
						(troop_get_inventory_slot, ":cur_item_id", lco_storage, ":slot_id"),
						(ge, ":cur_item_id", 0), # Slot is not empty
						(item_get_type, ":cur_type", ":cur_item_id"),
						(this_or_next|eq, ":cur_type", itp_type_bullets),
						(is_between, ":cur_type", itp_type_arrows, itp_type_shield),
						(assign, ":swap_item_id", ":cur_item_id"),
						(troop_get_inventory_slot_modifier, ":swap_item_mod", lco_storage, ":slot_id"),
					(try_end),
					# If we didn't find anything, that's an error and we report it. Otherwise, we are looking for swap_item slot in the original troop equipment
					(try_begin),
						(eq, ":swap_item_id", -1),
						(display_message, "str_lco_impossible_error"),
					(else_try),
						(try_for_range, ":slot_id", 0, num_equipment_kinds),
							(troop_get_inventory_slot, ":cur_item_id", ":troop_id", ":slot_id"),
							(troop_get_inventory_slot_modifier, ":cur_item_mod", ":troop_id", ":slot_id"),
							(eq, ":cur_item_id", ":swap_item_id"),
							(eq, ":cur_item_mod", ":swap_item_mod"),
							(assign, ":swap_slot", ":slot_id"),
						(try_end),
					(try_end),
				(try_end),

				# Now we have ":swap_slot" keeping the slot id in the original troop equipment that we are putting offered item to.
				(try_begin),
					(eq, ":swap_slot", -1),
					(assign, ":is_equipped", 0),
				(else_try),
					(troop_get_inventory_slot, ":out_item_id", ":troop_id", ":swap_slot"),
					(troop_get_inventory_slot_modifier, ":out_modifier", ":troop_id", ":swap_slot"),
					(troop_inventory_slot_get_item_amount, ":out_quantity", ":troop_id", ":swap_slot"),
					(troop_inventory_slot_get_item_max_amount, ":out_quantity", ":troop_id", ":swap_slot"),
					(troop_set_inventory_slot, ":troop_id", ":swap_slot", ":item_id"),
					(troop_set_inventory_slot_modifier, ":troop_id", ":swap_slot", ":modifier"),
					(assign, ":is_equipped", 1),
				(try_end),
			(try_end),
		(try_end),

		(eq, ":is_equipped", 1),
		(assign, reg0, ":out_item_id"),
		(assign, reg1, ":out_modifier"),
		(assign, reg2, ":out_quantity"),
		(assign, reg3, ":out_quantity_max"),
	]),

	("lco_backup_inventory", [
		(store_script_param_1, ":troop_id"),
		(call_script, "script_lco_clear_all_items", lco_storage),
		(troop_set_auto_equip, lco_storage, 0),
		(troop_get_inventory_capacity, ":capacity", ":troop_id"),
		(assign, ":target_id", num_equipment_kinds),
		(try_for_range, ":source_id", num_equipment_kinds, ":capacity"),
			(troop_get_inventory_slot, ":item_id", ":troop_id", ":source_id"),
			(ge, ":item_id", 0),
			(troop_get_inventory_slot_modifier, ":modifier", ":troop_id", ":source_id"),
			(troop_inventory_slot_get_item_amount, ":qty", ":troop_id", ":source_id"),
			(troop_set_inventory_slot, lco_storage, ":target_id", ":item_id"),
			(troop_set_inventory_slot_modifier, lco_storage, ":target_id", ":modifier"),
			(try_begin),
				(gt, ":qty", 0),
				(troop_inventory_slot_set_item_amount, lco_storage, ":target_id", ":qty"),
			(try_end),
			(troop_set_inventory_slot, ":troop_id", ":source_id", -1),
			(val_add, ":target_id", 1),
		(try_end),
	]),

	("lco_retrieve_inventory", [
		(store_script_param_1, ":troop_id"),
		(troop_sort_inventory, lco_storage),
		(troop_get_inventory_capacity, ":capacity", ":troop_id"),
		(assign, ":source_id", num_equipment_kinds),
		(try_for_range, ":target_id", num_equipment_kinds, ":capacity"),
			(troop_get_inventory_slot, ":cur_item_id", ":troop_id", ":target_id"),
			(lt, ":cur_item_id", 0), # Current slot empty?
			(troop_get_inventory_slot, ":item_id", lco_storage, ":source_id"),
			(ge, ":item_id", 0), # There is still an item in the storage?
			(troop_get_inventory_slot_modifier, ":modifier", lco_storage, ":source_id"),
			(troop_inventory_slot_get_item_amount, ":qty", lco_storage, ":source_id"),
			(troop_set_inventory_slot, ":troop_id", ":target_id", ":item_id"),
			(troop_set_inventory_slot_modifier, ":troop_id", ":target_id", ":modifier"),
			(try_begin),
				(gt, ":qty", 0),
				(troop_inventory_slot_set_item_amount, ":troop_id", ":target_id", ":qty"),
			(try_end),
			(val_add, ":source_id", 1),
		(try_end),
		(call_script, "script_lco_clear_all_items", lco_storage),
	]),

	("lco_clear_all_items", [
		(store_script_param_1, ":troop_id"),
		(troop_clear_inventory, ":troop_id"),
		(try_for_range, ":index", 0, 9),
			(troop_set_inventory_slot, ":troop_id", ":index", -1), # Cleaning equipment
		(try_end),
	]),

	("lco_replicate_attributes", [
		# BugFix V1.1. Added shield skill to the list of monitored skills and attributes.
		(store_script_param_1, ":troop_id"),
		(store_attribute_level, ":str", ":troop_id", ca_strength),
		(store_skill_level, ":pdraw", "skl_power_draw", ":troop_id"),
		(store_skill_level, ":pthrow", "skl_power_throw", ":troop_id"),
		(store_skill_level, ":riding", "skl_riding", ":troop_id"),
		(store_skill_level, ":shield", "skl_shield", ":troop_id"),
		(store_attribute_level, ":ex_str", lco_storage, ca_strength),
		(store_skill_level, ":ex_pdraw", "skl_power_draw", lco_storage),
		(store_skill_level, ":ex_pthrow", "skl_power_throw", lco_storage),
		(store_skill_level, ":ex_riding", "skl_riding", lco_storage),
		(store_skill_level, ":ex_shield", "skl_shield", lco_storage),
		(val_sub, ":str", ":ex_str"),
		(val_sub, ":pdraw", ":ex_pdraw"),
		(val_sub, ":pthrow", ":ex_pthrow"),
		(val_sub, ":riding", ":ex_riding"),
		(val_sub, ":shield", ":ex_shield"),
		(troop_raise_attribute, lco_storage, ca_strength, ":str"),
		(troop_raise_skill, lco_storage, "skl_power_draw", ":pdraw"),
		(troop_raise_skill, lco_storage, "skl_power_throw", ":pthrow"),
		(troop_raise_skill, lco_storage, "skl_riding", ":riding"),
		(troop_raise_skill, lco_storage, "skl_shield", ":shield"),
	]),

	("lco_replicate_equipment", [
		(store_script_param_1, ":troop_id"),
		(try_for_range, ":index", 0, num_equipment_kinds),
			(troop_get_inventory_slot, ":item_id", ":troop_id", ":index"),
			(troop_get_inventory_slot_modifier, ":modifier", ":troop_id", ":index"),
			(troop_set_inventory_slot, lco_storage, ":index", ":item_id"),
			(troop_set_inventory_slot_modifier, lco_storage, ":index", ":modifier"),
		(try_end),
	]),

	("lco_hero_grab_equipment", [
		(store_script_param, ":troop_id", 1),
		(assign, ":hero_offset", num_equipment_kinds),
		(troop_get_inventory_capacity, ":capacity", "trp_player"),
		(troop_get_inventory_capacity, ":hero_capacity", ":troop_id"),
		(try_for_range, ":slot_id", num_equipment_kinds, ":capacity"),
			(try_begin),
				(call_script, "script_cf_lco_slot_is_frozen", ":slot_id"), # If current slot is frozen, we skip it in either case
			(else_try),
				(troop_get_inventory_slot, ":item_id", "trp_player", ":slot_id"),
				(ge, ":item_id", 0),
				(assign, ":grab", 0),
				(item_get_type, ":type", ":item_id"),
				# Will companion grab this item?
				(try_begin),
					(eq, "$g_lco_auto_horses", 1),
					(eq, ":type", itp_type_horse),
					(assign, ":grab", 1),
				(else_try),
					(eq, "$g_lco_auto_armors", 1),
					(this_or_next|eq, ":type", itp_type_head_armor),
					(this_or_next|eq, ":type", itp_type_body_armor),
					(this_or_next|eq, ":type", itp_type_foot_armor),
					(eq, ":type", itp_type_hand_armor),
					(assign, ":grab", 1),
				(else_try),
					(eq, "$g_lco_auto_shields", 1),
					(eq, ":type", itp_type_shield),
					(assign, ":grab", 1),
				(try_end),
				(this_or_next|eq, ":troop_id", lco_storage), # When this operation is used on lco_storage, this means we are sorting player's inventory, so just take everything
				(eq, ":grab", 1),
				(troop_get_inventory_slot_modifier, ":modifier", "trp_player", ":slot_id"),
				(troop_inventory_slot_get_item_amount, ":amount", "trp_player", ":slot_id"),
				(troop_set_inventory_slot, ":troop_id", ":hero_offset", ":item_id"),
				(troop_set_inventory_slot_modifier, ":troop_id", ":hero_offset", ":modifier"),
				(try_begin),
					(gt, ":amount", 0),
					(troop_inventory_slot_set_item_amount, ":troop_id", ":hero_offset", ":amount"),
				(try_end),
				(troop_set_inventory_slot, "trp_player", ":slot_id", -1), # Remove item
				(val_add, ":hero_offset", 1),
				(ge, ":hero_offset", ":hero_capacity"),
				(assign, ":capacity", 0), # Break cycle because companion has no space in inventory for more items
			(try_end),
		(try_end),
	]),

	("lco_hero_return_equipment", [
		(store_script_param, ":troop_id", 1),
		(troop_sort_inventory, ":troop_id"),
		(troop_get_inventory_capacity, ":hero_capacity", ":troop_id"),
		# Companion is returning items to player
		(troop_get_inventory_capacity, ":capacity", "trp_player"),
		(assign, ":hero_offset", num_equipment_kinds),
		(try_for_range, ":slot_id", num_equipment_kinds, ":capacity"),
			(try_begin),
				(call_script, "script_cf_lco_slot_is_frozen", ":slot_id"), # If current slot is frozen, we skip it
			(else_try),
				(troop_get_inventory_slot, ":item_id", "trp_player", ":slot_id"),
				(lt, ":item_id", 0), # Slot is empty, can get item back
				(troop_get_inventory_slot, ":item_id", ":troop_id", ":hero_offset"),
				(troop_get_inventory_slot_modifier, ":modifier", ":troop_id", ":hero_offset"),
				(troop_inventory_slot_get_item_amount, ":amount", ":troop_id", ":hero_offset"),
				(troop_set_inventory_slot, "trp_player", ":slot_id", ":item_id"),
				(troop_set_inventory_slot_modifier, "trp_player", ":slot_id", ":modifier"),
				(try_begin),
					(gt, ":amount", 0),
					(troop_inventory_slot_set_item_amount, "trp_player", ":slot_id", ":amount"),
				(try_end),
				(troop_set_inventory_slot, ":troop_id", ":hero_offset", -1), # Remove item
				(val_add, ":hero_offset", 1),
				(ge, ":hero_offset", ":hero_capacity"),
				(assign, ":capacity", 0), # Break cycle because we reached the end of companion's inventory
			(try_end),
		(try_end),
		# If player's inventory is full and companion still has items in inventory, he will drop them to garbage
		(troop_get_inventory_capacity, ":capacity", "$g_lco_garbage_troop"),
		(assign, ":hero_offset", num_equipment_kinds),
		(try_for_range, ":slot_id", num_equipment_kinds, ":capacity"),
			(troop_get_inventory_slot, ":item_id", "$g_lco_garbage_troop", ":slot_id"),
			(lt, ":item_id", 0), # Slot is empty, can get item back
			(troop_get_inventory_slot, ":item_id", ":troop_id", ":hero_offset"),
			(troop_get_inventory_slot_modifier, ":modifier", ":troop_id", ":hero_offset"),
			(troop_inventory_slot_get_item_amount, ":amount", ":troop_id", ":hero_offset"),
			(troop_set_inventory_slot, "$g_lco_garbage_troop", ":slot_id", ":item_id"),
			(troop_set_inventory_slot_modifier, "$g_lco_garbage_troop", ":slot_id", ":modifier"),
			(try_begin),
				(gt, ":amount", 0),
				(troop_inventory_slot_set_item_amount, "$g_lco_garbage_troop", ":slot_id", ":amount"),
			(try_end),
			(troop_set_inventory_slot, ":troop_id", ":hero_offset", -1), # Remove item
			(val_add, ":hero_offset", 1),
			(ge, ":hero_offset", ":hero_capacity"),
			(assign, ":capacity", 0), # Break cycle because we reached the end of companion's inventory
		(try_end),
		(troop_sort_inventory, "$g_lco_garbage_troop"),
	]),

	("lco_initialize_presentation", [

		(presentation_set_duration, 999999),
		(set_fixed_point_multiplier, 1000),
		(try_begin),
			(eq, "$g_lco_initialized", 0),
			(assign, "$g_lco_activate_troop", 0), # By default, we do not make a particular troop active
			(assign, "$g_lco_active_hero", 0),    # We show the first hero by default
			(assign, "$g_lco_page", 0),           # We show the first page by default
			#(assign, "$g_lco_operation", 0),      # No special action by default
			#(assign, "$g_lco_target", 0),         # No action target by default
			(assign, "$g_lco_auto_horses", 1),    # Horses are auto-equipped by default
			(assign, "$g_lco_auto_armors", 1),    # Same
			(assign, "$g_lco_auto_shields", 1),   # Same
			(assign, "$g_lco_include_companions", 1),
			(assign, "$g_lco_include_lords", 0),
			(assign, "$g_lco_include_regulars", 0),
			# BugFix V1.1. Do not overwrite $g_lco_garbage_troop on first run if it's already initialized.
			(try_begin),
				(lt, "$g_lco_garbage_troop", 3),
				(assign, "$g_lco_garbage_troop", lco_garbage), # This troop will be used for discarding items or looting, and it's inventory will be purged on exit
			(try_end),
			(assign, "$g_lco_initialized", 1),
			# BugFix V1.2. Hardcoded xp-to-level conversion table has been removed
		(try_end),

		# GLOBAL VARIABLES INITIALIZATION

		(assign, "$g_lco_heroes", 0),             # Total number of heroes in the party, excluding player
		(assign, "$g_lco_inv_slots", 0),          # Total number of slots in the player's inventory
		(assign, "$g_lco_dragging", 0),           # Currently not dragging anything
		(assign, "$g_lco_dragging_from", 0),      # Troop ID of dragged item current owner
		(assign, "$g_lco_dragging_from_slot", 0), # Slot ID of dragged item current owner
		(assign, "$g_lco_drag_item", -1),         # Item type currently being dragged
		(assign, "$g_lco_drag_modifier", 0),      # Modifier of item currently being dragged
		(assign, "$g_lco_drag_quantity", 0),      # Quantity of item currently being dragged (for foods)
		(assign, "$g_lco_drag_quantity_max", 0),  # Max quantity of item currently being dragged (for foods)
		(assign, "$g_lco_popup_active", 0),       # Whether or not there's an active popup with item details
		(assign, "$g_lco_popup_overlay", 0),      # Overlay ID that caused the popup to appear (to prevent popup from disappearing when mouseout happens on another overlay)
		(assign, "$g_lco_popup_item", 0),         # ID of the item to show in popup
		(assign, "$g_lco_popup_modifier", 0),     # ID of the modifier to show in popup
		(assign, "$g_lco_panel_found", 0),        # Variable is used to prevent a single click from affecting two panels simultaneously in equipment_overview

		(val_clamp, "$g_lco_auto_horses", 0, 2),
		(val_clamp, "$g_lco_auto_armors", 0, 2),
		(val_clamp, "$g_lco_auto_shields", 0, 2),
		(val_clamp, "$g_lco_include_companions", 0, 2),
		(val_clamp, "$g_lco_include_lords", 0, 2),
		(val_clamp, "$g_lco_include_regulars", 0, 2),
		(try_begin),
			(is_presentation_active, "prsnt_companions_overview"),
			(val_clamp, "$g_lco_page", 0, 2),   # Current page to display
		(try_end),

		(assign, "$extra_text_preq_display", 1), # Tell NE's script_game_get_item_extra_text to force output of item's prerequisite
		# TROOP HANDLING

		(call_script, "script_lco_prepare_heroes"),
		(try_begin),
			# We are requested to make a particular troop active
			(gt, "$g_lco_activate_troop", 0),
			(try_for_range, reg0, 0, "$g_lco_heroes"),
				(store_add, ":offset", reg0, "$g_lco_heroes"),
				(troop_slot_eq, lco_storage, ":offset", "$g_lco_activate_troop"),
				(assign, "$g_lco_active_hero", ":offset"),
			(try_end),
			(assign, "$g_lco_activate_troop", 0),
		(try_end),
		(val_clamp, "$g_lco_active_hero", 0, "$g_lco_heroes"), # Index of currently selected hero
		(troop_get_inventory_capacity, "$g_lco_inv_slots", "trp_player"),
		(val_sub, "$g_lco_inv_slots", num_equipment_kinds),
		(troop_get_inventory_capacity, "$g_lco_garb_slots", "$g_lco_garbage_troop"),
		(val_sub, "$g_lco_garb_slots", num_equipment_kinds),
		(troop_set_auto_equip, lco_storage, 0),
		(call_script, "script_lco_clear_all_items", lco_storage),
		(troop_set_auto_equip, "$g_lco_garbage_troop", 0),
		# We do not clear garbage troop because it may be used for looting

		# PRESENTATION SHARED BUTTONS AND INCLUSION FORM

		(ui_create_game_button, "$g_lco_return", "str_lco_i_return", 855, 25, 190, 42),
		(ui_create_checkbox, "$g_lco_inc_0", mesh.checkbox_off, mesh.checkbox_on, 25, 75, "$g_lco_include_companions"),
		(ui_create_label, reg0, "str_lco_i_list_companions", 50, 75, 0, 750),
		(ui_create_checkbox, "$g_lco_inc_1", mesh.checkbox_off, mesh.checkbox_on, 25, 50, "$g_lco_include_lords"),
		(ui_create_label, reg0, "str_lco_i_list_lords", 50, 50, 0, 750),
		(ui_create_checkbox, "$g_lco_inc_2", mesh.checkbox_off, mesh.checkbox_on, 25, 25, "$g_lco_include_regulars"),
		(ui_create_label, reg0, "str_lco_i_list_regulars", 50, 25, 0, 750),

		(ui_create_image_button, "$g_lco_switch_page_0", mesh.ui_btn_1_u, mesh.ui_btn_1_d, 25, 685, 333, 400),
		(ui_create_image_button, "$g_lco_switch_page_1", mesh.ui_btn_1_u, mesh.ui_btn_1_d, 55, 685, 333, 400),
		(ui_create_image_button, "$g_lco_switch_page_2", mesh.ui_btn_1_u, mesh.ui_btn_1_d, 85, 685, 333, 400),
		(try_begin),
			(is_presentation_active, "prsnt_equipment_overview"),
			(assign, ":x", 85),
		(else_try),
			(store_mul, ":x", "$g_lco_page", 30),
			(val_add, ":x", 25),
		(try_end),

		(ui_create_mesh, "$g_lco_selected_page", mesh.ui_btn_1_d, ":x", 685, 333, 400),

		(ui_create_label, reg0, "@1", 35, 702, tf_center_justify|tf_vertical_align_center, 750),
		(ui_create_label, reg0, "@2", 65, 702, tf_center_justify|tf_vertical_align_center, 750),
		(ui_create_label, reg0, "str_lco_i_ie_icon", 95, 702, tf_center_justify|tf_vertical_align_center, 750),

		# DISPLAYING VERSION INFORMATION

		(ui_create_label, reg0, "str_lco_version", 975, 5, tf_right_align, 750),

	]),

	("lco_prepare_heroes", [
		(assign, "$g_lco_heroes", 0), # Total number of heroes in the party, excluding player
		# CALCULATING NUMBER OF HEROES
		(try_begin),
			(eq, "$g_lco_include_companions", 1),
			(party_get_num_companion_stacks, ":total_stacks", "p_main_party"),
			(try_for_range, reg0, 0, ":total_stacks"),
				(party_stack_get_troop_id, ":troop_id", "p_main_party", reg0),
				(is_between, ":troop_id", companions_begin, companions_end),
				(troop_set_slot, lco_storage, "$g_lco_heroes", ":troop_id"),
				(val_add, "$g_lco_heroes", 1),
			(try_end),
		(try_end),
		(try_begin),
			(eq, "$g_lco_include_lords", 1),
			(gt, "$players_kingdom", 0),
			(faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
			(try_for_range, ":troop_id", active_npcs_begin, active_npcs_end),
				(troop_slot_eq, ":troop_id", slot_troop_occupation, slto_kingdom_hero),
				(troop_get_slot, ":party_no", ":troop_id", slot_troop_leaded_party),
				(gt, ":party_no", 0),
				(party_is_active, ":party_no"),
				(troop_set_slot, lco_storage, "$g_lco_heroes", ":troop_id"),
				(val_add, "$g_lco_heroes", 1),
			(try_end),
		(try_end),
		(try_begin),
			(eq, "$g_lco_include_regulars", 1),
			(party_get_num_companion_stacks, ":total_stacks", "p_main_party"),
			(try_for_range, reg0, 0, ":total_stacks"),
				(party_stack_get_troop_id, ":troop_id", "p_main_party", reg0),
				(neg|troop_is_hero, ":troop_id"),
				(troop_set_slot, lco_storage, "$g_lco_heroes", ":troop_id"),
				(val_add, "$g_lco_heroes", 1),
			(try_end),
		(try_end),
	]),

	("cf_lco_controllable", [
		(store_script_param_1, ":troop_id"),
		(troop_is_hero, ":troop_id"), # We never have control over regulars
		(assign, ":control", 0),
		(try_begin),
			(this_or_next|eq, ":troop_id", "trp_player"),
			(eq, ":troop_id", "$g_lco_garbage_troop"),
			(assign, ":control", 1),
		(else_try),
			(gt, "$g_lco_heroes", 0),
			(is_between, ":troop_id", companions_begin, companions_end), # We do not provide control over lords
			(troop_slot_eq, ":troop_id", slot_troop_occupation, slto_player_companion),
			(assign, ":control", 1),
		(try_end),
		(eq, ":control", 1),
	]),

	("lco_troop_name_to_s40", [
		(store_script_param_1, ":troop_id"),
		(try_begin),
			(troop_is_hero, ":troop_id"),
			(str_store_troop_name, s40, ":troop_id"),
		(else_try),
			(str_store_troop_name_plural, s40, ":troop_id"),
		(try_end),
	]),

	("lco_discard_item", [
		(store_script_param, ":item_id", 1),
		(store_script_param, ":modifier", 2),
		(store_script_param, ":quantity", 3),
		(troop_sort_inventory, "$g_lco_garbage_troop"),
		(troop_get_inventory_capacity, ":capacity", "$g_lco_garbage_troop"),
		(store_sub, reg0, ":capacity", num_equipment_kinds),
		(assign, ":discarded", 0),
		(try_for_range, ":index", num_equipment_kinds, ":capacity"),
			(troop_get_inventory_slot, ":cur_item_id", "$g_lco_garbage_troop", ":index"),
			(lt, ":cur_item_id", 0),
			(troop_set_inventory_slot, "$g_lco_garbage_troop", ":index", ":item_id"),
			(troop_set_inventory_slot_modifier, "$g_lco_garbage_troop", ":index", ":modifier"),
			(try_begin),
				(ge, ":quantity", 1),
				(troop_inventory_slot_set_item_amount, "$g_lco_garbage_troop", ":index", ":quantity"),
			(try_end),
			(store_add, reg0, ":index", 1-num_equipment_kinds), # Total number of items in garbage
			(assign, ":capacity", 0), # Break cycle
			(assign, ":discarded", 1),
		(try_end),
		(try_begin),
			# If garbage troop inventory is full, we replace the last (cheapest) item
			(eq, ":discarded", 0),
			(assign, ":index", ":capacity"),
			(val_sub, ":index", 1),
			(troop_set_inventory_slot, "$g_lco_garbage_troop", ":index", ":item_id"),
			(troop_set_inventory_slot_modifier, "$g_lco_garbage_troop", ":index", ":modifier"),
			(try_begin),
				(ge, ":quantity", 1),
				(troop_inventory_slot_set_item_amount, "$g_lco_garbage_troop", ":index", ":quantity"),
			(try_end),
			(store_sub, reg0, ":capacity", num_equipment_kinds),
		(try_end),
		(troop_sort_inventory, "$g_lco_garbage_troop"),
	]),

	("lco_retrieve_discarded", [
		(troop_sort_inventory, "$g_lco_garbage_troop"),
		(assign, ":hero_offset", num_equipment_kinds),
		(troop_get_inventory_capacity, ":capacity", "trp_player"),
		(troop_get_inventory_capacity, ":hero_capacity", "$g_lco_garbage_troop"),
		(try_for_range, ":slot_id", num_equipment_kinds, ":capacity"),
			(try_begin),
				(call_script, "script_cf_lco_slot_is_frozen", ":slot_id"),
			(else_try),
				(troop_get_inventory_slot, ":item_id", "trp_player", ":slot_id"),
				(lt, ":item_id", 0), # Slot is empty, can get item back
				(troop_get_inventory_slot, ":item_id", "$g_lco_garbage_troop", ":hero_offset"),
				(troop_get_inventory_slot_modifier, ":modifier", "$g_lco_garbage_troop", ":hero_offset"),
				(troop_inventory_slot_get_item_amount, ":quantity", "$g_lco_garbage_troop", ":hero_offset"),
				(troop_set_inventory_slot, "trp_player", ":slot_id", ":item_id"),
				(troop_set_inventory_slot_modifier, "trp_player", ":slot_id", ":modifier"),
				(try_begin),
					(ge, ":quantity", 1),
					(troop_inventory_slot_set_item_amount, "trp_player", ":slot_id", ":quantity"),
				(try_end),
				(troop_set_inventory_slot, "$g_lco_garbage_troop", ":hero_offset", -1), # Remove item
				(val_add, ":hero_offset", 1),
				(ge, ":hero_offset", ":hero_capacity"),
				(assign, ":capacity", 0),
			(try_end),
		(try_end),
		(call_script, "script_lco_count_discarded"),
	]),

	("lco_sort_player_inventory", [
		(call_script, "script_lco_clear_all_items", lco_storage),
		(call_script, "script_lco_hero_grab_equipment", lco_storage),
		(troop_sort_inventory, lco_storage),
		(call_script, "script_lco_hero_return_equipment", lco_storage),
	]),

	# script_get_item_price
	# This script will return the price of an item in reg0
	# INPUT: <arg1> = item_type_id, <arg2> = item_modifier_id
	# OUTPUT: reg0 = nominal item price (price modifiers are ignored)
	("lco_get_item_price", [
		(store_script_param, ":item_id", 1),
		(store_script_param, ":item_modifier", 2),
		(store_script_param, ":item_amount", 3),
		(troop_clear_inventory, lco_storage),
		(troop_set_auto_equip, lco_storage, 0),
		(troop_set_inventory_slot, lco_storage, num_equipment_kinds, ":item_id"),
		(troop_set_inventory_slot_modifier, lco_storage, num_equipment_kinds, ":item_modifier"),
		(troop_inventory_slot_get_item_max_amount, ":max_amount", lco_storage, num_equipment_kinds),
		(troop_remove_items, lco_storage, ":item_id", 1),
		(try_begin),
			(ge, ":item_amount", 1),
			(val_mul, reg0, ":item_amount"),
			(val_div, reg0, ":max_amount"),
		(try_end),
	]),

	("lco_retrieve_discarded_best", [
		(call_script, "script_lco_retrieve_discarded"),
		(try_begin),
			(gt, reg0, 0), # If there are still items in loot
			# Sort player inventory
			(call_script, "script_lco_sort_player_inventory"),
			# Process
			(assign, ":hero_offset", num_equipment_kinds), # Offset of item in loot that is currently processed
			(troop_get_inventory_capacity, ":capacity", "trp_player"),
			(troop_get_inventory_capacity, ":hero_capacity", "$g_lco_garbage_troop"),
			(try_for_range_backwards, ":slot_id", num_equipment_kinds, ":capacity"),
				(try_begin),
					(call_script, "script_cf_lco_slot_is_frozen", ":slot_id"), # Skipping over frozen slots
				(else_try),
					# Retrieving item from garbage troop's inventory
					(troop_get_inventory_slot, ":loot_item_id", "$g_lco_garbage_troop", ":hero_offset"),
					(ge, ":loot_item_id", 0), # Garbage troop has an item in currently processed slot
					(troop_get_inventory_slot_modifier, ":loot_modifier", "$g_lco_garbage_troop", ":hero_offset"),
					(troop_inventory_slot_get_item_amount, ":loot_quantity", "$g_lco_garbage_troop", ":hero_offset"),
					(call_script, "script_lco_get_item_price", ":loot_item_id", ":loot_modifier", ":loot_quantity"),
					(assign, ":loot_price", reg0),
					# Retrieving item from player's inventory
					(troop_get_inventory_slot, ":item_id", "trp_player", ":slot_id"),
					(troop_get_inventory_slot_modifier, ":modifier", "trp_player", ":slot_id"),
					(troop_inventory_slot_get_item_amount, ":quantity", "trp_player", ":slot_id"),
					(call_script, "script_lco_get_item_price", ":item_id", ":modifier", ":quantity"),
					(assign, ":price", reg0),
					# If price for loot item is greater than price for player item, we swap them.
					# If it's equal or less, since both arrays are sorted, we quit the loop (subsequent loot items will be of same or lower price).
					(gt, ":loot_price", ":price"),
					# Overwriting item in player's inventory
					(troop_set_inventory_slot, "trp_player", ":slot_id", ":loot_item_id"),
					(troop_set_inventory_slot_modifier, "trp_player", ":slot_id", ":loot_modifier"),
					(try_begin),
						(ge, ":loot_quantity", 1),
						(troop_inventory_slot_set_item_amount, "trp_player", ":slot_id", ":loot_quantity"),
					(try_end),
					# Overwriting item in loot inventory
					(troop_set_inventory_slot, "$g_lco_garbage_troop", ":hero_offset", ":item_id"),
					(troop_set_inventory_slot_modifier, "$g_lco_garbage_troop", ":hero_offset", ":modifier"),
					(try_begin),
						(ge, ":quantity", 1),
						(troop_inventory_slot_set_item_amount, "$g_lco_garbage_troop", ":hero_offset", ":quantity"),
					(try_end),
					(val_add, ":hero_offset", 1), # Proceed to next loot item
					# Just in case, we are also checking for exceeding the loot troop inventory size
					(lt, ":hero_offset", ":hero_capacity"),
				(else_try),
					(assign, ":capacity", 0), # Terminate cycle if no more loot items, or current loot item is cheaper than current player's item, or loot inventory exhausted
				(try_end),
			(try_end),
		(try_end),
		(call_script, "script_lco_sort_player_inventory"),
		(call_script, "script_lco_count_discarded"),
	]),

	("lco_count_discarded", [
		(troop_get_inventory_capacity, ":hero_capacity", "$g_lco_garbage_troop"),
		(store_free_inventory_capacity, ":free_capacity", "$g_lco_garbage_troop"),
		(troop_sort_inventory, "$g_lco_garbage_troop"),
		(store_sub, reg0, ":hero_capacity", ":free_capacity"),
		(val_sub, reg0, num_equipment_kinds),
	]),

	("lco_xp_to_next_level", [
		(store_script_param_1, ":troop_id"),
		(store_character_level, ":level", ":troop_id"),
		(val_add, ":level", 1),
		(troop_get_xp, ":xp", ":troop_id"),
		(get_level_boundary, ":xp_needed", ":level"),
		(store_sub, reg40, ":xp_needed", ":xp"),
	]),

	("lco_freeze_slot_toggle", [
		(store_script_param_1, ":slot_id"),
		(try_begin),
			(troop_slot_eq, lco_garbage, ":slot_id", 1),
			(troop_set_slot, lco_garbage, ":slot_id", 0),
			(assign, reg0, 0),
		(else_try),
			(troop_set_slot, lco_garbage, ":slot_id", 1),
			(assign, reg0, 1),
		(try_end),
	]),

	("cf_lco_slot_is_frozen", [
		(store_script_param_1, ":slot_id"),
		(troop_slot_eq, lco_garbage, ":slot_id", 1),
	]),

	("lco_suppress_book_slots", [
		(store_script_param_1, "$g_lco_suppress_books"),
	]),

	# Returns item's primary stat, whatever it is. For weapons, it's max of both damage values, for armors and shields it's sum of all armor values, and for other items it's price.
	# Script is used to detect and highlight better or worse stuff than the item mouse cursor is pointing at.
	("lco_get_item_primary_stat", [
		(store_script_params, ":item_id", ":item_modifier"),
		(item_get_type, ":item_type", ":item_id"),
		(try_begin),
			(is_between, ":item_type", itp_type_one_handed_wpn, itp_type_thrown + 1),
			(neq, ":item_type", itp_type_shield),
			(item_get_swing_damage, reg0, ":item_id"),
			(item_get_thrust_damage, ":damage", ":item_id"),
			(val_max, reg0, ":damage"),
			(item_modifier_get_damage, ":damage", ":item_modifier"),
			(val_add, reg0, ":damage"),
		(else_try),
			(this_or_next|eq, ":item_type", itp_type_shield),
			(is_between, ":item_type", itp_type_head_armor, itp_type_hand_armor + 1),
			(item_get_head_armor, ":head", ":item_id"),
			(item_get_body_armor, ":body", ":item_id"),
			(item_get_leg_armor, ":leg", ":item_id"),
			(item_modifier_get_armor, ":bonus", ":item_modifier"),
			(assign, reg0, ":bonus"),
			(val_min, reg0, ":head"),
			(val_add, ":head", reg0),
			(val_max, ":head", 0),
			(assign, reg0, ":bonus"),
			(val_min, reg0, ":body"),
			(val_add, ":body", reg0),
			(val_max, ":body", 0),
			(assign, reg0, ":bonus"),
			(val_min, reg0, ":leg"),
			(val_add, reg0, ":leg"),
			(val_max, reg0, 0),
			(val_add, reg0, ":head"),
			(val_add, reg0, ":body"),
		(else_try),
			(item_get_value, reg0, ":item_id"),
			(assign, ":save_fp", 1),
			(convert_to_fixed_point, ":save_fp"),
			(set_fixed_point_multiplier, 1000),
			(item_modifier_get_value_multiplier, ":coeff", ":item_modifier"),
			(val_mul, reg0, ":coeff"),
			(val_div, reg0, 1000),
			(set_fixed_point_multiplier, ":save_fp"),
		(try_end),
	]),

	("lco_highlight_items", [
		(store_script_param, ":hilight", 1),
		(try_begin),
			(neq, ":hilight", 0),
			(store_script_param, ":item_id", 2),
			(store_script_param, ":item_modifier", 3),
			(call_script, "script_lco_get_item_primary_stat", ":item_id", ":item_modifier"),
			(assign, ":base_stat", reg0),
			(item_get_type, ":item_type", ":item_id"),
		(try_end),
		(store_mul, ":offset", "$g_lco_heroes", 2),
		(val_add, ":offset", 40),
		(val_add, ":offset", "$g_lco_inv_slots"),
		(try_for_range, ":index", 0, "$g_lco_inv_slots"),
			(store_add, ":inventory_offset", ":index", num_equipment_kinds), # Actual inventory slot for player
			(store_add, ":overlay_offset", ":offset", ":index"),
			(troop_get_slot, ":overlay_id", lco_storage, ":overlay_offset"), # Text overlay for slot
			(try_begin),
				(call_script, "script_cf_lco_slot_is_frozen", ":inventory_offset"),
			(else_try),
				(eq, ":hilight", 0), # Turn hilight off?
				(overlay_set_color, ":overlay_id", 0x00000000),
			(else_try),
				(troop_get_inventory_slot, ":inv_id", "trp_player", ":inventory_offset"),
				(lt, ":inv_id", 0),
				(overlay_set_color, ":overlay_id", 0x00000000),
			(else_try),
				(item_get_type, ":inv_type", ":inv_id"),
				(neq, ":item_type", ":inv_type"),
				(overlay_set_color, ":overlay_id", 0x00606060),
			(else_try),
				(troop_get_inventory_slot_modifier, ":inv_modifier", "trp_player", ":inventory_offset"),
				(call_script, "script_lco_get_item_primary_stat", ":inv_id", ":inv_modifier"),
				(gt, reg0, ":base_stat"),
				(overlay_set_color, ":overlay_id", 0x00004000),
			(else_try),
				(lt, reg0, ":base_stat"),
				(overlay_set_color, ":overlay_id", 0x00400000),
			(else_try),
				(overlay_set_color, ":overlay_id", 0x00000000),
			(try_end),
		(try_end),
	]),

]

presentations = [

	# Reference on slot usage.
	#
	# Two troops are used by Companions Overseer. They are referenced in module_constants as lco_storage and lco_garbage.
	#
	# lco_garbage troop slots are only used to store the experience-needed-to-level table which is initialized once per game.
	#
	# lco_storage troop slots are filled with references dynamically at the start of presentation according to following schema:
	#   *. List of all troops to display is generated. Total amount is stored in $g_lco_heroes.
	#   1. Starting from 0, a total of $g_lco_heroes slots are used to store references to troop name panels (overlay_id's).
	#   2. After that, the same amount of slots is used to store references to troops (troop_id's).
	#
	# For equipment_overview presentation, additional slots are used:
	#
	#   3. After that, 11 slots are used to store references to hero equipment panels, and 11 more to store references to their respective text labels.
	#   4. After that, 9 slots are used to store references to player equipment panels, and 9 more to store references to their respective text labels.
	#   *. Number of player equipment slots is calculated and stored in $g_lco_inv_slots. Note that 10 first slots are actually equipment slots and are not included in the count.
	#   5. After that, a total of $g_lco_inv_slots slots are used to store references to player inventory panels, and $g_lco_inv_slots more to store references to their text labels.
	#
	# References to all other important overlays are stored in global variables. References to static overlays are not permanently stored.

	("equipment_overview", 0, mesh.ui_bg_mp_profile, [

		(ti_on_presentation_load, [

			# PRESENTATION INITIALIZATION AND GENERIC ELEMENTS

			(call_script, "script_lco_initialize_presentation"),

			(ui_create_label, reg0, "str_lco_i_title_companions", 250, 714, tf_center_justify),
			(str_store_troop_name, s40, "trp_player"),
			(ui_create_label, reg0, "str_lco_s40", 750, 714, tf_center_justify),
			(str_clear, s40),
			(ui_create_mesh, reg0, "mesh_pic_camp", -300, 138, 750, 750),
			(ui_create_mesh, reg0, "mesh_pic_messenger", 110, 138, 750, 750),

			# PRESENTATION AUTO-EQUIP FORM

			(ui_create_label, reg0, "str_lco_i_ae_with", 275, 175, 750, 0),
			(ui_create_label, reg0, "str_lco_i_ae_with", 275, 175, 750, 0),
			(ui_create_checkbox, "$g_lco_cb_0", "mesh_checkbox_off", "mesh_checkbox_on", 275, 150, "$g_lco_auto_horses"),
			(ui_create_checkbox, "$g_lco_cb_1", "mesh_checkbox_off", "mesh_checkbox_on", 375, 150, "$g_lco_auto_armors"),
			(ui_create_checkbox, "$g_lco_cb_2", "mesh_checkbox_off", "mesh_checkbox_on", 275, 125, "$g_lco_auto_shields"),
			(ui_create_label, reg0, "str_lco_i_ae_with_horses",  300, 150, 0, 750),
			(ui_create_label, reg0, "str_lco_i_ae_with_armors",  400, 150, 0, 750),
			(ui_create_label, reg0, "str_lco_i_ae_with_shields", 300, 125, 0, 750),

			(ui_create_game_button, "$g_lco_auto_equip",     "str_lco_i_ae_companion", 355, 75, 190, 42),
			(ui_create_game_button, "$g_lco_auto_equip_all", "str_lco_i_ae_everyone",  355, 25, 190, 42),

			# GENERATING HERO NAME PANELS

			(ui_create_label, reg0, "str_lco_i_hero_panel_title", 25, 652, 0, 750),
			(ui_create_label, reg0, "str_lco_i_hero_panel_title", 25, 652, 0, 750),

			(ui_create_container, reg0, 0, 125, 250, 525+2),
			(set_container_overlay, reg0),

			(store_mul, ":base_y", "$g_lco_heroes", 25),
			(val_sub, ":base_y", 25),
			(val_max, ":base_y", 500),
			(try_for_range, ":index", 0, "$g_lco_heroes"),
				(troop_get_slot, ":troop_id", lco_storage, ":index"),
				(store_add, ":offset", "$g_lco_heroes", ":index"),
				(troop_set_slot, lco_storage, ":offset", ":troop_id"),
				(store_mul, ":y", ":index", 25),
				(store_sub, ":y", ":base_y", ":y"),
				(ui_create_mesh, reg0, "mesh_ui_btn_long_u", 25, ":y", 310, 300),
				(troop_set_slot, lco_storage, ":index", reg0),
			(try_end),
			(store_mul, ":y", "$g_lco_active_hero", 25),
			(store_sub, ":y", ":base_y", ":y"),
			(ui_create_mesh, "$g_lco_active_panel", "mesh_ui_btn_long_d", 25, ":y", 310, 300),
			(val_add, ":base_y", 1),
			(try_for_range, ":index", 0, "$g_lco_heroes"),
				(store_add, ":offset", "$g_lco_heroes", ":index"),
				(troop_get_slot, ":troop_id", lco_storage, ":offset"),
				(store_mul, ":y", ":index", 25),
				(store_sub, ":y", ":base_y", ":y"),
				(call_script, "script_lco_troop_name_to_s40", ":troop_id"),
				(ui_create_label, reg0, "str_lco_s40", 30, ":y", 0, 750),
			(try_end),
			(str_clear, s40),
			(set_container_overlay, -1),

			# GENERATING HERO EQUIPMENT PANELS

			# Weapons:
			(store_mul, ":index", "$g_lco_heroes", 2),
			(ui_create_label, reg0, "str_lco_i_weapons", 272, 650, 0, 750),
			(ui_create_label, reg0, "str_lco_i_weapons", 272, 650, 0, 750),
			(try_for_range, reg1, 0, 4),
				(store_mul, ":y", reg1, 25),
				(store_sub, ":y", 625, ":y"),
				(ui_create_mesh, reg0, "mesh_ui_btn_long_u", 272, ":y", 310, 300),
				(troop_set_slot, lco_storage, ":index", reg0),
				(val_add, ":index", 1),
			(try_end),
			# Armor:
			(ui_create_label, reg0, "str_lco_i_armor", 272, 500, 0, 750),
			(ui_create_label, reg0, "str_lco_i_armor", 272, 500, 0, 750),
			(try_for_range, reg1, 0, 4),
				(store_mul, ":y", reg1, 25),
				(store_sub, ":y", 475, ":y"),
				(ui_create_mesh, reg0, "mesh_ui_btn_long_u", 272, ":y", 310, 300),
				(troop_set_slot, lco_storage, ":index", reg0),
				(val_add, ":index", 1),
			(try_end),
			# Horse:
			(ui_create_label, reg0, "str_lco_i_horse", 272, 350, 0, 750),
			(ui_create_label, reg0, "str_lco_i_horse", 272, 350, 0, 750),
			(ui_create_mesh, reg0, "mesh_ui_btn_long_u", 272, 325, 310, 300),
			(troop_set_slot, lco_storage, ":index", reg0),
			(val_add, ":index", 1),
			# Books:
			(try_begin),
				(eq, "$g_lco_suppress_books", 0),
				(ui_create_label, reg0, "str_lco_i_books", 272, 275, 0, 750),
				(ui_create_label, reg0, "str_lco_i_books", 272, 275, 0, 750),
				(try_for_range, reg1, 0, 2),
					(store_mul, ":y", reg1, 25),
					(store_sub, ":y", 250, ":y"),
					(ui_create_mesh, reg0, "mesh_ui_btn_long_u", 272, ":y", 310, 300),
					(troop_set_slot, lco_storage, ":index", reg0),
					(val_add, ":index", 1),
				(try_end),
			(else_try),
				(val_add, ":index", 2),
			(try_end),

			# GENERATING HERO EQUIPMENT TEXT FIELDS

			# Weapons:
			(str_clear, s40),
			(try_for_range, reg1, 0, 4),
				(store_mul, ":y", reg1, 25),
				(store_sub, ":y", 625+1, ":y"),
				(ui_create_label, reg0, s40, 277, ":y", 0, 750),
				(troop_set_slot, lco_storage, ":index", reg0),
				(val_add, ":index", 1),
			(try_end),
			# Armor:
			(try_for_range, reg1, 0, 4),
				(store_mul, ":y", reg1, 25),
				(store_sub, ":y", 475+1, ":y"),
				(ui_create_label, reg0, s40, 277, ":y", 0, 750),
				(troop_set_slot, lco_storage, ":index", reg0),
				(val_add, ":index", 1),
			(try_end),
			# Horse:
			(ui_create_label, reg0, s40, 277, 325+1, 0, 750),
			(troop_set_slot, lco_storage, ":index", reg0),
			(val_add, ":index", 1),
			# Books:
			(try_begin),
				(eq, "$g_lco_suppress_books", 0),
				(try_for_range, reg1, 0, 2),
					(store_mul, ":y", reg1, 25),
					(store_sub, ":y", 250, ":y"),
					(ui_create_label, reg0, s40, 277, ":y", 0, 750),
					(troop_set_slot, lco_storage, ":index", reg0),
					(val_add, ":index", 1),
				(try_end),
			(else_try),
				(val_add, ":index", 2),
			(try_end),

			# GENERATING PLAYER EQUIPMENT PANELS

			# Weapons:
			(ui_create_label, reg0, "str_lco_i_weapons", 512, 650, 0, 750),
			(ui_create_label, reg0, "str_lco_i_weapons", 512, 650, 0, 750),
			(try_for_range, reg1, 0, 4),
				(store_mul, ":y", reg1, 25),
				(store_sub, ":y", 625, ":y"),
				(ui_create_mesh, reg0, "mesh_ui_btn_long_u", 512, ":y", 310, 300),
				(troop_set_slot, lco_storage, ":index", reg0),
				(val_add, ":index", 1),
			(try_end),
			# Armor:
			(ui_create_label, reg0, "str_lco_i_armor", 512, 500, 0, 750),
			(ui_create_label, reg0, "str_lco_i_armor", 512, 500, 0, 750),
			(try_for_range, reg1, 0, 4),
				(store_mul, ":y", reg1, 25),
				(store_sub, ":y", 475, ":y"),
				(ui_create_mesh, reg0, "mesh_ui_btn_long_u", 512, ":y", 310, 300),
				(troop_set_slot, lco_storage, ":index", reg0),
				(val_add, ":index", 1),
			(try_end),
			# Horse:
			(ui_create_label, reg0, "str_lco_i_horse", 512, 350, 0, 750),
			(ui_create_label, reg0, "str_lco_i_horse", 512, 350, 0, 750),
			(ui_create_mesh, reg0, "mesh_ui_btn_long_u", 512, 325, 310, 300),
			(troop_set_slot, lco_storage, ":index", reg0),
			(val_add, ":index", 1),

			# GENERATING PLAYER EQUIPMENT TEXT FIELDS

			# Weapons:
			(try_for_range, reg1, 0, 4),
				(store_mul, ":y", reg1, 25),
				(store_sub, ":y", 625+1, ":y"),
				(ui_create_label, reg0, s40, 517, ":y", 0, 750),
				(troop_set_slot, lco_storage, ":index", reg0),
				(val_add, ":index", 1),
			(try_end),
			# Armor:
			(try_for_range, reg1, 0, 4),
				(store_mul, ":y", reg1, 25),
				(store_sub, ":y", 475+1, ":y"),
				(ui_create_label, reg0, s40, 517, ":y", 0, 750),
				(troop_set_slot, lco_storage, ":index", reg0),
				(val_add, ":index", 1),
			(try_end),
			# Horse:
			(ui_create_label, reg0, s40, 517, 325+1, 0, 750),
			(troop_set_slot, lco_storage, ":index", reg0),
			(val_add, ":index", 1),

			# GENERATING PLAYER INVENTORY PANELS

			(ui_create_label, reg0, "str_lco_i_inventory", 750, 652, 0, 750),
			(ui_create_label, reg0, "str_lco_i_inventory", 750, 652, 0, 750),
			(ui_create_image_button, "$g_lco_sort_inventory", "mesh_ui_btn_downarrow_u", "mesh_ui_btn_downarrow_d", 935, 655, 200, 200),

			(ui_create_container, reg0, 750, 125, 215, 525+2),
			(set_container_overlay, reg0),

			(store_mul, ":top", "$g_lco_inv_slots", 25),
			(val_sub, ":top", 25),
			(val_max, ":top", 500),
			(try_for_range, reg1, 0, "$g_lco_inv_slots"),
				(store_mul, ":y", reg1, 25),
				(store_sub, ":y", ":top", ":y"),
				(ui_create_mesh, reg0, "mesh_ui_btn_long_u", 0, ":y", 300, 300),
				(troop_set_slot, lco_storage, ":index", reg0),
				(val_add, ":index", 1),
			(try_end),
			(try_for_range, reg1, 0, "$g_lco_inv_slots"),
				(store_mul, ":y", reg1, 25),
				(store_sub, ":y", ":top", ":y"),
				(val_add, ":y", 1),
				(ui_create_label, reg0, "str_empty_string", 5, ":y", 0, 750),
				(troop_set_slot, lco_storage, ":index", reg0),
				(val_add, ":index", 1),
			(try_end),

			(set_container_overlay, -1),

			# GENERATING DISCARDED ITEMS INTERFACE

			(ui_create_label, reg0, "str_lco_i_discard", 512, 275, 0, 750),
			(ui_create_label, reg0, "str_lco_i_discard", 512, 275, 0, 750),
			(ui_create_game_button, "$g_lco_retrieve", "str_lco_i_retrieve", 605, 25, 190, 42),
			(ui_create_container, reg0, 515, 75, 200, 200+2),
			(set_container_overlay, reg0),
			(store_mul, ":top", "$g_lco_garb_slots", 25),
			(val_sub, ":top", 25),
			(val_max, ":top", 175),
			(try_for_range, reg1, 0, "$g_lco_garb_slots"),
				(store_mul, ":y", reg1, 25),
				(store_sub, ":y", ":top", ":y"),
				(ui_create_mesh, reg0, "mesh_ui_btn_long_u", 0, ":y", 282, 300),
				(troop_set_slot, lco_storage, ":index", reg0),
				(val_add, ":index", 1),
			(try_end),
			(val_add, ":top", 1),
			(try_for_range, reg1, 0, "$g_lco_garb_slots"),
				(store_mul, ":y", reg1, 25),
				(store_sub, ":y", ":top", ":y"),
				(ui_create_label, reg0, "str_empty_string", 5, ":y", 0, 750),
				(troop_set_slot, lco_storage, ":index", reg0),
				(val_add, ":index", 1),
			(try_end),
			(set_container_overlay, -1),


			# GENERATING PLAYER MONEY INDICATOR

			(ui_create_mesh, reg0, "mesh_ui_gold_icon", 775, 82, 250, 250),
			(store_troop_gold, reg60, "trp_player"),
			(call_script, "script_game_get_money_text", reg60),
			(str_store_string_reg, s40, s1),
			(ui_create_label, reg0, "str_lco_s40", 810, 90, 0, 850),
			(overlay_set_color, reg0, 0xFFFF00),
			(ui_create_label, reg0, "str_lco_s40", 810, 90, 0, 850),
			(ui_create_label, reg0, "str_lco_s40", 810, 90, 0, 850),

			# GENERATING PANEL AND TEXT FOR DRAG-N-DROP ITEM

			(ui_create_container, "$g_lco_dragging_panel", 0, 0, 225, 27),
			(set_container_overlay, "$g_lco_dragging_panel"),
			(overlay_set_display, "$g_lco_dragging_panel", 0),

			(ui_create_mesh, reg0, "mesh_ui_btn_long_u", 0, 0, 310, 300),
			(ui_create_label, "$g_lco_dragging_text", s40, 5, 1, 0, 750),

			(set_container_overlay, -1),

			# FINALLY FILLING ALL THOSE PANELS WITH ACTUAL DATA

			(call_script, "script_lco_fill_hero_panels"),
			(call_script, "script_lco_fill_player_panels"),

		]),

		(ti_on_presentation_event_state_change, [

			(store_trigger_param_1, ":overlay_id"),
			(store_trigger_param_2, ":value"),
			(assign, ":sound", 1),
			(try_begin),
				(eq, ":overlay_id", "$g_lco_return"),
				(try_begin),
					(eq, "$g_lco_dragging", 1),
					(call_script, "script_lco_cancel_drag_item"),
				(try_end),
				(try_begin),
					(eq, "$g_lco_dragging", 1),
					(display_message, "str_lco_error_drop_first", 0xFF4040),
				(else_try),
					(call_script, "script_lco_clear_all_items", "$g_lco_garbage_troop"),
					(assign, "$g_lco_garbage_troop", lco_garbage),
					#(jump_to_menu, "mnu_lco_auto_return"),
					(try_begin),
						(gt, "$g_lco_return_to", 0),
						(assign, "$window_manager_action", WM_MENU),
						(assign, "$window_manager_param1", "$g_lco_return_to"),
					(else_try),
						(assign, "$window_manager_action", WM_RETURN),
					(try_end),
					(assign, "$extra_text_preq_display", 0), # Tell NE's script_game_get_item_extra_text to no longer generate item's prerequisite line
					(presentation_set_duration, 0),
				(try_end),
			(else_try),
				(eq, ":overlay_id", "$g_lco_retrieve"),
				(try_begin),
					(this_or_next|key_is_down, key_left_control),
					(key_is_down, key_right_control),
					(call_script, "script_lco_retrieve_discarded_best"),
				(else_try),
					(call_script, "script_lco_retrieve_discarded"),
				(try_end),
				(call_script, "script_lco_fill_player_panels"),
			(else_try),
				(eq, ":overlay_id", "$g_lco_sort_inventory"),
				(call_script, "script_lco_sort_player_inventory"),
				(call_script, "script_lco_fill_player_panels"),
		   (else_try),
				(eq, ":overlay_id", "$g_lco_cb_0"),
				(assign, "$g_lco_auto_horses", ":value"),
			(else_try),
				(eq, ":overlay_id", "$g_lco_cb_1"),
				(assign, "$g_lco_auto_armors", ":value"),
			(else_try),
				(eq, ":overlay_id", "$g_lco_cb_2"),
				(assign, "$g_lco_auto_shields", ":value"),
			(else_try),
				(eq, ":overlay_id", "$g_lco_inc_0"),
				(assign, "$g_lco_include_companions", ":value"),
				(assign, "$extra_text_preq_display", 0), # Tell NE's script_game_get_item_extra_text to no longer generate item's prerequisite line
				(presentation_set_duration, 0),
			(else_try),
				(eq, ":overlay_id", "$g_lco_inc_1"),
				(assign, "$g_lco_include_lords", ":value"),
				(assign, "$extra_text_preq_display", 0), # Tell NE's script_game_get_item_extra_text to no longer generate item's prerequisite line
				(presentation_set_duration, 0),
			(else_try),
				(eq, ":overlay_id", "$g_lco_inc_2"),
				(assign, "$g_lco_include_regulars", ":value"),
				(assign, "$extra_text_preq_display", 0), # Tell NE's script_game_get_item_extra_text to no longer generate item's prerequisite line
				(presentation_set_duration, 0),
			(else_try),
				(eq, ":overlay_id", "$g_lco_switch_page_0"),
				(assign, "$g_lco_page", 0),
				(assign, "$window_manager_action", WM_PRESENTATION),
				(assign, "$window_manager_param1", "prsnt_companions_overview"),
				(assign, "$extra_text_preq_display", 0), # Tell NE's script_game_get_item_extra_text to no longer generate item's prerequisite line
				(presentation_set_duration, 0),
			(else_try),
				(eq, ":overlay_id", "$g_lco_switch_page_1"),
				(assign, "$g_lco_page", 1),
				(assign, "$window_manager_action", WM_PRESENTATION),
				(assign, "$window_manager_param1", "prsnt_companions_overview"),
				(assign, "$extra_text_preq_display", 0), # Tell NE's script_game_get_item_extra_text to no longer generate item's prerequisite line
				(presentation_set_duration, 0),
			(else_try),
				(eq, ":overlay_id", "$g_lco_switch_page_2"),
			(else_try),
				(eq, ":overlay_id", "$g_lco_auto_equip"),
				(try_begin),
					(store_add, ":hero_offset", "$g_lco_heroes", "$g_lco_active_hero"),
					(troop_get_slot, ":troop_id", lco_storage, ":hero_offset"),
					(call_script, "script_cf_lco_controllable", ":troop_id"),
					(call_script, "script_lco_backup_inventory", ":troop_id"),
					(call_script, "script_lco_hero_grab_equipment", ":troop_id"),
					(troop_equip_items, ":troop_id"),
					(call_script, "script_lco_hero_return_equipment", ":troop_id"),
					(call_script, "script_lco_retrieve_inventory", ":troop_id"),
					(troop_get_type, reg60, ":troop_id"),
					(str_store_troop_name, s41, ":troop_id"),
					(display_message, "str_lco_message_hero_ae"),
					(call_script, "script_lco_fill_hero_panels"),
					(call_script, "script_lco_fill_player_panels"),
				(else_try),
					(display_message, "str_lco_drop_error_control", 0xFF4040),
				(try_end),
			(else_try),
				(eq, ":overlay_id", "$g_lco_auto_equip_all"),
				(store_add, ":upper_range", "$g_lco_heroes", "$g_lco_heroes"),
				(try_for_range, ":hero_offset", "$g_lco_heroes", ":upper_range"),
					(troop_get_slot, ":troop_id", lco_storage, ":hero_offset"),
					(call_script, "script_cf_lco_controllable", ":troop_id"),
					(call_script, "script_lco_backup_inventory", ":troop_id"),
					(call_script, "script_lco_hero_grab_equipment", ":troop_id"),
					(troop_equip_items, ":troop_id"),
					(call_script, "script_lco_hero_return_equipment", ":troop_id"),
					(call_script, "script_lco_retrieve_inventory", ":troop_id"),
				(try_end),
				(display_message, "str_lco_message_all_heroes_ae"),
				(call_script, "script_lco_fill_hero_panels"),
				(call_script, "script_lco_fill_player_panels"),
			(else_try),
				(assign, ":sound", 0),
			(try_end),
			(try_begin),
				(eq, ":value", 1),
				(eq, ":sound", 1),
				(play_sound, "snd_click"),
			(try_end),

		]),

		(ti_on_presentation_mouse_press, [

			(store_trigger_param_1, ":overlay_id"),
			(store_trigger_param_2, ":mouse_button"),
			(try_begin),
				(eq, ":mouse_button", 0), # Left mouse button

				# Checking if it's one of hero panels
				(try_begin),
					(eq, "$g_lco_panel_found", 0),
					(try_for_range, ":index", 0, "$g_lco_heroes"),
						(troop_slot_eq, lco_storage, ":index", ":overlay_id"),
						(assign, "$g_lco_panel_found", 1),
						(play_sound, "snd_click"),
						(try_begin),
							(this_or_next|key_is_down, key_left_control),
							(key_is_down, key_right_control),
							(try_begin),
								(eq, "$g_lco_dragging", 1),
								(store_add, ":hero_offset", "$g_lco_heroes", ":index"),
								(troop_get_slot, ":recipient_id", lco_storage, ":hero_offset"),
								(call_script, "script_cf_lco_controllable", ":recipient_id"),
								(try_begin),
									(call_script, "script_cf_lco_auto_offer_item", ":recipient_id", "$g_lco_drag_item", "$g_lco_drag_modifier", "$g_lco_drag_quantity"),
									(try_begin),
										(ge, reg0, 0),
										(assign, "$g_lco_drag_item", reg0),
										(assign, "$g_lco_drag_modifier", reg1),
										(assign, "$g_lco_drag_quantity", reg2),
										(assign, "$g_lco_drag_quantity_max", reg3),
										(call_script, "script_lco_item_name_to_s41", "$g_lco_drag_item", "$g_lco_drag_modifier", "$g_lco_drag_quantity", "$g_lco_drag_quantity_max"),
										(overlay_set_text, "$g_lco_dragging_text", s41),
									(else_try),
										(assign, "$g_lco_drag_item", -1),
										(assign, "$g_lco_drag_modifier", 0),
										(assign, "$g_lco_drag_quantity", 0),
										(assign, "$g_lco_drag_quantity_max", 0),
										(overlay_set_display, "$g_lco_dragging_panel", 0),
										(assign, "$g_lco_dragging", 0),
									(try_end),
									(call_script, "script_lco_fill_hero_panels"),
									(call_script, "script_lco_fill_player_panels"),
								(else_try),
									(str_store_troop_name, s40, ":recipient_id"),
									(call_script, "script_lco_item_name_to_s41", "$g_lco_drag_item", "$g_lco_drag_modifier", "$g_lco_drag_quantity", "$g_lco_drag_quantity_max"),
									(str_store_string, s40, "str_lco_message_hero_no_need"),
									(display_message, s40, 0xFF4040),
								(try_end),
							(try_end),
						(else_try),
							(this_or_next|key_is_down, key_left_alt),
							(key_is_down, key_right_alt),
							(call_script, "script_lco_set_active_hero", ":index"),
							(try_begin),
								(eq, "$g_lco_dragging", 1),
								(display_message, "str_lco_error_drop_first", 0xFF4040),
							(else_try),
								(store_add, ":hero_offset", "$g_lco_heroes", ":index"),

								#(troop_get_slot, "$g_lco_target", lco_storage, ":hero_offset"),
								#(assign, "$g_lco_operation", lco_view_character),
								#(jump_to_menu, "mnu_lco_auto_return"),

								(assign, "$window_manager_action", WM_MAP_CONVERSATION),
								(troop_get_slot, "$window_manager_param1", lco_storage, ":hero_offset"),
								(assign, "$window_manager_param2", "prsnt_equipment_overview"),
								(assign, "$talk_context", tc_companions_overseer),
								(modify_visitors_at_site, "scn_conversation_scene"),
								(reset_visitors),
								(set_visitor, 0, "trp_player"),
								(set_visitor, 17, "$window_manager_param1"),
								(set_jump_mission, "mt_conversation_encounter"),
								(jump_to_scene, "scn_conversation_scene"),

								(assign, "$extra_text_preq_display", 0), # Tell NE's script_game_get_item_extra_text to no longer generate item's prerequisite line
								(presentation_set_duration, 0),
							(try_end),
						(else_try),
							(call_script, "script_lco_set_active_hero", ":index"),
						(try_end),
					(try_end),
				(try_end),

				# Checking if it's one of item panels
				(try_begin),
					(eq, "$g_lco_panel_found", 0),
					(call_script, "script_cf_lco_is_active_panel", ":overlay_id"),
					(assign, "$g_lco_panel_found", 1),
					(play_sound, "snd_click"),
					(call_script, "script_lco_get_slot_details_for_panel", ":overlay_id"),
					(assign, ":troop_id", reg0),
					(assign, ":slot_id", reg1),
					(assign, ":item_id", reg2),
					(assign, ":modifier", reg3),
					(assign, ":quantity", reg4),
					(assign, ":quantity_max", reg5),
					(try_begin),
						(eq, "$g_lco_dragging", 0), # We are currently not dragging anything, so either drag start or quick give or item offer
						(try_begin),
							(ge, ":item_id", 0), # There is an item inside
							(try_begin),
								(this_or_next|key_is_down, key_left_control),
								(key_is_down, key_right_control),

								# This is a Ctrl-Click on an item while not dragging anything
								# For a player, this is an offer of an item to current hero
								# For a hero, this is a quick-move of item to player's inventory
								(try_begin),
									(eq, ":troop_id", "trp_player"), # Offering item to hero
									(store_add, ":hero_offset", "$g_lco_heroes", "$g_lco_active_hero"),
									(troop_get_slot, ":recipient_id", lco_storage, ":hero_offset"),
									(try_begin),
										(call_script, "script_cf_lco_auto_offer_item", ":recipient_id", ":item_id", ":modifier", ":quantity"),
										(try_begin),
											(ge, reg0, 0),
											(troop_set_inventory_slot, ":troop_id", ":slot_id", reg0),
											(troop_set_inventory_slot_modifier, ":troop_id", ":slot_id", reg1),
										(else_try),
											(troop_set_inventory_slot, ":troop_id", ":slot_id", -1),
										(try_end),
										(call_script, "script_lco_fill_hero_panels"),
										(call_script, "script_lco_fill_player_panels"),
									(else_try),
										(str_store_troop_name, s40, ":recipient_id"),
										(call_script, "script_lco_item_name_to_s41", ":item_id", ":modifier", ":quantity", ":quantity_max"),
										(str_store_string, s40, "str_lco_message_hero_no_need"),
										(display_message, s40, 0xFF4040),
									(try_end),
								(else_try),
									(assign, ":given", 0),
									(try_begin),
										(call_script, "script_cf_lco_controllable", ":troop_id"),
										(troop_get_inventory_capacity, ":capacity", "trp_player"),
										(try_for_range, ":index", num_equipment_kinds, ":capacity"),
											(eq, ":given", 0), # Failsafe
											(troop_get_inventory_slot, ":cur_item", "trp_player", ":index"),
											(lt, ":cur_item", 0),
											(troop_set_inventory_slot, "trp_player", ":index", ":item_id"),
											(troop_set_inventory_slot_modifier, "trp_player", ":index", ":modifier"),
											(try_begin),
												(gt, ":quantity", 0),
												(troop_inventory_slot_set_item_amount, ":quantity"),
											(try_end),
											(troop_set_inventory_slot, ":troop_id", ":slot_id", -1),
											(assign, ":given", 1),
											(assign, ":capacity", 0), # Break cycle
										(try_end),
										(try_begin),
											(eq, ":given", 0),
											(display_message, "str_lco_error_inv_full", 0xFF4040),
										(else_try),
											(call_script, "script_lco_fill_hero_panels"),
											(call_script, "script_lco_fill_player_panels"),
										(try_end),
									(else_try),
										(str_store_troop_name, s40, ":recipient_id"),
										(display_message, "str_lco_drop_error_control", 0xFF4040),
									(try_end),
								(try_end),

							(else_try),
								# Alt-Click means quick-deletion of object
								(this_or_next|key_is_down, key_left_alt),
								(key_is_down, key_right_alt),

								(try_begin),
									(call_script, "script_cf_lco_controllable", ":troop_id"),
									(neq, ":troop_id", "$g_lco_garbage_troop"),
									(call_script, "script_lco_discard_item", ":item_id", ":modifier", ":quantity"),
									(troop_set_inventory_slot, ":troop_id", ":slot_id", -1),
									(call_script, "script_lco_fill_hero_panels"),
									(call_script, "script_lco_fill_player_panels"),
								(try_end),


							(else_try),

								(this_or_next|key_is_down, key_left_shift),
								(key_is_down, key_right_shift),
								(eq, ":troop_id", "trp_player"),

								# This is a Shift-Click on a player's item while not dragging anything
								# This item will be offered to all heroes in sequence, swapping as appropriate.
								(assign, ":upper_range", "$g_lco_heroes"),
								(assign, ":any_changes", 0),
								(try_for_range, ":index", 0, ":upper_range"),
									(store_add, ":hero_offset", "$g_lco_heroes", ":index"),
									(troop_get_slot, ":recipient_id", lco_storage, ":hero_offset"),
									(call_script, "script_cf_lco_auto_offer_item", ":recipient_id", ":item_id", ":modifier", ":quantity"),
									(str_store_troop_name, s40, ":recipient_id"),
									(troop_get_type, reg4, ":recipient_id"),
									(call_script, "script_lco_item_name_to_s41", ":item_id", ":modifier", ":quantity", ":quantity_max"),
									(try_begin),
										(ge, reg0, 0), # Agent returned some item as well
										(str_store_string, s39, s41),
										(call_script, "script_lco_item_name_to_s41", reg0, reg1, reg2, reg3),
										(display_message, "str_lco_message_hero_replaced"),
									(else_try),
										(display_message, "str_lco_message_hero_equipped"),
										(assign, ":upper_range", 0), # Break cycle
									(try_end),
									(assign, ":item_id", reg0),
									(assign, ":modifier", reg1),
									(assign, ":quantity", reg2),
									(assign, ":quantity_max", reg3),
									(assign, ":any_changes", 1),
								(try_end),
								# Now we need to replace or remove the original item
								(try_begin),
									(ge, ":item_id", 0),
									(troop_set_inventory_slot, ":troop_id", ":slot_id", ":item_id"),
									(troop_set_inventory_slot_modifier, ":troop_id", ":slot_id", ":item_id"),
								(else_try),
									(troop_set_inventory_slot, ":troop_id", ":slot_id", -1),
								(try_end),
								(try_begin),
									(eq, ":any_changes", 1),
									(call_script, "script_lco_fill_hero_panels"),
									(call_script, "script_lco_fill_player_panels"),
								(else_try),
									(call_script, "script_lco_item_name_to_s41", ":item_id", ":modifier", ":quantity", ":quantity_max"),
									(display_message, "str_lco_message_nobody_needs", 0xFF4040),
								(try_end),

							(else_try),

								(call_script, "script_lco_drag_item", ":troop_id", ":slot_id"),
								(call_script, "script_lco_fill_hero_panels"),
								(call_script, "script_lco_fill_player_panels"),

							(try_end),
						(try_end),
					(else_try),
						# Item panel was clicked while player is dragging an item
						(try_begin),
							(call_script, "script_cf_lco_can_drop_item", ":troop_id", ":slot_id", "$g_lco_drag_item", "$g_lco_drag_modifier"),
							(call_script, "script_lco_drop_item", ":troop_id", ":slot_id"),
							(call_script, "script_lco_fill_hero_panels"),
							(call_script, "script_lco_fill_player_panels"),
						(else_try),
							(display_message, reg0, 0xFF4040),
						(try_end),
					(try_end),
				(try_end),

			(else_try),
				(eq, ":mouse_button", 1), # Right mouse button
				(eq, "$g_lco_panel_found", 0), # Normal processing has not been prevented by trigger in ti_on_presentation_run
				(eq, "$g_lco_dragging", 0), # We are currently not dragging anything
				(call_script, "script_cf_lco_is_active_panel", ":overlay_id"),
				(assign, "$g_lco_panel_found", 1),
				(play_sound, "snd_click"),
				(call_script, "script_lco_get_slot_details_for_panel", ":overlay_id"),
				(eq, reg0, "trp_player"), # Right mouse button clicked on one of player's panels
				(ge, reg1, num_equipment_kinds), # What's more, this is one of player's *inventory* panels which we can actually freeze!
				(call_script, "script_lco_freeze_slot_toggle", reg1), # We switch frozen status for this slot
				(call_script, "script_lco_fill_player_panels"), # And refresh the screen
			(try_end),

		]),

		(ti_on_presentation_run, [

			(set_fixed_point_multiplier, 1000),
			(assign, "$g_lco_panel_found", 0), # We enable mouse click detection every frame, but it only works once per frame (see ti_on_presentation_mouse_press)
			# ESC quits the presentation
			(try_begin),
				(key_clicked, key_escape),
				(try_begin),
					(eq, "$g_lco_dragging", 1),
					(call_script, "script_lco_cancel_drag_item"),
				(try_end),
				(try_begin),
					(eq, "$g_lco_dragging", 1),
					(display_message, "str_lco_error_drop_first", 0xFF4040),
				(else_try),
					(call_script, "script_lco_clear_all_items", "$g_lco_garbage_troop"),
					(assign, "$g_lco_garbage_troop", lco_garbage),
					#(jump_to_menu, "mnu_lco_auto_return"),
					(try_begin),
						(gt, "$g_lco_return_to", 0),
						(assign, "$window_manager_action", WM_MENU),
						(assign, "$window_manager_param1", "$g_lco_return_to"),
					(else_try),
						(assign, "$window_manager_action", WM_RETURN),
					(try_end),
					(assign, "$extra_text_preq_display", 0), # Tell NE's script_game_get_item_extra_text to no longer generate item's prerequisite line
					(presentation_set_duration, 0),
				(try_end),
			(try_end),
			# TAB and SHIFT-TAB switch current hero
			(try_begin),
				(key_clicked, key_tab),
				(try_begin),
					(this_or_next|key_is_down, key_left_shift),
					(key_is_down, key_right_shift),
					(store_add, ":new_index", "$g_lco_active_hero", "$g_lco_heroes"),
					(val_sub, ":new_index", 1),
					(val_mod, ":new_index", "$g_lco_heroes"),
					(call_script, "script_lco_set_active_hero", ":new_index"),
				(else_try),
					(this_or_next|key_is_down, key_left_control),
					(key_is_down, key_right_control),
					#(assign, "$g_lco_page", 0),
					(assign, "$window_manager_action", WM_PRESENTATION),
					(assign, "$window_manager_param1", "prsnt_companions_overview"),
					(assign, "$extra_text_preq_display", 0), # Tell NE's script_game_get_item_extra_text to no longer generate item's prerequisite line
					(presentation_set_duration, 0),
				(else_try),
					(neg|key_is_down, key_left_alt),
					(neg|key_is_down, key_right_alt),
					(store_add, ":new_index", "$g_lco_active_hero", 1),
					(val_mod, ":new_index", "$g_lco_heroes"),
					(call_script, "script_lco_set_active_hero", ":new_index"),
				(try_end),
			(try_end),
			# RIGHT MOUSE CLICK cancels dragging item, if there is any
			(try_begin),
				(key_clicked, key_right_mouse_button),
				(eq, "$g_lco_dragging", 1),
				(call_script, "script_lco_cancel_drag_item"),
				(eq, "$g_lco_dragging", 0),
				(call_script, "script_lco_fill_hero_panels"),
				(call_script, "script_lco_fill_player_panels"),
				(assign, "$g_lco_panel_found", 1), # If we cancelled drag, then on this frame we ignore any other effects of right mouse button
				(play_sound, "snd_click"),
			(try_end),
			# When drag-n-drop is active, it must be displayed
			(try_begin),
				(eq, "$g_lco_dragging", 1),
				(mouse_get_position, pos60),
				(position_get_x, reg10, pos60),
				(position_get_y, reg11, pos60),
				(val_add, reg10, 15),
				(val_sub, reg11, 40),
				(position_set_x, pos60, reg10),
				(position_set_y, pos60, reg11),
				(overlay_set_position, "$g_lco_dragging_panel", pos60),
			(try_end),
			# When popup is active, it must be displayed
			(try_begin),
				(eq, "$g_lco_popup_active", 1),
				(mouse_get_position, pos60),
				(position_get_y, reg11, pos60),
				(val_sub, reg11, 90),
				(position_set_y, pos60, reg11),
				# BugFix V1.1. Operation was called with incorrect price multiplier.
				(show_item_details_with_modifier, "$g_lco_popup_item", "$g_lco_popup_modifier", pos60, 100),
			(try_end),

		]),

		(ti_on_presentation_mouse_enter_leave, [

			(store_trigger_param_1, ":overlay_id"),
			(store_trigger_param_2, ":is_mouse_out"),
			(try_begin),
				(eq, ":is_mouse_out", 1),
				(try_begin),
					(eq, "$g_lco_popup_overlay", ":overlay_id"),
					(try_begin),
						(eq, "$g_lco_popup_active", 1),
						(assign, "$g_lco_popup_active", 0),
						(close_item_details),
						(call_script, "script_lco_highlight_items", 0),
					(try_end),
				(try_end),
			(else_try),
				# Is the object one of active panels?
				(call_script, "script_cf_lco_is_active_panel", ":overlay_id"),
				(call_script, "script_lco_get_slot_details_for_panel", ":overlay_id"),
				(try_begin),
					(ge, reg2, 0),
					(assign, "$g_lco_popup_active", 1),
					(assign, "$g_lco_popup_overlay", ":overlay_id"),
					(assign, "$g_lco_popup_item", reg2),
					(assign, "$g_lco_popup_modifier", reg3),
					(call_script, "script_lco_highlight_items", 1, reg2, reg3),
				(else_try),
					(eq, "$g_lco_popup_active", 1),
					(assign, "$g_lco_popup_active", 0),
					(close_item_details),
					(call_script, "script_lco_highlight_items", 0),
				(try_end),
			(try_end),

		]),

	]),


	("companions_overview", 0, mesh.ui_bg_mp_bg,
		[

			(ti_on_presentation_load,
				[

					# PRESENTATION INITIALIZATION

					(call_script, "script_lco_initialize_presentation"),

					(ui_create_mesh, reg0, "mesh_pic_camp", 0, 0, 1000, 1000),

					(ui_create_game_button, "$g_lco_dialog", "str_lco_i_character", 355, 25, 190, 42),

					# GENERATING CONTAINERS HIERARCHY AND MAJOR CONTROLS

					(store_mul, ":viewport_height", "$g_lco_heroes", 25),
					(val_add, ":viewport_height", 2),
					(assign, ":viewport_bottom", 0),
					(try_begin),
						(lt, ":viewport_height", 525),
						(store_sub, ":viewport_bottom", 525, ":viewport_height"),
					(try_end),
					(store_mul, ":top_y", "$g_lco_heroes", 25),
					(val_max, ":top_y", 525),
					(val_sub, ":top_y", 25),

					# GENERATING MAIN CONTAINER

					(ui_create_label, reg0, "str_lco_i_hero_panel_title", 25, 652, 0, 750),
					(ui_create_label, reg0, "str_lco_i_hero_panel_title", 25, 652, 0, 750),

					(ui_create_container, "$g_lco_main_container", 25, 125, 925, 525+2),
					(set_container_overlay, "$g_lco_main_container"),

					# GENERATING HERO NAME PANELS AND ACTIVE HERO PANEL

					(try_for_range, ":index", 0, "$g_lco_heroes"),
						(troop_get_slot, ":troop_id", lco_storage, ":index"),
						(store_add, ":hero_offset", "$g_lco_heroes", ":index"),
						(troop_set_slot, lco_storage, ":hero_offset", ":troop_id"),
						(store_mul, ":y", ":index", 25),
						(store_sub, ":y", ":top_y", ":y"),
						(ui_create_mesh, reg0, "mesh_ui_btn_long_u", 0, ":y", 310, 300),
						(troop_set_slot, lco_storage, ":index", reg0),
					(try_end),

					(store_mul, ":y", "$g_lco_active_hero", 25),
					(store_sub, ":y", ":top_y", ":y"),
					(ui_create_mesh, "$g_lco_active_panel", "mesh_ui_btn_long_d", 0, ":y", 310, 300),

					(val_add, ":top_y", 1),
					(try_for_range, ":index", 0, "$g_lco_heroes"),
						(store_add, ":hero_offset", "$g_lco_heroes", ":index"),
						(troop_get_slot, ":troop_id", lco_storage, ":hero_offset"),
						(store_mul, ":y", ":index", 25),
						(store_sub, ":y", ":top_y", ":y"),
						(call_script, "script_lco_troop_name_to_s40", ":troop_id"),
						(ui_create_label, reg0, "str_lco_s40", 5, ":y", 0, 750),
					(try_end),

					# GENERATING CONTENT CONTAINERS

					(ui_create_container, "$g_lco_attributes_1", 225, ":viewport_bottom", 725, ":viewport_height"),
					(ui_create_container, "$g_lco_attributes_2", 225, ":viewport_bottom", 725, ":viewport_height"),

					# GENERATING HERO STATISTICS - FIRST PAGE

					(set_container_overlay, "$g_lco_attributes_1"),

					(try_for_range, ":index", 0, "$g_lco_heroes"),

						(store_add, ":hero_offset", "$g_lco_heroes", ":index"),
						(troop_get_slot, ":troop_id", lco_storage, ":hero_offset"),
						(store_sub, ":y", "$g_lco_heroes", ":index"),
						(val_sub, ":y", 1),
						(val_mul, ":y", 25),
						(store_add, ":yt", ":y", 1),

						# Generating 1st block panel
						(ui_create_mesh, reg0, "mesh_ui_btn_long_u", 0, ":y", 353, 300),
						(store_character_level, reg40, ":troop_id"),
						(ui_create_label, reg0, "str_lco_reg40", 20, ":yt", tf_center_justify, 750),
						(troop_get_xp, reg40, ":troop_id"),
						(ui_create_label, reg0, "str_lco_reg40", 65, ":yt", tf_center_justify, 750),
						(call_script, "script_lco_xp_to_next_level", ":troop_id"),
						(ui_create_label, reg0, "str_lco_reg40", 125, ":yt", tf_center_justify, 750),
						(store_troop_health, reg40, ":troop_id", 1),
						(store_troop_health, reg42, ":troop_id", 0),
						(store_mul, reg41, reg40, 10000),
						(val_div, reg41, reg42),
						(val_add, reg41, 50),
						(val_div, reg41, 100), # This and the previous line ensures correct rounding
						(ui_create_label, reg0, "str_lco_reg40_41", 180, ":yt", tf_center_justify, 750),
						(try_begin),
							(eq, ":troop_id", "trp_player"),
							(assign, reg40, 100),
						(else_try),
							(call_script, "script_npc_morale", ":troop_id"),
							(assign, reg40, reg0),
						(try_end),
						(ui_create_label, reg0, "str_lco_reg40", 225, ":yt", tf_center_justify, 750),

						# Generating 2nd block panel
						(ui_create_mesh, reg0, "mesh_ui_btn_long_u", 255, ":y", 183, 300),
						(store_attribute_level, reg40, ":troop_id", ca_strength),
						(ui_create_label, reg0, "str_lco_reg40", 275, ":yt", tf_center_justify, 750),
						(store_attribute_level, reg40, ":troop_id", ca_agility),
						(ui_create_label, reg0, "str_lco_reg40", 305, ":yt", tf_center_justify, 750),
						(store_attribute_level, reg40, ":troop_id", ca_intelligence),
						(ui_create_label, reg0, "str_lco_reg40", 335, ":yt", tf_center_justify, 750),
						(store_attribute_level, reg40, ":troop_id", ca_charisma),
						(ui_create_label, reg0, "str_lco_reg40", 365, ":yt", tf_center_justify, 750),

						# Generating 3rd block panel
						(ui_create_mesh, reg0, "mesh_ui_btn_long_u", 390, ":y", 183, 300),
						(store_skill_level, reg40, "skl_ironflesh", ":troop_id"),
						(ui_create_label, reg0, "str_lco_reg40", 410, ":yt", tf_center_justify, 750),
						(store_skill_level, reg40, "skl_power_strike", ":troop_id"),
						(ui_create_label, reg0, "str_lco_reg40", 440, ":yt", tf_center_justify, 750),
						(store_skill_level, reg40, "skl_power_throw", ":troop_id"),
						(ui_create_label, reg0, "str_lco_reg40", 470, ":yt", tf_center_justify, 750),
						(store_skill_level, reg40, "skl_power_draw", ":troop_id"),
						(ui_create_label, reg0, "str_lco_reg40", 500, ":yt", tf_center_justify, 750),

						# Generating 4th block panel
						(ui_create_mesh, reg0, "mesh_ui_btn_long_u", 525, ":y", 268, 300),
						(store_skill_level, reg40, "skl_weapon_master", ":troop_id"),
						(ui_create_label, reg0, "str_lco_reg40", 545, ":yt", tf_center_justify, 750),
						(store_skill_level, reg40, "skl_shield", ":troop_id"),
						(ui_create_label, reg0, "str_lco_reg40", 575, ":yt", tf_center_justify, 750),
						(store_skill_level, reg40, "skl_athletics", ":troop_id"),
						(ui_create_label, reg0, "str_lco_reg40", 605, ":yt", tf_center_justify, 750),
						(store_skill_level, reg40, "skl_riding", ":troop_id"),
						(ui_create_label, reg0, "str_lco_reg40", 635, ":yt", tf_center_justify, 750),
						(store_skill_level, reg40, "skl_horse_archery", ":troop_id"),
						(ui_create_label, reg0, "str_lco_reg40", 665, ":yt", tf_center_justify, 750),
						(store_skill_level, reg40, "skl_looting", ":troop_id"),
						(ui_create_label, reg0, "str_lco_reg40", 695, ":yt", tf_center_justify, 750),

					(try_end),

					# GENERATING HERO STATISTICS - SECOND PAGE

					(set_container_overlay, "$g_lco_attributes_2"),

					(try_for_range, ":index", 0, "$g_lco_heroes"),

						(store_add, ":hero_offset", "$g_lco_heroes", ":index"),
						(troop_get_slot, ":troop_id", lco_storage, ":hero_offset"),
						(store_sub, ":y", "$g_lco_heroes", ":index"),
						(val_mul, ":y", 25),
						(val_sub, ":y", 25),
						(store_add, ":yt", ":y", 1),

						# Generating 5th block panel
						(ui_create_mesh, reg0, "mesh_ui_btn_long_u", 0, ":y", 486, 300),
						(store_skill_level, reg40, "skl_trainer", ":troop_id"),
						(ui_create_label, reg0, "str_lco_reg40", 20, ":yt", tf_center_justify, 750),
						(store_skill_level, reg40, "skl_tracking", ":troop_id"),
						(ui_create_label, reg0, "str_lco_reg40", 50, ":yt", tf_center_justify, 750),
						(store_skill_level, reg40, "skl_tactics", ":troop_id"),
						(ui_create_label, reg0, "str_lco_reg40", 80, ":yt", tf_center_justify, 750),
						(store_skill_level, reg40, "skl_pathfinding", ":troop_id"),
						(ui_create_label, reg0, "str_lco_reg40", 110, ":yt", tf_center_justify, 750),
						(store_skill_level, reg40, "skl_spotting", ":troop_id"),
						(ui_create_label, reg0, "str_lco_reg40", 140, ":yt", tf_center_justify, 750),
						(store_skill_level, reg40, "skl_inventory_management", ":troop_id"),
						(ui_create_label, reg0, "str_lco_reg40", 170, ":yt", tf_center_justify, 750),
						(store_skill_level, reg40, "skl_wound_treatment", ":troop_id"),
						(ui_create_label, reg0, "str_lco_reg40", 200, ":yt", tf_center_justify, 750),
						(store_skill_level, reg40, "skl_surgery", ":troop_id"),
						(ui_create_label, reg0, "str_lco_reg40", 230, ":yt", tf_center_justify, 750),
						(store_skill_level, reg40, "skl_first_aid", ":troop_id"),
						(ui_create_label, reg0, "str_lco_reg40", 260, ":yt", tf_center_justify, 750),
						(store_skill_level, reg40, "skl_engineer", ":troop_id"),
						(ui_create_label, reg0, "str_lco_reg40", 290, ":yt", tf_center_justify, 750),
						(store_skill_level, reg40, "skl_persuasion", ":troop_id"),
						(ui_create_label, reg0, "str_lco_reg40", 320, ":yt", tf_center_justify, 750),

						# Generating 6th block panel
						(ui_create_mesh, reg0, "mesh_ui_btn_long_u", 350, ":y", 141, 300),
						(store_skill_level, reg40, "skl_prisoner_management", ":troop_id"),
						(ui_create_label, reg0, "str_lco_reg40", 370, ":yt", tf_center_justify, 750),
						(store_skill_level, reg40, "skl_leadership", ":troop_id"),
						(ui_create_label, reg0, "str_lco_reg40", 400, ":yt", tf_center_justify, 750),
						(store_skill_level, reg40, "skl_trade", ":troop_id"),
						(ui_create_label, reg0, "str_lco_reg40", 430, ":yt", tf_center_justify, 750),

						# Generating 7th block panel
						(ui_create_mesh, reg0, "mesh_ui_btn_long_u", 455, ":y", 353, 300),
						(store_proficiency_level, reg40, ":troop_id", wpt_one_handed_weapon),
						(ui_create_label, reg0, "str_lco_reg40", 480, ":yt", tf_center_justify, 750),
						(store_proficiency_level, reg40, ":troop_id", wpt_two_handed_weapon),
						(ui_create_label, reg0, "str_lco_reg40", 520, ":yt", tf_center_justify, 750),
						(store_proficiency_level, reg40, ":troop_id", wpt_polearm),
						(ui_create_label, reg0, "str_lco_reg40", 560, ":yt", tf_center_justify, 750),
						(store_proficiency_level, reg40, ":troop_id", wpt_archery),
						(ui_create_label, reg0, "str_lco_reg40", 600, ":yt", tf_center_justify, 750),
						(store_proficiency_level, reg40, ":troop_id", wpt_crossbow),
						(ui_create_label, reg0, "str_lco_reg40", 640, ":yt", tf_center_justify, 750),
						(store_proficiency_level, reg40, ":troop_id", wpt_throwing),
						(ui_create_label, reg0, "str_lco_reg40", 680, ":yt", tf_center_justify, 750),

					(try_end),

					(set_container_overlay, -1),

					# GENERATING TITLES - FIRST PAGE

					(ui_create_container, "$g_lco_titles_1", 250, 655, 730, 95),
					(set_container_overlay, "$g_lco_titles_1"),

					(ui_create_label, reg0, "str_lco_c_level",          20, 10-89, 0, 750, 45), # All Y positions are offset by -89 to compensate for rotation side-effects in Warband
					(ui_create_label, reg0, "str_lco_c_xp",             65, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_lco_c_xp2next_level", 125, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_lco_c_hp",            180, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_lco_c_morale",        225, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_attribute_0",         275, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_attribute_1",         305, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_attribute_2",         335, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_attribute_3",         365, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_skill_36",            410, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_skill_35",            440, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_skill_34",            470, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_skill_33",            500, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_skill_27",            545, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_skill_26",            575, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_skill_25",            605, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_skill_24",            635, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_skill_23",            665, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_skill_22",            695, 10-89, 0, 750, 45),

					(set_container_overlay, -1),

					# GENERATING TITLES - SECOND PAGE

					(ui_create_container, "$g_lco_titles_2", 250, 655, 730, 95),
					(set_container_overlay, "$g_lco_titles_2"),

					(ui_create_label, reg0, "str_skill_17",             20, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_skill_16",             50, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_skill_15",             80, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_skill_14",            110, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_skill_13",            140, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_skill_12",            170, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_skill_11",            200, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_skill_10",            230, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_skill_09",            260, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_skill_08",            290, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_skill_07",            320, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_skill_02",            370, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_skill_01",            400, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_skill_00",            430, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_proficiency_0",       480, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_proficiency_1",       520, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_proficiency_2",       560, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_proficiency_3",       600, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_proficiency_4",       640, 10-89, 0, 750, 45),
					(ui_create_label, reg0, "str_proficiency_5",       680, 10-89, 0, 750, 45),

					(set_container_overlay, -1),

					# APPLYING CURRENT PAGE SETTINGS

					(try_begin),
						(eq, "$g_lco_page", 0),
						(overlay_set_display, "$g_lco_titles_1", 1),
						(overlay_set_display, "$g_lco_attributes_1", 1),
						(overlay_set_display, "$g_lco_titles_2", 0),
						(overlay_set_display, "$g_lco_attributes_2", 0),
					(else_try),
						(overlay_set_display, "$g_lco_titles_1", 0),
						(overlay_set_display, "$g_lco_attributes_1", 0),
						(overlay_set_display, "$g_lco_titles_2", 1),
						(overlay_set_display, "$g_lco_attributes_2", 1),
					(try_end),

				]
			), # End of ti_on_presentation_load

			(ti_on_presentation_event_state_change,
				[
					(store_trigger_param_1, ":overlay_id"),
					(store_trigger_param_2, ":value"),
					(try_begin),
						(eq, ":overlay_id", "$g_lco_return"),
						(call_script, "script_lco_clear_all_items", "$g_lco_garbage_troop"),
						(assign, "$g_lco_garbage_troop", lco_garbage),
						#(jump_to_menu, "mnu_lco_auto_return"),
						(try_begin),
							(gt, "$g_lco_return_to", 0),
							(assign, "$window_manager_action", WM_MENU),
							(assign, "$window_manager_param1", "$g_lco_return_to"),
						(else_try),
							(assign, "$window_manager_action", WM_RETURN),
						(try_end),
						(assign, "$extra_text_preq_display", 0), # Tell NE's script_game_get_item_extra_text to no longer generate item's prerequisite line
						(presentation_set_duration, 0),
					(else_try),
						(eq, ":overlay_id", "$g_lco_dialog"),
						(try_begin),
							(gt, "$g_lco_heroes", 0), # Safety check
							(store_add, ":hero_offset", "$g_lco_heroes", "$g_lco_active_hero"),
							#(troop_get_slot, "$g_lco_target", lco_storage, ":hero_offset"),
							#(assign, "$g_lco_operation", lco_view_character),
							#(jump_to_menu, "mnu_lco_auto_return"),
							(assign, "$window_manager_action", WM_MAP_CONVERSATION),
							(troop_get_slot, "$window_manager_param1", lco_storage, ":hero_offset"),
							(assign, "$window_manager_param2", "prsnt_companions_overview"),
							(assign, "$talk_context", tc_companions_overseer),
							(modify_visitors_at_site, "scn_conversation_scene"),
							(reset_visitors),
							(set_visitor, 0, "trp_player"),
							(set_visitor, 17, "$window_manager_param1"),
							(set_jump_mission, "mt_conversation_encounter"),
							(jump_to_scene, "scn_conversation_scene"),

							(assign, "$extra_text_preq_display", 0), # Tell NE's script_game_get_item_extra_text to no longer generate item's prerequisite line
							(presentation_set_duration, 0),
						(try_end),
					(else_try),
						(eq, ":overlay_id", "$g_lco_inc_0"),
						(assign, "$g_lco_include_companions", ":value"),
						(assign, "$window_manager_action", WM_PRESENTATION),
						(assign, "$window_manager_param1", "prsnt_companions_overview"),
						(assign, "$extra_text_preq_display", 0), # Tell NE's script_game_get_item_extra_text to no longer generate item's prerequisite line
						(presentation_set_duration, 0),
					(else_try),
						(eq, ":overlay_id", "$g_lco_inc_1"),
						(assign, "$g_lco_include_lords", ":value"),
						(assign, "$window_manager_action", WM_PRESENTATION),
						(assign, "$window_manager_param1", "prsnt_companions_overview"),
						(assign, "$extra_text_preq_display", 0), # Tell NE's script_game_get_item_extra_text to no longer generate item's prerequisite line
						(presentation_set_duration, 0),
					(else_try),
						(eq, ":overlay_id", "$g_lco_inc_2"),
						(assign, "$g_lco_include_regulars", ":value"),
						(assign, "$window_manager_action", WM_PRESENTATION),
						(assign, "$window_manager_param1", "prsnt_companions_overview"),
						(assign, "$extra_text_preq_display", 0), # Tell NE's script_game_get_item_extra_text to no longer generate item's prerequisite line
						(presentation_set_duration, 0),
					(else_try),
						(eq, ":overlay_id", "$g_lco_switch_page_0"),
						(neq, "$g_lco_page", 0),
						(assign, "$g_lco_page", 0),
						(position_set_x, pos60, 25),
						(position_set_y, pos60, 685),
						(overlay_set_position, "$g_lco_selected_page", pos60),
						(overlay_set_display, "$g_lco_titles_1", 1),
						(overlay_set_display, "$g_lco_attributes_1", 1),
						(overlay_set_display, "$g_lco_titles_2", 0),
						(overlay_set_display, "$g_lco_attributes_2", 0),
					(else_try),
						(eq, ":overlay_id", "$g_lco_switch_page_1"),
						(neq, "$g_lco_page", 1),
						(assign, "$g_lco_page", 1),
						(position_set_x, pos60, 55),
						(position_set_y, pos60, 685),
						(overlay_set_position, "$g_lco_selected_page", pos60),
						(overlay_set_display, "$g_lco_titles_1", 0),
						(overlay_set_display, "$g_lco_attributes_1", 0),
						(overlay_set_display, "$g_lco_titles_2", 1),
						(overlay_set_display, "$g_lco_attributes_2", 1),
					(else_try),
						(eq, ":overlay_id", "$g_lco_switch_page_2"),
						#(assign, "$g_lco_page", 2),
						(assign, "$window_manager_action", WM_PRESENTATION),
						(assign, "$window_manager_param1", "prsnt_equipment_overview"),
						(assign, "$extra_text_preq_display", 0), # Tell NE's script_game_get_item_extra_text to no longer generate item's prerequisite line
						(presentation_set_duration, 0),
					(try_end),
				]
			), # End of ti_on_presentation_event_state_change

			(ti_on_presentation_run,
				[
					# ESC quits the presentation
					(try_begin),
						(key_clicked, key_escape),
						(call_script, "script_lco_clear_all_items", "$g_lco_garbage_troop"),
						(assign, "$g_lco_garbage_troop", lco_garbage),
						#(jump_to_menu, "mnu_lco_auto_return"),
						(try_begin),
							(gt, "$g_lco_return_to", 0),
							(assign, "$window_manager_action", WM_MENU),
							(assign, "$window_manager_param1", "$g_lco_return_to"),
						(else_try),
							(assign, "$window_manager_action", WM_RETURN),
						(try_end),
						(assign, "$extra_text_preq_display", 0), # Tell NE's script_game_get_item_extra_text to no longer generate item's prerequisite line
						(presentation_set_duration, 0),
					(try_end),
					# TAB switches between two pages of stats
					(try_begin),
						(key_clicked, key_tab),
						(try_begin),
							(this_or_next|key_is_down, key_left_control),
							(key_is_down, key_right_control),
							#(assign, "$g_lco_page", 2),
							(assign, "$window_manager_action", WM_PRESENTATION),
							(assign, "$window_manager_param1", "prsnt_equipment_overview"),
							(assign, "$extra_text_preq_display", 0), # Tell NE's script_game_get_item_extra_text to no longer generate item's prerequisite line
							(presentation_set_duration, 0),
						(else_try),
							(neg|key_is_down, key_left_alt),
							(neg|key_is_down, key_right_alt),
							(val_add, "$g_lco_page", 1),
							(val_mod, "$g_lco_page", 2),
							(try_begin),
								(eq, "$g_lco_page", 0),
								(position_set_x, pos60, 25),
								(position_set_y, pos60, 685),
								(overlay_set_position, "$g_lco_selected_page", pos60),
								(overlay_set_display, "$g_lco_titles_1", 1),
								(overlay_set_display, "$g_lco_attributes_1", 1),
								(overlay_set_display, "$g_lco_titles_2", 0),
								(overlay_set_display, "$g_lco_attributes_2", 0),
							(else_try),
								(position_set_x, pos60, 55),
								(position_set_y, pos60, 685),
								(overlay_set_position, "$g_lco_selected_page", pos60),
								(overlay_set_display, "$g_lco_titles_1", 0),
								(overlay_set_display, "$g_lco_attributes_1", 0),
								(overlay_set_display, "$g_lco_titles_2", 1),
								(overlay_set_display, "$g_lco_attributes_2", 1),
							(try_end),
						(try_end),
					(try_end),
				]
			),

			(ti_on_presentation_mouse_press,
				[
					(store_trigger_param_1, ":overlay_id"),
					(store_trigger_param_2, ":mouse_button"),
					(set_fixed_point_multiplier, 1000),
					(try_begin),
						(eq, ":mouse_button", 0), # Left mouse button

						# Checking if it's one of hero panels
						(try_begin),
							(try_for_range, ":index", 0, "$g_lco_heroes"),
								(troop_slot_eq, lco_storage, ":index", ":overlay_id"),
								(assign, "$g_lco_active_hero", ":index"),
								(set_container_overlay, "$g_lco_main_container"),
								(store_mul, ":y", "$g_lco_active_hero", 25),
								(assign, ":main_height_raw", 525),
								(store_mul, ":top_y", "$g_lco_heroes", 25),
								(val_max, ":top_y", ":main_height_raw"),
								(val_sub, ":top_y", 25),
								(store_sub, ":y", ":top_y", ":y"),
								(position_set_x, pos60, 0),
								(position_set_y, pos60, ":y"),
								(overlay_set_position, "$g_lco_active_panel", pos60),
								(try_begin),
									(this_or_next|key_is_down, key_left_alt),
									(key_is_down, key_right_alt),
									(store_add, ":hero_offset", "$g_lco_heroes", ":index"),
									#(troop_get_slot, "$g_lco_target", lco_storage, ":hero_offset"),
									#(assign, "$g_lco_operation", lco_view_character),
									#(jump_to_menu, "mnu_lco_auto_return"),
									(assign, "$window_manager_action", WM_MAP_CONVERSATION),
									(troop_get_slot, "$window_manager_param1", lco_storage, ":hero_offset"),
									(assign, "$window_manager_param2", "prsnt_companions_overview"),
									(assign, "$talk_context", tc_companions_overseer),
									(modify_visitors_at_site, "scn_conversation_scene"),
									(reset_visitors),
									(set_visitor, 0, "trp_player"),
									(set_visitor, 17, "$window_manager_param1"),
									(set_jump_mission, "mt_conversation_encounter"),
									(jump_to_scene, "scn_conversation_scene"),

									(assign, "$extra_text_preq_display", 0), # Tell NE's script_game_get_item_extra_text to no longer generate item's prerequisite line
									(presentation_set_duration, 0),
								(try_end),
							(try_end),
						(try_end),
					(try_end),
				]
			),

		]
	),

]
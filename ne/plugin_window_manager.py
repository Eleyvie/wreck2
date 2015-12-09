from compiler import *
register_plugin()


export_plugin_globals(
	globals(),
	WM_QUIT                = -1,
	WM_RETURN              =  0,
	WM_MAP                 =  1,
	WM_OPTIONS             =  2,
	WM_CONTROLS            =  3,
	WM_MENU                =  4,
	WM_PRESENTATION        =  5,
	WM_NOTES               =  6,
	WM_LOOT                =  7,
	WM_TRADE               =  8,
	WM_EXCHANGE_MEMBERS    =  9,
	#WM_TRADE_PRISONERS     = 10,
	#WM_BUY_MERCENARIES     = 11,
	#WM_VIEW_CHARACTER      = 12,
	WM_MISSION             = 13,
	WM_MAP_CONVERSATION    = 14,
	WM_EXCHANGE_WITH_PARTY = 15,
	WM_EQUIP_OTHER         = 16,
	WM_GIVE_MEMBERS        = 17,
	WM_TALK_TROOP          = 18,
)

injection = {
	'game_start_globals': [
		(assign, "$window_manager_action", WM_RETURN),
		(assign, "$window_manager_param1", 0),
		(assign, "$window_manager_param2", 0),
	],
}

game_menus = [

	("window_manager", mnf_disable_all_keys, "Window Manager error has occurred! Please let us know how and where.", "none", [
		(try_begin),
			(eq, "$window_manager_action", WM_RETURN),
			(change_screen_return),
		(else_try),
			(eq, "$window_manager_action", WM_MENU),
			(jump_to_menu, "$window_manager_param1"),
		(else_try),
			(eq, "$window_manager_action", WM_PRESENTATION),
			(start_presentation, "$window_manager_param1"),
		(else_try),
			(eq, "$window_manager_action", WM_TALK_TROOP),
			(start_map_conversation, "$window_manager_param1", "$window_manager_param2"),
		(else_try),
			(eq, "$window_manager_action", WM_MAP_CONVERSATION),
			(change_screen_map_conversation, "$window_manager_param1"),
		(else_try),
			(eq, "$window_manager_action", WM_MISSION),
			(change_screen_mission),
		(else_try),
			(eq, "$window_manager_action", WM_MAP),
			(change_screen_map),
		(else_try),
			(eq, "$window_manager_action", WM_LOOT),
			(change_screen_loot, "$window_manager_param1"),
		(else_try),
			(eq, "$window_manager_action", WM_TRADE),
			(change_screen_trade, "$window_manager_param1"),
		(else_try),
			(eq, "$window_manager_action", WM_EQUIP_OTHER),
			(change_screen_equip_other, "$window_manager_param1"),
		(else_try),
			(eq, "$window_manager_action", WM_EXCHANGE_MEMBERS),
			(change_screen_exchange_members, "$window_manager_param2", "$window_manager_param1"),
		(else_try),
			(eq, "$window_manager_action", WM_EXCHANGE_WITH_PARTY),
			(change_screen_exchange_with_party, "$window_manager_param1"),
		(else_try),
			(eq, "$window_manager_action", WM_GIVE_MEMBERS),
			(change_screen_give_members, "$window_manager_param1"),
		(else_try),
			(eq, "$window_manager_action", WM_NOTES),
			(change_screen_notes, "$window_manager_param1", "$window_manager_param2"),
		(else_try),
			(eq, "$window_manager_action", WM_QUIT),
			(change_screen_quit),
		#(else_try),
		#	(eq, "$window_manager_action", WM_TRADE_PRISONERS),
		#	(change_screen_, "$window_manager_param1", "$window_manager_param2"),
		#(else_try),
		#	(eq, "$window_manager_action", WM_BUY_MERCENARIES),
		#	(change_screen_, "$window_manager_param1", "$window_manager_param2"),
		#(else_try),
		#	(eq, "$window_manager_action", WM_VIEW_CHARACTER),
		#	(change_screen_, "$window_manager_param1", "$window_manager_param2"),
		(try_end),
	], [
		("leave", [], "Leave...", [(change_screen_return)]),
	]),

]

def start_window_manager(operation, param1 = 0, param2 = 0, *argl):
	return [
		(assign, "$window_manager_action", operation),
		(assign, "$window_manager_param1", param1),
		(assign, "$window_manager_param2", param1),
		(jump_to_menu, "mnu_window_manager"),
	]

extend_syntax(start_window_manager)

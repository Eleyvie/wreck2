from compiler import *
register_plugin()

simple_triggers = [

	(0, [
		(key_clicked, key_1),
		(map_free),
		(try_for_parties, reg0),
			(str_store_party_name, s0, reg0),
			(display_message, "@Party[{reg0}] = \"{s0}\""),
		(try_end),
	]),

]
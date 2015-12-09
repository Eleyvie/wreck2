from compiler import *
register_plugin()
require_plugin('plugin_data_structures')

slot_item_owned_by = 0 # TODO: Pick a slot
slot_item_rightful_owner = 0 # TODO: pick a slot

scripts = [

    ("initialize_unique_items", [
        (struct_create, g.list_of_artifacts, struct_type_heap),
        (struct_add_items, g.list_of_artifacts, itm.swadian_horse_royal, itm.vaegir_horse_royal, itm.khergit_horse_royal, itm.nordic_horse_royal, itm.rhodok_horse_royal, itm.sarranid_horse_royal, itm.dk_horse_royal, itm.swadian_helm_royal, itm.nordic_helm_royal, itm.sarranid_helm_royal, itm.dk_helm_royal, itm.swadian_boots_royal, itm.vaegir_boots_royal, itm.khergit_boots_royal, itm.nord_boots_royal, itm.larktin_black_greaves, itm.vaegir_gauntlets_royal, itm.khergit_gauntlets_royal, itm.sarranid_gauntlets_royal, itm.larktin_gauntlets, itm.swadian_armor_royal, itm.vaegir_armor_royal, itm.khergit_armor_royal, itm.nordic_armor_royal, itm.rhodok_armor_royal, itm.sarranid_armor_royal, itm.larktin_black_armor, itm.swadian_shield_royal, itm.vaegir_shield_royal, itm.khergit_shield_royal, itm.nord_shield_royal, itm.rhodok_shield_royal, itm.sarranid_shield_royal, itm.dk_shield_royal),
        (struct_iterate_with_callback, g.list_of_artifacts, script.initialize_unique_item),
        (try_for_range, l.troop_id, active_npcs_begin, active_npcs_end),
            (troop_get_inventory_capacity, l.capacity, l.troop_id),
            (try_for_range, l.slot, 0, l.capacity),
                (troop_get_inventory_slot, l.item, l.troop_id, l.slot),
                (ge, l.item, 0),
                (item_slot_eq, l.item, slot_item_owned_by, -1),
                (item_set_slot, l.item, slot_item_owned_by, l.troop_id),
                (item_set_slot, l.item, slot_item_righful_owner, l.troop_id),
            (try_end),
        (try_end),
    ]),

    ("initialize_unique_item", [
        (store_script_param, l.item_id, 1),
        (item_set_slot, l.item_id, slot_item_owned_by, -1), # Item is currently not owned by anyone
    ]),

    ("check_unique_item_init", [
        (store_script_param, l.item_id, 1),
        (try_begin),
            (item_slot_eq, l.item_id, slot_item_owned_by, -1),
            (str_store_item_name, s1, l.item_id),
            (display_message, "@Item `{s1}` is marked as artifact but is not owned by anyone."),
        (try_end),
    ]),

    ("check_unique_item_stolen", [
        (store_script_param, l.item_id, 1),
        (item_get_slot, l.owner_id, l.item_id, slot_item_owned_by),
        (item_get_slot, l.belongs_to, l.item_id, slot_item_rightful_owner),
        (try_begin),
            (neq, l.owner_id, l.belongs_to),
            (store_item_kind_count, l.has_item, l.owner_id, l.item_id),
            (gt, l.has_item, 0), # Actually has item
            # TODO: handle the fact that unique item is in someone else's hands (reduce relation, possibly check for it being sold etc).
        (try_end),
    ]),

]

simple_triggers = [

    (24, [
        (struct_iterate_with_callback, g.list_of_artifacts, script.check_unique_item_stolen),
    ]),
]

injection = {

    'script_game_start': [
        (call_script, script.initialize_unique_items),
    ],

}
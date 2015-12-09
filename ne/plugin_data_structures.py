from compiler import *
register_plugin()

slot_struct_type        = 0
slot_struct_item_count  = 1
slot_struct_block_count = 2
slot_struct_first_block = 3
slot_struct_last_block  = 4
slot_struct_first_free_block = 5

struct_block_size = 32

struct_block_offset_count = 0 # For used blocks, zero element contains # of items inside of it
struct_block_offset_next  = 1 # For used blocks, 1st element contains reference to next used block
struct_block_offset_prev  = 2 # For used blocks, 2nd element contains reference to previous used block
struct_block_offset_data  = 3 # For used blocks, 3rd element and onwards contain actual data

struct_free_block_offset_next = 0 # For free blocks, zero element contains reference to next free block

struct_block_data_size = 32 - struct_block_offset_data # Each block is 3 slots header and 29 slots data

struct_type_heap = 0 # Allow performance optimization by re-ordering elements arbitratily
struct_type_list = 1 # Maintain elements order despite lower performance

# This will make these values accessible to the rest of module system
export_plugin_globals(
    struct_type_set          = struct_type_set,
    struct_type_list         = struct_type_list,
    struct_type_ordered_list = struct_type_ordered_list,
    struct_type_stack        = struct_type_stack,
    struct_type_queue        = struct_type_queue,
)

map_icons = [
    ("data_structure", mcn_no_shadow, "battle_track", 1.0, 0),
]

party_templates = [
    ("data_structure", "{!}", pf_hide_defenders|pf_is_static|pf_no_label|pf_disabled|icon.data_structure, 0, fac.no_faction, 0, []),
]

scripts = [

    ("struct_copy_slot_range", [
        (store_script_param, l.source_struct, 1),
        (store_script_param, l.source_offset, 2),
        (store_script_param, l.target_struct, 3),
        (store_script_param, l.target_offset, 4),
        (store_script_param, l.slot_count, 5),
        (store_script_param, l.backwards, 6),
        (try_begin),
            (eq, l.backwards, 0),
            (assign, l.increment, 1),
        (else_try),
            (val_add, l.source_offset, l.slot_count),
            (val_sub, l.source_offset, 1),
            (val_add, l.target_offset, l.slot_count),
            (val_sub, l.target_offset, 1),
            (assign, l.increment, -1),
        (try_end),
        (try_for_range, l.slot, 0, l.slot_count),
            (party_get_slot, l.slot, l.source_struct, l.source_offset),
            (party_set_slot, l.target_struct, l.target_offset, l.slot),
            (val_add, l.source_offset, l.increment),
            (val_add, l.target_offset, l.increment),
        (try_end),
    ]),

    # script_struct_allocate_block
    # INPUT: <arg1> = data structure reference, <arg2> = offset of block to insert in front of (0 to add as the last)
    # OUTPUT: reg0 = slot offset of new data block
    ("struct_allocate_block", [
        (store_script_param, l.struct, 1),
        (store_script_param, l.next_block_offset, 2),
        (try_begin),
            (party_slot_eq, l.struct, slot_struct_first_free_block, 0), # There's no allocated but free block
            (party_get_slot, l.new_offset, l.struct, slot_struct_block_count),
            (val_add, l.new_offset, 1),
            (party_set_slot, l.struct, slot_struct_first_free_block, l.new_offset), # Increase counter of allocated blocks by 1
            (val_mul, l.new_offset, struct_block_size), # Get offset for our new block
        (else_try),
            (party_get_slot, l.new_offset, l.struct, slot_struct_first_free_block), # We use first free block
            (party_get_slot, l.next_free_offset, l.struct, l.new_offset), # This is offset of next free block
            (party_set_slot, l.struct, slot_struct_first_free_block, l.next_free_offset),
        (try_end),
        # l.new_offset contains the offset of newly allocated block.
        (assign, reg0, l.new_offset), # This is the value we'll return
        (party_set_slot, l.struct, l.new_offset, 0), # No items in this block ATM
        # Calculate offsets of previous and next blocks
        (try_begin),
            (eq, l.next_block_offset, 0), # We are to add the block at the end
            (party_get_slot, l.prev_block_offset, l.struct, slot_struct_last_block),
        (else_try),
            (store_add, l.prev_block_offset, l.next_block_offset, struct_block_offset_prev),
            (party_get_slot, l.prev_block_offset, l.struct, l.prev_block_offset),
        (try_end),
        # Connect previous block with current one
        (try_begin),
            (eq, l.prev_block_offset, 0), # There is no previous block, so ours will be the first now
            (party_set_slot, l.struct, slot_struct_first_block, l.new_offset),
        (else_try),
            (store_add, l.offset, l.prev_block_offset, struct_block_offset_next),
            (party_set_slot, l.struct, l.offset, l.new_offset), # Link previous block to current one
        (try_end),
        (store_add, l.offset, l.new_offset, struct_block_offset_prev),
        (party_set_slot, l.struct, l.offset, l.prev_block_offset), # Link current block to previous
        # Connect next block with current one
        (try_begin),
            (eq, l.next_block_offset, 0), # There is no next block, so ours will be the last now
            (party_set_slot, l.struct, slot_struct_last_block, l.new_offset),
        (else_try),
            (store_add, l.offset, l.next_block_offset, struct_block_offset_prev),
            (party_set_slot, l.struct, l.offset, l.new_offset), # Link next block to current one
        (try_end),
        (store_add, l.offset, l.new_offset, struct_block_offset_next),
        (party_set_slot, l.struct, l.offset, l.next_block_offset), # Link current block to next
    ]),

    # script_struct_free_block
    # INPUT: <arg1> = data structure reference, <arg2> = offset of block to free
    # OUTPUT: none
    ("struct_free_block", [
        (store_script_param, l.struct, 1),
        (store_script_param, l.block_offset, 2),
        # First, extract block from the list
        (store_add, l.offset_next, l.block_offset, struct_block_offset_next),
        (store_add, l.offset_prev, l.block_offset, struct_block_offset_prev),
        (party_get_slot, l.next_block, l.struct, l.offset_next),
        (party_get_slot, l.prev_block, l.struct, l.offset_prev),
        # Deal with removed block and next one
        (try_begin),
            (eq, l.next_block, 0),
            # No next block means this is the last one, so we only overwrite root last block reference
            (party_set_slot, l.struct, slot_struct_last_block, l.prev_block), # Block that was previous to removed one becomes the last
        (else_try),
            # There's a next block, so we rewrite it's prev_block reference
            (store_add, l.offset, l.next_block, struct_block_offset_prev),
            (party_set_slot, l.struct, l.offset, l.prev_block),
        (try_end),
        # Deal with removed block and previous one
        (try_begin),
            (eq, l.prev_block, 0),
            # No previous block means this is the first one, so we only overwrite root first block reference
            (party_set_slot, l.struct, slot_struct_first_block, l.next_block), # Block that was next to removed one becomes the first
        (else_try),
            # There's a previous block, so we rewrite it's next_block reference
            (store_add, l.offset, l.prev_block, struct_block_offset_next),
            (party_set_slot, l.struct, l.offset, l.next_block),
        (try_end),
        # Insert block as the first free one.
        (try_begin),
            (party_slot_eq, l.struct, slot_struct_first_free_block, 0),
            # There are no free blocks ATM, so this is the only one
            (party_set_slot, l.struct, l.block_offset, 0), # There are no other free blocks after this one
        (else_try),
            # There's at least one free blocks, so we insert our block before them
            (party_get_slot, l.was_first_free_block, l.struct, slot_struct_first_free_block),
            (party_set_slot, l.struct, l.block_offset, l.was_first_free_block), # Connect to next free block
        (try_end),
        # Write down our block as the first free block
        (party_set_slot, l.struct, slot_struct_first_free_block, l.block_offset), # Our block becomes the first free block
    ]),

    # script_struct_find_offset_by_index
    # INPUT: <arg1> = data structure reference, <arg2> = item index to find
    # OUTPUT: reg0 = physical slot offset of the item in question
    ("struct_find_offset_by_index", [
        (store_script_param, l.struct, 1),
        (store_script_param, l.index, 2),
        (party_get_slot, l.current_block, l.struct, slot_struct_first_block),
        (party_get_slot, l.total_blocks, l.struct, slot_struct_block_count),
        (assign, l.remaining, l.index),
        (assignm l.found, -1),
        (try_for_range, reg0, 0, l.total_blocks),
            (party_slot_ge, l.struct, l.current_block, l.remaining),
            # Index is not in current block
            (party_get_slot, l.reduce_remaining, l.struct, l.current_block),
            (val_sub, l.remaining, l.reduce_remaining),
            (val_add, l.current_block, struct_block_offset_next),
            (party_get_slot, l.current_block, l.struct, l.current_block), # Proceed to next block
        (else_try),
            (store_add, l.found, l.current_block, struct_block_offset_data),
            (val_add, l.found, l.remaining),
            (assign, l.total_blocks, 0), # Terminate search
        (try_end),
        (assign, reg0, l.found),
    ]),

    # script_struct_add_item
    # INPUT: none
    # OUTPUT: none
    ("struct_add_item", [
        (store_script_param, l.struct, 1),
        (store_script_param, l.value, 2),
        (party_get_slot, l.total_items_count, l.struct, slot_struct_item_count),
        (try_begin),
            (party_slot_ge, l.struct, slot_struct_last_block, 1), # Structure has last data block allocated
            (party_get_slot, l.current_block, l.struct, slot_struct_last_block),
            (neg|party_slot_ge, l.struct, l.current_block, struct_block_data_size), # Last block has free space
        (else_try),
            (assign, l.cached, reg0),
            (call_script, script.struct_allocate_block, l.struct, 0),
            (assign, l.current_block, reg0),
            (assign, reg0, l.cached),
        (try_end),
        # Now add item
        (party_get_slot, l.block_items_count, l.struct, l.current_block),
        (store_add, l.item_offset, l.block_items_count, struct_block_offset_data), # Offset within the block
        (val_add, l.item_offset, l.current_block), # Offset within the entire struct
        (party_set_slot, l.struct, l.item_offset, l.value),
        # Increase total number of items in current block and entire data structure
        (val_add, l.block_items_count, 1),
        (party_set_slot, l.struct, l.current_block, l.block_items_count),
        (val_add, l.total_items_count, 1),
        (party_set_slot, l.struct, slot_struct_item_count, l.total_items_count),
    ]),

    # script_insert_item
    # INPUT: none
    # OUTPUT: none
    ("struct_insert_item", [
        (store_script_param, l.struct, 1),
        (store_script_param, l.value, 2),
        (store_script_param, l.index, 3),
        (assign, l.cached, reg0),

        (call_script, script.struct_find_offset_by_index, l.struct, l.index),
        (assign, l.insert_offset, reg0),
        (store_div, l.current_block, l.insert_offset, struct_block_size),
        (val_mul, l.current_block, struct_block_size),
        (try_begin),
            (neg|party_slot_ge, l.struct, l.current_block, struct_block_data_size), # Current block has free space
            # We insert new value within the current block (as there's free space to expand)
            (party_get_slot, l.block_items_count, l.struct, l.current_block),
            (store_add, l.block_items_end, l.current_block, struct_block_offset_data),
            (val_add, l.block_items_end, l.block_items_count),
            (try_for_range_backwards, l.slot, l.insert_offset, l.block_items_end),
                (party_get_slot, l.shifted_value, l.struct, l.slot),
                (val_add, l.slot, 1),
                (party_set_slot, l.struct, l.slot, l.shifted_value),
            (try_end),
            (party_set_slot, l.struct, l.insert_offset, l.value),
            (val_add, l.block_items_count, 1),
            (party_set_slot, l.struct, l.current_block, l.block_items_count),
        (else_try),
            # Check that next block has at least 1 free space to migrate items to
            (store_add, l.next_block_offset, l.current_block, struct_block_offset_next),
            (party_slot_ge, l.struct, l.next_block_offset, 1), # There's a next block
            (party_get_slot, l.next_block_offset, l.struct, l.next_block_offset),
            (neg|party_slot_ge, l.struct, l.next_block_offset, struct_block_data_size), # Next block has some free space
            # Calculate how many values to spill from current block to next
            (party_get_slot, l.next_block_size, l.struct, l.next_block_offset), # Number of items in next block
            (store_sub, l.spill_size, struct_block_data_size + 1, l.next_block_size),
            (val_rshift, l.spill_size, 1), # This is how many items we move from current block to next by default
            # Restrict spill size to prevent our selected index being moved to next block
            (store_add, l.limit_spill_size, l.current_block, struct_block_size),
            (val_sub, l.limit_spill_size, l.insert_offset),
            (val_min, l.spill_size, l.limit_spill_size),
            # Move existing values in the next block to the right to free up the space from spilling values
            (store_add, l.offset, l.next_block_offset, struct_block_offset_data), # Start of next block data range
            (store_add, l.shift_offset, l.offset, l.spill_size), # This is where we move those values
            (call_script, script.struct_copy_slot_range, l.struct, l.offset, l.struct, l.shift_offset, l.spill_size, 1), # Shift all current values to the right
            # Spill values from current block to the beginning of the next one
            (store_add, l.shift_offset, l.current_block, struct_block_size),
            (val_sub, l.shift_offset, l.spill_size),
            (call_script, script.struct_copy_slot_range, l.struct, l.shift_offset, l.struct, l.offset, l.spill_size, 0), # Shift values from current block to the next
            # Update number of items in the next block
            (val_add, l.next_block_size, l.spill_size),
            (party_set_slot, l.struct, l.next_block_offset, l.next_block_size),
            # Shift values in the current block to free the slot for inserted value, and insert the value in current block
            (try_for_range_backwards, l.offset, l.insert_offset, l.shift_offset),
                (party_get_slot, l.slot, l.struct, l.offset),
                (val_add, l.offset, 1),
                (party_set_slot, l.struct, l.offset, l.slot),
            (try_end),
            (party_set_slot, l.struct, l.insert_offset, l.value),
            # Update current block items count
            (store_sub, l.block_items_count, struct_block_data_size + 1, l.spill_size),
            (party_set_slot, l.struct, l.current_block, l.block_items_count),
        (else_try),
            # We insert new value by splitting the current block into two
            (store_add, l.next_block_offset, l.current_block, struct_block_offset_next),
            (party_get_slot, l.next_block_offset, l.struct, l.next_block_offset),
            (call_script, script.struct_allocate_block, l.struct, l.next_block_offset), # Insert a new data block before next one
            (assign, l.next_block_offset, reg0),
            # Move all elements starting from insert position to the newly created block
            (store_add, l.spill_size, l.current_block, struct_block_size),
            (val_sub, l.spill_size, l.insert_offset), # This is how may elements we move
            (store_add, l.shift_offset, l.next_block_offset, struct_block_offset_data),
            (call_script, script.struct_copy_slot_range, l.struct, l.insert_offset, l.struct, l.shift_offset, l.spill_size, 0), # Shift values from current block to the next
            # Insert value and update item counts for both blocks
            (party_set_slot, l.struct, l.insert_offset, l.value),
            (party_set_slot, l.struct, l.next_block_offset, l.spill_size),
            (store_sub, l.block_items_count, struct_block_data_size + 1, l.spill_size),
            (party_set_slot, l.struct, l.current_block, l.block_items_count),
        (try_end),
        # Update total items count for data structure
        (party_get_slot, l.total_items_count, l.struct, slot_struct_item_count),
        (val_add, l.total_items_count, 1),
        (party_set_slot, l.struct, slot_struct_item_count, l.total_items_count),
        # Restore reg0 cached value
        (assign, reg0, l.cached),
    ]),

    # script_struct_remove_item_by_index
    # INPUT: none
    # OUTPUT: none
    ("struct_remove_item_by_index", [
        #(store_script_param, l.struct, 1),
        #(store_script_param, l.index, 2),
    ]),

    # script_
    # INPUT: none
    # OUTPUT: none
    ("struct_find_offset_by_value", [
        #(store_script_param, l.struct, 1),
        #(store_script_param, l.value, 2),
        #(store_script_param, l.current_block, 3), # Block from which to start looking
        #(store_script_param, l.current_offset, 4), # Offset from which to start looking
    ]),

]

def struct_create(destination, struct_type = struct_type_heap):
    if destination == reg0:
        return [
            (spawn_around_party, p.temp_party, pt.data_structure),
            (party_set_slot, reg0, slot_party_struct_type, struct_type),
        ]
    else:
        return [
            (assign, l._cached_, reg0),
            (spawn_around_party, p.temp_party, pt.data_structure),
            (party_set_slot, reg0, slot_party_struct_type, struct_type),
            (assign, destination, reg0),
            (assign, reg0, l._cached_),
        ]

def struct_destroy(struct):
    return [
        (remove_party, struct),
    ]

def struct_set_name(struct, new_name):
    return [
        (party_set_name, struct, new_name),
    ]

def str_store_struct_name(destination, struct):
    return [
        (str_store_party_name, destination, struct),
    ]

def struct_clear(struct):
    return [
        (party_set_slot, struct, slot_struct_item_count, 0),
        (party_set_slot, struct, slot_struct_block_count, 0),
        (party_set_slot, struct, slot_struct_first_block, 0),
        (party_set_slot, struct, slot_struct_last_block, 0),
        (party_set_slot, struct, slot_struct_first_free_block, 0),
    ]

def struct_get_item_count(destination, struct):
    return [
        (party_get_slot, destination, struct, slot_struct_item_count),
    ]

def struct_is_empty(struct):
    return [
        (party_slot_eq, struct, slot_struct_item_count, 0),
    ]

def struct_has_items(struct):
    return [
        (neg|party_slot_eq, struct, slot_struct_item_count, 0),
    ]

def struct_item_count_eq(struct, value):
    return [
        (party_slot_eq, struct, slot_struct_item_count, value),
    ]

def struct_item_count_neq(struct, value):
    return [
        (neg|party_slot_eq, struct, slot_struct_item_count, value),
    ]

def struct_item_count_ge(struct, value):
    return [
        (party_slot_ge, struct, slot_struct_item_count, value),
    ]

def struct_item_count_lt(struct, value):
    return [
        (neg|party_slot_ge, struct, slot_struct_item_count, value),
    ]

def struct_has_value(struct, value):
    return [
        (call_script, script.cf_struct_contains_value, struct, value, 1),
    ]

def struct_lacks_value(struct, value):
    return [
        (call_script, script.cf_struct_contains_value, struct, value, 0),
    ]

def struct_add_item(struct, value, index = -1):
    if index < 0:
        return [
            (call_script, script.struct_add_item, struct, value),
        ]
    else:
        return [
            (try_begin),
                (party_get_slot, l._cached_, struct, slot_struct_item_count),
                (lt, index, l._cached_),
                (call_script, script.struct_insert_item, struct, value, index),
            (else_try),
                (call_script, script.struct_add_item, struct, value),
            (try_end),
        ]

#(struct_add_items, <struct>, <value1>, [<value2>...])      - add any number of new elements at the tail of data structure

def struct_get_item(destination, struct, index = -1): # CAN_FAIL
    if index < 0:
        return [
            (party_get_slot, destination, struct, slot_struct_last_block),
            (gt, destination, 0), # There's a last block
            (party_get_slot, l._cached_, struct, destination), # Number of items in last block
            (val_add, destination, struct_block_offset_data - 1),
            (val_add, destination, l._cached_),
            (party_get_slot, destination, struct, destination), # Retrieve last element
        ]
    else:
        return [
            (assign, l._cached_, reg0),
            (call_script, script.struct_find_offset_by_index, struct, index),
            (assign, destination, reg0),
            (assign, reg0, l._cached_),
            (gt, destination, 0), # Offset found
            (party_get_slot, destination, struct, destination),
        ]

def struct_get_random_item(destination, struct): # CAN_FAIL
    return [
        (party_get_slot, destination, struct, slot_struct_item_count),
        (gt, destination, 0), # structure has elements
        (store_random_in_range, destination, 0, destination),
        (assign, l._cached_, reg0),
        (call_script, script.struct_find_offset_by_index, struct, destination),
        (party_get_slot, destination, struct, reg0),
        (assign, reg0, l._cached_),
    ]

def struct_get_two_random_items(dest1, dest2, struct): # CAN_FAIL
    return [
        (party_get_slot, dest2, struct, slot_struct_item_count),
        (gt, dest2, 1), # structure has at least two elements
        (store_random_in_range, dest1, 0, dest2),
        (val_sub, dest2, 1),
        (store_random_in_range, dest2, 0, dest2),
        (try_begin),
            (ge, dest2, dest1),
            (val_add, dest2, 1),
        (try_end),
        (assign, l._cached_, reg0),
        (call_script, script.struct_find_offset_by_index, struct, dest1),
        (party_get_slot, dest1, struct, reg0),
        (call_script, script.struct_find_offset_by_index, struct, dest2),
        (party_get_slot, dest2, struct, reg0),
        (assign, reg0, l._cached_),
    ]

    #(struct_pop_item, <destination>, <struct>, [<index>]),     - same, but also removes item from the data structure
    #(struct_pop_random_item, <destination>, <struct>),         - retrieves a single randomly chosen item and removes it from the data structure

    #(struct_iterate_with_callback, <struct>, <callback>, [<param>...]), - iterate through all items, calling the provided callback script for each of them
    #(struct_filter_with_callback, <struct>, <cf_callback>),    - iterate through all items, removing all that will fail the provided callback script

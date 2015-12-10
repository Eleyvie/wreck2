#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""wreck.core

File created by lav on 19.11.15 at 15:58.
Email: alex@lomskih.net
"""

__version__ = "$Revision$"
# $Source$

# region Import Statements
from traceback import format_exc as formatted_exception, extract_tb as extract_traceback
from inspect import currentframe as inspect_currentframe, getmembers as inspect_getmembers
import inspect
import os
import sys
import imp
import re
import time
from collections import OrderedDict
try: import colorama
except ImportError: pass
# endregion

# region Compiler Standard Constants
#   +------------------------------------------------------------------------+
#  /                                                                          \
# +                                                                            +
# |    COMPILER STANDARD CONSTANTS                                             |
# |                                                                            |


_python_import = None


EVERYTHING = 9
DEBUG    = 8 # Technical message about compiler's internal proceedings.
DETAILS  = 7 # Informational message about minor events during compilation. Everything is ok.
INFO     = 6 # General informational message. Everything is ok.
ADVICE   = 5 # Not an error, but WRECK still advises to change something to improve readability, portability etc.
WARNING  = 4 # Not necessarily an error, but has the potential to become such.
MISTAKE  = 3 # Most likely an error unless it's some trickery that WRECK cannot recognize. Module is still compilable.
ERROR    = 2 # An error that makes it impossible to compile the module, but doesn't stop the compilation.
FAILURE  = 1 # An error that prevents the compilation from completing.
CRITICAL = 0 # An error within WRECK code.
NOTHING = -1

DEBUG_MODE = True

bignum = 0x40000000000000000000000000000000

op_num_value_bits = 24 + 32

tag_register        =  1
tag_variable        =  2
tag_string          =  3
tag_item            =  4
tag_troop           =  5
tag_faction         =  6
tag_quest           =  7
tag_party_tpl       =  8
tag_party           =  9
tag_scene           = 10
tag_mission_tpl     = 11
tag_menu            = 12
tag_script          = 13
tag_particle_sys    = 14
tag_scene_prop      = 15
tag_sound           = 16
tag_local_variable  = 17
tag_map_icon        = 18
tag_skill           = 19
tag_mesh            = 20
tag_presentation    = 21
tag_quick_string    = 22
tag_track           = 23
tag_tableau         = 24
tag_animation       = 25
tags_end            = 26

opmask_register       = tag_register       << op_num_value_bits
opmask_variable       = tag_variable       << op_num_value_bits
opmask_local_variable = tag_local_variable << op_num_value_bits
opmask_quick_string   = tag_quick_string   << op_num_value_bits
opmask_string         = tag_string         << op_num_value_bits

# assign     = 2133
# store_add  = 2120
# store_sub  = 2121
# store_mul  = 2122
# store_div  = 2123
# store_mod  = 2119
# store_pow  = 2126
# store_and  = 2117
# store_or   = 2116
# val_abs    = 2113
# val_lshift = 2100
# val_rshift = 2101
# val_add    = 2105 # Used in binary xor
# val_mul    = 2107 # Used in binary xor

DEFAULT_ITEM_MODIFIERS = [
    ("plain",       "Plain %s",         1.000000, 1.000000), # Default. No effects. Item name is not modified.
    ("cracked",     "Cracked %s",       0.500000, 1.000000), # -5 damage, -4 armor, -46 hp
    ("rusty",       "Rusty %s",         0.550000, 1.000000), # -3 damage, -3 armor
    ("bent",        "Bent %s",          0.650000, 1.000000), # -3 damage,                   -3 speed
    ("chipped",     "Chipped %s",       0.720000, 1.000000), # -1 damage
    ("battered",    "Battered %s",      0.750000, 1.000000), #            -2 armor, -26 hp
    ("poor",        "Poor %s",          0.800000, 1.000000), # No effects.
    ("crude",       "Crude %s",         0.830000, 1.000000), # -2 damage, -1 armor
    ("old",         "Old %s",           0.860000, 1.000000), # No effects.
    ("cheap",       "Cheap %s",         0.900000, 1.000000), # No effects.
    ("fine",        "Fine %s",          1.900000, 0.600000), # +1 damage
    ("well_made",   "Well_Made %s",     2.500000, 0.500000), # No effects.
    ("sharp",       "Sharp %s",         1.600000, 0.600000), # No effects.
    ("balanced",    "Balanced %s",      3.500000, 0.500000), # +3 damage,                   +3 speed
    ("tempered",    "Tempered %s",      6.700000, 0.400000), # +4 damage
    ("deadly",      "Deadly %s",        8.500000, 0.300000), # No effects.
    ("exquisite",   "Exquisite %s",    14.500000, 0.300000), # No effects.
    ("masterwork",  "Masterwork %s",   17.500000, 0.300000), # +5 damage,                   +1 speed, +4 prerequisite
    ("heavy",       "Heavy %s",         1.900000, 0.700000), # +2 damage, +3 armor, +10 hp, -2 speed, +1 prerequisite, +4 horse charge
    ("strong",      "Strong %s",        4.900000, 0.400000), # +3 damage,                   -3 speed, +2 preresuisite
    ("powerful",    "Powerful %s",      3.200000, 0.400000), # No effects.
    ("tattered",    "Tattered %s",      0.500000, 1.000000), #            -3 armor
    ("ragged",      "Ragged %s",        0.700000, 1.000000), #            -2 armor
    ("rough",       "Rough %s",         0.600000, 1.000000), # No effects.
    ("sturdy",      "Sturdy %s",        1.700000, 0.500000), #            +1 armor
    ("thick",       "Thick %s",         2.600000, 0.350000), #            +2 armor, +47 hp
    ("hardened",    "Hardened %s",      3.900000, 0.300000), #            +3 armor
    ("reinforced",  "Reinforced %s",    6.500000, 0.250000), #            +4 armor, +83 hp
    ("superb",      "Superb %s",        2.500000, 0.250000), # No effects.
    ("lordly",      "Lordly %s",       11.500000, 0.250000), #            +6 armor, +155 hp
    ("lame",        "Lame %s",          0.400000, 1.000000), # -5 horse maneuver, -10 horse speed
    ("swaybacked",  "Swaybacked %s",    0.600000, 1.000000), # -2 horse maneuver, -4 horse speed
    ("stubborn",    "Stubborn %s",      0.900000, 1.000000), #                       +5 hp,           +1 prerequisite
    ("timid",       "Timid %s",         1.800000, 1.000000), #                                        -1 prerequisite
    ("meek",        "Meek %s",          1.800000, 1.000000), # No effects.
    ("spirited",    "Spirited %s",      6.500000, 0.600000), # +1 horse maneuver, +2 horse speed, +1 horse charge, +1 prerequisite
    ("champion",    "Champion %s",     14.500000, 0.200000), # +2 horse maneuver, +4 horse speed, +2 horse charge, +2 prerequisite
    ("fresh",       "Fresh %s",         1.000000, 1.000000), # No effects. Commonly used to track perishable foods.
    ("day_old",     "Day-old %s",       1.000000, 1.000000), # No effects. Commonly used to track perishable foods.
    ("two_day_old", "Two Days-old %s",  0.900000, 1.000000), # No effects. Commonly used to track perishable foods.
    ("smelling",    "Smelling %s",      0.400000, 1.000000), # No effects. Commonly used to track perishable foods.
    ("rotten",      "Rotten %s",        0.050000, 1.000000), # No effects. Commonly used to track perishable foods.
    ("large_bag",   "Large Bag of %s",  1.900000, 0.300000), # Increased item amount, repeated shot for crossbows.
]


WRECK_SYNTAX_HELP_TEXT = """
Warband Refined & Enhanced Compiler Kit (W.R.E.C.K.) v.{version}

Usage:
    python {file} help         show this help message and exit
    python {file} [OPTIONS]    compile Warband module

Available options:
    test         Compile module but don\'t create output files (do a test run)
    bw           Do not use colored output (useful when logging)
    tag          Use all entity tags (imitate vanilla compiler behavior)
    wait         Prompt user to press Enter at the end of compilation
    nodupe       Suppress warnings about duplicate entries in module files
    silent       Do not report any compilation messages
    error(s)     Only report compilation errors, suppress warnings and notices
    warning(s)   Report compilation errors and warnings, suppress notices
    notice(s)    Report all compilation messages
    warband      Force WRECK to compile your module as a Warband module
    mnb          Force WRECK to compile your module as a Mount&Blade module
    auto         WRECK will auto-detect module version (default value)

Override options (if present, will override settings in module_info.py):
    performance=y/n    Will turn on/off WRECK performance reporting
    module=PATH        Override path where WRECK will look for module files
    export=PATH        Override path where WRECK will export compiled module

Options character case and ordering in command line doesn't matter. Options can
be prepended by dashes and slashes, i.e. `--help` is fully equivalent to `help`.
For paths that include spaces, put those paths in double quotes, for example:

    python {file} export="C:/My Games/Warband/Modules/My Super Module/"
"""


# |                                                                            |
# |    COMPILER STANDARD CONSTANTS END                                         |
# +                                                                            +
#  \                                                                          /
#   +------------------------------------------------------------------------+
# endregion

# region Compiler Data Wrappers
#   +------------------------------------------------------------------------+
#  /                                                                          \
# +                                                                            +
# |    COMPILER DATA WRAPPERS                                                  |
# |                                                                            |


def _get_current_stack():
    return map(lambda i: (i[1], i[2], i[3], i[4][0]), inspect.stack())[1:]

# Generic class which is used to quietly replace some pipe-joined lists in the game (particularly, item property list and troop attribute/skill/proficiency lists)
class WreckAggregateValue(dict):
    """A wrapper class for some combined values in Warband modules.

    This class is used to handle various pipe-connected parameter lists in Warband module files, like item properties
    and troop attribute/skill/proficiencies. Vanilla Warband compile combines those parameters into a single value with
    binary OR operation (pipe, "|"). WRECK uses a different approach, keeping the individual values as keys to an
    aggregate dictionary, making it easier to interact with those values, but also preventing various value overflow
    issues.
    """

    def __or__(self, other):
        if not other: return self
        result = WreckAggregateValue(self)
        for key, value in other.iteritems():
            if type(value) == float: result[key] = max(result.get(key, 0.0), value)
            else: result[key] = result.get(key, 0) | value
        #result.update(other)
        return result

    __ror__ = __radd__ = __add__ = __or__


# |                                                                            |
# |    COMPILER DATA WRAPPERS END                                              |
# +                                                                            +
#  \                                                                          /
#   +------------------------------------------------------------------------+
# endregion

# region Compiler Helper Functions
#   +------------------------------------------------------------------------+
#  /                                                                          \
# +                                                                            +
# |    COMPILER HELPER FUNCTIONS                                               |
# |                                                                            |


def parse_int(value):
    """Converts a single value to integer, or tuple/list of values to list of integers recursively."""
    if isinstance(value, list) or isinstance(value, tuple): return map(parse_int, value) # Recursion
    if isinstance(value, WreckVariable) and value.is_static and (value.module is not None) and value.module['opmask']:
        return int(value) & 0xffffffff # Disable opmask if present, otherwise leave value as it is
    return int(value)

external_string = lambda value: value.replace(' ', '_').replace('\t', '_')
external_identifier = lambda name: name.replace(" ","_").replace("'","_").replace("`","_").replace("(","_").replace(")","_").replace("-","_").replace(",","").replace("|","").replace("\t","_")
internal_identifier = lambda name: external_identifier(name).replace('=','_').lower()

_detect_missing_var_name = re.compile("^[^']+'(\w+)'")
_detect_file_encoding = re.compile('^#(.*coding\s*[:=]\s*([\w\d\-]+)(?:[^\w\d\-].*|$))', re.MULTILINE)

def unparse_item_aggregate(value):
    """WreckAggregateValue helper function.

    Converts binary-packed item parameters into WRECK aggregate.
    """
    if isinstance(value, WreckAggregateValue): return value
    return WreckAggregateValue({
        'weight': get_weight(value),
        'head': get_head_armor(value),
        'body': get_body_armor(value),
        'leg': get_leg_armor(value),
        'diff': get_difficulty(value),
        'hp': get_hit_points(value) & 0x3ff, # patch for Native compiler glitch
        'speed': get_speed_rating(value),
        'msspd': get_missile_speed(value),
        'size': get_weapon_length(value),
        'qty': get_max_ammo(value),
        'swing': get_swing_damage(value),
        'thrust': get_thrust_damage(value),
        'abundance': get_abundance(value),
    })

def unparse_attr_aggregate(value):
    """WreckAggregateValue helper function.

    Converts binary-packed troop attributes into WRECK aggregate.
    """
    if isinstance(value, WreckAggregateValue): return value
    return WreckAggregateValue({
        'str': value & 0xFF,
        'agi': (value >> 8) & 0xFF,
        'int': (value >> 16) & 0xFF,
        'cha': (value >> 24) & 0xFF,
        'level': (value >> 32) & 0xFF
    })

def unparse_wp_aggregate(value):
    """WreckAggregateValue helper function.

    Converts binary-packed troop weapon proficiencies into WRECK aggregate.
    """
    if isinstance(value, WreckAggregateValue): return value
    return WreckAggregateValue([(i, (value >> (10*i)) & 0x3FF) for i in xrange(WRECK.num_weapon_proficiencies)])

def unparse_terrain_aggregate(value):
    """WreckAggregateValue helper function.

    Converts scene terrain code into WRECK aggregate.
    """
    value = str(value).lower()
    if value[0:2] == '0x':
        value = value[2:]
        return WreckAggregateValue({
            'terrain_seed': int('0x0%s' % value[-4:], 16),
            'river_seed': int('0x0%s' % value[-12:-8], 16),
            'flora_seed': int('0x0%s' % value[-20:-16], 16),
            'size_x': int('0x0%s' % value[-29:-24], 16) & 0x3ff,
            'size_y': (int('0x0%s' % value[-29:-24], 16) >> 10) & 0x3ff,
            'valley': (int('0x0%s' % value[-39:-32], 16) >> 0) & 0x7f,
            'hill_height': (int('0x0%s' % value[-39:-32], 16) >> 7) & 0x7f,
            'ruggedness': (int('0x0%s' % value[-39:-32], 16) >> 14) & 0x7f,
            'vegetation': (int('0x0%s' % value[-39:-32], 16) >> 21) & 0x7f,
            'terrain': int('0x0%s' % value[-40:-39], 16),
            'polygon_size': (int('0x0%s' % value[-41:-40], 16) & 0x3) + 2,
            'disable_grass': (int('0x0%s' % value[-41:-40], 16) >> 2) & 0x1,
            'shade_occlude': (int('0x0%s' % value[-32:-31], 16) >> 2) & 0x1,
            'place_river': (int('0x0%s' % value[-32:-31], 16) >> 3) & 0x1,
            'deep_water': (int('0x0%s' % value[-16:-15], 16) >> 3) & 0x1,
        })
    else:
        value = long(value)
        return WreckAggregateValue({
            'terrain_seed': value & 0xffffffff,
            'river_seed': (value >> 32) & 0x7fffffff,
            'flora_seed': (value >> 64) & 0xffffffff,
            'deep_water': (value >> 63) & 0x1,
        })

def _get_exception_details():
    global sys, extract_traceback
    exc_type, exc_msg, exc_tb = sys.exc_info()
    if exc_tb is None: return None, 0, None, ''
    frames = extract_traceback(exc_tb)
    del exc_tb
    return frames[-1] # filename, lineno, function, text

def _parse_reference_by_name(reference):
    global WRECK
    for library in WRECK.libraries:
        prefix = library['prefix']
        if not prefix: continue
        if reference.startswith(prefix):
            return getattr(library, reference[len(prefix):])
    return None

def _import_sanitize_module_constants(data):
    for key, value in data.iteritems():
        if isinstance(value, str):
            new_value = _parse_reference_by_name(value)
            if new_value is not None:
                data[key] = new_value
                WRECK.log.details('%s.%s: replaced %r with %r' % (current_module(), key, value, new_value))

def _import_sanitize_references(data, *libraries):
    for library in libraries:
        with library as library_data:
            old_defaults = dict(library_data.defaults)
            library_data.defaults['required'] = False
            prefix = library_data.prefix
            for key, value in data.iteritems():
                if key.startswith(prefix) and (type(value) in {int, long}):
                    data[key] = getattr(library, key[len(prefix):])
                    WRECK.log.details('%s.%s: replaced %r with %r' % (current_module(), key, value, data[key]))
            library_data.defaults = old_defaults

def _import_sanitize_overrides(data):
    global WRECK
    allkeys = data.keys()
    for key in allkeys:
        if (key in WRECK._module_overrides) and (data[key] != WRECK._module_overrides[key]):
            WRECK.log.details('%s: restored value of WRECK-tracked %s (type %s)' % (current_module(), key, type(WRECK._module_overrides[key]).__name__))
            data[key] = WRECK._module_overrides[key]
        elif (key == 'pos_belfry_begin') and not isinstance(data[key], WreckVariable):
            WRECK._module_namespace[key] = data[key] = getattr(WRECK.libraries._posreg, 'pos%d' % int(data[key]))
            WRECK.log.details('%s: updated %s value' % (current_module(), key))
        elif (key == 'def_attrib') and not isinstance(data[key], WreckAggregateValue):
            WRECK._module_namespace[key] = data[key] = unparse_attr_aggregate(data[key])
            WRECK.log.details('%s: updated %s value' % (current_module(), key))
        elif (key == 'num_weapon_proficiencies'):
            WRECK.num_weapon_proficiencies = WRECK._module_namespace[key] = data[key]
            WRECK.log.details('%s: updated %s value' % (current_module(), key))

def _import_sanitize_header_skills(data):
    global WRECK, re
    with WRECK.libraries.skl as library_data:
        old_defaults = dict(library_data.defaults)
        library_data.defaults['required'] = False # Any variables we create are not is_required, i.e. compilation may proceed even if they're undefined
        prefix = library_data.prefix
        parser = re.compile('^knows_([\w\d]+)_(\d+)$')
        for key, value in data.iteritems():
            match = parser.match(key)
            if match:
                data[key] = int(match.groups()[1]) << (getattr(WRECK.libraries.skl, match.groups()[0]) << 2)
                WRECK.log.details('%s.%s: replaced %r with %r' % (current_module(), key, value, data[key]))
        library_data.defaults = old_defaults

def _import_sanitize_header_operations(data):
    # Ensure that the following operation is in lhs_operations list (this error was only fixed in Warband 1.166 patch)
    check_lhs = ['troop_inventory_slot_get_item_max_amount']
    # Ensure that we have depth_operations list and it's filled with correct operations
    check_depth = ['try_begin', 'try_for_range', 'try_for_range_backwards', 'try_for_parties', 'try_for_agents', 'try_for_prop_instances', 'try_for_players']
    for opname in check_lhs:
        if (opname in data) and (opname not in data['lhs_operations']):
            data['lhs_operations'].append(data[opname])
            WRECK.log.details('%s: added operation %s to lhs_operations list' % (current_module(), opname))
    if 'depth_operations' not in data:
        data['depth_operations'] = []
        WRECK.log.details('%s: added depth_operations list' % current_module())
    for opname in check_depth:
        if (opname in data) and (opname not in data['depth_operations']):
            data['depth_operations'].append(data[opname])
            WRECK.log.details('%s: added operation %s to depth_operations list' % (current_module(), opname))
    for opname, opcode in data.iteritems():
        if type(opcode) == int:
            WRECK.reference_operations[opcode] = opname
            setattr(WRECK.libraries._opcode, opname, opcode)

def _import_sanitize_header_triggers(data):
    for key, value in data.iteritems():
        if key.startswith('ti_') and (value < 0):
            WRECK.reference_triggers[int(value)] = key
    _import_sanitize_overrides(data)

def _wreck_import_hook(module_name, gvars = None, lvars = None, fromlist = [], level = -1):
    global _python_import, WRECK, sys
    # Check for already loaded modules
    if module_name in sys.modules:
        #print 'IMPORT: %s already loaded, using cache' % module_name
        return sys.modules[module_name]
    # Change import context
    bottom_name = module_name.split('.')[-1]
    with current_module(bottom_name):
        # Attempt to retrieve module code, assuming it's an actual module
        mfile = None
        module_code = None
        try:
            mfile, mpath, mdesc = imp.find_module(module_name)
            #print 'IMPORT: working on %s: %r, %r, %r' % (module_name, mfile, mpath, mdesc)
            if os.path.abspath(mpath).startswith(os.path.abspath(WRECK.config.module_path)):
                module_code = mfile.read()
                match = _detect_file_encoding.search(module_code[:200])
                if match:
                    module_code = module_code.replace(match.groups()[0], '...', 1) # Disable encoding tag
        finally:
            if isinstance(mfile, file): mfile.close()
        # Process module
        if module_code:
            module = imp.new_module(module_name)
            module.__dict__['__file__'] = mpath
            if bottom_name.startswith('ID_') or bottom_name.startswith('header_') or bottom_name.startswith('process_') or bottom_name in ('module_constants'):
                #print 'IMPORT: %s is auxilliary module file, using simple exec' % module_name
                exec(module_code, module.__dict__)
                # Sanitize
                if bottom_name.startswith('ID_'):
                    libraries = []
                    for library in WRECK.libraries:
                        if not library['module']: continue
                        if not library['prefix']: continue
                        if bottom_name == ''.join(['ID_', library['module']]):
                            libraries.append(library)
                    _import_sanitize_references(module.__dict__, *libraries)
                elif bottom_name == 'module_constants':
                    _import_sanitize_module_constants(module.__dict__)
                elif bottom_name == 'header_operations':
                    _import_sanitize_header_operations(module.__dict__)
                elif bottom_name == 'header_skills':
                    _import_sanitize_references(module.__dict__, WRECK.libraries.skl)
                    _import_sanitize_header_skills(module.__dict__)
                elif bottom_name == 'header_item_modifiers':
                    _import_sanitize_references(module.__dict__, WRECK.libraries.imod, WRECK.libraries.imodbit)
                elif bottom_name == 'header_triggers':
                    _import_sanitize_header_triggers(module.__dict__)
                elif bottom_name.startswith('header_'):
                    _import_sanitize_overrides(module.__dict__)
                # Extend module namespace if it was a header or ID file
                if not bottom_name.startswith('process_'):
                    WRECK._module_namespace.update(i for i in module.__dict__.iteritems() if not i[0].startswith('__'))
            else:
                module.__dict__.update(WRECK._module_namespace)
                #print 'IMPORT: %s is proper module file, using dynamic namespace: %r' % (module_name, module.__dict__.keys())
                namespace_backup = dict(module.__dict__)
                successful = False
                module_bytecode = compile(module_code, mpath, 'exec')
                while not successful:
                    try:
                        #print 'IMPORT: execcing...'
                        exec(module_bytecode, module.__dict__)
                        successful = True
                    except NameError as e:
                        exc_file, exc_line, exc_func, exc_text = _get_exception_details()
                        match = _detect_missing_var_name.match(e.message)
                        if not match: raise #WreckException('failed to parse NameError message to identify missing variable', formatted_exception())
                        missing_var = match.groups()[0]
                        correct_var = _parse_reference_by_name(missing_var)
                        if correct_var is None: raise #WreckException('failed to match undefined variable `{0}` to a module reference'.format(missing_var), formatted_exception())
                        namespace_backup[missing_var] = correct_var
                        WRECK.log.details('%s: auto-resolved variable %s to %r' % (current_module(), missing_var, correct_var))
                        WRECK.log.warning('had to auto-resolve reference `%s` in %s:%d, please fix to improve compilation speed' % (missing_var, exc_file, exc_line))
                        module.__dict__.clear()
                        module.__dict__.update(namespace_backup)
            sys.modules[module_name] = module
        else:
            if gvars is None: gvars = imp.new_module(module_name).__dict__
            if lvars is None: lvars = gvars
            module = _python_import(module_name, gvars, lvars, fromlist, level)
    return module


def _import_sanitize_plugin(data):
    # FIXME: load `injection` dict
    # FIXME: load data entries for all libraries
    pass

def register_plugin(name = None, glob = None):
    if WRECK.register_plugins:
        # If this is the first run for our plugin, we interrupt it's execution with a custom exception.
        # This exception will be caught by our import hook and plugin will be stored for later.

        stack = _get_current_stack()
        raise WreckInterruptPlugin(stack[1][2])

def require_plugin(*req_list):
    pass

def export_plugin_globals(**exported):
    pass

def extend_syntax(callback):
    pass


def _collect_injections(point, source = None):
    # Check if we need sourced list or not
    if source is not None:
        copy_list = lambda data, source: [WreckSourcedList(data[index], source, index) for index in xrange(len(data))]
    else:
        copy_list = lambda data, source: list(data)
    # Handle empty injection
    if point.name not in WRECK.injections: return copy_list(point.empty, source)
    inject_list = WRECK.injections[point.name]
    if not inject_list: return copy_list(point.empty, source)
    # Start generating list
    result = copy_list(point.prefix, source)
    first_run = True
    for inject in inject_list:
        result.extend(copy_list(inject.entries, inject.plugin))
        if not first_run: result.extend(copy_list(point.separator, source))
        first_run = False
    result.extend(copy_list(point.postfix, source))
    return result

def inject(name, prefix = None, separator = None, suffix = None, empty = None):
    return WreckInjectionPoint(name, prefix, separator, suffix, empty)

def _uid_std(offset):
    def _retrieve_uid(entry, index):
        return entry[offset]
    return _retrieve_uid

def _uid_index(entry, index):
    return '#{0}'.format(index)

def _uid_dialog(entry, index):
    return 'dlga_{0}:{1}'.format(entry[1], entry[4])

def _uid_trigger(entry, index):
    if int(entry[0]) in WRECK.reference_triggers: timer = WRECK.reference_triggers[int(entry[0])]
    else: timer = '{0:.2f}'.format(entry[0])
    repeat = 'ti_once' if entry[2] == 100000000.0 else '{0:.2f}'.format(entry[2])
    return 'trigger({1},{2:.2f},{3})'.format(index, timer, entry[1], repeat)

def _uid_strigger(entry, index):
    if int(entry[0]) in WRECK.reference_triggers: timer = WRECK.reference_triggers[int(entry[0])]
    else: timer = '{0:.2f}'.format(entry[0])
    return 'simple_trigger({1})'.format(index, timer)

_re_parser_id = re.compile('^[\w\d_]+$', re.IGNORECASE)

def _parse_id(rec, ofs, path = [], **argd):
    if rec[ofs] == 0: return '0', 1
    if not isinstance(rec[ofs], str): raise WreckParserException(path + [ofs], 'value {0!r} is not a legal identifier'.format(rec[ofs]))
    if _re_parser_id.match(internal_identifier(rec[ofs])): return rec[ofs], 1
    raise WreckParserException(path + [ofs], 'value `{0}` contains illegal symbols'.format(rec[ofs]))

def _parse_uid(rec, ofs, path = [], **argd):
    if not isinstance(rec[ofs], str): raise WreckParserException(path + [ofs], 'value {0!r} is not a legal identifier'.format(rec[ofs]))
    if _re_parser_id.match(internal_identifier(rec[ofs])): return rec[ofs], 1
    raise WreckParserException(path + [ofs], 'value `{0}` contains illegal symbols'.format(rec[ofs]))

def _parse_int(rec, ofs, path = [], **argd):
    if isinstance(rec[ofs], int): return rec[ofs], 1
    if isinstance(rec[ofs], long): return rec[ofs], 1
    if isinstance(rec[ofs], WreckVariable):
        if not rec[ofs].is_static:
            raise WreckParserException(path + [ofs], 'value of variable {0!r} cannot be determined at compile time'.format(rec[ofs]))
        value = rec[ofs]
    else:
        value = None
        if isinstance(rec[ofs], str): value = _parse_reference_by_name(rec[ofs])
        if value is None:
            try:
                value = int(rec[ofs])
            except Exception:
                raise WreckParserException(path + [ofs], 'cannot convert {0!r} to integer'.format(rec[ofs]))
    return value, 1

def _parse_float(rec, ofs, path = [], **argd):
    if isinstance(rec[ofs], WreckVariable):
        if not rec[ofs].is_static:
            raise WreckParserException(path + [ofs], 'value of variable {0!r} cannot be determined at compile time'.format(rec[ofs]))
        value = rec[ofs]
    else:
        try:
            value = float(rec[ofs])
        except Exception:
            raise WreckParserException(path + [ofs], 'cannot convert {0!r} to float'.format(rec[ofs]))
    return value, 1

def _parse_str(rec, ofs, path = [], **argd):
    if isinstance(rec[ofs], WreckVariable):
        if not rec[ofs].is_static:
            raise WreckParserException(path + [ofs], 'value of variable {0!r} cannot be determined at compile time'.format(rec[ofs]))
        value = rec[ofs]
    else:
        try:
            value = str(rec[ofs])
        except Exception:
            raise WreckParserException(path + [ofs], 'cannot convert {0!r} to string'.format(rec[ofs]))
    if value == '': value = '_'
    return value, 1

def _parse_ref(lib_name):
    def _parser(rec, ofs, path = [], **argd): # lib, base_entry, index, uid, path
        library = getattr(WRECK.libraries, lib_name, None)
        if not library: raise WreckException('illegal library {0!r} in _parse_ref definition'.format(lib_name))
        if isinstance(rec[ofs], WreckVariable): return rec[ofs], 1
        if isinstance(rec[ofs], str):
            prefix = library['prefix']
            if prefix and rec[ofs].startswith(prefix):
                return library(rec[ofs][len(prefix):]), 1
            else:
                return library(rec[ofs]), 1
        if isinstance(rec[ofs], int): return rec[ofs], 1
        raise WreckParserException(path + [ofs], 'cannot parse `{0}` as `{1}`'.format(rec[ofs], library['basename']))
    return _parser

def _parse_script(name_template, conversions = None, check_canfail = False):
    def _parser(rec, ofs, path = [], **argd):
        if isinstance(rec[ofs], tuple): rec[ofs] = list(rec[ofs])
        if not isinstance(rec[ofs], list):
            raise WreckParserException(path + [ofs], 'this is not a script: {0!r}'.format(rec[ofs]))
        result = list(rec[ofs]) # We leave rec[ofs] in source, but pass result to sanitized
        WRECK.scripting_blocks.append(WreckScript(name_template, rec[ofs], result, argd.get('entry'), path + [ofs], argd.get('library'), argd.get('uid'), conversions, check_canfail))
        return result, 1
    return _parser

def _validate_subparser(subparser):
    if isinstance(subparser, tuple): return _parse_tuple(*subparser)
    if isinstance(subparser, list): return _parse_list(*subparser)
    return subparser

def _optional(subparser, default):
    subparser = _validate_subparser(subparser)
    def _parser(rec, ofs, path = [], **argd):
        try:
            return subparser(rec, ofs, path, **argd)
        except WreckParserException:
            return default, 0
        except IndexError:
            return default, 0
    return _parser

def _repeatable(subparser):
    subparser = _validate_subparser(subparser)
    def _parser(rec, ofs, path = [], **argd):
        added = 0
        result = []
        try:
            while True:
                value, steps = subparser(rec, ofs + added, path, **argd)
                result.append(value)
                added += steps
        except WreckParserException: pass
        except IndexError: pass
        return result, added
    return _parser

def _parse_tuple(*subparsers):
    subparsers = map(_validate_subparser, subparsers)
    def _parser(rec, ofs, path = [], **argd):
        if isinstance(rec[ofs], tuple): rec[ofs] = list(rec[ofs])
        if not isinstance(rec[ofs], list): raise WreckParserException(path + [ofs], 'expected tuple, received {0!r}'.format(rec[ofs]))
        subentry = rec[ofs]
        subpath = path + [ofs]
        offset = 0
        result = []
        try:
            for subparser in subparsers:
                value, steps = subparser(subentry, offset, subpath, **argd)
                result.append(value)
                offset += steps
        except IndexError:
            raise WreckParserException(path + [ofs], 'not enough elements in tuple {0!r}'.format(rec[ofs]))
        if offset < len(rec[ofs]):
            WRECK.log.warning('extra data at the end of tuple {0!r}'.format(rec[ofs]))
            # TODO: need more elaborate message, use argd
        return result, 1
    return _parser

def _parse_list(subparser):
    subparser = _validate_subparser(subparser)
    repeatable_subparser = _repeatable(subparser)
    def _parser(rec, ofs, path = [], **argd):
        if isinstance(rec[ofs], tuple): rec[ofs] = list(rec[ofs])
        if not isinstance(rec[ofs], list): raise WreckParserException(path + [ofs], 'expected list, received {0!r}'.format(rec[ofs]))
        result, steps = repeatable_subparser(rec[ofs], 0, path + [ofs], **argd)
        if steps < len(rec[ofs]):
            # We failed at some step before the end of list, so try again since _repeatable has suppressed any exception
            failure = subparser(rec[ofs], steps, path + [ofs], **argd)
            # Previous line should have thrown a WreckParserException, but if it didn't, it's a major mistake by itself
            raise WreckException('_parse_list() parser failed', 'call parameters: rec = %r, ofs = %d, path = %r, argd = %r\n_repeatable returned result = %r, steps = %r\nlen(rec[ofs]) = %d, hence called subparser\ncall parameters: rec = %r, ofs = %d, path = %r, argd\nsubparser returned %r instead of throwing exception' % (rec, ofs, path, argd, result, steps, len(rec[ofs]), rec[ofs], steps, path + [ofs], failure))
        return result, 1
    return _parser

def _parse_expect(value):
    def _parser(rec, ofs, path = [], **argd):
        if rec[ofs] != value: raise WreckParserException(path + [ofs], 'value {0!r} found, {1!r} expected'.format(rec[ofs], value))
        return rec[ofs], 1
    return _parser

def _parse_aggregate(unpack):
    def _parser(rec, ofs, path = [], **argd):
        if isinstance(rec[ofs], WreckAggregateValue): return rec[ofs], 1
        try:
            return unpack(rec[ofs]), 1
        except Exception:
            raise WreckParserException(path + [ofs], 'failed to unpack value {0!r} as aggregate'.format(rec[ofs]))
    return _parser

def _parse_file(*lookups):
    return _parse_str # TODO: implement proper filename check, maybe with folder reference so WRECK could check for file's presence

def _parse_intpair(rec, ofs, path = [], **argd):
    if isinstance(rec[ofs], tuple): rec[ofs] = list(rec[ofs])
    if isinstance(rec[ofs], list): return _parse_tuple(_parse_int, _parse_int)(rec, ofs, path, **argd)
    value, steps = _parse_int(rec, ofs, path, **argd)
    return [value, 0], 1


# |                                                                            |
# |    COMPILER HELPER FUNCTIONS END                                           |
# +                                                                            +
#  \                                                                          /
#   +------------------------------------------------------------------------+
# endregion

# region Compiler Base Classes
#   +------------------------------------------------------------------------+
#  /                                                                          \
# +                                                                            +
# |    COMPILER BASE CLASSES                                                   |
# |                                                                            |


class WreckException(Exception):
    """Basic WRECK exception class.

    Used for all WRECK-related situations. Provides some basic output formatting and limited traceback ability.

    Would be better to use Python 3.x syntax for exception chaining, but we're trying to keep things 2.6 compatible for now.
    """

    def formatted(self):
        output = []
        for index in xrange(len(self.args)):
            prefix = '  ' * index
            messages = self.args[index].strip().split('\n')
            for message in messages:
                output.append(prefix)
                output.append(message.rstrip())
                output.append('\n')
        return ''.join(output)

    __str__ = formatted

    __repr__ = lambda self: 'WreckException(%r)' % self.args


class WreckParserException(WreckException):

    error_path = None

    def __init__(self, path, *args):
        self.error_path = path
        super(WreckParserException, self).__init__(*args)


class WreckInterruptPlugin(Exception):
    pass


class current_module(object):

    __stack = []

    def __call__(self, module_name = None):
        if module_name is None: return self.name
        self.__stack.append(module_name)
        return self

    @property
    def name(self):
        return self.__stack[-1] if self.__stack else None

    @property
    def stack(self):
        return tuple(self.__stack)

    def enter(self):
        return self.name

    __enter__ = enter

    def exit(self, exc_type = None, exc_value = None, tb = None):
        if not self.__stack: raise WreckException('cannot leave current execution context: top of the stack already')
        self.__stack.pop()
        return self.name

    __exit__ = exit

current_module = current_module()


class WreckLogger(object):

    messages = None

    def __init__(self):
        self.messages = {}

    def add_message(self, severity, message):
        if severity not in self.messages: self.messages[severity] = []
        if not isinstance(message, list): message = [message]
        self.messages[severity].append((time.time(), message))

    def debug(self, message):
        self.add_message(DEBUG, message)
    def details(self, message):
        self.add_message(DETAILS, message)
    def info(self, message):
        self.add_message(INFO, message)
    def advice(self, message):
        self.add_message(ADVICE, message)
    def warning(self, message):
        self.add_message(WARNING, message)
    def mistake(self, message):
        self.add_message(MISTAKE, message)
    def error(self, message):
        self.add_message(ERROR, message)
    def failure(self, message):
        self.add_message(FAILURE, message)
    def critical(self, message):
        self.add_message(CRITICAL, message)

    def get_messages(self, severity):
        if severity not in self.messages: return []
        return self.messages[severity]

    def format_messages(self, severity, prefix = '', offset = 0, format = '{message}', line_width = None):
        if severity not in self.messages: return ''
        result = []
        for timestamp, stack in self.messages[severity]:
            output = []
            for index in xrange(len(stack)):
                if index:
                    output.append('\n')
                    output.append(' ' * (len(prefix) + index * offset))
                    output.append(stack[index])
                else:
                    output.append(prefix)
                    output.append(format.format(timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp)), message = stack[index]))
            result.append(''.join(output))
        return '\n'.join(result)


class WreckConfig(object):
    """Class to hold WRECK configuration settings.

    Essentially, a glorified dictionary. Accepts arbitrary number of values and stores them in objectified format.
    """

    def __init__(self, **argd):
        super(WreckConfig, self).__init__()
        self.__dict__.update(argd)

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __iter__(self):
        return self.__dict__.itervalues()


class WreckInjection(object):
    plugin = None
    entries = None
    def __init__(self, entries, plugin = '<wreck>'):
        self.plugin = plugin
        self.entries = entries


class WreckInjectionPoint(object):
    name = None
    prefix = None
    separator = None
    postfix = None
    empty = None
    def __init__(self, name, prefix = None, separator = None, postfix = None, empty = None):
        self.name = name
        self.prefix = prefix if prefix else []
        self.separator = separator if separator else []
        self.postfix = postfix if postfix else []
        self.empty = empty if empty else []


class WreckSourcedList(list):
    source = None
    index = 0
    def __init__(self, data = [], source = None, index = 0):
        self.source = source
        self.index = index
        super(WreckSourceList, self).__init__(data)


class WreckOperation(object):
    """Class for handling mathematical operations with WreckVariable's.

    Essentially, this is just a placeholder for information related to mathematical operations. For each operation
    there's info on how to display it in different situations, how to evaluate it at compile time and how to convert
    it to Warband module code.
    """

    shorthand = '?'
    code = None
    text = ''
    bytecode = None
    opcount = 0
    unary = False
    associative = False

    def __init__(self, shorthand, code, text, *operations, **extras):
        self.shorthand = shorthand
        self.code = code
        self.text = text
        self.opcount = len(operations)
        self.bytecode = reduce(lambda a, b: a+b, operations)
        self.unary = extras.get('unary', False)
        self.associative = extras.get('associative', False)

    def __call__(self, *argl):
        return self.code(*argl)

    def __repr__(self):
        return 'WreckOperation[%s]' % self.shorthand

    def compile(self, dest, *operands):
        global _wreck_op_parser
        code = map(lambda el: int(el.format(*operands, dest = dest)) if isinstance(el, str) else el, self.bytecode)
        return self.opcount, code


class WreckVariable(object):
    """Base class for Warband module variables and references.

    This class handles module variables and references, as well as any mathematical expressions that use them.

    All the magic that allows the modder to freely use references in the code is contained here.

    WreckVariable works in tandem with WreckLibrary class, which represents an array of module references. So where
    a WreckVariable may represent a single reference like "itm_sword", WreckLibrary represents the entire module_items
    file.

    WreckVariable.__int__() - for variables and static expressions, resolves and returns it's value
    WreckVariable.__long__() - same as __int__
    WreckVariable.__index__() - same as __int__
    WreckVariable.__float__() - same as __int__, converts resulting value to float
    WreckVariable.__str__() - same as __int__, converts resulting value to string
    WreckVariable.__repr__() - describes variable/expression in detail for debugging and error reporting routines.
    WreckVariable.__call__() - for dynamic expressions, resolves them and returns dynamically generated code.
    """

    references = None     # Contains set of names for modules that reference this variable in the code
    is_expression = False # Signifies a mathematical expression instead of a simple reference
    is_static = True      # Signifies that the variable contains a static value and can be computed at compile-time
    is_required = True    # If true, this variable will generate error if it's value is not defined
    is_forced = False     # Set to True if this variable or expression was forcefully evaluated

    module = None
    name = None
    value = None
    operation = None

    def __init__(self, module = None, name = None, value = None, operation = None, static = True, required = True):
        self.module = module
        self.name = name
        self.references = set()
        self.is_required = required
        if operation:
            if not isinstance(operation[0], WreckOperation): raise SyntaxError('illegal operation %r' % operation[0])
            self.operation = operation
            self.is_expression = True
            self.is_required = False
            if static:
                for operand in operation[1:]:
                    if isinstance(operand, WreckVariable) and not operand.is_static: static = False
        else:
            self.value = value
        self.is_static = static

    def add_reference(self, reference = None):
        if self.is_expression: return
        if reference is None: reference = current_module()
        if not reference: return
        self.references.add(reference)

    def list_references(self):
        return ', '.join(sorted(self.references))

    def __add__(self, other):    return WreckVariable(operation = (_add, self, other))
    def __sub__(self, other):    return WreckVariable(operation = (_sub, self, other))
    def __mul__(self, other):    return WreckVariable(operation = (_mul, self, other))
    def __div__(self, other):    return WreckVariable(operation = (_div, self, other))
    def __mod__(self, other):    return WreckVariable(operation = (_mod, self, other))
    def __pow__(self, other):    return WreckVariable(operation = (_pow, self, other))
    def __lshift__(self, other): return WreckVariable(operation = (_shl, self, other))
    def __rshift__(self, other): return WreckVariable(operation = (_shr, self, other))
    def __and__(self, other):    return WreckVariable(operation = (_and, self, other))
    def __or__(self, other):     return WreckVariable(operation = (_or, self, other))

    def __radd__(self, other):    return WreckVariable(operation = (_add, other, self))
    def __rsub__(self, other):    return WreckVariable(operation = (_sub, other, self))
    def __rmul__(self, other):    return WreckVariable(operation = (_mul, other, self))
    def __rdiv__(self, other):    return WreckVariable(operation = (_div, other, self))
    def __rmod__(self, other):    return WreckVariable(operation = (_mod, other, self))
    def __rpow__(self, other):    return WreckVariable(operation = (_pow, other, self))
    def __rlshift__(self, other): return WreckVariable(operation = (_shl, other, self))
    def __rrshift__(self, other): return WreckVariable(operation = (_shr, other, self))
    def __rand__(self, other):    return WreckVariable(operation = (_and, other, self))
    def __ror__(self, other):     return WreckVariable(operation = (_or, other, self))

    def __neg__(self): return WreckVariable(operation = (_neg, self))
    def __pos__(self): return self
    def __abs__(self): return WreckVariable(operation = (_abs, self))

    def formatted_name(self):
        if self.is_expression: return '<expr>'
        if self.module is None: return '?.%s' % self.name
        return '%s.%s' % (self.module['basename'], self.name)

    def __int__(self):
        try:
            if self.is_expression:
                if not isinstance(self.operation[0], WreckOperation): raise WreckException('illegal operation %r' % (self.operation[0]))
                if not self.is_static: raise WreckException('expression %r is not static and cannot be calculated at compile-time' % self)
                try:
                    return self.operation[0](*map(int, self.operation[1:]))
                except ArithmeticError:
                    if not self.force_resolution: raise
                    for operand in self.operation[1:]:
                        if isinstance(operand, WreckVariable) and operand.is_forced:
                            self.is_forced = True
                            return 0
                    raise
            else:
                if self.value is not None: return self.value
                name = 'reference' if self.is_static else 'variable'
                if self.force_resolution:
                    WRECK.log.error('undefined %s %r, referenced by: %s' % (name, self, self.list_references()))
                    WRECK.undefined_variables.add(self)
                    self.is_forced = True
                    return 0
                else:
                    raise WreckException('undefined %s %r, referenced by: %s' % (name, self, self.list_references()))
        except WreckException as e:
            raise WreckException('failed to calculate expression %r' % self, *e.args)
        except Exception as e:
            raise WreckException('failed to calculate expression %r' % self, formatted_exception())

    __long__ = lambda self: self.__int__() # lambda works as wrapper, so we can safely replace __int__ in child classes
    __index__ = lambda self: self.__int__()
    __float__ = lambda self: float(self.__int__())
    __str__ = lambda self: str(self.__int__())

    def __repr__(self):
        if self.is_expression:
            if isinstance(self.operation[0], WreckOperation):
                if self.operation[0].unary:
                    return self.operation[0].text % self.operation[1:]
                repr_ops = map(repr, self.operation[1:])
                if self.operation[0].associative:
                    clear_ops = []
                    for index in (1,2):
                        op = self.operation[index]
                        if isinstance(op, WreckVariable) and op.is_expression:
                            if op.operation[0].unary:
                                clear_ops.append(repr_ops[index-1])
                            elif op.operation[0] == self.operation[0]:
                                clear_ops.append(repr_ops[index-1][1:-1])
                            else:
                                break
                        else:
                            clear_ops.append(repr_ops[index-1])
                    if len(clear_ops) == 2: return '({1} {0} {2})'.format(self.operation[0].text, clear_ops[0], clear_ops[1])
                return '({1} {0} {2})'.format(self.operation[0].text, repr_ops[0], repr_ops[1])
            else:
                return '%s(operation = %r)' % (type(self).__name__, self.operation)
        else:
            if not DEBUG_MODE:
                return self.formatted_name()
            elif self.is_static:
                value = '?' if self.value is None else str(self.value)
                return '%s<=%s>' % (self.formatted_name(), value)
            else:
                value = '?' if self.value is None else str(self.value)
                return '%s<@%s>' % (self.formatted_name(), value)

    def __call__(self, script_name, destination, local_depth = 0):
        if not self.is_expression: raise WreckException('attempt to generate code from static reference %r' % self)
        if self.is_static: raise WreckException('attempt to generate code from static expression %r' % self)
        try:
            total_commands = 0 # Usually an expression will generate one command
            code = [] # Resulting Warband code (already compiled)
            # Pre-calculate operands
            operands = []
            for operand in self.operation[1:]:
                if isinstance(operand, WreckVariable) and operand.is_expression and not operand.is_static:
                    tmp_local = opmask_local_variable | WRECK.get_local_tmp_id(script_name, local_depth)
                    op_count, new_code = operand(script_name, tmp_local, local_depth)
                    code.extend(new_code)
                    total_commands += op_count
                    local_depth += 1
                    operands.append(tmp_local)
                else:
                    operands.append(operand)
            if isinstance(self.operation[0], WreckOperation):
                try:
                    op_count, new_code = self.operation[0].compile(destination, *operands)
                    code.extend(new_code)
                    total_commands += op_count
                except Exception as e:
                    raise WreckException('operation %r failed to compile' % (self.operation, ), formatted_exception())
            else:
                raise WreckException('illegal operation in expression %r' % self)
            return total_commands, code
        except WreckException as e:
            raise WreckException('failed to generate dynamic code for expression %r' % self, *e.args)
        except Exception as e:
            raise WreckException('failed to generate dynamic code for expression %r' % self, formatted_exception())


class WreckProperty(WreckVariable):
    """A subclass of WreckVariable, providing compile-time hooks to actual values in module files.

    With properties it becomes possible to retrieve values directly from module files tuples at compile-time, like
    using itm.bastard_sword.price will return actual price for "itm_bastard_sword", as it's defined in module_items.py
    and possibly modified in active plugins. This is primarily intended for situations when you have a number of related
    game entities. For example, it's possible to use formulaes for weapon prices, making them dependent on starting
    price for iron and lumber.
    """

    entity = None
    #normalizer = None

    def __init__(self, module, entity, prop_name, *retrieval):
        if not entity.is_static: raise WreckException('property {0!r} cannot be evaluated: reference {1!r} not static'.format(self, entity))
        super(WreckProperty, self).__init__(module)
        self.name = prop_name
        self.is_expression = True
        self.entity = entity
        self.operation = retrieval
        self.is_static = True

    def add_reference(self, *argl, **argd):
        super(WreckProperty, self).add_reference(*argl, **argd)
        self.entity.add_reference(*argl, **argd)

    def formatted_name(self):
        return '%s.%s' % (self.entity.formatted_name(), self.name)

    __repr__ = formatted_name

    def __int__(self):
        try:
            if not self.module['sanitized']:
                raise WreckException('cannot evaluate property %r: module %r has no sanitized data source' % (self, self.module))
            result = self.module['sanitized'][int(self.entity)]
        except WreckException as e: raise WreckException('failed to calculate property %s' % repr(self), *e.args)
        except Exception as e: raise WreckException('failed to calculate property %s' % repr(self), formatted_exception())
        for key, convertor, default in self.operation:
            try:
                result = result[key]
                if convertor: result = convertor(result)
            except IndexError: result = default
            except KeyError: result = default
        #if self.normalizer: result = self.normalizer(result)
        return result

    def __call__(self):
        raise WreckException('cannot generate dynamic code from property %r' % self)


class WreckItemReference(WreckVariable):
    """WreckVariable subclass for game items.

    Provides a number of hooks for item properties to access them at compile-time.
    """

    @property
    def flags(self):              return WreckProperty(WRECK.itm, self, 'flags', (3, None, 0))
    @property
    def capabilities(self):       return WreckProperty(WRECK.itm, self, 'capabilities', (4, None, 0))
    @property
    def price(self):              return WreckProperty(WRECK.itm, self, 'price', (5, None, 0))
    @property
    def weight(self):             return WreckProperty(WRECK.itm, self, 'weight', (6, unparse_item_aggregate, {}), ('weight', None, 0.0))
    @property
    def head_armor(self):         return WreckProperty(WRECK.itm, self, 'head_armor', (6, unparse_item_aggregate, {}), ('head', None, 0))
    @property
    def body_armor(self):         return WreckProperty(WRECK.itm, self, 'body_armor', (6, unparse_item_aggregate, {}), ('body', None, 0))
    @property
    def leg_armor(self):          return WreckProperty(WRECK.itm, self, 'leg_armor', (6, unparse_item_aggregate, {}), ('leg', None, 0))
    @property
    def difficulty(self):         return WreckProperty(WRECK.itm, self, 'difficulty', (6, unparse_item_aggregate, {}), ('diff', None, 0))
    @property
    def hp(self):                 return WreckProperty(WRECK.itm, self, 'hp', (6, unparse_item_aggregate, {}), ('hp', None, 0))
    @property
    def speed(self):              return WreckProperty(WRECK.itm, self, 'speed', (6, unparse_item_aggregate, {}), ('speed', None, 0))
    @property
    def missile_speed(self):      return WreckProperty(WRECK.itm, self, 'missile_speed', (6, unparse_item_aggregate, {}), ('msspd', None, 0))
    @property
    def size(self):               return WreckProperty(WRECK.itm, self, 'size', (6, unparse_item_aggregate, {}), ('size', None, 0))
    @property
    def max_amount(self):         return WreckProperty(WRECK.itm, self, 'max_amount', (6, unparse_item_aggregate, {}), ('qty', None, 0))
    @property
    def swing(self):              return WreckProperty(WRECK.itm, self, 'swing', (6, unparse_item_aggregate, {}), ('swing', None, 0))
    @property
    def swing_damage(self):       return WreckProperty(WRECK.itm, self, 'swing_damage', (6, unparse_item_aggregate, {}), ('swing', lambda x: x & ibf_armor_mask, 0))
    @property
    def swing_damage_type(self):  return WreckProperty(WRECK.itm, self, 'swing_damage_type', (6, unparse_item_aggregate, {}), ('swing', lambda x: x >> iwf_damage_type_bits, 0))
    @property
    def thrust(self):             return WreckProperty(WRECK.itm, self, 'thrust', (6, unparse_item_aggregate, {}), ('thrust', None, 0))
    @property
    def thrust_damage(self):      return WreckProperty(WRECK.itm, self, 'thrust_damage', (6, unparse_item_aggregate, {}), ('thrust', lambda x: x & ibf_armor_mask, 0))
    @property
    def thrust_damage_type(self): return WreckProperty(WRECK.itm, self, 'thrust_damage_type', (6, unparse_item_aggregate, {}), ('thrust', lambda x: x >> iwf_damage_type_bits, 0))
    @property
    def abundance(self):          return WreckProperty(WRECK.itm, self, 'abundance', (6, unparse_item_aggregate, {}), ('abundance', None, 0))
    @property
    def modifiers(self):          return WreckProperty(WRECK.itm, self, 'modifiers', (7, None, 0))

    food_quality = head_armor
    accuracy = leg_armor
    horse_maneuver = speed
    horse_speed = shield_height = missile_speed
    weapon_length = horse_scale = size
    horse_charge = thrust_damage


class WreckSceneReference(WreckVariable):
    """WreckVariable subclass for game scenes.

    Provides a number of hooks for scene properties to access them at compile-time.
    """

    @property
    def flags(self): return WreckProperty(WRECK.scn, self, 'flags', (1, None, 0))
    @property
    def min_x(self): return WreckProperty(WRECK.scn, self, 'min_x', (4, None, 0), (0, int, 0))
    @property
    def min_y(self): return WreckProperty(WRECK.scn, self, 'min_y', (4, None, 0), (1, int, 0))
    @property
    def max_x(self): return WreckProperty(WRECK.scn, self, 'max_x', (5, None, 0), (0, int, 0))
    @property
    def max_y(self): return WreckProperty(WRECK.scn, self, 'max_y', (5, None, 0), (1, int, 0))
    @property
    def water_level(self): return WreckProperty(WRECK.scn, self, 'water_level', (6, lambda x: int(x + 0.5), 0))
    @property
    def water_level_cm(self): return WreckProperty(WRECK.scn, self, 'water_level_cm', (6, lambda x: int(x * 100 + 0.5), 0))
    @property
    def terrain_seed(self): return WreckProperty(WRECK.scn, self, 'terrain_seed', (7, unparse_terrain_aggregate, None), ('terrain_seed', None, 0))
    @property
    def river_seed(self): return WreckProperty(WRECK.scn, self, 'river_seed', (7, unparse_terrain_aggregate, None), ('river_seed', None, 0))
    @property
    def flora_seed(self): return WreckProperty(WRECK.scn, self, 'flora_seed', (7, unparse_terrain_aggregate, None), ('flora_seed', None, 0))
    @property
    def size_x(self): return WreckProperty(WRECK.scn, self, 'size_x', (7, unparse_terrain_aggregate, None), ('size_x', None, 0))
    @property
    def size_y(self): return WreckProperty(WRECK.scn, self, 'size_y', (7, unparse_terrain_aggregate, None), ('size_y', None, 0))
    @property
    def valley(self): return WreckProperty(WRECK.scn, self, 'valley', (7, unparse_terrain_aggregate, None), ('valley', None, 0))
    @property
    def hill_height(self): return WreckProperty(WRECK.scn, self, 'hill_height', (7, unparse_terrain_aggregate, None), ('hill_height', None, 0))
    @property
    def ruggedness(self): return WreckProperty(WRECK.scn, self, 'ruggedness', (7, unparse_terrain_aggregate, None), ('ruggedness', None, 0))
    @property
    def vegetation(self): return WreckProperty(WRECK.scn, self, 'vegetation', (7, unparse_terrain_aggregate, None), ('vegetation', None, 0))
    @property
    def terrain(self): return WreckProperty(WRECK.scn, self, 'terrain', (7, unparse_terrain_aggregate, None), ('terrain', None, 0))
    @property
    def polygon_size(self): return WreckProperty(WRECK.scn, self, 'polygon_size', (7, unparse_terrain_aggregate, None), ('polygon_size', None, 2))
    @property
    def disable_grass(self): return WreckProperty(WRECK.scn, self, 'disable_grass', (7, unparse_terrain_aggregate, None), ('disable_grass', None, 0))
    @property
    def shade_occlude(self): return WreckProperty(WRECK.scn, self, 'shade_occlude', (7, unparse_terrain_aggregate, None), ('shade_occlude', None, 0))
    @property
    def place_river(self): return WreckProperty(WRECK.scn, self, 'place_river', (7, unparse_terrain_aggregate, None), ('place_river', None, 0))
    @property
    def deep_water(self): return WreckProperty(WRECK.scn, self, 'deep_water', (7, unparse_terrain_aggregate, None), ('deep_water', None, 0))


class WreckFactionReference(WreckVariable):
    """WreckVariable subclass for game factions.

    Provides a number of hooks for faction properties to access them at compile-time.
    """

    @property
    def flags(self): return WreckProperty(WRECK.fac, self, 'flags', (2, None, 0))
    @property
    def coherence(self): return WreckProperty(WRECK.fac, self, 'coherence', (3, lambda x: int(x * 100 + 0.5), 0))
    @property
    def default_color(self): return WreckProperty(WRECK.fac, self, 'default_color', (6, None, 0xAAAAAA))


class WreckItemModifierReference(WreckVariable):
    """WreckVariable subclass for game item modifiers.

    Provides a number of hooks for item modifier properties to access them at compile-time.
    """

    @property
    def price_coeff(self): return WreckProperty(WRECK.imod, self, 'price_coeff', (2, lambda x: int(x * 100 + 0.5), 0))
    @property
    def rarity_coeff(self): return WreckProperty(WRECK.imod, self, 'rarity_coeff', (3, lambda x: int(x * 100 + 0.5), 0))


class WreckPartyReference(WreckVariable):
    """WreckVariable subclass for game parties.

    Provides a number of hooks for party properties to access them at compile-time.
    """

    @property
    def flags_field(self): return WreckProperty(WRECK.p, self, 'flags_field', (2, None, 0)) # Use this if you need icon+flags combined value
    @property
    def icon(self): return WreckProperty(WRECK.p, self, 'icon', (2, lambda x: x & 0xff, 0))
    @property
    def flags(self): return WreckProperty(WRECK.p, self, 'flags', (2, lambda x: (x >> 8) << 8, 0))
    @property
    def default_menu(self): return WreckProperty(WRECK.p, self, 'menu', (3, None, 0))
    @property
    def template(self): return WreckProperty(WRECK.p, self, 'template', (4, None, 0))
    @property
    def faction(self): return WreckProperty(WRECK.p, self, 'faction', (5, None, 0))
    @property
    def personality(self): return WreckProperty(WRECK.p, self, 'personality', (6, None, 0))
    @property
    def ai(self): return WreckProperty(WRECK.p, self, 'ai', (7, None, ai_bhvr_hold))
    @property
    def ai_target(self): return WreckProperty(WRECK.p, self, 'ai_target', (8, None, 0))
    @property
    def start_x(self): return WreckProperty(WRECK.p, self, 'start_x', (9, None, None), (0, lambda x: int(x + 0.5), 0))
    @property
    def start_x_cm(self): return WreckProperty(WRECK.p, self, 'start_x_cm', (9, None, None), (0, lambda x: int(x * 100 + 0.5), 0))
    @property
    def start_y(self): return WreckProperty(WRECK.p, self, 'start_y', (9, None, None), (0, lambda x: int(x + 0.5), 0))
    @property
    def start_y_cm(self): return WreckProperty(WRECK.p, self, 'start_y_cm', (9, None, None), (0, lambda x: int(x * 100 + 0.5), 0))
    @property
    def angle(self): return WreckProperty(WRECK.p, self, 'angle', (11, lambda x: int(x + 0.5), 0))
    @property
    def angle_100(self): return WreckProperty(WRECK.p, self, 'angle_100', (11, lambda x: int(x * 100 + 0.5), 0))


class WreckPartyTemplateReference(WreckVariable):
    """WreckVariable subclass for game party templates.

    Provides a number of hooks for party template properties to access them at compile-time.
    """

    @property
    def flags_field(self): return WreckProperty(WRECK.pt, self, 'flags_field', (2, None, 0)) # Use this if you need icon+flags combined value
    @property
    def icon(self): return WreckProperty(WRECK.pt, self, 'icon', (2, lambda x: x & 0xff, 0))
    @property
    def flags(self): return WreckProperty(WRECK.pt, self, 'flags', (2, lambda x: (x >> 8) << 8, 0))
    @property
    def default_menu(self): return WreckProperty(WRECK.pt, self, 'default_menu', (3, None, 0))
    @property
    def faction(self): return WreckProperty(WRECK.pt, self, 'faction', (4, None, 0))
    @property
    def personality(self): return WreckProperty(WRECK.pt, self, 'personality', (5, None, 0))


class WreckTroopReference(WreckVariable):
    """WreckVariable subclass for game troops.

    Provides a number of hooks for troop properties to access them at compile-time.
    """

    @property
    def flags(self): return WreckProperty(WRECK.trp, self, 'flags', (3, None, 0))
    @property
    def scene(self): return WreckProperty(WRECK.trp, self, 'scene', (4, None, 0))
    @property
    def faction(self): return WreckProperty(WRECK.trp, self, 'faction', (6, None, 0))
    @property
    def level(self): return WreckProperty(WRECK.trp, self, 'level', (8, unparse_attr_aggregate, 0), ('level', None, 0))
    @property
    def strength(self): return WreckProperty(WRECK.trp, self, 'strength', (8, unparse_attr_aggregate, 0), ('str', None, 0))
    @property
    def agility(self): return WreckProperty(WRECK.trp, self, 'agility', (8, unparse_attr_aggregate, 0), ('agi', None, 0))
    @property
    def intelligence(self): return WreckProperty(WRECK.trp, self, 'intelligence', (8, unparse_attr_aggregate, 0), ('int', None, 0))
    @property
    def charisma(self): return WreckProperty(WRECK.trp, self, 'charisma', (8, unparse_attr_aggregate, 0), ('cha', None, 0))
    @property
    def wp_1h(self): return WreckProperty(WRECK.trp, self, 'wp_1h', (9, unparse_wp_aggregate, 0), (wpt_one_handed_weapon, None, 0))
    @property
    def wp_2h(self): return WreckProperty(WRECK.trp, self, 'wp_2h', (9, unparse_wp_aggregate, 0), (wpt_two_handed_weapon, None, 0))
    @property
    def wp_polearms(self): return WreckProperty(WRECK.trp, self, 'wp_polearms', (9, unparse_wp_aggregate, 0), (wpt_polearm, None, 0))
    @property
    def wp_archery(self): return WreckProperty(WRECK.trp, self, 'wp_archery', (9, unparse_wp_aggregate, 0), (wpt_archery, None, 0))
    @property
    def wp_crossbows(self): return WreckProperty(WRECK.trp, self, 'wp_crossbows', (9, unparse_wp_aggregate, 0), (wpt_crossbow, None, 0))
    @property
    def wp_thrown(self): return WreckProperty(WRECK.trp, self, 'wp_thrown', (9, unparse_wp_aggregate, 0), (wpt_throwing, None, 0))
    @property
    def wp_firearms(self): return WreckProperty(WRECK.trp, self, 'wp_firearms', (9, unparse_wp_aggregate, 0), (wpt_firearm, None, 0))
    @property
    def skills(self): return WreckProperty(WRECK.trp, self, 'skills', (10, None, 0))
    @property
    def facecode_1(self): return WreckProperty(WRECK.trp, self, 'facecode_1', (11, None, 0))
    @property
    def facecode_2(self): return WreckProperty(WRECK.trp, self, 'facecode_2', (12, None, 0))
    @property
    def upgrade_path_1(self): return WreckProperty(WRECK.trp, self, 'upgrade_path_1', (14, None, 0))
    @property
    def upgrade_path_2(self): return WreckProperty(WRECK.trp, self, 'upgrade_path_2', (15, None, 0))


class _WreckLibraryData(object):
    entries = None
    unassigned = None
    basename = None
    defaults = None
    extendable = True
    opmask = 0
    varclass = None
    source = None    # Raw data entries for associated module
    sanitized = None # Sanitized data entries (passed through parser and code injection)
    processed = None # Processed data entries (converted to M&B bytecode but not yet merged together)
    compiled = None  # A single string containing the compiled module, ready for export
    module = None # module name, to help find python module file
    data = None   # data name, to detect what module container has the actual tuples
    export = None # exported filename
    export_ext = 'txt' # exported file extension
    prefix = '' # prefix for reference IDs generation
    uid_generator = None
    parser = None
    processor = None
    aggregator = None
    def __init__(self, basename, defaults = None, opmask = 0, varclass = WreckVariable, source = [], **argd):
        self.basename = basename
        self.entries = {}
        self.unassigned = set()
        self.defaults = defaults if defaults else {}
        self.opmask = opmask
        self.varclass = varclass
        self.source = source if source else []
        self.__dict__.update(argd)


class WreckLibrary(object):
    """Reference generator class.

    This class is used to represent an entire Warband module file, like module_items.py.

    It will dynamically generate references to entries within it's associated module, track their value assignments
    and provide support for WRECK syntax sugar.
    """

    __data = None

    def __init__(self, basename, varclass = WreckVariable, opmask = 0, **argd):
        self.__dict__['_WreckLibrary__data'] = _WreckLibraryData(basename = basename, opmask = opmask, varclass = varclass, **argd)

    def __getattr__(self, name, reference = None):
        """Supports ``itm.sword`` syntax in module files and plugins. Intended primarily for module files."""
        if name in self.__data.entries:
            variable = self.__data.entries[name]
        elif not self.__data.extendable:
            raise WreckException('illegal reference `%s.%s`' % (self.__data.basename, name))
        else:
            self.__data.entries[name] = variable = self.__data.varclass(module = self, name = name, **self.__data.defaults)
            self.__data.unassigned.add(name)
        variable.add_reference(reference)
        return variable

    # Supports ``itm('sword')`` syntax in module files and plugins. Intended primarily for plugins.
    __call__ = __getattr__

    def __setattr__(self, name, value):
        """To be called in WRECK own code mostly, and possibly in more complex plugins."""
        if name in self.__data.entries:
            self.__data.entries[name].value = value
        elif not self.__data.extendable:
            raise WreckException('illegal reference `%s.%s`' % (self.__data.basename, name))
        else:
            self.__data.entries[name] = self.__data.varclass(module = self, name = name, value = value, **self.__data.defaults)
        if name in self.__data.unassigned: self.__data.unassigned.remove(name)

    def __enter__(self):
        return self.__data

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __getitem__(self, key):
        """Internal data fields of WreckLibrary can be accessed through dict-like syntax (we cannot use object syntax since it's used by entity references)."""
        # TODO: integer key should retrieve a reference from the library once sanitized array is ready
        return getattr(self.__data, key)

    def __setitem__(self, key, value):
        """Internal data fields of WreckLibrary can be accessed through dict-like syntax (we cannot use object syntax since it's used by entity references)."""
        setattr(self.__data, key, value)

    def __iter__(self):
        return self.__data.entries.iteritems()

    def __str__(self):
        return '%s(%r, %r, %d, %s, list(len=%d))' % (type(self).__name__, self.__data.basename, self.__data.defaults, self.__data.opmask, self.__data.varclass.__name__, len(self.__data.source))

    __repr__ = __str__

    def __len__(self):
        return len(self.__data.entries)


class WreckScript(object):
    name = ''
    source = None
    sanitized = None
    entry = None
    path = None
    check_canfail = False

    def __init__(self, name_gen, code_source, code_sanitized, entry, path, lib = None, uid = '', conversions = None, check_canfail = False):
        self.source, self.sanitized, self.entry, self.path = code_source, code_sanitized, entry, path
        if check_canfail and not uid.startswith('cf_'):
            self.check_canfail = True
        # name_gen = '{lib}.{uid}{0}..{N}'
        replacer = list(path)
        if conversions:
            for key, value in conversions.iteritems():
                if isinstance(value, dict):
                    replacer[key] = value.get(replacer[key])
                elif callable(value):
                    replacer[key] = value(replacer[key], entry, path)
                else:
                    replacer[key] = value # Fallback, we shouldn't ever use this
        lib_name = '<?>'
        self.name = name_gen.format(*replacer, lib = lib['basename'], uid = uid)

    def compress_entry(self, entry):
        result = ', '.join(self.compress_entry(item) if isinstance(item, list) else repr(item) for item in entry[:5])
        return '[%s%s]' % (result, ', ...' if len(entry) > 5 else '')

    def compile(self):
        return
        output = []
        source = []
        buffer = []
        for op_number, operation in enumerate(source):
            if isinstance(operation, WreckInjectionPoint):
                pass # FIXME: implement injections
            else:
                pass


# |                                                                            |
# |    COMPILER BASE CLASSES END                                               |
# +                                                                            +
#  \                                                                          /
#   +------------------------------------------------------------------------+
# endregion

# region WRECK Global Instances
#   +------------------------------------------------------------------------+
#  /                                                                          \
# +                                                                            +
# |    WRECK GLOBAL INSTANCES                                                  |
# |                                                                            |


_opcode = WreckLibrary('opcode')

_add = WreckOperation('+', lambda a, b: a+b, '+', [_opcode.store_add, 3, '{dest}', '{0}', '{1}'], associative = True)
_sub = WreckOperation('-', lambda a, b: a-b, '-', [_opcode.store_sub, 3, '{dest}', '{0}', '{1}'])
_mul = WreckOperation('*', lambda a, b: a*b, '*', [_opcode.store_mul, 3, '{dest}', '{0}', '{1}'], associative = True)
_div = WreckOperation('/', lambda a, b: a/b, '/', [_opcode.store_div, 3, '{dest}', '{0}', '{1}'])
_mod = WreckOperation('%', lambda a, b: a%b, '%', [_opcode.store_mod, 3, '{dest}', '{0}', '{1}'])
_pow = WreckOperation('**', lambda a, b: a**b, '**', [_opcode.store_pow, 3, '{dest}', '{0}', '{1}'])
_shl = WreckOperation('<<', lambda a, b: a<<b, '<<', [_opcode.assign, 2, '{dest}', '{0}'], [_opcode.val_lshift, 2, '{dest}', '{1}'])
_shr = WreckOperation('>>', lambda a, b: a<<b, '>>', [_opcode.assign, 2, '{dest}', '{0}'], [_opcode.val_rshift, 2, '{dest}', '{1}'])
_and = WreckOperation('&', lambda a, b: a&b, '&', [_opcode.store_and, 3, '{dest}', '{0}', '{1}'], associative = True)
_or  = WreckOperation('|', lambda a, b: a|b, '|', [_opcode.store_or, 3, '{dest}', '{0}', '{1}'], associative = True)
_xor = WreckOperation('^', lambda a, b: a^b, '^', [_opcode.store_and, 3, '{dest}', '{0}', '{1}'], [_opcode.val_mul, 2, '{dest}', -2], [_opcode.val_add, 2, '{dest}', '{0}'], [_opcode.val_add, 2, '{dest}', '{1}'], associative = True)
_neg = WreckOperation('neg', lambda a: -a, '(-%r)', [_opcode.store_sub, 3, '{dest}', 0, '{0}'], unary = True)
_abs = WreckOperation('abs', abs, 'abs(%r)', [_opcode.assign, 2, '{dest}', '{0}'], [_opcode.val_abs, 1, '{dest}'], unary = True)


# |                                                                            |
# |    WRECK GLOBAL INSTANCES END                                              |
# +                                                                            +
#  \                                                                          /
#   +------------------------------------------------------------------------+
# endregion

# region WRECK Convenience Functions
#   +------------------------------------------------------------------------+
#  /                                                                          \
# +                                                                            +
# |    WRECK CONVENIENCE FUNCTIONS                                             |
# |                                                                            |


def SKILLS(**argd):
    result = 0x000000000000000000000000000000000000000000
    for skill_name, value in argd.iteritems():
        result |= (value & 0xF) << (getattr(WRECK.skl, skill_name) << 2)
    return result

def ATTR(_str, _agi, _int, _cha, _lvl = 0):
    return WreckAggregateValue([('str', _str), ('agi', _agi), ('int', _int), ('cha', _cha), ('level', _lvl)])

def define_troop_upgrade(*argl):
    stack = _get_current_stack() # stack[0] points to this line, stack[1] to whatever called this function
    args = list(argl)
    try:
        if isinstance(args[0], (list, tuple)):
            args.pop(0) # Catch for old-style use, where entries list is passed as first parameter
        base = args[0]
        upg1 = args[1]
    except IndexError:
        raise WreckException('function call error in {2} at {0}:{1} - not enough arguments'.format(*stack[1]), stack[1][3].strip())
    try:
        upg2 = args[2] # Optional
    except IndexError:
        upg2 = 0
    WRECK.troop_upgrades.append((current_module(), base, upg1, upg2, '{}:{}'.format(stack[1][0], stack[1][1])))

# |                                                                            |
# |    WRECK CONVENIENCE FUNCTIONS END                                         |
# +                                                                            +
#  \                                                                          /
#   +------------------------------------------------------------------------+
# endregion

# region WRECK Module Overrides
#   +------------------------------------------------------------------------+
#  /                                                                          \
# +                                                                            +
# |    WRECK MODULE OVERRIDES                                                  |
# |                                                                            |


# These functions override their counterparts in header_items.py

weight         = lambda x: WreckAggregateValue([('weight', 0.01 * int(x * 100 + 0.5))]) # Allow weights > 63 kg and weight precision up to 0.01 kg (Warband however only displays up to 0.1 kg).
head_armor     = lambda x: WreckAggregateValue([('head', x)]) # Allow armor values > 255
body_armor     = lambda x: WreckAggregateValue([('body', x)]) # Allow armor values > 255
leg_armor      = lambda x: WreckAggregateValue([('leg', x)]) # Allow armor values > 255
difficulty     = lambda x: WreckAggregateValue([('diff', x)])
hit_points     = lambda x: WreckAggregateValue([('hp', x)])
spd_rtng       = lambda x: WreckAggregateValue([('speed', x)])
shoot_speed    = lambda x: WreckAggregateValue([('msspd', x)])
horse_scale    = lambda x: WreckAggregateValue([('size', x)])
weapon_length  = lambda x: WreckAggregateValue([('size', x)])
shield_width   = lambda x: WreckAggregateValue([('size', x)])
shield_height  = lambda x: WreckAggregateValue([('msspd', x)])
max_ammo       = lambda x: WreckAggregateValue([('qty', x)]) # Enable quantity > 255
swing_damage   = lambda d, dt: WreckAggregateValue([('swing',  (dt << 8) | (d & 255))]) # Damage is still limited to 255
thrust_damage  = lambda d, dt: WreckAggregateValue([('thrust', (dt << 8) | (d & 255))]) # Damage is still limited to 255
horse_speed    = lambda x: WreckAggregateValue([('msspd', x)])
horse_maneuver = lambda x: WreckAggregateValue([('speed', x)])
horse_charge   = lambda x: thrust_damage(x, 2) # Hardcoded blunt damage
food_quality   = lambda x: WreckAggregateValue([('head', x)])
abundance      = lambda x: WreckAggregateValue([('abundance', x)])
accuracy       = lambda x: WreckAggregateValue([('leg', x)])

get_weight = lambda y: y.get('weight', 0.0) if isinstance(y, WreckAggregateValue) else 0.25 * ((y >> 24) & 0xff)

get_head_armor    = lambda y: y.get('', 0) if isinstance(y, WreckAggregateValue) else (y & 0xff)
get_body_armor    = lambda y: y.get('', 0) if isinstance(y, WreckAggregateValue) else ((y >> 8) & 0xff)
get_leg_armor     = lambda y: y.get('', 0) if isinstance(y, WreckAggregateValue) else ((y >> 16) & 0xff)
get_difficulty    = lambda y: y.get('', 0) if isinstance(y, WreckAggregateValue) else ((y >> 32) & 0xff)
get_hit_points    = lambda y: y.get('', 0) if isinstance(y, WreckAggregateValue) else ((y >> 40) & 0xffff)
get_speed_rating  = lambda y: y.get('', 0) if isinstance(y, WreckAggregateValue) else ((y >> 80) & 0xff)
get_missile_speed = lambda y: y.get('', 0) if isinstance(y, WreckAggregateValue) else ((y >> 90) & 0x3ff)
get_weapon_length = lambda y: y.get('', 0) if isinstance(y, WreckAggregateValue) else (((y >> 70) & 0x3ff))
get_max_ammo      = lambda y: y.get('', 0) if isinstance(y, WreckAggregateValue) else ((y >> 100) & 0xff)
get_swing_damage  = lambda y: y.get('', 0) if isinstance(y, WreckAggregateValue) else ((y >> 50) & 0x3ff)
get_thrust_damage = lambda y: y.get('', 0) if isinstance(y, WreckAggregateValue) else ((y >> 60) & 0x3ff)
def get_abundance(y):
    abundance = (y >> 110) & 0xff
    return abundance if abundance else 100

# Overrides for functions and constants in header_troops.py

level = lambda value: WreckAggregateValue({'level':value})



# |                                                                            |
# |    WRECK MODULE OVERRIDES END                                              |
# +                                                                            +
#  \                                                                          /
#   +------------------------------------------------------------------------+
# endregion

# region WRECK Root Class
#   +------------------------------------------------------------------------+
#  /                                                                          \
# +                                                                            +
# |    WRECK ROOT CLASS                                                        |
# |                                                                            |


class WRECK(object):

    version = '1.1.0'

    config = WreckConfig(
        show_help = False,        # Show command line syntax help instead of doing any processing.
        use_color = True,         # Use colored output by default.
        all_tags = False,         # Do not try to imitate Native Warband compiler output by adding entity tags to everything in sight.
        test_run = False,         # Do a normal compilation run instead of a dry test run.
        wait_enter = False,       # Do not prompt user with 'Press Enter to finish' message at the end of compilation.
        report_duplicates = True, # Entities with duplicate identifiers will generate warnings if found in the module files.
        warband_module = None,    # Compile as Warband module instead of Mount&Blade module. Will auto-detect if left as None.

        reporting = WARNING, # WRECK will report all warnings and above by default.

        module_path = None, # Will be set to current folder unless specified explicitly in command line
        export_path = None, # Will be imported from module_info.py file unless specified explicitly in command line

        import_module_files = 'module_{module_name}.py',     # --> "./module_items.py"
        import_header_files = 'header_{module_name}.py',     # --> "./header_items.py"
        export_module_files = '{export_name}.{export_ext}',  # --> "./item_kinds1.txt"
        export_id_files     = 'ID_{module_name}.py',         # --> "./ID_items.txt"
        variables_file      = '{export_path}/variables.txt', # --> "./variables.txt"

        performance  = None,

        extras = WreckConfig(), # Any arguments that WRECK failed to parse will be here

        parse_module_info = True, # If WRECK cannot find module_info.py file, this will be set to False
    )

    current_module = None # TODO: decide what to do with this. Note: it is currently extensively used

    libraries = WreckConfig()

    reference_triggers = {} # Filled when importing header_triggers, used to convert trigger condition values back to human-readable strings
    reference_operations = {} # Filled when importing header_operations, used to convert operation codes back to human-readable strings

    num_weapon_proficiencies = 6 # Default value, will be overridden from header_troops

    log = WreckLogger()

    # This dict contains pre-made namespace for imported modules.
    _module_namespace = {}
    # This dict contains values that WRECK will always override when importing any module (like reg11, imod_rusty etc).
    _module_overrides = {}
    # Contains modules which have already been imported and sanitized, and thus no longer need handling.
    _module_sanitized = set()

    troop_upgrades = []
    scripting_blocks = []

    plugins = OrderedDict()
    injections = {}

    undefined_variables = set()

    @classmethod
    def initialize_wreck(cls):
        global _python_import, _wreck_import_hook
        import __builtin__
        _python_import = __builtin__.__import__
        __builtin__.__import__ = _wreck_import_hook
        sys.modules['compiler'] = imp.new_module('compiler')

    @classmethod
    def initialize_config(cls):
        for index in xrange(1, len(sys.argv)):
            option = sys.argv[index].split('=', 1)
            option[0] = option[0].lstrip('-/').lower()
            if option[0] == 'help': cls.config.show_help = True
            elif option[0] == 'test': cls.config.test_run = True
            elif option[0] == 'bw': cls.config.use_color = False
            elif option[0] == 'tag': cls.config.all_tags = True
            elif option[0] == 'wait': cls.config.wait_enter = True
            elif option[0] == 'nodupe': cls.config.report_duplicates = False
            elif option[0] == 'silent': cls.config.reporting = float('inf')
            elif option[0].startswith('critical'): cls.config.reporting = CRITICAL
            elif option[0].startswith('failure'): cls.config.reporting = FAILURE
            elif option[0].startswith('error'): cls.config.reporting = ERROR
            elif option[0].startswith('mistake'): cls.config.reporting = MISTAKE
            elif option[0].startswith('warning'): cls.config.reporting = WARNING
            elif option[0].startswith('advice'): cls.config.reporting = ADVICE
            elif option[0].startswith('notice'): cls.config.reporting = INFO
            elif option[0].startswith('detail'): cls.config.reporting = DETAILS
            elif option[0].startswith('debug'): cls.config.reporting = DEBUG
            elif option[0] == 'warband': cls.config.warband_module = True
            elif option[0] == 'mnb': cls.config.warband_module = False
            elif option[0] == 'auto': cls.config.warband_module = None
            elif len(option) > 1:
                if option[0] == 'performance':
                    if option[1].lower() in ('true', 'y', 'yes', '1'): cls.config.performance = True
                    elif option[1].lower() in ('false', 'n', 'no', '0'): cls.config.performance = False
                    else: cls.config.extras.performance = option[1]
                elif option[0] == 'module':
                    cls.config.module_path = option[1].rstrip('\\/')
                elif option[0] == 'export':
                    cls.config.export_path = option[1].rstrip('\\/')
                else:
                    setattr(cls.config.extras, option[0], option[1])
            else:
                setattr(cls.config.extras, option[0], True)

    @classmethod
    def module_files_exist(cls, *filenames):
        for filename in filenames:
            if not os.path.exists('/'.join([cls.config.module_path, filename])): return False
        return True

    @classmethod
    def validate_config(cls):
        """Security check function.

        Will make sure that module and export paths actually exist, that module_info.py file exists in module folder,
        and will also auto-detect module version (Warband or Mount&Blade) if necessary.
        """
        if cls.config.module_path is None:
            cls.config.module_path = os.getcwd().rstrip(r'\/').replace('\\', '/')
        if not os.path.exists(cls.config.module_path):
            raise WreckException('module path "{0}" does not exist'.format(cls.config.module_path))
        if not os.path.exists('/'.join([cls.config.module_path, 'module_info.py'])):
            cls.log.error('file "{0}/module_info.py" was not found at module path'.format(cls.config.module_path))
            cls.config.parse_module_info = False
        if cls.config.warband_module is None:
            cls.config.warband_module = cls.module_files_exist('module_info_pages.py', 'module_postfx.py')
        if cls.config.use_color and sys.platform.startswith('win') and 'colorama' not in sys.modules:
            cls.config.use_color = False
        sys.path.insert(0, cls.config.module_path)

    @classmethod
    def initialize_libraries(cls):

        # Core libraries (exportable)
        cls.libraries.fac       = WreckLibrary('fac', WreckFactionReference, module = 'factions', data = 'factions', export = 'factions', prefix = 'fac_', uid_generator = _uid_std(0),
                                               parser = _parse_tuple(_parse_uid, _parse_str, _parse_int, _parse_float, [(_parse_ref('fac'), _parse_float)], [_parse_str], _optional(_parse_int, 0xAAAAAA)),
                                              )
        cls.libraries.itm       = WreckLibrary('itm', WreckItemReference, module = 'items', data = 'items', export = 'item_kinds1', prefix = 'itm_', uid_generator = _uid_std(0),
                                               parser = _parse_tuple(_parse_uid, _parse_str, [(_parse_id, _parse_int)], _parse_int, _parse_int, _parse_int, _parse_aggregate(unparse_item_aggregate), _parse_int, _optional([(_parse_float, _parse_script('{lib}.{uid}(#{0}).trigger(#{2})'))], []), _optional([_parse_int], [])),
                                              )
        cls.libraries.icon      = WreckLibrary('icon', module = 'map_icons', data = 'map_icons', export = 'map_icons', prefix = 'icon_', uid_generator = _uid_std(0),
                                               parser = _parse_tuple(_parse_uid, _parse_int, _parse_id, _parse_float, _parse_int, _optional(_parse_float, 0), _optional(_parse_float, 0), _optional(_parse_float, 0), _optional([(_parse_float, _parse_script('{lib}.{uid}(#{0}).trigger(#{2})'))], []) ),
                                              )
        cls.libraries.mnu       = WreckLibrary('mnu', module = 'game_menus', data = 'game_menus', export = 'menus', prefix = 'mnu_', uid_generator = _uid_std(0),
                                               parser = _parse_tuple(_parse_uid, _parse_int, _parse_str, _parse_expect('none'), _parse_script('{lib}.{uid}(#{0}).init'), [(_parse_id, _parse_script('{lib}.{uid}(#{0}).item(#{2}).conditions'), _parse_str, _parse_script('{lib}.{uid}(#{0}).item(#{2}).consequences'), _optional(_parse_str, ''))]),
                                              )
        cls.libraries.mesh      = WreckLibrary('mesh', module = 'meshes', data = 'meshes', export = 'meshes', prefix = 'mesh_', uid_generator = _uid_std(0),
                                               parser = _parse_tuple(_parse_uid, _parse_int, _parse_id, _parse_float, _parse_float, _parse_float, _parse_float, _parse_float, _parse_float, _parse_float, _parse_float, _parse_float),
                                              )
        cls.libraries.mt        = WreckLibrary('mt', module = 'mission_templates', data = 'mission_templates', export = 'mission_templates', prefix = 'mt_', uid_generator = _uid_std(0),
                                               parser = _parse_tuple(_parse_uid, _parse_int, _parse_int, _parse_str, [(_parse_int, _parse_int, _parse_int, _parse_int, _parse_int, [_parse_int])], [(_parse_float, _parse_float, _parse_float, _parse_script('{lib}.{uid}(#{0}).trigger(#{2}).conditions'), _parse_script('{lib}.{uid}(#{0}).trigger(#{2}).consequences'))]),
                                              )
        cls.libraries.track     = WreckLibrary('track', module = 'music', data = 'tracks', export = 'music', prefix = 'track_', uid_generator = _uid_std(0),
                                               parser = _parse_tuple(_parse_uid, _parse_file('{export_path}/Music/{file}', '{warband_path}/music/{file}'), _parse_int, _parse_int),
                                              )
        cls.libraries.psys      = WreckLibrary('psys', module = 'particle_systems', data = 'particle_systems', export = 'particle_systems', prefix = 'psys_', uid_generator = _uid_std(0),
                                               parser = _parse_tuple(_parse_uid, _parse_int, _parse_id, _parse_int, _parse_float, _parse_float, _parse_float, _parse_float, _parse_float, (_parse_float, _parse_float), (_parse_float, _parse_float), (_parse_float, _parse_float), (_parse_float, _parse_float), (_parse_float, _parse_float), (_parse_float, _parse_float), (_parse_float, _parse_float), (_parse_float, _parse_float), (_parse_float, _parse_float), (_parse_float, _parse_float), (_parse_float, _parse_float, _parse_float), (_parse_float, _parse_float, _parse_float), _parse_float, _optional(_parse_float, 0), _optional(_parse_float, 0)),
                                              )
        cls.libraries.p         = WreckLibrary('p', WreckPartyReference, module = 'parties', data = 'parties', export = 'parties', prefix = 'p_', uid_generator = _uid_std(0),
                                               parser = _parse_tuple(_parse_uid, _parse_str, _parse_int, _parse_int, _parse_int, _parse_int, _parse_int, _parse_int, _parse_int, (_parse_float, _parse_float), [(_parse_int, _parse_int, _parse_int)], _optional(_parse_float, 0)),
                                              )
        cls.libraries.pt        = WreckLibrary('pt', WreckPartyTemplateReference, module = 'party_templates', data = 'party_templates', export = 'party_templates', prefix = 'pt_', uid_generator = _uid_std(0),
                                               parser = _parse_tuple(_parse_uid, _parse_str, _parse_int, _parse_int, _parse_int, _parse_int, [(_parse_int, _parse_int, _parse_int, _optional(_parse_int, 0))]),
                                              )
        cls.libraries.prsnt     = WreckLibrary('prsnt', module = 'presentations', data = 'presentations', export = 'presentations', prefix = 'prsnt_', uid_generator = _uid_std(0),
                                               parser = _parse_tuple(_parse_uid, _parse_int, _parse_int, [(_parse_float, _parse_script('{lib}.{uid}(#{0}).trigger(#{2})'))]),
                                              )
        cls.libraries.qst       = WreckLibrary('qst', module = 'quests', data = 'quests', export = 'quests', prefix = 'qst_', uid_generator = _uid_std(0),
                                               parser = _parse_tuple(_parse_uid, _parse_str, _parse_int, _parse_str),
                                              )
        cls.libraries.spr       = WreckLibrary('spr', module = 'scene_props', data = 'scene_props', export = 'scene_props', prefix = 'spr_', uid_generator = _uid_std(0),
                                               parser = _parse_tuple(_parse_uid, _parse_int, _parse_id, _parse_id, [(_parse_float, _parse_script('{lib}.{uid}(#{0}).trigger(#{2})'))]),
                                              )
        cls.libraries.scn       = WreckLibrary('scn', WreckSceneReference, module = 'scenes', data = 'scenes', export = 'scenes', prefix = 'scn_', uid_generator = _uid_std(0),
                                               parser = _parse_tuple(_parse_file('{export_path}/SceneObj/{file}.scn'), _parse_int, _parse_id, _parse_id, (_parse_float, _parse_float), (_parse_float, _parse_float), _parse_float, _parse_id, [_parse_ref('scn')], [_parse_ref('trp')], _optional(_parse_id, '0')),
                                              )
        cls.libraries.script    = WreckLibrary('script', module = 'scripts', data = 'scripts', export = 'scripts', prefix = 'script_', uid_generator = _uid_std(0),
                                               parser = _parse_tuple(_parse_uid, _parse_script('{lib}.{uid}(#{0})', check_canfail = True)),
                                              )
        cls.libraries.skl       = WreckLibrary('skl', module = 'skills', data = 'skills', export = 'skills', prefix = 'skl_', uid_generator = _uid_std(0),
                                               parser = _parse_tuple(_parse_uid, _parse_str, _parse_int, _parse_int, _parse_str),
                                              )
        cls.libraries.snd       = WreckLibrary('snd', module = 'sounds', data = 'sounds', export = 'sounds', prefix = 'snd_', uid_generator = _uid_std(0),
                                               parser = _parse_tuple(_parse_uid, _parse_int, [_parse_file('{export_path}/Sounds/{file}', '{warband_path}/Sounds/{file}')]),
                                              )
        cls.libraries.s         = WreckLibrary('s', opmask = opmask_string, module = 'strings', data = 'strings', export = 'strings', prefix = 'str_', uid_generator = _uid_std(0),
                                               parser = _parse_tuple(_parse_uid, _parse_str),
                                              )
        cls.libraries.tableau   = WreckLibrary('tableau', module = 'tableau_materials', data = 'tableaus', export = 'tableau_materials', prefix = 'tableau_', uid_generator = _uid_std(0),
                                               parser = _parse_tuple(_parse_uid, _parse_int, _parse_id, _parse_int, _parse_int, _parse_int, _parse_int, _parse_int, _parse_int, _parse_script('{lib}.{uid}(#{0})')),
                                              )
        cls.libraries.trp       = WreckLibrary('trp', WreckTroopReference, module = 'troops', data = 'troops', export = 'troops', prefix = 'trp_', uid_generator = _uid_std(0),
                                               parser = _parse_tuple(_parse_uid, _parse_str, _parse_str, _parse_int, _parse_int, _parse_int, _parse_int, [_parse_intpair], _parse_aggregate(unparse_attr_aggregate), _parse_aggregate(unparse_wp_aggregate), _parse_int, _parse_int, _optional(_parse_int, 0), _optional(_parse_str, '0'), _optional(_parse_int, 0), _optional(_parse_int, 0)),
                                              )
        if cls.config.warband_module:
            cls.libraries.ip    = WreckLibrary('ip', module = 'info_pages', data = 'info_pages', export = 'info_pages', prefix = 'ip_', uid_generator = _uid_std(0),
                                               parser = _parse_tuple(_parse_uid, _parse_str, _parse_str),
                                              )
            cls.libraries.pfx   = WreckLibrary('pfx', module = 'postfx', data = 'postfx_params', export = 'postfx', prefix = 'pfx_', uid_generator = _uid_std(0),
                                               parser = _parse_tuple(_parse_uid, _parse_int, _parse_int, (_parse_float, _parse_float, _parse_float, _parse_float), (_parse_float, _parse_float, _parse_float, _parse_float), (_parse_float, _parse_float, _parse_float, _parse_float)),
                                              )
            cls.libraries.anim  = WreckLibrary('anim', module = 'animations', data = 'animations', export = 'actions', prefix = 'anim_', uid_generator = _uid_std(0),
                                               parser = _parse_tuple(_parse_uid, _parse_int, _parse_int, _repeatable((_parse_float, _parse_id, _parse_int, _parse_int, _parse_int, _optional(_parse_int, 0), _optional((_parse_float, _parse_float, _parse_float), (0, 0, 0)), _optional(_parse_float, 0)))),
                                              )
        else:
            cls.libraries.anim  = WreckLibrary('anim', module = 'animations', data = 'animations', export = 'actions', prefix = 'anim_', uid_generator = _uid_std(0),
                                               parser = _parse_tuple(_parse_uid, _parse_int, _repeatable((_parse_float, _parse_id, _parse_int, _parse_int, _parse_int, _optional(_parse_int, 0), _optional((_parse_float, _parse_float, _parse_float), (0, 0, 0)), _optional(_parse_float, 0)))),
                                              )

        # Core libraries that don't need reference handling (exportable)
        cls.libraries._dlg      = WreckLibrary('dialog', module = 'dialogs', data = 'dialogs', export = 'conversation', extendable = False, uid_generator = _uid_dialog,
                                               parser = _parse_tuple(_parse_int, _parse_uid, _parse_script('{lib}.{uid}(#{0}).conditions'), _parse_str, _parse_uid, _parse_script('{lib}.{uid}(#{0}).consequences'), _optional(_parse_str, 'NO_VOICEOVER')),
                                              )
        cls.libraries._dlgst    = WreckLibrary('dialog_state', export = 'dialog_states', extendable = False) # Filled by dialog processor/aggregator
        cls.libraries._skin     = WreckLibrary('skin', module = 'skins', data = 'skins', export = 'skins', extendable = False, uid_generator = _uid_std(0),
                                               parser = _parse_tuple(_parse_uid, _parse_int, _parse_id, _parse_id, _parse_id, _parse_id, [(_parse_int, _parse_int, _parse_float, _parse_float, _parse_str)], [_parse_id], [_parse_id], [_parse_id], [_parse_id], [(_parse_id, _parse_int, [_parse_id], [_parse_int])], [(_parse_int, _parse_ref('snd'))], _parse_id, _parse_float, _parse_int, _parse_int, _optional([(_parse_float, _parse_int, _repeatable((_parse_float, _parse_int)))], []) ),
                                              )
        cls.libraries._trig     = WreckLibrary('trigger', module = 'triggers', data = 'triggers', export = 'triggers', extendable = False, uid_generator = _uid_trigger,
                                               parser = _parse_tuple(_parse_float, _parse_float, _parse_float, _parse_script('{lib}.{uid}(#{0}).conditions'), _parse_script('{lib}.{uid}(#{0}).consequences')),
                                              )
        cls.libraries._strig    = WreckLibrary('simple_trigger', module = 'simple_triggers', data = 'simple_triggers', export = 'simple_triggers', extendable = False, uid_generator = _uid_strigger,
                                               parser = _parse_tuple(_parse_float, _parse_script('{lib}.{uid}(#{0})')),
                                              )

        # Optional WRECK libraries (exportable to special locations)
        if cls.module_files_exist('module_ui_strings.py'):
            cls.libraries.uistr = WreckLibrary('uistr', module = 'ui_strings', data = 'ui_strings', export = 'Languages/en/ui', export_ext = 'csv', uid_generator = _uid_std(0),
                                               parser = _parse_tuple(_parse_uid, _parse_str),
                                              )
        if cls.module_files_exist('module_user_hints.py'):
            cls.libraries.hint  = WreckLibrary('hint', module = 'user_hints', data = 'user_hints', export = 'Languages/en/hints', export_ext = 'csv', extendable = False, uid_generator = _uid_index,
                                               parser = _parse_tuple(_parse_str),
                                              )
        if cls.module_files_exist('module_item_modifiers.py'):
            cls.libraries.imod  = WreckLibrary('imod', WreckItemModifierReference, module = 'item_modifiers', data = 'item_modifiers', export = 'Data/item_modifiers', prefix = 'imod_', uid_generator = _uid_std(0),
                                               parser = _parse_tuple(_parse_uid, _parse_str, _parse_float, _parse_float),
                                              )
        else:
            cls.libraries.imod  = WreckLibrary('imod', WreckItemModifierReference, prefix = 'imod_', source = DEFAULT_ITEM_MODIFIERS, uid_generator = _uid_std(0),
                                               parser = _parse_tuple(_parse_uid, _parse_str, _parse_float, _parse_float),
                                              )
        cls.libraries.imodbit   = WreckLibrary('imodbit', prefix = 'imodbit_')

        # Libraries for variable/string support (quick_strings is exportable, globals need special handling which cannot be provided by standard pipeline)
        cls.libraries.l         = WreckLibrary('l', opmask = opmask_local_variable, defaults = { 'static': False }, prefix = ':')
        cls.libraries.g         = WreckLibrary('g', opmask = opmask_variable, defaults = { 'static': False }, prefix = '$')
        #cls.libraries.registers = WreckLibrary('reg', defaults = { 'static': False })
        #cls.libraries.qstr      = WreckLibrary('qstr', defaults = { 'static': False }, export = 'quick_strings')

        cls.libraries._intreg   = WreckLibrary('reg', defaults = { 'static': False })
        cls.libraries._posreg   = WreckLibrary('pos')
        cls.libraries._strreg   = WreckLibrary('sreg')
        cls.libraries._qstr     = WreckLibrary('qstr', defaults = { 'static': False }, export = 'quick_strings')
        cls.libraries._opcode   = _opcode

        if cls.config.all_tags:
            cls.libraries.fac['opmask'] = tag_faction << op_num_value_bits
            cls.libraries.itm['opmask'] = tag_item << op_num_value_bits
            cls.libraries.icon['opmask'] = tag_map_icon << op_num_value_bits
            cls.libraries.mnu['opmask'] = tag_menu << op_num_value_bits
            cls.libraries.mesh['opmask'] = tag_mesh << op_num_value_bits
            cls.libraries.mt['opmask'] = tag_mission_tpl << op_num_value_bits
            cls.libraries.track['opmask'] = tag_track << op_num_value_bits
            cls.libraries.psys['opmask'] = tag_particle_sys << op_num_value_bits
            cls.libraries.p['opmask'] = tag_party << op_num_value_bits
            cls.libraries.pt['opmask'] = tag_party_tpl << op_num_value_bits
            cls.libraries.prsnt['opmask'] = tag_presentation << op_num_value_bits
            cls.libraries.qst['opmask'] = tag_quest << op_num_value_bits
            cls.libraries.spr['opmask'] = tag_scene_prop << op_num_value_bits
            cls.libraries.scn['opmask'] = tag_scene << op_num_value_bits
            cls.libraries.script['opmask'] = tag_script << op_num_value_bits
            cls.libraries.skl['opmask'] = tag_skill << op_num_value_bits
            cls.libraries.snd['opmask'] = tag_sound << op_num_value_bits
            cls.libraries.tableau['opmask'] = tag_tableau << op_num_value_bits
            cls.libraries.trp['opmask'] = tag_troop << op_num_value_bits

        cls._module_namespace.update((name, lib) for (name, lib) in cls.libraries.__dict__.iteritems() if not name.startswith('_'))

        cls._module_namespace.update({
            'ATTR': ATTR,
            'SKILLS': SKILLS,
            'define_troop_upgrade': define_troop_upgrade,
            'inject': inject,
            'num_weapon_proficiencies': cls.num_weapon_proficiencies,
        })

        cls._module_overrides.update({
            'weight': weight,
            'head_armor': head_armor,
            'body_armor': body_armor,
            'leg_armor': leg_armor,
            'difficulty': difficulty,
            'hit_points': hit_points,
            'spd_rtng': spd_rtng,
            'shoot_speed': shoot_speed,
            'horse_scale': horse_scale,
            'weapon_length': weapon_length,
            'shield_width': shield_width,
            'shield_height': shield_height,
            'max_ammo': max_ammo,
            'swing_damage': swing_damage,
            'thrust_damage': thrust_damage,
            'horse_speed': horse_speed,
            'horse_maneuver': horse_maneuver,
            'horse_charge': horse_charge,
            'food_quality': food_quality,
            'abundance': abundance,
            'accuracy': accuracy,
            'level': level,
            'reg': lambda index: getattr(cls.libraries._intreg, 'reg%d' % index),
            'pos': lambda index: getattr(cls.libraries._posreg, 'pos%d' % index),
            'upgrade': define_troop_upgrade,
            'upgrade2': define_troop_upgrade,
            'get_head_armor': get_head_armor,
            'get_body_armor': get_body_armor,
            'get_leg_armor': get_leg_armor,
            'get_difficulty': get_difficulty,
            'get_hit_points': get_hit_points,
            'get_speed_rating': get_speed_rating,
            'get_missile_speed': get_missile_speed,
            'get_weapon_length': get_weapon_length,
            'get_max_ammo': get_max_ammo,
            'get_swing_damage': get_swing_damage,
            'get_thrust_damage': get_thrust_damage,
            'get_abundance': get_abundance,
        })

        # Initialize register modules
        for index in xrange(128):
            setattr(cls.libraries._intreg, 'reg%d' % index, opmask_register | index)
            cls._module_overrides['reg%d' % index] = cls.libraries._intreg('reg%d' % index)
            setattr(cls.libraries._posreg, 'pos%d' % index, index)
            cls._module_overrides['pos%d' % index] = cls.libraries._posreg('pos%d' % index)
            setattr(cls.libraries._strreg, 's%d' % index, index)
            cls._module_overrides['s%d' % index]   = cls.libraries._strreg('s%d' % index)
        cls.libraries._intreg['extendable'] = False # Do not allow any register declarations after this point
        cls.libraries._posreg['extendable'] = False # Do not allow any position declarations after this point
        cls.libraries._strreg['extendable'] = False # Do not allow any string register declarations after this point

        for index in xrange(3, 32):
            for attr in ('str', 'agi', 'int', 'cha'):
                cls._module_overrides['%s_%d' % (attr, index)] = WreckAggregateValue({attr: index})

        cls._module_namespace['WRECK'] = cls
        cls._module_namespace.update(cls._module_overrides)

        sys.modules['compiler'].update(cls._module_namespace)

    @classmethod
    def preload_headers(cls):
        for module in ('common', 'operations', 'animations', 'dialogs', 'factions', 'game_menus', 'ground_types',
                       'item_modifiers', 'items', 'map_icons', 'meshes', 'mission_templates', 'mission_types', 'music',
                       'particle_systems', 'parties', 'postfx', 'presentations', 'quests', 'scene_props', 'scenes',
                       'skills', 'skins', 'sounds', 'strings', 'tableau_materials', 'terrain_types', 'triggers', 'troops'):
            header_file = '/'.join([cls.config.module_path, cls.config.import_header_files.format(module_name = module)])
            if not os.path.exists(header_file):
                cls.log.debug('Failed to preload header file {0}'.format(header_file))
                continue
            try:
                _wreck_import_hook('header_{0}'.format(module))
                cls.log.details('Successfully preloaded header file {0}'.format(header_file))
            except Exception:
                pass

    @classmethod
    def initialize_module(cls):
        import module_info
        data = module_info.__dict__
        if WRECK.config.export_path is None:
            current_dir = os.getcwd()
            os.chdir(cls.config.module_path)
            cls.config.export_path = os.path.abspath(data['export_dir'].rstrip(r'\/')).replace('\\', '/')
            os.chdir(current_dir)
        if 'write_id_files' in data:
            value = data['write_id_files']
            if isinstance(value, str) and ('%s' in value):
                value = value.replace('%s', '{module_name}')
            cls.config.export_id_files = value
        if ('show_performance_data' in data) and (cls.config.performance is None):
            cls.config.performance = data['show_performance_data']
        if 'export_filename' in data:
            value = data['export_filename']
            if isinstance(value, str) and ('%s' in value):
                if value.endswith('.txt'): value = value[:-4] + '.{export_ext}'
                value = value.replace('%s', '{export_name}')
            cls.config.export_module_files = value

    @classmethod
    def validate_module(cls):
        if cls.config.export_path is None: raise WreckException('export path not defined by module_info.py or command line options')
        if not os.path.exists(cls.config.export_path): raise WreckException('export path "{0}" does not exist'.format(cls.config.export_path))
        module_ini = '/'.join([cls.config.export_path, 'module.ini'])
        if not os.path.exists(module_ini): cls.log.warning('could not find {0}, are you sure it is correct export destination?'.format(module_ini))
        variables_txt = cls.config.variables_file.format(module_path = cls.config.module_path, export_path = cls.config.export_path)
        if os.path.exists(variables_txt):
            try:
                with open(variables_txt, 'r') as f:
                    variables = filter(lambda st: st, map(lambda st: st.strip(), f.readlines()))
                    # FIXME: use this data
            except IOError as e:
                cls.log.error('I/O error trying to read {0} file: {1}'.format(variables_txt, e.message))
        if not cls.config.test_run:
            tmp_path = '/'.join([cls.config.export_path, '.tmpwreck'])
            try:
                with open(tmp_path, 'w') as f:
                    f.write('test')
                with open(tmp_path, 'r') as f:
                    if f.read() != 'test':
                        raise IOError('data mismatch, read/write check failed')
            except IOError as e:
                cls.log.error('export path is not writeable: %s' % e.message)
            finally:
                if os.path.exists(tmp_path):
                    os.remove(tmp_path)

    @classmethod
    def load_module_data(cls):
        for library in cls.libraries:
            if not library['module']: continue
            module = _wreck_import_hook('module_{0}'.format(library['module']))
            library['source'] = module.__dict__[library['data']]

    @classmethod
    def apply_plugins(cls):
        pass # TODO: implement

    @classmethod
    def validate_module_data(cls):
        for library in cls.libraries:
            with library as lib_data:
                if lib_data.source and lib_data.parser:
                    sanitized = []
                    index = 0
                    norm_index = 0
                    while index < len(lib_data.source):
                        entry = lib_data.source[index]
                        if isinstance(entry, WreckInjectionPoint):
                            # TODO: Handle injection
                            index += 1
                            continue
                        try:
                            uid = lib_data.uid_generator(entry, norm_index)
                            parsed = lib_data.parser(lib_data.source, index, library = library, entry = entry, uid = uid)
                            sanitized.append(parsed[0])
                        except WreckParserException as e:
                            WRECK.log.error('syntax error in {0} entry #{1} "{2}": {3}\nentry source: {4!r}\npath to error: {5!r}'.format(lib_data.basename, norm_index, uid, e.formatted(), entry, e.error_path))
                        index += 1
                        norm_index += 1
                    lib_data.sanitized = sanitized
                    WRECK.log.details('library {0!r} parsed.'.format(library))

    @classmethod
    def resolve_references(cls):
        for library in cls.libraries:
            with library as lib_data:
                if lib_data.extendable and lib_data.sanitized:
                    for index in xrange(len(lib_data.sanitized)):
                        entry = lib_data.sanitized[index]
                        try:
                            setattr(library, internal_identifier(lib_data.uid_generator(entry, index)), index)
                        except Exception:
                            raise WreckException('failed to assign reference %r' % lib_data.uid_generator(entry, index), formatted_exception())
                    #lib_data.extendable = False
        WreckVariable.force_resolution = True

    @classmethod
    def apply_troop_upgrades(cls):
        for module, base, upg1, upg2, ref in cls.troop_upgrades:
            if module is None: module = '<wreck>'
            with current_module(module):
                if not isinstance(base, WreckVariable): base = cls.libraries.trp(base, ref)
                if not isinstance(upg1, WreckVariable): upg1 = cls.libraries.trp(upg1, ref)
                if upg2 and not(isinstance(upg2, WreckVariable)): upg2 = cls.libraries.trp(upg2, ref)
            trp_index = int(base)
            if not base.is_forced:
                with cls.libraries.trp as trp_data:
                    troop_tuple = trp_data.sanitized[trp_index]
                    troop_tuple[14] = upg1
                    troop_tuple[15] = upg2

    @classmethod
    def compile_scripts(cls):
        for script in cls.scripting_blocks:
            script.compile()

# |                                                                            |
# |    WRECK ROOT CLASS END                                                    |
# +                                                                            +
#  \                                                                          /
#   +------------------------------------------------------------------------+
# endregion

# ??? TODO: variable forced resolution

# DONE: use WreckModule (current_module())
# DONE: add detail to _parse_script, collect data blocks to be parsed
# DONE: deal with encodings in imported module files
# TODO: enhance script parser (operations, operands)

# TODO: implement plugins
# TODO: implement multiple paths in config (wreck_path, game_path, module_path, export_path, header_path, id_path)
# TODO: implement simplified argument processing
# DONE: add operations library, replace some WRECK constants with values from this lib, update lib at import
# TODO: add module constants library, replace some WRECK constants with values from this lib, update lib at import
# TODO: more detail for WreckAggregateValue, make it typed
# TODO: convert some classes to __slots__ to decrease memory footprint

# Workflow:
#
# CANCELLED: 1. Load all header files, provide own replacements both in header file namespace and compiler's own.
# DONE: 1. Hijack import of header files, override some resulting data with WRECK values.
# MOSTLY DONE: 2. Detect module version (M&B or Warband), determining the list of EntityLibraries and methods to use.
# DONE: 2. Prepare shared globals namespace for module files.
# DONE: 3. To optimize reference substitution, ALLOW loading ID files, but replace values with WRECK references.
#          However these references should be "weak", i.e. they might end up undefined and this should not cause error.
# DONE: 3. Prepare empty namespaces for ID files.
# DONE: 4. For each module file:
# DONE: 4.1. Load module source. Compile (?).
# DONE: 4.2. Repeatedly attempt to execute module in separate namespace, introducing missing references.
# DONE: 4.3. On successful execution, export resulting tuples into WarbandEntity.source property.
# 5. For each plugin file:
# 5.1. Load plugin source. Compile (?).
# 5.2. Extend existing entries with plugin data.
# 5.3. Load plugin injections into WRECK.
# DONE: 6. For each entity:
# DONE: 6.1. Check entity sources for syntax errors, processing injections along the way.
# DONE: 6.2. Evaluate entity references.
# DONE: 6.3. Link entity libraries to sources so property references can be resolved.
# AFTER SCRIPTS ARE COMPILED 7. Allocate references for global variables and quick strings.
# DONE: 8. Allocate references for game entities.
# CANCELLED, WORKFLOW CHANGED 9. Check for any references with undefined value.
# DONE: 10. Run main compilation preprocessor.
# 11. For each plugin:
# 11.1. Run plugin compilation preprocessor if defined (may create code injections).
# 12. For each entity:
# 12.1. Run entity processor on it's sources.
# 12.1.1. Handle code-level injections from plugins.
# 12.2. Run entity aggregator to generate resulting output.
# 13. Run main compilation postprocessor (compile dialog states, quick strings, globals).
# 14. For each exportable entity:
# 14.1. Export compiled data, creating files and directories as necessary.
# 15. For each exportable entity with ID files:
# 15.1. Generate, sort and export ID file for compatibility mode.

# Possible solutions:
#
# DONE: 4. Remake parser entries, these should include validators instead of declarators, making parsing more streamlined.
# IMPOSSIBLE: 5. Since we're virtualizing import of module files, can we finally link entries to line numbers?
# DONE FOR MODULE ONLY ATM: 6. Manage code injections gracefully on the fly instead of a separate pass?
# PARTIALLY DONE: 7. Trace plugin that injected current code? Inherit list() with own class, linking back to file?
# 8. Clearly separate module-level and code-level injections? Still need to maintain old syntax though.
# IMPOSSIBLE: 9. Streamline steps 4, 5 and 6?
# 10. Expand exception classes in more detail!

if __name__ == '__main__':
    print current_module()
    with current_module('level1'):
        print current_module()
        with current_module('level2'):
            print current_module()
        print current_module()
    print current_module()

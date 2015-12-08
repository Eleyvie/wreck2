#!/usr/bin/env python2.5
# -*- coding: utf-8 -*-

"""wreck.compile

File created by lav on 21.11.15 at 11:19.
Email: alex@lomskih.net
"""

__version__ = "$Revision$"
# $Source$

import pdb

import sys
sys.dont_write_bytecode = True
from pprint import pprint
from wreck import *

compiler_exit_code = 0

if __name__ == '__main__':
    WRECK.config.module_path = 'wb_1166'
    WRECK.config.export_path = 'compiled'
    WRECK.config.wait_enter = True
    try:
        WRECK.initialize_wreck()
        WRECK.initialize_config()
        if WRECK.config.show_help:
            print WRECK_SYNTAX_HELP_TEXT.format(file = sys.argv[0], version = WRECK.version)
            sys.exit(0)
        WRECK.validate_config()
        WRECK.initialize_libraries()
        WRECK.preload_headers()
        WRECK.initialize_module()
        WRECK.validate_module()

        WRECK.load_module_data()      # load module files and process them
        #WRECK.apply_plugins()         # apply plugin effects (extend module data, prepare injections)
        WRECK.validate_module_data()  # validate module data (parse all entries, apply injections)
        WRECK.resolve_references()    # assign all references to their actual values
        # Data entry modifications are no longer allowed after this point
        WRECK.apply_troop_upgrades()  # Replace placeholders in troop definitions with actual upgrade paths accumulated by this point
        WRECK.compile_scripts()       # Compile all script objects
        #WRECK.run_preprocessors()     # run WRECK main preprocessor and all plugin preprocessors
        #WRECK.process_module_data()   # convert module data to Warband text format, compile code, resolve code-level injections, resolve expressions
        #WRECK.aggregate_module_data() # format compiled data to export-ready text
        #if not WRECK.errors:
        #    WRECK.export_module_files() # export compiled module to destination folder, export ID files if necessary

    except WreckException as e:
        print 'FAIL!'
        print e.formatted()
        exit(1)

    for severity in range(ADVICE):
        print('SEVERITY {0}:'.format(severity))
        print(WRECK.log.format_messages(severity))
    with open('compiler.log', 'w+') as f:
        for severity in range(EVERYTHING):
            f.write('SEVERITY {0}:'.format(severity))
            f.write('\n')
            f.write(WRECK.log.format_messages(severity))
            f.write('\n')

    #print repr(WRECK.libraries.itm['source'][7])
    #print WRECK.libraries.itm.spice.references
    #print WRECK.libraries.skl.riding.list_references()

    #pdb.set_trace()


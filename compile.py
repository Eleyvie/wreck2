#!/usr/bin/env python2.5
# -*- coding: utf-8 -*-

"""wreck.compile

File created by lav on 21.11.15 at 11:19.
Email: alex@lomskih.net
"""

__version__ = "$Revision$"
# $Source$

import sys
sys.dont_write_bytecode = True
import time

timers = []

if __name__ == '__main__':

    timers.append(time.time())

    import logging
    logging.basicConfig(filename = 'compile.log', filemode = 'w+', format = '%(name)s: %(message)s', level = logging.DEBUG)
    from wreck import *

    compiler_exit_code = 0

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
        WRECK.initialize_module()
        WRECK.validate_module()
        WRECK.preload_headers()

        timers.append(time.time())

        WRECK.load_module_data()      # load module files and process them

        timers.append(time.time())

        WRECK.apply_plugins()         # apply plugin effects (extend module data, prepare injections)

        timers.append(time.time())

        WRECK.validate_module_data()  # validate module data (parse all entries, apply injections)

        timers.append(time.time())

        WRECK.resolve_references()    # assign all references to their actual values

        timers.append(time.time())

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

    timers.append(time.time())

    from pprint import pprint
    pprint(WRECK.issues.__dict__)
    print
    print 'INIT     : %.03f sec.' % (timers[1] - timers[0])
    print 'LOAD     : %.03f sec.' % (timers[2] - timers[1])
    print 'PLUGINS  : %.03f sec.' % (timers[3] - timers[2])
    print 'PARSE    : %.03f sec.' % (timers[4] - timers[3])
    print 'REFERENCE: %.03f sec.' % (timers[5] - timers[4])
    print 'CLOSING  : %.03f sec.' % (timers[6] - timers[5])
    print

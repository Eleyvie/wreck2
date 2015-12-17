#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""WRECK >> example_argparse

File created by lav on 12/17/15 at 3:40 PM.
Email: Aliaksandr_Lomski@epam.com
"""

__version__ = "$Revision$"
# $Source$

import sys
sys.dont_write_bytecode = True



class WreckCmdlineParser(object):
    __options = None
    __arguments = None
    __extras = None
    __initialized = False

    class WreckCmdlineOption(object):
        __slots__ = ('name', 'args', 'value', 'help', 'parsed')

        def __init__(self, _name, _help, _default = None, **args):
            self.name = _name
            self.value = _default
            self.help = _help
            self.args = args
            self.parsed = False

    class WreckCmdlineArgument(object):
        __slots__ = ('name', 'argname', 'value', 'validator', 'help', 'parsed')

        def __init__(self, name, help, default = None, validator = None, argname = None):
            self.name = name
            self.help = help
            self.argname = name if argname is None else argname
            self.value = default
            self.validator = validator
            self.parsed = False

    def __init__(self):
        self.__options = {}
        self.__arguments = {}
        self.__extras = {}
        self.__initialized = True
        self.add_option('help', 'show this help message', False, help = True)

    def add_option(self, _name, _help, default = None, **args):
        self.__options[_name] = self.WreckCmdlineOption(_name, _help, default, **args)

    def add_argument(self, name, help, default = None, validator = None, argname = None):
        self.__arguments[name] = self.WreckCmdlineArgument(name, help, default, validator, argname)

    def parse(self, args = None):
        if args is None: args = sys.argv[1:]
        for argument in args:
            argument = argument.lstrip('-/')
            duplicate = False
            try:
                argname, value = argument.split('=', 1)
                found = None
                for arg in self.__arguments.itervalues():
                    if arg.argname.startswith(argname):
                        if found:
                            duplicate = True
                        found = arg
                if found and not duplicate:
                    if not found.validator or found.validator(value):
                        found.value = value
                        found.parsed = True
                    else:
                        print 'illegal argument value'
                else:
                    self.__extras[argname] = value
            except ValueError:
                found = value = None
                for opt in self.__options.itervalues():
                    for arg, argval in opt.args.iteritems():
                        if arg.startswith(argument):
                            if found and ((found != opt) or (value != argval)):
                                duplicate = True
                            found, value = opt, argval
                if found and not duplicate:
                    found.value = value
                    found.parsed = True
                else:
                    self.__extras[argument] = True

    def __getattr__(self, item):
        if item in self.__arguments:
            return self.__arguments[item].value
        if item in self.__options:
            return self.__options[item].value
        if item in self.__extras:
            return self.__extras[item]
        return None

    def __setattr__(self, item, value):
        if not self.__initialized:
            object.__setattr__(self, item, value)
        elif item in self.__arguments:
            self.__arguments[item].value = value
        elif item in self.__options:
            self.__options[item].value = value
        else:
            self.__extras[item] = value

    def __repr__(self):
        result = []
        result.append('Arguments:')
        for arg in self.__arguments.itervalues():
            if arg.parsed: result.append('  %s = %r' % (arg.name, arg.value))
        result.append('Options:')
        for opt in self.__options.itervalues():
            if opt.parsed: result.append('  %s = %r' % (opt.name, opt.value))
        result.append('Unparsed extras:')
        for k,v in self.__extras.iteritems(): result.append('  %s = %r' % (k, v))
        return '\n'.join(result)


if __name__ == '__main__':
    parser = WreckCmdlineParser()
    parser.add_option('test_run', 'perform a test run without creating output files', False, test_run = True)
    parser.add_option('use_color', 'use colored or b&w compiler output', None, colored = True, use_color = True, bw = False)
    parser.add_option('all_tags', 'use tags for all entities for better output match', False, tags = True, all_tags = True)
    parser.add_option('wait_enter', 'wait for user input after compilation', False, wait = True)
    parser.add_option('report_duplicates', 'report all duplicate entries', True, nodupes = False)
    parser.add_option('reporting', 'determine reporting level', 2, verbose = 0, notices = 0, notifications = 0, advices = 1, warnings = 2, mistakes = 3, errors = 4, silent = 5)
    parser.add_option('warband_module', 'parse as Warband module', None, warband = True, mnb = False, autodetect = None)
    parser.add_option('performance', 'show performance data after compilation', False, performance = True)
    parser.add_argument('module_path', 'path to look for module files', argname = 'module_path')
    parser.add_argument('export_path', 'path for compiled module files', argname = 'export_path')
    parser.add_argument('game_path', 'path where game executable is located', argname = 'game_path')
    parser.add_argument('id_path', 'path to import ID files from', argname = 'id_path')
    parser.add_argument('header_path', 'path to import header files from', argname = 'header_path')
    parser.parse()
    parser.parse_module_info = True
    print repr(parser)

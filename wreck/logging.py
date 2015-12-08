#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""WRECK >> logging

File created by lav on 11/26/15 at 11:26 AM.
Email: Aliaksandr_Lomski@epam.com
"""

__version__ = "$Revision$"
# $Source$

import sys
sys.dont_write_bytecode = True
import time


DEBUG    = 10 # Technical message about compiler's internal proceedings.
DETAILS  = 15 # Informational message about minor events during compilation. Everything is ok.
INFO     = 20 # General informational message. Everything is ok.
ADVICE   = 25 # Not an error, but WRECK still advises to change something to improve readability, portability etc.
WARNING  = 30 # Not necessarily an error, but has the potential to become such.
MISTAKE  = 35 # Most likely an error unless it's some trickery that WRECK cannot recognize. Module is still compilable.
ERROR    = 40 # An error that makes it impossible to compile the module, but doesn't stop the compilation.
FAILURE  = 45 # An error that prevents the compilation from completing.
CRITICAL = 50 # An error within WRECK code.

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

    def format_messages(self, severity, prefix = '* ', offset = 2, format = '{timestamp} - {message}', line_width = None):
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

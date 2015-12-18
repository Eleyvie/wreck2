#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""WRECK >> test

File created by lav on 11/26/15 at 11:53 AM.
Email: Aliaksandr_Lomski@epam.com
"""

__version__ = "$Revision$"
# $Source$

import sys
sys.dont_write_bytecode = True

import inspect
from inspect import currentframe as inspect_currentframe, getmembers as inspect_getmembers

def get_caller_info():
    frame_name = frame_l0 = frame_l1 = frame_l2 = frame_gv = None
    frame_line = 0
    try:
        frame_l0  = inspect_currentframe()
        frame_l1  = dict(inspect_getmembers(frame_l0))
        print frame_l1
        frame_l1 = frame_l1['f_back']
        frame_l2  = dict(inspect_getmembers(frame_l1))
        print frame_l2
        frame_l2 = frame_l2['f_back']
        frame_gv = dict(inspect_getmembers(frame_l2))
        print frame_gv
        frame_gv = frame_gv['f_globals']
        frame_line = frame_l2.f_lineno
        frame_name = frame_gv['__name__']
    finally:
        del frame_l0
        del frame_l1
        del frame_l2
        del frame_gv
    return frame_name, frame_line

def get_execution_stack():
    return map(lambda i: (i[1], i[2], i[3], i[4][0]), inspect.stack())[1:]

    stack = []
    frame = inspect_currentframe()
    while frame:
        if frame.f_globals is frame.f_locals:
            func = None
        else:
            func = '%s()' % frame.f_code.co_name
        stack.append((frame.f_globals.get('__name__'), frame.f_globals.get('__file__'), frame.f_lineno))
        previous = frame.f_back
        del frame
        frame = previous
    return reversed(stack)

# Testing

def subtester2():
    return get_execution_stack()

def subtester():
    return subtester2()

class descriptor(object):
    func = None
    def __init__(self, func): self.func = func
    def _decor(self, *argl, **argd): return self.func(owner, *argl, **argd)
    def __get__(self, obj, owner = None, *argl, **argd):
        print 'get', obj, owner
        print argl
        print argd
        return self._decor

class T(object):
    @descriptor
    def tralala(self, param):
        print 'tralala', self, param


if __name__ == '__main__':
    a = subtester()
    from pprint import pprint
    pprint(a)


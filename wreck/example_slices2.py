#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""WRECK >> example_slices2

File created by lav on 12/2/15 at 4:39 PM.
Email: Aliaksandr_Lomski@epam.com
"""

__version__ = "$Revision$"
# $Source$

import sys
sys.dont_write_bytecode = True


class SubList(object):

    source = None
    index = None

    def __init__(self, source, index):
        self.source = source
        self.index = index

    def __getitem__(self, key):
        return SubList(self.source[self.index], key)

    def __setitem__(self, key, value):
        self.source[self.index][key] = value

data = [
    [[11,12,13], [14,15,16], [17,18,19]],
    [[21,22,23], [24,25,26], [27,28,29]],
    [[31,32,33], [34,35,36], [37,38,39]],
    [[41,42,43], [44,45,46], [47,48,49]],
    [[51,52,53], [54,55,56], [57,58,59]],
    [[61,62,63], [64,65,66], [67,68,69]],
    [[71,72,73], [74,75,76], [77,78,79]],
    [[81,82,83], [84,85,86], [87,88,89]],
    [[91,92,93], [94,95,96], [97,98,99]],
]

subdata = SubList(data, 1)
print subdata

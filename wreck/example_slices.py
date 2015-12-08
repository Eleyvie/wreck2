#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""W.R.E.C.K..example_slices.py

File created by lav on 23.11.15 at 14:10.
Email: Aliaksandr_Lomski@epam.com
"""

__version__ = "$Revision$"
# $Source$

import sys
from traceback import format_exc

def list_slice_generator(source, items):
    def _generator():
        resolved = source if (type(source) == list) else list(source)
        for item in items:
            if isinstance(item, slice):
                sublist = resolved[item]
                for i in sublist: yield i
            else:
                yield resolved[item]
    return _generator

class ListSlice(object):
    source = None
    items = None
    def __init__(self, source_list, items):
        self.source = source_list
        self.items = items
    def __iter__(self):
        return list_slice_generator(self.source, self.items)()

class FilteredListSearch(object):

    source = None
    filters = None

    def __init__(self, source = None, filters = []):
        self.source = source
        self.filters = filters

    def __getitem__(self, keys):
        if not isinstance(keys, tuple): keys = (keys, )
        return FilteredListSlice(self, keys)
    def __setitem__(self, keys, value):
        if not isinstance(keys, tuple): keys = (keys, )
        return FilteredListSlice(self, keys).assign(value)

    def find_all(self, filter = None):
        if filter is None: return self
        pass
    def find_first(self):
        pass
    def find_last(self):
        pass

    def insert_before(self):
        pass
    def insert_after(self):
        pass

class FilteredListJoined(object):
    pass

class FilteredListSlice(object):
    source = None
    items = None

    def __init__(self, source, items):
        self.source = source
        self.items = items if (type(items) == tuple) else (items, )

    def __resolve_items(self, data = [], items = None):
        result = []
        datalen = len(data)
        if items is None: items = self.items
        for item in items:
            if isinstance(item, slice):
                a, b, c = item.start, item.stop, item.step
                if a is None: a = 0
                elif a < 0: a = datalen - a
                if b is None: b = datalen
                elif b < 0: b = datalen - b
                if c is None: c = 1
                result.extend(range(max(a, 0), min(datalen, b), c))
            elif item < datalen:
                result.append(item)
        return result

    def __iter__(self):
        items = self.items
        def _generator():
            source_iter = iter(self.source)
            try:
                while True:
                    source_item = source_iter.next()
                    if not isinstance(source_item, list): raise TypeError('cannot slice') # TODO: elaborate
                    elements = [source_item[el] for el in self.__resolve_items(source_item)]
                    for el in elements:
                        yield el
            except StopIteration:
                pass
        return _generator()

    def __getitem__(self, keys):
        if not isinstance(keys, tuple): keys = (keys,)
        return FilteredListSlice(self, keys)

    def __setitem__(self, keys, value):
        if isinstance(value, FilteredListSlice): return
        if not isinstance(keys, tuple): keys = (keys,)
        for source_item in self:
            indices = self.__resolve_items(source_item, keys)
            for index in indices:
                source_item[index] = value

    def __setslice__(self, i, j, sequence):
        if i == 0: i = None
        if j == sys.maxsize: j = None
        self.__setitem__(slice(i, j), sequence)

    def __iadd__(self, other):
        for source_item in self.source:
            indices = self.__resolve_items(source_item)
            for index in indices:
                print 'source item =', source_item, 'index =', index, 'other =', other
                print id(source_item)
                try: source_item[index] = source_item[index] + other
                except: print format_exc()
                print id(source_item)
        return self

test_source = [
    [1, 2, 3, 4, [5, 6, 7], [[10, 11], [20, 21], [30, 31]]],
    [4, 8, 2, 4, [8, 2, 0], [[40, 41], [50, 51], [60, 61]]],
    [2, 9, 1, 7, [5, 4, 9], [[70, 71], [80, 81]]],
]

if __name__ == '__main__':
    pass

a = FilteredListSlice(test_source, (5, ))
b = FilteredListSlice(a, (slice(1,None), ))

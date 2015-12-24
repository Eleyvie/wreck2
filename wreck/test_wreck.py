#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""mnb.test_compiler.py

File created by lav on 20.11.15 at 16:49.
Email: Aliaksandr_Lomski@epam.com
"""

__version__ = "$Revision$"
# $Source$

import sys
sys.dont_write_bytecode = True

import unittest
import core as compiler


class TestWreckInternals(unittest.TestCase):

    def test_parse_int_for_legal_atoms(self):
        self.assertEquals(compiler.parse_int(-11), -11)
        self.assertEquals(compiler.parse_int(56.7), 56)
        self.assertEquals(compiler.parse_int('82'), 82)

    def test_parse_int_for_illegal_atoms(self):
        self.assertRaises(Exception, compiler.parse_int, 'abc')

    def test_parse_int_recursive(self):
        source = (7, ['345', 11.2], ([1, 2], -1))
        expect = [7, [345, 11], [[1, 2], -1]]
        result = compiler.parse_int(source)
        self.assertEquals(result, expect)


class TestWreckOperationClass(unittest.TestCase):

    def test_wreck_operations(self):
        self.assertEquals(compiler.maths.wo_add(4, 11), 15)
        self.assertEquals(compiler.maths.wo_mul.text % (4, 11), '(4 * 11)')
        op_count, code = compiler.maths.wo_shl.compile(10, 8, 1)
        self.assertEquals(op_count, 2)
        self.assertEquals(code, [compiler.assign, 2, 10, 8, compiler.val_lshift, 2, 10, 1])
        op_count, code = compiler.maths.wo_xor.compile(5, 11, 4)
        self.assertEquals(op_count, 4)


class TestWreckVariableBasics(unittest.TestCase):

    class MockModule(object):
        basename = None
        source = None
        def __init__(self, name = 'mockmodule'): self.basename = name
        def __enter__(self): return self
        def __exit__(self, exc_type, exc_val, exc_tb): pass
        def __getitem__(self, key): return getattr(self, key)

    class MockModuleWithSource(object):
        basename = None
        source = [
                     (1,  5.2, 12, ['44', '30']),
                     (2, 51.6, 11),
                 ]
        def __init__(self, name = 'mockmodule2'): self.basename = name
        def __enter__(self): return self
        def __exit__(self, exc_type, exc_val, exc_tb): pass
        def __getitem__(self, key): return getattr(self, key)

    class MockWreck(object):
        current_module = None
        @classmethod
        def get_local_tmp_id(cls, script_name, index):
            return -1

    mock_module = MockModule()
    linked_module = MockModuleWithSource('propmodule')
    local_vars = MockModule('locals')
    true_wreck = None

    def setUp(self):
        self.true_wreck = compiler.WRECK
        compiler.WRECK = self.MockWreck
        compiler.DEBUG_MODE = True

    def tearDown(self):
        compiler.WRECK = self.true_wreck
        self.true_wreck = None

    def test_wreck_static_variable(self):
        undefined_var = compiler.WreckVariable(name = 'undef_var')
        self.assertIs(undefined_var.value, None) # value is none for undefined variables
        self.assertEquals(undefined_var.formatted_name(), '?.undef_var') # unknown module
        self.assertEquals(repr(undefined_var), '?.undef_var<=?>') # unknown module, unknown value
        self.assertRaises(compiler.WreckException, undefined_var.__int__) # cannot evaluate value as it's undefined
        self.assertRaises(compiler.WreckException, undefined_var, 'test', -1) # Cannot generate code from static var
        defined_var = compiler.WreckVariable(name = 'def_var', value = 17)
        self.assertEquals(defined_var.formatted_name(), '?.def_var') # unknown module
        self.assertEquals(repr(defined_var), '?.def_var<=17>') # unknown module, defined value
        self.assertEquals(int(defined_var), 17) # correctly returns
        self.assertRaises(compiler.WreckException, defined_var, 'test', -1) # Cannot generate code from static var

    def test_wreck_module_reference(self):
        module_var = compiler.WreckVariable(module = self.mock_module, name = 'module_var')
        self.assertEquals(module_var.formatted_name(), 'mockmodule.module_var') # mock module
        self.assertEquals(repr(module_var), 'mockmodule.module_var<=?>') # mock module, unknown value

    def test_wreck_static_expression(self):
        a = compiler.WreckVariable(module = self.mock_module, name = 'a', value = 4)
        b = compiler.WreckVariable(module = self.mock_module, name = 'b', value = 7)
        c = a + b
        self.assertEquals(c.is_expression, True)
        self.assertEquals(c.is_static, True)
        self.assertEquals(repr(c), '(mockmodule.a<=4> + mockmodule.b<=7>)')
        self.assertEquals(int(c), 11)
        self.assertRaises(compiler.WreckException, c, 'test', -1) # Cannot evaluate code from static expression

    def test_wreck_simple_dynamic_expression(self):
        a = compiler.WreckVariable(module = self.local_vars, name = 'a', value = 100, static = False)
        b = compiler.WreckVariable(module = self.mock_module, name = 'b', value = 14)
        r = a * b
        self.assertEquals(r.is_expression, True)
        self.assertEquals(r.is_static, False)
        self.assertEquals(repr(r), '(locals.a<@100> * mockmodule.b<=14>)')
        self.assertRaises(compiler.WreckException, r.__int__)
        num_ops, code = r(script_name = 'test', destination = -5)
        self.assertEquals(num_ops, 1)
        self.assertEquals(code, [compiler.store_mul, 3, -5, 100, 14])

    def test_wreck_complex_dynamic_expression(self):
        a = compiler.WreckVariable(module = self.local_vars, name = 'a', value = 100, static = False)
        b = compiler.WreckVariable(module = self.mock_module, name = 'b', value = 14)
        c = compiler.WreckVariable(module = self.local_vars, name = 'c', value = 101, static = False)
        r = a * (b + c)
        self.assertEquals(r.is_expression, True)
        self.assertEquals(r.is_static, False)
        self.assertEquals(repr(r), '(locals.a<@100> * (mockmodule.b<=14> + locals.c<@101>))')
        self.assertRaises(compiler.WreckException, r.__int__)
        num_ops, code = r(script_name = 'test', destination = -5)
        # Next line is equivalent to:
        #     (store_add, tmp_var, 14, local_@_101),
        #     (store_mul, <destination>, local_@_100, tmp_var),
        self.assertEquals(code, [compiler.store_add, 3, -1, 14, 101, compiler.store_mul, 3, -5, 100, -1])
        self.assertEquals(num_ops, 2)

    def test_wreck_reference_properties(self):
        a = compiler.WreckVariable(module = self.linked_module, name = 'a')
        b = compiler.WreckVariable(module = self.linked_module, name = 'b', value = 1)
        c = compiler.WreckVariable(module = self.local_vars, name = 'c', static = False)
        p1 = compiler.WreckProperty(self.linked_module, a, 'root_property', (2, None, -1)) # 12
        p2 = compiler.WreckProperty(self.linked_module, b, 'fallback_property', (4, None, -1)) # -1
        p3 = compiler.WreckProperty(self.linked_module, a, 'converted_property', (1, int, -1)) # 5
        p4 = compiler.WreckProperty(self.linked_module, a, 'nested_property', (3, None, []), (0, int, -1)) # 44
        p5 = compiler.WreckProperty(self.linked_module, b, 'nested_fallback_property', (3, None, []), (0, int, -1)) # -1
        create_property = lambda var: compiler.WreckProperty(self.linked_module, var, 'illegal property', (0, None, 0))
        self.assertRaises(compiler.WreckException, create_property, c) # Should fail to create a property since variable isn't static
        self.assertEquals(repr(p1), 'propmodule.a.root_property') # Check repr function works correctly even though locals.a is not initialized yet
        evaluate_property = lambda prop: int(prop)
        self.assertRaises(compiler.WreckException, evaluate_property, p1) # Attempt to evaluate property while locals.a still unassigned
        a.value = 0
        self.assertEqual(int(p1), 12) # Should retrieve 3rd element of 1st tuple
        self.assertEqual(int(p2), -1) # Should fallback to -1
        self.assertEqual(int(p3), 5) # Should retrieve 2nd element of 2nd tuple and run int() on it
        self.assertEqual(int(p4), 44) # Should retrieve 4th element of 1st tuple, then 1st element and run int()
        self.assertEqual(int(p5), -1) # Should fallback due to missing list in declaration


class TestWreckVariableAndLibrary(unittest.TestCase):

    def test_basic_library_functions(self):
        itm = compiler.WreckLibrary('itm', varclass = compiler.WreckItemReference)
        self.assertEquals(len(itm), 0) # There should be no entries at the moment
        i1 = itm.long_sword
        i2 = itm.short_sword
        self.assertEquals(len(itm), 2) # There should be 2 items now
        self.assertIs(itm.long_sword, i1) # Attempt to retrieve itm.long_sword again should yield the same object
        self.assertIsInstance(i1, compiler.WreckItemReference) # Ensure that variable is of correct class
        entries = itm['entries']
        self.assertIsInstance(entries, dict) # Ensure we can retrieve library fields through dict-syntax
        self.assertEquals(len(entries), 2) # We should have 2 elements in the dict
        with itm as itm_data:
            unassigned = itm_data.unassigned
        self.assertIsInstance(unassigned, set) # Ensure we can retrieve library fields through with-syntax
        self.assertEquals(len(unassigned), 2) # We should have 2 unassigned elements
        self.assertItemsEqual(unassigned, {'long_sword', 'short_sword'}) # Another check
        itm.long_sword = 2
        self.assertEquals(len(itm), 2) # There should still be 2 items
        self.assertEquals(len(unassigned), 1) # There should be only 1 item now
        self.assertEquals(int(itm('long_sword')), 2) # Item should parse to value of 2 now
        itm['extendable'] = False # Disable adding new items to library
        self.assertRaises(compiler.WreckException, lambda i: i.illegal_item, itm) # Attempt to retrieve itm.illegal_item should raise an exception
        self.assertEquals(len(itm), 2) # There should still be 2 items even after an attempt to add another


class Test1(unittest.TestCase):
    pass


class Test1(unittest.TestCase):
    pass


class Test1(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""WRECK >> example_fakeint

File created by lav on 12/18/15 at 11:29 AM.
Email: Aliaksandr_Lomski@epam.com
"""

__version__ = "$Revision$"
# $Source$

import sys
sys.dont_write_bytecode = True
import operator

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
        self.bytecode = reduce(lambda a, b: a+b, operations) if operations else []
        self.unary = extras.get('unary', False)
        self.associative = extras.get('associative', False)

    @property
    def operations(self):
        return None

    @operations.setter
    def operations(self, ops):
        self.opcount = len(ops)
        self.bytecode = reduce(lambda a, b: a+b, ops) if ops else []

    def add_operation(self, op):
        self.opcount += 1
        self.bytecode += op

    def __call__(self, *argl):
        return self.code(*argl)

    def __repr__(self):
        return 'WreckOperation[%s]' % self.shorthand

    def compile(self, dest, *operands):
        code = map(lambda el: int(el.format(*operands, dest = dest)) if isinstance(el, str) else el, self.bytecode)
        return self.opcount, code


wo_add = WreckOperation('+', lambda a, b: a + b, '+', associative = True)
wo_sub = WreckOperation('-', lambda a, b: a - b, '-')
wo_mul = WreckOperation('*', lambda a, b: a * b, '*', associative = True)
wo_div = WreckOperation('/', lambda a, b: a / b, '/')
wo_mod = WreckOperation('%', lambda a, b: a % b, '%')
wo_pow = WreckOperation('**', lambda a, b: a ** b, '**')
wo_shl = WreckOperation('<<', lambda a, b: a << b, '<<')
wo_shr = WreckOperation('>>', lambda a, b: a << b, '>>')
wo_and = WreckOperation('&', lambda a, b: a & b, '&', associative = True)
wo_or  = WreckOperation('|', lambda a, b: a | b, '|', associative = True)
wo_xor = WreckOperation('^', lambda a, b: a ^ b, '^', associative = True)
wo_neg = WreckOperation('neg', lambda a: -a, '(-%r)', unary = True)
wo_abs = WreckOperation('abs', abs, 'abs(%r)', unary = True)


class WreckVariable(object):

    value = None
    operation = None
    expression_class = None # What class to use when generating expressions

    is_expression = False # Signifies a mathematical expression instead of a simple reference
    is_static = True      # Signifies that the variable contains a static value and can be computed at compile-time
    is_forced = False

    def __init__(self, value = None, operation = None, static = True):
        if self.expression_class is None: self.expression_class = type(self, True)
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

    def __repr__(self):
        if self.operation: return '{cls}(operation = {op!r})'.format(cls = self.__class__.__name__, op = self.operation)
        return '{cls}({val!r})'.format(cls = self.__class__.__name__, val = self.value)

    def resolve_illegal_operation(self, op):
        raise SyntaxError('illegal operation {0!r} in {1!r}'.format(op, self))

    def resolve_dynamic_eval(self):
        raise SyntaxError('cannot calculate dynamic expression {0!r} at runtime'.format(self))

    def resolve_failed_eval(self, exc):
        raise ArithmeticError('failed to calculate expression {0!r}: {1}'.format(self, exc.message))

    def resolve_undefined_eval(self):
        raise ValueError('variable {0!r} value not defined'.format(self))

    def _resolve_value(self):
        if self.is_expression:
            if not isinstance(self.operation[0], WreckOperation):
                return self.resolve_illegal_operation(self.operation[0])
            if not self.is_static:
                return self.resolve_dynamic_eval()
            try:
                return self.operation[0](*map(lambda v: v._resolve_value() if isinstance(v, WreckVariable) else v, self.operation[1:]))
            except ArithmeticError as e:
                self.is_forced = True
                for operand in self.operation[1:]:
                    if isinstance(operand, WreckVariable) and operand.is_forced:
                        return 0
                return self.resolve_failed_eval(e)
        else:
            if self.value is not None:
                return self.value
            return self.resolve_undefined_eval()

    __int__ = lambda self: int(self._resolve_value())
    __long__ = lambda self: long(self._resolve_value())
    __index__ = lambda self: int(self._resolve_value())
    __float__ = lambda self: float(self._resolve_value())
    __str__ = lambda self: str(self._resolve_value())

    def __add__(self, other):    return self.expression_class(operation = (wo_add, self, other))
    def __sub__(self, other):    return self.expression_class(operation = (wo_sub, self, other))
    def __mul__(self, other):    return self.expression_class(operation = (wo_mul, self, other))
    def __div__(self, other):    return self.expression_class(operation = (wo_div, self, other))
    def __mod__(self, other):    return self.expression_class(operation = (wo_mod, self, other))
    def __pow__(self, other):    return self.expression_class(operation = (wo_pow, self, other))
    def __lshift__(self, other): return self.expression_class(operation = (wo_shl, self, other))
    def __rshift__(self, other): return self.expression_class(operation = (wo_shr, self, other))
    def __and__(self, other):    return self.expression_class(operation = (wo_and, self, other))
    def __or__(self, other):     return self.expression_class(operation = (wo_or, self, other))

    def __radd__(self, other):    return self.expression_class(operation = (wo_add, other, self))
    def __rsub__(self, other):    return self.expression_class(operation = (wo_sub, other, self))
    def __rmul__(self, other):    return self.expression_class(operation = (wo_mul, other, self))
    def __rdiv__(self, other):    return self.expression_class(operation = (wo_div, other, self))
    def __rmod__(self, other):    return self.expression_class(operation = (wo_mod, other, self))
    def __rpow__(self, other):    return self.expression_class(operation = (wo_pow, other, self))
    def __rlshift__(self, other): return self.expression_class(operation = (wo_shl, other, self))
    def __rrshift__(self, other): return self.expression_class(operation = (wo_shr, other, self))
    def __rand__(self, other):    return self.expression_class(operation = (wo_and, other, self))
    def __ror__(self, other):     return self.expression_class(operation = (wo_or, other, self))

    def __neg__(self): return self.expression_class(operation = (wo_neg, self))
    def __pos__(self): return self
    def __abs__(self): return self.expression_class(operation = (wo_abs, self))

    __truediv__ = __div__
    __rtruediv__ = __rdiv__
    __floordiv__ = __div__
    __rfloordiv__ = __rdiv__

    __eq__ = lambda self, other: int(self) == other
    __ne__ = lambda self, other: int(self) != other
    __lt__ = lambda self, other: int(self) < other
    __le__ = lambda self, other: int(self) <= other
    __gt__ = lambda self, other: int(self) > other
    __ge__ = lambda self, other: int(self) >= other


class WreckAggregateValue(WreckVariable, dict):

    fields = {
        'byte0': (lambda v: v & 0xff,         lambda f: f),
        'byte1': (lambda v: (v >> 8)  & 0xff, lambda f: f << 8),
        'byte2': (lambda v: (v >> 16) & 0xff, lambda f: f << 16),
        'byte3': (lambda v: (v >> 24) & 0xff, lambda f: f << 24),
    }

    def __init__(self, raw_value = None, **argd):
        if raw_value is None:
            dict.__init__(self, argd)
        else:
            dict.__init__(self)
            for key, (unpack, pack) in self.fields.iteritems():
                self[key] = unpack(raw_value)
        WreckVariable.__init__(self, self.__int__())

    def __int__(self):
        if not len(self): return 0
        return reduce(operator.or_, map(lambda i: self.fields[i[0]][1](i[1]), self.iteritems()))

    def __getattr__(self, key):
        if key in self: return self[key]
        if key in self.fields: return self.fields[key][0](0)
        return super(WreckAggregateValue, self).__getattr__(key)

    def _combine(self, other, op):
        if type(self, True) != type(other, True):
            other = type(self, True)(int(other))
        init = {}
        for key in set(self.keys() + other.keys()):
            try:
                init[key] = op(self.get(key, 0), other.get(key, 0))
            except TypeError:
                if key not in self.fields:
                    raise
                packed_result = op(self.fields[key][1](self.get(key, 0)), self.fields[key][1](other.get(key, 0)))
                init[key] = self.fields[key][0](packed_result)
        return type(self, True)(**init)

    def _apply(self, op):
        init = {}
        for key, value in self.iteritems():
            if isinstance(self.get(key, 0), float):
                init[key] = float_op(value)
            else:
                init[key] = op(value)
        return type(self, True)(**init)

    __ror__ = __or__ = lambda self, other: self._combine(other, operator.or_)
    __rand__ = __and__ = lambda self, other: self._combine(other, operator.and_)
    __rxor__ = __xor__ = lambda self, other: self._combine(other, operator.xor)

    __radd__ = __add__ = __or__
    __rsub__ = __sub__ = lambda self, other: self._combine(other._apply(operator.neg), operator.and_)
    __rmul__ = __mul__ = lambda self, other: type(self, True)(int(self) * int(other))
    __rdiv__ = __div__ = lambda self, other: type(self, True)(int(self) / int(other))
    __rmod__ = __mod__ = lambda self, other: type(self, True)(int(self) % int(other))
    __rpow__ = __pow__ = lambda self, other: type(self, True)(int(self) ** int(other))
    __rlshift__ = __lshift__ = lambda self, other: int(self) << int(other)
    __rrshift__ = __rshift__ = lambda self, other: int(self) >> int(other)
    __neg__ = lambda self: self._apply(operator.neg)
    __abs__ = lambda self: self._apply(abs)


def forge_inheritances(disguise_heir = {}, disguise_type = {}, disguise_tree = {},
                       isinstance = None, issubclass = None, type = None):
    """
    Monkey patch isinstance(), issubclass() and type() built-in functions to create fake inheritances.

    :param disguise_heir: dict of desired subclass:superclass pairs; type(subclass()) will return subclass
    :param disguise_type: dict of desired subclass:superclass pairs, type(subclass()) will return superclass
    :param disguise_tree: dict of desired subclass:superclass pairs, type(subclass()) will return superclass for subclass and all it's heirs
    :param isinstance: optional callable parameter, if provided it will be used instead of __builtins__.isinstance as Python real isinstance() function.
    :param issubclass: optional callable parameter, if provided it will be used instead of __builtins__.issubclass as Python real issubclass() function.
    :param type: optional callable parameter, if provided it will be used instead of __builtins__.type as Python real type() function.
    """

    if not(disguise_heir or disguise_type or disguise_tree): return

    import __builtin__
    from itertools import chain

    python_isinstance = __builtin__.isinstance if isinstance is None else isinstance
    python_issubclass = __builtin__.issubclass if issubclass is None else issubclass
    python_type       = __builtin__.type if type is None else type

    def disguised_isinstance(obj, cls, honest = False):
        if cls == disguised_type: return disguised_isinstance(obj, python_type)
        if honest:
            if python_isinstance.__name__ == 'disguised_isinstance':
                return python_isinstance(obj, cls, True)
            return python_isinstance(obj, cls)
        if python_type(cls) == tuple:
            return any(map(lambda subcls: disguised_isinstance(obj, subcls), cls))
        for subclass, superclass in chain(disguise_heir.iteritems(),
                                          disguise_type.iteritems(),
                                          disguise_tree.iteritems()):
            if python_isinstance(obj, subclass) and python_issubclass(superclass, cls):
                return True
        try:
            return python_isinstance(obj, cls)
        except:
            print obj
            print cls
            raise
    __builtin__.isinstance = disguised_isinstance

    def disguised_issubclass(qcls, cls, honest = False):
        if cls == disguised_type: return disguised_issubclass(qcls, python_type)
        if honest:
            if python_issubclass.__name__ == 'disguised_issubclass':
                return python_issubclass(qcls, cls, True)
            return python_issubclass(qcls, cls)
        if python_type(cls) == tuple:
            return any(map(lambda subcls: disguised_issubclass(qcls, subcls), cls))
        for subclass, superclass in chain(disguise_heir.iteritems(),
                                          disguise_type.iteritems(),
                                          disguise_tree.iteritems()):
            if python_issubclass(qcls, subclass) and python_issubclass(superclass, cls):
                return True
        return python_issubclass(qcls, cls)
    __builtin__.issubclass = disguised_issubclass

    if not(disguise_type or disguise_tree): return # No need to patch type() if these are empty

    def disguised_type(obj, honest = False, extra = None):
        if (extra is not None):
            # this is a call to create a type instance, we must not touch it
            return python_type(obj, honest, extra)
        if honest:
            if python_type.__name__ == 'disguised_type':
                return python_type(obj, True)
            return python_type(obj)
        for subclass, superclass in disguise_type.iteritems():
            if obj == subclass:
                return superclass
        for subclass, superclass in disguise_tree.iteritems():
            if python_isinstance(obj, subclass):
                return superclass
        return python_type(obj)
    __builtin__.type       = disguised_type

forge_inheritances(disguise_tree = { WreckVariable: int })

if __name__ == '__main__':
    a = WreckAggregateValue(5184)
    print dict(a)

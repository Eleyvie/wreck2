import inspect

class A(object):
    def aaa(self):
        return 5

A.bbb = lambda self: self.aaa + 5

print inspect.getsource(A)
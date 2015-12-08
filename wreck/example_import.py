import sys
sys.dont_write_bytecode = True
import __builtin__
from imp import is_builtin, PY_SOURCE, find_module, load_module, new_module
from traceback import format_exc as formatted_exception
import os

def import_hook(module_name, gvars, lvars, fromdata, level = -1):
    if module_name in sys.modules:
        module = sys.modules[module_name]
    else:
        try:
            mfile, mpath, mdesc = find_module(module_name)
            try:
                if not os.path.abspath(mpath).startswith(main_folder): raise ImportError()
                module = new_module(module_name)
                module.__dict__['__file__'] = mpath
                module_code = mfile.read()
                exec(module_code, module.__dict__)
                sys.modules[module_name] = module
            finally:
                if isinstance(mfile, file): mfile.close()
        except ImportError:
            module = python_import(module_name, gvars, lvars, fromdata, level)
    return module

python_import = __builtin__.__import__
__builtin__.__import__ = import_hook
main_folder = os.getcwd()

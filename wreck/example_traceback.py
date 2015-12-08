import sys
from traceback import format_exc, extract_tb

def failure():
    a = b
    return a

try:
    #c = failure()
    a = b
except:
    et, ev, etb = sys.exc_info()

frames = extract_tb(etb)
print frames
# frames = list(tuple(filename, line_no, func_name, text))
# func_name == '<module>' if at top level

#print etb.tb_lineno
#print etb.tb_frame.f_lineno
#print etb.tb_frame.f_globals['__name__']
#print etb.tb_frame.f_globals['__file__']


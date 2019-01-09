import ctypes
from ctypes import *

dll = cdll.LoadLibrary('tsim.dll')
retCode = dll.DiGdiOpen
print('retCode',retCode)

lib = ctypes.CDLL('tsim.dll')
print('lib',lib)

pfun = lib.DiGdiOpen
print('pfun',pfun)

pfun.restype = ctypes.c_int32
pfun.argtypes = (ctypes.c_void_p,)

x = pfun

print('x',x)






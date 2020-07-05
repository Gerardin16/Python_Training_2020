import ctypes
import sys
import gc

a = "i am assigning a value"
b = a


#print(ctypes.c_long.from_address(id(a)).value)

print(sys.getrefcount('asdasdasdasdasdasdasd'))
del a
del b

print(sys.getrefcount('asdasdasdasdasdasdasd'))

gc.collect()

print(sys.getrefcount('asdasdasdasdasdasdasd'))
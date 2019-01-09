import struct

str = (dir(struct))

for s in str:
    print(s)

_L = struct.pack('>L',0x1514)

print(_L)




from struct import *

# Store as bytes data
# i = int
# f = float
packed_data = pack('iif', 6, 19, 6.92)
print(packed_data)

print(calcsize('i'))
print(calcsize('i'))
print(calcsize('iif'))

# Good for transferring data over the network
# How to convert byte data into human readable form
original_data = unpack('iif', packed_data)

print(original_data)

print(unpack('iif', b'\x06\x00\x00\x00\x13\x00\x00\x00\xa4p\xdd@'))
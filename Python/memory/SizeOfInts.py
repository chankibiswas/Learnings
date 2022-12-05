import sys

# Size of normal ints is 28 bytes
print(sys.getsizeof(1))

print(sys.getsizeof(5))

print(sys.getsizeof(10))

print(sys.getsizeof(100000000))

# Size grows with bigger ints
print(sys.getsizeof(10000000000000000000000000000000))
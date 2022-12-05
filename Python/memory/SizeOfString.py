import sys

# Size of empty string is 49 bytes and it grows by 1 byte with every character
print(sys.getsizeof(""))

print(sys.getsizeof("a"))

print(sys.getsizeof("ab"))
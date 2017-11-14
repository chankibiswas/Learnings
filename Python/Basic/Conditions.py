# If condition
a=1
b=2
c=3
d=2

if a < b:
    print("a is less than b")

if a < b < c > d:
    print("Multiple checks at same line")

if b == d:
    print("b is equal to d")

if b != c:
    print("b is not equal to c")

if b > c:
    print("b is greater than c")
else:
    print("b is not greater than c")

if b < d:
    print("b is less than d")
elif b == d:
    print("b is equal to d")
else:
    print("b is greater than d")

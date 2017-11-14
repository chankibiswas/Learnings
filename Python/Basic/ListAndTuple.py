# Tuple has () or no enclosure during definition. They are immutable.
x = (3,1,9,5)

# List has [] enclosure. They are mutable.
y = [2,5,3,8]

print(x[3], x[0])

print(y[1], y[0])

# Appending to the end of list
y.append(100)

print(y)

# Inserting a value at nth index (Index, value)
y.insert(2, 34)

print(y)

# Same as y.remove(2, 34)
y.remove(y[2])

print(y)

# Use of negative index - Reads from end
print(y[-2])

# Slicing. Getting values from one index to another. (Index 1 inclusive, Index 2 exclusive)
print(y[2:4])

# Get index value of certain element
print(y.index(100))

# Count of certain element
print(y.count(100))

# Sort Alpha numeric list according to alpha order and numbers according to value
z = ['Chennai','Mumbai','Kolkata','Delhi']
z.sort()
print(z)


# Multi dimentional List
a = [
    [2,3],
    [[5,1],[6,0],[3,2]]
    ]
print(a[0])
print(a[1][2][0])







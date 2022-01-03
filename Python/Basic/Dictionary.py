employee = {123:'Ram',234:'Ramesh',345:'Jignesh'}

print(employee)
# Print just 1 element
print(employee[234])

# Update element
employee[123] = 'XYZ'

# Add a new element
employee[456] = 'Mohan'

print(employee)

# Delete element
del employee[123]

print(employee)


emp = {123:['Ram',29],234:['Ramesh',31],345:['Jignesh',30]}

print(emp)

print(emp[345][1])

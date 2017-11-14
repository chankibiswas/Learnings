# Basic function
def basicFunction():
    print("My first basic function")

# Function with parameter
def func1(n1, n2):
    print(n1, n2)

# Function with parameter and default assigned value
def func2(n1, n2=5):
    print(n1, n2)


# Calling functions in different ways

basicFunction()

func1(3, 5)

# When value assigned with variable names, order doesn't mater
func1(n2=10, n1=12)

func2(15)

func2(n2=19, n1=20)





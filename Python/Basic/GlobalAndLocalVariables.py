# Functions and global variables
x = 10

def func1():
    print(x)
    print(x+5)

func1()
print("End func1")

def func2():
    print(x)
    # x+=5
    #print(x)

func2()
print("End func2")

def func3():
    global x
    x+=5
    print(x)

func3()
print("End func3")

def func4():
    temp = x
    temp += 10
    return temp

x = func4()
print(x)
print("End func4")

# Python program to illustrate *args
# *args (Non-Keyword Arguments)
def myFun1(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)


myFun1('Hello', 'Welcome', 'to', 'GeeksForGeeks')


# Python program to illustrate **kwargs for
# **kwargs (Keyword Arguments)

def myFun2(arg2, **kwargs):
    print("First argument :", arg2)
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


myFun2("Hi", first='Geeks', mid='for', last='Geeks')

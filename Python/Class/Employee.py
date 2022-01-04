class Employee:
    x = 5

    def __init__(self, name):
        print("Init method called")
        print("Accessing global variable - ", self.x)
        self.x = name

    def get(self):
        print("Dummy method")


e1 = Employee("Ram")
print(e1.x)
e1.get()

print("---------------------------")

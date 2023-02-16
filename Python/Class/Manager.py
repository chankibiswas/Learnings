import Employee


class Manager(Employee):
    def __init__(self, age, name):
        super().__init__(name)
        print(self.x)


m = Manager(30, "Mahesh")
print(m.x)
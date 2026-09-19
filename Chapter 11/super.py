class Employee:
    def __init__(self):
        print("This is the constructor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("This is the constructor of Programmer")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__() # Calls the parent constructore in chiled or derived class without initializing parent obect
        print("This is the constructor of Manager")
    c = 3

# o = Employee()
# print(o.a)

# o = Programmer()
# print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)
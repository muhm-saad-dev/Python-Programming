class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The value of class attribute is {cls.a}")

e = Employee()
e.a = 50
e.name = "Saad"
print(e.name)
e.show()

class Employee:
    company = "ITC"
    def show(self):
        print(f"The company of employee is {self.company}")

class Programmer(Employee): # This is drived class from the class Employee
    def showlang(self):
        print(f"The company of Programmer is {self.lang}")

b = Employee()
a = Programmer()
print(a.company, b.company)

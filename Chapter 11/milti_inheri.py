class Employee:
    company = "ITC"
    def show(self):
        print(f"The company of employee is {self.company}")


class Coder:
    lang = "python"
    def printLang(self):
        print(f"The languge for COders is {self.lang}")

class Programmer(Employee, Coder): # This is drived class from the class Employee
    def showlang(self):
        print(f"The company of Programmer is {self.lang}")

b = Employee()
a = Programmer()

a.show()
a.printLang()
a.showlang()

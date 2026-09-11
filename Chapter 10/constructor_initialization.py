class employee:
    language = "py"  # This is a class attribute
    salary = 1300000

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        print("this is a constructore running")

    def get_info(self):
        print(f"The language is {self.language} and salary is {self.salary}")
    @staticmethod # it prevent to get the self perameter as a whole object 
    def greet():
        print("hello, i am greeting you")


saad = employee("saad", 1500000, "Python")
print(saad.name, saad.language, saad.salary)

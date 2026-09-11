class employee:
    language = "py"  # This is a class attribute
    salary = 1300000

    def get_info(self):
        print(f"The language is {self.language} and salary is {self.salary}")
    @staticmethod # it prevent to get the self perameter as a whole object 
    def greet():
        print("hello, i am greeting you")


saad = employee()
saad.language = "Java"   # This is an instance attribute
saad.get_info() # This is Same as under
employee.get_info(saad) # as this is written 
saad.greet()

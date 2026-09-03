class employee:
    language = "py"  # This is a class attribute
    salary = 1300000


saad = employee()
saad.language = "Java"   # This is an instance attribute
print(saad.language, saad.salary)

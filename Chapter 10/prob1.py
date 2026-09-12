class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("saad", 1500000, 245)
print(p.name, p.salary, p.company, p.pin)
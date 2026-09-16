class Calculator:
    def __init__(self, n):
        self.n = n

    def squar(self):
        print(f"The squar is {self.n * self.n}")

    def cube(self):
        print(f"The cube is {self.n * self.n * self.n}")

    def squarRoot(self):
        print(f"The squarRoot is {self.n ** 1/2}")

    @staticmethod
    def hello():
        print("Hello User")

a = Calculator(4)
a.squar()
a.cube()
a.squarRoot()
a.hello()

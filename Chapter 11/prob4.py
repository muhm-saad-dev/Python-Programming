class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i
    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)

    def __mul__(self, c2):
        return Complex(
        self.r * c2.r - self.i * c2.i,
        self.r * c2.i + self.i * c2.r
    )

    def __str__(self):
        return f"{self.r} + {self.i}i"
    
c1 = Complex(1, 3)
c2 = Complex(2, 4)
c3 = Complex(5, 3)
c4 = Complex(6, 9)
print(c2 + c4)
print(c1 * c3)

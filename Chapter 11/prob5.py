class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, v2):
        return Vector(
        self.x + v2.x,
        self.y + v2.y,
        self.z + v2.z
    )
    def __mul__(self, v2):
        return self.x * v2.x + self.y * v2.y + self.z * v2.z

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)

print(v1 + v3)
print(v1 * v3)
print(v3 + v2)
print(v3 * v2)

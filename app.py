class Point:
    defaul_color = "Red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ( {self.x}, {self.y})")


Point.defaul_color = "Green"

point = Point(1, 2)
point.draw()
print(point.defaul_color)


another = Point(3, 4)
another.draw()
print(another.defaul_color)

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        print(int(self.base * self.height / 2))


new_triangle = Triangle(3, 4)
new_triangle.area()

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimetr(self):
        print(2 * (self.length + self.width))


new_rectangle = Rectangle(5, 3)
new_rectangle.calculate_perimetr()

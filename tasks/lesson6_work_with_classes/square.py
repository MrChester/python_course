class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_perimetr(self):
        print(4 * self.side_length)

    def change_size(self, rate):
        self.side_length = self.side_length + rate


new_square = Square(5)
print(new_square.side_length)
new_square.calculate_perimetr()
new_square.change_size(3)
print(new_square.side_length)
new_square.calculate_perimetr()
new_square.change_size(-3)
print(new_square.side_length)
new_square.calculate_perimetr()

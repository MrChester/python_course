class Apple:
    def __init__(self, color, size, weight, variety):
        self.color = color
        self.size = size
        self.weight = weight
        self.variety = variety


new_apple = Apple("Green", "Middle", 285, "Honeycrisp")
print(new_apple.color)
print(new_apple.size)
print(new_apple.weight)
print(new_apple.variety)

new_apple.variety = "Golden Delicious"
print(new_apple.variety)

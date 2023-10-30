# ---------- Arithmetic Operations using Magic Methods ----------

# __add__
# __sub__
# __mul__
# __floordiv__

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # __add__ magic method "+"
    def __add__(self, other):
        return f"Coordinates: {self.x + other.x}, {self.y + other.y}"

    # __sub__ magic method "-"
    def __sub__(self, other):
        return f"Coordinates: {self.x - other.x}, {self.y - other.y}"

    # __mul__ magic method "*"
    def __mul__(self, other):
        return f"Coordinates: {self.x * other.x}, {self.y * other.y}"

    # __floordiv__ magic method "//"   the reason for using this is that it will round the result, if it is 6.999 it will give whole number, 6
    def __floordiv__(self, other):
        return f"Coordinates: {self.x // other.x}, {self.y // other.y}"


test1 = Robot(1, 5)
test2 = Robot(3, 3)

print(test1 + test2)
print(test1 - test2)
print(test1 * test2)
print(test1 // test2)

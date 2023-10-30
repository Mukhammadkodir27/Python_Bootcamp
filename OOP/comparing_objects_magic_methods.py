# ---------- Comparing Objects using Magic Methods ----------

# __eq__
# __gt__
# __lt__

# --

# class Robot:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


# r1 = Robot(1.2, 2.2)
# r2 = Robot(1.2, 2.2)

# print(r1 == r2)  # false because they have different ids or locations though parameters are same

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):  # as we compare two objects, we will need two arguments
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):  # greater than operator
        return self.x > other.x and self.y > other.y

    def __lt__(self, other):  # less than operator
        return self.x < other.x and self.y < other.y

    # note than we cannot use two operators at the same time like <= or >=


r1 = Robot(2, 2)
r2 = Robot(2, 2)

print(r1 == r2)  # True, now we can use == operator by the help of eq magic method
print(r1 > r2)
print(r1 < r2)

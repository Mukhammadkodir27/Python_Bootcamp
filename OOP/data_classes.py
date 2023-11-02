# ---------- Data Classes ----------

# issues

# class Robot:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


# robot1 = Robot(1, 2)
# robot2 = Robot(1, 2)

# print(robot1 == robot2)  # False as their id (memory location) is wrong but values are same
# print(id(robot1))
# print(id(robot2))

# Solution 1 -- __eq__
from collections import namedtuple

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


robot1 = Robot(1, 2)
robot2 = Robot(1, 2)

print(robot1 == robot2)  # True as we used __eq__ magic method
print(id(robot1))
print(id(robot2))


# Solution 2  -> namedtuple()


Robot2 = namedtuple("Robot2", ["x", "y"])

robot1 = Robot2(x=1, y=2)
robot2 = Robot2(1, 2)

print(robot1 == robot2)

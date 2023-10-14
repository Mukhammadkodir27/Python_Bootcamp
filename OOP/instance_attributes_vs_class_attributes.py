# ---------- instance attributes vs class attributes ---------

# Objects in Python are dynamic, you can provide attributes to the objects after
# you have defined the constructor of the class.

class Robot:
    # class attribute
    z = 23

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def walk(self):
        print(f"walking coordinates - ({self.x}, {self.y}, {self.z})")


robot1 = Robot(12, 12)
robot1.walk()

print(robot1.x)
print(robot1.z)

robot2 = Robot(21, 21)
robot2.m = 22
print(robot2.m)
# print(robot1.m) # attributeError because m is assigned to robot2 only and
# cannot be accessed by other instances of the class


"""
1) Instance(Object) Attributes - are defined within the constructor of a class
2) Class Attributes - are created within the class itself
"""


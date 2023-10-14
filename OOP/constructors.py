# ---------- Constructors ----------

# - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - #
# class Robot:
#     def walk(self, x, y):
#         print(f"walking coordinates: ({x},{y})")


# robot = Robot()
# robot.walk(1.2, 2.2)
# - # - # - # - # - # - # - # - # - # - # - # - # - # - #z - # - # - #


class Robot:
    def __init__(self, x, y):  # consturctor
        # default
        # self.x = 10
        # self.y = 10
        self.x = x
        self.y = y

    def walk(self):
        print(f"walking coordinates ({self.x}, {self.y})")

    def run(self, where, how):
        print(f"run {where} very {how}")


robot = Robot(1, 2)
robot.walk()
robot.run("home", "fast")


class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        # self.age = 20   # then it could assign 20 no matter what input you provide
        self.age = age

    def introduce(self):
        print(
            f"Hello I am {self.name} {self.surname}, I am {self.age} years old.")


person1 = Person("Mukhammadkodir", "Abdusalomov", 21)
person1.introduce()

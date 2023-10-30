# ---------- Object Methods vs Class Methods ----------

# Instance Methods -- Object Methods

class Robot:
    def __init__(self, x, y):  # constructor
        self.x = x
        self.y = y

    def walk(self):
        print(f"Walking coordinates are {self.x}, {self.y}")


robot1 = Robot(1.1, 2.2)
robot1.walk()

# ----------------------------------------------------------------------

# Class Methods


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def introduce(self):
        print(f"I am {self.name} {self.surname}")

    # decorator
    @classmethod
    def specific_method(cls):
        return cls("Adil", "Khan")


person1 = Person.specific_method()
person1.introduce()

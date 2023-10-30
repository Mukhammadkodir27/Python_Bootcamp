# ---------- Magic Methods -----------

# --
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def introduce(self):
        print(f"Hi, I am {self.name} {self.surname}")


person1 = Person("Adil", "Khan")
person1.introduce()
print(person1)  # gives the memory location of that ...

# magic method -- __str__


class Robot:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def details(self):
        print(f"This is a {self.model} model robot designed in {self.year}!")

    def __str__(self):
        return f"It is {self.model} model robot produced in {self.year}!"


robot1 = Robot("Hybrid", 2023)
robot1.details()
print(robot1)
print(str(robot1))

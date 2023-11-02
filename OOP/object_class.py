# ---------- Object Class ----------

# The Object Class is the base class for all classes (class hierarchy)

# ALl the built-in functions, all the magic methods, - belong to this object class
# which ironically is a function --- class object()

class Person:
    def __init__(self):
        self.employed = True

    def singing(self):
        print("Singing")


class Richard(Person):
    def running(self):
        print("Running")


runner = Richard()
print(runner.employed)

base_object = object()

# base_object.

# to check if class is inherited from another class

print(isinstance(runner, Richard))
print(isinstance(runner, Person))
print(isinstance(runner, object))
print(isinstance(base_object, object))
print(isinstance(base_object, Person))

# ---------- Method Overriding ---------

class Person:
    def __init__(self):
        print("Base Class")
        self.employed = True

    def singing(self):
        pass


class James(Person):
    def __init__(self):
        # method overriding
        super().__init__()   # Base first then Sub class is called
        print("Sub Class")
        self.jogger = True

        # super().__init__()  # Sub first then Base Class is called

    def running(self):
        pass


runner = James()

print(runner.jogger)
print(runner.employed)

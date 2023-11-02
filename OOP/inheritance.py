# ---------- Inheritance ----------

# Method Inheritance

# parent/base class
class Person:
    def __init__(self):
        pass

    def introduce(self):
        print("Hello, I am a human!")
        print("How may I help you")

    def fivebyfive(self):
        return 5 + 5

    def __str__(self):
        return f" "

# sub/child/inherited/derived class


class Robert(Person):
    def __init__(self):
        pass

    def his_name(self):
        print("Hi, My name is Robert!")


class Roland(Person):
    def __init__(self):
        pass

    def profession(self):
        return "footballer!"


class Messi(Roland):
    def __init__(self):
        pass


person1 = Person()
result = person1.fivebyfive
print(str(result))

user = Roland()
user.introduce()

messi = Messi()
messi.introduce()

robert = Robert()
robert.his_name()

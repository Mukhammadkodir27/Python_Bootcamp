# ---------- Scope ----------

# Two variable types
# 1- Local Variables
# 2- Global Variables

# Example
def message(date):
    content = "something very cool has happened"


message("May 21, 2023")

# print(date) # NameError because date is being called outside of a function
# print(content) # NameError because content is within a function and cannot be called outside of it

# the good thing about local variables is that you will not have naming collapsion.
# which means you can have as many same names as you want in each function(inside of it)
# local variables have short life time


def comment(date):
    content = "amazing landscape"


comment("May 23, 2022")

# Example
content = "just do it"


def post(date):
    content = "i am on a trip"


post("Jan 1, 2021")
# just do it    -> as it is global variable not the one inside a function
print(content)


# Example
dog_name = "Hachi"


def animal_name():
    global dog_name   # making local variable a global variable
    dog_name = "Georgie"


animal_name()
print(dog_name)

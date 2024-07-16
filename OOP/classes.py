# Introduction to classes

# you must have a class to create an object
# int class, float class, str class, all have classes


# ---------- Classes ----------

"""
Objects
1) Attributes
2) Behaviour
"""

# A class is a blueprint for creating objects

class Robot:
    pass

# we are using Pascal naming convention not Snake Case naming convention for naming classes

# An object (instance) is an instantiation of a class

robot_obj = Robot()
print(robot_obj)
print(type(robot_obj))

x = 25
print(type(x))  # x is an object of integer class

n = 2.5
print(type(n))  # n is an object of float class

my_list = [1, 2, 3, 4]
print(type(my_list))  # my_list is an object of list class

my_info = {
    "name": "Kadir", 
    "surname": "Abdusalomov"
}
print(type(my_info))  # my_info is an object of dict class

#class
# ---------Creating Classes Objects ---------

class Robot:
    def walk(self):
        print("The robot is walking!")


robot = Robot()
robot.walk()

print(type(robot))

# Example 2 ->>>> isinstance() method to check if it is object of the class

# two parameters should be given: 1) object 2) class  --- isinstance(object, class)

print(isinstance(robot, Robot))

robot_obj = Robot()
print(isinstance(robot_obj, Robot))

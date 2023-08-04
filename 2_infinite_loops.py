# it is better not to touch infinite loops because it might crash your pc or vs code... !

#number = 100
#while number > 1:
#  print("Hello")

# if you do not provide ending point, it will not stop from execution which results in breaking your pc and vs code. 
# to solve it use:
number = 100
while number > 1:
  print("Hello")
  number -= 10

# this will prevent infinite loops

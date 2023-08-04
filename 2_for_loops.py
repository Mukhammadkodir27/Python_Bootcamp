# ------------ For Loops ------------

# for x in range(10):
#    print(x)

"""
Result: 
0
1
2
3
4
5
6
7
8
9
"""

# Example 2 ->>>
for number in range(5):
    print(f"The code has run for {number} time(s)")

# Example 3 ->>>
for a in range(5, 15, 2):  # starting point, and ending point, also jumping measure
    print(a)

"""
Result: 
5
7
9
11
13
"""

# ------ Part 2, For Loops ------

# status = True

# for number in range(1, 4):
#    print(f"Attempt {number}")  #instead of hard-coding numbers, use formatted strings

#    if status:
#       print("Success")
#       break

print("")

# Example ->>>

status = False

for number in range(1, 4):
    # instead of hard-coding numbers, use formatted strings
    print(f"Attempt {number}")

    if status:
        print("Success")
        break
else:
    print("Failed")

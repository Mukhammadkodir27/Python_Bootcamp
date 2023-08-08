# ---------- Swapping List Items ----------

numbers = [2, 4, 6]

numbers[0], numbers[1], numbers[2] = numbers[2], numbers[1], numbers[0]
print(numbers)

# this is not reversing, this is swapping!
# we are changing the positions, values of every indicises, changing the value of every individual index


# Example
full_name = ["Mukhammadkodir", "Abdusalomov"]
full_name[0], full_name[1] = full_name[1], full_name[0]
print(full_name) # Mukhammadkodir Abdusalomov -> Abdusalomov Mukhammadkodir

# ---------- Required & Optional Parameters ----------

# Example
def working_condition(device, status="working"):
    return f"The {device} is {status}"


print(working_condition("Laptop"))
# overriding the optional parameter
print(working_condition("fridge", "out of order"))


# Example
def subtract(x, z, y=15):    # it gives error because optional parameter has to be the last one
    return x - y - z


print(subtract(25, 5))
print(subtract(25, 5, 10))  # overriding the above optional parameter


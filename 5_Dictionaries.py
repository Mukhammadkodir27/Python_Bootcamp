8# ---------- Introduction to Dictionaries ----------

# a collection of key value pairs

# Example 1
contacts = {
    "Samantha": 456,
    "John": 123
}

print(contacts)

# Example 2
employee_info = {
    "Name": "Will",
    "Last Name": "Oldman",
    "Address": "NYC, USA",
    "Job": "Salesperson",
    "Age": 31
}

print(employee_info)


# Example 3
animal_names = dict(cat="Sebastian", dog="Togo")
# dog is the key and togo is the value


# Accessing Dictionary Key Values

# Example 4
print(employee_info["Name"])
# we have the key here and output will be its value:
print(employee_info["Job"])
print(employee_info["Age"])

employee_info["Job"] = "Developer"
employee_info["Age"] = 32
employee_info["Hobbies"] = "Reading", "Walking"
# here we added new key to our dictionary


# Example 6
# what if we try to access key which does not exists in our dictionary
# print(employee_info["Favorite Color"])

employee_info["Favorite Color"] = "Grey"

# 1 - Checking whether a key exists
if "Favorite Color" in employee_info:
    print(employee_info["Favorite Color"])

# 2 - get() method
print("Hallo", employee_info.get("Favorite Color"))


# Example 7
print(employee_info.get("Favorite Color", "Green"))
# in case if value of this key provided does not exists, then this value given with key will be used

# Keyword Arguments

# Keyword arguments are used whenever we do not know how many parameters are going to be passed, but we can do one thing,
# we will provide the key value pairs similar to dict.
# for example: name="Kadir", surname="Abdusalomov", age=21
# as is a dictionary we need to give ** inside () - *key-*value pairs

def employee_information(**info):
    print(f"Employee details: {info}")


employee_information(name="Kadir", surname="Abdusalomov", age=21,
                     position="Developer", about="I love creating random stuff!")


def student_details(**details):
    return details


student_information = student_details(
    classNo="10 A", teacher="Unknown", GPA=5.0)

print(f"Student Details: {student_information} ...")


# Keyword Arguments -> Dictionaries (**variable)
# Non-Keyword Arguments -> Tuples (*varibale)


# Non-Keyword Arguments
# same as keyword arguments but with no key-value pairs
# for example, (*variable) = ("Kadir", "Abdusalomov", 21, "Developer")

def info_employee(*info):
    print("Non Keyword Arguments:::")
    print(info)


info_employee("Kadir", "Abdusalomov", 21, "Developer")


def random_numbers(*nums):
    return nums


numbers_generated = random_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

print(f"Generated Random Numbers: {numbers_generated}...")


def subtract(*nums):
    number = 100
    for n in nums:
        number = number - n
    return number if number > 0 else print("Number is less than 0")


subtacted_number = subtract(10, 23, 34, 10)
print(subtacted_number)
print(f"Results are: {subtract(10, 10, 10)}")

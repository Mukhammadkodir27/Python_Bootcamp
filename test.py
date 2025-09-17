# # int
# # float
# # bool
# # string
# # char
# # list
# # dict
# # tuple
# # set

# # integers
# a = 5
# b = 5
# c = a + b
# print(f'{a+b}')


# # floating point numbers
# a_a = 5.4
# b_b = 3.4

# c_c = a_a + b_b

# print(f'Result is {c_c}')


# # booleans
# online = True
# offline = False

# print(type(online))

# # strings
# name = 'John'
# surname = 'John'

# print(f'{name}, {surname}')

# # Lists - ordered
# numbers = [1, 2, 3, 4, 5]
# mid_numbers = [1.2, 2, 23.12, 22, 31]
# mix_numbers = [1, 'John', True, offline]

# # dictionary - unordered
# user_details = {'name': 'Kadir', 'surname': 'Abdusalomov'}

# # tuple - ordered
# mix_numbers = (1, 2, 3, 4, True, 'John')

# # set - unordered - unique values
# mix_numbers = {1, 1, 1, 1, 1, 'John', False}
# print(mix_numbers)

# user_details = None


# # string methods
# address = 'Heerlen, Netherlands'
# print(len(address))

# print(address[0])

# print(address[:-1])
# print(address[:])
# print(address[-8:-1])

# # concatenation
# city = 'Heerlen'
# country = 'Netherlands'
# address = city + ', ' + country
# print(address)

# address = f'{city}, {country}'
# print(address)


# print(address.upper())
# print(address.lower())
# print(address.title())
# print(address.capitalize())

# # name = input(str('Enter your name: '))
# # print(len(name))
# # # Kadir is 5 letters but if i add space it is calculating space too so in total 6

# # # solution is
# # name = name.strip()
# # print(len(name))
# # # now it returns 5

# print(f'Your current address is: {address}')
# address = address.replace('Heerlen', input('Enter city to update: '))
# print(f'Your updated address is: {address}')


# if 'Heerlen' in address:
#     print('He lives in Heerlen')
# elif 'Heerlen' not in address:
#     print('He does not live in Heerlen')
# else:
#     pass

# print(type(address))


# # Numeric Operators
# print(13/2)  # returns float number
# print(13 // 2)  # returns integer number

# for i in range(1, 4):
#     print(i)

# for i in range(1, 17 // 4):
#     print(i)

# name = input('').split(',')
# for i in name:
#     print(i)

# online = False
# if online:
#     print('He is online')
# else:
#     print('He is offline')

# grade = 5.0
# result = 'Passed' if grade >= 3.0 else 'Failed'
# print(result)


# attempts = 10
# while attempts >= 0:
#     if attempts != 0:
#         print(f'Attempt: {attempts}')
#     elif attempts == 0:
#         print('No more attempts left!')
#     attempts = attempts - 1

# def print_function():
#     print('It is working!')


# print_function()


# def calculate_age_difference(my_age, her_age):
#     return my_age - her_age


# print('Age difference is:', calculate_age_difference(23, 22))


# keyword - key - value functions
# def student_info(**details):
#     print(f'Student Information: {details}')


# student_info(name='Kadir', id='474***', status='Active')


# def selected_student_ids(*ids):
#     print(f'Selected Student IDs: {ids}')


# selected_student_ids(4564, 1232, 1321, 42121, 1212)
# selected_student_ids('4746**, 47467**, 3737**'.split(','))


# def user_status(name='unknown', status='offline'):
#     return f'User {name} is currently {status}'

# imo_user1234 = user_status('Kadir', 'online')
# print(imo_user1234)


# #! Data Structures: List, Dict, Set, Tuple
# numbers = [1, 2, 3, 4, 5, 6]
# name_list = list('kadir')
# range_hundred = range(100)
# range_list = list(range(100))
# print(len(range_hundred))
# print(len(range_list))
# print(range_hundred)
# print(range_list)


# name = 'Kadir'
# for i in name:
#     print(i)

# for i in range(len(name)):
#     print(name[i])

# for n, i in enumerate(range(len(name))):
#     print(n + 1, name[i])

# name_list = list(name)
# for i in name_list:
#     print(i)

# numbers = [1, 2, 3, 4, 5, 6]
# for n in numbers:
#     print(n)


# for i in range(len(numbers)):
#     print(numbers[i])


# numbers = [1, 2, 3]
# print(numbers)

# numbers[2], numbers[1], numbers[0] = numbers[0], numbers[1], numbers[2]
# print(numbers)

#! ===============================
# append()
# insert(index, value)
# pop(index & no index)
# remove(value)
# del numbers[0:-1]
# clear()
# reverse()
# join()
#! ===============================

# numbers = list(range(100))
# print(len(numbers))

# numbers.clear()
# print(len(numbers))

# nums = ['1', '2', '3', '4', '5']
# print('-'.join(nums))
# print(', '.join(nums))

# ? =*=*=*=*=*=*=*=*=*=* Dictionary =*=*=*=*=*=*=*=*=*=*=*=

# user_info = {
#     'name': 'Kadir',
#     'age': 23,
#     'status': 'student',
#     'active': True
# }

# user_info = dict(name='Kadir', student=True, age=23)

# print(type(user_info))
# print(user_info['name'])
# print(user_info['student'])
# user_info['active'] = True
# user_info['address'] = 'Maastricht', 'Netherlands'

# print(user_info)
# print(type(user_info['address']))


# if 'city' in user_info:
#     print(user_info['city'])
# else:
#     user_info['city'] = 'Heerlen'

# print(user_info)

# print(user_info.get('is_working'))

# # print(user_info['is_working']) # gives an error
# # hence safe to use .get() function
# print(user_info.get('surname'))

#! =================================
# get()
# clear()
# fromkeys()
# items()
# keys()
# values()
# popitem()
# setdefault(key, value) -> setdefault(key)
# pop(key)
# pop(key, new_value) -> removes and assigns new value
# update()
# diction.update(new_diction)
#! =================================

# # printing keys only
# # for i in user_info:
# #     print(i)

# # # printing values only not keys
# # for i in user_info:
# #     print(user_info[i])
# # # print(user_info[key]) # ex: same as above


# # ? =*=*=*=*=*=*=*=*=*=* Tuples =*=*=*=*=*=*=*=*=*=*=*=
# # similar to lists, ordered, but once assigned we cannot change the elements of a tuple
# example_tuple = ()
# print(type(example_tuple))

# numbers = (1, 2, 3, 4, 5)
# print(numbers[1])

# # this is tuple too
# names = 'Kadir', 'Adil', 'Boy'
# numbers = 1, 2, 3, 4, 5
# print(numbers[1])

# num1, num2, num3, *num_plus = numbers

# # tuple with one element
# name = ('Kadir')  # string
# name = ('Kadir', )  # tuple
# name = 'Kadir',  # tuple
# number = 1,  # tuple

# print(type(name))
# print(type(number))

# print('Boy' in name)  # Boy is in name?

# del numbers
# number = ()
# del name

# #! ===============================
# # count(value)
# # index(value)
# # del
# #! ===============================

# # ? =*=*=*=*=*=*=*=*=*= Sets *=*=*=*=*=*=*=*=*=*=*=*=
# # sets are mutable, unordered, removes duplicates
# example_set = {1, 2, 3, 4, 4, 5, 5, 5}

# # creating a set from a tuple
# colors = set(('green', 'green', 'yellow'))
# # it removed duplicates so only unique values

# numbers = set()
# numbers.add(31)
# numbers.update(['Name', 'Surname'], (True, False))

# # discard(value) - even not exists
# numbers.discard(33)

# # remove(value) - error if not exists
# numbers.remove(31)

# # pop() - removes any random element
# numbers.pop()

# # clear() - clears the set
# numbers.clear()


# # print(2**32)

# numbers = input('Enter 5 numbers: ').split(' ')
# print('Returned a list: ', numbers)

# # * - unpacking operator
# print('Returned: ', *numbers)


# numbers = [1, 2, 3, 4, 5, 6]
# numbers = sorted(numbers, reverse=True)
# print(numbers)

# nums = [1, 2, 3, 4]
# nums.sort(reverse=True)
# print(nums)

# import sys

# try:
#     pass
# except ValueError as exp_error:
#     print(exp_error)
#     print(type(exp_error))
# else:
#     pass


# try:
#     age = int(input('Enter your age: '))
#     bonus = age * 0.057
#     not_zero = 100 / age
# except (ValueError, ZeroDivisionError) as exp_error:
#     print('Please enter a valid value', exp_error)
#     print('Error occured due to', type(exp_error))
# else:
#     print('Successfull Operation')


# class Student:
#     def __init__(self, name, surname, id, is_active):
#         self.name = name
#         self.surname = surname
#         self.id = id
#         self.is_active = is_active

#     def __str__(self):
#         return f'Hello'

#     def details(self):
#         print(f'Name: {self.name}, is active student: {self.is_active}')


# student_1405 = Student('Boy', 'Khamidov', 147641, True)
# print(student_1405)
# # student_1405.details()

# #! ================ Modules ====================

# import sys
# from functions import calculate_age
# from functions import output_basics
# import functions
# output_basics()
# print(calculate_age(2002, 2025))

# functions.output_basics()
# print(functions.calculate_age(2003, 2025))

# # * from folder_name.file_name import function_name
# # * import sys

# print(sys.path)
# #! ================ ------- ====================

# import webbrowser
# webbrowser.open('https://fmovies.co')

# from pathlib import Path

# path = Path()
# print(path)

# # ? home()
# print(Path.home())

# # ? exists(file_path) - if file/folder exists [True/False]
# print(path.exists())

# # ? absolute()
# print(path.absolute())

# # ? changing the extension of a file
# print(path3.with_suffix(".js"))


# #! Virtual Environment
# pip install pipenv
# pipenv - -version
# pipenv install requests  # or module_name
# pipenv shell
# exit  # or deactivate

# # this will create Pipfile and Pipfile.lock then pip install other libraries/modules


import statistics
import math


class Car:
    is_new = True
    is_used = False

    def __init__(self, name=None, brand=None, color=None, year=None):
        self.name = name if name else 'Default Name'
        self.brand = brand if brand else 'Default Brand'
        self.color = color if color else 'Default Color'
        self.year = year if year else 2025

    def get_car_info(self):
        return f'This is {self.name} manufactured by {self.brand} in {self.year}'


tesla_model_s = Car()
# assigning new attribute to class object
tesla_model_s.is_electric = True
car_info = tesla_model_s.get_car_info()
print(f'{car_info} and it operates in electricity' if tesla_model_s.is_electric else '{car_info} and it is not electric')


#! ------------------------------------------------------


class Calc:
    mem_list = []

    def __init__(self, name, producer, color):
        self.name = name
        self.name = name
        self.producer = producer
        self.color = color

    def add(self, a, b):
        self.mem_list.append(a+b)
        return a + b

    def substract(self, a, b):
        self.mem_list.append(a-b)

    def divide(self, a, b):
        self.mem_list.append(a//b)

    def multiply(self, a, b):
        self.mem_list.append(a*b)

    def __str__(self):
        return f"Here are the results: {self.name} {self.producer}, {self.color}"

    def print_me(self):
        for i in self.mem_list:
            print(i)


class Scientific_calc(Calc):
    def __init__(self, name, producer, color):
        Calc.__init__(self, name, producer, color)

    def log(self, a):
        self.mem_list.append(math.log(a))
        return math.log(a)

    def pow(self, a, b):
        self.mem_list.append(a**b)
        return a**b


class ExtraCalc(Calc):
    def __init__(self, name, producer, color, owner_name):
        Calc.__init__(self, name, producer, color)
        self.owner_name = owner_name

    def get_min_result(self):
        return min(self.mem_list)

    def get_mean_result(self):
        return statistics.mean(self.mem_list)

    def get_std_result(self):
        return statistics.stdev(self.mem_list)


random_value = Calc("Hmm", "Hmm", "red")
random_value.add(5, 5)
random_value.substract(5, 5)
random_value.divide(5, 5)
random_value.multiply(5, 5)

random_value.print_me()


rr_val = Scientific_calc("Hmm", "Hmm", "red")
print(rr_val.log(5))
print(rr_val.pow(5, 5))


r_val = ExtraCalc("Hmm", "Hmm", "Hmm", "Hmm")
print(r_val.get_min_result())
print(r_val.get_mean_result())
print(r_val.get_std_result())

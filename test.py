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

online = False
if online:
    print('He is online')
else:
    print('He is offline')

# Date Class

#! 1 ->>> Getting the current Date & Time
# from datetime import datetime
# print(datetime.now())

#! 2 ->>> Getting the current Date
# import datetime
# print(datetime.date.today())

#! 3 ->>> Getting the Datetime attributes
# import datetime
# print(dir(datetime))

#! 4 ->>> Creating a date object
# import datetime
# date = datetime.date(2024, 7, 2)
# print(date)
# print(type(date))

# ! 5 ->>> Importing the date class
# from datetime import date
# print(date(2024, 7, 2))

#! 6 ->>> Getting data from a timestamp
# from datetime import date
# time_stamp = date.fromtimestamp(1234567890)
# print(time_stamp)

#! 7 ->>> Getting today's year, month and day
# from datetime import date
# today = date.today()
import datetime
today = datetime.date.today()
print("Current Year: ", today.year)
print("Current Month: ", today.month)
print("Current Day: ", today.day)

# from datetime import date
# import datetime
# print(date.today())
# today = date.today()
# print("Current Year:", today.year)
# print("Current Month: ", today.month)
# print("Current Day: ", today.day)
# print(datetime.datetime.now())


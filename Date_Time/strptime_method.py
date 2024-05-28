# strptime() Method

from datetime import datetime

#! strptime()
date_str = "21 December, 2021"
print(date_str)
print(type(date_str))  # string

# we need to provide two args (string obj, date format)
date_obj = datetime.strptime(date_str, "%d %B, %Y")
print(date_obj)
print(type(date_obj))

#! String to datetime object
date_str = "11 Aug, 2019"

# if you provide wrong date format, it gives an error, ex: %d, %m, %Y
date_obj = datetime.strptime(date_str, "%d %b, %Y")
print(date_obj)
print(type(date_obj))

#! String to datetime object
date_str1 = "18/01/2002 19:10:10"  # dd/mm/yyyy
date_str2 = "12/31/2001 10:19:19"  # mm/dd/yyyy

# considering the date is in dd/mm/yyyy format
date_obj1 = datetime.strptime(date_str1, "%d/%m/%Y %H:%M:%S")
print(date_obj1)
print(type(date_obj1))

date_obj2 = datetime.strptime(date_str2, "%m/%d/%Y %H:%M:%S")
print(date_obj2)
print(type(date_obj2))

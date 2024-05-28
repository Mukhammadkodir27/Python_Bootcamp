# strftime() Method

#! Date Formats
# US ->>> mm/dd/yyyy
# UK ->>> dd/mm/yyyy

from datetime import datetime

#! Formatting date using strftime()
# current date & time
now = datetime.now()

time = now.strftime("%H:%M:%S")  # %H - hours, %M - minutes, %S - seconds
print(time)

# %d - day, %m - month, %Y - Year
full_date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
print(full_date_time)
# print(type(full_date_time))
#! datetime to string using strftime()
now = datetime.now()

year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")

print(year)
print(month)
print(day)

# print(year, end="/")
# print(month, end="/")
# print(day, end="")

#! creating string from a timestamp
timestamp = 4313259999
date_time = datetime.fromtimestamp(timestamp)

print(date_time)
# print(type(date_time)) class datetime

date = date_time.strftime("%d/%m/%Y, %H:%M:%S")
print(date)
# print(type(date)) class str

# read more about date and time on python docs and find more directives
# https://docs.python.org/3/library/datetime.html

date2 = date_time.strftime("%d %b, %Y")
print(date2)
print(now.strftime("%d %b, %Y"))

date3 = date_time.strftime("%d %B, %Y")
print(date3)

time2 = now.strftime("%I:%p")
print(time2)

#! locale's appropriate date and time
timestamp = 4599999999
date_time = datetime.fromtimestamp(timestamp)

d1 = date_time.strftime("%c")
print(d1)

# dd/mm/yyyy
d2 = date_time.strftime("%x")
print(d2)
dd2 = now.strftime("%x")
print(dd2)

# hh:mm:ss
d3 = date_time.strftime("%X")
print(d3)
dd3 = now.strftime("%X")
print(dd3)

#! python datetime to timestamp
now = datetime.now()

# converting to timestamp
time_stamp = datetime.timestamp(now)
print(time_stamp)

# converting from timestamp
date_time = datetime.fromtimestamp(time_stamp)
print(date_time)
print(date_time.strftime("%d %b %Y - %H:%M:%S"))

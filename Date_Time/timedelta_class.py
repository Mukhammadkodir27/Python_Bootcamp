# Timedelta Class

from datetime import timedelta, date, datetime

#! Difference between two dates and times

date1 = date(year=2024, month=5, day=28)
date2 = date(year=2005, month=4, day=17)

date3 = date1 - date2
print(date3)
# print(type(date3))


time1 = datetime(year=2024, month=5, day=28, hour=22, minute=27, second=34)
time2 = datetime(year=2002, month=7, day=2, hour=5, minute=22, second=22)

time3 = time1 - time2
print(time3)
# print(type(time3))

#! Difference between two timedelta objects
time_1 = timedelta(weeks=2, days=5, hours=1, seconds=33)
time_2 = timedelta(days=5, hours=11, minutes=12, seconds=33, microseconds=60)

time_3 = time_1 - time_2
print(time_3)

#! wrong!!!
# date_1 = timedelta(years=2024, months=5, days=28)
# date_2 = timedelta(years=2002, months=7, days=2)

#! Getting negative timedelta object
t1 = timedelta(seconds=33)
t2 = timedelta(seconds=54)

t3 = t1 - t2
print(t3)

#! Time duration in seconds
time = timedelta(days=110, hours=25, minutes=110, seconds=10000)
print("total seconds:", time.total_seconds())

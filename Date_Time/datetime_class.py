# Datetime Class

from datetime import datetime

now = datetime.now()
print(now)
today = datetime.today()
print(today)

print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hours:", now.hour)
print("Minutes:", now.minute)
print("Seconds:", now.second)
print("Seconds till this time:", now.timestamp())
print(datetime.fromtimestamp(now.timestamp()))

total_seconds = now.timestamp()
print(datetime.fromtimestamp(total_seconds))


#! Python datetime object
# these first three args are must to provide
time_1 = datetime(year=2024, month=12, day=23)
print(time_1)

time_2 = datetime(2024, 8, 24, 22, 22, 25)
print(time_2)

#! Getting year, month, hour, minute, second, timestamp
time_3 = datetime(2010, 10, 25, 23, 13, 50)
print("year:", time_3.year)
print("hour:", time_3.hour)

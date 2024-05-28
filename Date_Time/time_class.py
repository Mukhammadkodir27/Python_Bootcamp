# Time Class

from datetime import time

#! Time object to represent time
time_1 = time()
print("Time A:", time_1)

time_2 = time()
print("Time B:", time_2)

time_3 = time(hour=9, minute=51, second=15)
print("Time C:", time_3)

time_4 = time(13, 55, 23, 10000)
print("Time D:", time_4)

#! Getting hour, minute, second and microsecond
time_5 = time(hour=11, minute=34, second=56)

print("Hour:", time_5.hour)
print("Minute:", time_5.hour)
print("Second:", time_5.second)
print("Microsecond:", time_5.microsecond)

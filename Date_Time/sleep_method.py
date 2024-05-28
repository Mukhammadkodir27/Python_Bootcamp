# sleep() Method

import time

#! sleep()
print("Printed Immediately")
time.sleep(2.0)
print("Printed after 2 seconds delay")
time.sleep(1)
print("printed after a second")

#! local time
local_time = time.localtime()
result = time.strftime("%I:%M:%S", local_time)
result2 = time.strftime("%I %p", local_time)
print(result)
print(result2)


# when we use time.sleep() method the execution stops for a specific time period provided.
# it can be 1 second, 2 seconds or even 10 seconds. 
# it is useful while working with big data or large codebases. "to stop the execution for a while"

#! creating a simple low level digital clock
# while True:
#     local_time = time.localtime()
#     result = time.strftime("%H:%M:%S", local_time)
#     print(result)
#     time.sleep(1)

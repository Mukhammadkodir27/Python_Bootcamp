# Pip

# pip install --upgrade requests
# pip install requests

import os
import requests
from datetime import datetime
import pytz  # for timezone

response = requests.get("https://google.com")
print(response)

local = datetime.now()
print(os.getcwd())
print("Local Time:", local.strftime("%H:%M:%S"))

time_zone_NYC = pytz.timezone("America/New_York")
datetime_NYC = datetime.now(time_zone_NYC)
print("New York Time:", datetime_NYC.strftime("%H:%M:%S"))

tz_London = pytz.timezone("Europe/London")
datetime_London = datetime.now(tz_London)
print("London Time:", datetime_London.strftime("%H:%M:%S"))

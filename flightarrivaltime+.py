# -*- coding: utf-8 -*-
"""flightArrivalTime.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EUBxsGaIkapZrLp214aWqaEJc5tE-8oJ
"""

# Flight Arrival Time

from datetime import datetime, timedelta
from dateutil import tz

destination = input("TZ code for the sestination: ")
now = datetime.now(tz.gettz(destination))
destination_time = datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
now = datetime.now(tz.gettz("Asia/Seoul"))
orgin_time = datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)

td = origin_time - destination_time
tlist = list(map(int, input("Input the departure time (YYYY:MM:DD:HH:MM:SS): ").split(":")))
dpt_time = datetime(tlist[0], tlist[1], tlist[2], tlist[3], tlist[4], tlist[5])
f_time = list(int, input("Flight time (HH:MM): ").split(":"))
arv_time = dpt_time + timedelta(hours = f_time[0], minutes = f_time[1]) - td
print("Will arrive at the destination at", arv_time)
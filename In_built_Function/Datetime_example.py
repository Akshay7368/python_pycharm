
import datetime as dt
from datetime import *


current_time = dt.datetime.now()
print(current_time)

current_day = dt.date.today()
print(current_day)
'''
print(current_time.year)
print(current_time.month)
print(current_time.day)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)
print(current_time.weekday())
print(current_time.isoweekday())
print(weekday,current_time)
'''
my_date = dt.date(2022, 6, 21)
print(my_date)

my_time = dt.time(11, 25, 45, 8000)
print(my_time)

my_date_time = dt.datetime.combine(my_date, my_time)
print(my_date_time)

hour_replace = my_date_time.replace(hour=12)
print(hour_replace)

hour_replace = my_date_time.replace(minute=45)
print(hour_replace)

hour_replace = my_date_time.replace(month=9)
print(hour_replace)

time_delta_ex = my_date_time+dt.timedelta(days=5)
print(time_delta_ex)

time_delta_ex = my_date_time+dt.timedelta(days=50)
print(time_delta_ex)

time_delta_ex = my_date_time+dt.timedelta(weeks=12)
print(time_delta_ex)

print(time_delta_ex.strftime("%Y-%m"))
print(time_delta_ex.strftime("%y-%m"))
print(time_delta_ex.strftime("%Y-%B"))
print(time_delta_ex.strftime("%Y-%b"))
print(time_delta_ex.strftime("%Y/%B/%d"))
print(time_delta_ex.strftime("%Y/%B/%d %H:%M:%S"))
print(time_delta_ex.strftime("%Y/%B/%d %I:%M:%S"))
print(time_delta_ex.strftime("%Y/%b/%d %I:%M:%S %p"))
print(time_delta_ex.strftime("%A"))
print(time_delta_ex.strftime("%a"))

print(time_delta_ex.strftime("%B,%d,%Y %I:%M:%S"))















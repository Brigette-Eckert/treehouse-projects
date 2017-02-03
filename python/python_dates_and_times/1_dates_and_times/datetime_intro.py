import datetime



treehouse_start = datetime.datetime.now()
print(treehouse_start)

#both ways of creating new dates
treehouse_start = treehouse_start.replace(hour = 16, minute = 40, second = 0, microsecond= 0)
print(treehouse_start)

th_start = datetime.datetime(2017, 2, 2, 16, 40)
print(th_start)

time_worked = datetime.datetime.now()- treehouse_start
print(time_worked)

print(time_worked.days)
print(time_worked.microseconds)

hours_worked = round(time_worked.seconds/3630)
print(hours_worked)
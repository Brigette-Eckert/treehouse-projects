import datetime

now = datetime.datetime.now()

delta_hours = datetime.timedelta(hours=5)
print(delta_hours)

delta_days = datetime.timedelta(days = 3)
print delta_days

print(now + delta_days)

#can minuplate date time with operators
# extact same number either way
print(now + datetime.timedelta(days = -5))
print(now - datetime.timedelta(days = 5))

just_date = now.date()
print(just_date)

just_time = now.time()
print(just_time)

appointment = datetime.timedelta(minutes = 45)
start = datetime.datetime(2017, 2, 3, 9, 30)
end = start + appointment
print(end)



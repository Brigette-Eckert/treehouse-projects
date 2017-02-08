import datetime

# offset from UTC
pacific = datetime.timezone(datetime.timedelta(hours = -8))
eastern = datetime.timezone(datetime.timedelta(hours = -5))
aucklund = datetime.timezone(datetime.timedelta(hours = 13))
mumbai = datetime.timezone(datetime.timedelta(hours = 5, minutes = 30))
naive = datetime.datetime(2017, 2, 8, 8, 30)
aware = datetime.datetime(2017, 2, 8, 8, 30, tzinfo=pacific)

print(naive)
print(aware)

#can't use astime zone on naive date - will return error

print(aware.astimezone(eastern))
print(aware.astimezone(aucklund))
print(aware.astimezone(mumbai))
import datetime


now = datetime.datetime.now()
print(now)

# strf time is string from time/ string formatted time

print(now.strftime('%B %d'))
print(now.strftime('%m/%d/%y'))


# strp time is string parsed into time

birthday = datetime.datetime.strptime('2017-03-19', '%Y-%m-%d')

print(birthday)

# can use flag for am/pm instead of using 24 time
birthday_party = datetime.datetime.strptime('2017-03-19 19:30', '%Y-%m-%d %H:%M')
print(birthday_party)
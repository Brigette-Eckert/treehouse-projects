import datetime
import pytz

pacific = pytz.timezone('US/Pacific')
eastern = pytz.timezone('US/Eastern')
auckland = pytz.timezone('Pacific/Auckland')
mumbai = pytz.timezone('Asia/Calcutta')
fmt = '%Y-%m-%d %H:%M:%S %Z%z'
utc = pytz.utc

# localize is for naive datetimes
start = pacific.localize(datetime.datetime(2017, 2, 8, 9, 30))
start_eastern = start.astimezone(eastern)
start_utc = datetime.datetime(2017, 2, 8, 9, 30, tzinfo=utc)
start_pacific = start_utc.astimezone(pacific)
apollo_13_naive = datetime.datetime(1979, 4, 11, 14, 13)
apollo_13_eastern = eastern.localize(apollo_13_naive)
apollo_13_utc = apollo_13_eastern.astimezone(utc)
apollo_13_pacific = apollo_13_utc.astimezone(pacific).strftime(fmt)
apollo_13_auckland = apollo_13_utc.astimezone(auckland).strftime(fmt)
apollo_13_mumbai = apollo_13_utc.astimezone(mumbai).strftime(fmt)

print(" start fmt: {}".format(start.strftime(fmt)))
print(" start eastern: {}".format(start_eastern))
print(" start utc: {}".format( start_utc.strftime(fmt)))
print(" start pacific: {}".format(start_pacific))
print(" start apollo naive: {}".format( apollo_13_naive))
print (" apollo eastern: {}".format(apollo_13_eastern))
print(" apollo utc: {}".format(apollo_13_utc))
print(" apollo pacific: {}".format(apollo_13_pacific))
print(" apollo mumbai: {}".format(apollo_13_mumbai))
print(" apollo auckland: {}".format(apollo_13_auckland))
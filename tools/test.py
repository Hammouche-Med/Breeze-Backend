from datetime import datetime
import calendar

# metar = [ "hjklk", "jlkn", "03", "18","30" ]

# m = datetime.now().strftime('%m')
# y = datetime.now().strftime('%Y')

# obs = metar[2]+"-"+m+"-"+y

# obs_date = datetime.strptime("06:00:00", '%H:%M:%S')
# rec_date = datetime.strptime("07:36:00", '%H:%M:%S')

# difff = rec_date - obs_date
# diff = (difff.total_seconds() / 60) - 60

# print(diff)

# if diff <=  3 :
#     print (diff," ph5")
# elif diff <= 5 :
#     print(diff," ph10")
# elif diff <= 33:
#     print(diff," ph33")
# elif diff <= 49:
#     print(diff," ph49")
# else :
#     print(diff,' omis') 



now = datetime.now()
if calendar.isleap(2024):
    num = 366
else:
    num = 365
print(num)
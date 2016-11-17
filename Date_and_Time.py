
#1.
import calendar

date_string=input().split()
Date=[int(date) for date in date_string] #Converting into Integer, as the input was initially a String
month=Date[0]
day=Date[1] 
year=Date[2]
week_day=calendar.day_name[calendar.weekday(year,month,day)] #Getting Weekday Using Builtin Function
print(week_day.upper())
#2.
from datetime import datetime 

fmt = '%a %d %b %Y %H:%M:%S %z' #Format for the Input
test_cases=int(input())
for i in range(test_cases):
    time1=input()
    time2=input()
    difference=(datetime.strptime(time1,fmt))-(datetime.strptime(time2,fmt))
    print(int(abs(difference.total_seconds())))

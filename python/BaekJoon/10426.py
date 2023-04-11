import datetime

mydate, celebrate = input().split()
yy, mm, dd = map(int, mydate.split('-'))
celebrate = int(celebrate) - 1
dday = datetime.datetime(yy, mm, dd)
dday = dday + datetime.timedelta(days = celebrate)

print(dday.strftime("%Y-%m-%d"))
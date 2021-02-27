import calendar

ans = input('Do you want calendar for a year or a specific month (y/m): ')
if ans == 'y':
  y = int(input("the year you want calendar of: "))
  print(calendar.calendar(y))

elif ans == 'm':
    yy = int(input("the year : "))
    mm = int(input("the numerical no. of the month: "))
    print(calendar.month(yy,mm))
else:
  print("please input y or m depending on what you want")

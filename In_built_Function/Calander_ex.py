import calendar
yy = 2022
mm = 2
# print(calendar.month(yy, mm))
# print(calendar.calendar(yy))
# mon = input("Enter the month:")
# print(calendar.calendar(2025))
# print(calendar.monthrange(2025,8))


yy = int(input("Enter the year: "))
mm = int(input("Enter the Month: "))

if mm == 12:
    print("Previous Month:")
    print(calendar.month(yy,mm-1))
    print("Current Month:")
    print(calendar.month(yy,mm))
    print("Next Month:")
    print(calendar.month(yy+1, 1))

else:
    print("Previous Month:")
    print(calendar.month(yy, mm - 1))
    print("Current Month:")
    print(calendar.month(yy, mm))
    print("Next Month:")
    print(calendar.month(yy,mm+1))


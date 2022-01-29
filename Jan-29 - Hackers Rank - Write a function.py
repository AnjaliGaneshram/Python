year_1 = int(input("Enter the year: "))
year_2 = int(year_1/100)
if year_1%4 == 0 and year_1%400 ==0:
    print(year_1%4 == 0 and year_1%400 ==0,"It's a leap year")
elif year_1%4==0 and year_1%100!=0:
    print(year_1%4==0 and year_1%100!=0,"It's a leap year")
else:
    print(year_1%4==0 and year_1%100!=0, "It's not a leap year")
''' This program is to identify whether the given year is a leap year according to Gregorian calendar.'''    


import sys

def is_leap(year):
    leap = False
    if year % 4 == 0 and year % 100 != 0 :
        leap = True
    elif  year % 4 == 0 and  year % 100 == 0 and year % 400 == 0 :
        leap = True
    else:
        leap = False
    return leap



year = int(input())

if 1900<= year <=10**5:
    print(is_leap(year))

else:
    print("error")



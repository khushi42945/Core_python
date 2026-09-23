# 1.Leap Year and Century Checker
# Problem Statement:
# Without using any built-in date/time libraries, write a program to check whether a given year is a Leap Year and determine if it is a Century Year.
# Rule: A year is a leap year if it is divisible by 4, but not by 100, unless it is also divisible by 400.

year = int(input("enter a year"))
if year %100 ==0:
    print("century year")
else:
    print("not a century year")

if(year%400==0)or(year%4==0 and year%100!=0):
    print("leap year")
else:
    print("not a leap year")
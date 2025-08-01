# a year is leap year if it is divisible by 4 and not divisible by 100
year = int(input())

if year%4 ==0 and year%100 !=0 or year%400 ==0:
    print("leap year")
else:
    print("no")
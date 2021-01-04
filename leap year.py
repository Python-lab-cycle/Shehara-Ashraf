print("print leap year between two given years")
print("enter start year")
startYear = int(input())
print("enter last year")
endYear = int(input())
print("list of leap years")
#loop through between the start and end year
for year in range(startYear, endYear):
    #check if the year is a leap year if yes print
    if((year%4==0) and (year%100!=0) or (year%400==0)):
        print(year)

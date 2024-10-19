def checkYear(year) :
    if year % 4 == 0 and year % 100 != 0 :
        return 1
    elif year % 400 == 0 :
        return 1
    return 0


y = int(input())

print(checkYear(y))
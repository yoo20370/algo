
# 삼각형 두 변의 길이의 합은 나머지 한 변의 길이보다 크다.

while True :
    x, y, z = map(int, input().split())
    if x == y == z == 0 :
        break 
    listA = [x,y,z]

    listA.sort(reverse=True)

    x, y, z = listA
    if x < y + z :
        if x == y == z :
            print("Equilateral")
        elif x == y or y == z or x == z :
            print("Isosceles")
        else :
            print("Scalene")
    else :
        print("Invalid")
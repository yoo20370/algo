# X = int(input())
# Y = int(input())
# Z = int(input())

# if X == Y and Y == Z and X == 60 :
#     print("Equilateral")
# elif (X + Y + Z) // 3 == 60 and (X == Y and X != Z or Y == Z and Y != X or X == Z and X != Y) :
#     print("Isosceles")
# elif (X + Y + Z) // 3 == 60 and X != Y and X != Z :
#     print("Scalene")
# else :
#     print("Error")

X = int(input())
Y = int(input())
Z = int(input())

if X + Y + Z != 180 :
    print("Error")
else :
    if X == Y == Z :
        print("Equilateral")
    elif X == Y or Y == Z or X == Z :
        print("Isosceles")
    else :
        print("Scalene")
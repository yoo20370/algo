
# def func(ch) :
#     if ch == 'A' or ch ==  'B' or ch == 'C' :
#         return 2
#     elif ch == 'D' or ch ==  'E' or ch == 'F' :
#         return 3
#     elif ch == 'G' or ch ==  'H' or ch == 'I' :
#         return 4
#     elif ch == 'J' or ch ==  'K' or ch == 'L' :
#         return 5
#     elif ch == 'M' or ch ==  'N' or ch == 'O' :
#         return 6
#     elif ch == 'P' or ch ==  'Q' or ch == 'R' or ch == 'S' :
#         return 7
#     elif ch == 'T' or ch ==  'U' or ch == 'V' :
#         return 8
#     elif ch == 'W' or ch ==  'X' or ch == 'Y' or ch == 'Z' :
#         return 9

# string = input()
# length = len(string)

# sum = 0
# for i in range(length) :
#     sum += func(string[i])
# sum += length
# print(sum)

dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

word = input()

sum = 0
for i in range(len(word)) :
    for j in range(len(dial)) :
        if word[i] in dial[j] :
            sum += j + 3
print(sum)
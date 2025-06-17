import sys

number_count = int(sys.stdin.readline().rstrip())

number_list = [0] * (number_count + 1)
for _ in range(number_count) :
    data = int(sys.stdin.readline().rstrip())
    number_list[data] += 1


for index in range(1, number_count) :
    cnt = number_list[index]
    if cnt != 0 :
        for _ in range(cnt) :
            print(index)


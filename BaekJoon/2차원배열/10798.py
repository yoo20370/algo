
# pan = [[""] * 15 for i in range(5)]

# # 입력
# for i in range(5) :
#     dataList = input()

#     for j in range(len(dataList)) :
#         pan[i][j] = dataList[j]

# # 출력 

# string = ""
# for i in range(15) :
#     for j in range(5) :
#         string += pan[j][i]

# print(string)

pan = [input() for _ in range(5)]

for i in range(15) :
    for j in range(5) :
        if i < len(pan[j]) :
            print(pan[j][i], end="")
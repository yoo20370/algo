# import sys 

# N = int(sys.stdin.readline().rstrip())

# topList = list(map(int, sys.stdin.readline().split()))

# def sendSignal(topList) :
#     result = [0 for i in range(len(topList))]

#     for i in range(len(topList)) :
#         for j in range(i - 1, -1, -1):
#             if topList[i] <= topList[j] :
#                 result[i] = j + 1
#                 break

#     return result


    

# for i in sendSignal(topList) :
#     print(i, end =" ")


top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):

    answer = [0] * len(heights)
    for i in range(len(heights)-1, 0, -1):
        for j in range(i-1, -1, -1):
            if heights[i] <= heights[j]:
                answer[i] = j + 1
                break
    return answer 

print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ",get_receiver_top_orders([6,9,5,7,4]))
print("정답 = [0, 0, 0, 3, 3, 3, 6] / 현재 풀이 값 = ",get_receiver_top_orders([3,9,9,3,5,7,2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ",get_receiver_top_orders([1,5,3,6,7,6,5]))
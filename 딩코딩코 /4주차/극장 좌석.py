# import sys
# from collections import deque 
# MX = 41

# seat_count = int(sys.stdin.readline().rstrip())

# vip_count = int(sys.stdin.readline().rstrip())
# vip_list = []

# for _ in range(vip_count) :
#     vip_list.append(int(sys.stdin.readline().rstrip()))

# def theater_seat(seat_count, vip_count, vip_list) :

#     dp = [0] * MX 

#     dp[0] = 1
#     dp[1] = 1
#     dp[2] = 2

#     # 좌석수별 경우의 수 
#     for i in range(3, MX) :
#         dp[i] = dp[i-2] + dp[i-1]

#     if seat_count == vip_count :
#         return 1
    
#     if vip_count == 0 :
#         return dp[seat_count]
    
#     seat_list = [i for i in range(seat_count + 1)]

#     queue = deque(seat_list)
#     queue.popleft()
    
#     total_count = 1
#     for end in vip_list :
#         count = 0 

#         while queue[0] != end :
#             queue.popleft()
#             count += 1

#         if count != 0 :
#             total_count *= dp[count]
#         queue.popleft()

#     if count != 0 :
#         total_count *= dp[len(queue)]

#     return total_count

# print(theater_seat(seat_count, vip_count, vip_list))


seat_count = 9
vip_seat_array = [4, 7]


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    return


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))

print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9,[2,4,7]))
print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11,[2,5]))
print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10,[2,6,9]))


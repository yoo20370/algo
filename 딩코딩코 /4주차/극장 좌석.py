import sys
from collections import deque 
MX = 41

seat_count = int(sys.stdin.readline().rstrip())

vip_count = int(sys.stdin.readline().rstrip())
vip_list = []

for _ in range(vip_count) :
    vip_list.append(int(sys.stdin.readline().rstrip()))

def theater_seat(seat_count, vip_count, vip_list) :

    dp = [0] * MX 

    dp[1] = 1
    dp[2] = 2

    # 좌석수별 경우의 수 
    for i in range(3, MX) :
        dp[i] = dp[i-2] + dp[i-1]

    if seat_count == vip_count :
        return 1
    
    if vip_count == 0 :
        return dp[seat_count]
    
    seat_list = [i for i in range(seat_count + 1)]

    queue = deque(seat_list)
    queue.popleft()
    
    total_count = 1
    for end in vip_list :
        count = 0 

        while queue[0] != end :
            queue.popleft()
            count += 1

        if count != 0 :
            total_count *= dp[count]
        queue.popleft()

    if count != 0 :
        total_count *= dp[len(queue)]

    return total_count

print(theater_seat(seat_count, vip_count, vip_list))


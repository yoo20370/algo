seat_count = 9
vip_seat_array = [4, 7]

# VIP는 반드시 자신의 좌석에 앉아야 함 
# 그 외에 좌석은 왼쪽 혹은 오른쪽으로 옮길 수 있음

# 마지막 좌석 사용자가 자기 자리에 앉는 경우 f(n-1)
# 마지막 좌석 사용자가 왼쪽 자리와 좌석을 자꾼 경우 f(n-2)

# 여기서 중요한 건 VIP 위치가 중요함
# 어떤 경우가 있을까 ??
# 모든 좌석이 VIP인 경우
# 모든 좌석이 VIP가 아닌 경우
# VIP 좌석이 연속으로 나오는 경우 

def seatCaseCount(dp, n) :

    if dp[n] != 0 :
        return dp[n]
    
    dp[n] = seatCaseCount(dp, n-1) + seatCaseCount(dp, n -2)
    return dp[n]


def get_all_ways_of_theater_seat(total_count, fixed_seat_array) :

    dp = [0] * (total_count + 1)

    # 모두 VIP인 경우와 좌석이 한 가지인 경우, 한 가지 밖에 없음  
    if total_count == len(fixed_seat_array) or total_count == 1 :
        return 1 

    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    # 모든 좌석이 VIP가 아닌 경우 
    if len(fixed_seat_array) == 0 :
        return seatCaseCount(dp, total_count)
    
    startSeat = 1 

    seatCountList = []

    for endSeat in fixed_seat_array :
        seatCount = endSeat - startSeat
        seatCountList.append(seatCount)
        startSeat = endSeat + 1


    # 마지막 좌석이 VIP가 아닌 경우
    ## 마지막 좌석이 startSeat인 경우
    ## 마지막 좌석은 중간Seat인 경우
    if startSeat < total_count + 1 :
        endSeat = total_count + 1
        seatCount = endSeat - startSeat
        seatCountList.append(seatCount)


    # 마지막 좌석이 VIP인 경우 
    ## 마지막 좌석이 VIP인 경우 startSeat가 total_count + 1일 것임 
    ### 굳이 넣을 필요가 없음 
    totalSeatCaseCount = 1
    for currentSeatCount in seatCountList :
        totalSeatCaseCount *= seatCaseCount(dp, currentSeatCount)

    return totalSeatCaseCount

# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))

print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9,[2,4,7]))
print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11,[2,5]))
print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10,[2,6,9]))
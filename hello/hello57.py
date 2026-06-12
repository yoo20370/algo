import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    # 남은 재고가 4개인데 
    # 4일차에 공급을 받을 수 있음 
    # 즉 재고가 stock >= K가 되는 순간 종료
    maxHeap = []

    suppliedDates = set()

    count = 0 
    while stock < k :

        # 가능한 모든 공급을 넣음 
        for index in range(len(dates)) :
            date = dates[index]

            if date <= stock and date not in suppliedDates :
                heapq.heappush(maxHeap, -supplies[index])
                suppliedDates.add(date) 

        # 한 번 공급 받음 
        supplyStock = heapq.heappop(maxHeap)
        stock += -supplyStock
        count += 1

    
    return count


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
print("정답 = 2 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 4 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print("정답 = 1 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))

# 경계값 테스트 케이스들

# 1. stock = k (이미 충분한 경우)
print("정답 = 0 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(10, [5], [20], 10))

# 2. stock = 0 (재고 완전 바닥)
print("정답 = 2 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(0, [0, 10, 15], [20, 10, 15], 35))

# 3. 딱 한 번만 공급받으면 되는 경우
print("정답 = 1 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(5, [5], [30], 30))

# 4. 공급 후 stock이 정확히 k가 되는 경우
print("정답 = 1 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(10, [10], [20], 30))

# 5. 첫날부터 공급 가능한 경우
print("정답 = 1 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(0, [0], [100], 50))

# 6. k = 1 (최소 기간)
print("정답 = 1 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(0, [0], [10], 1))

# 7. 여러 번 공급받아야 하고 딱 맞아떨어지는 경우
print("정답 = 3 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(0, [0, 5, 10], [5, 5, 5], 15))

# 8. 공급 가능 날짜가 여러 개지만 하나만 선택해야 하는 경우
print("정답 = 1 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(5, [5, 6, 7], [100, 10, 10], 50))

# 9. 마지막 날에 공급받는 경우
print("정답 = 2 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(10, [10, 29], [20, 100], 30))

# 10. stock이 k보다 1 작은 경우
print("정답 = 1 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(29, [29], [100], 30))
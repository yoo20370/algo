import heapq
from collections import deque
ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


# 필요한 개수를 카운트
# 현재 재고로 버티면서 가장 많이 받을 수 있는 수입을 선택해야 함 
# -> stock 값으로 dates를 순회하면서 heap에 삽입한다. 
# heap에서 재고를 꺼내 stock에 추가한 후, 필요한 개수를 넘는지 확인, 넘지 않았다면, heap에서 재고를 또 꺼내 heap이 바닥날 때까지 반복
# 그럼에도 불구하고 재고가 채워지지 않았다면 또 현재 재고를 기반으로 dates를 순회하면서 heap에 삽입 
# 위 과정 반복 

def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    dates_queue = deque(dates)
    supplies_queue = deque(supplies)

    total_count = 0
    while stock < k :
        heap = []

        while dates_queue and dates_queue[0] <= stock :
            dates_queue.popleft()
            heapq.heappush(heap, -supplies_queue.popleft())
        
        
        while stock < k and heap :
        
            total_count += 1
            stock += -heapq.heappop(heap)
            
     
    return total_count

print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
print("정답 = 2 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 4 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print("정답 = 1 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))



ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


# 필요한 개수를 카운트
# 현재 재고로 버티면서 가장 많이 받을 수 있는 수입을 선택해야 함 
# -> stock 값으로 dates를 순회하면서 heap에 삽입한다. 
# heap에서 재고를 꺼내 stock에 추가한 후, 필요한 개수를 넘는지 확인, 넘지 않았다면, heap에서 재고를 또 꺼내 heap이 바닥날 때까지 반복
# 그럼에도 불구하고 재고가 채워지지 않았다면 또 현재 재고를 기반으로 dates를 순회하면서 heap에 삽입 
# 위 과정 반복 

def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):

    total_count = 0
    curr_index = 0
    while stock < k :
        heap = []

        while curr_index < len(dates) and dates[curr_index] <= stock :
            heapq.heappush(heap, -supplies[curr_index])
            curr_index += 1

        while stock < k and heap :
            total_count += 1
            stock += -heapq.heappop(heap)

    return total_count

print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
print("정답 = 2 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 4 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print("정답 = 1 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))

















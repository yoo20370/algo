import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):

    # 힙에 모든 [date, supply] 형태로 모두 넣는다.
    # 공급일 까지 몇 개의 밀가루가 필요한지 계산한다. 
    # 힙에서 하나씩 꺼내며, 공급일까지 필요한 밀가루 개수 -1개 보다 많거나 같은지 비교해야한다. 
    # 왜 -1개까지냐면 부족한 날에 밀가루가 들어오기 때문 

    heap = []
    need_amount = k - stock
    for index in range(len(dates)) :
        date = dates[index]
        supply = supplies[index]

        heapq.heappush(heap, (-supply, date))
    
    
    supply_count = 0
    curr_stock = 0
    while curr_stock < need_amount :
        amount, date = heapq.heappop(heap)
        curr_amount = - amount
        curr_stock += curr_amount
        supply_count += 1

    return supply_count


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
print("정답 = 2 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 4 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print("정답 = 1 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))
import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30

def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    
    # 재고를 보고 버틸 수 있는 날짜들의 수량을 가져온다.
    # MaxHeap에서 하나씩 뽑아 재고에 더한 후 k - 1 보다 큰지 확인 한다.
    # 만약 크다면 count한 개수를 반환하고
    # 만약 작다면 heapq가 빌 때까지 반복한다.
    # 아직 k까지 버틸 수 없다면 처음으로 돌아간다. 

    count = 0
    date_index = 0 
    while stock <= k :

        heap = []
        while date_index < len(dates) and stock >= dates[date_index] :
            heapq.heappush(heap, - supplies[date_index])
            date_index += 1
            

        while heap :
            amount = heapq.heappop(heap)
            count += 1  
            stock -= amount
        
            if stock >= k:
                return count
            
    return count

print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
print("정답 = 2 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 4 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print("정답 = 1 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))

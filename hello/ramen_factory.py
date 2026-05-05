# Q. 라면 공장에서는 하루에 밀가루를 1톤씩 사용합니다. 원래 밀가루를 공급받던 공장의 고장으로 앞으로 k일 이후에야 밀가루를 공급받을 수 있기 때문에 해외 공장에서 밀가루를 수입해야 합니다.
# 해외 공장에서는 향후 밀가루를 공급할 수 있는 날짜와 수량을 알려주었고, 라면 공장에서는 운송비를 줄이기 위해 최소한의 횟수로 밀가루를 공급받고 싶습니다.
# 현재 공장에 남아있는 밀가루 수량 stock, 밀가루 공급 일정(dates)과 해당 시점에 공급 가능한 밀가루 수량(supplies), 
# 원래 공장으로부터 공급받을 수 있는 시점 k가 주어질 때, 밀가루가 떨어지지 않고 공장을 운영하기 위해서 최소한 몇 번 해외 공장으로부터 밀가루를 공급받아야 하는지를 반환 하시오.
# dates[i]에는 i번째 공급 가능일이 들어있으며, supplies[i]에는 dates[i] 날짜에 공급 가능한 밀가루 수량이 들어 있습니다.

# k일 이후에 공급 받을 수 있음, 부족한 부분은 수입
# 밀가루를 공급할 수 있는 날짜와 수량 알려줌, 
### 최소한 횟수로 밀가루 공급 받고 싶음 
# 남아 있는 밀가루 stock
# 밀가루 공급 일정 dates
# 공급 가능한 밀가루 수량

# 어떻게 풀어야 할까 ? 
# 공급일에 두 가지 선택지가 있음, 받을 것인지, 받지 않을 것인지
# 만약 다음 공급일까지 버티지 못한다면 바로 받아야 함 -> 공장 중단되기 떄문 
# 만약 다음 공급일까지 버틸 수 있다면 현재 받을지, 아니면 다음에 받을지를 고려해야 함 

# 5 6 7 8 9 10 11 12 13 14

# 15 16 17 18 19 20 21 22 23 24

# 25 26 27 28 29 30(들어오니까 가능)

# 30 - 1일까지만 버틸 수 있으면 되는거네 ?? 예를 들어 

# 현재 밀가루 재고가 당일 이전까지만 버틸 수 있으면 되는거네 
# 현재 재고를 바탕으로 몇 개의 재고가 필요한지 확인 
# supply_recover_k - rame_stock - 1 (당일에 공급되기 때문에 없어도 됨) - 총 필요한 수 
# 내가 생각한 문제 풀이는 일단 가장 가까운 날짜까지 버틸 수 있느냐를 확인 
# 버틸 수 있다면 그 날 공급되는 수량을 가지고 언제까지 버틸 수 있는지를 확인, 이 중 가장 큰 값만 받을 수 있으면 되는거 아닌가 ?? 
# 현재 밀가루를 기준으로 가능한 dates를 가져온다. 


# 언제까지 반복 -> 남은 개수가 0보다 큰 경우 
# 현재 남은 재고를 바탕으로 날짜를 카운트 -> [공급 가능한 날짜, 공급수] 형태로 최대힙에 삽입 
# 공급 받은 후, 공급일들 다시 최대 힙에 삽입 

ramen_stock = 4
supply_dates = [4, 10, 15] # 해외 공장, 공급일
supply_supplies = [20, 5, 10] # 해외 공장 공급 수량 
supply_recover_k = 30 # 원래 공급 일 

import heapq
from collections import deque 

# 결국 반복문은 공급을 다 할 수 있으면 끝나면 됨
# 오늘로부터 필요한 총 수량 = supply_recover_k - remain_stock - 1 (당일에는 공급 받을 수 있음)
# 만약 아직 공급을 받아야 한다면, 아래의 과정을 수행한다.
# dates에서 현재 수량으로 견딜 수 있는 날짜 안에 있는 녀석들을 모두 heap에 삽입
# 그리고 최대힙에서 꺼내어 계산
# 다시 처음부터 제 계산 수행 

def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    
    require_stock = k - stock # 받는 당일에는 공급되기 때문에 괜찮
    current_date = stock # 남은 개수 일만큼 버틸 수 있음 

    dates = deque(dates)
    supplies = deque(supplies)

    count = 0

    heap = []

    # 현재 날짜 보다 이전인 날짜들에 대해서 최대힙에 삽입 -공급개수
    while require_stock > 0 : 
        
        while dates :
            if dates and dates[0] <= current_date :
                date = dates.popleft()
                supply = supplies.popleft()

                heapq.heappush(heap, -supply)
            else : 
                break 
        
        # 이제 뽑아서 한 번 카운트해줘야 함
        supply = heapq.heappop(heap)

        supply = -supply 
        current_date += supply
        require_stock -= supply 
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
print("정답 = 1 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(10, [10, 29], [20, 100], 30))

# 10. stock이 k보다 1 작은 경우
print("정답 = 1 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(29, [29], [100], 30))
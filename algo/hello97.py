import heapq

def solution(food_times, k):
    
    if sum(food_times) <= k :
        return -1
    
    priority_queue = []
    for index in range(len(food_times)) :
        heapq.heappush(priority_queue, (food_times[index], index + 1))
        
    sum_value = 0
    previous = 0
    
    length = len(food_times)
    
    while sum_value + (priority_queue[0][0] - previous) * length <= k :
        now = heapq.heappop(priority_queue)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now
    
    priority_queue.sort(key=lambda x : x[1])
    return priority_queue[(k - sum_value) % length][1]
        

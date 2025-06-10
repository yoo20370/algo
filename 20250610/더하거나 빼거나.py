from collections import deque

# numbers = [1, 1, 1, 1, 1]
# target_number = 3

# def func(array, target, index, sum) :
#     if len(array) == index :
#         return 1 if sum == target else 0 
    
#     plus = func(array, target, index + 1, sum + numbers[index])
#     minus = func(array, target, index + 1, sum - numbers[index])

#     return plus + minus
# def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
#     return func(array, target, 0, 0)

# print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!!


numbers = [1, 1, 1, 1, 1]
target_number = 3

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    # bfs, 너비 우선 탐색을 이용해서 구현해보자 
    # 큐에 인덱스와 현재 합을 저장한다. [0,1], [0,-1]
    # 값을 꺼내서 인덱스를 1 더하고 또 더하기 빼기를 진행한다. [1, 0], [1,2], [1, 0], [1, -1]
    # 방문처리가 필요 없는 이유는 한 쪽으로만 이동하기 때문 

    count = 0

    queue = deque()
    queue.append([0, + array[0]])
    queue.append([0, - array[0]])

    while queue :
        curr_index, curr_sum = queue.popleft()

        curr_index += 1
        if curr_index != len(array) :
            queue.append([curr_index, curr_sum + array[curr_index]])
            queue.append([curr_index, curr_sum - array[curr_index]])
        
        else : 
            if target == curr_sum :
                count += 1

    return count

print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!


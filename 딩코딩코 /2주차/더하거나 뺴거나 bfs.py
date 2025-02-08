from collections import deque

numbers = [1, 1, 1, 1, 1]
target_number = 3


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):

    # 현재 인덱스를 두고 배열을 순회한다.
    # 큐에 첫 번째 인덱스 원소를 인덱스와 누적합을 저장 후 방문 처리 한다. 
    
    # 방문처리 어떻게 할거야 ??  -> 인덱스가 배열의 길이와 같다면 안 넣으면 된다.
    count = 0 
    queue = deque()
    queue.append((0, array[0]))
    queue.append((0, -array[0]))

    while queue :
        curr_index, curr_sum = queue.popleft()

        if len(array) - 1 == curr_index :
            if target == curr_sum :
                count += 1
        else : 
            queue.append((curr_index + 1, curr_sum + array[curr_index + 1]))
            queue.append((curr_index + 1, curr_sum - array[curr_index + 1]))
    
    return count


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!
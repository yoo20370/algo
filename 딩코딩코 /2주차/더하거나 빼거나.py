numbers = [1, 1, 1]
target_number = 3

def recursiveFunction(array, target, curr_index) -> int :

    # 리스트 각 원소에 대하여 양수일 때 재귀, 음수일 때 재귀를 수행할 예정 
    # 배열의 마지막 인덱스에 도달했을 때, 배열의 합과 target의 값이 동일하면 count 값을 1 올려서 반환 
    # 종료 조건은 배열의 마지막 인덱스에 도달했을 때

    if len(array) == curr_index :
        if sum(array) == target :
            print(array)
            return 1
        else :
            return 0
    else :
        count = 0
        # 양수로 전달
        count += recursiveFunction(array, target, curr_index + 1)

        # 음수로 전달 
        array[curr_index] = - array[curr_index]
        count += recursiveFunction(array, target, curr_index + 1)

        return count


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target) -> int:

    
    return recursiveFunction(array, target, 0) 




print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!
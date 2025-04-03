numbers = [1, 1, 1, 1, 1]
target_number = 3

def recusion_func(array, curr_index, target, total) -> int :
    if len(array)  == curr_index :
        if total == target :
            return 1
        return 0
    
    curr_val = array[curr_index]
    resultA = recusion_func(array, curr_index + 1, target, total + curr_val)
    resultB = recusion_func(array, curr_index + 1, target, total - curr_val)

    return resultA + resultB

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):

    return recusion_func(array, 0, target, 0)
    
print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!


 

 
 
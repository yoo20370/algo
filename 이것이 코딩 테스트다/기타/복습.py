import sys 

array = list(map(int, sys.stdin.readline().split()))


def solution(array, start_index, end_index) -> int :

    total_sum = 0
    p = [0]

    for curr_value in array :

        total_sum += curr_value
        p.append(total_sum)

    result = p[end_index] - p[start_index - 1]
    return result 

    
print(solution(array, 1, 1))
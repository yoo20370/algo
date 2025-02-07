import sys


array_count = int(sys.stdin.readline().rstrip())

array = list(map(int, sys.stdin.readline().split()))

target = int(sys.stdin.readline().rstrip())

# 투 포인터를 맨 앞과 맨 뒤에 둔다. 
# 배열을 정렬을 한다. 
# 만약 값이 같다면 

def solution(array_count, array, target) -> int :

    start_index = 0
    end_index = array_count - 1
    count = 0

    array.sort()

    while start_index != end_index :

        two_number_sum = array[start_index] + array[end_index]

        if two_number_sum == target :
            count += 1
            end_index -= 1
        elif two_number_sum < target :
            start_index += 1
        else :
            end_index -= 1
    
    return count

print(solution(array_count, array, target))
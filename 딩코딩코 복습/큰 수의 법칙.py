import sys

N, M, K = map(int, sys.stdin.readline().split())
input_list = list(map(int, sys.stdin.readline().split()))

def max_value_func(N, M, K, inputList) -> int :

    # 내림차순 정렬을 수행하여 가장 큰 값과 그 다음으로 큰 값을 구한다.
    # (K + 1) 연산을 몇 번 수행할 수 있는지 구한다. - cycle을 구해라 
    # cycle * (K * 최대값 + 그다음큰값)을 수행하여 사이클을 수행했을 때의 값을 구한다.
    # 남은 연산의 경우는 모두 최대값을 더한다. 

    inputList.sort(reverse=True)
    
    first = input_list[0]
    second = input_list[1]

    cycle = M // (K + 1)
    remain = M % (K + 1)

    result = 0
    result = cycle * (K * first + second)
    result += remain * first

    return result


print(max_value_func(N, M, K, input_list))
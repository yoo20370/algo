# 주어진 동전을 가지고 만들 수 없는 최소 금액을 구하는 문제
# 주어진 동전을 오름차순으로 정렬한다.
# target을 설정하고, 1 ~ target - 1 값은 이미 가능한 경우로 생각한다.
# 그리고 각 target에 대하여 꺼낸 동전을 더한다. 만약 target 값보다 큰 값이 나오면 종료한다. 

import sys 

input = sys.stdin.readline

def solution() :
    coin_count = input().rstrip()

    coins = list(map(int, sys.stdin.readline().split()))

    coins.sort(reverse=True)

    target = 1 
    while coins :
        curr_coin = coins.pop()

        if target < curr_coin :
            break
        else :
            target += curr_coin

    return target

print(solution())
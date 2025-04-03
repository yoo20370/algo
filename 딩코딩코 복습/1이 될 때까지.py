import sys 

N, K = map(int, sys.stdin.readline().split())

def makeOne(curr, target) :
    # 현재 값을 K로 나눠서 몫을 구한다.
    # 다시 몫에 K를 곱한다.
    # 현재 값 - (몫 * K)를 수행하여 더하기 1을 수행할 값을 구한다. 
    # 만약 현재값을 K로 나눴을 때 몫이 0이라면 연산 한계에 현재값을 더한후 1을 빼준다. 
    count = 0

    while curr // target != 0 :
        remain = curr // target
        result = remain * target
        count += curr - result

        curr = remain
        count += 1

    count += curr 

    return count - 1

print(makeOne(N, K))



# N에서 1을 빼거나 
# N에서 K로 나눠서 
# 가장 적은 연산을 수행해야 한다. 


# 25 5 
# 5
# 1

# 24 1 
# 23 1
# 22 1
# 21 1
# 20 5
# 4 1
# 3 1
# 2 1
# 1

# 24 // 5
# 4 * 5 -> 20
# 24 - 20 
# 4 -> 연산 합계에 추가 
# 20 -> 5로 나눈다. -> 1개 추가
# 4 -> 




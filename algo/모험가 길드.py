# 한 마을에 모험가 N명
# N 명의 공포도 측정 
# 공포가 X인 사람은 X명인 사람과 함께해야 한다. 
# 여행을 떠날 수 있는 그룹 수의 최대값을 구하여라 

## 몇 명의 모험가는 마을에 그대로 남아 있어도 된다. 
import sys, math

def func() :
    N = int(sys.stdin.readline().rstrip())

    people = list(map(int, sys.stdin.readline().split()))

    people.sort()
    length = len(people)

    count = 0 

    curr_index = 0

    while curr_index < length and length - curr_index >= people[curr_index] :
        
        # 특정 범위의 합이 현재 인덱스 
        result = sum(people[curr_index:curr_index + people[curr_index]]) / people[curr_index]
        result = int(math.ceil(result))

        if result > people[curr_index] :
            return count 
        
        count += 1
        curr_index += people[curr_index]

    return count
print(func())


        



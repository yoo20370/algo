# 최대한 다양한 종류의 포켓몬을 가지길 원함
# 최대한 많은 종류의 포켓몬을 포함해서 N/2마리를 선택하려고 함 
# 가장 많은 종류의 포켓몬을 선택하는 방법을 찾아야 할 때 종류의 개수를 반환하도록 하자 
# set()에 다 넣는 과정을 수행하자 이때, 모두 돌았음에도 불구하고 N // 2를 넘지 못했다면 
# 해당 종류 개수만큼이 최대인거고 
# 반대로 넘었다면 N // 2개수가 최대인거임 

# set()을 이용한 풀이
def solution(nums):
    
    kindSet = set()
    
    for kind in nums :
        kindSet.add(kind)
    
    setLength = len(kindSet)
    
    selectCount = len(nums) // 2
    
    result = setLength 
    if setLength >= selectCount :
        result = selectCount
    
    return result

# 문제를 봤을 땐 Set()으로 푸는게 좋다고 판단 -> 중복 제거를 통해서 쉽게 풀이 
# 해당 문제는 해시 문제이므로 해시로 어떻게 풀지 고민해보면 좋을 듯 
def solution(nums):
    
    dict = {}
    
    for kind in nums :
        if dict.get(kind) is None :
            dict[kind] = True 
    
    dictLength = len(dict)
    
    selectCount = len(nums) // 2
    
    result = dictLength
    if dictLength >= selectCount:
        result = selectCount
    return result
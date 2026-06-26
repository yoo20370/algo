# 해시로 옷 종류를 분류
# 각 종류 별 개수
# 조합을 이용해서 전체 종류 중, 몇 개의 종류를 선택할 것인지 생각해야 함
# 조합을 요구하는게 아니라 개수를 요구하므로 조합 라이브러리를 사용할 필요가 없어보임
# 결국 아예 안 입는 경우를 한 가지로 보면 됨 
# kindCount *= (종류 별 개수 + 1) 
# kindCount - 1 하면 됨 # 모든 종류를 안 입는 경우는 빼야 함

def solution(clothes):
    clothesDict = {}
    
    for index in range(len(clothes)) :
        name, kind = clothes[index]
        
        
        if clothesDict.get(kind) :
            clothesDict.get(kind).append(name)    
        else :
            clothesDict[kind] = [name]
            
    kindList = list(clothesDict.keys())
    
    totalCount = 1
    for kind in kindList :
        kindArray = clothesDict[kind]
        totalCount *= len(kindArray) + 1
    
    return totalCount - 1
    
    

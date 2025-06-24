# 정렬된 두 묶음의 숫자 카드가 있음 
# 각 묶음의 카드의 수를 A, B라고 하면, 보통 두 묶음을 합쳐서 하나로 만드는데에는 A + B 번의 비교를 해야 함 

## 고르는 순서에 따라서 비교 횟수가 매우 달라진다. 
## 힙을 써야할 것 같은데 
import sys, heapq 

def merge(A, B) :
    return A + B 

def solution() :
    N = int(sys.stdin.readline().rstrip())

    heap = []

    for _ in range(N) :
        heapq.heappush(heap, int(sys.stdin.readline().rstrip()))
    
    # 힙에서 두 개의 원소를 꺼내고 넣은 다음, 다시 힙에 삽입한다. 
    count = 0 
    while len(heap) >= 2 :
        first = heapq.heappop(heap)
        seconde = heapq.heappop(heap)

        result = first + seconde
        count += result

        heapq.heappush(heap, result)

    print(count)

solution()




    


    

    
    
    




    
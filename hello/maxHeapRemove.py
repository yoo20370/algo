# 제거하는 순서
# 마지막 삭제 할 원소와 마지막 노드의 원소를 교체한다.
# 마지막 노드를 제거한다.(교체된 삭제할 노드가 됨)
# 교체된 노드를 자식들과 비교하면서 자리를 맞춰야 한다.

class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    
    # 왼쪽와 오른쪽 노드를 비교해야 함 
    # 왼쪽 자식 노드가 존재하는지 검사 -> len(items) - 1 <= 부모 // 2 -> 있다는 의미 -> 조건에 맞지 않으면 없다는 의미 -> 더 이상 할 필요 없음 
    # 있다면 오른쪽 노드가 있는지 확인해야 함 그리고 비교해서 교체할 대상을 정해줘야 함 
    # 왼쪽 노드가 있다는 건 확정이니까 부모와 비교해서 삽입할 값을 결정한다. (왼쪽인지, 자식인지)
    # 오른쪽 노드가 있다면, 삽입하기로 결정할 값과 오른쪽 노드를 비교해서 최종 삽입할 값을 결정한다. 
    def delete(self):

        # 힙이 비어 있는 경우 
        if len(self.items) == 1 :
            return -1 
        
        if len(self.items) == 2 :
            return self.items.pop()
        
        deleteData = self.items[1]

        rootIndex = 1
        lastIndex = len(self.items) - 1

        self.items[rootIndex], self.items[lastIndex] = self.items[lastIndex], self.items[rootIndex]

        self.items.pop()

        parentIndex = rootIndex
        leftChildIndex = parentIndex * 2

        # 왼쪽 자식이 존재할 떄까지 해야 해 !! 
        while leftChildIndex <= len(self.items) - 1 : 
            
            # 부모랑 교체할 대상 
            targetIndex = parentIndex

            # 왼쪽 자식과 비교 후, 타겟 설정 
            if self.items[targetIndex] < self.items[leftChildIndex] :
                targetIndex = leftChildIndex
            
            rightChildIndex = parentIndex * 2 + 1

            # 오른쪽 자식도 있니 ??
            if rightChildIndex <= len(self.items) - 1 :
                
                # 오른쪽 자식이 더 크니 ??
                if self.items[targetIndex] < self.items[rightChildIndex] :
                    targetIndex = rightChildIndex

            if parentIndex == targetIndex :
                break

            ## 가능한 경우의 수 
            # 부모와 부모 교체
            # 부모와 왼쪽 교체
            # 부모와 오른쪽 교체
            self.items[parentIndex], self.items[targetIndex] = self.items[targetIndex], self.items[parentIndex]
            
            parentIndex = targetIndex
            leftChildIndex = parentIndex * 2

        return deleteData


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]
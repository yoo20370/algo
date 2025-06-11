class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        # 힙은 부모 자식 간의 우선순위 특성을 갖고 완전 트리 구조 형태의 자료구조
        # 힙에 데이터가 삽입되면 마지막 위치에 삽입되며, 해당 노드의 데이터를 부모와 비교하여 해당 노드의 위치를 찾아 나간다. 
        # 즉, 단순히 부모와 비교해서 위치를 찾아 나간다.

        # 우선 힙에 데이터를 삽입한다. 
        # 삽입한 데이터의 인덱스를 구한다. 
        # 부모와 비교하여 삽입된 데이터의 위치를 찾아가는 과정을 수행한다.
        # 단, 루트 노드까지 수행한다.
        heap = self.items

        heap.append(value)
        insert_index = len(heap) - 1

        curr_index = insert_index
        parent = curr_index // 2
        while parent > 0 and heap[parent] < heap[curr_index] :
            heap[curr_index], heap[parent] = heap[parent], heap[curr_index]
            curr_index = parent
            parent = curr_index // 2
        
        return


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!
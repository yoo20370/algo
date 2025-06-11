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

    def delete(self):
        # 루트 원소를 마지막 원소와 교체합니다.
        # 마지막 원소를 제거합니다. pop()
        # 루트 원소는 자식 노드를 비교하며 위치를 찾습니다.
        # 만약 자식이 하나라면 누가 더 큰 지만 비교해서 바꾸면되고, 자식이 둘이라면 자식들 중 더 큰 값과 교체해야 합니다. 
        # 이 과정을 자식이 없을 때까지 반복 

        heap = self.items

        last_index = len(heap) - 1
        heap[1], heap[last_index] = heap[last_index], heap[1]
        return_data = heap.pop()

        length = len(heap)

        curr_index = 1

        left_child_index = curr_index * 2
        right_child_index = left_child_index + 1
        while left_child_index < length and heap[curr_index] < heap[left_child_index]:
            
            change_index = left_child_index
            
            if right_child_index < length and heap[change_index] < heap[right_child_index]:
                change_index = right_child_index
            
            heap[curr_index], heap[change_index] = heap[change_index], heap[curr_index]

            curr_index = change_index
            left_child_index = curr_index * 2
            right_child_index = left_child_index + 1

        return return_data  # 8 을 반환해야 합니다.


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
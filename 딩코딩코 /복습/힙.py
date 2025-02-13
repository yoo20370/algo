class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value) -> int :
        self.items.append(value)

        curr_index = len(self.items) - 1

        # 현재 노드가 루트 노드가 아니고, 부모 노드의 값보다 현재 노드의 값이 크다면 
        while curr_index != 1 and self.items[curr_index // 2] < self.items[curr_index] :
            self.items[curr_index], self.items[curr_index // 2] = self.items[curr_index // 2], self.items[curr_index] 
            curr_index = curr_index // 2

        return curr_index 


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!

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
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        
        return_value = self.items.pop()

        curr_index = 1
        last_index = len(self.items) - 1
        left_child_index = curr_index * 2

        while left_child_index <= last_index :
            if self.items[left_child_index] > self.items[curr_index] :
                larger_index = left_child_index

                right_child_index = curr_index * 2 + 1
                if right_child_index <= last_index and self.items[right_child_index] > self.items[larger_index] :
                    larger_index = right_child_index

                self.items[larger_index], self.items[curr_index] = self.items[curr_index], self.items[larger_index]
                curr_index = larger_index
                left_child_index = curr_index * 2
            else :
                break 

        return return_value


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
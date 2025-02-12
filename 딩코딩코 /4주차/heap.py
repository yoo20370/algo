class MaxHeap :

    def __init__ (self) :
        self.items = [None]

    def insert(self, value) :
        self.items.append(value)

        curr_index = len(self.items) - 1
        parent_index = curr_index // 2

        # 루트가 아니고 부모보다 자식이 큰 경우 부모 자식 교환
        while curr_index != 1 and self.items[parent_index] < self.items[curr_index] :
            self.items[parent_index], self.items[curr_index] = self.items[curr_index], self.items[parent_index]
            curr_index = parent_index
            parent_index = curr_index // 2

    def delete(self) :
        
        # 삭제 할 것이 없기 때문
        if len(self.items) == 1 :
            return -1

        return_value = self.items[1]
        last_index = len(self.items) - 1

        self.items[1], self.items[last_index] = self.items[last_index], self.items[1]
        self.items.pop()

        # 삭제 후 
        curr_index = 1
        last_index = len(self.items) - 1

        # 현재 인덱스가 마지막 인덱스 보다 작다면 반복문 수행
        while curr_index < last_index :
            left_child_index = curr_index * 2
            right_child_index = curr_index * 2 + 1

            # 오른쪽 자식 인덱스가 마지막 노드 인덱스보다 작거나 같고 왼쪽 자식보다 오른쪽 자식의 값이 더 크다면 
            # 오른쪽 자식과 부모의 값보다 크다면 교환한다.
            if right_child_index <= last_index and self.items[left_child_index] < self.items[right_child_index] :
                left_child_index = right_child_index

            # 왼쪽 자식 인덱스가 마지막 노드 인덱스보다 작거나 같고 왼쪽 자식이 부모의 값보다 크다면 교환한다.
            if left_child_index <= last_index and self.items[curr_index] < self.items[left_child_index] :
                self.items[left_child_index], self.items[curr_index] = self.items[curr_index], self.items[left_child_index]
                curr_index = left_child_index
            else :
                 # 자식이 둘 다 없는 경우는 종료한다. 
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
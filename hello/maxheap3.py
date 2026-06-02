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

    # 제거는 어떻게 구현할 것인가 
    # 제거할 대상을 마지막 노드와 교체 
    # 마지막 노드가 루트로 이동했으니 이 노드의 위치를 재조정해줘야 함 
    # 가장 먼저 왼쪽 자식 노드와 비교, 오른쪽 자식 노드가 있다면 오른쪽 자식 노드도 비교 하는 방향으로 가야 함 

    def delete(self):
        
        array = self.items

        lastIndex = len(array) - 1

        array[1], array[lastIndex] = array[lastIndex], array[1]

        outputData = array.pop()

        lastIndex = len(array) - 1

        currentIndex = 1
        leftChildIndex = currentIndex * 2 
        while leftChildIndex <= lastIndex :
            changeIndex = currentIndex

            if array[changeIndex] < array[leftChildIndex] :
                changeIndex = leftChildIndex
            
            rightChildIndex = currentIndex * 2 + 1
            if rightChildIndex <= lastIndex :
                if array[changeIndex] < array[rightChildIndex] :
                    changeIndex = rightChildIndex
            
            if changeIndex == currentIndex :
                break

            array[changeIndex], array[currentIndex] = array[currentIndex], array[changeIndex]
            currentIndex = changeIndex
            leftChildIndex = currentIndex * 2

        return outputData


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
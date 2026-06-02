class MaxHeap:
    def __init__(self):
        self.items = [None]

    # 완전 이진 트리이므로 마지막에 원소를 추가
    # 부모와 비교하며, 부모가 더 작은 경우 교체
    # 반대로 작은 경우 끝 
    def insert(self, value):
        
        length = len(self.items)

        array = self.items

        # 마지막에 원소 추가 
        array.append(value)

        if length != 0 :
            currentIndex = len(array) - 1
            parentIndex = currentIndex // 2
            while parentIndex > 0 and array[parentIndex] <  array[currentIndex] :
                array[parentIndex], array[currentIndex] = array[currentIndex], array[parentIndex]
                currentIndex = parentIndex
                parentIndex = currentIndex // 2


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!
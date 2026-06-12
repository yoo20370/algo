class MaxHeap:
    def __init__(self):
        self.items = [None]

    # 어떤 식으로 진행해야 하는가 ?? 
    # 마지막 위치에 노드를 삽입하고, 해당 노드의 부모와 비교해서 노드의 위치를 재조정한다. 

    def insert(self, value):
        
        datas = self.items

        datas.append(value)

        lastIndex = len(datas) - 1

        # 데이터가 있어서 재조정이 필요한 경우 
        if lastIndex != 1 :
            currentIndex = lastIndex
            parentIndex = currentIndex // 2

            # 루트노드까지 최대 진행 가능하며, 현재 노드보다 부모 노드가 더 작은 경우 
            while parentIndex > 0 and datas[parentIndex] < datas[currentIndex] :

                # 부모와 값을 Swap
                datas[parentIndex], datas[currentIndex] = datas[currentIndex], datas[parentIndex]

                # 현재 인덱스 수정 
                currentIndex = parentIndex
                # 현재 인덱스의 부모 인덱스 수정 
                parentIndex = currentIndex // 2

    def delete(self) :

        length = len(self.items)

        datas = self.items

        # 원소가 존재하지 않는 경우 
        if length == 1 :
            return -1 
        
        lastIndex = length - 1
        

        datas[1], datas[lastIndex] = datas[lastIndex], datas[1]

        returnData = datas.pop()
        lastIndex = len(datas) - 1

        currentIndex = 1
        leftChildIndex = currentIndex * 2 
        # 루트의 값을 자식 노드를 비교해서 최대힙을 유지하도록 해야함 
        # 1. 현재 노드의 왼쪽 자식 노드 인덱스를 구한 뒤, 마지막 인덱스 값과 같거나 작은 경우 반복문을 반복 
        # 2. 둘 중 선택할 노드를 생각하고, 오른쪽 노드가 존재하는지 확인한다. (마지막 인덱스보다 작거나 같으면 진행)

        while leftChildIndex <= lastIndex :
            
            changeIndex = currentIndex
            if datas[currentIndex] < datas[leftChildIndex] :
                changeIndex = leftChildIndex
            
            rightChildIndex = currentIndex * 2 + 1

            if rightChildIndex <= lastIndex and datas[changeIndex] < datas[rightChildIndex]:
                changeIndex = rightChildIndex
            
            # 만약 자식과 교환할 이유가 없다면 
            if changeIndex == currentIndex :
                break
            
            # 둘이 교환
            datas[currentIndex], datas[changeIndex] = datas[changeIndex], datas[currentIndex]

            currentIndex = changeIndex
            leftChildIndex = currentIndex * 2


        return returnData    

    

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
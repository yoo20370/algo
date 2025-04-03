# 최대힙 구현하기 
heap = []
def insert(heap, num) -> None :

    # 맨 마지막 위치에 원소를 삽입한다. 
    # 현재 원소와 부모 원소를 비교하여 현재 원소가 값이 더 크다면 교환한다.
    # 부모 원소가 더 크거나 같을 때까지 반복한다. 
    heap.append(num)

    curr = len(heap) - 1
    parent = (curr - 1) // 2

    while curr > 0 and heap[parent] < heap[curr]:
        heap[parent], heap[curr] = heap[curr], heap[parent]
        curr = parent
        parent = (curr - 1) // 2

def remove(heap) -> int :

    if len(heap) <= 0 :
        return None
    
    if len(heap) == 1 :
        return heap.pop()

    last_index = len(heap) - 1
    heap[0], heap[last_index] = heap[last_index], heap[0]
    last_value = heap.pop()

    last_index -= 1

    curr_index = 0 
    left_child_idx = curr_index * 2 + 1 
    right_child_idx = curr_index * 2 + 2 

    while left_child_idx <= last_index :
        change_index = curr_index
        if heap[left_child_idx] > heap[curr_index] :
            change_index = left_child_idx
        
        if right_child_idx <= last_index and heap[right_child_idx] > heap[change_index]:
            change_index = right_child_idx

        if curr_index == change_index :
            break
        heap[curr_index], heap[change_index] = heap[change_index], heap[curr_index]
        curr_index = change_index
        left_child_idx = curr_index * 2 + 1
        right_child_idx = curr_index * 2 + 2 

    return last_value


    


    

    
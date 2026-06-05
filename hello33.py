

data = [13, 4, 19, 1, 8, 16, 5, 11, 20, 3, 14, 7, 18, 10, 2, 15, 6, 17, 9, 12]


def solution() :

    pass

    # insertSort(data)

    # selectSort(data)

    # bubbleSort(data)

def insertSort(data) :

    # 삽입 정렬
    # 삽입될 위치에 들어갈 값을 선택해서 삽입하는 정렬 
    # 맨 인덱스 위치부터 차근 차근 결정한다. 
    # 앞에 배열은 정렬되어 있는 것으로 간주한다.
    # 이미 정렬된 배열인 경우 O(N) 시간 복잡도로 끝난다.
    # 최악의 경우 O(N**2)

    for step in range(1, len(data)) :
        
        currentIndex = step
        currentData = data[currentIndex]

        # 앞으로 이동하면서 비교해야 함 
        # 앞의 값이 더 크다면, 뒤에 덮어쓰기 
        while currentIndex - 1 >= 0 and currentData < data[currentIndex - 1] :
            data[currentIndex] = data[currentIndex - 1]
            currentIndex -= 1
        
        data[currentIndex] = currentData
    
    print(data)


def selectSort(data) :

    # 선택정렬 
    # 배열을 순회하여 가장 큰 값 혹은 가장 작은 값을 선택하여 값을 확정지어 정렬하는 방법 

    # 마지막 단계는 하지 않아도 자동 정렬됨 
    for step in range(0, len(data) - 1) :
        minIndex = step

        # step + 1인 이유는 이미 첫 비교 기준 인덱스를 step 값으로 잡았기 때문
        # 끝까지 수행해야 하지 않나 ?? 확정된 것 제외하고 모두 순회해서 최소값을 찾아야 하니까 
        for currentIndex in range(step + 1, len(data)) :
            if data[minIndex] > data[currentIndex] :
                minIndex = currentIndex
        
        data[step], data[minIndex] = data[minIndex], data[step]

    print(data)

def bubbleSort(data) :
    # 버블 정렬   
    # 인접한 원소끼리 비교하여, 마지막 위치부터 값을 확정하는 정렬 방법 
    # 바깥 반복문의 경우 0 ~ n-1번까지 증가하면 됨 -> 단계이자 마지막 인덱스로부터 떨어진 거리라고 생각하면 됨 
    # 내부 반복문 0부터 인접한 원소를 비교하며 이동 이 때 n-1까지만 비교하면 n번째는 자동으로 결정됨 

    for step in range(0, len(data) - 1) :
        for leftIndex in range(0, len(data) - 1 - step) :
            rightIndex = leftIndex + 1
            if data[leftIndex] > data[rightIndex] :
                data[leftIndex], data[rightIndex] = data[rightIndex], data[leftIndex]

    print(data)

solution()
import sys
sys.setrecursionlimit(int(1e6))

def func(array, left, right, count) :
    
    if left >= right :
        return count 
    
    if array[left] != array[right - 1] :

        if count == 0 :

            # 왼쪽을 제거하고 진행
            result = func(array, left + 1, right, 1)
            if result != 2 :
                return result         

            # 오른쪽을 제거하고 진행 
            return func(array, left, right - 1, 1)

        else :
            return 2
    
    return func(array, left + 1, right -1, count)
        

def solution() :
    T = int(sys.stdin.readline().rstrip())

    for _ in range(T):
        string = sys.stdin.readline().rstrip()

        print(func(string, 0, len(string), 0))

solution()
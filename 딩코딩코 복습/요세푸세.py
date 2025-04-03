import sys

N, K = map(int, sys.stdin.readline().split())

def josephus_problem(n, k) -> None :

    arr = [i for i in range(1, n+1)]
    resultList = []
    index = 0
    
    while len(arr) != 1 :
        index = (index + k - 1) % (len(arr))
        resultList.append(arr.pop(index))
    resultList.append(arr.pop())
    
    print("<", ", ".join(map(str, resultList)), ">", sep='')

josephus_problem(N, K)

          

from collections import deque
import sys

def appendleft(arr, x) :
    arr.appendleft(x)

def append(arr, x) :
    arr.append(x)

def popleft(arr) :
    if len(arr) < 1 :
        print(-1)
    else :
        print(arr.popleft())

def pop(arr) :
    if len(arr) < 1 :
        print(-1)
    else :
        print(arr.pop())

def length(arr) :
    print(len(arr))

def isEmpty(arr) :
    if len(arr) == 0 :
        print(1)
    else :
        print(0)

def front(arr) :
    if len(arr) > 0 :
        print(arr[0])
    else :
        print(-1)

def back(arr) :
    if len(arr) > 0 :
        print(arr[len(arr) - 1])
    else :
        print(-1)
N = int(sys.stdin.readline().rstrip())
dequeue = deque()

for i in range(N) :
    data = sys.stdin.readline().rstrip()
    if len(data) != 1 :
        x, y = map(int, data.split())
    else :
        x = int(data)
    
    if x == 1 :
        appendleft(dequeue, y)
    elif x == 2 :
        append(dequeue, y)
    elif x == 3 :
        popleft(dequeue)
    elif x == 4 :
        pop(dequeue)
    elif x == 5 :
        length(dequeue)
    elif x == 6 :
        isEmpty(dequeue)
    elif x == 7 :
        front(dequeue)
    elif x == 8 :
        back(dequeue)


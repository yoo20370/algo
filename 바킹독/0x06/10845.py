import sys

MX = int(1e5)

dat = [0] * (MX + 1)
head = 0
tail = 0

def empty() -> bool :
    if head == tail :
        return 1
    else :
        return 0

def push(data) -> None :
    global tail
    if tail == MX :
        return None
    dat[tail] = data
    tail += 1

def pop() -> int :
    global head 
    if empty() :
        return -1
    temp = dat[head]
    head += 1

    return temp 

def size() -> int :
    return tail - head

def front() -> int :
    if empty() :
        return -1
    return dat[head]

def back() -> int :
    if empty() :
        return -1
    return dat[tail -1]

N = int(sys.stdin.readline().rstrip())


result = []
for i in range(N) :
    commands = sys.stdin.readline().split()

    if commands[0] == "push" :
        push(int(commands[1]))
    elif commands[0] == "pop" :
        # print(pop())
        result.append(pop())
    elif commands[0] == "size" :
        # print(size())
        result.append(size())
    elif commands[0] == "empty" :
        # print(empty())
        result.append(empty())
    elif commands[0] == "front" :
        # print(front())
        result.append(front())
    elif commands[0] == "back" :
        # print(back())
        result.append(back())

for i in result :
    print(i)
    
    

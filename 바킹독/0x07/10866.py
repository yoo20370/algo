import sys

MX = int(1e6)
dat = [0] *(2*MX+1)
head = MX
tail = MX 

def size() -> int :
    return tail - head

def empty() -> int :
    if head == tail :
        return 1
    else :
        return 0

def push_front(data) -> None :
    global head
    head -= 1
    dat[head] = data

def push_back(data) -> None :
    global tail
    dat[tail] = data
    tail += 1

def pop_front() -> int :
    global head
    if empty() :
        return -1
    else :
        temp = dat[head]
        head += 1
        return temp 

def pop_back() -> int :
    global tail
    if empty() :
        return -1
    else : 
        tail -= 1
        return dat[tail]

def front() -> int :
    if empty() :
        return -1
    else :
        return dat[head]

def back() -> int :
    if empty() :
        return -1
    else :
        return dat[tail-1]

N = int(sys.stdin.readline().rstrip())

result = []
for i in range(N) :
    commands = sys.stdin.readline().split()
    if commands[0] == "push_front" :
        push_front(int(commands[1]))
    elif commands[0] == "push_back" :
        push_back(int(commands[1]))
    elif commands[0] == "pop_front" :
        result.append(pop_front()) 
    elif commands[0] == "pop_back" :
        result.append(pop_back()) 
    elif commands[0] == "size" :
        result.append(size())
    elif commands[0] == "empty" :
        result.append(empty())
    elif commands[0] == "front" :
        result.append(front()) 
    elif commands[0] == "back" :
        result.append(back())

for i in result :
    print(i)
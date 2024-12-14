import sys

MX = int(10e5)
dat = [0] * MX
pos = 0 

N = int(sys.stdin.readline().rstrip())


def push(data) -> None :
    global pos
    if pos >= MX :
        return None
    dat[pos] = data 
    pos += 1

def pop() -> int :
    global pos
    if pos == 0 :
        return -1
    pos -= 1
    return dat[pos]

def size() -> int :
    global pos
    return pos

def empty() -> int :
    global pos
    if pos == 0 :
        return 1
    else :
        return 0
    
def top() -> int :
    global pos
    if pos == 0 :
        return -1
    else :
        return dat[pos-1]


for i in range(N) :
    commands = sys.stdin.readline().split()

    if commands[0] == "push" :
        push(commands[1])
    elif commands[0] == "pop" :
        print(pop())
    elif commands[0] == "size" :
        print(size())
    elif commands[0] == "empty" :
        print(empty())
    elif commands[0] == "top" :
        print(top())
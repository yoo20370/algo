MX = int(1e6)
dat = [0] * (2*MX+1)
head = MX
tail = MX

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
    if head == MX:
        return 1
    else :
        temp = dat[head]
        head -= 1
        return temp 
    
def pop_back() -> int :
    global tail 
    if tail == MX :
        return 1
    else : 
        tail -= 1
        return dat[tail]

def front() -> int :
    return dat[head]

def back() -> int :
    return dat[tail-1]

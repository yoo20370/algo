MX = int(1e5)
dat = [0] * MX + 1
head = 0 
tail = 0

def push(data) -> None :
    global tail
    if tail == MX :
        return None
    dat[tail]
    tail += 1
 
def pop() -> None :
    global head 
    if head == tail :
        return None
    head += 1
def front() -> int :
    if head == tail :
        return -1
    print(dat[head])
    
def back() -> int :
    if head == tail :
        return -1
    print(dat[tail-1])


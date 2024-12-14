MX = 10000005
dat = [0] * MX
pos = 0 

def push(x : int) -> None :

    global pos
    # 스택이 가득찬 경우 
    if pos > MX -1 : 
        return None 
    
    dat[pos] = x
    pos += 1


def pop() -> None :
    global pos
    # 스택이 비어있는 경우
    if pos == 0 :
        return None
    pos -= 1

def top() -> int :
    global pos
    # 스택이 비어있는 경우 출력할 것이 없음 
    if pos == 0 :
        return None
    
    return dat[pos-1]

def test() -> None :
    pass

def mainFunc() -> int :
    test()
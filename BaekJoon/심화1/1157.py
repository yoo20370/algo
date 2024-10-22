
data = input()

def wordCheck(data) :

    alpha = [0] * 26
    idxList = set() 

    for i in range(len(data)) :
        ch = data[i]
        ch = ord(ch)
        # 소문자를 대문자로 바꾸기
        if ch > 90 :
            ch -= 32

        idx = ch - 65
        alpha[idx] += 1

        idxList.add(idx)
    
    maxVal = 0
    maxidx = 0
    for i in range(len(alpha)) :
        if maxVal < alpha[i] :
            maxVal = alpha[i]
            maxidx = i

    cnt = 0 
    for i in idxList :
        if maxVal == alpha[i] :
            cnt += 1
    
    if cnt != 1 :
        return "?"
    
    return chr(maxidx + 65)

print(wordCheck(data))
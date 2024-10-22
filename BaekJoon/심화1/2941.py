data = input() 

strList = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=" , "z="]

def checkWord(data, ch) :

    # 변경된 문자의 길이 
    chLength = len(ch)

    cnt = 0 
    for i in range(len(data) - chLength + 1) :
        string = ""
        for j in range(chLength) :
            string += data[i + j] 
        
        if string == ch :
            cnt += 1

    return cnt 

cnt = 0
for i in strList :
    cnt += checkWord(data, i)

print(len(data) - cnt)
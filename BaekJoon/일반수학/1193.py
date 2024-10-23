N = int(input())

def func(N) :
    if N == 1 :
        return "1/1"
    sum = 1 
    std = 2

    while N > sum :
        sum += std
        std += 1
    std -= 1
    sum -= std
    sum += 1
    
    if std % 2 == 0 :
        a = 1
        b = std
    else :
        a = std
        b = 1

    while N != sum :
        sum += 1
        if std % 2 == 0 :
            a += 1
            b -= 1
        else :
            a -= 1
            b += 1
        
    return str(a)+"/"+str(b)

print(func(N))

# a=int(input())
# i=1
# while i*(i+1)//2 < a:
#     i+=1
# if i==1:
#     print(1,'/',1, sep='')
# if i!=1:
#     if i%2==0:
#       print(a-(i-1)*i//2,'/',i+1-(a-(i-1)*i//2),sep='')
#     else:
#       print(i+1-(a-(i-1)*i//2),'/',a-(i-1)*i//2,sep='')

# num = int(input())
# line = 1

# while num > line:
#     num -= line
#     line += 1
    
# # 짝수일경우
# if line % 2 == 0:
#     a = num
#     b = line - num + 1
# # 홀수일경우
# elif line % 2 == 1:
#     a = line - num + 1
#     b = num

# print(f'{a}/{b}')
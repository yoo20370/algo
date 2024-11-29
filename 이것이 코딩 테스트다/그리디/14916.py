# import sys 

# N = int(sys.stdin.readline().rstrip())

# list = [5,2]

# def moneyBack(n) :
#     # 거스름돈 개수 
#     cnt = 0 
#     if n == 1 :
#         return -1

#     # 짝수인지 홀수인지 체크 
#     if n % 2 != 0 and n < 7:
#         return -1
    
#     # 홀수인 경우 5원짜리 하나 2원짜리 하나로 먼저 바꿔줌으로써 짝수로 만들어준다. 
#     if n % 2 != 0 :
#        cnt += 2
#        n -= 7
    
#     while n != 0 :

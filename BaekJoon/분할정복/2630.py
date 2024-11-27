# import sys 

# N = int(sys.stdin.readline().rstrip())

# pan = list()
# for i in range(N) :
#     pan.append(list(map(int, sys.stdin.readline().split())))

# white = 0
# blue = 0 

# def colorPaper(n, start, end) :

#     global blue
#     global white
#     # 색이 같지 않으면 자른다. 
#     if n == 1 :
#         if pan[start] == 0 :
#             blue += 1
#         else :
#             white += 1
#         return -1
#     else :
#         cnt = 0
#         for i in range(start, end+1) :
#             for j in range(start, end+1) :
#                 cnt += pan[i][j]
#         if cnt == 0 :
#             white += 1
#             return 
#         elif (end-start+1) ** 2 == cnt :
#             blue += 1
#             return 
        
#         start1 = start
#         start2 = 
            

# 정렬 라이브러리 풀이 
# import sys

# N = int(sys.stdin.readline().rstrip())

# arr = list()

# for i in range(N) :
#     name, score = sys.stdin.readline().split()
#     arr.append([name,int(score)])

# def setting(data) :
#     return data[1]

# arr.sort(key = setting) 

# for name, score in arr :
#     print(name, end=" ")

# 계수 정렬
import sys

N = int(sys.stdin.readline().rstrip())

MX = 101 
# arr[0]은 수, arr[1]은 이름 저장 
arr = [[0,list()] for i in range(MX)]
for i in range(N) :
    name, score = sys.stdin.readline().split()
    arr[int(score)][0] += 1
    arr[int(score)][1].append(name)


for idx in range(MX) :
    for cnt in range(len(arr[idx][1])) :
        print(arr[idx][1][cnt], end=" ")

# 마지막 공백을 제거하기 위한 코드 
# # 점수별 이름 출력
# result = []
# for idx in range(MX):
#     result.extend(arr[idx][1])

# # 이름 출력 (공백으로 구분)
# print(" ".join(result))
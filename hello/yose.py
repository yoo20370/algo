# BOJ 1158

# 결국, k - 1만큼 계속 이동해야 함 -> 숫자가 제거되면서 한 칸 이동한 게 됨 
# 그리고 남은 배열 길이로 나눠서 나머지가 몇인지 확인해야 함 -> 나머지의 인덱스가 다음 선택 인덱스 

def josephus_problem(n, k):
    # 이 부분을 채워보세요!
    result = []

    array = [i for i in range(1, n + 1)]

    currentIndex = k - 1
    while array :
        result.append(array.pop(currentIndex))

        currentIndex = currentIndex + k - 1
        while array and len(array) <= currentIndex :
            currentIndex = currentIndex % len(array)
     
    print("<" + ", ".join(map(str, result)) + ">")

n, k = map(int, input().split())
josephus_problem(n, k)


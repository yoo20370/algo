def select_sort(a) :
	n = len(a)
	for i in range(n-1) :    # 마지막 부터 앞으로 
		min = i # 정렬할 부분에서 가장 작은 인덱스
		for j in range(i + 1, n) : # 정렬 안 된 부분부터 비교 
			if a[j] < a[min] :
				min = j
		a[i], a[min] = a[min], a[i]
	return a
N = int(input())
arr = list()

for i in range(N) :
    arr.append(int(input()))

print(select_sort(arr))
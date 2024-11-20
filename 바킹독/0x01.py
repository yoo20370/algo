def func2(arr, N) :
	for i in range(0, len(arr)-1) :
		for j in range(i+1, len(arr)) :
			if arr[i] + arr[j] == 100 :
				return 1
	return 0 

print(func2([1,52,48],3))

import math

def func3(n) :
	if n == 1 :
		return 1
	if n == 2 or n == 3:
		return 0 
	for i in range(2, math.isqrt(n)+1) :
		if n == i*i :
			return 1

	return 0

print(func3(int(input())))

def func3(n) :
    if n == 1 :
        return 1
    
def func4(n) :
    i = 1
    max = 0
    while 2 ** i <= n :
        if 2 ** i  > max :
            max = 2 ** i
        i += 1
    print(max)            

func4(97615282)

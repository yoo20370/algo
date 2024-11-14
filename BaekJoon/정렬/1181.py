def quick(arr, left, right, option) :

   pl = left
   pr = right
   p = arr[(pl+pr) // 2][option]

   while pl <= pr :
      compl = arr[pl][option]
      compr = arr[pr][option]
      while compl < p :
         pl += 1
         compl = arr[pl][option]
      while p < compr :
         pr -= 1
         compr = arr[pr][option]
      
      if pl <= pr :
         arr[pl], arr[pr] = arr[pr], arr[pl]
         pl += 1
         pr -= 1

   if left < pr :
      quick(arr, left, pr, option)
      
   if pl < right :
      quick (arr, pl, right, option)

N = int(input())

setA = set()
arr = list()
for i in range(N) :
   data = input()
   setA.add(data)

for i in setA :
   arr.append([len(i), i])

quick(arr, 0, len(arr) - 1, 0)

s = 0
for i in range(0, len(arr) + 1) :
   if i == len(arr) or arr[i][0] != arr[s][0] :
      quick(arr, s, i - 1, 1)
      s = i

for x, y in arr :
   print(y)
def quick(arr, left, right, option) :

   pl = left
   pr = right
   p = arr[(pl+pr) // 2][option]

   while pl <= pr :
      while arr[pl][option] < p :
         pl += 1
      while p < arr[pr][option] :
         pr -= 1
      
      if pl <= pr :
         arr[pl], arr[pr] = arr[pr], arr[pl]
         pl += 1
         pr -= 1
   if left < pr :
      quick(arr, left, pr, option)
   if pl < right :
      quick (arr, pl, right, option)

def quick2(arr, left, right) :

   pl = left
   pr = right
   p = arr[(pl+pr) // 2][1]

   while pl <= pr :
      while arr[pl][1] < p :
         pl += 1
      while p < arr[pr][1] :
         pr -= 1
      
      if pl <= pr :
         arr[pl], arr[pr] = arr[pr], arr[pl]
         pl += 1
         pr -= 1

   if left < pr :
      quick2(arr, left, pr)
   if pl < right :
      quick2(arr, pl, right)

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
      quick2(arr, s, i - 1)
      s = i

for x, y in arr :
   print(y)
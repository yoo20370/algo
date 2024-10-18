a, b, c = map(int, input().split())

standard = 0
if a > b :
    if a > c :
        standard = a
    else :
        standard = c
else :
    if b > c :
        standard = b
    else :
        standard = c

start = 0
while True :
    start += standard
    if start % a == 0 and start % b == 0 :
        break
    
print(start)
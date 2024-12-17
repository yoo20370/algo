import sys

# x, y
route = [(2,-1),(2,1),(-2, -1),(-2,1),(-1,2), (1,2), (-1, -2), (1,-2)]

location = sys.stdin.readline()

x = int(ord(location[0])) - int(ord("a")) + 1
y = int(location[1])


cnt = 0 
for nx, ny in route :
    dx = x + nx 
    dy = y + ny 

    if dx > 0 and dy > 0 and dx < 9 and dy < 9 :
        cnt += 1

print(cnt)




import sys

N = int(sys.stdin.readline().rstrip())

distance = ["L", "R", "U", "D"]

movement = [(0, -1), (0, 1), (-1, 0), (1, 0)]

x = 1
y = 1

for ch in sys.stdin.readline().split() :

    for now_idx in range(len(distance)) :
        if ch == distance[now_idx] :
            a, b = movement[now_idx]

            d_x = x + b
            d_y = y + a

            if d_x > 0 and d_y > 0 and d_x < N + 1 and d_y < N + 1 :
                x = d_x
                y = d_y

print(y, x)


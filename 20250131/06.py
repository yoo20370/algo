import sys 

data = sys.stdin.readline().rstrip()

# 사용하기 쉽도록 알파벳 숫자로 변환
x = int(ord(data[0]) - ord('a') + 1)
y = int(data[1])

available_movement = ((2, 1), (2, -1),(-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2))


cnt = 0
for n_x, n_y in available_movement :

    d_x = n_x + x 
    d_y = n_y + y

    if d_x > 0 and d_y > 0 and d_x < 9 and d_y < 9 :
        cnt += 1

print(cnt)

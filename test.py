from collections import deque

N = int(input())

card_list = deque([i+1 for i in range(N)])

idx = 0

while(len(card_list) != 1):
  if idx % 2 == 0:
    card_list.popleft()
  else:
    card_list.append(card_list.popleft())
  idx += 1

print(card_list[0])
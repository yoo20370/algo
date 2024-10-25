x1, y1, w, h = map(int, input().split())
print(min(w - x1, h - y1, x1, y1))



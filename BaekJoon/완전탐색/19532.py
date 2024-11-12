# a, b, c, d, e, f = map(int, input().split())

# def func() :
#     for i in range(-999, 1000) :
#         for j in range(-999, 1000):
#             if (a*i) + (b*j) == c and (d*i) + (e*j) == f :
#                 print(i, j)
#                 return 0

# func()

a, b, c, d, e, f = map(int, input().split())

print((c*e - d*f)//(a*e - b*d), (a*f-d*c)//(a*e-b*d))

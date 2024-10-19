A, B = input().split()

RA = ""
RB = ""

for i in range(len(A)-1, -1, -1) :
    RA += A[i]
    RB += B[i]
RA = int(RA)
RB = int(RB)

if RA > RB :
    print(RA)
else :
    print(RB)
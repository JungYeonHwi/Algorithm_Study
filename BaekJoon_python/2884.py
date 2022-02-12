A, B = map(int, input().split())

if B>=45 : B = B - 45
else :
    if A==0 :
        A = 23
        B = B + 15
    else :
        A = A - 1
        B = B + 15

print(A, B, end=' ')
N, A, B, C, D = map(int, input().split())

if N % A : A = (N // A + 1) * B
else : A = N // A * B

if N % C : C = (N // C + 1) * D
else : C = N // C * D

print(min(A, C))
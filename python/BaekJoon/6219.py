A, B, D = map(int, input().split())
arr = [1]*(B+1)
for i in range(2, int(B**0.5)+1):
    if arr[i]:
        for j in range(i+i, B+1, i):
            arr[j] = 0
prime = [i for i in range(A, B+1) if arr[i]]
cnt = 0
for n in prime:
    if str(D) in str(n):
        cnt += 1
print(cnt)
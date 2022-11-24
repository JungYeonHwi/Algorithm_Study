n = int(input())
check = [i for i in range(1, n+1)]
arr = list(map(int, input().split()))
cnt = 0

for i, j in zip(check, arr) : 
    if i != j : cnt += 1
    
print(cnt)
N, K = map(int, input().split())
students = [[0]*2 for _ in range(6)]

for _ in range(N) : 
    s, y = map(int, input().split())
    students[y-1][s-1] += 1
    
cnt = 0

for a in range(6) : 
    for b in range(2) : 
        if students[a][b] % K == 0 : cnt += students[a][b] / K
        else : cnt += students[a][b] // K + 1

print(int(cnt))

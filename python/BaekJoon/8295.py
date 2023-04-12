n, m, p = map(int, input().split())

answer = 0

for i in range(1, n+1) : 
    for j in range(1, m+1) :
        tmp = (i + j) * 2
        
        if tmp >= p : 
            answer += (n - i + 1) * (m - j + 1) * 1

print(answer)
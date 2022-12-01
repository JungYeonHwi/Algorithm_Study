A, B, C, N = map(int, input().split())

answer = 0

for a in range(101) : 
    for b in range(101) : 
        for c in range(101) : 
            if (a * A) + (b * B) + (c * C) == N : answer = 1
            
print(answer)

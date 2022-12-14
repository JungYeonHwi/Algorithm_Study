N, M = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

for i in range(1, N+1) :
    for n in arr :
        if i % n == 0 :
            answer += i
            break
        
print(answer)
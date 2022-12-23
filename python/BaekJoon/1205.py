n, new, p = map(int, input().split())
if n == 0 : print(1)
else : 
    score = list(map(int, input().split()))
    if n == p and score[-1] >= new : print(-1)
    else : 
        answer = n + 1
        for i in range(n) : 
            if score[i] <= new : 
                answer = i + 1
                break
    
        print(answer)
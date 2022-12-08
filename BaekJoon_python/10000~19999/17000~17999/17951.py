N, K = map(int, input().split())
paper = list(map(int, input().split()))

left = 1
right = (10 ** 5 * 20) + 1

answer = 0
while left <= right :
    
    mid = (left + right) // 2
    cnt = 0
    score = 0
    
    for p in paper :
        score += p
        if score >= mid :
            cnt += 1
            score = 0

    if cnt < K : right = mid - 1
    else : 
        answer = mid
        left = mid + 1

print(answer)
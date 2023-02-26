answer = [0, 0, 0]

while 1 : 
    arr = list(map(int, input().split()))

    A = min(arr)
    C = max(arr)
    B = sum(arr) - A - C

    if A + B <= C : break
    else : 
        if A ** 2 + B ** 2 == C ** 2 : answer[0] += 1
        if A ** 2 + B ** 2 > C ** 2 : answer[1] += 1
        if A ** 2 + B ** 2 < C ** 2 : answer[2] += 1
        
print(sum(answer), *answer)
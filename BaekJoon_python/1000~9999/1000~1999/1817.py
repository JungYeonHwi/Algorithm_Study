N, M = map(int, input().split())

if N <= 0 : print(0)
else : 
    arr = list(map(int, input().split()))
    tmp = 0
    answer = 1
    
    for i in arr : 
        if i + tmp > M :
            tmp = i
            answer += 1
        else : 
            tmp += i
        
    print(answer)
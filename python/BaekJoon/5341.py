while 1 : 
    n = int(input())
    answer = 0
    if n == 0 : break
    else : 
        for i in range(1, n+1) : 
            answer += i
            
        print(answer)
while 1 : 
    n = int(input())
    answer = []
    
    if n == 0 : break
    else : 
        for _ in range(n) : 
            tmp = input()
            value = tmp.lower()
            answer.append([value, tmp])
            
    answer.sort()
    print(answer[0][1])
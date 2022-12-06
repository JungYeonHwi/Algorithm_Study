while 1 : 
    answer = []
    
    num = input().split()
    
    if num[0] == "0" : break
    num.remove(num[0])
    
    for i in num : 
        if len(answer) == 0 : answer.append(i)
        elif answer[-1] != i : answer.append(i)
        
    answer.append("$")
    
    print(*answer)
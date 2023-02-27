while 1 : 
    n = int(input())
    if n == 0 : break
    else : 
        s = input()
        arr = []
        chk = 0
        for i in range(0, len(s), n) : 
            if chk == 0 : 
                value = s[i:i+n]
                arr.append(value)
                chk = 1
            else : 
                value = s[i:i+n]
                value = value[::-1]
                arr.append(value)
                chk = 0
                
    result = list(map(list, zip(*arr)))
    answer = ""
    for i in result : 
        for j in i : 
            answer += j
            
    print(answer)
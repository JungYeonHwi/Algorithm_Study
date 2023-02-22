while 1 : 
    try : 
        n = int(input())
        answer = 1
        arr = []
        while 1 : 
            value = list(map(str, str(n * answer)))
            for i in value : 
                arr.append(i)
                
            if len(set(arr)) == 10 : 
                print(answer)
                break
            
            answer += 1
    except : break
        
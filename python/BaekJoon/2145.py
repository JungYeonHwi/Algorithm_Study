while 1 : 
    n = input()
    
    if n == "0" : break
    else : 
        arr = list(n)
        while len(arr) != 1 :
            s = 0
            for i in arr : 
                s += int(i)
            arr = list(str(s))
            
        print(arr[0])
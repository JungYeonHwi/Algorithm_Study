while 1 : 
    s = input()
    if s == "*" : break
    else : 
        s = s.lower()
        arr = list(map(str, s.split(" ")))
        value = arr[0][0]
        check = 0
        for i in arr : 
            if value != i[0] :
                check = 1
                
        if check == 1 : print("N")
        else : print("Y")
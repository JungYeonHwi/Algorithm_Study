while 1 : 
    n = int(input())
    arr = []
    if n == 0 : break
    else : 
        arr.append(n)
        while n != 1 : 
            if n % 2 == 0 : 
                n = n // 2
                arr.append(n)
            else : 
                n = n * 3 + 1
                arr.append(n)
                
        print(max(arr))
while 1 : 
    n = int(input())
    if n == 0 : break
    else : 
        arr = list(map(int, str(n)))
        while len(str(sum(arr))) != 1 : 
            arr = list(map(int, str(sum(arr))))
        print(sum(arr))
while 1 : 
    n, money = map(int, input().split())
    if n == 0 and money == 0 : break
    else : 
        arr = list(map(int, input().split()))
        pp = money // n
        cnt = 0
        for i in arr : 
            if pp <= i : cnt += pp
            else : cnt += i
        
        print(cnt)
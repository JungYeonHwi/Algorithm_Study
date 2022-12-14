for _ in range(int(input())) :
    a, n = map(int, input().split())
    s = ""
    while a >= n : 
        s = str(hex(a % n)[2:]) + s
        a //= n
    
    s = str(hex(a)[2:]) + s
    
    print(int(s == s[::-1]))
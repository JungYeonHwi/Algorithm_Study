while 1 :
    arr = list(map(int, input().split()))
    if arr[0] == 0 : break
    b, p, m = arr[0], arr[1], arr[2]
    n = int(str(p), b) % int(str(m), b)
    
    res = []
    while n >= b :
        res.append(str(n%b))
        n = n//b
    res.append(str(n))
    print(int(''.join(res[::-1])))
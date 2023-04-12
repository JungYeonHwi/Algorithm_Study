while 1:
    n = int(input())
    if n == 0:
        break
    s, e = 1, 50
    while s <= e:
        m = (s+e)//2
        print(m, end=' ')
        if m == n:
            break
        elif m < n:
            s = m+1
        else:
            e = m-1
    print()
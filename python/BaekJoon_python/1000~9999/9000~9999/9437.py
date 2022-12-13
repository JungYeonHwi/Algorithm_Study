while 1:
    t = list(map(int, input().split()))
    if t == [0] : break
    for i in range(t[0]//4) :
        arr = [2*i+1, 2*i+2, t[0]-2*i-1, t[0]-2*i]
        if t[1] in arr :
            arr.remove(t[1])
            print(*arr)
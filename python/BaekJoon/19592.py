for _ in range(int(input())):
    n, x, y = map(int,input().split()) 
    toys = list(map(int, input().split()))

    winner = max(toys)    
    if toys.count(winner) == 1 and toys[n-1] == winner :
        print(0)
        continue
    else :
        winner = x/winner

        def booster(v, bv) :
            dist = x - bv
            return (dist/v)+1

        l, r = 0, y
        time = x / toys[-1]

        while 1 :
            m = (l + r) // 2
            boost = booster(toys[-1], m)
            if l > r : break
            if boost >= winner : l = m+1
            else : r = m-1
        if l > y : print(-1)
        else : print(l)
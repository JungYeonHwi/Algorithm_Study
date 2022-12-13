T = int(input())

for _ in range(T) :
    n = int(input())
    t = 0
    
    while (t+1) + (t+1)**2 <= n :
        t += 1
    print(t)
for i in range(1, int(input()) + 1) : 
    a, b = map(int, input().split())
    
    res = a + b
    if res >= 24 : res -= 24
    
    print("#" + str(i) + res)
while 1 : 
    a, b, c = map(int, input().split())
    if (a == b and b == c and c == 0) : break
    
    if (a - b == b - c) : print("AP", c + (c-b))
    else : print("GP", c * (c // b))
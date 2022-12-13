while 1 :
    a, b, c = map(int, input().split())
    if a == b == c == 0 : break
    elif (c-a) % b == 0 : print((c-a)//b+1)
    else : print("X")
while 1 : 
    a, b, c = map(str, input().split())
    if a == "0" and b == "W" and c == "0" : break
    else : 
        if b == "W" : 
            value = int(a) - int(c)
            if value < -200 : print("Not allowed")
            else : print(value)
        if b == "D" : 
            value = int(a) + int(c)
            print(value)
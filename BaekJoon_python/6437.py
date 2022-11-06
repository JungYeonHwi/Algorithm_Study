num = 1
while 1 : 
    p, s = map(int, input().split())
    
    if p == 0 and s == 0 : break
    print("Hole #" + str(num))
    
    if s == 1 : 
        print("Hole-in-one.")
    elif s - p == -2 : 
        print("Eagle.")
    elif s - p == -1 : 
        print("Bridie.")
    elif s - p == 0 : 
        print("Par.")
    elif s - p == 1 :
        print("Bogey.")
    else : 
        if s - p < -2 : print("Double eagle.")
        else : print("Double Bogey.")
    
    print()
    
    num += 1
    
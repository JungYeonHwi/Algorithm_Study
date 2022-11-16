while 1 : 
    s = int(input())
    if s == 0 : break
    else : 
        print(s, end=" ")
        while len(str(s)) != 1 : 
            arr = list(map(int, str(s)))
            value = 1
            for i in arr : 
                value *= i
            s = value
            print(s, end=" ")
    print()
for _ in range(int(input())) : 
    s = input()
    if len(s) % 2 == 1 :
        for i in range(0,len(s), 2) : print(s[i],end='')
        for i in range(1, len(s),2) : print(s[i], end='')
        print()
        for i in range(1, len(s), 2) : print(s[i], end='')
        for i in range(0,len(s),2) : print(s[i],end='')
        print()
    else :
        for i in range(0, len(s), 2) : print(s[i], end='')
        print()
        for i in range(1, len(s), 2) : print(s[i], end='')
        print()

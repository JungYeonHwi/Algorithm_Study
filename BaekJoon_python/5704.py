while (1) : 
    s = input()
    check = 'Y'
    if (s == '*') : break
    else : 
        for a in range(97, 123) : 
            if s.find(chr(a)) == -1 : 
                check = 'N'
                
        print(check)
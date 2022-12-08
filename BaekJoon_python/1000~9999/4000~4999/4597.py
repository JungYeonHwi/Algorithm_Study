while 1 : 
    s = input()
    
    if s == "#" : break
    else : 
        i = s.count("1")
        
        if s[-1] == "e" :
            if i % 2 == 1 :
                s = s[:-1] + "1"
            else : 
                s = s[:-1] + "0"
        else : 
            if i % 2 == 1 :
                s = s[:-1] + "0"
            else : 
                s = s[:-1] + "1"
                
    print(s)
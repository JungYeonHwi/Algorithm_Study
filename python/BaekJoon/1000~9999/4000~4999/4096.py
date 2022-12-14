def check(s) : 
    if s == s[::-1] : return True
    else : return False

while 1 : 
    s = input()
    
    if s == "0" : break
    else : 
        cnt = 0

        while check(s) == False : 
            cnt += 1
            l = len(s)        
            s = str(int(s)+1)
            
            if len(s) != l : 
                diff = l - len(s)
                zero = "0" * diff
                s = zero + s
        
        print(cnt)
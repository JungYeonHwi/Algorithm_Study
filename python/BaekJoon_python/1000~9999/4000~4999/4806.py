s = 0
while 1 :    
    try :       
        i = input()        
        s += 1    
    except EOFError : break
print(s)
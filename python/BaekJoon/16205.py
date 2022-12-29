n, s = map(str, input().split())
answer = ["", "", ""]

if n == "1" : 
    answer[0] = s
    value = s[0].upper() + s[1:]
    answer[2] = value
    
    value = ""
    
    for i in s : 
        if i.isupper() : 
            value += "_" + i.lower()
        else : 
            value += i
    
    answer[1] = value
    
elif n == "2" : 
    answer[1] = s
    
    idx = []
    
    for i in range(len(s)) : 
        if s[i] == "_" : 
            idx.append(i+1)
    
    for j in idx : 
        s = s.replace(s[j], s[j].upper())
        
    s = s.replace("_", "") 
    
    answer[0] = s
    value = s[0].upper() + s[1:]
    answer[2] = value 
            
elif n == "3" : 
    answer[2] = s

    s = s.replace(s[0], s[0].lower())
    answer[0] = s
    
    value = ""
    
    for i in s : 
        if i.isupper() : 
            value += "_" + i.lower()
        else : 
            value += i
    
    answer[1] = value
    
for i in answer : 
    print(i)
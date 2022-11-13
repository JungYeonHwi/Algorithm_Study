import string

for _ in range(int(input())) : 
    
    check = list(string.ascii_lowercase)
    s = input()
    value = ''
    
    for i in s : 
        if i.isalpha() : value += i
    
    value = value.lower()
    arr = list(set(value))
    arr.sort()
    
    answer = ''
    
    for i in arr : 
        if i in check : check.remove(i)
        
    answer = "".join(check)
    
    if len(answer) == 0 : print("pangram")
    else : print("missing " + answer)
            
        
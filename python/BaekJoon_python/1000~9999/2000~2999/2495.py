result = []

for _ in range(3) : 
    s = input()
    length = 1
    List = []
    
    for i in range(1, 8) : 
        if s[i] == s[i - 1] : length += 1
        else : 
            List.append(length)
            length = 1
            
    List.append(length)
    result.append(max(List))
    
print(*result, sep='\n')
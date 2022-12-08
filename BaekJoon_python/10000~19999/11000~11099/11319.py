arr = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

for _ in range(int(input())) : 
    s = input()
    s = s.replace(" ", "")
    
    a = b = 0
    
    for i in s : 
        if i in arr : a += 1
        else : b += 1
        
    print(b, a)
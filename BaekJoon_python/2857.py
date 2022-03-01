List = []

for i in range(1, 6) : 
    s = input()
    
    if "FBI" in s : 
        List.append(i)
      
if List : print(*List)  
else : print("HE GOT AWAY!")
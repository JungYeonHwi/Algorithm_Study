dict = {}

for _ in range(int(input())) : 
    s = input()
    
    if s in dict : dict[s] += 1
    else : dict[s] = 1
    
m = max(dict.values())    

arr = [k for k,v in dict.items() if max(dict.values()) == v]
arr.sort()

print(arr[-1], m)

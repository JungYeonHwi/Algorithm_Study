d = 0
p = 0

for i in range(int(input())) : 
    s = input()
    
    if d < p + 2 and p < d + 2 : 
        if s == "D" : d += 1
        elif s == "P" : p += 1
        
print(str(d) + ":" + str(p))
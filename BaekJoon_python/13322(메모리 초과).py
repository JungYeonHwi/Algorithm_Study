s = input()
value = []

for i in range(len(s)) : 
    value.append(s[i:])
    
value.sort()

for i in value : 
    print(len(s) - len(i))
s = input()
joi = 0
ioi = 0

for i in range(0, len(s)-2) : 
    
    if s[i:i+3] == "JOI" : joi += 1
    elif s[i:i+3] == "IOI" : 
        ioi += 1
    
print(joi)
print(ioi)
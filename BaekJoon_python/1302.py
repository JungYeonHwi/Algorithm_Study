n = int(input())
a = []
d = dict()
b = []

for i in range(n) : 
    a.append(input())
    
for j in list(set(a)) : 
    d[j] = a.count(j)
    
for k in d.keys() : 
    if d[k] == max(d.values()) : b.append(k)
    
b.sort()
print(b[0])
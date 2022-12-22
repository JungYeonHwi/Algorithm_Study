arr = list(map(str, input()))

check = 10 - int(arr[-1])

idx = arr.index("*")

result = 0

for i in range(0, idx) : 
    if i % 2 == 0 : result += int(arr[i]) 
    else : result += int(arr[i]) * 3
    
for j in range(idx+1, len(arr)-1) : 
    if j % 2 == 0 : result += int(arr[j]) 
    else : result += int(arr[j]) * 3

if idx % 2 == 0 : rhq = 1
else : rhq = 3

for k in range(0, 10) : 
    
    c = result + rhq * k

    if c % 10 == check : 
        print(k)
        
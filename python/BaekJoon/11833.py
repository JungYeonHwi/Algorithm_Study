n, m = map(int, input().split())

origin = []
increase = []

for i in range(n) : 
    origin.append(input())
    
for i in range(n) : 
    increase.append(input())
    
check = 1
    
for o, i in zip(origin, increase) : 
    value = ""
    for j in o : 
        value += j * 2
    
    if value != i : 
        check = 0
        break
    
if check : print("Eyfa")
else : print("Not Eyfa")
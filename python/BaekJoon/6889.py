n = int(input())
m = int(input())

N = []
M = []

for _ in range(n) : 
    N.append(input())
    
for _ in range(m) : 
    M.append(input())
    
for i in N : 
    for j in M : 
        print(i, "as", j)
n, m = map(int, input().split())

pos = []
arr = []

for i in range(n) : 
    arr.append(list(map(int, input().split())))
    
for i in range(n) : 
    for j in range(m) : 
        if arr[i][j] == 1 : pos.append([i+1, j+1])
        
print(abs(pos[0][0] - pos[1][0]) + abs(pos[0][1] - pos[1][1]))
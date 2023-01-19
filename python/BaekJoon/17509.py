pen = 0
cnt = 0

arr = []

for i in range(11) : 
    a, b = map(int, input().split())
    arr.append([a, b])
    
arr.sort()

for i in range(11) : 
    pen += cnt + arr[i][0]
    cnt += arr[i][0]
    
for i in range(11) : 
    pen += (20 * arr[i][1])
    
print(pen)
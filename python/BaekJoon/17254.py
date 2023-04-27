n,m = map(int, input().split())
 
arr = []
 
for _ in range(m):
    a,b,c = input().split()
    a,b = int(a), int(b)
    c = str(c)
    arr.append([a,b,c])
    
arr.sort(key=lambda x: [x[1],x[0]])
 
[print(arr[i][2], end='') for i in range(len(arr)) ]

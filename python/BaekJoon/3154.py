def effortFun(h, m) : 
    h = str(h)
    m = str(m)
    result = 0
    
    if len(h) == 1 : h = "0" + h
    if len(m) == 1 : m = "0" + m

    arr = list(map(int, list(h+m)))
    
    for i in range(3) : 
        result += (abs(num[arr[i]][0] - num[arr[i+1]][0]) + abs(num[arr[i]][1] - num[arr[i+1]][1]))
        
    return result

origin = list(map(int, input().split(":")))    
num = {
    1 : [0, 0],
    2 : [0, 1],
    3 : [0, 2],
    4 : [1, 0],
    5 : [1, 1],
    6 : [1, 2],
    7 : [2, 0],
    8 : [2, 1],
    9 : [2, 2],
    0 : [3, 1]
}

hours = [origin[0] + 24 * i for i in range(5) if origin[0] + 24 * i < 100]
minutes = [origin[1] + 60 * i for i in range(2) if origin[1] + 60 * i < 100]
value = 999999
time = []

for h in hours : 
    for m in minutes : 
        effort = effortFun(h, m)
        if effort < value : 
            value = effort
            time = [[h, m]]
        elif effort == value : time.append([h, m])
        
time.sort(key = lambda x : [x[0], x[1]])    

h = str(time[0][0])
m = str(time[0][1])

if len(h) == 1 : h = "0" + h
if len(m) == 1 : m = "0" + m

print("{}:{}".format(h, m))

n, m = map(int, input().split())
data = []
qus = 0
s = 0
e = 0

for _ in range(n) : 
    value = input()
    
    
    if "#" in value : 
        value = "".join(value)
        s = value.find("#")
        e = value.rfind("#")
        
        arr = list(map(str, value[s:e+1]))
        data.append(arr)

qus = len(data)

for i in data : 
    while len(i) != qus : 
        i.append(".")
        
if data[0][qus//2] == "." : print("UP")
if data[len(data)-1][qus//2] == "." : print("DOWN")
if data[qus//2][len(data)-1] == "." : print("RIGHT")
if data[qus//2][0] == "." : print("LEFT")
n = int(input())

dx = [0,-1,0,1]
dy = [1,0,-1,0] 

for i in range(n):
    px = 0
    py = 0
    pd = 0 
    move = list(input())
    trace = [(px, py)]
    for j in move:
        if j == 'F':
            px = px + dx[pd]
            py = py + dy[pd]
        elif j == 'B':
            px = px - dx[pd]
            py = py - dy[pd]
        elif j == 'L':
            if pd == 3:
                pd = 0
            else:
                pd += 1
        elif j == 'R':
            if pd == 0:
                pd = 3
            else:
                pd -= 1

        trace.append((px, py))
    width = max(trace, key = lambda x:x[0])[0] - min(trace, key = lambda x:x[0])[0]
    height = max(trace, key = lambda x:x[1])[1] - min(trace, key = lambda x:x[1])[1]
    print(width * height)
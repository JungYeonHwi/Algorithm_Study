import sys

def draw(depth, idx):
    if depth == 1:
        Map[idx][idx] = '*'
        Map[idx+1][idx] = '*'
        Map[idx+2][idx] = '*'
        return
    
    r = 4 * (depth - 1) + 1
    c = 4 * (depth - 1) + 3
    
    for i in range(idx, r+idx):
        Map[idx][i] = '*'
        Map[idx+r+1][i] = '*'
    for i in range(idx, c+idx):
        Map[i][idx] = '*'
        Map[i][idx+r-1] = '*'
        
    Map[idx+1][idx+r-1] = ' '
    Map[idx+2][idx+r-2] = '*'
    
    draw(depth-1, idx+2)
    return
    
    
n = int(input())

if n == 1:
    print('*')
    sys.exit()

row = 4 * (n - 1) + 1
col = 4 * (n - 1) + 3

Map = [[' '] * row for _ in range(col)]

draw(n,0)

for i in range(col):
    if i == 1:
        print('*')
        continue
    for j in range(row):
        print(Map[i][j], end="")
    print("")
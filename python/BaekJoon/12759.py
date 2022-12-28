def isFinished(turn) : 

    for i in range(3) : 
        for j in range(3) : 
            if Map[i][j] != turn : break
            if j == 2 : return turn

    for j in range(3) :
        for i in range(3) : 
            if Map[i][j] != turn : break
            if j == 2 : return turn
 
    for i in range(3) : 
        if Map[i][i] != turn : break
        if i == 2 : return turn
        
    for i in range(3) : 
        if Map[i][2-i] != turn : break
        if i == 2 : return turn
 

r = 0
c = 0
win = 0
next = 0

stop = False

Map = [[0 for _ in range(4)] for _ in range(4)]

start = int(input())

for i in range(9) :
    if i % 2 == 0 : next = start
    else : 
        if start == 2 : next = 1
        else : next = 2

    r, c = map(int, input().split())

    r -= 1
    c -= 1

    Map[r][c] = next
    
    if not stop :
        win = isFinished(next)
        if win != 0 : stop = True

print(win)
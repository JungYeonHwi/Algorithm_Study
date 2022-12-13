def check(i, j) : 
    for a in range(8) : 
        ni, nj = i+di[a], j+dj[a]
        
        if 0 <= ni < R and 0 <= nj < C and board[ni][nj] != "*" : board[ni][nj] += 1


di = [-1, -1, -1, 0, 1, 1, 1, 0]
dj = [-1, 0, 1, 1, 1, 0, -1, -1]

while 1 : 
    R, C = map(int, input().split())
    if R == C == 0 : break
    
    board = [[] for _ in range(R)]

    for i in range(R) : 
        data = input()
        for j in range(C) :
            if data[j] == "." : board[i].append(0)
            else : board[i].append("*")
            
    for i in range(R) : 
        for j in range(C) : 
            if board[i][j] == "*" : check(i, j)
    
    for i in board : 
        print(*i, sep="")
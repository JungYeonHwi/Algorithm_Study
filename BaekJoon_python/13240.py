n, m = map(int, input().split())

board = [[0 for i in range(m)] for _ in range(n)]

for i in range(n) : 
    for j in range(m) : 
        if i % 2 == 0 : 
            if j % 2 == 0 : board[i][j] = "*"
            else : board[i][j] = "."
        else : 
            if j % 2 == 0 : board[i][j] = "."
            else : board[i][j] = "*"
            
for i in range(n) : 
    for j in range(m) : 
        print(board[i][j], end="")
    print()
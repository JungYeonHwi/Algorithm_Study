n = int(input())
board = [list(map(int, input())) for _ in range(n)]

def DFS(x, y, n) : 
    check = board[x][y]
    for i in range(x, x + n) :
        for j in range(y, y + n) : 
            if check != board[i][j] : 
                check = -1
                break
    
    if check == -1 : 
        print("(", end="")
        n = n // 2
        DFS(x, y, n)
        DFS(x, y + n, n)
        DFS(x + n, y, n)
        DFS(x + n, y + n, n)
        print(")", end="")
        
    elif check == 1 : print(1, end="")
    elif check == 0 : print(0, end="")
    
DFS(0, 0, n)
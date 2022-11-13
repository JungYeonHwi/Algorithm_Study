from sys import stdin

n, m, q = map(int, stdin.readline().split())
board = []

for _ in range(n) : 
    one = list(map(int, stdin.readline().split()))
    board.append(one)
    
for i in range(q) : 
    arr = list(map(int, stdin.readline().split()))
    
    if arr[0] == 0 : 
        a = arr[1]
        b = arr[2]
        k = arr[3]
        board[a][b] = k
    elif arr[0] == 1 : 
        a = arr[1]
        b = arr[2]
        board[a], board[b] = board[b], board[a]

for ii in board : 
    for jj in ii : 
        print(jj, end = " ")
    print()
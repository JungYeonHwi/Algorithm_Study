board = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(4) : 
    a, b, c, d = map(int, input().split())
    
    for i in range(a, c) : 
        for j in range(b, d) : 
            board[i][j] = 1
            
answer = 0
for row in board :
    answer += sum(row)
print(answer)
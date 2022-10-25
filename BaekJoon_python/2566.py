import sys
input = sys.stdin.readline

board = []

for _ in range(9) : 
    board.append(list(map(int, input().split())))
    
x = 0
y = 9
maxValue = -1

for i in range(9) : 
    for j in range(9) : 
        if board[i][j] > maxValue : 
            maxValue = board[i][j]
            x = i + 1
            y = j + 1

print(maxValue)
print(x, y)
import sys
input = sys.stdin.readline

board = [[0 for _ in range(101)] for _ in range(101)]

answer = 0

n = int(input())

for _ in range(n) : 
    a, b = map(int, input().split())
    
    for i in range(a, a+10) : 
        for j in range(b, b+10) : 
            board[i][j] = 1
            
for row in board :
    answer += row.count(1)
    
print(answer)
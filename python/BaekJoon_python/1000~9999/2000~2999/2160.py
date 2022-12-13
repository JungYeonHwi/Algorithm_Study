n = int(input())
board = []

answer1 = 0
answer2 = 0
m = 36

for i in range(n) : 
    row = []
    for _ in range(5) : 
        row.append(input())
    board.append(row)
    
for i in range(n) : 
    for j in range(i+1, n) : 
        cnt = 0
        for r in range(5) : 
            for c in range(7) : 
                if board[i][r][c] != board[j][r][c] : cnt += 1

        if m > cnt : 
            m = cnt
            answer1 = i
            answer2 = j


print(f'{answer1 + 1} {answer2 + 1}')
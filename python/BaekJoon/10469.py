import sys
input = sys.stdin.readline

def check(x,y):
    for a,b in move:
        tx = x; ty = y
        for i in range(7) :
            tx += a; ty += b
            if tx >= 8 or tx < 0 or ty >= 8 or ty < 0 :
                break
            if board[tx][ty] == '*' :
                return 1
    

board = [list(input().rstrip()) for _ in range(8)]
move = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
cnt = 0
for i in range(8):
    for j in range(8):
        if board[i][j]=='*':
            cnt += 1
            if check(i,j):
                print('invalid')
                sys.exit()
print('valid' if cnt==8 else 'invalid')
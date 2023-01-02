import sys
sys.stdin.readline

def makeSnail(n):
    global tx, ty
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    completeSnail = [[0 for _ in range(n)] for _ in range(n)]
    
    cnt = n**2
    direction = 0
    x, y = 0, 0
    completeSnail[x][y] = cnt
    cnt -= 1
    while cnt > 0:

        nx = x + dx[direction]
        ny = y + dy[direction]

        if 0 <= nx < n and 0 <= ny < n and not completeSnail[nx][ny]:
            completeSnail[nx][ny] = cnt
            if cnt==target:
                tx,ty = nx,ny
            x, y = nx, ny
            cnt -= 1
        else :
            direction = (direction+1) % 4
    return completeSnail


N = int(input())
target = int(input())
tx, ty = 0,0
snail = makeSnail(N)
for row in snail :
    print(*row)
print(tx+1, ty+1)
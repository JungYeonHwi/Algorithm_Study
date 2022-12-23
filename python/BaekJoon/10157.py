C, R = map(int,input().split())

s = int(input())

if s > C * R :
    print(0)
    exit()

dx = [0,1,0,-1]
dy = [-1,0,1,0]

grid = [[0]*C for _ in range(R)]
direction = x = y = 0

for seat in range(1,C*R+1) :
    
    if seat == s :
        print(y+1,x+1)
        break
    else :
        grid[x][y] = seat
        
        x += dx[direction]
        y += dy[direction]

        if x < 0 or y < 0 or x >= R or y >= C or grid[x][y] :
            x -= dx[direction]
            y -= dy[direction]
            
            direction = (direction+1)%4
            x += dx[direction]
            y += dy[direction]
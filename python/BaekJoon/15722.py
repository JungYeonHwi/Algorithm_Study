n = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x = 0
y = 0
cnt = 0
now = 0

while 1 : 
    for _ in range(cnt // 2 + 1) : 
        if now == n : 
            print(x, y)
            exit()
        x += dx[cnt % 4]
        y += dy[cnt % 4]
        now += 1
    cnt += 1
    
print(x, y)
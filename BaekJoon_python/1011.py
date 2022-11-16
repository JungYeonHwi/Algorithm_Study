t = int(input())

for _ in range(t) :
    x, y = map(int,input().split())
    distance = y - x
    count = 0
    move = 1
    s = 0
    while s < distance :
        count += 1
        s += move
        if count % 2 == 0 : move += 1  
    print(count)
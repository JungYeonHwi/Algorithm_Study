n, k = map(int, input().split())
medals = [list(map(int, input().split())) for _ in range(n)]
medals.sort(key = lambda x : (x[1], x[2], x[3]), reverse = True)

grade, s = 1, 0

for i in range(n) : 
    if i != 0 : 
        if medals[i-1][1:] == medals[i][1:] : 
            s += 1
        else : 
            if s : 
                grade += s
                s = 0
            grade += 1
    if medals[i][0] == k : 
        print(grade)
        break
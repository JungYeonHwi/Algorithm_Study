for _ in range(int(input())) : 
    p, s = map(str, input().split())
    answer = 0
    while s in p : 
        p = p.replace(s, "", 1)
        answer += 1
        
    print(answer + len(p))
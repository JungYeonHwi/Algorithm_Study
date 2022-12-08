for _ in range(int(input())) : 
    n, m = map(int, input().split())
    score = [[0, 0] for _ in range(n)]
    answer = []
    
    for i in range(m) : 
        a, b, p, q = map(int, input().split())
        score[a-1][0] += p
        score[a-1][1] += q
        score[b-1][0] += q
        score[b-1][1] += p
    
    for j in range(n) : 
        if score[j][0] == 0 and score[j][1] == 0 : answer.append(0)
        else : answer.append(1000 * score[j][0] ** 2 / (score[j][0] ** 2 + score[j][1] ** 2))
        
    print(int(max(answer)))
    print(int(min(answer)))
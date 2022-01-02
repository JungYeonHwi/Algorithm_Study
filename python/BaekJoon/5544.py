n = int(input())
score = {i : 0 for i in range(1, n+1)}

for _ in range(n * (n - 1) // 2) : 
    a, b, scorea, scoreb = map(int, input().split())
    if scorea > scoreb :
        score[a] += 3
    elif scorea == scoreb : 
        score[a] += 1
        score[b] += 1
    else : score[b] += 3
    
result = []

for team, s in score.items() : 
    result.append([s, team])

result.sort(reverse=True)

idx = 0
result[0].append(1)

for i in range(1, n) : 
    if result[i-1][0] == result[i][0] : 
        result[i].append(result[i-1][2])
        idx += 1
    elif result[i-1][0] > result[i][0] : 
        result[i].append(result[i-1][2] + 1 + idx)
        idx = 0

result.sort(key = lambda x : x[1])

for i in range(n) :
    print(result[i][2])
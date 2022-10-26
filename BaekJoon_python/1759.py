from itertools import combinations

l, c = map(int, input().split())
alpha = list(map(str, input().split()))
alpha.sort()

result = list(combinations(alpha, l))
answer = []

for i in result : 
    one = []
    for j in i : 
        one.append(j)
    one.sort()
    
    vCnt = 0
    cCnt = 0
    
    for key in one : 
        if key == "a" or key == "e" or key == "i" or key == "o" or key == "u" : vCnt += 1
        else : cCnt += 1
        
    tmp = "".join(one)
        
    if vCnt >= 1 and cCnt >= 2 and tmp not in answer : answer.append(tmp)
    
answer.sort()

for i in answer : 
    print(i)
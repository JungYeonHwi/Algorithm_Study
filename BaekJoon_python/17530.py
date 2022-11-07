score = []
maxS = 0

for _ in range(int(input())) : 
    tmp = int(input())
    score.append(tmp)
    
    if maxS < tmp : maxS = tmp
    
if maxS == score[0] : print("S")
else : print("N")
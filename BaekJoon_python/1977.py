M = int(input())
N = int(input())
List = []
answer = []

for i in range(1, 101) : 
    List.append(i*i)

for i in List : 
    if (i >= M and i <= N) : answer.append(i)
    
if (len(answer) == 0) : print(-1)
else : 
    print(sum(answer))
    print(min(answer))
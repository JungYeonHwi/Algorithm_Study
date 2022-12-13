List = [0] * 31

for _ in range(28) :
    n = int(input())
    List[n] = 1

answer = [] 
   
for i in range(1, 31) : 
    if List[i] == 0 : answer.append(i)

m = min(answer)
M = max(answer)

print(m)
print(M)
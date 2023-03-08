n = int(input())
s = []
a = []
answer = 0

for i in range(n) : 
    s.append(input())
    
for j in range(n) : 
    a.append(input())
    
for ss, aa in zip(s, a) : 
    if ss == aa : answer += 1
    
print(answer)
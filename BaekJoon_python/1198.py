n = int(input())
x = []
y = []
for _ in range(n) : 
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
    
answer = 0
    
for i in range(n) : 
    for j in range(i+1, n) : 
        for k in range(j+1, n) : 
            answer = max(answer, abs(x[i] * y[j] + x[j] * y[k] + x[k] * y[i] - x[j] * y[i] - x[k] * y[j] - x[i] * y[k]))

if answer % 2 : print(answer / 2)
else : print(answer / 2);   
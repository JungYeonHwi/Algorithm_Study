n, k = map(int, input().split())
arr = []
answer = []
num = 0

for i in range(1, n+1) : 
    arr.append(i)
    
for _ in range(n) : 
    num += k - 1
    if num >= len(arr) : num = num % len(arr)
    
    answer.append(str(arr.pop(num)))
    
print("<", ", ".join(answer)[:], ">", sep="")
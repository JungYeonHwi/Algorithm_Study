n = int(input())
answer = 0

for i in range(1, n+1) : 
    num = list(map(int, str(i)))
    if i % sum(num) == 0 : answer += 1

print(answer)
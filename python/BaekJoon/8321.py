n, k, s = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=1)

answer = 0
value = k * s

for i in arr : 
    if value > 0 : 
        answer += 1
        value -= i
        
print(answer)
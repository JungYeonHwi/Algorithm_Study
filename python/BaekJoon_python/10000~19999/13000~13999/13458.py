n = int(input())
arr = list(map(int, input().split()))
a, b = map(int, input().split())

answer = n

for i in arr : 
    i -= a
    if i > 0 : 
        if i % b : answer += (i // b) + 1
        else : answer += (i // b)

print(answer)
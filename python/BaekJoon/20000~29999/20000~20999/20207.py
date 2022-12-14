N = int(input())
calendar = [0] * 367
arr = []

for _ in range(N) :
    s, e = map(int, input().split())
    calendar[s] += 1
    calendar[e+1] -= 1
 
width = 0
height = 0
answer = 0

for i in range(1, 367) :
    calendar[i] += calendar[i-1]
    if calendar[i] == 0 :
        answer += width*height
        width = 0
        height = 0
    else :
        width += 1
        height = max(height, calendar[i])
 
print(answer)
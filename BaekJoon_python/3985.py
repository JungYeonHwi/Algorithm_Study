l = int(input())
n = int(input())

arr = []
predict = 0
answer1 = 0
answer2 = 0
bread = [0 for _ in range(l)]

for idx in range(1, n+1) : 
    a, b = map(int, input().split())
    for i in range(a, b+1) :
        if bread[i-1] == 0 : bread[i-1] = idx
    
    if predict < abs(a-b) + 1 : 
        predict = abs(a-b) + 1
        answer2 = idx
    
for i in range(1, n+1) : 
    if answer1 < bread.count(i) : 
        answer1 = bread.count(i)
        value = i
        
print(answer2)
print(value)
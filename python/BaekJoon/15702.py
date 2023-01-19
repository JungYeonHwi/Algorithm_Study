n, m = map(int, input().split())
score = list(map(int, input().split()))
answer = 0
ans = []
name = 100000

whole = []

for _ in range(m) :
    value = list(map(str, input().split()))
    
    num = int(value[0])
    arr = value[1:]
    
    result = 0
    
    for i in range(len(arr)) : 
        if arr[i] == "O" : result += score[i]
        
    whole.append([num, result])
    
    answer = max(answer, result)
    
for i in range(len(whole)) : 
    if whole[i][1] == answer : 
        name = min(name, whole[i][0])
        
print(name, answer)
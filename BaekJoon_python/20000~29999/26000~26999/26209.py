arr = list(map(int, input().split()))
answer = "S"

for i in arr : 
    if i != 0 and i != 1 : answer = "F"
    
print(answer)
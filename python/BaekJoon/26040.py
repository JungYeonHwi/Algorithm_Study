s = input()
arr = list(map(str, input().split()))

answer = ""

for i in s : 
    if i in arr : answer += i.lower()
    else : answer += i
    
print(answer)
s = input()
change = []

for i in range(1, len(s)) :
    if s[i-1] != s[i] : change.append(i) # 반환점 위치 저장
    
isOdd = False
if len(change) %2 == 1 : isOdd = True
    
result = len(change)//2

if isOdd :
    result += 1
print(result)
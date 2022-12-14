answer = 0

for _ in range(int(input())) :
    s = input()
    num = int(s[2:])
    if num <= 90 : answer += 1
    
print(answer)
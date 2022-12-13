n = int(input())
s = input()

answer = 0

if n % 2 == 0 :
    copy = s[n//2:]
    s = s[:n//2]
    
    for i, j in zip(s, copy[::-1]) : 
        if i != j : answer += 1

else : 
    copy = s[n//2+1:]
    s = s[:n//2]
    
    for i, j in zip(s, copy[::-1]) : 
        if i != j : answer += 1

print(answer)
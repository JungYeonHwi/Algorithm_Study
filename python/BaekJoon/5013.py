answer = 0

for _ in range(int(input())) : 
    s = input()
    for i in range(len(s)-1) : 
        if s[i] == "C" and s[i+1] != "D" : answer += 1
        
print(answer)
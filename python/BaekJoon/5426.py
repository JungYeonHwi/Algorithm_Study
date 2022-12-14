from math import sqrt

for i in range(int(input())) : 
    s = input()
    n = int(sqrt(len(s)))
    
    answer = ""
    
    for j in range(n-1, -1, -1) : 
        for idx in range(0, len(s), n) : 
            word = s[idx:idx+n]
            answer += word[j]
            
    print(answer)
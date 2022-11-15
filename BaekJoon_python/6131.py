n = int(input())
answer = 0

for a in range(1, 501) : 
    for b in range(1, a+1) : 
        aa = a ** 2
        bb = b ** 2
        if aa - bb == n : answer += 1
        
print(answer)
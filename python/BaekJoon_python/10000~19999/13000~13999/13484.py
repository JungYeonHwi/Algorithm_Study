x = int(input())
answer = 0
for _ in range(int(input())) : 
    n = int(input())
    answer += (x - n)
    
if answer + x <= 0 : print(0)
else : print(answer + x)
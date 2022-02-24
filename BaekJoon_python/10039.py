s = 0

for i in range(5) : 
    N = int(input())
    
    if N < 40 : s += 40
    else : s += N

print(int(s / 5))
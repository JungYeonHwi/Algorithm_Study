import sys
from itertools import product

n = int(sys.stdin.readline())

data = ['O', 'L', 'A']

result = list(product(data, repeat=n))
answer = 0

for i in result : 
    comb = list(i)
    s = "".join(comb)
    
    lCount = s.count("L")
    
    if lCount < 2 : 
        idx = s.find("A")
        if s[idx:idx+3] != "AAA" : answer += 1
        
print(answer)
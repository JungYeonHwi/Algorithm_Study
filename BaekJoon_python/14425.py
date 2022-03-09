import sys
input = sys.stdin.readline

A, B = map(int, input().split())
S = []
count = 0

for _ in range(A) : 
    S.append(input().strip())
    
for _ in range(B) : 
    data = input().strip()
    if data in S : count += 1
    
print(count)
import sys
input = sys.stdin.readline

n = int(input())
answer = []
m = 0

for _ in range(n) : 
    a, b = map(str, input().split())
    answer.append([a, int(b)])
    
    if int(b) > m : m = int(b)
    
answer.sort(key = lambda x : x[1], reverse=True)

name = []
for i, j in answer : 
    if j == m : name.append(i)
    
name.sort()
print(name[0])
a, b = map(int, input().split())
aSet = set()
bSet = set()

for _ in range(a) : 
    aSet.add(input())
    
for _ in range(b) : 
    bSet.add(input())

answer = sorted(list(aSet & bSet))

print(len(answer))

for i in answer : 
    print(i)
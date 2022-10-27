t = int(input())

for i in range(t) :
    problems = int(input())
    
    for j in range(problems) : 
        n = list(map(int, input().split()))
        print(n[0] + n[1], n[0] * n[1])

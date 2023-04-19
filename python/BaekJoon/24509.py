import sys
input = sys.stdin.readline

n = int(input().rstrip())
students = {}
ans = [[-1, -1] for _ in range(4)]

for i in range(n) : 
    number, a, b, c, d = map(int, input().split())
    score = [a, b, c, d]
    students[number] = score
    
for i in range(4) : 
    for s in students : 
        if ans[i][1] < students[s][i] : 
            ans[i][0] = s
            ans[i][1] = students[s][i]
        if ans[i][1] == students[s][i] : 
            ans[i][0] = min(s, ans[i][0])
        
    del(students[ans[i][0]])
    
for i in range(4) : 
    print(ans[i][0], end=" ")
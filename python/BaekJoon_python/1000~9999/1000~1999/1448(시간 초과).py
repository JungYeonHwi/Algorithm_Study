from itertools import combinations

n = int(input())
arr = []

for _ in range(n) :
    arr.append(int(input()))
    
result = list(combinations(arr, 3))
answer = []

for i in result :
    lst = list(i)
    lst.sort()
    if lst[0] + lst[1] > lst[2] : 
        answer.append(sum(lst))
    
if len(answer) == 0 : print(-1)
else : print(max(answer))
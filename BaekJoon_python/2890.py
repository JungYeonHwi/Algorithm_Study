import re

R, C = map(int, input().split())
answer = [-1] * 9

for _ in range(R) : 
    S = re.split('[1-9]{2}', input())
    if S[0].count('.') != (C-2) :
        answer[int(S[1][0])-1] = ((C-5) - S[0].count('.'))
        
dict = {}
rank = 1

for i in sorted(answer) : 
    if i not in dict : 
        dict[i] = rank
        rank += 1

arr = [dict[i] for i in answer]

for i in arr : 
    print(i)
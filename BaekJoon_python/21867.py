n = int(input())
s = input()

answer = ""

for i in s : 
    if i not in ["J", "A", "V"] : answer += i

if len(answer) == 0 : print("nojava")
else : print(answer)
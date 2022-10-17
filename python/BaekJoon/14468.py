import sys
cows = sys.stdin.readline().strip()
answer = []
dic = {chr(i): [-1, -1] for i in range(65, 91)} 
for i, c in enumerate(cows): 
    if dic[c][0] == -1: 
        dic[c][0] = i
    else: 
        dic[c][1] = i

for i in range(52):
    for j in range(i+1, 52): 
        if dic[cows[i]][0] < dic[cows[j]][0] < dic[cows[i]][1] < dic[cows[j]][1] or dic[cows[i]][0] > dic[cows[j]][0] > dic[cows[i]][1] > dic[cows[j]][1]:
            if cows[i] != cows[j] and set([cows[i], cows[j]]) not in answer:
                answer.append(set([cows[i], cows[j]])) 
print(len(answer))

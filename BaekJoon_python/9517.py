i = int(input()) - 1
q = [input().split() for _ in range(int(input()))]
tt = 0

for t, answer in q : 
    tt += int(t)
    if tt >= 210 : 
        print(i+1)
        break
    if answer == "T" : 
        i = (i + 1) % 8
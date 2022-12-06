n = input()
dongari = ['PROBRAIN','GROW','ARGOS','ADMIN','ANT','MOTION','SPG','COMON','ALMIGHTY']
dongariMax = []
for i in range(9) :
    dongariMax.append(max(list(map(int, input().split()))))
checkmax = max(dongariMax)

for i in range(9) :
    if checkmax == dongariMax[i] : 
        print (dongari[i])
        break
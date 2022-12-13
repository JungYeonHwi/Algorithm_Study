N = int(input())

check = [False] + [True] * 103
primenum = []
answer = []

for i in range(2, 104) :
    if check[i] :
        primenum.append(i)
        for j in range(2*i,104, i) :
            check[j] = False

for i in range(1,len(primenum)) :
    answer.append(primenum[i]*primenum[i-1])

for i in answer :
    if i > N :
        print(i)
        break
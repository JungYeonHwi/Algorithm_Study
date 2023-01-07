n=int(input())
a = [False,False] + [True]*(n-1)
primes = []

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

answer = []

for i in primes :
    visited = dict()
    temp = str(i)
    while 1 :
        tmp = sum(map(lambda x:int(x)**2,temp))
        
        idx = int(temp)
        if tmp == 1 :
            answer.append(i)
            break
        if visited.get(idx) :
            break
        else :
            visited[idx] = 1
        temp = str(tmp)

answer.sort()

for i in answer:
    print(i)
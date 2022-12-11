n, k = map(int, input().split())
s = k*(k+1)//2
if s > n : print(-1) 
elif (n-s) % k == 0 : print(k-1)
else : print(k)
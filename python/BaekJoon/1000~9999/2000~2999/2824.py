def gcd(n,m) :
	while m > 0 : n, m = m, n % m
	return n

n = int(input())
nList = list(map(int,input().split()))
m = int(input())
mList = list(map(int,input().split()))

nNum = 1
mNum = 1

for i in nList : nNum *= i
for i in mList : mNum *= i

print(str(gcd(nNum, mNum))[-9:])
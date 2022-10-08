import sys
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

n=int(sys.stdin.readline().rstrip())

for i in range(n):  
    li=[]
    a=list(map(int,sys.stdin.readline().split()))
    for j in range(len(a)):  
        for k in range(len(a)):  
            if j>k and j!=k: 
                li.append(gcd(a[j],a[k]))  
            else:
                pass
    print(max(li))

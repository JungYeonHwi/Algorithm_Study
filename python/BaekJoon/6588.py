import math
arr = [True for i in range(1000001)]
primelist = []
def prime_list(x):
    global primelist
    for i in range(2,int(math.sqrt(1000000))+1):
        if arr[i] == True:
            for j in range(i+i,1000001,i):
                arr[j] = False
    primelist = [i for i in range(2,1000001) if arr[i]==True]
prime_list(1000000)

while True:
    n = int(input())
    if not n:
        break       
    for i in primelist:
        if arr[n-i] :
            print('%d = %d + %d' %(n,i,n-i))
            break
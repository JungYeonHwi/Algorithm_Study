n1, a = input().split()
n2 = int(a+n1)
n1 = int(n1)

arr = [1] * (n2+1)
for i in range(2, int(n2**0.5)+1):
    if arr[i] == 1 :
        for j in range(i+i, n2+1, i) :
            arr[j] = 0
prime = [i for i in range(2, n2+1) if arr[i] == 1]
print("Yes" if n1 in prime and n2 in prime else "No")
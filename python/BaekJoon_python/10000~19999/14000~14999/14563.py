def prime(num) : 
    s = 0
    for i in range(1, num) :
        if num % i == 0 :
            s += i
    return s

n = int(input())
arr = list(map(int, input().split()))

for i in arr : 
    if i == prime(i) : print("Perfect")
    elif i < prime(i) : print("Abundant")
    elif i > prime(i) : print("Deficient")
def GCD(a, b) :
    if max(a, b) % min(a, b) : return GCD(max(a, b) % min(a, b), min(a, b))
    else : return min(a, b)

a, b = map(int, input().split())

for i in range(1, GCD(a, b) + 1) :
    if GCD(a, b) % i == 0 :
        print(i, a // i, b // i)
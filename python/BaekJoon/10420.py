N = int(input())
Y = 2014
M = 4
D = 1
years = [i for i in range(2014, 2044) if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0]

for _ in range(N) :
    if M == 2 :
        if D == 28 and Y in years : D = 29
        elif (D == 28 and Y not in years) or (D == 29 and Y in years) :
            D = 1
            M = 3
        else :
            D += 1
    elif M in [4, 6, 9, 11] and D == 30 :
        D = 1
        M += 1
    elif M in [1, 3, 5, 7, 8, 10] and D == 31 :
        D = 1
        M += 1
    elif M == 12 and D == 31 :
        M = 1
        D = 1
        Y += 1
    else :
        D += 1

print(f'{Y}-{M:02d}-{D:02d}')
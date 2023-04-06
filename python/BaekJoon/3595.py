n = int(input())

m = 987654321
num = [0, 0, 0]

for i in range(1, n+1) : 
    for j in range(1, i+1) : 
        if i * j > n :  break

        for k in range(1, j+1) : 
            if i * j * k > n : break
            if i * j * k == n :
                s = i * j + j * k + k * i;
                if s < m : 
                    m = sum
                    num[0] = i
                    num[1] = j
                    num[2] = k

print(*num)
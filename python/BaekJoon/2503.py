import sys
from itertools import permutations

n = int(input())
num = list(permutations([1,2,3,4,5,6,7,8,9], 3))

for _ in range(n):
    test, s, b = map(int, input().split())
    test = list(str(test))
    remove = 0

    for i in range(len(num)):
        sc = bc = 0
        i -= remove

        for j in range(3):
            test[j] = int(test[j])
            if test[j] in num[i] :
                if j == num[i].index(test[j]) :
                    sc += 1
                else:
                    bc += 1
    
        if sc != s or bc != b :
            num.remove(num[i])
            remove += 1

print(len(num))
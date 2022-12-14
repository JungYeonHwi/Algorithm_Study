import math

for _ in range(int(input())) : 
    n = int(input())
    value = math.factorial(n)
    arr = list(str(value))
    reversedArr = arr[::-1]
    for i in reversedArr : 
        if i != "0" : 
            print(i)
            break
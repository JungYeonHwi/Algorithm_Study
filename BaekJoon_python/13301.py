a1 = 4     #
a2 = 6
result = 0
n = int(input())
if n == 1 : result = a1
elif n == 2 : result = a2
else :
    for i in range(2, n) :
        result = a1 + a2
        a1 = a2
        a2 = result
print(result)
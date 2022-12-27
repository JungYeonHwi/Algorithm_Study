from sys import stdin
from math import factorial

def solve(string, i):
    global cnt
    if i == len(a):
        cnt += 1
        if cnt == b:
            return string
    else:
        for k in a:
            if k not in string:
                res = solve(string + k, i + 1)
                if res:
                    return res

    return


while 1:
    cnt = 0
    data = stdin.readline().rstrip().split()

    if len(data) != 2 : break

    a, b = data
    b = int(b)

    if factorial(len(a)) < b :
        print(a, b, '=', 'No permutation')
    else :
        print(a, b, '=', solve('', 0))
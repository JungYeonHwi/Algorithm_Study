import sys

T = int(sys.stdin.readline())
for i in range(T) :
    arr = list()
    res = 0
    money = 5 * (10 ** 6)
    while 1 :
        ground = int(sys.stdin.readline())
        if ground == 0 : break
        arr.append(ground)

    arr.sort(reverse=True)
    for j in range(len(arr)) :
        res += 2 * (arr[j] ** (j + 1))

    if money < res : print("Too expensive")
    else : print(res)
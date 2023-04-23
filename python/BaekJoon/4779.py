from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

def div(s, idx):
    ls = len(s)
    if ls == 3 and idx != 1:
        return '- -'
    elif ls >= 3 and idx == 1:
        return s.replace('-', ' ')

    arr = []

    for i in range(0, ls, ls // 3):
        arr.append(string[i:i+ls//3])

    k = div(arr[0], 0) + div(arr[1], 1) + div(arr[2], 2)
    return k


while 1:
    k = '-'
    n = stdin.readline().rstrip()
    if n == '':
        break
    num = (3 ** int(n))
    if num == 1:
        print('-')
        continue

    string = k * num
    arr = div(string, 0)
    print(arr)
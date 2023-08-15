while True:
    n = input()
    if n == '0': break
    li = sorted(n.split()[1:])
    num1, num2 = str(), str()
    for i in range(len(li)):
        if li[i] != '0':
            num1, num2 = li[i], li[i + 1]
            li = li[:i] + li[i + 2:]
            break
    for i in range(0, len(li), 2):
        num1 += li[i]
        if i < len(li) - 1:
            num2 += li[i + 1]

    print(int(num1) + int(num2))

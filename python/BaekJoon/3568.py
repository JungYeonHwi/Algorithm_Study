string = input()

arr = string.split(' ')

bt = arr[0]
del arr[0]

for s in arr:
    s = s.replace(",", '').replace(";", '')

    print(bt, end='')

    for i in range(len(s) - 1, 0, -1):
        if not s[i].isalpha():
            if s[i] == ']':
                print('[', end='')
            elif s[i] == '[':
                print(']', end='')
            else:
                print(s[i], end='')

    print(' ', end='')

    for i in range(len(s)):
        if s[i].isalpha():
            print(s[i], end='')

    print(';')

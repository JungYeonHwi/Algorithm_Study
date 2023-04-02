t = int(input())
for i in range(t):
    l = int(input())
    q = input()
    a = input()
    cnt = 0
    for j in range(l):
        if q[j] != a[j]:
            cnt += 1
    print('Case {}: {}'.format(i + 1, cnt))
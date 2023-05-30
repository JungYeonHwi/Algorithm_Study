from sys import stdin

n, m = map(int, stdin.readline().split())

n_arr = [0 for _ in range(10)]
m_arr = [0 for _ in range(10)]

n -= 1
point = 1
while n != 0:
    while n % 10 != 9:
        for i in str(n):
            n_arr[int(i)] += point
        n -= 1
    if n < 10:
        for i in range(n + 1):
            n_arr[i] += point
        n_arr[0] -= point
        break
    else:
        for i in range(10):
            n_arr[i] += (n // 10 + 1) * point
    n_arr[0] -= point
    point *= 10
    n //= 10


point = 1
while m != 0:
    while m % 10 != 9:
        for i in str(m):
            m_arr[int(i)] += point
        m -= 1
    if m < 10:
        for i in range(m + 1):
            m_arr[i] += point
        m_arr[0] -= point
        break
    else:
        for i in range(10):
            m_arr[i] += (m // 10 + 1) * point
    m_arr[0] -= point
    point *= 10
    m //= 10


ans = 0
for i in range(10):
    ans += (m_arr[i] - n_arr[i]) * i

print(ans)

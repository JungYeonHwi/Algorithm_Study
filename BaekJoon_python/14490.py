from math import gcd

n, m = map(int, input().split(':'))

x = gcd(n, m)
nx = n//x
mx = m//x

print(f'{nx}:{mx}')
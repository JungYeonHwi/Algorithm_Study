import sys
input = sys.stdin.readline
from math import log2


def make():
    MAX = int(4e9)
    m = int(MAX**0.5)+1
    sieve = [False,False] + [True] * m
    for i in range(2,m):
        if sieve[i]:
            for j in range(i+i,m,i):
                sieve[j] = False
    return [num for num in range(2,m) if sieve[num]]


def check(num):
    
    for prime in primeNums:
        if not num%prime and num//prime > 1:
            return False
        if prime > num:
            return True
    return True


primeNums = make()

for test_case in range(int(input())):
    n = int(input())
    MAX = int(4e9)
    if n==0 or n==1:
        print(2)
        continue
    for i in range(n,MAX+int(log2(MAX))):
        if check(i):
            print(i)
            break
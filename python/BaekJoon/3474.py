import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())  
    count = 0
    i = 5
    while i <= n:
        count += n // i  
        i *= 5
    print(count)
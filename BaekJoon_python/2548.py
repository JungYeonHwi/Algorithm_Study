import sys

n = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))

if (n % 2) == 0 : print(arr[n // 2 - 1])
else : print(arr[n // 2])
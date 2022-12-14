import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

value = [i for i in range(1, n+1)]

answer = list(set(value) - set(arr))
print(answer[0])
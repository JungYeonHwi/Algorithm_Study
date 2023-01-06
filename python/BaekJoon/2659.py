import sys

nums = list(map(int, sys.stdin.readline().split()))

def check(n):
    min = int(''.join(map(str, n)))
    for i in range(1,4):
        tmp = int(''.join(map(str, n[i:]+n[:i])))
        if min > tmp:
            min = tmp
    return min

n = check(nums)
cnt = 1
for i in range(1111, n):
    if '0' not in list(str(i)) and i == check(list(map(int, str(i)))) :
        cnt += 1
print(cnt)
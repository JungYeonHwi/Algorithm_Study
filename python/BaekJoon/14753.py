import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
lst2 = [lst[0]*lst[1], lst[-2]*lst[-1]]
lst3 = [lst[-3]*lst[-2]*lst[-1], lst[0]*lst[1]*lst[-1]]
print(max(max(lst2), max(lst3)))

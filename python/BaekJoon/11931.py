import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort(reverse=True)

for i in nums : 
    print(i)
n = int(input())
nums = list(map(int, input().split()))
nums.sort()
m = nums[-1]
q = 0

for i in reversed(range(1, m)) :
    tmp = list(filter(lambda x: x >= i, nums))
    if len(tmp) >= i :
        q = i
        break

print(q)
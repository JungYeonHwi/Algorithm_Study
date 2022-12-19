N = int(input())
nums = list(map(int, input().split()))

s = sum(nums)
answer = 0

for n in nums :
    s -= n
    answer += s * n

print(answer)
from itertools import combinations

nums = list(map(int, input().split()))
nums.sort()

combi = list(combinations(nums, 3))

for i in combi : 
    a, b, c = i[0], i[1], i[2]
    
    if a + b + c in nums and a + b in nums and a + c in nums and b + c in nums : 
        print(a, b, c)
        break

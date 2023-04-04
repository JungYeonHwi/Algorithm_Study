t = int(input())
for i in range(t):
    k = int(input())    
    d_nums = {}
    nums = list(map(int, input().split()))  
    n = int(input())    
    best = 360
    for i in range(n):
        a, b, c = map(int, input().split())
        if a in nums:
            if b == -1:
                pass
            else:
                d_nums[a] = b * 60 + c
                if best > d_nums[a]:
                    best = d_nums[a]
    cnt = 0 
    bNums = [] 
    for key in d_nums.keys() :
        if d_nums[key] == best :
            bNums.append(key)
        if d_nums[key] != 0 and d_nums[key] <= 360:
            cnt += 1
    print(*bNums, cnt)
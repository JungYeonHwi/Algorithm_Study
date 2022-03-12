N, K = map(int, input().split())

cnt = 0

nums = [1] * (N + 1)

for i in range(2, len(nums) + 1) : 
    for j in range(i, N+1, i) : 
        if nums[j] == 1 : 
            nums[j] = 0
            cnt += 1
            if cnt == K : 
                print(j)
                break
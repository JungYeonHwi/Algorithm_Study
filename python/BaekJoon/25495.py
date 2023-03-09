numsLen = int(input())
nums = (list(map(int, input().split())))

cp = nums[0]
cb = 2
ac = 1
for i in range(1, len(nums)) :
    if cb >= 100 :
        cp = 0
        cb = 0
        ac = 1
        
    if cp == nums[i] :
        ac += 1
        cb += 2 ** ac
    else :
        ac = 1
        cb += 2
    cp = nums[i]

if cb >= 100 :
    cp = 0
    cb = 0
    ac = 1
    
answer = cb

print(answer)
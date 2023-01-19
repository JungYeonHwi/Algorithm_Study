n, x = map(int, input().split()) 
arr = list(map(int, input().split()))

if max(arr) == 0:
    print("SAD")
else:
    
    prefix = [0]
    for i, a in enumerate(arr):
        prefix.append(prefix[i] + a)

    left = 0
    right = x
    result = 0
    count = 0

    while right <= n :
        if right - left == x :
            if result < prefix[right] - prefix[left] :
                result = prefix[right] - prefix[left]
                count = 1
            elif result == prefix[right] - prefix[left] :
                count += 1
                
            left += 1
            right += 1

    print(result)
    print(count)
N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 0, max(tree)

while start <= end : 
    mid = (start + end) // 2
    height = 0
    for i in tree : 
        if i > mid : height += i - mid
        
    if height >= M : start = mid + 1
    else : end = mid - 1
print(end)
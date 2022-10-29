from array import array


N, K = map(int, input().split())
arr = list(map(int, input().split(',')))

for _ in range(K) :
    t = [arr[i+1] - arr[i] for i in range(len(arr) - 1)]
    arr = t
    
print(*arr, sep=',')
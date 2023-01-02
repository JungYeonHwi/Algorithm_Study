import sys
input = sys.stdin.readline
 
K = int(input())
arr = list(map(int, input().split()))
tree = [[] for _ in range(K)]
 
 
def makeTree(arr, x):
    mid = (len(arr)//2)
    tree[x].append(arr[mid])
    if len(arr) == 1:
        return
    makeTree(arr[:mid], x+1)
    makeTree(arr[mid+1:], x+1)
 
 
makeTree(arr, 0)
for i in range(K):
    print(*tree[i])
n = int(input())
tree = list(map(int, input().split()))

tree.sort(reverse=True)

for i in range(len(tree)) : 
    tree[i] = tree[i] + 1 + i
    
print(max(tree) + 1)
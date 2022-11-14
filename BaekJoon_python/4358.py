import sys
input = sys.stdin.readline

trees = {}
n = 0

while 1 : 
    tree = input().rstrip()
    
    if not tree : break
    if tree in trees : trees[tree] += 1
    else : trees[tree] = 1
    
    n += 1
    
arr = list(trees.keys())
arr.sort()

for tree in arr : 
    print("%s %.4f" %(tree, trees[tree] / n * 100))
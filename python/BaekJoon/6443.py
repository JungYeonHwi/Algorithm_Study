import sys

def permutations(l, n, k):
    global visited
    global s
    global arr
    if l==k:
        sys.stdout.write("".join(arr)+"\n")
        return
    for a in visited:
        if visited[a]:
            visited[a] -=1
            arr[l] = a
            permutations(l+1, n, k)
            visited[a] +=1

n = int(sys.stdin.readline())

for _ in range(n) :
    s = list(sys.stdin.readline().strip())
    s.sort()
    visited = {}
    
    for a in range(len(s)) :
        if s[a] in visited :
            visited[s[a]] += 1
        else :
            visited[s[a]] = 1
    arr = [0] * len(s)
    permutations(0, len(s), len(s))
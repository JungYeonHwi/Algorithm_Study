from sys import stdin
input = stdin.readline

def DFS(depth, string) :
    global N, ret, charSet, cntMap

    if depth == N :
        ret += 1
        return

    for char in charSet :
        idx = ord(char) - ord('a')
        if cntMap[idx] == 0:
            continue

        if string and string[-1] == char:
            continue

        cntMap[idx] -= 1
        DFS(depth + 1, string + char)
        cntMap[idx] += 1


raw = input().strip()
cntMap = [0] * 26
N = len(raw)
ret = 0
charSet = set()

for char in raw:
    idx = ord(char) - ord('a')
    cntMap[idx] = cntMap[idx] + 1
    charSet.add(char)

DFS(0, '')
print(ret)
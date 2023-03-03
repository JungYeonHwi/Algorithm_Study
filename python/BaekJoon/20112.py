import sys

N = int(sys.stdin.readline())

rowWord = [['' for _ in range(N)] for _ in range(N)]
colWord = [['' for _ in range(N)] for _ in range(N)]
result = "YES"

for i in range(N) :
    word = input()
    for j, val in enumerate(word, start = 0) :
        rowWord[i][j] = val
        colWord[j][i] = rowWord[i][j]

if rowWord != colWord:
    result = "NO"

print(result)
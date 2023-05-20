import sys
input = sys.stdin.readline

villiage = []
all_people = 0

N = int(input())

for i in range(N):
    n_viliage, people = map(int, input().split())
    villiage.append([n_viliage, people])
    all_people += people

villiage.sort(key= lambda x: x[0])

count = 0
for i in range(N):
    count += villiage[i] [1]
    if count >= all_people/2:
        print (villiage[i][0])
        break

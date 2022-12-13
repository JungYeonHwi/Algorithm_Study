def ascending(trophies):
    n = trophies[0]
    count = 1
    for trophy in trophies:
        if trophy > n :
            count +=1
        n = max(n, trophy)
    return count

n = int(input())
trophies = []

for _ in range(n):
    trophies.append(int(input()))

print(ascending(trophies))
trophies.reverse()

print(ascending(trophies))

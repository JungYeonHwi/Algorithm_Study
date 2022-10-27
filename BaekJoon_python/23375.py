x, y = map(int, input().split())
radius = int(input())

print(x - radius, y + radius)
print(x + radius, y + radius)
print(x + radius, y - radius)
print(x - radius, y - radius)
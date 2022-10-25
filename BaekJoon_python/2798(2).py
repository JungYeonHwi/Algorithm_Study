from itertools import combinations
        
n, s = map(int, input().split())
cards = list(map(int, input().split()))
maxSum = 0

for c in combinations(cards, 3):
    if sum(c) <= s and sum(c) > maxSum:
        maxSum = sum(c)
print(maxSum)
ranks = [card[0] for card in input().split()]

print(ranks.count(max(ranks, key=ranks.count)))
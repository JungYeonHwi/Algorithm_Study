n, m = map(int, input().split())

def twoCount(n):
    two = 0
    while n != 0:
        n = n // 2
        two += n
    return two

def fiveCount(n):
    five = 0
    while n != 0:
        n = n // 5
        five += n
    return five

print(min(twoCount(n) - twoCount(n - m) - twoCount(m), fiveCount(n) - fiveCount(n - m) - fiveCount(m)))
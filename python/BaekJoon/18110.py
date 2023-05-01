import sys
from collections import deque
input = sys.stdin.readline
def round2(n):
	return int(n) + 1 if n - int(n) >= 0.5 else int(n)
difficulty = []
n = int(input())

for _ in range(n) :
	difficulty.append(int(input()))
if n == 0 : print(0)
else :
	remove = round2(n * 15 / 100)
	difficulty.sort()
	difficulty = deque(difficulty)
 
	for i in range(remove) :
		difficulty.popleft()
		difficulty.pop()
	print(round2(sum(difficulty) / (n - 2 * remove)))

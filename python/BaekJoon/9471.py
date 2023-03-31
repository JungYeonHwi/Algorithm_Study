import sys
input = sys.stdin.readline

def check(num):
  answer = 1
  mod1, mod2 = 1, 2
  while True:
    if mod1 % num == 1 and mod2 % num == 1:
      break

    answer += 1
    mod1, mod2 = mod2, (mod1 + mod2) % num
  return answer


P = int(input())

for _ in range(P):
  N, M = map(int, input().split())
  answer = check(M)
  print(f"{N} {answer}")

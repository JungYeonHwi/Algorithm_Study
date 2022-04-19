from itertools import permutations
n = input()
permu = (sorted(set(map(lambda x: ''.join(x), permutations(n, len(n))))))
print(0) if permu[-1] == n else print(permu[permu.index(n) + 1])
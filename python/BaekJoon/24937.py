N = int(input())
n = N % 10
scicomlove = "SciComLove"
answer = scicomlove[n:] + scicomlove[:n]

print(answer)
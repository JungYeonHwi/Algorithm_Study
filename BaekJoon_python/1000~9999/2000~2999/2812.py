n, k = map(int, input().split())
number = list(input())

stack = []
cnt = k

for num in number:
    while stack and cnt > 0 and stack[-1] < num:
        del stack[-1]
        cnt -= 1
    stack.append(num)

print(''.join(stack[:n-k]))
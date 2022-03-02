import sys

def spush(x) :
    stack.append(x)

def spop() :
    if(not stack):
        return -1
    else:
        return stack.pop()

def ssize() :
    return len(stack)

def sempty() :
    return 0 if stack else 1

def stop() :
    return stack[-1] if stack else -1

N = int(sys.stdin.readline().rstrip())
stack = []

for _ in range(N):
    input_split = sys.stdin.readline().rstrip().split()

    order = input_split[0]

    if order == "push" :
        spush(input_split[1])
    elif order == "pop" :
        print(spop())
    elif order == "size" :
        print(ssize())
    elif order == "empty" :
        print(sempty())
    elif order == "top" :
        print(stop())
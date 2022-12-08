n = int(input())

for _ in range(n) : 
    print("@@@" * n, end="")
    print(" " * n, end="")
    print("@" * n)
for _ in range(n * 3) :
    print("@" * n, end="")
    print(" " * n, end="")
    print("@" * n, end="")
    print(" " * n, end="")
    print("@" * n)
for _ in range(n) : 
    print("@" * n, end="")
    print(" " * n, end="")
    print("@@@" * n)
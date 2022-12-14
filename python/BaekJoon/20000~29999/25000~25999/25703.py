N = int(input())
print("int a;")
    
for i in range(1, N + 1):
    s = f"ptr{i-1 if i-1 > 1 else ''};" if i > 1 else "a;"
    print(f"int {'*' * i}ptr{i if i > 1 else ''} = &{s}")
            
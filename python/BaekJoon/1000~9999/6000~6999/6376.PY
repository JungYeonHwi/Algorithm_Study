def f(num) :
    if num == 0 or num == 1 :
        return 1
    return f(num - 1) * num


print('n e')
print('- -----------')

e = 0

for i in range(10):
    n = i
    e += f(i) ** (-1)
    
    if n < 2 :
        print(f'{n} {e:.0f}')
    elif n == 2 :
        print(f'{n} {e:.1f}')
    else :
        print(f'{n} {e:.9f}')
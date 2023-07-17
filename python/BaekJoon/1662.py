s = input()
stack = []
length = 0
temp = ''
for c in s:
    if c.isdigit():
        length += 1
        temp = c
    elif c == '(':
        # temp는 곱해야 하는 수, length-1 은 ( 를 만나기 전까지의 전체 길이
        stack.append((temp, length - 1))

        length = 0 # 초기화. ( )가 또 나올 수도 있기 때문에
    else:
        # ) 일때, multi 곱해야 되는 수, preL '('부터 multi 전까지의 길이, length는 ( ) 사이에 있는 문자 길이 
        multi, preL = stack.pop()

        length = (int(multi) * length) + preL


print(length)

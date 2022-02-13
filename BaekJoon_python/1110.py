input_num = int(input())

num = input_num
count = 0
while True:
    sum_num = (num // 10) + (num % 10)
    new_num = ((num % 10) * 10) + (sum_num % 10)
    count = count + 1
    if new_num == input_num :
        break
    num = new_num
print(count)
n = int(input())

value = input()

s = value.count("security")
b = value.count("bigdata")

if s > b : print("security!")
elif s < b : print("bigdata?")
else : print("bigdata? security!")
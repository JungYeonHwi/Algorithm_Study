keypad = {"1" : "", "2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}

new = input().split()

value = {}

for i in range(len(new)) : 
    value[str(i+1)] = keypad[new[i]]
    
ip = input()

result = ""

key = []

for i in range(len(ip)) : 
    for k, v in value.items() : 
        if ip[i] in v : 
            if len(key) > 0 and (key[-1] == k) : 
                result = result + "#" + (v.find(ip[i]) + 1) * k
            else : 
                result += (v.find(ip[i]) + 1) * k

            key.append(k)
            
print(result)
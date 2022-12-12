from sys import stdin

word = stdin.readline().rstrip()

length = len(word)

lines = [".", ".", "#", ".", "."]

for idx in range(length) : 
    if (idx + 1) % 3 != 0 : 
        lines[0] += ".#."
        lines[1] += "#.#"
        lines[2] += f'.{word[idx]}.'
        lines[3] += "#.#"
        lines[4] += ".#."
    else : 
        lines[0] += "..*.."
        lines[1] += ".*.*."
        lines[2] += f'*.{word[idx]}.*'
        lines[3] += ".*.*."
        lines[4] += "..*.."
        
    if (idx + 1) % 3 == 1 : 
        lines[0] += "."
        lines[1] += "."
        lines[2] += "#"
        lines[3] += "."
        lines[4] += "."

if length % 3 == 2 : 
    lines[0] += "."
    lines[1] += "."
    lines[2] += "#"
    lines[3] += "."
    lines[4] += "."
    
for i in lines : 
    print(i)
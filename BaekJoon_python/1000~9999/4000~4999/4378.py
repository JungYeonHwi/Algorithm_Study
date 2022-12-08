def fuc(value):
    keyboard = {
        "1": "`", "2": "1", "3": "2", "4": "3", "5": "4", "6": "5", "7": "6", "8": "7", "9": "8", "0": "9", "-": "0", "=": "-",
        "w": "q", "e": "w", "r": "e", "t": "r", "y": "t", "u": "y", "i": "u", "o": "i", "p": "o", "[": "p", "]": "[", "\\": "]",
        "s": "a", "d": "s", "f": "d", "g": "f", "h": "g", "j": "h", "k": "j", "l": "k", ";": "l", "'": ";",
        "x": "z", "c": "x", "v": "c", "b": "v", "n": "b", "m": "n", ",": "m", ".":",", "/": ".", " ": " "
    }
            
    return keyboard[value.lower()].upper()

while 1 :
    try :
        for t in input() :
            print(fuc(t), end='')
        print()
    except : break
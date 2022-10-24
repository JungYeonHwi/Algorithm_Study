def solution(numbers):
    answer = 0
    value = ''
    words = {
        "zero" : "0",
        "one" : "1",
        "two" : "2",
        "three" : "3",
        "four" : "4",
        "five" : "5",
        "six" : "6",
        "seven" : "7",
        "eight" : "8",
        "nine" : "9"
    }
    tmpS = ""
    for i in numbers:
        tmpS += i
        if tmpS in words :
            value += words[tmpS]
            tmpS = ""
    
    answer = int(value)
    
    return answer
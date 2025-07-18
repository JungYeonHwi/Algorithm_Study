function solution(keymap, targets) {
    var answer = [];
    
    let arr = [];
    for (let i = 0; i < 26; i++) {
        arr.push(-1);
    }
    
    for (let i = 0; i < keymap.length; i++) {
        for (let j = 0; j < keymap[i].length; j++) {
            let item = keymap[i][j].charCodeAt() - 65;
            if (arr[item] === -1) arr[item] = j + 1;
            else {
                let min = Math.min(arr[item], j + 1);
                arr[item] = min;
            }
        }
    }
    
    for (let i = 0; i < targets.length; i++) {
        let temp = 0;
        for (let j = 0; j < targets[i].length; j++) {
            let item = targets[i][j].charCodeAt() - 65;
            if (arr[item] === -1) {
                temp = -1;
                break;
            } else {
                temp += arr[item];
            }
        }
        
        answer.push(temp)
        
    }
    
    return answer;
}
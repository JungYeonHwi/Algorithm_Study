function solution(s) {
  var answer = "";

  let wordIndex = 0;

  for (let i = 0; i < s.length; i++) {
    const char = s[i];

    if (char === " ") {
      answer += " ";
      wordIndex = 0;
    } else {
      if (wordIndex % 2 === 0) {
        answer += char.toUpperCase();
      } else {
        answer += char.toLowerCase();
      }
      wordIndex++;
    }
  }

  return answer;
}

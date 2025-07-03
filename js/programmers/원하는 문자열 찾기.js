function solution(myString, pat) {
  var answer = myString.toLowerCase().includes(pat.toLowerCase()) ? 1 : 0;
  return answer;
}

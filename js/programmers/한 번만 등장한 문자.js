function solution(s) {
  var answer = "";

  let arr = Array.from({ length: 26 }, (_, i) => 0);

  for (i = 0; i < s.length; i++) {
    arr[Number(s[i].charCodeAt() - 97)] += 1;
  }

  let res = [];

  for (index = 0; index < arr.length; index++) {
    if (arr[index] === 1) {
      res.push(String.fromCharCode(97 + index));
    }
  }

  return res.join("");
}

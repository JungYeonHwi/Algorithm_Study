function solution(arr, queries) {
  var answer = [];

  for (let item = 0; item < queries.length; item++) {
    let [s, e, k] = queries[item];
    let temp = arr
      .filter((v, i) => i >= s && i <= e && v > k)
      .sort((a, b) => a - b)[0];
    answer.push(temp ? temp : -1);
  }

  return answer;
}

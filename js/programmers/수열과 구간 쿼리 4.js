function solution(arr, queries) {
  var answer = arr;

  for (let item = 0; item < queries.length; item++) {
    let [s, e, k] = queries[item];

    for (let i = s; i <= e; i++) {
      if (i % k === 0) answer[i] += 1;
    }
  }

  return answer;
}

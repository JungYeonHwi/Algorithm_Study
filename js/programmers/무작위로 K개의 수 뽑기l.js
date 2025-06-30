function solution(arr, k) {
  const set = new Set(arr);

  const result = [...set].slice(0, k);

  while (result.length !== k) {
    result.push(-1);
  }

  return result;
}

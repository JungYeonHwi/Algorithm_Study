function solution(arr1, arr2) {
  var answer = 0;

  if (arr1.length === arr2.length) {
    let s1 = arr1.reduce((a, b) => a + b);
    let s2 = arr2.reduce((a, b) => a + b);

    if (s1 === s2) return 0;
    else if (s1 > s2) return 1;
    else return -1;
  } else {
    if (arr1.length > arr2.length) return 1;
    else return -1;
  }

  return answer;
}

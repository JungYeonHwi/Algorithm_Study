function solution(n, arr1, arr2) {
  var answer = [];

  let val = 9;

  for (let i = 0; i < n; i++) {
    let a = arr1[i].toString(2).padStart(n, "0");
    let b = arr2[i].toString(2).padStart(n, "0");
    let temp = "";

    for (let k = 0; k < n; k++) {
      if (a[k] === "1" || b[k] === "1") temp += "#";
      else temp += " ";
    }

    answer.push(temp);
  }

  return answer;
}

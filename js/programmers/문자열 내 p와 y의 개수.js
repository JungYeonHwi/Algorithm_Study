function solution(s) {
  var answer = true;

  let p = [...s].filter((item) => item === "p" || item === "P").length;
  let y = [...s].filter((item) => item === "y" || item === "Y").length;

  return (answer = p === y ? true : false);
}

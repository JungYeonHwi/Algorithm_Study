function solution(arr) {
  const arrLength = arr.length;
  let exponent = 0;

  while (Math.pow(2, exponent) < arrLength) exponent++;

  let fillNum = Math.pow(2, exponent) - arrLength;

  const zArr = Array(fillNum).fill(0);

  return arr.concat(zArr);
}

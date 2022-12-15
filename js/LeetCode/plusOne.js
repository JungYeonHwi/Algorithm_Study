/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function (digits) {
  let number = BigInt(digits.join(""));
  let numOne = number + BigInt(1);

  const arr = Array.from(String(numOne));
  return arr;
};

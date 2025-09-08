/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function (a, b) {
  let aa = `0b${a}`;
  let bb = `0b${b}`;
  let n = BigInt(aa) + BigInt(bb);
  return n.toString(2);
};

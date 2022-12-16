/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let left = 0;
  let right = 1;
  let m = 0;

  while (right < prices.length) {
    current = prices[right] - prices[left];

    if (prices[left] < prices[right]) {
      m = Math.max(current, m);
    } else {
      left = right;
    }

    right += 1;
  }

  return m;
};

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let answer = 0;
    let min = prices[0];

    for (let i = 1; i < prices.length; i++) {
        min = Math.min(min, prices[i-1]);
        answer = Math.max(prices[i] - min, answer)
    }

    return answer;
};
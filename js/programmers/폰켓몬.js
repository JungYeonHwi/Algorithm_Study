function solution(nums) {
  var answer = 0;
  let count = parseInt(nums.length / 2);
  let s = [...new Set(nums)];

  if (count >= s.length) answer = s.length;
  else answer = count;

  return answer;
}

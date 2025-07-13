function solution(nums) {
  var answer = 0;

  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      for (let k = j + 1; k < nums.length; k++) {
        let val = nums[i] + nums[j] + nums[k];
        let count = 0;

        for (let index = 1; index <= val; index++) {
          if (val % index === 0) count += 1;
        }

        if (count === 2) answer += 1;
      }
    }
  }

  return answer;
}

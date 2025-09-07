/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function (haystack, needle) {
  for (let i = 0; i < haystack.length; i++) {
    let count = 0;

    for (let j = i; j < i + needle.length; j++) {
      if (haystack[j] === needle[count]) {
        count++;
      }
    }

    if (count === needle.length) {
      return i;
    }
  }

  return -1;
};

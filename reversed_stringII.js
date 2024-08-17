// 541. Reverse String II
// Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

// If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

 

// Example 1:

// Input: s = "abcdefg", k = 2
// Output: "bacdfeg"
// Example 2:

// Input: s = "abcd", k = 2
// Output: "bacd"



/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var reverseStr = function(s, k) {
    
    let befStr = s.slice(0,k);

    let reStr = ''
    for(let i=befStr.length-1;i>=0;i--){
        reStr += befStr[i]
    }

    return reStr+s.slice(k);

//     let result = '';
  
//   for (let i = 0; i < s.length; i+=2*k) {
//     let part1 = s.slice(i, i + k).split('').reverse().join('');

//     console.log("part1",part1);
//     let part2 = s.slice(i + k, i + 2 * k);

//     console.log("part2",part2);
//     result += part1 + part2;
//   }
//   return result;
};
console.log(reverseStr('abcdefg',2))
console.log(reverseStr('abcd',2))

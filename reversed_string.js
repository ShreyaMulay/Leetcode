
// 344. Reverse String

// Write a function that reverses a string. The input string is given as an array of characters s.

// You must do this by modifying the input array in-place with O(1) extra memory.

 

// Example 1:

// Input: s = ["h","e","l","l","o"]
// Output: ["o","l","l","e","h"]
// Example 2:

// Input: s = ["H","a","n","n","a","h"]
// Output: ["h","a","n","n","a","H"]
 
var reverseString = function(s) {

    //1st sol
    // let newArray = []
    // for(let i=s.length-1;i>=0;i--)
    // {
    //     newArray.push(s[i]);
    // }
    // return newArray;
    
    //2nd sol
    // let newStr = s.join(",");
    // let reversedStr="";
    //  for (let i = newStr.length - 1; i >= 0; i--) {
    //     reversedStr += newStr[i];
    // }

    // let revArray = reversedStr.split(',');
    // console.log("revArray",(revArray)) ;
    // return revArray;


    let n = s.length;
    for (let i = 0; i < n / 2; i++) {
        let temp = s[i];
        s[i] = s[n - 1 - i];
        s[n - 1 - i] = temp;
    }
    return s;

};

console.log(reverseString(["h","e","l","l","o"]))
console.log(reverseString(["H","a","n","n","a","h"]))

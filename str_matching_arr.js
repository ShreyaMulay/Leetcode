// 1408. String Matching in an Array

// Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.

// A substring is a contiguous sequence of characters within a string

 

// Example 1:

// Input: words = ["mass","as","hero","superhero"]
// Output: ["as","hero"]
// Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
// ["hero","as"] is also a valid answer.
// Example 2:

// Input: words = ["leetcode","et","code"]
// Output: ["et","code"]
// Explanation: "et", "code" are substring of "leetcode".
// Example 3:

// Input: words = ["blue","green","bu"]
// Output: []
// Explanation: No string of words is substring of another string.


var stringMatching = function(words) {
    console.log("words : ",words)
    let res = []
    for(let i=0;i<words.length;i++)
    {
        for(let j=0;j<words.length;j++)
        {
            if(i !=j && words[i].includes(words[j]))
            {
                if(!res.includes(words[j]))
                    res.push(words[j])
            }
        }
    }
    return res;
};

// console.log(stringMatching(["mass","as","hero","superhero"]))
// console.log(stringMatching(["leetcode","et","code"]))
// console.log(stringMatching(["blue","green","bu"]))
console.log(stringMatching(["leetcoder","leetcode","od","hamlet","am"]))

let a={x:'a',y:null,z:'c'}
let b='y'
for(let key in a){
    if((a[key] != null || a[key] != undefined ) && key == b){
        console.log("true");
    }
}